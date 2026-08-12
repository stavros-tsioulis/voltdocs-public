## Overview

The **CD4511** (CD4511B / HEF4511B) is a classic BCD-to-7-segment latch/decoder/driver IC manufactured by Texas Instruments, ON Semiconductor, and Renesas. Designed to operate across a wide supply voltage range of **3.0V to 18.0V DC**, it incorporates internal bipolar NPN transistor drivers that supply up to **25 mA per segment** directly to common-cathode 7-segment LED displays.

Features include 4-bit BCD input latches ($A, B, C, D$), an active-LOW Lamp Test input ($\overline{LT}$ — lights up all 7 segments for display verification), and an active-LOW Blanking input ($\overline{BL}$ — turns off all segments for zero-suppression or PWM intensity control).

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VDD - VSS`)** | 3.0 V to 18.0 V DC |
| **Input Format** | 4-bit BCD ($A, B, C, D$ — LSB to MSB) |
| **Output Drive** | 7 Active-HIGH outputs ($a \dots g$, up to $25\text{ mA}$ source current per segment at $VDD = 15\text{V}$) |
| **Display Type** | Common-Cathode 7-Segment LED Displays |
| **Control Features** | Latch Enable ($\overline{LE}$), Lamp Test ($\overline{LT}$), Blanking ($\overline{BL}$) |
| **Package** | 16-pin DIP / SOIC-16 |

## Pinout (DIP-16 Package)

```
             ┌───┴───┐
          B 1│ 1   16│ VDD (+3V to +18V)
          C 2│       │15 f
        /LT 3│ CD4511│14 g
        /BL 4│       │13 a
        /LE 5│       │12 b
          D 6│       │11 c
          A 7│       │10 d
   VSS(GND) 8│       │9  e
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `B` | Input | BCD Bit 1 Input ($2^1 = 2$) |
| 2 | `C` | Input | BCD Bit 2 Input ($2^2 = 4$) |
| 3 | `\LT` | Input | Lamp Test Input (Active LOW: Low = Turn ON all segments $a \dots g$) |
| 4 | `\BL` | Input | Blanking Input (Active LOW: Low = Turn OFF all segments $a \dots g$) |
| 5 | `\LE` | Input | Latch Enable Input (Active LOW: Low = Pass-through; High = Latch BCD data) |
| 6 | `D` | Input | BCD Bit 3 Input ($2^3 = 8$, MSB) |
| 7 | `A` | Input | BCD Bit 0 Input ($2^0 = 1$, LSB) |
| 8 | `VSS` | Power | Digital Ground (0 V) |
| 9–15 | `e, d, c, b, a, g, f` | Output | 7-Segment Active-HIGH LED Driver Outputs |
| 16 | `VDD` | Power | Positive Power Supply (+3.0V to +18.0V DC) |

## Application Notes

- **Current-Limiting Resistors:** Always insert $220\ \Omega \dots 1\text{ k}\Omega$ series current-limiting resistors between pins $a \dots g$ and the common-cathode 7-segment display.
- **Unused BCD inputs ($A, B, C, D$):** Tie unused inputs to $V_{SS}$ (GND) or $V_{DD}$.

## Common mistakes

- **Leaving $\overline{LT}$ or $\overline{BL}$ un-connected:** Control pins $\overline{LT}$ and $\overline{BL}$ are active-LOW inputs. Leaving them ungrounded or floating causes blank displays. Tie both $\overline{LT}$ and $\overline{BL}$ to **`VDD`** for normal operation.

## Notes

- **CD4511 vs CD4055 / CD4543:** CD4511 is designed specifically for active-HIGH common-cathode LED displays; CD4543 is designed with a phase input for driving LCDs and common-anode displays.
