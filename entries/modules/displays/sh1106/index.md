## Overview

The **SH1106** is a single-chip CMOS OLED/PLED driver manufactured by Sino Wealth Microelectronic. It is designed for driving 132x64 dot-matrix organic LED displays and is standard on larger **1.3-inch 128x64 monochrome OLED display modules**.

While visually similar to 0.96-inch OLED displays driven by the SSD1306, the SH1106 chip contains an internal **132x64 GRAM frame buffer** (4 columns wider than 128 pixels). Consequently, software drivers must shift display columns by **2 pixels** ($Column = Column + 2$) to center a 128x64 image frame on screen.

## Quick reference

| | |
|---|---|
| **Module VCC** | 3.3 V to 5.0 V DC (onboard LDO + charge pump) |
| **Chip VDD** | 1.65 V to 3.5 V DC |
| **Display Resolution** | 128 x 64 pixels (driven from 132 x 64 internal RAM) |
| **Diagonal Screen Size** | Typically 1.3 inches |
| **Communication interfaces** | I2C (address `0x3C` or `0x3D`, up to 400 kHz), 4-wire SPI |
| **Page Addressing** | Page addressing mode (8 pages of 132 x 8 bits) |
| **Contrast Control** | 256-level brightness contrast steps |

## Pinout

### Standard 4-Pin I2C 1.3-inch OLED Module Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` | Power | Ground (0 V) |
| 2 | `VCC` | Power | Supply voltage (+3.3 V to +5.0 V DC) |
| 3 | `SCL` | Digital Input | I2C Serial Clock line |
| 4 | `SDA` | Digital I/O | I2C Serial Data line |

### 7-Pin SPI 1.3-inch OLED Module Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` | Power | Ground (0 V) |
| 2 | `VCC` | Power | Supply voltage (+3.3 V to +5.0 V DC) |
| 3 | `D0` / `SCLK` | Digital Input | SPI Clock input line |
| 4 | `D1` / `MOSI` | Digital Input | SPI Master Output Data line |
| 5 | `RES` / `RST` | Digital Input | Hardware Reset line (Active-LOW) |
| 6 | `DC` / `A0` | Digital Input | Data / Command control pin (`LOW` = Command, `HIGH` = Data) |
| 7 | `CS` | Digital Input | SPI Chip Select (Active-LOW) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{CC}$ | 3.3 | 5.0 | 5.5 | V | DC |
| Logic Voltage High | $V_{IH}$ | $0.8 V_{DD}$ | — | $V_{DD}$ | V | `SCL`, `SDA` |
| Logic Voltage Low | $V_{IL}$ | 0 | — | $0.2 V_{DD}$ | V | `SCL`, `SDA` |
| Operating Supply Current | $I_{CC}$ | — | 15 | 25 | mA | 100% pixels ON |
| Sleep Current | $I_{SLEEP}$ | — | 5 | 10 | µA | Display OFF (`0xAE`) |
| GRAM Size | $RAM$ | — | $132 \times 64$ | — | bits | 8 Pages $\times$ 132 Columns |

## SH1106 vs SSD1306 Differences

| Feature | SSD1306 (0.96-inch typical) | SH1106 (1.3-inch typical) |
|---|---|---|
| **Internal RAM Size** | $128 \times 64$ bits | **$132 \times 64$ bits** |
| **Column Offset** | Direct 0-to-127 column mapping | **Requires +2 column offset ($Column + 2$)** |
| **Addressing Modes** | Page, Horizontal, Vertical addressing | **Page Addressing Mode only** |
| **Charge Pump Command** | `0x8D` (Enable Charge Pump) | `0x8D` / `0xAD` (Built-in charge pump) |

> [!WARNING]
> Column Shift Distortion in Software:
> If an SH1106 display is driven using standard SSD1306 software code, the image will appear **shifted 2 pixels to the right** with 2 pixels of static noise/garbled lines on the left edge. Always select `SH1106` in display driver libraries (such as `U8g2` or `Adafruit_SH1106`).

## Wiring

| SH1106 I2C Module Pin | → | Microcontroller (Arduino Uno / ESP32) |
|---|---|---|
| `GND` | | `GND` |
| `VCC` | | `5V` (or `3.3V`) |
| `SCL` | | `SCL` (A5 on Uno, GPIO22 on ESP32) |
| `SDA` | | `SDA` (A4 on Uno, GPIO21 on ESP32) |

## Common mistakes

- **Using SSD1306 display drivers:** SSD1306 drivers lack page-by-page column offset handling ($Column + 2$), resulting in shifted/garbled images.
- **Attempting to use Horizontal / Vertical Addressing modes:** The SH1106 only supports Page Addressing mode (`0xB0` to `0xB7`).
- **Forgetting I2C slave address:** Most SH1106 1.3-inch displays default to address `0x3C`, but some boards use `0x3D`.

## Notes

- Low power consumption allows direct battery operation without backlight power penalty.
