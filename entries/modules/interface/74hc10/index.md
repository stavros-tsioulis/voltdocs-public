## Overview

The **74HC10** (SN74HC10) is a high-speed silicon-gate CMOS integrated circuit containing three independent 3-input **NAND** logic gates. Each gate performs the Boolean function $Y = \overline{A \cdot B \cdot C}$ (or by De Morgan's laws, $Y = \overline{A} + \overline{B} + \overline{C}$).

Operating across a $2.0\text{V}$ to $6.0\text{V}$ supply voltage window with standard CMOS rail-to-rail drive capability and low static power dissipation ($2\ \mu\text{A}$ max), the 74HC10 is a versatile building block for address decoding, state-machine condition checking, and multi-input interlock logic.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | 2.0 V to 6.0 V DC (5.0 V nominal) |
| **Logic Family** | High-Speed CMOS (74HC) / TTL-Compatible (74HCT) |
| **Gate Count** | 3 Independent 3-Input NAND Gates |
| **Logic Function** | $Y = \overline{A \cdot B \cdot C}$ |
| **Propagation Delay ($t_{pd}$)** | $9\text{ ns}$ typ ($18\text{ ns}$ max) at $V_{CC} = 4.5\text{V}$ |
| **Output Drive Current** | $\pm 5.2\text{ mA}$ at $V_{CC} = 4.5\text{V}$ |
| **Package Options** | 14-pin DIP / SOIC-14 / TSSOP-14 |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
          1A 1│ 1   14│ VCC
          1B 2│       │13 1C
          2A 3│       │12 1Y
          2B 4│ 74HC10│11 3C
          2C 5│       │10 3B
          2Y 6│       │9  3A
         GND 7│       │8  3Y
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1, 2, 13 | `1A`, `1B`, `1C` | Digital Input | Gate 1 Data Inputs |
| 3, 4, 5 | `2A`, `2B`, `2C` | Digital Input | Gate 2 Data Inputs |
| 6 | `2Y` | Digital Output | Gate 2 NAND Output ($2Y = \overline{2A \cdot 2B \cdot 2C}$) |
| 7 | `GND` | Power | Ground reference (0 V) |
| 8 | `3Y` | Digital Output | Gate 3 NAND Output ($3Y = \overline{3A \cdot 3B \cdot 3C}$) |
| 9, 10, 11 | `3A`, `3B`, `3C` | Digital Input | Gate 3 Data Inputs |
| 12 | `1Y` | Digital Output | Gate 1 NAND Output ($1Y = \overline{1A \cdot 1B \cdot 1C}$) |
| 14 | `VCC` | Power | Supply voltage (+2.0 V to +6.0 V DC) |

## Function Table

| Input A | Input B | Input C | Output Y ($\overline{A \cdot B \cdot C}$) |
|---|---|---|---|
| High ($H$) | High ($H$) | High ($H$) | Low ($L$) |
| Low ($L$) | X | X | High ($H$) |
| X | Low ($L$) | X | High ($H$) |
| X | X | Low ($L$) | High ($H$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.0 | 5.0 | 6.0 | V | Operating DC voltage |
| High-Level Input Voltage | $V_{IH}$ | 3.15 | — | — | V | $V_{CC} = 4.5\text{V}$ |
| Low-Level Input Voltage | $V_{IL}$ | — | — | 1.35 | V | $V_{CC} = 4.5\text{V}$ |
| High-Level Output Voltage | $V_{OH}$ | 4.4 | 4.5 | — | V | $V_{CC} = 4.5\text{V}, I_{OH} = -20\ \mu\text{A}$ |
| Low-Level Output Voltage | $V_{OL}$ | — | 0.0 | 0.1 | V | $V_{CC} = 4.5\text{V}, I_{OL} = 20\ \mu\text{A}$ |
| Propagation Delay | $t_{PLH}, t_{PHL}$ | — | 9 | 18 | ns | $V_{CC} = 4.5\text{V}, C_L = 50\text{ pF}$ |
| Quiescent Current | $I_{CC}$ | — | — | 2.0 | µA | $V_{IN} = V_{CC}\text{ or GND}$ |

## Common mistakes

- **Leaving the third input (C) floating when using as a 2-input gate:** If only 2 inputs are needed, Pin C must not float. Tie the unused input either to **`VCC`** (which acts as a logical 1, enabling the remaining two inputs) or tie it in parallel with input A or B.
- **Floating unused gates:** Never leave any input pins on unused gates disconnected. Tie all unused inputs to `VCC` or `GND` to prevent CMOS rail-to-rail oscillation and increased standby current.
- **Missing decoupling capacitor:** Rapid simultaneous switching of multiple outputs creates inductive transients. Place a $100\text{ nF}$ ceramic capacitor directly across Pin 14 ($VCC$) and Pin 7 ($GND$).

## Notes

- **74HC10 vs 74HC00 vs 74HC20:** 74HC00 contains four 2-input NAND gates; 74HC10 contains three 3-input NAND gates; 74HC20 contains two 4-input NAND gates.
