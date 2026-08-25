## Overview

The **CD4081B** (CD4081) is a monolithic CMOS integrated circuit containing four independent 2-input **AND** logic gates. Fabricated with complementary N- and P-channel enhancement mode MOS transistors, it provides standard B-series buffered outputs for high output drive and symmetrical transition times.

Operating across an expansive supply voltage span of **$3.0\text{V}$ to $18.0\text{V}$ DC**, the CD4081B is ideal for high-noise industrial controls, 12V automotive electronics, battery-powered systems, and legacy digital logic interfacing where low static power dissipation and wide operating margins are required.

## Quick reference

| | |
|---|---|
| **Supply Voltage Range (`VDD`)** | 3.0 V to 18.0 V DC (20.0 V maximum limit) |
| **Logic Family** | Standard CMOS 4000B Series |
| **Gate Count** | 4 Independent 2-Input AND Gates |
| **Logic Function** | $Y = A \cdot B$ |
| **Propagation Delay ($t_{pd}$)** | $60\text{ ns}$ typ at $VDD = 10\text{V}$ ($120\text{ ns}$ at $5\text{V}$) |
| **Package Options** | 14-pin DIP / SOIC-14 / TSSOP-14 |
| **Noise Immunity** | $0.45 \times V_{DD}$ typical |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
          1A 1│ 1   14│ VDD
          1B 2│       │13 4B
          1Y 3│       │12 4A
          2Y 4│CD4081B│11 4Y
          2A 5│       │10 3Y
          2B 6│       │9  3B
         VSS 7│       │8  3A
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1, 2 | `1A`, `1B` | Digital Input | Gate 1 Data Inputs |
| 3 | `1Y` | Digital Output | Gate 1 AND Output ($1Y = 1A \cdot 1B$) |
| 4 | `2Y` | Digital Output | Gate 2 AND Output ($2Y = 2A \cdot 2B$) |
| 5, 6 | `2A`, `2B` | Digital Input | Gate 2 Data Inputs |
| 7 | `VSS` | Power | Negative Supply / Ground reference (0 V) |
| 8, 9 | `3A`, `3B` | Digital Input | Gate 3 Data Inputs |
| 10 | `3Y` | Digital Output | Gate 3 AND Output ($3Y = 3A \cdot 3B$) |
| 11 | `4Y` | Digital Output | Gate 4 AND Output ($4Y = 4A \cdot 4B$) |
| 12, 13 | `4A`, `4B` | Digital Input | Gate 4 Data Inputs |
| 14 | `VDD` | Power | Positive Supply Voltage (+3.0 V to +18.0 V DC) |

## Function Table

| Input A | Input B | Output Y ($A \cdot B$) |
|---|---|---|
| Low ($L$) | Low ($L$) | Low ($L$) |
| Low ($L$) | High ($H$) | Low ($L$) |
| High ($H$) | Low ($L$) | Low ($L$) |
| High ($H$) | High ($H$) | High ($H$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 3.0 | — | 18.0 | V | Operating DC voltage |
| Low-Level Input Voltage | $V_{IL}$ | — | — | 1.5 | V | $V_{DD} = 5\text{V}, V_O = 0.5\text{V}$ |
| High-Level Input Voltage | $V_{IH}$ | 3.5 | — | — | V | $V_{DD} = 5\text{V}, V_O = 4.5\text{V}$ |
| Output Sink Current | $I_{OL}$ | 0.51 | 1.0 | — | mA | $V_{DD} = 5\text{V}, V_{OUT} = 0.4\text{V}$ |
| Output Source Current | $I_{OH}$ | -0.51 | -1.0 | — | mA | $V_{DD} = 5\text{V}, V_{OUT} = 4.6\text{V}$ |
| Propagation Delay | $t_{PLH}, t_{PHL}$ | — | 120 | 250 | ns | $V_{DD} = 5\text{V}, C_L = 50\text{ pF}$ |
| Propagation Delay (10V) | $t_{PLH}, t_{PHL}$ | — | 60 | 120 | ns | $V_{DD} = 10\text{V}, C_L = 50\text{ pF}$ |
| Quiescent Device Current | $I_{DD}$ | — | 0.02 | 1.0 | µA | $V_{DD} = 5\text{V}, 25^\circ\text{C}$ |

## Common mistakes

- **Leaving unused gate inputs floating:** In high-impedance CMOS devices, open inputs drift randomly between logic levels, causing excessive power dissipation and oscillation. Tie all unused input pins ($A$ and $B$) directly to **`VSS` (GND)** or **`VDD`**.
- **Assuming TTL output drive strength:** While 74HC series ICs can source/sink $>5\text{ mA}$, standard CD4000B CMOS outputs only drive $\sim 1\text{ mA}$ at $5\text{V}$. Use a buffer (such as CD4050B or a 2N7000 MOSFET) when driving relays, optocouplers, or high-current LEDs directly.
- **Powering from 5V while driving from 12V without level shifting:** Input voltages must not exceed $V_{DD} + 0.5\text{V}$. Driving a 5V-powered CD4081 from a 12V sensor will forward-bias the internal ESD protection diode.

## Notes

- **CD4081B vs 74HC08:** The 74HC08 is much faster ($t_{pd} \approx 9\text{ ns}$ vs $120\text{ ns}$) but is limited to $2\text{V} \dots 6\text{V}$ operation. The CD4081B supports up to $18\text{V}$ supplies.
