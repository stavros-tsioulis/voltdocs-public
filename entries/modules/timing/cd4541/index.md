## Overview

The **CD4541** (standardized as the **CD4541B** / `HEF4541B` / `MC14541B`) is a versatile CMOS programmable timer and frequency divider integrated circuit in a 14-pin DIP or SOIC package. Designed as a high-precision digital alternative to analog RC timers (such as the classic NE555), the CD4541 solves the notorious problem of timing drift and unreliability in long-duration delay circuits.

In an analog 555 timer, generating time delays of several minutes, hours, or days requires massive electrolytic timing capacitors ($100\ \mu\text{F} - 1000\ \mu\text{F}$) paired with multi-megohm timing resistors. At these high resistance values, capacitor internal leakage current easily equals or exceeds charging current, causing timing inaccuracy, temperature drift, or outright failure to trigger.

The CD4541 solves this by combining:
1. An on-chip high-frequency, low-leakage **RC oscillator** that uses small, stable, non-electrolytic ceramic or film capacitors ($100\text{ pF} - 100\text{ nF}$).
2. A **16-stage binary ripple counter** that divides the oscillator clock by selectable digital powers of two ($2^8 = 256$, $2^{10} = 1024$, $2^{13} = 8192$, or $2^{16} = 65,536$).
3. Built-in logic for **single-transition delay (one-shot)** or **continuous frequency division**, selectable output polarity (active-High or active-Low), power-on auto-reset, and external master reset.

With a $2^{16}$ division ratio, an easily calibrated $1.0\text{ Hz}$ oscillator pulse produces an exact $18.2$-hour timeout without requiring a microcontroller or battery-draining circuitry.

## Quick reference

| Parameter | Value | Notes |
|---|---|---|
| **Supply Voltage Range ($V_{DD}$)** | $3.0\text{ V}$ to $18.0\text{ V}$ DC | Standard 4000B CMOS voltage window |
| **Logic Family** | CD4000B High-Voltage CMOS | High noise immunity ($45\%$ of $V_{DD}$) |
| **Counter Depth** | 16 binary stages | Divisions up to $65,536$ |
| **Programmable Division Ratios** | $256$, $1024$, $8192$, $65536$ | Selected via digital pins `A` and `B` |
| **Operating Modes** | Single-cycle timer or free-running clock | Selected via `MODE` pin |
| **Output Polarity** | Non-inverting or inverting | Selected via `Q/Q_BAR` pin |
| **Quiescent Power Drain** | $< 0.01\ \mu\text{A}$ typical at $5\text{ V}$ | Negligible standby current |
| **Package** | 14-pin DIP / SOIC-14 | Breadboard and prototyping friendly |

## Terminals

