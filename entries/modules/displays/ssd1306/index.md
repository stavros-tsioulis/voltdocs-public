## Overview

The **SSD1306** is a single-chip CMOS OLED/PLED driver with controller manufactured by Solomon Systech. It is designed to drive 128x64 or 128x32 dot-matrix graphic organic light-emitting diode (OLED) displays.

Commonly found on 0.96" and 0.91" monochrome display modules, the SSD1306 embeds an internal 1 KB Graphic Display Data RAM (GDDRAM), an onboard charge pump circuit to generate high OLED driving voltage ($V_{CC} \sim 9\text{ V}$) from a low logic supply, contrast control, and an internal oscillator.

## Quick reference

| | |
|---|---|
| **Module VCC** | 3.3 V to 5.0 V DC (onboard LDO & charge pump) |
| **Logic voltage ($V_{DD}$)** | 1.65 V to 3.3 V |
| **Display resolution** | 128 × 64 pixels or 128 × 32 pixels |
| **GDDRAM capacity** | 1 KB ($128 \times 64$ bits) |
| **Communication interfaces** | I2C (up to 400 kHz), 4-wire / 3-wire SPI |
| **Default I2C address** | `0x3C` (SA0 = LOW) / `0x3D` (SA0 = HIGH) |
| **Display color** | Monochrome (White, Blue, Yellow, or Yellow-Blue dual color) |

## Pinout

### Standard 4-Pin I2C Breakout Module

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` | Power | Ground (0 V) |
| 2 | `VCC` | Power | Power supply input (+3.3 V to +5.0 V DC) |
| 3 | `SCL` / `SCK` | Digital Input | I2C Serial Clock input pin |
| 4 | `SDA` | Digital I/O | I2C Serial Data line |

### 7-Pin SPI / I2C Breakout Module

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` | Power | Ground (0 V) |
| 2 | `VCC` | Power | Supply voltage (+3.3 V to +5.0 V) |
| 3 | `D0` / `CLK` | Digital Input | SPI Clock line |
| 4 | `D1` / `MOSI` | Digital Input | SPI Data line (Master Out Slave In) |
| 5 | `RES` / `RST` | Digital Input | Active-LOW Hardware Reset line |
| 6 | `DC` / `A0` | Digital Input | Data / Command control pin (`LOW` = Command, `HIGH` = Data) |
| 7 | `CS` | Digital Input | Active-LOW Chip Select line |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Chip Logic Voltage | $V_{DD}$ | 1.65 | 2.8 | 3.3 | V | Core logic supply |
| Display Panel Voltage | $V_{CC}$ | 7.0 | 9.0 | 15.0 | V | Generated via internal charge pump or external |
| Operating Current | $I_{CC}$ | — | 15 | 25 | mA | 128x64 display, 50% pixels ON |
| Sleep Current | $I_{sleep}$ | — | 1 | 10 | µA | Display OFF / Sleep mode |
| I2C Clock Frequency | $f_{SCL}$ | 0 | — | 400 | kHz | Fast Mode |
| SPI Clock Cycle | $t_{cycle}$ | 100 | — | — | ns | Max 10 MHz SPI clock |
| Operating Temperature | $T_{OP}$ | -40 | — | 85 | °C | |

## Addressing & Command set

### I2C Framing & Control Byte
On the I2C bus, data bytes are preceded by a Control Byte containing the $D/\bar{C}$ (Data/Command) bit:
- **`0x00` (Command byte):** Following byte is interpreted as a setup/configuration command.
- **`0x40` (Data byte):** Following byte is written directly to GDDRAM.

### Key Configuration Commands

| Command Hex | Description |
|---|---|
| `0xAE` | Display OFF (Sleep mode) |
| `0xAF` | Display ON (Normal mode) |
| `0x20` | Set Memory Addressing Mode (`0x00` = Horizontal, `0x01` = Vertical, `0x02` = Page) |
| `0x81` | Set Contrast Control (followed by contrast value `0x00`–`0xFF`) |
| `0x8D` | Charge Pump Setting (followed by `0x14` to enable internal charge pump) |
| `0xA6` / `0xA7` | Set Normal (`0xA6`) / Inverse (`0xA7`) display |

## Wiring

| SSD1306 I2C Module | → | Microcontroller (Arduino Uno / ESP32) | Notes |
|---|---|---|---|
| `GND` | | `GND` | Ground |
| `VCC` | | `5V` (or `3.3V`) | Power supply |
| `SCL` | | `SCL` (A5 on Uno, GPIO22 on ESP32) | I2C Clock |
| `SDA` | | `SDA` (A4 on Uno, GPIO21 on ESP32) | I2C Data |

## Common mistakes

- **Forgetting to enable internal charge pump:** Without sending `0x8D` followed by `0x14` during initialization, the internal high-voltage display supply ($V_{CC}$) remains disabled and the screen remains completely black.
- **I2C address mismatch:** Cheap 0.96" OLED modules alternate between `0x3C` (default for 128x64) and `0x3D` depending on how the hardware `SA0` resistor jumper is populated on the back PCB.
- **RAM footprint on small MCUs:** Storing a full $128 \times 64$ bit monochrome frame buffer requires 1024 bytes of SRAM. On ATmega328P (2 KB SRAM), this leaves only 1 KB of RAM for remaining application code.

## Notes

- Monochrome OLED pixels degrade over extended continuous display of static images. Implement a screen saver or pixel-shifting routine for long-running displays.
