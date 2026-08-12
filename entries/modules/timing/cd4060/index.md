## Overview

The **CD4060** (CD4060B / HEF4060B / 74HC4060) is a 14-stage binary ripple counter with an integrated **on-chip oscillator driver circuit** manufactured by Texas Instruments, ON Semiconductor, and Renesas. It combines an oscillator stage (supporting an external RC network or a 32.768 kHz / MHz quartz crystal) with a 14-stage frequency divider inside a single 16-pin package.

Operating from **3.0V to 18.0V DC**, the CD4060 divides the oscillator frequency by up to **16,384 ($2^{14}$)**. Ten outputs are available externally ($Q_4 \dots Q_{10}$ and $Q_{12} \dots Q_{14}$), enabling long-duration electronic timers (seconds to hours), LED flashers, tone generators, and crystal clock sources with no external microcontrollers.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VDD - VSS`)** | 3.0 V to 18.0 V DC (CD4000B) / 2.0V to 6.0V DC (74HC4060) |
| **Oscillator Capability** | Integrated Inverter Driver for RC Networks OR Quartz Crystal Oscillators |
| **Divider Stages** | 14 Binary Stages ($2^1 \dots 2^{14} = 16,384$) |
| **Exposed Outputs** | 10 Stage Outputs ($Q_4, Q_5, Q_6, Q_7, Q_8, Q_9, Q_{10}, Q_{12}, Q_{13}, Q_{14}$) |
| **Missing Outputs** | $Q_1, Q_2, Q_3$, and $Q_{11}$ are NOT exposed externally |
| **Reset Input** | Asynchronous Active-HIGH Master Reset ($RESET$) |
| **Max Clock Frequency** | $12\text{ MHz}$ at $VDD = 15\text{V}$ ($3.5\text{ MHz}$ at $5\text{V}$) |
| **Package** | 16-pin DIP / SOIC-16 |

## Pinout (DIP-16 Package)

```
             ┌───┴───┐
         Q12 1│ 1   16│ VDD (+3V to +18V)
         Q13 2│       │15 Q10
         Q14 3│ CD4060│14 Q8
          Q6 4│       │13 Q9
          Q5 5│       │12 RESET (Master Reset)
          Q7 6│       │11 RS (Oscillator In / Clock In)
          Q4 7│       │10 RTC (R_EXT)
   VSS(GND) 8│       │9  CTC (C_EXT)
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
| 9 | `CTC` | Oscillator | Capacitor Connection Pin for RC Oscillator ($C_X$) |
| 10 | `RTC` | Oscillator | Resistor Connection Pin for RC Oscillator ($R_X$) |
| 11 | `RS` | Oscillator | Oscillator Input Pin / External Clock Input |
| 12 | `RESET` | Input | Master Reset (Active HIGH: High = Reset all outputs to LOW & stop counter) |
| 13 | `Q9` | Output | Stage 9 Output ($\div 512$) |
| 14 | `Q8` | Output | Stage 8 Output ($\div 256$) |
| 15 | `Q10` | Output | Stage 10 Output ($\div 1,024$) |
| 16 | `VDD` | Power | Positive Power Supply (+3.0V to +18.0V DC) |

## Standard RC Oscillator Circuit Configuration

$$ f_{OSC} = \frac{1}{2.3 \times R_X \times C_X} $$

Where $R_{S2} \approx 2 \dots 10 \times R_X$ isolates the timing network:

```
  Pin 9 (CTC) ───[ C_X ]───┬───[ R_X ]─── Pin 10 (RTC) ───[ R_S2 (2*R_X) ]─── Pin 11 (RS)
                           │
                           └─── Timing Node
```

## 32.768 kHz Quartz Crystal Oscillator Application (2 Hz Output)

Connecting a standard $32.768\text{ kHz}$ watch crystal across Pins 10 and 11 produces an ultra-accurate $2.0\text{ Hz}$ square wave on Output **$Q_{14}$ (Pin 3)**:

$$ f_{Q14} = \frac{32,768\text{ Hz}}{2^{14}} = \frac{32,768}{16,384} = 2.0\text{ Hz (0.5 second period)} $$

## Common mistakes

- **Expecting $Q_1, Q_2, Q_3$, or $Q_{11}$ outputs:** These four internal stages are NOT connected to external pins on the CD4060.
- **Leaving `RESET` (Pin 12) ungrounded:** Tie `RESET` to **GND** for continuous oscillation and counting.

## Notes

- **CD4060 vs CD4020 vs NE555:** CD4060 has an integrated oscillator + 14-stage divider for long multi-hour timing; NE555 is limited to shorter timing intervals due to capacitor leakage.