```
               +---+--+---+
        RTC --| 1   14 |-- VDD
        CTC --| 2   13 |-- B
         RS --| 3   12 |-- A
         NC --| 4   11 |-- NC
 AUTO RESET --| 5   10 |-- MODE
MASTER RESET -| 6    9 |-- Q/Q_BAR
        VSS --| 7    8 |-- OUT (Q)
               +----------+
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `RTC` | Oscillator | Resistor timing connection for internal RC oscillator. |
| 2 | `CTC` | Oscillator | Capacitor timing connection for internal RC oscillator. |
| 3 | `RS` | Oscillator / Clock | Bias resistor connection, or external clock signal input. |
| 4, 11| `NC` | — | No internal connection. Leave floating. |
| 5 | `AUTO RESET` | Digital Input | Automatic power-on reset. Low ($0\text{ V}$) = auto-reset enabled. High ($V_{DD}$) = disabled. |
| 6 | `MASTER RESET`| Digital Input | External master reset input. High = resets counter to 0; Low = normal counting. |
| 7 | `VSS` | Power | Circuit ground reference ($0\text{ V}$). |
| 8 | `OUT` (`Q`) | Digital Output | Timer output terminal. Drives logic, transistors, or relays. |
| 9 | `Q/Q_BAR` | Digital Input | Output polarity select. Low = output initial Low; High = output initial High. |
| 10 | `MODE` | Digital Input | Mode select. Low = Single-cycle timer (stops after timeout). High = Free-running frequency divider. |
| 12 | `A` | Digital Input | Binary division select input A (least significant bit). |
| 13 | `B` | Digital Input | Binary division select input B (most significant bit). |
| 14 | `VDD` | Power | Positive DC supply rail ($+3.0\text{ V}$ to $+18.0\text{ V}$ DC). |

## The technical core

### Division ratio programming table

The division ratio ($N$) of the 16-stage binary counter is configured by pins 12 (`A`) and 13 (`B`):

| Pin 13 (`B`) | Pin 12 (`A`) | Counter Division Ratio ($N$) | Time Delay ($t_{delay}$) |
|---|---|---|---|
| Low ($0\text{ V}$) | Low ($0\text{ V}$) | $2^{13} = \mathbf{8,192}$ | $8,192 \times T_{OSC}$ |
| Low ($0\text{ V}$) | High ($V_{DD}$) | $2^{10} = \mathbf{1,024}$ | $1,024 \times T_{OSC}$ |
| High ($V_{DD}$) | Low ($0\text{ V}$) | $2^8 = \mathbf{256}$ | $256 \times T_{OSC}$ |
| High ($V_{DD}$) | High ($V_{DD}$) | $2^{16} = \mathbf{65,536}$ | $65,536 \times T_{OSC}$ |

### RC oscillator frequency calculation

When using the internal RC oscillator network across pins 1 (`RTC`), 2 (`CTC`), and 3 (`RS`):

$$ f_{OSC} = \frac{1}{2.3 \times R_{TC} \times C_{TC}} $$

Where:
- $R_{TC}$ is connected between Pin 1 and Pin 2.
- $C_{TC}$ is connected between Pin 2 and Pin 7 (`VSS`).
- $R_S$ is connected between Pin 1 and Pin 3 ($R_S \approx 2 \times R_{TC}$ to maintain symmetry and temperature stability).

**Total Delay Time ($t_{delay}$):**

$$ t_{delay} = \frac{N}{f_{OSC}} = 2.3 \times N \times R_{TC} \times C_{TC} $$

**Worked Example for a 1-Hour Timer:**
Target timeout $t_{delay} = 3600\text{ s}$.
Select division ratio $N = 65,536$ (`A` = High, `B` = High).
Required oscillator frequency:
$$ f_{OSC} = \frac{N}{t_{delay}} = \frac{65,536}{3600\text{ s}} \approx 18.2\text{ Hz} $$
Select a stable $0.1\ \mu\text{F}$ film capacitor for $C_{TC}$:
$$ R_{TC} = \frac{1}{2.3 \times 18.2\text{ Hz} \times 100\text{ nF}} \approx 239\text{ k}\Omega \quad (\text{Use } 240\text{ k}\Omega) $$
$$ R_S = 2 \times R_{TC} \approx 470\text{ k}\Omega $$
A standard $240\text{ k}\Omega$ resistor and $100\text{ nF}$ capacitor provide a rock-solid 1-hour timeout without relying on electrolytic caps.

### Electrical specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage Range | $V_{DD}$ | 3.0 | 5.0 / 12.0 | 18.0 | V | Operating range |
| Input High Voltage | $V_{IH}$ | 3.5 | — | — | V | $V_{DD} = 5.0\text{ V}$ |
| Input Low Voltage | $V_{IL}$ | — | — | 1.5 | V | $V_{DD} = 5.0\text{ V}$ |
| Output Drive Current (Sink) | $I_{OL}$ | 1.0 | 2.5 | — | mA | $V_{DD} = 5\text{ V}$, $V_{OUT} = 0.4\text{ V}$ |
| Output Drive Current (Source) | $I_{OH}$ | -1.0 | -2.0 | — | mA | $V_{DD} = 5\text{ V}$, $V_{OUT} = 4.6\text{ V}$ |
| Max Oscillator Frequency | $f_{OSC\_MAX}$| — | 100 | — | kHz | $V_{DD} = 5.0\text{ V}$ |
| Master Reset Pulse Width | $t_{W\_MR}$ | 150 | — | — | ns | $V_{DD} = 5.0\text{ V}$ |

## Usage

### Long-duration interval timer circuit

```
       +5V to +15V DC
  VDD o------+-----------------------------------+
             |                                   |
            [ ] R_S (470k)                      [ ] R_pullup (10k)
             |                                   |
             +-------------+ (Pin 3, RS)         |
             |             |                     |
            [ ] R_TC (240k)|                     |
             |             |                     |
             +-------------+ (Pin 1, RTC)        |
             |             |                     |
             |             | 14   13  12  10  9  |
             |          +--+---+---+---+---+--+--+
             |          | VDD  B   A  MODE Q/QBAR|
             |          |      CD4541B           |
             |          | RTC CTC RS   AR  MR OUT|
             |          +--+---+---+---+---+--+--+
             |             1   2   3   5   6  8  |
             |                 |       |   |  |  +----> OUT (Drives NPN/MOSFET)
             +-----------------+       |   |  |
                               |       |   |  |
                              ===      |   |  |
                         C_TC ---      |   |  |
                        (100nF)|       |   |  |
  GND o------------------------+-------+---+--+
```

To configure:
- **Pin 5 (`AUTO RESET`):** Tie to Ground (`VSS`) to enable automatic power-on reset when power is switched on.
- **Pin 6 (`MASTER RESET`):** Tie to Ground for normal counting; pulse High to manually restart the timer.
- **Pin 9 (`Q/Q_BAR`):** Tie to Ground so output starts Low and transitions High upon timeout.
- **Pin 10 (`MODE`):** Tie to Ground for single-transition timer (shuts off counter and holds output state after timeout).

## Common mistakes

- **Leaving unused programming pins floating:** As a pure CMOS integrated circuit, leaving pins `A`, `B`, `MODE`, or `Q/Q_BAR` floating will result in capacitive pickup, unpredictable timeout durations, and erratic output behavior. Tie every control pin solidly to $V_{DD}$ or $V_{SS}$.
- **Driving relays directly from Pin 8:** The CD4541 output can only source or sink $\approx 2\text{ mA} - 5\text{ mA}$ at 12V. Attempting to directly drive a relay coil will overload the CMOS output driver. Use an external NPN transistor (e.g. 2N2222) or N-channel MOSFET (e.g. 2N7000).
- **Omitting $R_S$ in the oscillator:** Leaving Pin 3 disconnected degrades oscillator frequency stability and symmetry. Always include $R_S \approx 2 \times R_{TC}$.

## Notes

- **CD4541 vs NE555:** While the 555 timer is ideal for microsecond-to-second timing and high current output (200mA), the CD4541 is vastly superior for delays beyond 5 minutes, drawing 1000x less quiescent current and requiring only tiny film or ceramic timing capacitors.
