## Overview

The **CD4543** (CD4543B / HEF4543B) is a versatile BCD-to-7-segment latch/decoder/driver IC manufactured by Texas Instruments, ON Semiconductor, and Renesas. Unlike the CD4511 (which is restricted to active-HIGH common-cathode LEDs), the CD4543 includes a **Phase control input (`PH`)**, allowing it to drive **Liquid Crystal Displays (LCDs)**, **common-anode LEDs**, or **common-cathode LEDs**.

Operating over **3.0V to 18.0V DC**, the CD4543 converts a 4-bit BCD input ($A, B, C, D$) into a 7-segment display pattern ($a \dots g$). When driving reflective LCD panels, an external AC square wave signal (typically $50\text{ Hz} \dots 100\text{ Hz}$) is applied simultaneously to the LCD backplane and the `PH` pin, providing true AC drive to prevent LCD electrochemical degradation.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VDD - VSS`)** | 3.0 V to 18.0 V DC |
| **Input Format** | 4-bit BCD ($A, B, C, D$) |
| **Display Outputs** | 7 Phase-Controlled outputs ($a \dots g$) |
| **Display Types Supported** | LCD Displays (AC Drive), Common-Cathode LEDs, Common-Anode LEDs |
| **Control Features** | Latch Disable ($LD$), Blanking ($BL$), Phase Control ($PH$) |
| **Package** | 16-pin DIP / SOIC-16 |

## Pinout (DIP-16 Package)

```
             ┌───┴───┐
         LD 1│ 1   16│ VDD (+3V to +18V)
          B 2│       │15 g
          C 3│ CD4543│14 f
          D 4│       │13 e
          A 5│       │12 d
         PH 6│       │11 c
         BL 7│       │10 b
   VSS(GND) 8│       │9  a
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `LD` | Input | Latch Disable Input (High = Pass-through BCD data; Low = Latch stored BCD value) |
| 2 | `B` | Input | BCD Bit 1 Input ($2^1 = 2$) |
| 3 | `C` | Input | BCD Bit 2 Input ($2^2 = 4$) |
| 4 | `D` | Input | BCD Bit 3 Input ($2^3 = 8$, MSB) |
| 5 | `A` | Input | BCD Bit 0 Input ($2^0 = 1$, LSB) |
| 6 | `PH` | Input | Phase Control Input (Connect to AC square wave for LCD backplane, GND for CC LEDs, VDD for CA LEDs) |
| 7 | `BL` | Input | Blanking Input (Active HIGH: High = Turn OFF all segments; Low = Enable display) |
| 8 | `VSS` | Power | Digital Ground (0 V) |
| 9–15 | `a, b, c, d, e, f, g` | Output | 7-Segment Driver Outputs |
| 16 | `VDD` | Power | Positive Power Supply (+3.0V to +18.0V DC) |

## Phase Pin Configuration Matrix

| Target Display Type | `PH` (Pin 6) Connection | Output Logic Level |
|---|---|---|
| **Common-Cathode LED** | Connect `PH` to **GND** | Active-HIGH ($a \dots g$ HIGH turns segment ON) |
| **Common-Anode LED** | Connect `PH` to **`VDD`** | Active-LOW ($a \dots g$ LOW turns segment ON) |
| **Reflective LCD Panel**| Connect `PH` & LCD Backplane to **50Hz Square Wave** | Out-of-phase AC square wave drives segment ON |

## Common mistakes

- **Connecting DC directly to reflective LCD glass:** Direct DC voltage across liquid crystal segments destroys the panel via electrolysis. Always apply an AC square wave to the `PH` pin and LCD backplane.
- **Forgetting that `LD` pin logic is inverse to CD4511 `LE`:** On the CD4543, `LD` is Latch Disable (HIGH = real-time count; LOW = latched memory). On the CD4511, `LE` is Latch Enable (LOW = real-time count; HIGH = latched memory).

## Notes

- **CD4543 vs CD4511:** CD4543 supports LCD panels and common-anode LEDs via phase inversion; CD4511 is limited to active-HIGH common-cathode LEDs.
