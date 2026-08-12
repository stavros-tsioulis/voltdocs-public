## Overview

The **CD4040** (CD4040B / HEF4040B / 74HC4040) is a 12-stage binary ripple counter and frequency divider IC manufactured by Texas Instruments, ON Semiconductor, and Renesas. Unlike the CD4020, **all 12 stage outputs ($Q_1$ through $Q_{12}$)** are connected to external IC pins.

Operating from **3.0V to 18.0V DC**, the CD4040 increments its 12-bit binary count on each negative-going clock transition ($\downarrow$). It divides the input clock frequency by powers of 2 ($2^1 = 2$ up to $2^{12} = 4,096$), making it a favourite in audio synthesizers, frequency dividers, and multi-channel timing circuits.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VDD - VSS`)** | 3.0 V to 18.0 V DC (CD4000B) / 2.0V to 6.0V DC (74HC4040) |
| **Divider Stages** | 12 Binary Stages ($2^1 \dots 2^{12} = 4,096$) |
| **Exposed Outputs** | ALL 12 Buffered Outputs ($Q_1, Q_2, Q_3, Q_4, Q_5, Q_6, Q_7, Q_8, Q_9, Q_{10}, Q_{11}, Q_{12}$) |
| **Clock Input Trigger** | Negative-Edge Triggered ($\downarrow$ HIGH-to-LOW transition) |
| **Reset Input** | Asynchronous Active-HIGH Master Reset ($RESET$) |
| **Max Clock Frequency** | $12\text{ MHz}$ at $VDD = 15\text{V}$ ($3.5\text{ MHz}$ at $5\text{V}$) |
| **Package** | 16-pin DIP / SOIC-16 |

## Pinout (DIP-16 Package)

```
             ┌───┴───┐
         Q12 1│ 1   16│ VDD (+3V to +18V)
          Q6 2│       │15 Q11
          Q5 3│ CD4040│14 Q10
          Q7 4│       │13 Q8
          Q4 5│       │12 Q9
          Q3 6│       │11 RESET (Master Reset)
          Q2 7│       │10 /CLK (Clock In)
   VSS(GND) 8│       │9  Q1
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `Q12` | Output | Stage 12 Output ($\div 4,096$, MSB) |
| 2 | `Q6` | Output | Stage 6 Output ($\div 64$) |
| 3 | `Q5` | Output | Stage 5 Output ($\div 32$) |
| 4 | `Q7` | Output | Stage 7 Output ($\div 128$) |
| 5 | `Q4` | Output | Stage 4 Output ($\div 16$) |
| 6 | `Q3` | Output | Stage 3 Output ($\div 8$) |
| 7 | `Q2` | Output | Stage 2 Output ($\div 4$) |
| 8 | `VSS` | Power | Digital Ground (0 V) |
| 9 | `Q1` | Output | Stage 1 Output ($\div 2$, LSB) |
| 10 | `\CLK` | Input | Master Clock Input (Negative-edge triggered $\downarrow$) |
| 11 | `RESET` | Input | Master Reset (Active HIGH: High = Reset all outputs to LOW) |
| 12 | `Q9` | Output | Stage 9 Output ($\div 512$) |
| 13 | `Q8` | Output | Stage 8 Output ($\div 256$) |
| 14 | `Q10` | Output | Stage 10 Output ($\div 1,024$) |
| 15 | `Q11` | Output | Stage 11 Output ($\div 2,048$) |
| 16 | `VDD` | Power | Positive Power Supply (+3.0V to +18.0V DC) |

## Frequency Division Ratios

| Stage Pin | Binary Power | Division Factor | Example ($f_{CLK} = 1.0\text{ MHz}$) |
|---|---|---|---|
| $Q_1$ (Pin 9) | $2^1$ | $\div 2$ | $500.0\text{ kHz}$ |
| $Q_2$ (Pin 7) | $2^2$ | $\div 4$ | $250.0\text{ kHz}$ |
| $Q_3$ (Pin 6) | $2^3$ | $\div 8$ | $125.0\text{ kHz}$ |
| $Q_4$ (Pin 5) | $2^4$ | $\div 16$ | $62.5\text{ kHz}$ |
| $Q_{12}$ (Pin 1)| $2^{12}$ | $\div 4,096$ | $244.14\text{ Hz}$ |

## Common mistakes

- **Assuming positive-edge clocking:** The CD4040 triggers on **falling clock edges** ($\downarrow$).
- **Leaving `RESET` (Pin 11) ungrounded:** `RESET` is active-HIGH. Connect `RESET` to **GND** to enable counting.

## Notes

- **CD4040 vs CD4020:** CD4040 exposes all 12 stage outputs ($Q_1 \dots Q_{12}$); CD4020 is a 14-stage counter but omits $Q_2$ and $Q_3$.
