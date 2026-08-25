## Overview

The **74HC373** (SN74HC373) is an 8-bit octal D-type transparent latch with 3-state outputs fabricated in high-speed silicon-gate CMOS technology. It features eight individual data latches sharing a common **Latch Enable (`LE`)** input and an active-low **Output Enable (`\overline{OE}`)** control.

When `LE` is driven HIGH, the latches operate in **transparent mode**, meaning the outputs ($Q0$–$Q7$) follow the data inputs ($D0$–$D7$) continuously. When `LE` transitions LOW, the input data meeting setup time requirements is frozen and held in the latches. Driving `\overline{OE}` HIGH places all eight outputs into a high-impedance (High-Z) state, allowing direct connection to bus-organized systems (such as multiplexed microprocessor address/data buses) without loading the line.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | 2.0 V to 6.0 V DC (5.0 V nominal) |
| **Logic Family** | High-Speed CMOS (74HC) / TTL-Compatible (74HCT) |
| **Bus Width** | 8 Bits (Octal) |
| **Propagation Delay ($t_{pd}$)** | $15\text{ ns}$ typical at $VCC = 4.5\text{V}$ |
| **Output Drive Current** | $\pm 6.0\text{ mA}$ continuous ($\pm 7.8\text{ mA}$ peak at $4.5\text{V}$) |
| **Package Options** | 20-pin DIP / SOIC-20 / TSSOP-20 / SSOP-20 |
| **Pinout Layout** | Interspersed/alternating data I/O architecture |

## Pinout (DIP-20 / SOIC-20)

```
             ┌───┴───┐
        /OE 1│ 1   20│ VCC
         Q0 2│       │19 Q7
         D0 3│       │18 D7
         D1 4│       │17 D6
         Q1 5│ 74HC373 16 Q6
         Q2 6│       │15 Q5
         D2 7│       │14 D4
         D3 8│       │13 D4
         Q3 9│       │12 Q4
        GND 10│      │11 LE
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `\overline{OE}` | Digital Input | Active-Low Output Enable (LOW = Outputs Active, HIGH = High-Z) |
| 2, 5, 6, 9, 12, 15, 16, 19 | `Q0`–`Q7` | 3-State Output | 8 Latch Data Outputs |
| 3, 4, 7, 8, 13, 14, 17, 18 | `D0`–`D7` | Digital Input | 8 Data Inputs |
| 10 | `GND` | Power | Ground reference (0 V) |
| 11 | `LE` | Digital Input | Latch Enable input (HIGH = Transparent, LOW = Latched) |
| 20 | `VCC` | Power | Supply voltage (+2.0 V to +6.0 V DC) |

## Function Table

| Inputs | | | Output $Q_n$ | Operating Mode |
|---|---|---|---|---|
| `\overline{OE}` | `LE` | $D$ | | |
| Low ($L$) | High ($H$) | High ($H$) | High ($H$) | Transparent (Output follows Input) |
| Low ($L$) | High ($H$) | Low ($L$) | Low ($L$) | Transparent (Output follows Input) |
| Low ($L$) | Low ($L$) | X | $Q_0$ | Latched / Memory (Holds previous state) |
| High ($H$) | X | X | High-Z ($Z$) | Disabled / High Impedance |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.0 | 5.0 | 6.0 | V | Operating DC range |
| High-Level Input Voltage | $V_{IH}$ | 3.15 | — | — | V | $V_{CC} = 4.5\text{V}$ |
| Low-Level Input Voltage | $V_{IL}$ | — | — | 1.35 | V | $V_{CC} = 4.5\text{V}$ |
| Data Setup Time | $t_{su}$ | 10 | 5 | — | ns | $D_n$ valid before $LE \downarrow, V_{CC} = 4.5\text{V}$ |
| Data Hold Time | $t_h$ | 5 | 0 | — | ns | $D_n$ valid after $LE \downarrow, V_{CC} = 4.5\text{V}$ |
| Latch Enable Pulse Width | $t_w$ | 16 | 8 | — | ns | $LE$ high duration, $V_{CC} = 4.5\text{V}$ |
| Output Enable Propagation | $t_{en}$ | — | 15 | 30 | ns | $\overline{OE} \downarrow$ to $Q_n, V_{CC} = 4.5\text{V}$ |
| Quiescent Current | $I_{CC}$ | — | — | 8.0 | µA | $V_{IN} = V_{CC}\text{ or GND}$ |

## Typical Applications

### Microcontroller Multiplexed Bus Demultiplexing (ALE Latch)

In 8-bit microcontrollers (e.g. 8051 or AVR external memory interface) where lower address lines $A0$–$A7$ share physical pins with data lines $D0$–$D7$:

```
               MCU Bus Port
          (AD0-AD7 Multiplexed)
                   │
                   ├───► [D0-D7 Inputs]
                   │       74HC373
 MCU ALE Signal ───┴───► [LE Input]   [Q0-Q7 Outputs] ───► Static Lower Address Bus (A0-A7)
                         [\overline{OE} = GND]
```

## Common mistakes

- **Leaving `\overline{OE}` floating:** High-impedance CMOS inputs must never float. If output enable is not actively controlled by MCU GPIO, tie Pin 1 (`\overline{OE}`) directly to **`GND`**.
- **Confusing transparent latch (`74HC373`) with edge-triggered register (`74HC374` / `74HC574`):** The 74HC373 is level-sensitive (`LE` HIGH means outputs track inputs continuously). If edge-triggered storage on a clock pulse is required, choose the **74HC374** or **74HC574** flip-flop register instead.
- **Overlooking setup time before dropping `LE` LOW:** If input data changes simultaneously with the falling edge of `LE`, metastable output states can occur. Ensure data is stable at least $10\text{ ns}$ before dropping `LE` LOW.

## Notes

- **74HC373 vs 74HC573:** The 74HC373 and 74HC573 are functionally identical. The 74HC573 features modern "flow-through" pinout (all inputs on pins 2–9, all outputs on pins 12–19) to simplify PCB routing.
