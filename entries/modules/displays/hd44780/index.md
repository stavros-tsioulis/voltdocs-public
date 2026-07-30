## Overview

The **HD44780** (and its updated revision **HD44780U**) is an industry-standard dot-matrix liquid crystal display (LCD) controller and driver IC developed by Hitachi. It handles character generation, display refresh, and internal RAM management for alphanumeric displays, most commonly **16x2** (16 characters, 2 lines) and **20x4** modules.

The controller includes an integrated Character Generator ROM (CGROM) containing 208 $5 \times 8$ dot font characters, a Character Generator RAM (CGRAM) for 8 custom user-defined characters, and a Display Data RAM (DDRAM) storing up to 80 characters of display text.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 4.5 V – 5.5 V (typically 5.0 V) |
| **Logic level** | 5V TTL compatible |
| **Display format** | 16x2 or 20x4 alphanumeric characters |
| **Interface** | 4-bit / 8-bit parallel, or I2C via PCF8574 backpack |
| **Current draw** | 1.5 mA (IC only, excluding LED backlight ~100–120 mA) |
| **Character fonts** | 208 $5\times8$ characters in CGROM + 8 custom $5\times8$ in CGRAM |

## Pinout

### Standard 16-Pin Parallel Interface

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VSS` | Power | Ground (0 V) |
| 2 | `VDD` | Power | Supply voltage (+5 V) |
| 3 | `V0` | Analog Input | Contrast adjust (0 V to 5 V via 10 kΩ potentiometer) |
| 4 | `RS` | Digital Input | Register Select (`LOW`: Instruction register, `HIGH`: Data register) |
| 5 | `RW` | Digital Input | Read/Write select (`LOW`: Write to LCD, `HIGH`: Read from LCD) |
| 6 | `E` | Digital Input | Enable signal (falling-edge latch for data/commands) |
| 7 | `DB0` | Digital I/O | Data bus bit 0 (Unused in 4-bit mode) |
| 8 | `DB1` | Digital I/O | Data bus bit 1 (Unused in 4-bit mode) |
| 9 | `DB2` | Digital I/O | Data bus bit 2 (Unused in 4-bit mode) |
| 10 | `DB3` | Digital I/O | Data bus bit 3 (Unused in 4-bit mode) |
| 11 | `DB4` | Digital I/O | Data bus bit 4 |
| 12 | `DB5` | Digital I/O | Data bus bit 5 |
| 13 | `DB6` | Digital I/O | Data bus bit 6 |
| 14 | `DB7` | Digital I/O | Data bus bit 7 |
| 15 | `LED+` / `A` | Power | Backlight Anode (+5 V via current-limiting resistor) |
| 16 | `LED-` / `K` | Power | Backlight Cathode (GND) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Operating Voltage | `VDD` | 4.5 | 5.0 | 5.5 | V | Standard supply |
| Supply Current | `IDD` | — | 1.5 | 3.0 | mA | $V_{DD} = 5.0\text{ V}$, no backlight |
| High-level Input Voltage | `VIH` | 2.2 | — | `VDD` | V | TTL compatible |
| Low-level Input Voltage | `VIL` | -0.3 | — | 0.6 | V | TTL compatible |
| Enable Pulse Width | `PWEH` | 450 | — | — | ns | High period for `E` pulse |
| Enable Rise/Fall Time | `tEr`, `tEf` | — | — | 25 | ns | Data latch timing |

## Instruction set

HD44780 accepts commands when `RS = 0` and `RW = 0`. Data is latched on the **falling edge** of the Enable (`E`) pin.

| Instruction | RS | RW | DB7 | DB6 | DB5 | DB4 | DB3 | DB2 | DB1 | DB0 | Description | Execution Time |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Clear Display | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Clears DDRAM and sets DDRAM address 0 in address counter | 1.52 ms |
| Return Home | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | * | Sets DDRAM address 0 and returns display to original position | 1.52 ms |
| Entry Mode Set | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | I/D | S | Sets cursor move direction (`I/D`) and spec. display shift (`S`) | 37 µs |
| Display ON/OFF | 0 | 0 | 0 | 0 | 0 | 0 | 1 | D | C | B | Sets Display (`D`), Cursor (`C`), and Blink (`B`) ON/OFF | 37 µs |
| Cursor/Shift | 0 | 0 | 0 | 0 | 0 | 1 | S/C | R/L | * | * | Shifts display or moves cursor without changing DDRAM | 37 µs |
| Function Set | 0 | 0 | 0 | 0 | 1 | DL | N | F | * | * | Sets Data Length (`DL`: 8/4 bit), Lines (`N`: 2/1 line), Font (`F`) | 37 µs |
| Set CGRAM Addr | 0 | 0 | 0 | 1 | AGC | AGC | AGC | AGC | AGC | AGC | Sets CGRAM address | 37 µs |
| Set DDRAM Addr | 0 | 0 | 1 | ADD | ADD | ADD | ADD | ADD | ADD | ADD | Sets DDRAM address (Line 1: `0x00`–`0x27`, Line 2: `0x40`–`0x67`) | 37 µs |

## Wiring

### 4-Bit Parallel Mode (Arduino Uno)

| HD44780 Pin | → | Arduino Uno Pin | Notes |
|---|---|---|---|
| 1 (`VSS`) | | `GND` | Ground |
| 2 (`VDD`) | | `5V` | Power |
| 3 (`V0`) | | Potentiometer Wiper | 10 kΩ pot between 5V and GND for contrast control |
| 4 (`RS`) | | Pin `12` | Register Select |
| 5 (`RW`) | | `GND` | Tied to GND for Write-only mode |
| 6 (`E`) | | Pin `11` | Enable |
| 11 (`DB4`) | | Pin `5` | Data Bit 4 |
| 12 (`DB5`) | | Pin `4` | Data Bit 5 |
| 13 (`DB6`) | | Pin `3` | Data Bit 6 |
| 14 (`DB7`) | | Pin `2` | Data Bit 7 |
| 15 (`LED+`) | | `5V` | Backlight Anode |
| 16 (`LED-`) | | `GND` | Backlight Cathode |

> [!INFO]
> When using an I2C backpack (PCF8574 expansion board soldered to the LCD), the 16-pin interface is converted to a 4-pin I2C interface (`VCC`, `GND`, `SDA`, `SCL`) with default I2C address `0x27` or `0x3F`.

## Common mistakes

- **Blank screen / Solid black blocks:** The contrast pin (`V0`) is floating or set incorrectly. Adjust the 10 kΩ potentiometer connected to pin 3 until characters become visible.
- **Incorrect line addresses:** Line 1 DDRAM addresses start at `0x00`, while Line 2 DDRAM addresses start at `0x40` (not `0x10`). On 20x4 displays, Line 3 starts at `0x14` and Line 4 starts at `0x54`.
- **Missing initialization delays:** The HD44780 requires a strict startup timing sequence (>15 ms after $V_{DD}$ reaches 4.5 V) before receiving initialization instructions.

## Notes

- **Custom Characters:** Up to 8 custom characters can be stored in CGRAM (addresses `0x00`–`0x07`). Each character is defined as an 8-byte array representing $5 \times 8$ pixel patterns.
