## Overview

The **74HC00** (SN74HC00) is a quad 2-input NAND gate IC manufactured using high-speed silicon-gate CMOS technology. Containing four independent 2-input NAND gates in a 14-pin DIP/SOIC package, it performs the Boolean function $Y = \overline{A \cdot B}$ in positive logic.

The NAND gate is a **universal logic gate**; any basic logic function (AND, OR, NOT, NOR, XOR, SR Latch) can be constructed using only 74HC00 ICs. Operating over a supply range of **2.0V to 6.0V DC**, it offers low CMOS power consumption with high-speed switching speeds ($7\text{ ns}$ propagation delay).

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | 2.0 V to 6.0 V DC |
| **Logic Family** | High-Speed CMOS (74HC) / TTL Compatible (74HCT) |
| **Independent Gates** | 4 (Quad 2-Input NAND) |
| **Propagation Delay** | $7\text{ ns}$ typical at $VCC = 5.0\text{V}$ |
| **Output Drive Current** | $\pm 5.2\text{ mA}$ at $VCC = 4.5\text{V}$ |
| **Package** | 14-pin DIP / SOIC-14 / TSSOP-14 |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
          1A 1│ 1   14│ VCC
          1B 2│       │13 4B
         1/Y 3│       │12 4A
          2A 4│ 74HC00│11 4/Y
          2B 5│       │10 3B
         2/Y 6│       │9  3A
         GND 7│       │8  3/Y
             └───────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `1A` | Gate 1 Input A |
| 2 | `1B` | Gate 1 Input B |
| 3 | `1/Y` | Gate 1 Output ($1Y = \overline{1A \cdot 1B}$) |
| 4 | `2A` | Gate 2 Input A |
| 5 | `2B` | Gate 2 Input B |
| 6 | `2/Y` | Gate 2 Output ($2Y = \overline{2A \cdot 2B}$) |
| 7 | `GND` | Ground reference (0 V) |
| 8 | `3/Y` | Gate 3 Output ($3Y = \overline{3A \cdot 3B}$) |
| 9 | `3A` | Gate 3 Input A |
| 10 | `3B` | Gate 3 Input B |
| 11 | `4/Y` | Gate 4 Output ($4Y = \overline{4A \cdot 4B}$) |
| 12 | `4A` | Gate 4 Input A |
| 13 | `4B` | Gate 4 Input B |
| 14 | `VCC` | Power supply voltage (+2.0V to +6.0V DC) |

## Function & Truth Table (Per Gate)

| Input A | Input B | Output Y |
|---|---|---|
| Low ($L$) | Low ($L$) | High ($H$) |
| Low ($L$) | High ($H$) | High ($H$) |
| High ($H$) | Low ($L$) | High ($H$) |
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

### 1. NAND SR Latch (Flip-Flop)

Cross-coupling two NAND gates creates an active-LOW Set-Reset ($\overline{S}$-$\overline{R}$) latch.

```
  Set (/S) ─────► [Pin 1: 1A]   [Pin 3: 1Y] ──┬──► Output Q
                       │                      │
                       └───[Cross Feedback]───┼──┐
                                              │  │
  Reset (/R) ───► [Pin 5: 2B]   [Pin 6: 2Y] ──┴──┼──► Output /Q
                       │                         │
                       └─────────────────────────┘
```

## Common mistakes

- **Leaving unused NAND inputs floating:** Floating inputs on pins 4, 5, 9, 10, 12, 13 cause internal switching noise and excessive supply current. Tie unused inputs to **$V_{CC}$ or GND**.
- **Confusing 74HC00 pinout with CD4011 pinout:** Although both are Quad 2-Input NAND ICs, their pin layouts differ. On 74HC00, outputs are on pins 3, 6, 8, 11; on CD4011, outputs are on pins 3, 4, 10, 11.
- **Driving 74HC00 inputs with 3.3V logic when powered from 5V:** When powered from $5\text{V}$, the 74HC00 requires $V_{IH} \ge 3.15\text{V}$. Use **74HCT00** for direct 3.3V logic compatibility.

## Notes

- **74HC00 vs CD4011:** 74HC00 operates up to 6V DC with 7ns delay; CD4011 operates up to 18V DC with 60ns delay.
