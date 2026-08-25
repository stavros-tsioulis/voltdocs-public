## Overview

The **74HC240** (SN74HC240 / 74HCT240) is a high-speed silicon-gate CMOS octal inverting buffer / line driver IC manufactured by Texas Instruments, Nexperia, and onsemi. Housed in a 20-pin through-hole **DIP-20** and surface-mount **SOIC-20 / TSSOP-20** package, it is organized as two independent 4-bit inverting buffer banks, each controlled by its own active-LOW output enable pin ($1\bar{OE}$ and $2\bar{OE}$).

Operating across a supply range of **$2.0\text{V}$ to $6.0\text{V}$ DC** with a rapid propagation delay of **$9\text{ ns}$ at $5\text{V}$**, the 74HC240 provides high current drive capability ($\pm 6.0\text{ mA}$, driving up to 15 LSTTL loads) and true 3-state output isolation. Paired with its non-inverting twin the **74HC244**, the 74HC240 is standard equipment in retrocomputer architectures (Z80, 6502, 68000) and digital glue-logic for **inverting memory address/data lines, high-current LED indicator driving, transmission line termination, and bus isolation**.

## Quick reference

| | |
|---|---|
| **Logic Family** | High-Speed CMOS (74HC) / TTL-Compatible (74HCT) |
| **Function** | Octal Inverting Buffer / Line Driver (3-State) |
| **Bus Architecture** | Two 4-Bit Inverting Groups with Independent Enables |
| **Package** | 20-pin DIP (DIP-20 / PDIP-20) / 20-pin SOIC / TSSOP-20 |
| **Supply Voltage ($V_{CC}$)** | $2.0\text{ V}$ to $6.0\text{ V}$ (74HC) / $4.5\text{ V} \dots 5.5\text{ V}$ (74HCT) |
| **Propagation Delay ($t_{pd}$)** | **$9\text{ ns}$ typ** ($19\text{ ns}$ max) at $V_{CC} = 5.0\text{ V}$ |
| **Output Drive Current ($I_{OH}/I_{OL}$)**| **$\pm 6.0\text{ mA}$ at $5.0\text{ V}$** (15 LSTTL loads) |
| **Controls** | Dual Active-LOW Output Enables ($1\bar{OE}$ on Pin 1, $2\bar{OE}$ on Pin 19) |
| **Non-Inverting Twin** | **74HC244** (Octal Non-Inverting Buffer) |

## Pinout (DIP-20 Package)

```
                            ┌───┴───┐
       (Active-Low) 1/OE   1│ 1   20│ VCC (+2V to +6V)
       (Bank 1, In)  1A1   2│       │19 2/OE (Active-Low)
       (Bank 2, Out) 2Y4   3│ 74HC  │18 1Y1 (Bank 1, Out)
       (Bank 1, In)  1A2   4│  240  │17 2A4 (Bank 2, In)
       (Bank 2, Out) 2Y3   5│ DIP-20│16 1Y2 (Bank 1, Out)
       (Bank 1, In)  1A3   6│       │15 2A3 (Bank 2, In)
       (Bank 2, Out) 2Y2   7│       │14 1Y3 (Bank 1, Out)
       (Bank 1, In)  1A4   8│       │13 2A2 (Bank 2, In)
       (Bank 2, Out) 2Y1   9│       │12 1Y4 (Bank 1, Out)
                     GND  10│       │11 2A1 (Bank 2, In)
                            └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `1/OE` | Control Input | Bank 1 Active-LOW Output Enable (Tie to GND to enable $1Y_1 \dots 1Y_4$) |
| 2, 4, 6, 8 | `1A1 - 1A4` | Data Inputs | Bank 1 Data Inputs |
| 3, 5, 7, 9 | `2Y4 - 2Y1` | Data Outputs | Bank 2 Inverted 3-State Outputs |
| 10 | `GND` | Power | Common Ground reference ($0\text{ V}$) |
| 11, 13, 15, 17 | `2A1 - 2A4` | Data Inputs | Bank 2 Data Inputs |
| 12, 14, 16, 18 | `1Y4 - 1Y1` | Data Outputs | Bank 1 Inverted 3-State Outputs |
| 19 | `2/OE` | Control Input | Bank 2 Active-LOW Output Enable (Tie to GND to enable $2Y_1 \dots 2Y_4$) |
| 20 | `VCC` | Power | Positive Supply Voltage ($+2.0\text{ V}$ to $+6.0\text{ V}$) |

## Function / Truth Table (Each 4-Bit Bank)

| Output Enable ($\bar{OE}$) | Data Input ($A$) | Output ($Y$) | Output State |
|---|---|---|---|
| **L** | **L** | **H** | Active Inverting ($Y = \bar{A}$) |
| **L** | **H** | **L** | Active Inverting ($Y = \bar{A}$) |
| **H** | X | **Z** | High Impedance (Disabled / Disconnected) |

## Comparison: 74HC240 vs 74HC244 vs 74HC541

| IC Part Number | Polarity | Pinout Organization | Enable Control |
|---|---|---|---|
| **74HC240** | **Inverting ($Y = \bar{A}$)** | Staggered (Dual 4-Bit) | Dual Separate ($1\bar{OE}, 2\bar{OE}$) |
| **74HC244** | Non-Inverting ($Y = A$) | Staggered (Dual 4-Bit) | Dual Separate ($1\bar{OE}, 2\bar{OE}$) |
| **74HC541** | Non-Inverting ($Y = A$) | **Flow-Through (All In Left, All Out Right)**| Dual Gated Common |

## Common mistakes

- **Leaving Output Enable pins floating:** If $1\bar{OE}$ or $2\bar{OE}$ is left unconnected, floating charges will randomly place the corresponding 4-bit output group into high-impedance (Z) mode. Connect enable pins to **GND** for permanent active buffering.
- **Tracing confusion due to staggered pinout:** Note that Pins 2, 4, 6, 8 are Inputs for Bank 1, but adjacent Pins 3, 5, 7, 9 are Outputs for Bank 2. (For a clean flow-through layout with inputs on one side and outputs on the other, consider the **74HC541**).

## Notes

- **74HCT240 Variant:** Uses TTL input switching thresholds ($V_{IH} = 2.0\text{V}, V_{IL} = 0.8\text{V}$), making it ideal for interfacing 3.3V logic signals into 5V system buses.
