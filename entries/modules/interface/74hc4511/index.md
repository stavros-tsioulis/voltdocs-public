## Overview

The **74HC4511** (CD74HC4511E) is a high-speed CMOS BCD-to-7-segment latch/decoder/driver IC manufactured by Texas Instruments, Nexperia, and ON Semiconductor. It accepts a 4-bit Binary Coded Decimal (BCD) input ($A, B, C, D$) and decodes it into active-HIGH signals ($a, b, c, d, e, f, g$) to drive common-cathode 7-segment LED displays directly.

Operating over **2.0V to 6.0V DC**, the 74HC4511 features internal 4-bit data storage latches, a Lamp Test input ($\overline{LT}$ — turns on all 7 segments for display testing), and a Blanking input ($\overline{BL}$ — turns off all segments for power saving or PWM dimming).

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | 2.0 V to 6.0 V DC |
| **Logic Family** | High-Speed CMOS (74HC) / TTL Compatible (74HCT) |
| **Input Format** | 4-bit BCD ($A, B, C, D$ — LSB to MSB) |
| **Output Drive** | 7 Active-HIGH outputs ($a \dots g$, up to $25\text{ mA}$ source current per segment) |
| **Display Type** | Common-Cathode 7-Segment LED Displays |
| **Control Pin Features** | Latch Enable ($\overline{LE}$), Lamp Test ($\overline{LT}$), Blanking ($\overline{BL}$) |
| **Package** | 16-pin DIP / SOIC-16 / TSSOP-16 |

## Pinout (DIP-16 Package)

```
             ┌───┴───┐
          B 1│ 1   16│ VCC (+2V to +6V)
          C 2│       │15 f
        /LT 3│ 74HC  │14 g
        /BL 4│ 4511  │13 a
        /LE 5│       │12 b
          D 6│       │11 c
          A 7│       │10 d
        GND 8│       │9  e
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
| 8 | `GND` | Power | Ground reference (0 V) |
| 9–15 | `e, d, c, b, a, g, f` | Output | 7-Segment Active-HIGH LED Driver Outputs |
| 16 | `VCC` | Power | Positive Power Supply (+2.0V to +6.0V DC) |

## Truth Table & Decoded Output Numbers

| BCD Input ($D,C,B,A$) | Decoded Digit | Active Segments ($a \dots g$) |
|---|---|---|
| $0000_2$ ($0$) | `0` | $a, b, c, d, e, f$ (HIGH) |
| $0001_2$ ($1$) | `1` | $b, c$ (HIGH) |
| $0010_2$ ($2$) | `2` | $a, b, d, e, g$ (HIGH) |
| $0011_2$ ($3$) | `3` | $a, b, c, d, g$ (HIGH) |
| $0100_2$ ($4$) | `4` | $b, c, f, g$ (HIGH) |
| $0101_2$ ($5$) | `5` | $a, c, d, f, g$ (HIGH) |
| $0110_2$ ($6$) | `6` | $a, c, d, e, f, g$ (HIGH) |
| $0111_2$ ($7$) | `7` | $a, b, c$ (HIGH) |
| $1000_2$ ($8$) | `8` | $a, b, c, d, e, f, g$ (HIGH) |
| $1001_2$ ($9$) | `9` | $a, b, c, d, f, g$ (HIGH) |
| $> 1001_2$ ($10\dots15$) | Blank | All segments OFF ($a \dots g$ LOW) |

## Common mistakes

- **Leaving $\overline{LT}$, $\overline{BL}$, or $\overline{LE}$ floating:** Control pins $\overline{LT}$ (Pin 3) and $\overline{BL}$ (Pin 4) **must be tied to $V_{CC}$** for normal display operation. Pin $\overline{LE}$ (Pin 5) **must be tied to GND**. Leaving them floating causes dark or blank displays.
- **Connecting to Common-Anode displays:** The 74HC4511 has **active-HIGH** outputs, meant to drive **Common-Cathode** 7-segment displays. Connect current-limiting resistors ($220\ \Omega \dots 470\ \Omega$) between outputs $a \dots g$ and the display pins.

## Notes

- **74HC4511 vs CD4511:** 74HC4511 operates on 2V to 6V logic levels at high speed; CD4511 operates on 3V to 18V CMOS power rails.
