## Overview

The **74HC157** (SN74HC157 / 74HCT157) is a high-speed silicon-gate CMOS Quad 2-to-1 line data selector / multiplexer IC manufactured by Texas Instruments, Nexperia, and onsemi. Housed in a standard 16-pin through-hole **DIP-16** and surface-mount **SOIC-16 / TSSOP-16** package, it contains **four independent 2-input digital multiplexers** sharing a common Select input ($S$) and a common active-LOW Strobe / Enable input ($\bar{G}$).

Operating across a supply voltage range of **$2.0\text{V}$ to $6.0\text{V}$ DC** with a rapid propagation delay of **$11\text{ ns}$ at $5\text{V}$**, the 74HC157 selects four bits of data from two alternative 4-bit sources ($A$ or $B$) and passes them to the four outputs ($1Y \dots 4Y$). It is a cornerstone building block in retrocomputing architectures (Commodore 64, Apple II, ZX Spectrum) and FPGA/CPLD glue-logic for **4-bit/8-bit bus multiplexing, dynamic RAM (DRAM) row/column address multiplexing, and video signal switching**.

## Quick reference

| | |
|---|---|
| **Logic Family** | High-Speed CMOS (74HC) / TTL-Compatible (74HCT) |
| **Function** | Quad 2-Input to 1-Output Data Multiplexer (Non-Inverting) |
| **Channels** | 4 independent 2-to-1 multiplexers ($1A/1B \dots 4A/4B$) |
| **Package** | 16-pin DIP (DIP-16 / PDIP-16) / 16-pin SOIC / TSSOP-16 |
| **Supply Voltage ($V_{CC}$)** | $2.0\text{ V}$ to $6.0\text{ V}$ (74HC) / $4.5\text{ V} \dots 5.5\text{ V}$ (74HCT) |
| **Propagation Delay ($t_{pd}$)** | $11\text{ ns}$ typ ($21\text{ ns}$ max) at $V_{CC} = 5.0\text{ V}$ |
| **Output Drive Current ($I_{OH}/I_{OL}$)**| $\pm 4.0\text{ mA}$ at $5.0\text{ V}$ ($10\text{ LSTTL}$ load fan-out) |
| **Controls** | 1 Common Select ($S$ / $\bar{A}/B$), 1 Common Strobe ($\bar{G}$) |

## Pinout (DIP-16 Package)

```
                            ┌───┴───┐
       (Common Select)  S  1│ 1   16│ VCC (+2V to +6V)
       (Mux 1, Input A) 1A 2│       │15 /G / STROBE (Active-Low)
       (Mux 1, Input B) 1B 3│ 74HC  │14 4A (Mux 4, Input A)
       (Mux 1, Output)  1Y 4│  157  │13 4B (Mux 4, Input B)
       (Mux 2, Input A) 2A 5│ DIP-16│12 4Y (Mux 4, Output)
       (Mux 2, Input B) 2B 6│       │11 3A (Mux 3, Input A)
       (Mux 2, Output)  2Y 7│       │10 3B (Mux 3, Input B)
                   GND  8│       │9  3Y (Mux 3, Output)
                            └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `SELECT` | Digital Input | Common Data Select ($S$ / $\bar{A}/B$); LOW selects $A$ inputs, HIGH selects $B$ inputs |
| 2 | `1A` | Digital Input | Multiplexer 1, Input A |
| 3 | `1B` | Digital Input | Multiplexer 1, Input B |
| 4 | `1Y` | Digital Output | Multiplexer 1, Output |
| 5 | `2A` | Digital Input | Multiplexer 2, Input A |
| 6 | `2B` | Digital Input | Multiplexer 2, Input B |
| 7 | `2Y` | Digital Output | Multiplexer 2, Output |
| 8 | `GND` | Power | Common Ground reference ($0\text{ V}$) |
| 9 | `3Y` | Digital Output | Multiplexer 3, Output |
| 10 | `3B` | Digital Input | Multiplexer 3, Input B |
| 11 | `3A` | Digital Input | Multiplexer 3, Input A |
| 12 | `4Y` | Digital Output | Multiplexer 4, Output |
| 13 | `4B` | Digital Input | Multiplexer 4, Input B |
| 14 | `4A` | Digital Input | Multiplexer 4, Input A |
| 15 | `STROBE` | Digital Input | Active-LOW Common Strobe ($\bar{G}$; tie to GND for normal operation) |
| 16 | `VCC` | Power | Positive Supply Voltage ($+2.0\text{ V}$ to $+6.0\text{ V}$) |

## Function / Truth Table

| Strobe / Enable ($\bar{G}$) | Select ($S$) | Input $A$ ($nA$) | Input $B$ ($nB$) | Output $Y$ ($nY$) |
|---|---|---|---|---|
| **H** | X | X | X | **L** (All outputs forced LOW) |
| **L** | **L** | **L** | X | **L** ($nY = nA$) |
| **L** | **L** | **H** | X | **H** ($nY = nA$) |
| **L** | **H** | X | **L** | **L** ($nY = nB$) |
| **L** | **H** | X | **H** | **H** ($nY = nB$) |

## Typical Application: 4-Bit Nibble Bus Selector

```
     4-Bit Bus A (A3, A2, A1, A0) ────► [Pins 14, 11, 5, 2: 4A, 3A, 2A, 1A]
     4-Bit Bus B (B3, B2, B1, B0) ────► [Pins 13, 10, 6, 3: 4B, 3B, 2B, 1B]
                                               74HC157
     Control Signal (Select A/B) ─────► [Pin 1: SELECT]
     Enable (GND) ────────────────────► [Pin 15: /G]
                                               │
     Selected 4-Bit Bus Output ◄─────── [Pins 12, 9, 7, 4: 4Y, 3Y, 2Y, 1Y]
```

## Comparison: 74HC157 vs 74HC158 vs 74HC257

| IC Part Number | Function | Output Stage | Inverting / Non-Inverting |
|---|---|---|---|
| **74HC157** | **Quad 2-to-1 Multiplexer** | **Standard Push-Pull** | **Non-Inverting ($nY$)** |
| **74HC158** | Quad 2-to-1 Multiplexer | Standard Push-Pull | Inverting ($n\bar{Y}$) |
| **74HC257** | Quad 2-to-1 Multiplexer | 3-State (Tri-State) | Non-Inverting ($nY$) |

## Common mistakes

- **Leaving Strobe Pin 15 ($\bar{G}$) floating:** If $\bar{G}$ is disconnected or pulled HIGH, all four outputs ($1Y \dots 4Y$) are forced to logic LOW. Always tie Pin 15 to **GND (0V)** for continuous multiplexing.
- **Using 74HC157 for bidirectional data buses:** The 74HC157 is strictly a unidirectional multiplexer ($A/B \to Y$). If bidirectional data transmission is needed between buses, use a bus transceiver like the **74HC245**.

## Notes

- **Cascading for 8-Bit / 16-Bit Words:** Two 74HC157 ICs wired with their Select and Strobe pins in parallel create an instant 8-bit wide 2-to-1 byte selector.
