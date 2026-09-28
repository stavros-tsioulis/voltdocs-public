## Overview

The **74HC164** (SN74HC164) is an 8-bit serial-in parallel-out (SIPO) shift register fabricated in high-speed silicon-gate CMOS technology, manufactured by Texas Instruments, Nexperia, and ON Semiconductor. It features an active-low asynchronous master clear (`~CLR~`), a positive-edge triggered clock (`CLK`), and dual AND-gated serial data inputs ($A$ and $B$).

Unlike the popular 74HC595—which incorporates an auxiliary storage latch and 3-state outputs—the 74HC164 presents shifted data directly at its parallel outputs ($Q_A$ through $Q_H$) immediately upon every clock edge. Housed in a smaller 14-pin package, it is commonly chosen for lightweight serial-to-parallel data deserialization, LCD character display drivers (such as HD44780 in 2-wire serial mode), LED bar graphs, and sequential control logic where intermediate latching is unnecessary.

## Quick reference

| | |
|---|---|
| **Function** | 8-Bit Serial-In / Parallel-Out (SIPO) Shift Register |
| **Logic Family** | High-Speed CMOS (74HC Series) / TTL Compatible (74HCT) |
| **Supply Voltage Range ($V_{CC}$)** | $2.0\text{ V}$ to $6.0\text{ V}$ DC ($4.5\text{ V} \dots 5.5\text{ V}$ nominal) |
| **Register Width** | 8 bits ($Q_A \dots Q_H$) |
| **Max Clock Frequency ($f_{MAX}$)** | $50\text{ MHz}$ typ at $4.5\text{ V}$ ($25\text{ MHz}$ min, $60\text{ MHz}$ at $6.0\text{ V}$) |
| **Propagation Delay ($t_{pd}$)** | $16\text{ ns}$ typ at $4.5\text{ V}$ ($C_L = 50\text{ pF}$) |
| **Output Drive Current** | $\pm 5.2\text{ mA}$ at $4.5\text{ V}$ ($\pm 25\text{ mA}$ absolute maximum per pin) |
| **Reset Function** | Asynchronous Master Clear (`~CLR~`, active-LOW) |
| **Package Options** | 14-pin DIP (N), SOIC-14 (D), TSSOP-14 (PW) |

## Pin configuration

### 14-Pin DIP / SOIC Package

