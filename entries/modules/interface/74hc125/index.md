## Overview

The **74HC125** (such as the `SN74HC125N` or `74HC125D`) is a high-speed silicon-gate CMOS logic device containing four independent non-inverting buffer / line drivers with 3-state outputs in a 14-pin DIP or SOIC package. Each of the four buffer gates is controlled by its own dedicated active-LOW output enable pin ($\overline{\text{OE}}$ or `nOE`).

When an enable pin is driven Low, the corresponding gate acts as a transparent non-inverting buffer ($Y = A$). When the enable pin is driven High, the output is forced into a high-impedance (Hi-Z) state, effectively disconnecting the gate from the output line. This capability makes the 74HC125 an essential component for driving shared bus architectures, multiplexing lines, and preventing bus contention.

In maker electronics and embedded development, the 74HC125 is famous as the level-shifting and bus-isolation IC populated on Arduino SD card shields and modules:
- SD cards operate strictly at $3.3\text{ V}$ logic levels and cannot tolerate $5\text{ V}$ signaling.
- Furthermore, many micro-SD cards fail to properly release the shared SPI `MISO` line when deselected, causing bus contention with other SPI peripherals.
- The 74HC125, powered from $+3.3\text{ V}$ with its active-LOW enable tied to the chip select line ($\overline{\text{CS}}$), provides clean $5\text{V} \to 3.3\text{V}$ level shifting while ensuring complete electrical disconnection of the shared `MISO` line whenever the card is idle.

## Quick reference

| Parameter | Value | Notes |
|---|---|---|
| **Logic Family** | High-Speed CMOS (74HC) | 74HCT version available for TTL thresholds |
| **Supply Voltage Range ($V_{CC}$)** | $2.0\text{ V}$ to $6.0\text{ V}$ DC | $4.5\text{ V}$ to $5.5\text{ V}$ for 74HCT |
| **Number of Channels** | 4 independent buffer gates | Individual active-LOW enables |
| **Propagation Delay ($t_{pd}$)** | $11\text{ ns}$ typical at $4.5\text{ V}$ | High-speed data throughput ($> 40\text{ MHz}$) |
| **Output Drive Current ($I_{OUT}$)** | $\pm 6.0\text{ mA}$ at $4.5\text{ V}$ | Drives up to 15 LSTTL loads |
| **3-State Leakage Current ($I_{OZ}$)** | $\pm 0.5\ \mu\text{A}$ maximum | Negligible load when in Hi-Z state |
| **Input Capacitance** | $3\text{ pF}$ typical | Minimal bus loading |
| **Package** | 14-pin DIP / SOIC-14 / TSSOP-14 | Standard logic pinout |

## Terminals

