## Overview

The **74HC283** (SN74HC283N) is a 4-bit binary full adder IC with fast internal look-ahead carry generation, manufactured by Texas Instruments, Nexperia, and ON Semiconductor. It adds two 4-bit binary words ($A_1 \dots A_4$ and $B_1 \dots B_4$) plus an incoming carry bit ($C_0$), producing a 4-bit binary sum ($S_1 \dots S_4$) and a final carry-out bit ($C_4$).

Operating from **2.0V to 6.0V DC**, the 74HC283 is a staple logic component in computer architecture educational kits, ALU (Arithmetic Logic Unit) designs, breadboard computers (such as SAP-1 / Ben Eater 8-bit computer builds), and high-speed hardware accumulator circuits.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | 2.0 V to 6.0 V DC |
| **Logic Family** | High-Speed CMOS (74HC) / TTL Compatible (74HCT) |
| **Operand Inputs** | 4-Bit $A$ ($A_1, A_2, A_3, A_4$) & 4-Bit $B$ ($B_1, B_2, B_3, B_4$) |
| **Carry Control** | Carry In ($C_0$) and Carry Out ($C_4$) |
| **Sum Outputs** | 4-Bit Sum ($S_1, S_2, S_3, S_4$) |
| **Propagation Delay** | $16\text{ ns}$ typical at $VCC = 4.5\text{V}$ |
| **Package** | 16-pin DIP / SOIC-16 / TSSOP-16 |

## Pinout (DIP-16 Package)

```
             ┌───┴───┐
          S2 1│ 1   16│ VCC (+2V to +6V)
          B2 2│       │15 B3
          A2 3│ 74HC  │14 A3
          S1 4│  283  │13 S3
          A1 5│       │12 A4
          B1 6│       │11 B4
          C0 7│       │10 S4
         GND 8│       │9  C4 (Carry Out)
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `S2` | Output | Sum Bit 2 Output |
| 2 | `B2` | Input | Operand B Bit 2 Input |
| 3 | `A2` | Input | Operand A Bit 2 Input |
| 4 | `S1` | Output | Sum Bit 1 Output (LSB Sum) |
| 5 | `A1` | Input | Operand A Bit 1 Input (LSB A) |
| 6 | `B1` | Input | Operand B Bit 1 Input (LSB B) |
| 7 | `C0` | Input | Carry In (LSB Carry Input) |
| 8 | `GND` | Power | Ground reference (0 V) |
| 9 | `C4` | Output | Carry Out (MSB Carry Output — Connect to $C_0$ of next 74HC283 for 8-bit adding) |
| 10 | `S4` | Output | Sum Bit 4 Output (MSB Sum) |
| 11 | `B4` | Input | Operand B Bit 4 Input (MSB B) |
| 12 | `A4` | Input | Operand A Bit 4 Input (MSB A) |
| 13 | `S3` | Output | Sum Bit 3 Output |
| 14 | `A3` | Input | Operand A Bit 3 Input |
| 15 | `B3` | Input | Operand B Bit 3 Input |
| 16 | `VCC` | Power | Power Supply (+2.0V to +6.0V DC) |

## Mathematical Operation

The arithmetic addition performed by the chip follows:

$$ (S_4 S_3 S_2 S_1)_2 + 16 \cdot C_4 = (A_4 A_3 A_2 A_1)_2 + (B_4 B_3 B_2 B_1)_2 + C_0 $$

For an 8-bit adder, cascade two 74HC283 chips by connecting $C_4$ of the lower nibble adder to $C_0$ of the upper nibble adder.

## Subtraction Mode (A - B via Two's Complement)

Invert all $B$ inputs ($B_1 \dots B_4$) using XOR gates (`74HC86`) driven by a `SUB` control line, and set $C_0 = 1$. The adder computes $A + \bar{B} + 1 = A - B$.

## Common mistakes

- **Leaving Carry In ($C_0$, Pin 7) floating:** For standard addition, $C_0$ must be tied directly to **GND**. Leaving $C_0$ floating produces incorrect LSB additions.
- **Conflating pinout with older 7483 / 74LS83 chips:** The 74HC283 has a different, optimized pinout arrangement compared to the legacy 7483/74LS83.

## Notes

- **74HC283 vs 74LS283:** 74HC283 is CMOS (low power, 2V-6V supply); 74LS283 is TTL (5V supply only, higher power consumption).
