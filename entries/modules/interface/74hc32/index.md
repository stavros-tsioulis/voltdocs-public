## Overview

The **74HC32** (SN74HC32) is a quad 2-input OR gate IC manufactured using high-speed silicon-gate CMOS technology. Containing four independent 2-input OR gates in a 14-pin DIP/SOIC package, it performs the Boolean function $Y = A + B$ in positive logic.

Operating from a wide supply voltage range of **2.0V to 6.0V DC**, it combines low power CMOS consumption with high-speed switching speeds ($7\text{ ns}$ propagation delay). It is widely used in digital logic designs for multi-source alarm trigger ORing, address decoding logic, and control signal combining.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | 2.0 V to 6.0 V DC |
| **Logic Family** | High-Speed CMOS (74HC) / TTL Compatible (74HCT) |
| **Independent Gates** | 4 (Quad 2-Input OR) |
| **Propagation Delay** | $7\text{ ns}$ typical at $VCC = 5.0\text{V}$ |
| **Output Drive Current** | $\pm 5.2\text{ mA}$ at $VCC = 4.5\text{V}$ |
| **Package** | 14-pin DIP / SOIC-14 / TSSOP-14 |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
          1A 1│ 1   14│ VCC
          1B 2│       │13 4B
          1Y 3│       │12 4A
          2A 4│ 74HC32│11 4Y
          2B 5│       │10 3B
          2Y 6│       │9  3A
         GND 7│       │8  3Y
             └───────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `1A` | Gate 1 Input A |
| 2 | `1B` | Gate 1 Input B |
| 3 | `1Y` | Gate 1 Output ($1Y = 1A + 1B$) |
| 4 | `2A` | Gate 2 Input A |
| 5 | `2B` | Gate 2 Input B |
| 6 | `2Y` | Gate 2 Output ($2Y = 2A + 2B$) |
| 7 | `GND` | Ground reference (0 V) |
| 8 | `3Y` | Gate 3 Output ($3Y = 3A + 3B$) |
| 9 | `3A` | Gate 3 Input A |
| 10 | `3B` | Gate 3 Input B |
| 11 | `4Y` | Gate 4 Output ($4Y = 4A + 4B$) |
| 12 | `4A` | Gate 4 Input A |
| 13 | `4B` | Gate 4 Input B |
| 14 | `VCC` | Power supply voltage (+2.0V to +6.0V DC) |

## Function & Truth Table (Per Gate)

| Input A | Input B | Output Y |
|---|---|---|
| Low ($L$) | Low ($L$) | Low ($L$) |
| Low ($L$) | High ($H$) | High ($H$) |
| High ($H$) | Low ($L$) | High ($H$) |
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

### Multi-Sensor Fault Alarm ORing

Triggering an alarm buzzer if Sensor A OR Sensor B OR Sensor C detects a fault condition.

```
  Sensor A ──► [Pin 1: 1A]
                74HC32 ───► [Pin 3: 1Y] ──► [Pin 4: 2A]
  Sensor B ──► [Pin 2: 1B]                   74HC32 ───► [Pin 6: 2Y] ──► Alarm Buzzer Driver
  Sensor C ───────────────────────────────► [Pin 5: 2B]
```

## Common mistakes

- **Leaving unused OR gate inputs floating:** Unused inputs (e.g. pins 9, 10, 12, 13) must be tied to **GND or $V_{CC}$** to prevent floating CMOS states and excessive power consumption.
- **Driving 74HC32 from 3.3V logic when powered at 5V:** High-speed CMOS requires $V_{IH} \ge 3.15\text{V}$ at $V_{CC} = 5\text{V}$. Use **74HCT32** for direct 3.3V to 5V TTL compatibility.

## Notes

- **74HC32 vs 74HC86 vs 74HC02:** 74HC32 contains quad 2-input OR gates; 74HC86 contains quad 2-input XOR gates; 74HC02 contains quad 2-input NOR gates.