```
            +---+--+---+
     1nOE -| 1   14 |-- VCC
       1A -| 2   13 |-- 4nOE
       1Y -| 3   12 |-- 4A
     2nOE -| 4   11 |-- 4Y
       2A -| 5   10 |-- 3nOE
       2Y -| 6    9 |-- 3A
      GND -| 7    8 |-- 3Y
            +----------+
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `1nOE` ($\overline{1\text{OE}}$) | Digital Input | Gate 1 Active-LOW Output Enable. Low = Enable, High = Hi-Z. |
| 2 | `1A` | Digital Input | Gate 1 Data Input. |
| 3 | `1Y` | Digital Output | Gate 1 3-State Output. |
| 4 | `2nOE` ($\overline{2\text{OE}}$) | Digital Input | Gate 2 Active-LOW Output Enable. |
| 5 | `2A` | Digital Input | Gate 2 Data Input. |
| 6 | `2Y` | Digital Output | Gate 2 3-State Output. |
| 7 | `GND` | Ground | Circuit ground reference ($0\text{ V}$). |
| 8 | `3Y` | Digital Output | Gate 3 3-State Output. |
| 9 | `3A` | Digital Input | Gate 3 Data Input. |
| 10 | `3nOE` ($\overline{3\text{OE}}$) | Digital Input | Gate 3 Active-LOW Output Enable. |
| 11 | `4Y` | Digital Output | Gate 4 3-State Output. |
| 12 | `4A` | Digital Input | Gate 4 Data Input. |
| 13 | `4nOE` ($\overline{4\text{OE}}$) | Digital Input | Gate 4 Active-LOW Output Enable. |
| 14 | `VCC` | Power | Positive DC supply rail ($+2.0\text{ V}$ to $+6.0\text{ V}$ DC). |

## The technical core

### Function truth table (each gate)

| Output Enable ($\overline{\text{OE}}$) | Data Input ($A$) | Output ($Y$) | State |
|---|---|---|---|
| **Low ($L$)** | Low ($L$) | **Low ($L$)** | Active driving (Logic 0) |
| **Low ($L$)** | High ($H$) | **High ($H$)** | Active driving (Logic 1) |
| **High ($H$)** | $X$ (Don't Care) | **High-Z ($Z$)** | Disconnected (Floating) |

### Electrical specifications (74HC125 at $25^\circ\text{C}$)

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.0 | 5.0 | 6.0 | V | Operating range |
| High-Level Input Voltage | $V_{IH}$ | 3.15 | — | — | V | $V_{CC} = 4.5\text{ V}$ |
| Low-Level Input Voltage | $V_{IL}$ | — | — | 1.35 | V | $V_{CC} = 4.5\text{ V}$ |
| High-Level Output Voltage | $V_{OH}$ | 4.4 | 4.49 | — | V | $V_{CC} = 4.5\text{ V}$, $I_{OH} = -20\ \mu\text{A}$ |
| High-Level Output Voltage | $V_{OH}$ | 3.84 | 4.2 | — | V | $V_{CC} = 4.5\text{ V}$, $I_{OH} = -6.0\text{ mA}$ |
| Low-Level Output Voltage | $V_{OL}$ | — | 0.01 | 0.1 | V | $V_{CC} = 4.5\text{ V}$, $I_{OL} = 20\ \mu\text{A}$ |
| Low-Level Output Voltage | $V_{OL}$ | — | 0.17 | 0.33 | V | $V_{CC} = 4.5\text{ V}$, $I_{OL} = 6.0\text{ mA}$ |
| Propagation Delay ($A \to Y$) | $t_{pd}$ | — | 11 | 18 | ns | $V_{CC} = 4.5\text{ V}$, $C_L = 50\text{ pF}$ |
| 3-State Output Enable Time | $t_{en}$ | — | 14 | 25 | ns | $V_{CC} = 4.5\text{ V}$, $C_L = 50\text{ pF}$ |
| 3-State Output Disable Time | $t_{dis}$ | — | 14 | 25 | ns | $V_{CC} = 4.5\text{ V}$, $C_L = 50\text{ pF}$ |
| 3-State Leakage Current | $I_{OZ}$ | — | — | $\pm 0.5$ | µA | $V_{OUT} = V_{CC}$ or $GND$ |

## Usage

### SD card SPI bus level shifter and isolation circuit

When connecting a $3.3\text{ V}$ SD card socket to a $5\text{ V}$ Arduino Uno:

```
        Arduino (5V)                                      SD Card Socket (3.3V)
  +----------------------+                           +-----------------------------+
  |                      |     74HC125 (VCC = 3.3V)  |                             |
  |  MOSI (Pin 11, 5V) --+-----[ 1A  ->  1Y ]--------+--> MOSI (3.3V)              |
  |                      |      (1nOE = GND)         |                             |
  |   SCK (Pin 13, 5V) --+-----[ 2A  ->  2Y ]--------+--> SCK (3.3V)               |
  |                      |      (2nOE = GND)         |                             |
  |    CS (Pin 10, 5V) --+--+--[ 3A  ->  3Y ]--------+--> CS (3.3V)                |
  |                      |  |   (3nOE = GND)         |                             |
  |                      |  |                        |                             |
  |  MISO (Pin 12, 5V) <-+--|--[ 4Y  <-  4A ]<-------+--- MISO (3.3V)              |
  |                      |  +--[ 4nOE       ]        |                             |
  +----------------------+                           +-----------------------------+
```

#### How it works:
1. Powered from $+3.3\text{ V}$, gates 1, 2, and 3 clamp the $5\text{ V}$ inputs safely down to clean $3.3\text{ V}$ signals for the SD card.
2. Gate 4 buffers the SD card's $3.3\text{ V}$ `MISO` signal back to the Arduino. Its enable (`4nOE`) is driven by the card's Chip Select line (`CS`).
3. When `CS` is High (card deselected), `4nOE` is High, putting gate 4 in Hi-Z state and freeing the `MISO` bus line completely for other sensors or SPI devices.

## Common mistakes

- **Leaving unused inputs floating:** CMOS inputs must never float. Leaving unused gate inputs (e.g. `4A`, `4nOE`) un-connected causes parasitic oscillation, elevating quiescent current by hundreds of microamps. Tie unused inputs to $V_{CC}$ or $GND$.
- **Confusing 74HC125 with 74HC126:** The 74HC125 has **active-LOW** output enables ($\overline{\text{OE}}$: 0 = on, 1 = off). The 74HC126 has **active-HIGH** output enables (`OE`: 1 = on, 0 = off). Swapping them will completely invert bus enable logic.
- **Overdriving inputs above $V_{CC}$ on standard 74HC:** The standard 74HC series contains internal ESD clamp diodes from input pins to $V_{CC}$. If powering the 74HC125 at $3.3\text{ V}$ and driving inputs with $5\text{ V}$, use current-limiting series resistors ($1\text{ k}\Omega$) or use the 74LVC125 / 74AHC125 which have $5\text{ V}$-tolerant inputs without upper clamp diodes.

## Notes

- **74HC125 vs 74HC244:** The 74HC125 provides four independently enabled 1-bit gates. For wider 8-bit parallel buses or byte-wide data lines, the 20-pin **74HC244** or **74HC541** is more space-efficient, grouping eight gates under two quad-enable signals.
