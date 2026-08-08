## Overview

The **TM1637** is an LED drive control circuit manufactured by Titan Micro Electronics. It integrates a 2-wire serial interface, an internal MCU digital interface, data latches, LED high-voltage drive, and a keyboard scanning circuit.

It is universally used to drive 4-digit 0.36" and 0.56" 7-segment LED display modules featuring a central clock colon (`:`) or decimal points. The TM1637 requires only two signal pins (`CLK` and `DIO`) to communicate with a microcontroller and provides 8 selectable LED brightness levels via internal PWM pulse duty control.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.5 V DC (5 V nominal) |
| **Display capacity** | Up to 6 digits $\times$ 8 segments (4 digits typical on breakout) |
| **Interface** | Custom 2-wire serial bus (`CLK`, `DIO`) |
| **Brightness control** | 8-level pulse width modulation (PWM) duty cycle control |
| **Keyboard matrix** | $8 \times 2$ key-scan matrix input (16 keys) |
| **Peak segment current** | 50 mA per segment |
| **Quiescent current** | $< 1\text{ mA}$ |

## Pinout

### Standard 4-Pin Module Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` | Power | Ground (0 V) |
| 2 | `VCC` | Power | Supply voltage (+3.3 V to +5.5 V DC) |
| 3 | `DIO` | Digital I/O | Serial Data Input/Output line (requires pull-up resistor) |
| 4 | `CLK` | Digital Input | Serial Clock input line |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 3.3 | 5.0 | 5.5 | V | DC |
| Logic Input High Voltage | $V_{IH}$ | $0.7 V_{DD}$ | — | $V_{DD}$ | V | `CLK`, `DIO` |
| Logic Input Low Voltage | $V_{IL}$ | 0 | — | $0.3 V_{DD}$ | V | `CLK`, `DIO` |
| Segment Sink Current | $I_{OL1}$ | 30 | 50 | 80 | mA | $V_{DS} = 0.5\text{ V}$, segment ON |
| Grid Source Current | $I_{OH1}$ | 20 | 35 | 50 | mA | $V_{DS} = V_{DD} - 2.0\text{ V}$, grid ON |
| Maximum Clock Frequency | $f_{CLK}$ | — | 250 | 500 | kHz | `CLK` pin pulse rate |

## Communication protocol & Command set

The TM1637 uses a custom I2C-like 2-wire serial protocol (without I2C slave addressing). Data is transmitted LSB first.

### Data Command Set

| Command Byte | Description |
|---|---|
| `0x40` | Write data to display register (Automatic address incrementing) |
| `0x44` | Write data to display register (Fixed address mode) |
| `0x42` | Read keyboard matrix data |
| `0xC0` to `0xC5` | Set display memory address (Digit 1 = `0xC0`, Digit 2 = `0xC1`, etc.) |
| `0x80` to `0x87` | Display OFF (`0x80`) / Display ON with brightness levels 1 to 8 (`0x88`–`0x8F`) |

### 7-Segment Encoding Table (Common Anode)

Bit mapping: `[DP/Colon, g, f, e, d, c, b, a]`

| Character | Segment Byte (Hex) | Character | Segment Byte (Hex) |
|---|---|---|---|
| `0` | `0x3F` | `5` | `0x6D` |
| `1` | `0x06` | `6` | `0x7D` |
| `2` | `0x5B` | `7` | `0x07` |
| `3` | `0x4F` | `8` | `0x7F` |
| `4` | `0x66` | `9` | `0x6F` |

## Wiring

| TM1637 Module Pin | → | Microcontroller (Arduino Uno / ESP32) |
|---|---|---|
| `GND` | | `GND` |
| `VCC` | | `5V` (or `3.3V`) |
| `DIO` | | Digital Output Pin (e.g. GPIO2) |
| `CLK` | | Digital Output Pin (e.g. GPIO3) |

> [!NOTE]
> Standard TM1637 modules incorporate $10\text{ k}\Omega$ pull-up resistors on `CLK` and `DIO`, along with $100\text{ pF}$ filtering capacitors. If communicating at speeds above 250 kHz, ensure clock signal pulse widths are at least 2 µs.

## Common mistakes

- **Treating TM1637 as a standard I2C device:** Although `CLK` and `DIO` resemble I2C, TM1637 does NOT use 7-bit slave addresses (`0x00`–`0x7F`). Standard I2C libraries (e.g. `Wire.h`) will not work.
- **Forgetting to send Display Control command (`0x88`..`0x8F`):** Writing segment data to `0xC0`–`0xC3` alone will not turn on the display. Software MUST send the Display ON command (e.g. `0x8F` for max brightness) after updating memory.
- **Clock colon control on 4-digit modules:** The central colon (`:`) is typically wired to the Decimal Point (DP - Bit 7) of Digit 2 (`0xC1`). Setting bit 7 to `1` on Digit 2 illuminates the colon.

## Notes

- Low power consumption allows direct USB or battery operation.
