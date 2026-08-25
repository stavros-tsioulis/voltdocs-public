## Overview

The **CD4093B** (CD4093) is a monolithic CMOS integrated circuit containing four independent 2-input **NAND** gates with built-in **Schmitt-trigger** action on both inputs. Each gate behaves as a regular 2-input NAND logic gate ($Y = \overline{A \cdot B}$), but features distinct positive ($V_T+$) and negative ($V_T-$) threshold levels.

Operating from **$3.0\text{V}$ to $18.0\text{V}$ DC** with substantial input hysteresis ($0.6\text{V}$ typ at $5\text{V}$, $2.0\text{V}$ at $10\text{V}$, $2.7\text{V}$ at $15\text{V}$), the CD4093B is renowned in **analog/modular synthesis (Lunetta synths, CMOS noise generators, drone machines)**, pulse stretchers, timer circuits, and industrial logic where slow or corrupted inputs must be cleaned up without extraneous triggering.

## Quick reference

| | |
|---|---|
| **Supply Voltage Range (`VDD`)** | 3.0 V to 18.0 V DC (20.0 V maximum rating) |
| **Logic Family** | Standard CMOS 4000B Series |
| **Gate Count** | 4 Independent 2-Input Schmitt-Trigger NAND Gates |
| **Hysteresis Voltage ($V_H$)** | $0.6\text{ V}$ typ at $5\text{V}$, $2.0\text{ V}$ typ at $10\text{V}$, $2.7\text{ V}$ typ at $15\text{V}$ |
| **Positive Threshold ($V_T+$)** | $2.9\text{ V}$ typ at $5\text{V}$ ($5.9\text{ V}$ typ at $10\text{V}$) |
| **Negative Threshold ($V_T-$)** | $2.3\text{ V}$ typ at $5\text{V}$ ($3.9\text{ V}$ typ at $10\text{V}$) |
| **Propagation Delay ($t_{pd}$)** | $130\text{ ns}$ typ at $V_{DD} = 10\text{V}$ ($250\text{ ns}$ at $5\text{V}$) |
| **Package Options** | 14-pin DIP / SOIC-14 / TSSOP-14 |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
          1A 1│ 1   14│ VDD
          1B 2│       │13 4B
          1Y 3│       │12 4A
          2Y 4│CD4093B│11 4Y
          2A 5│       │10 3Y
          2B 6│       │9  3B
         VSS 7│       │8  3A
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1, 2 | `1A`, `1B` | Schmitt Input | Gate 1 Inputs with Hysteresis |
| 3 | `1Y` | Digital Output | Gate 1 NAND Output ($1Y = \overline{1A \cdot 1B}$) |
| 4 | `2Y` | Digital Output | Gate 2 NAND Output ($2Y = \overline{2A \cdot 2B}$) |
| 5, 6 | `2A`, `2B` | Schmitt Input | Gate 2 Inputs with Hysteresis |
| 7 | `VSS` | Power | Ground / Negative Supply reference (0 V) |
| 8, 9 | `3A`, `3B` | Schmitt Input | Gate 3 Inputs with Hysteresis |
| 10 | `3Y` | Digital Output | Gate 3 NAND Output ($3Y = \overline{3A \cdot 3B}$) |
| 11 | `4Y` | Digital Output | Gate 4 NAND Output ($4Y = \overline{4A \cdot 4B}$) |
| 12, 13 | `4A`, `4B` | Schmitt Input | Gate 4 Inputs with Hysteresis |
| 14 | `VDD` | Power | Positive Supply Voltage (+3.0 V to +18.0 V DC) |

## Function Table

| Input A | Input B | Output Y ($\overline{A \cdot B}$) |
|---|---|---|
| Low ($L < V_T-$) | Low ($L < V_T-$) | High ($H$) |
| Low ($L < V_T-$) | High ($H > V_T+$) | High ($H$) |
| High ($H > V_T+$) | Low ($L < V_T-$) | High ($H$) |
| High ($H > V_T+$) | High ($H > V_T+$) | Low ($L$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 3.0 | — | 18.0 | V | Operating DC range |
| Positive Threshold Voltage | $V_T+$ | 2.2 | 2.9 | 3.6 | V | $V_{DD} = 5\text{V}$ |
| Negative Threshold Voltage | $V_T-$ | 1.4 | 2.3 | 2.8 | V | $V_{DD} = 5\text{V}$ |
| Hysteresis Voltage | $V_H$ | 0.3 | 0.6 | 1.6 | V | $V_{DD} = 5\text{V}$ |
| Output Sink Current | $I_{OL}$ | 0.51 | 1.0 | — | mA | $V_{DD} = 5\text{V}, V_{OUT} = 0.4\text{V}$ |
| Output Source Current | $I_{OH}$ | -0.51 | -1.0 | — | mA | $V_{DD} = 5\text{V}, V_{OUT} = 4.6\text{V}$ |
| Propagation Delay | $t_{PLH}, t_{PHL}$ | — | 130 | 260 | ns | $V_{DD} = 10\text{V}, C_L = 50\text{ pF}$ |
| Quiescent Current | $I_{DD}$ | — | 0.02 | 1.0 | µA | $V_{DD} = 5\text{V}, T_A = 25^\circ\text{C}$ |

## Typical Applications

### 9V/12V Gated Audio Oscillator / Drone Voice

```
 Control Voltage / Gate (High = Run) ───► [Pin 1: 1A]
                                                 CD4093B
                                          [Pin 3: 1Y] ───┬──────► Audio Square Wave Out
                                                 │       │
                               ┌──────[ R = 100kΩ Pot ]──┘
                               │
                          [Pin 2: 1B]
                               │
                          [ C = 10nF ]
                               │
                              GND
```

## Common mistakes

- **Leaving unused gate inputs open:** Floating inputs on unused gates float to intermediate voltages and consume milli-amps of power while injecting high-frequency switching noise into other gates. Tie all unused input pins to `VDD` or `VSS`.
- **Assuming TTL load driving capability:** At $5\text{V}$, the CD4093B can only source/sink $\sim 1\text{ mA}$. When driving bipolar transistors, relays, or speaker stages, buffer the output with a transistor or MOSFET.

## Notes

- **CD4093B vs CD4011B:** CD4093B is pin-for-pin identical to CD4011B, but with Schmitt-trigger inputs on all pins.
