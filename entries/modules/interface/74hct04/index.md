## Overview

The **74HCT04** (SN74HCT04) is a high-speed silicon-gate CMOS hex inverter IC containing six independent inverting buffer circuits (NOT gates). It provides identical logical functionality and pinout to the standard 74HC04, but is specifically engineered with **TTL-compatible input threshold voltages**.

While a standard 74HC04 powered from $+5\text{V}$ requires a high-level input of at least $V_{IH} \ge 3.15\text{V}$ ($0.7 \times V_{CC}$), the 74HCT04 switches reliably with **$V_{IH} \ge 2.0\text{V}$ and $V_{IL} \le 0.8\text{V}$**. This allows the 74HCT04 to serve as a fast, low-cost **3.3 V to 5.0 V logic level up-shifter** and direct interface between legacy TTL microprocessors (74LS, NMOS) or 3.3V microcontrollers (ESP32, STM32, Raspberry Pi) and 5V CMOS subsystems.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | 4.5 V to 5.5 V DC (5.0 V nominal) |
| **Logic Family** | TTL-Compatible High-Speed CMOS (74HCT) |
| **Input Thresholds** | $V_{IH} \ge 2.0\text{ V}$, $V_{IL} \le 0.8\text{ V}$ (Direct 3.3V logic compatibility) |
| **Output Type** | Full rail-to-rail CMOS output drive ($V_{OH} \approx V_{CC}$, $V_{OL} \approx \text{GND}$) |
| **Inverters Count** | 6 Independent NOT Gates ($Y = \overline{A}$) |
| **Propagation Delay ($t_{pd}$)** | $9\text{ ns}$ typ ($20\text{ ns}$ max) at $V_{CC} = 4.5\text{V}$ |
| **Package Options** | 14-pin DIP / SOIC-14 / TSSOP-14 |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
          1A 1│ 1   14│ VCC
          1Y 2│       │13 6A
          2A 3│       │12 6Y
          2Y 4│74HCT04│11 5A
          3A 5│       │10 5Y
          3Y 6│       │9  4A
         GND 7│       │8  4Y
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `1A` | Digital Input | Inverter 1 Input (TTL/3.3V compatible) |
| 2 | `1Y` | Digital Output | Inverter 1 Output ($1Y = \overline{1A}$) |
| 3 | `2A` | Digital Input | Inverter 2 Input |
| 4 | `2Y` | Digital Output | Inverter 2 Output |
| 5 | `3A` | Digital Input | Inverter 3 Input |
| 6 | `3Y` | Digital Output | Inverter 3 Output |
| 7 | `GND` | Power | Ground reference (0 V) |
| 8 | `4Y` | Digital Output | Inverter 4 Output |
| 9 | `4A` | Digital Input | Inverter 4 Input |
| 10 | `5Y` | Digital Output | Inverter 5 Output |
| 11 | `5A` | Digital Input | Inverter 5 Input |
| 12 | `6Y` | Digital Output | Inverter 6 Output |
| 13 | `6A` | Digital Input | Inverter 6 Input |
| 14 | `VCC` | Power | Supply voltage (+4.5 V to +5.5 V DC) |

## Function Table

| Input A | Output Y ($\overline{A}$) |
|---|---|
| Low ($L \le 0.8\text{V}$) | High ($H \ge 4.4\text{V}$) |
| High ($H \ge 2.0\text{V}$) | Low ($L \le 0.1\text{V}$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 4.5 | 5.0 | 5.5 | V | Standard HCT range |
| High-Level Input Voltage | $V_{IH}$ | 2.0 | — | — | V | $V_{CC} = 4.5\text{V} \dots 5.5\text{V}$ |
| Low-Level Input Voltage | $V_{IL}$ | — | — | 0.8 | V | $V_{CC} = 4.5\text{V} \dots 5.5\text{V}$ |
| High-Level Output Voltage | $V_{OH}$ | 4.4 | 4.5 | — | V | $V_{CC} = 4.5\text{V}, I_{OH} = -20\ \mu\text{A}$ |
| High-Level Output Voltage (Load) | $V_{OH}$ | 3.84 | 4.32 | — | V | $V_{CC} = 4.5\text{V}, I_{OH} = -4.0\text{ mA}$ |
| Low-Level Output Voltage | $V_{OL}$ | — | 0.0 | 0.1 | V | $V_{CC} = 4.5\text{V}, I_{OL} = 20\ \mu\text{A}$ |
| Low-Level Output Voltage (Load) | $V_{OL}$ | — | 0.17 | 0.33 | V | $V_{CC} = 4.5\text{V}, I_{OL} = 4.0\text{ mA}$ |
| Propagation Delay | $t_{PLH}, t_{PHL}$ | — | 9 | 20 | ns | $V_{CC} = 4.5\text{V}, C_L = 50\text{ pF}$ |
| Additional Quiescent Current | $\Delta I_{CC}$ | — | 100 | 360 | µA | Per input pin at $V_I = V_{CC} - 2.1\text{V}$ |

## Comparison: 74HCT04 vs 74HC04

| Parameter | 74HCT04 | 74HC04 |
|---|---|---|
| **Input Threshold Architecture** | Fixed TTL thresholds ($V_{IH}=2.0\text{V}, V_{IL}=0.8\text{V}$) | Proportional CMOS thresholds ($0.7 \times V_{CC} = 3.15\text{V}$ at $4.5\text{V}$) |
| **3.3V Logic Driven from 5V $V_{CC}$** | **Guaranteed valid logic HIGH** | **Marginal/Unreliable** ($3.3\text{V}$ barely exceeds $3.15\text{V}$) |
| **Operating Voltage Range** | Narrow: $4.5\text{ V} \dots 5.5\text{ V}$ | Wide: $2.0\text{ V} \dots 6.0\text{ V}$ |
| **Primary Application** | Interfacing 3.3V MCU / TTL outputs to 5V CMOS | General CMOS digital logic circuits |

## Typical Applications

### 3.3V to 5.0V Level Up-Shifting (Dual Inverter Buffer)

Cascading two inverters on a 74HCT04 yields a non-inverting, high-speed 3.3V-to-5.0V level shifter:

```
 3.3V Signal In (e.g. ESP32 GPIO)
          │
          ▼
     [Pin 1: 1A]
       74HCT04 (VCC = 5V)
     [Pin 2: 1Y] ──► Inverted 5V ──► [Pin 3: 2A]
                                       74HCT04
                                     [Pin 4: 2Y] ──► Clean +5V Rail-to-Rail Logic Output
```

## Common mistakes

- **Operating outside the 4.5V to 5.5V supply window:** Unlike the 74HC04 which operates down to 2.0V, the 74HCT04 requires $4.5\text{V} \le V_{CC} \le 5.5\text{V}$ to maintain calibrated TTL input threshold trip points.
- **Floating unused input pins:** Even though inputs are TTL-compatible, the underlying transistor gate is CMOS. Floating inputs drift and cause continuous shoot-through current across internal input stages. Tie all unused inputs to $V_{CC}$ or $GND$.
- **Expecting bidirectional operation:** The 74HCT04 is strictly unidirectional.

## Notes

- **Pin-Compatible Replacements:** 74HC04, 74LS04, 74ALS04, SN74HCT04N, CD74HCT04.