```
             ┌───┴───┐
           A 1│ 1   14│ VCC (+2V to +6V)
           B 2│       │13 QH (Bit 7 Output)
          QA 3│       │12 QG (Bit 6 Output)
          QB 4│ 74HC16411 QF (Bit 5 Output)
          QC 5│       │10 QE (Bit 4 Output)
          QD 6│       │ 9 ~CLR~ (Active-Low Reset)
         GND 7│       │ 8 CLK (Clock)
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `A` | Digital Input | Serial data input A (internally AND-gated with B) |
| 2 | `B` | Digital Input | Serial data input B (internally AND-gated with A) |
| 3 | `QA` | Digital Output | Parallel output stage 0 (first bit loaded) |
| 4 | `QB` | Digital Output | Parallel output stage 1 |
| 5 | `QC` | Digital Output | Parallel output stage 2 |
| 6 | `QD` | Digital Output | Parallel output stage 3 |
| 7 | `GND` | Power Supply | Ground reference ($0\text{ V}$) |
| 8 | `CLK` | Digital Input | Clock input (Data shifts on rising edge $\uparrow$) |
| 9 | `~CLR~` | Digital Input | Master clear (Active-LOW asynchronous reset; clears all outputs to `LOW`) |
| 10 | `QE` | Digital Output | Parallel output stage 4 |
| 11 | `QF` | Digital Output | Parallel output stage 5 |
| 12 | `QG` | Digital Output | Parallel output stage 6 |
| 13 | `QH` | Digital Output | Parallel output stage 7 (last bit) |
| 14 | `VCC` | Power Supply | Positive supply voltage ($+2.0\text{ V}$ to $+6.0\text{ V}$) |

## Functional description

### Function Truth Table

| Mode | `~CLR~` | `CLK` | $A$ | $B$ | $Q_A$ | $Q_B \dots Q_H$ | Description |
|---|---|---|---|---|---|---|---|
| **Reset** | **`LOW`** | X | X | X | **`LOW`** | **`LOW`** | Asynchronous reset (all stages cleared) |
| **Shift 0** | **`HIGH`** | $\uparrow$ | `LOW` | X | **`LOW`** | $Q_{An-1} \dots Q_{Gn-1}$ | Shift zero into $Q_A$, prior bits shift right |
| **Shift 0** | **`HIGH`** | $\uparrow$ | X | `LOW` | **`LOW`** | $Q_{An-1} \dots Q_{Gn-1}$ | Shift zero into $Q_A$, prior bits shift right |
| **Shift 1** | **`HIGH`** | $\uparrow$ | `HIGH` | `HIGH` | **`HIGH`** | $Q_{An-1} \dots Q_{Gn-1}$ | Shift one into $Q_A$, prior bits shift right |
| **Hold** | **`HIGH`** | `LOW` / `HIGH` | X | X | $Q_A$ | $Q_B \dots Q_H$ | No change while clock is steady |

- **AND-Gated Serial Inputs:** The serial data input is determined by the logical AND of pins $A$ and $B$:
  $$D_{serial} = A \cdot B$$
  To use a single microcontroller serial line, tie either pin $A$ or pin $B$ directly to $V_{CC}$, using the remaining pin as the data input. Alternatively, one pin can be used as an active-high data gate / enable.
- **Direct Output Operation:** Data shifted into the register appears immediately at $Q_A \dots Q_H$. During the 8 clock pulses required to load a full byte, intermediate transient bit patterns will appear on the output pins.

### Comparison: 74HC164 vs 74HC595

| Feature | 74HC164 | 74HC595 |
|---|---|---|
| **Package** | 14-pin DIP / SOIC | 16-pin DIP / SOIC |
| **Control Lines Required** | 2 lines (`CLK`, `DATA`) | 3 lines (`SER`, `SRCLK`, `RCLK`) |
| **Storage Latch** | No (outputs update instantly on shift) | Yes (latched via separate `RCLK`) |
| **Output Ripple During Shift** | Yes (visible ripple) | None (outputs held steady until latched) |
| **3-State Outputs** | No (always active) | Yes (via active-low `~OE~`) |
| **Best Used For** | Pin-constrained designs, 2-wire LCD interfaces, shift chasers | LED matrices, glitch-free display driving, bus expanders |

## Absolute maximum ratings

> [!WARNING]
> Exceeding these ratings may cause permanent damage to the device.

| Parameter | Symbol | Min | Max | Unit |
|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | $-0.5$ | $+7.0$ | V |
| Input Clamp Current ($V_I < 0$ or $V_I > V_{CC}$) | $I_{IK}$ | — | $\pm 20$ | mA |
| Output Clamp Current ($V_O < 0$ or $V_O > V_{CC}$) | $I_{OK}$ | — | $\pm 20$ | mA |
| Continuous Output Current per pin | $I_O$ | — | $\pm 25$ | mA |
| Continuous $V_{CC}$ or Ground Current | $I_{CC}$ / $I_{GND}$ | — | $\pm 50$ | mA |
| Storage Temperature Range | $T_{stg}$ | $-65$ | $+150$ | °C |

## Electrical characteristics

### Recommended DC Operating Conditions ($T_A = 25^\circ\text{C}$)

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.0 | 5.0 | 6.0 | V | Operating range |
| High-Level Input Voltage | $V_{IH}$ | 3.15 | — | — | V | $V_{CC} = 4.5\text{ V}$ |
| Low-Level Input Voltage | $V_{IL}$ | — | — | 1.35 | V | $V_{CC} = 4.5\text{ V}$ |
| High-Level Output Voltage | $V_{OH}$ | 4.4 | 4.49 | — | V | $V_{CC} = 4.5\text{ V}, I_{OH} = -20\,\mu\text{A}$ |
| | | 3.84 | 4.3 | — | V | $V_{CC} = 4.5\text{ V}, I_{OH} = -4.0\text{ mA}$ |
| Low-Level Output Voltage | $V_{OL}$ | — | 0.001 | 0.1 | V | $V_{CC} = 4.5\text{ V}, I_{OL} = 20\,\mu\text{A}$ |
| | | — | 0.17 | 0.33 | V | $V_{CC} = 4.5\text{ V}, I_{OL} = 4.0\text{ mA}$ |
| Quiescent Current | $I_{CC}$ | — | — | 8.0 | µA | $V_I = V_{CC}\text{ or GND}$ |

### Switching & Timing Requirements ($V_{CC} = 4.5\text{ V}, C_L = 50\text{ pF}, T_A = 25^\circ\text{C}$)

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Maximum Clock Frequency | $f_{MAX}$ | 25 | 50 | — | MHz | $V_{CC} = 4.5\text{ V}$ |
| Propagation Delay (`CLK` to $Q_n$) | $t_{pd}$ | — | 16 | 30 | ns | Clock to any output |
| Propagation Delay (`~CLR~` to $Q_n$) | $t_{PHL}$ | — | 18 | 32 | ns | Asynchronous clear |
| Data Setup Time ($A, B$ valid before `CLK` $\uparrow$) | $t_{su}$ | 10 | 5 | — | ns | — |
| Data Hold Time ($A, B$ valid after `CLK` $\uparrow$) | $t_h$ | 5 | 0 | — | ns | — |
| Clock Pulse Width (`CLK` High or Low) | $t_w$ | 16 | 8 | — | ns | — |
| Clear Recovery Time (`~CLR~` $\uparrow$ to `CLK` $\uparrow$) | $t_{rec}$ | 5 | 0 | — | ns | — |

## Typical application: 2-Wire Microcontroller GPIO Expansion

The 74HC164 allows an 8-bit output expansion using only 2 GPIO pins on a microcontroller (`GPIO_DATA` and `GPIO_CLK`). By pulling pin 2 ($B$) and pin 9 (`~CLR~`) HIGH, pin 1 ($A$) becomes the single serial data input.

```
       Microcontroller                                74HC164 Shift Register
     ┌─────────────────┐                       ┌───────────────────────────────────┐
     │                 │                       │                                   │
     │       GPIO_DATA ┼───────────────────────┤ 1 (A)                      (QA) 3 ├───[330Ω]───> LED 0
     │                 │               +5V ────┤ 2 (B)                      (QB) 4 ├───[330Ω]───> LED 1
     │                 │                       │                            (QC) 5 ├───[330Ω]───> LED 2
     │        GPIO_CLK ┼───────────────────────┤ 8 (CLK)                    (QD) 6 ├───[330Ω]───> LED 3
     │                 │                       │                            (QE) 10├───[330Ω]───> LED 4
     │                 │               +5V ────┤ 9 (~CLR~)                  (QF) 11├───[330Ω]───> LED 5
     │                 │                       │                            (QG) 12├───[330Ω]───> LED 6
     │                 │                       │                            (QH) 13├───[330Ω]───> LED 7
     │                 │                       │                                   │
     │                 │                       │ 7 (GND)                   (VCC) 14├─── +5V
     └─────────────────┘                       └───────┬───────────────────┬───────┘
                                                       │    0.1µF MLCC     │
                                                       └────────┤├───[GND]─┘
