## Overview

The **74HC573** (SN74HC573) is an 8-bit octal D-type transparent latch with 3-state outputs fabricated in high-speed silicon-gate CMOS technology. It provides identical logical functionality to the classic 74HC373 latch, but reorganizes the pinout into a modern **flow-through bus architecture**: all eight data inputs ($D0$–$D7$) are located on one side of the dual-in-line package (pins 2–9), while all eight 3-state latch outputs ($Q0$–$Q7$) are positioned directly opposite on the other side (pins 19–12).

This flow-through layout drastically simplifies PCB trace routing for microprocessor bus buffering, interface port expansion, and memory address latching. When **Latch Enable (`LE`)** is HIGH, the outputs follow the data inputs in real time. When `LE` goes LOW, the current state of data inputs is latched. Driving **Output Enable (`\overline{OE}`)** HIGH switches all outputs to high impedance (High-Z).

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | 2.0 V to 6.0 V DC (5.0 V nominal) |
| **Logic Family** | High-Speed CMOS (74HC) / TTL-Compatible (74HCT) |
| **Bus Width** | 8 Bits (Octal) |
| **Propagation Delay ($t_{pd}$)** | $14\text{ ns}$ typical at $VCC = 4.5\text{V}$ |
| **Output Drive Current** | $\pm 6.0\text{ mA}$ continuous ($\pm 7.8\text{ mA}$ peak at $4.5\text{V}$) |
| **Package Options** | 20-pin DIP / SOIC-20 / TSSOP-20 / SSOP-20 |
| **Pinout Architecture** | Flow-through bus layout (Inputs opposite Outputs) |

## Pinout (DIP-20 / SOIC-20)

```
             ┌───┴───┐
        /OE 1│ 1   20│ VCC
         D0 2│       │19 Q0
         D1 3│       │18 Q1
         D2 4│       │17 Q2
         D3 5│ 74HC573 16 Q3
         D4 6│       │15 Q4
         D5 7│       │14 Q5
         D6 8│       │13 Q6
         D7 9│       │12 Q7
        GND 10│      │11 LE
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `\overline{OE}` | Digital Input | Active-Low Output Enable (LOW = Active Outputs, HIGH = High-Z) |
| 2–9 | `D0`–`D7` | Digital Input | 8 Data Inputs (Pins 2 to 9 on left side) |
| 10 | `GND` | Power | Ground reference (0 V) |
| 11 | `LE` | Digital Input | Latch Enable input (HIGH = Transparent, LOW = Latched) |
| 12–19 | `Q7`–`Q0` | 3-State Output | 8 Latch Data Outputs (Pins 19 down to 12 on right side) |
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
| Output Enable Propagation | $t_{en}$ | — | 15 | 28 | ns | $\overline{OE} \downarrow$ to $Q_n, V_{CC} = 4.5\text{V}$ |
| Quiescent Current | $I_{CC}$ | — | — | 8.0 | µA | $V_{IN} = V_{CC}\text{ or GND}$ |

## Comparison: 74HC573 vs 74HC373

| Parameter | 74HC573 | 74HC373 |
|---|---|---|
| **Logic Function** | Identical 8-bit transparent latch | Identical 8-bit transparent latch |
| **Pinout Style** | **Flow-Through** (Inputs on Left, Outputs on Right) | **Interspersed** (Inputs & Outputs mingled) |
| **PCB Bus Routing** | Straight line traces with zero cross-overs | Requires trace twisting / via routing |
| **Recommended Use** | **New designs & custom PCBs** | Direct replacement on legacy circuit boards |

## Typical Applications

```
    Microcontroller / Bus In                             Latched Bus Output
   ──────────────────────────                          ──────────────────────
               D0 ───────────────── Pin 2   Pin 19 ──────────────── Q0
               D1 ───────────────── Pin 3   Pin 18 ──────────────── Q1
               D2 ───────────────── Pin 4   Pin 17 ──────────────── Q2
               D3 ───────────────── Pin 5   Pin 16 ──────────────── Q3
               D4 ───────────────── Pin 6   Pin 15 ──────────────── Q4
               D5 ───────────────── Pin 7   Pin 14 ──────────────── Q5
               D6 ───────────────── Pin 8   Pin 13 ──────────────── Q6
               D7 ───────────────── Pin 9   Pin 12 ──────────────── Q7
                                    74HC573
   MCU /OE Control ──────────────── Pin 1   Pin 11 ──────────────── MCU Latch Enable (LE)
```

## Common mistakes

- **Leaving unused input pins floating:** CMOS inputs draw excessive supply current and toggle randomly if left open. Connect any unused $D_n$ inputs to $VCC$ or $GND$.
- **Expecting edge-triggered clock behavior:** The 74HC573 is a **level-sensitive transparent latch**, not an edge-triggered register. While `LE` is held HIGH, any change or glitch on $D_n$ passes directly to $Q_n$. For edge-triggered flip-flop registers with flow-through pinout, use the **74HC574**.
- **Missing bypass capacitor:** Rapid 3-state switching of all 8 output lines simultaneously causes inductive rail bounce. Place a $100\text{ nF}$ ceramic decoupling capacitor immediately adjacent to Pin 20 ($VCC$) and Pin 10 ($GND$).

## Notes

- **Pin-Compatible Drop-In Replacements:** SN74HC573N, 74HC573D, 74HCT573, CD74HC573.
