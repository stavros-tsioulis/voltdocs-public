## Overview

The **CD4028** (CD4028B / HEF4028B) is a BCD-to-decimal and 3-bit binary-to-octal decoder IC manufactured by Texas Instruments, ON Semiconductor, and Renesas. It decodes a 4-bit Binary Coded Decimal (BCD) code ($A, B, C, D$) into one of ten mutually exclusive active-HIGH outputs (`Q0` through `Q9`).

Operating over a wide CMOS supply range of **3.0V to 18.0V DC**, the CD4028 is widely used in digital clock counter decoding, 1-of-10 line selection, relay multiplexing, and driving high-voltage Nixie tube driver transistors (such as MPSA42 NPNs).

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VDD - VSS`)** | 3.0 V to 18.0 V DC |
| **Input Format** | 4-bit BCD ($A, B, C, D$ — LSB to MSB) |
| **Output Lines** | 10 Mutually Exclusive Active-HIGH Outputs (`Q0` to `Q9`) |
| **Octal Mode** | 3-bit Binary ($A, B, C$) to 8 Octal Outputs (`Q0` to `Q7`) when $D = 0$ |
| **Propagation Delay** | $80\text{ ns}$ typical at $VDD = 10\text{V}$ |
| **Noise Immunity** | $0.45 \times VDD$ typical |
| **Package** | 16-pin DIP / SOIC-16 |

## Pinout (DIP-16 Package)

```
             ┌───┴───┐
         Q4 1│ 1   16│ VDD (+3V to +18V)
         Q2 2│       │15 Q3
         Q0 3│ CD4028│14 Q1
         Q7 4│       │13 D (BCD Bit 3 / MSB)
         Q9 5│       │12 C (BCD Bit 2)
         Q5 6│       │11 B (BCD Bit 1)
         Q6 7│       │10 A (BCD Bit 0 / LSB)
   VSS(GND) 8│       │9  Q8
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 3 | `Q0` | Output | Decimal 0 Output (Active HIGH) |
| 14 | `Q1` | Output | Decimal 1 Output (Active HIGH) |
| 2 | `Q2` | Output | Decimal 2 Output (Active HIGH) |
| 15 | `Q3` | Output | Decimal 3 Output (Active HIGH) |
| 1 | `Q4` | Output | Decimal 4 Output (Active HIGH) |
| 6 | `Q5` | Output | Decimal 5 Output (Active HIGH) |
| 7 | `Q6` | Output | Decimal 6 Output (Active HIGH) |
| 4 | `Q7` | Output | Decimal 7 Output (Active HIGH) |
| 9 | `Q8` | Output | Decimal 8 Output (Active HIGH) |
| 5 | `Q9` | Output | Decimal 9 Output (Active HIGH) |
| 8 | `VSS` | Power | Digital Ground (0 V) |
| 10 | `A` | Input | BCD Bit 0 Input ($2^0 = 1$, LSB) |
| 11 | `B` | Input | BCD Bit 1 Input ($2^1 = 2$) |
| 12 | `C` | Input | BCD Bit 2 Input ($2^2 = 4$) |
| 13 | `D` | Input | BCD Bit 3 Input ($2^3 = 8$, MSB) |
| 16 | `VDD` | Power | Positive Power Supply (+3.0V to +18.0V DC) |

## Decoded Truth Table

| $D$ (MSB) | $C$ | $B$ | $A$ (LSB) | Active Output (HIGH) | All Other Outputs |
|---|---|---|---|---|---|
| $0$ | $0$ | $0$ | $0$ | **`Q0`** | LOW ($0\text{V}$) |
| $0$ | $0$ | $0$ | $1$ | **`Q1`** | LOW ($0\text{V}$) |
| $0$ | $0$ | $1$ | $0$ | **`Q2`** | LOW ($0\text{V}$) |
| $0$ | $0$ | $1$ | $1$ | **`Q3`** | LOW ($0\text{V}$) |
| $0$ | $1$ | $0$ | $0$ | **`Q4`** | LOW ($0\text{V}$) |
| $0$ | $1$ | $0$ | $1$ | **`Q5`** | LOW ($0\text{V}$) |
| $0$ | $1$ | $1$ | $0$ | **`Q6`** | LOW ($0\text{V}$) |
| $0$ | $1$ | $1$ | $1$ | **`Q7`** | LOW ($0\text{V}$) |
| $1$ | $0$ | $0$ | $0$ | **`Q8`** | LOW ($0\text{V}$) |
| $1$ | $0$ | $0$ | $1$ | **`Q9`** | LOW ($0\text{V}$) |
| $> 1001_2$ ($10\dots15$) | Invalid BCD | None (All outputs LOW) | LOW ($0\text{V}$) |

## Common mistakes

- **Invalid BCD inputs ($D,C,B,A > 1001_2$):** When BCD inputs exceed 9 (i.e. binary $1010_2 \dots 1111_2$), all ten outputs (`Q0`–`Q9`) remain LOW ($0\text{V}$). Ensure input counters are BCD decade counters (like CD4017 or CD4553).

## Notes

- **CD4028 vs 74HC42:** CD4028 is CMOS (3V to 18V supply); 74HC42 is a 5V BCD-to-decimal decoder with active-LOW outputs.
