## Overview

The **74HC245** (SN74HC245) is an octal 3-state non-inverting bidirectional bus transceiver manufactured using high-speed Silicon-Gate CMOS technology. Designed for asynchronous 8-bit two-way data communication between data buses, it features 8 channels (`A1`–`A8` and `B1`–`B8`), a direction control pin (`DIR`), and an active-low output enable pin (`/OE` or `CE`).

It is widely used in retro-computing, microcontroller development, LED matrix driving, and logic-level conversion circuits to isolate buses or buffer high-capacitance bus lines.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | 2.0 V to 6.0 V DC |
| **Logic Family** | High-Speed CMOS (74HC) / TTL-Compatible (74HCT) |
| **Bus Width** | 8 Bits (Octal) |
| **Max Output Drive Current** | $\pm 35\text{ mA}$ per pin |
| **Propagation Delay** | $13\text{ ns}$ typical at $VCC = 4.5\text{V}$ |
| **Package** | 20-pin DIP / SOIC-20 / TSSOP-20 |

## Pinout (DIP-20 Package)

```
             ┌───┴───┐
       DIR 1 │ 1  20 │ VCC
        A1 2 │ 2  19 │ /OE (Output Enable)
        A2 3 │ 3  18 │ B1
        A3 4 │ 4  17 │ B2
        A4 5 │ 5  16 │ B3
        A5 6 │ 6  15 │ B4
        A6 7 │ 7  14 │ B5
        A7 8 │ 8  13 │ B6
        A8 9 │ 9  12 │ B7
       GND 10│10  11 │ B8
             └───────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `DIR` | Direction Control: High ($1$) = A data to B bus; Low ($0$) = B data to A bus |
| 2–9 | `A1`–`A8` | Side A 8-bit bidirectional data pins |
| 10 | `GND` | System ground reference (0 V) |
| 11–18 | `B8`–`B1` | Side B 8-bit bidirectional data pins |
| 19 | `/OE` | Output Enable (Active Low): Low ($0$) = Outputs enabled; High ($1$) = High-Impedance (Z) |
| 20 | `VCC` | Positive supply voltage (+2V to +6V DC) |

## Function Table

| Control Inputs | | Bus Operation |
|---|---|---|
| **/OE** | **DIR** | **Data Path** |
| Low ($L$) | Low ($L$) | B data to A bus ($B \rightarrow A$) |
| Low ($L$) | High ($H$) | A data to B bus ($A \rightarrow B$) |
| High ($H$) | X (Don't Care) | High-Impedance state ($Z$) on both A and B buses |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.0 | 5.0 | 6.0 | V | DC |
| High-Level Input Voltage | $V_{IH}$ | 3.15 | — | — | V | $V_{CC} = 4.5\text{V}$ |
| Low-Level Input Voltage | $V_{IL}$ | — | — | 1.35 | V | $V_{CC} = 4.5\text{V}$ |
| Propagation Delay ($A \rightarrow B$) | $t_{PD}$ | — | 13 | 22 | ns | $V_{CC} = 4.5\text{V}, C_L = 50\text{pF}$ |
| Output Drive Current | $I_{OUT}$ | — | — | $\pm 35$ | mA | $V_{CC} = 6.0\text{V}$ |
| Quiescent Supply Current | $I_{CC}$ | — | — | 8.0 | µA | $V_{IN} = V_{CC}\text{ or GND}$ |

## Typical Application (5V to 3.3V Unidirectional Buffer / Level Shifter)

When powered from $V_{CC} = 3.3\text{V}$, the 74HC245's inputs on Side A are 5V-tolerant in 74LVC245 or 74AHCT245 variants. For standard 74HC245 powered at 3.3V, use voltage divider resistors or 74LVC245 for 5V-to-3.3V translation.

```
       5V MCU / Bus                             3.3V Target Device
   [Arduino D2..D9]                             [Display / SD Card]
         │                                               │
     5V Signal A1..A8 ──► [Side A: Pins 2-9]           3.3V Signal B1..B8 ──► [Side B: Pins 18-11]
                           74LVC245 / 74HC245
                           [Pin 1: DIR] ◄── 3.3V / GND (Set Direction)
                           [Pin 19: /OE] ◄── GND (Enable Output)
```

## Common mistakes

- **Leaving `/OE` or `DIR` pins floating:** CMOS inputs must never be left floating. Unconnected `/OE` or `DIR` pins float between high and low logic states, causing high supply current draw, erratic bus output, or high-Z oscillations.
- **Bus contention:** Enabling the outputs (`/OE` = LOW) when both Side A and Side B are simultaneously driven by external outputs of different voltage levels creates short-circuit conditions between bus drivers, damaging the 74HC245 or microcontrollers.
- **Assuming 74HC245 powered at 5V recognizes 3.3V logic high:** When powered from $5\text{V}$, a standard 74HC245 requires $V_{IH} \ge 3.15\text{V}$ (which is $0.7 \times V_{CC}$). A 3.3V microcontroller GPIO output ($3.0\text{V} \dots 3.3\text{V}$) is barely on the threshold margin and can fail intermittently. Use **74HCT245** (TTL input levels, $V_{IH} \ge 2.0\text{V}$) when driving a 5V transceiver from 3.3V logic.

## Notes

- **74HC245 vs 74HCT245 vs 74LVC245:** 74HC245 features pure CMOS inputs ($0.7 \times V_{CC}$ threshold); 74HCT245 has TTL-compatible input thresholds ($2.0\text{V}$ high threshold); 74LVC245 has 5V tolerant inputs even when powered from a 3.3V supply rail.
