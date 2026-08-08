## Overview

The **74HC02** (SN74HC02) is a quad 2-input NOR gate IC manufactured using high-speed silicon-gate CMOS technology. Containing four independent 2-input NOR gates in a 14-pin DIP/SOIC package, it performs the Boolean function $Y = \overline{A + B}$ in positive logic.

Like the NAND gate, the NOR gate is a **universal logic gate** capable of implementing any Boolean function without other gate types. Operating across a supply voltage range of **2.0V to 6.0V DC**, the 74HC02 features low CMOS power consumption and high switching speeds ($7\text{ ns}$ propagation delay).

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | 2.0 V to 6.0 V DC |
| **Logic Family** | High-Speed CMOS (74HC) / TTL Compatible (74HCT) |
| **Independent Gates** | 4 (Quad 2-Input NOR) |
| **Propagation Delay** | $7\text{ ns}$ typical at $VCC = 5.0\text{V}$ |
| **Output Drive Current** | $\pm 5.2\text{ mA}$ at $VCC = 4.5\text{V}$ |
| **Package** | 14-pin DIP / SOIC-14 / TSSOP-14 |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
         1/Y 1│ 1   14│ VCC
          1A 2│       │13 4/Y
          1B 3│       │12 4B
         2/Y 4│ 74HC02│11 4A
          2A 5│       │10 3/Y
          2B 6│       │9  3B
         GND 7│       │8  3A
             └───────┘
```

*Important Pinout Note: On 74HC02, outputs are on Pins 1, 4, 10, 13, and inputs are on Pins 2/3, 5/6, 8/9, 11/12 (unlike 74HC00/08/32 where inputs are on Pins 1/2)!*

| Pin | Name | Description |
|---|---|---|
| 1 | `1/Y` | Gate 1 Output ($1Y = \overline{1A + 1B}$) |
| 2 | `1A` | Gate 1 Input A |
| 3 | `1B` | Gate 1 Input B |
| 4 | `2/Y` | Gate 2 Output ($2Y = \overline{2A + 2B}$) |
| 5 | `2A` | Gate 2 Input A |
| 6 | `2B` | Gate 2 Input B |
| 7 | `GND` | Ground reference (0 V) |
| 8 | `3A` | Gate 3 Input A |
| 9 | `3B` | Gate 3 Input B |
| 10 | `3/Y` | Gate 3 Output ($3Y = \overline{3A + 3B}$) |
| 11 | `4A` | Gate 4 Input A |
| 12 | `4B` | Gate 4 Input B |
| 13 | `4/Y` | Gate 4 Output ($4Y = \overline{4A + 4B}$) |
| 14 | `VCC` | Power supply voltage (+2.0V to +6.0V DC) |

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
| Supply Voltage | $V_{CC}$ | 2.0 | 5.0 | 6.0 | V | DC |
| High-Level Input Voltage | $V_{IH}$ | 3.15 | — | — | V | $V_{CC} = 4.5\text{V}$ |
| Low-Level Input Voltage | $V_{IL}$ | — | — | 1.35 | V | $V_{CC} = 4.5\text{V}$ |
| Propagation Delay ($A,B \rightarrow Y$) | $t_{PD}$ | — | 7 | 15 | ns | $V_{CC} = 4.5\text{V}, C_L = 50\text{pF}$ |
| Output Drive Current | $I_{OUT}$ | — | — | $\pm 5.2$ | mA | $V_{CC} = 4.5\text{V}$ |
| Quiescent Supply Current | $I_{CC}$ | — | — | 2.0 | µA | $V_{IN} = V_{CC}\text{ or GND}$ |

## Typical Applications

### Active-HIGH SR Latch (Flip-Flop)

Cross-coupling two NOR gates creates an active-HIGH Set-Reset ($S$-$R$) latch.

```
  Reset (R) ────► [Pin 2: 1A]   [Pin 1: 1/Y] ──┬──► Output Q
                       │                       │
                       └───[Cross Feedback]────┼──┐
                                               │  │
  Set (S) ──────► [Pin 6: 2B]   [Pin 4: 2/Y] ──┴──┼──► Output /Q
                       │                          │
                       └──────────────────────────┘
```

## Common mistakes

- **Assuming Pin 1 is Input A:** On 74HC02, **Pin 1 is the Gate 1 Output**, while Pins 2 and 3 are inputs. Applying a 5V signal directly to Pin 1 short-circuits the output driver.
- **Confusing 74HC02 pinout with CD4001 pinout:** 74HC02 has outputs on Pins 1, 4, 10, 13; CD4001 has outputs on Pins 3, 4, 10, 11.
- **Leaving unused inputs floating:** Tie all unused gate inputs (e.g. Pins 5, 6, 8, 9, 11, 12) to **GND or $V_{CC}$**.

## Notes

- **74HC02 vs CD4001:** 74HC02 operates up to 6V DC with 7ns delay; CD4001 operates up to 18V DC with 60ns delay.
