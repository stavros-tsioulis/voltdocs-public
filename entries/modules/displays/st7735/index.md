## Overview

The **ST7735** (and its variants ST7735S / ST7735R) is a single-chip controller/driver for 262K-color graphic TFT-LCD displays manufactured by Sitronix Technology. It is widely used on **1.8-inch 128x160** and **0.96-inch 80x160** color TFT screen modules.

The controller integrates a 132RGB x 162 frame memory buffer, display timing generator, and power supply circuits. Communication occurs over a fast 4-wire serial peripheral interface (SPI) with support for 16-bit RGB565 color depth (65,536 colors).

## Quick reference

| | |
|---|---|
| **Module VCC** | 3.3 V to 5.0 V DC (onboard LDO) |
| **Chip VDD / VDDIO** | 2.3 V to 3.3 V DC |
| **Resolution** | $128 \times 160$ pixels (or $80 \times 160$ pixels) |
| **Color Depth** | 16-bit RGB565 (65,536 colors) or 18-bit RGB666 (262,144 colors) |
| **Communication interface** | 4-wire SPI (`SCL`, `SDA`, `CS`, `DC`, `RES`) |
| **Maximum SPI Clock** | 15 MHz |
| **LED Backlight Supply** | 3.3 V DC (draws ~40 mA) |

## Pinout

### Standard 8-Pin 1.8-inch TFT Module Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` | Power | Ground (0 V) |
| 2 | `VCC` | Power | Supply voltage (+3.3 V to +5.0 V DC) |
| 3 | `SCL` / `SCK` | Digital Input | SPI Clock input line |
| 4 | `SDA` / `MOSI` | Digital Input | SPI Data Input line |
| 5 | `RES` / `RST` | Digital Input | Active-LOW Hardware Reset line |
| 6 | `DC` / `A0` | Digital Input | Data / Command control pin (`LOW` = Command, `HIGH` = Data) |
| 7 | `CS` | Digital Input | SPI Chip Select line (Active-LOW) |
| 8 | `BLK` / `LED` | Power / PWM | LED Backlight power control (`HIGH` / `3.3V` = Backlight ON, PWM for dimming) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{CC}$ | 3.3 | 5.0 | 5.5 | V | DC |
| Supply Voltage (Chip) | $V_{DD}$ | 2.3 | 2.8 | 3.3 | V | DC |
| Logic High Input | $V_{IH}$ | $0.7 V_{DD}$ | — | $V_{DD}$ | V | `SCL`, `SDA`, `DC`, `CS` |
| Logic Low Input | $V_{IL}$ | 0 | — | $0.3 V_{DD}$ | V | `SCL`, `SDA`, `DC`, `CS` |
| Driver Operating Current | $I_{DD}$ | — | 10 | 15 | mA | Normal display operation |
| Backlight Current | $I_{LED}$ | — | 40 | 50 | mA | $V_{LED} = 3.3\text{ V}$ |

## Key Command Table

| Address Hex | Command Name | Description |
|---|---|---|
| `0x01` | `SWRESET` | Software Reset command |
| `0x11` | `SLPOUT` | Sleep Out (Turn on internal charge pump oscillator) |
| `0x29` | `DISPON` | Display ON command |
| `0x2A` | `CASET` | Column Address Set ($X_{start}$ to $X_{end}$) |
| `0x2B` | `RASET` | Row Address Set ($Y_{start}$ to $Y_{end}$) |
| `0x2C` | `RAMWR` | Memory Write (Stream 16-bit RGB565 pixel color data) |
| `0x36` | `MADCTL` | Memory Data Access Control (Orientation, BGR/RGB color order) |
| `0x3A` | `COLMOD` | Interface Pixel Format (`0x05` = 16-bit RGB565) |

## Wiring

| ST7735 Module Pin | → | Microcontroller (Arduino Uno / ESP32) | Notes |
|---|---|---|---|
| `GND` | | `GND` | Ground |
| `VCC` | | `5V` (or `3.3V`) | Module power supply |
| `SCL` | | SPI `SCK` (D13 on Uno / GPIO18 on ESP32) | SPI Clock |
| `SDA` | | SPI `MOSI` (D11 on Uno / GPIO23 on ESP32) | SPI Master Output |
| `RES` | | GPIO Pin (e.g. D8 on Uno / GPIO4 on ESP32) | Reset pin |
| `DC` | | GPIO Pin (e.g. D9 on Uno / GPIO2 on ESP32) | Data/Command pin |
| `CS` | | SPI `SS` (e.g. D10 on Uno / GPIO5 on ESP32) | Chip Select |
| `BLK` | | `3.3V` (or PWM GPIO Pin) | Backlight control |

> [!WARNING]
> 3.3V Signal Logic Level Requirement:
> The ST7735 controller operates on **3.3V logic levels**. Connecting 5V SPI data lines directly from an Arduino Uno to the ST7735 `SCL`, `SDA`, and `DC` pins without $1\text{ k}\Omega / 2\text{ k}\Omega$ resistor dividers can cause white screen glitches or destroy the display controller over time.

## Common mistakes

- **Tab Color Configuration Mismatch:** ST7735 breakout modules come in different silicon revisions identified by colored protective film tabs (**ST7735B**, **ST7735R Red Tab**, **ST7735R Green Tab**, **ST7735S Black Tab**). Initializing a Green Tab display with Red Tab software settings causes shifted screen offsets and inverted colors (Red/Blue swap).
- **Leaving Backlight (`BLK`) Floating:** On some breakout modules, the `BLK` pin must be connected to 3.3V; leaving it floating results in a black screen.
- **Forgetting `SLPOUT` Delay:** After sending the `SLPOUT` (`0x11`) command, software MUST pause for **120 ms** before sending the `DISPON` (`0x29`) command to allow the internal charge pump to stabilize.

## Notes

- Supported by popular graphics libraries such as `Adafruit_ST7735`, `TFT_eSPI` (ESP32), and `TFT_ST7735` (ESPHome).
