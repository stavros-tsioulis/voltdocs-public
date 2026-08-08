## Overview

The **CD4001B** (HEF4001B) is a quad 2-input NOR gate IC in the classic CMOS 4000 series manufactured by Texas Instruments, ON Semiconductor, and Renesas. Containing four independent 2-input NOR gates in a 14-pin DIP/SOIC package, it operates over a wide voltage range of **3.0V to 18.0V DC**.

Providing high noise immunity, symmetrical output characteristics, and negligible static power consumption, the CD4001B is widely used in 12V automotive control circuits, high-voltage bistable latches, RC oscillators, and industrial sensor threshold gating.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VDD`)** | 3.0 V to 18.0 V DC |
| **Logic Family** | CMOS 4000 Series (CD4000 / HEF4000) |
| **Independent Gates** | 4 (Quad 2-Input NOR) |
| **Propagation Delay** | $60\text{ ns}$ typical at $VDD = 10\text{V}$ |
| **Output Drive Current** | $\pm 1.5\text{ mA}$ at $VDD = 10\text{V}$ |
| **Package** | 14-pin DIP / SOIC-14 / TSSOP-14 |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
          1A 1│ 1   14│ VDD
          1B 2│       │13 4B
         1/Y 3│ CD4001│12 4A
         2/Y 4│       │11 4/Y
          2A 5│       │10 3/Y
          2B 6│       │9  3B
         VSS 7│       │8  3A
             └───────┘
```

*Note: Pinout of CD4001 (outputs on Pins 3, 4, 10, 11) is different from 74HC02 (outputs on Pins 1, 4, 10, 13).*

| Pin | Name | Description |
|---|---|---|
| 1 | `1A` | Gate 1 Input A |
| 2 | `1B` | Gate 1 Input B |
| 3 | `1/Y` | Gate 1 Output ($1Y = \overline{1A + 1B}$) |
| 4 | `2/Y` | Gate 2 Output ($2Y = \overline{2A + 2B}$) |
| 5 | `2A` | Gate 2 Input A |
| 6 | `2B` | Gate 2 Input B |
| 7 | `VSS` | Ground reference (0 V) |
| 8 | `3A` | Gate 3 Input A |
| 9 | `3B` | Gate 3 Input B |
| 10 | `3/Y` | Gate 3 Output ($3Y = \overline{3A + 3B}$) |
| 11 | `4/Y` | Gate 4 Output ($4Y = \overline{4A + 4B}$) |
| 12 | `4A` | Gate 4 Input A |
| 13 | `4B` | Gate 4 Input B |
| 14 | `VDD` | Positive power supply voltage (+3.0V to +18.0V DC) |

## Function & Truth Table (Per Gate)

| Input A | Input B | Output Y |
|---|---|---|
| Low ($L$) | Low ($L$) | High ($H$) |
| Low ($L$) | High ($H$) | Low ($L$) |
| High ($H$) | Low ($L$) | Low ($L$) |
| High ($H$) | High ($H$) | Low ($L$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 3.0 | 10.0 | 18.0 | V | DC |
| High-Level Input Voltage | $V_{IH}$ | 3.5 | — | — | V | $V_{DD} = 5\text{V}$ |
| Low-Level Input Voltage | $V_{IL}$ | — | — | 1.5 | V | $V_{DD} = 5\text{V}$ |
| Propagation Delay ($A,B \rightarrow Y$) | $t_{PHL}, t_{PLH}$ | — | 60 | 120 | ns | $V_{DD} = 10\text{V}$ |
| High Output Drive Current | $I_{OH}$ | $-0.5$ | $-1.6$ | — | mA | $V_{DD} = 5\text{V}, V_{OH} = 4.6\text{V}$ |
| Quiescent Supply Current | $I_{DD}$ | — | 0.02 | 1.0 | µA | $V_{DD} = 5\text{V}$ |

## Typical Applications

### 12V Active-HIGH Sensor Latch Circuit

```
  Sensor Trigger (S) ──► [Pin 1: 1A]   [Pin 3: 1/Y] ──┬──► [Pin 5: 2A]
                              │                       │
                              └───[Cross Feedback]────┼──┐
                                                      │  │
  Reset Button (R) ────► [Pin 6: 2B]   [Pin 4: 2/Y] ──┴──┼──► Relay Driver Transistor
                              │                          │
                              └──────────────────────────┘
```

## Common mistakes

- **Mixing up CD4001 and 74HC02 pinouts:** Outputs on CD4001 are on **Pins 3, 4, 10, 11**, while outputs on 74HC02 are on **Pins 1, 4, 10, 13**. Replacing a CD4001 directly with a 74HC02 will short outputs to inputs.
- **Low drive current limit:** CD4001 outputs deliver only around $1\text{ mA} \dots 2\text{ mA}$ at 5V. Use a transistor buffer to drive LEDs or relays.
- **Leaving unused inputs floating:** Connect unused inputs to **$V_{SS}$ (GND) or $V_{DD}$**.

## Notes

- **CD4001 vs 74HC02:** CD4001 operates up to 18V supply voltage; 74HC02 operates up to 6V DC with 7ns switching speed.
