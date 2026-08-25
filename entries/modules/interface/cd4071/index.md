## Overview

The **CD4071B** (CD4071) is a monolithic CMOS integrated circuit containing four independent 2-input **OR** logic gates. Fabricated using complementary N- and P-channel MOS enhancement transistors with standard B-series buffered outputs, it provides symmetrical output drive capability and high noise margin.

Capable of operating across an expansive power supply range from **$3.0\text{V}$ to $18.0\text{V}$ DC**, the CD4071B is widely utilized in battery-powered electronics, 12V automotive and industrial control panels, logic gating, and fault-detection systems where low standby current and high noise tolerance are essential.

## Quick reference

| | |
|---|---|
| **Supply Voltage Range (`VDD`)** | 3.0 V to 18.0 V DC (20.0 V maximum rating) |
| **Logic Family** | Standard CMOS 4000B Series |
| **Gate Count** | 4 Independent 2-Input OR Gates |
| **Logic Function** | $Y = A + B$ |
| **Propagation Delay ($t_{pd}$)** | $60\text{ ns}$ typ at $VDD = 10\text{V}$ ($120\text{ ns}$ at $5\text{V}$) |
| **Package Options** | 14-pin DIP / SOIC-14 / TSSOP-14 |
| **Noise Immunity** | $0.45 \times V_{DD}$ typical |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
          1A 1│ 1   14│ VDD
          1B 2│       │13 4B
          1Y 3│       │12 4A
          2Y 4│CD4071B│11 4Y
          2A 5│       │10 3Y
          2B 6│       │9  3A
         VSS 7│       │8  3B
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1, 2 | `1A`, `1B` | Digital Input | Gate 1 Data Inputs |
| 3 | `1Y` | Digital Output | Gate 1 OR Output ($1Y = 1A + 1B$) |
| 4 | `2Y` | Digital Output | Gate 2 OR Output ($2Y = 2A + 2B$) |
| 5, 6 | `2A`, `2B` | Digital Input | Gate 2 Data Inputs |
| 7 | `VSS` | Power | Ground / Negative Supply reference (0 V) |
| 8, 9 | `3B`, `3A` | Digital Input | Gate 3 Data Inputs |
| 10 | `3Y` | Digital Output | Gate 3 OR Output ($3Y = 3A + 3B$) |
| 11 | `4Y` | Digital Output | Gate 4 OR Output ($4Y = 4A + 4B$) |
| 12, 13 | `4A`, `4B` | Digital Input | Gate 4 Data Inputs |
| 14 | `VDD` | Power | Positive Supply Voltage (+3.0 V to +18.0 V DC) |

## Function Table

| Input A | Input B | Output Y ($A + B$) |
|---|---|---|
| Low ($L$) | Low ($L$) | Low ($L$) |
| Low ($L$) | High ($H$) | High ($H$) |
| High ($H$) | Low ($L$) | High ($H$) |
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

- **Leaving unused inputs floating:** Unconnected CMOS inputs float to intermediate voltage levels, causing internal shoot-through current and unpredictable power dissipation. Connect all unused inputs to `VSS` (GND) or `VDD`.
- **Assuming 74HC current drive:** Standard 4000B CMOS outputs provide $\sim 1\text{ mA}$ sink/source current at $5\text{V}$ ($4\text{ mA}$ at $15\text{V}$). Driving LEDs, buzzer transducers, or optocouplers directly from a 5V-powered CD4071 will cause voltage droop; use a transistor or buffer driver.
- **Driving 5V-powered CD4071 with 12V signals:** If the chip is powered at $5\text{V}$, input signals must not exceed $5.5\text{V}$. Driving a $12\text{V}$ signal into a $5\text{V}$ chip will forward-bias internal ESD diodes.

## Notes

- **CD4071B vs 74HC32:** 74HC32 is a high-speed $2\text{V} \dots 6\text{V}$ CMOS gate with higher current drive ($5.2\text{ mA}$). CD4071B supports high-voltage supply operation up to $18\text{V}$.
