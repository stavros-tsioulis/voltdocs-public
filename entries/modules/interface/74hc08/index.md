## Overview

The **74HC08** (SN74HC08) is a quad 2-input AND gate IC manufactured using high-speed silicon-gate CMOS technology. Containing four independent 2-input AND gates in a 14-pin DIP/SOIC package, it performs the Boolean function $Y = A \cdot B$ or $Y = \overline{\overline{A} + \overline{B}}$ in positive logic.

Operating from a wide supply voltage range of **2.0V to 6.0V DC**, it combines low power CMOS consumption with high-speed switching speeds comparable to Low-Power Schottky TTL (LS-TTL). It is a staple component in digital logic kits, signal gating networks, enable/disable switches, and safety interlock systems.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | 2.0 V to 6.0 V DC |
| **Logic Family** | High-Speed CMOS (74HC) / TTL Compatible (74HCT) |
| **Independent Gates** | 4 (Quad 2-Input AND) |
| **Propagation Delay** | $7\text{ ns}$ typical at $VCC = 5.0\text{V}$ |
| **Output Drive Current** | $\pm 5.2\text{ mA}$ at $VCC = 4.5\text{V}$ |
| **Package** | 14-pin DIP / SOIC-14 / TSSOP-14 |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
          1A 1│ 1   14│ VCC
          1B 2│       │13 4B
          1Y 3│       │12 4A
          2A 4│ 74HC08│11 4Y
          2B 5│       │10 3B
          2Y 6│       │9  3A
         GND 7│       │8  3Y
             └───────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `1A` | Gate 1 Input A |
| 2 | `1B` | Gate 1 Input B |
| 3 | `1Y` | Gate 1 Output ($1Y = 1A \cdot 1B$) |
| 4 | `2A` | Gate 2 Input A |
| 5 | `2B` | Gate 2 Input B |
| 6 | `2Y` | Gate 2 Output ($2Y = 2A \cdot 2B$) |
| 7 | `GND` | Ground reference (0 V) |
| 8 | `3Y` | Gate 3 Output ($3Y = 3A \cdot 3B$) |
| 9 | `3A` | Gate 3 Input A |
| 10 | `3B` | Gate 3 Input B |
| 11 | `4Y` | Gate 4 Output ($4Y = 4A \cdot 4B$) |
| 12 | `4A` | Gate 4 Input A |
| 13 | `4B` | Gate 4 Input B |
| 14 | `VCC` | Power supply voltage (+2.0V to +6.0V DC) |

## Function & Truth Table (Per Gate)

| Input A | Input B | Output Y |
|---|---|---|
| Low ($L$) | Low ($L$) | Low ($L$) |
| Low ($L$) | High ($H$) | Low ($L$) |
| High ($H$) | Low ($L$) | Low ($L$) |
| High ($H$) | High ($H$) | High ($H$) |

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

### Signal Gate / Pulse Enable Control

Passing a PWM clock signal to a motor driver or buzzer only when a control ENABLE pin is HIGH.

```
  Clock Signal ────────► [Pin 1: 1A]
                          74HC08 ───► [Pin 3: 1Y] ───► Gated Clock Out (Active when ENABLE is High)
  Enable Control ──────► [Pin 2: 1B]
```

## Common mistakes

- **Leaving inputs of unused AND gates floating:** Unused CMOS gate inputs (e.g. pins 4, 5, 9, 10, 12, 13) must be tied to **$V_{CC}$ or GND**. Floating CMOS inputs drift into linear operating regions, causing high supply current draw and cross-talk noise.
- **Driving 74HC08 inputs with 3.3V logic when powered from 5V:** When powered from $V_{CC} = 5\text{V}$, the 74HC08 requires $V_{IH} \ge 3.15\text{V}$. A 3.3V GPIO output is right on the noise margin threshold. Use the **74HCT08** variant ($V_{IH} \ge 2.0\text{V}$) for 3.3V to 5V TTL level compatibility.

## Notes

- **74HC08 vs 74HC00 vs 74HC11:** 74HC08 contains quad 2-input AND gates; 74HC00 contains quad 2-input NAND gates; 74HC11 contains triple 3-input AND gates.
