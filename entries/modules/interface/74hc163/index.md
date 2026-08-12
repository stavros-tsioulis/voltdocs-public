## Overview

The **74HC163** (SN74HC163N) is a high-speed CMOS synchronous 4-bit binary up counter IC manufactured by Texas Instruments, Nexperia, and ON Semiconductor. Unlike ripple counters, all four internal D-type flip-flops change state simultaneously on the rising edge of the master clock (`CLK`), preventing output glitches.

Operating from **2.0V to 6.0V DC**, the 74HC163 features synchronous parallel loading ($\overline{LOAD}$), synchronous master clearing ($\overline{CLR}$), two active-HIGH count enable inputs (`ENP` and `ENT`), and a Ripple Carry Output (`RCO`) for multi-stage synchronous counter cascading.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | 2.0 V to 6.0 V DC |
| **Logic Family** | High-Speed CMOS (74HC) / TTL Compatible (74HCT) |
| **Counting Mode** | Fully Synchronous 4-Bit Binary Up Counter ($Q_A \dots Q_D$, $0000_2 \dots 1111_2$) |
| **Clock Frequency** | Up to $40\text{ MHz}$ at $VCC = 4.5\text{V}$ |
| **Clear Operation** | Synchronous (Clear occurs on next rising `CLK` edge when $\overline{CLR}$ is LOW) |
| **Parallel Load** | Synchronous (Loads inputs $A,B,C,D$ on next rising `CLK` edge when $\overline{LOAD}$ is LOW) |
| **Package** | 16-pin DIP / SOIC-16 / TSSOP-16 |

## Pinout (DIP-16 Package)

```
             ┌───┴───┐
        /CLR 1│ 1   16│ VCC (+2V to +6V)
         CLK 2│       │15 RCO (Ripple Carry Out)
           A 3│ 74HC  │14 QA (LSB Output)
           B 4│  163  │13 QB
           C 5│       │12 QC
           D 6│       │11 QD (MSB Output)
         ENP 7│       │10 ENT
         GND 8│       │9  /LOAD
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `\CLR` | Input | Synchronous Master Clear Input (Active LOW) |
| 2 | `CLK` | Input | Master Clock Input (Triggered on LOW-to-HIGH positive edge) |
| 3 | `A` | Input | Parallel Data Input A (LSB, $2^0 = 1$) |
| 4 | `B` | Input | Parallel Data Input B ($2^1 = 2$) |
| 5 | `C` | Input | Parallel Data Input C ($2^2 = 4$) |
| 6 | `D` | Input | Parallel Data Input D (MSB, $2^3 = 8$) |
| 7 | `ENP` | Input | Parallel Count Enable Input (Active HIGH) |
| 8 | `GND` | Power | Ground reference (0 V) |
| 9 | `\LOAD` | Input | Synchronous Parallel Load Input (Active LOW) |
| 10 | `ENT` | Input | Trickle Count Enable Input (Active HIGH — drives `RCO`) |
| 11–14 | `QD, QC, QB, QA` | Output | 4-Bit Binary Counter Outputs ($Q_A$ LSB, $Q_D$ MSB) |
| 15 | `RCO` | Output | Ripple Carry Output (High when counter reaches $1111_2$ AND `ENT` is HIGH) |
| 16 | `VCC` | Power | Positive Power Supply (+2.0V to +6.0V DC) |

## Function Table

| \CLR | \LOAD | ENP | ENT | CLK | Operation Mode |
|---|---|---|---|---|---|
| Low ($L$) | X | X | X | $\uparrow$ | **Synchronous Reset:** Outputs $Q_A \dots Q_D$ set to $0000_2$ |
| High ($H$) | Low ($L$) | X | X | $\uparrow$ | **Synchronous Preset:** Outputs load inputs $A,B,C,D$ |
| High ($H$) | High ($H$) | High ($H$) | High ($H$) | $\uparrow$ | **Count Up:** Increments binary count ($0 \dots 15$) |
| High ($H$) | High ($H$) | Low ($L$) | X | X | **Inhibit:** Holds current count value |
| High ($H$) | High ($H$) | X | Low ($L$) | X | **Inhibit:** Holds current count value (`RCO` forced LOW) |

## Common mistakes

- **Expecting asynchronous clear like 74HC161:** The 74HC163 has a **synchronous** clear pin ($\overline{CLR}$). Pulling $\overline{CLR}$ LOW does NOT immediately reset the counter outputs to zero until a positive clock edge ($\uparrow$) arrives. For instant asynchronous reset, use the **74HC161** instead.

## Notes

- **74HC163 vs 74HC161 vs 74HC191:** 74HC163 has synchronous clear; 74HC161 has asynchronous clear; 74HC191 is an Up/Down counter.