```

### Control Example (C / Arduino)

```cpp
const int PIN_DATA = 2;
const int PIN_CLK  = 3;

void sendByte(uint8_t value) {
  // Shift out MSB first
  for (int i = 7; i >= 0; i--) {
    digitalWrite(PIN_DATA, (value >> i) & 0x01);
    digitalWrite(PIN_CLK, HIGH);
    delayMicroseconds(1);
    digitalWrite(PIN_CLK, LOW);
    delayMicroseconds(1);
  }
}
```

## Design considerations & common mistakes

- **Do Not Leave Pin B Floating or Grounded:** Because inputs $A$ and $B$ are internally AND-gated, if pin 2 ($B$) is grounded or left floating LOW, the effective data input ($A \cdot B$) will always evaluate to zero, and the register will only ever shift zeros. Tie pin 2 firmly to $V_{CC}$ if only using pin 1 as data.
- **Do Not Leave `~CLR~` Floating:** Pin 9 is an active-low asynchronous clear. If left unconnected, ambient capacitive noise will occasionally pull it LOW, randomly resetting all outputs. Connect to $V_{CC}$ directly or to a dedicated MCU reset GPIO.
- **Handling Output Ripple:** During the 8 clock pulses of a shift transmission, outputs $Q_A$ through $Q_H$ will display the shifting bit stream in real time. If driving loads where transient switching cannot be tolerated (such as relay coils, triacs, or motor drivers), use a latched register like the **74HC595** instead.
- **Decoupling Capacitor:** Fast CMOS edge transitions generate sharp current spikes. Place a $0.1\,\mu\text{F}$ ceramic capacitor directly across pin 14 ($V_{CC}$) and pin 7 (GND).
