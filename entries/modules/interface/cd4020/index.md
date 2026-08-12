## Overview

The **CD4020** (CD4020B / HEF4020B / 74HC4020) is a 14-stage binary ripple counter and frequency divider IC manufactured by Texas Instruments, ON Semiconductor, and Renesas. It advances its internal binary count on each negative-going edge ($\downarrow$) of the master clock input ($\overline{CLK}$).

Operating over **3.0V to 18.0V DC** (CD4000B series), the CD4020 divides the input clock frequency by powers of 2 ($2^1$ to $2^{14} = 16,384$). Twelve of the 14 stages are available on external pins ($Q_1$ and $Q_4$ through $Q_{14}$), making it ideal for long-period digital timers, clock prescalers, and frequency synthesizers.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VDD - VSS`)** | 3.0 V to 18.0 V DC (CD4000B) / 2.0V to 6.0V DC (74HC4020) |
| **Divider Stages** | 14 Binary Stages ($2^1 \dots 2^{14} = 16,384$) |
| **Exposed Outputs** | 12 Buffered Outputs ($Q_1, Q_4, Q_5, Q_6, Q_7, Q_8, Q_9, Q_{10}, Q_{11}, Q_{12}, Q_{13}, Q_{14}$) |
| **Missing Outputs** | $Q_2$ ($2^2 = 4$) and $Q_3$ ($2^3 = 8$) are NOT exposed externally |
| **Clock Input Trigger** | Negative-Edge Triggered ($\downarrow$ HIGH-to-LOW transition) |
| **Reset Input** | Asynchronous Active-HIGH Master Reset ($RESET$) |
| **Max Clock Frequency** | $12\text{ MHz}$ at $VDD = 15\text{V}$ ($3.5\text{ MHz}$ at $5\text{V}$) |
| **Package** | 16-pin DIP / SOIC-16 |

## Pinout (DIP-16 Package)

```
             ┌───┴───┐
         Q12 1│ 1   16│ VDD (+3V to +18V)
         Q13 2│       │15 Q9
         Q14 3│ CD4020│14 Q8
          Q6 4│       │13 NC (Q3 internal)
          Q5 5│       │12 NC (Q2 internal)
          Q7 6│       │11 RESET (Master Reset)
          Q4 7│       │10 /CLK (Clock In)
   VSS(GND) 8│       │9  Q1
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `Q12` | Output | Stage 12 Output ($\div 4,096$) |
| 2 | `Q13` | Output | Stage 13 Output ($\div 8,192$) |
| 3 | `Q14` | Output | Stage 14 Output ($\div 16,384$) |
| 4 | `Q6` | Output | Stage 6 Output ($\div 64$) |
| 5 | `Q5` | Output | Stage 5 Output ($\div 32$) |
| 6 | `Q7` | Output | Stage 7 Output ($\div 128$) |
| 7 | `Q4` | Output | Stage 4 Output ($\div 16$) |
| 8 | `VSS` | Power | Digital Ground (0 V) |
| 9 | `Q1` | Output | Stage 1 Output ($\div 2$) |
| 10 | `\CLK` | Input | Master Clock Input (Negative-edge triggered $\downarrow$) |
| 11 | `RESET` | Input | Master Reset (Active HIGH: High = Reset all stages to LOW) |
| 12, 13 | `NC` | Unused | Internal $Q_2$ and $Q_3$ stages (Not brought out to pins) |
| 14 | `Q8` | Output | Stage 8 Output ($\div 256$) |
| 15 | `Q9` | Output | Stage 9 Output ($\div 512$) |
| 16 | `VDD` | Power | Positive Power Supply (+3.0V to +18.0V DC) |

## Frequency Division Table

| Output Pin | Division Ratio ($2^N$) | Output Frequency ($f_{CLK} = 32.768\text{ kHz}$) |
|---|---|---|
| $Q_1$ (Pin 9) | $\div 2$ | $16.384\text{ kHz}$ |
| $Q_4$ (Pin 7) | $\div 16$ | $2.048\text{ kHz}$ |
| $Q_8$ (Pin 14) | $\div 256$ | $128\text{ Hz}$ |
| $Q_{14}$ (Pin 3) | $\div 16,384$ | $2.0\text{ Hz}$ |

## Common mistakes

- **Expecting $Q_2$ or $Q_3$ outputs:** Pins 12 and 13 on the CD4020 are No Connection (NC). If your design requires division by 4 ($Q_2$) or division by 8 ($Q_3$), use the **CD4040** instead.
- **Leaving `RESET` (Pin 11) floating:** `RESET` is active-HIGH. Tie `RESET` to **GND** for normal counting.

## Notes

- **CD4020 vs CD4040 vs CD4060:** CD4020 is a 14-stage counter (omits $Q_2, Q_3$); CD4040 is a 12-stage counter (all 12 outputs exposed); CD4060 is a 14-stage counter with an integrated on-chip oscillator driver circuit.
