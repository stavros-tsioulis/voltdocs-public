## Overview

The **SSD1306** is a single-chip CMOS OLED/PLED driver with controller manufactured by Solomon Systech. It is designed to drive monochrome dot matrix graphic OLED displays up to **128x64** resolution (including 128x32 variants).

It incorporates an internal $128 \times 64$ bit Display Data RAM (GDDRAM), 256-step contrast control, an internal oscillator, and an integrated DC-DC charge pump to generate high OLED driving voltages (7 V to 9 V) from a low 3.3 V logic supply. Most commonly sold as a 0.96-inch or 0.91-inch I2C/SPI OLED breakout module, it is the primary high-density display module used across Arduino, ESP32, and Raspberry Pi IoT projects.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 1.65 V – 3.3 V (bare IC) / 3.3 V – 5.0 V (breakout module) |
| **Display resolution** | 128 x 64 pixels (or 128 x 32 pixels) |
| **Display technology** | Self-luminous OLED (no backlight required) |
| **Interface** | I2C (400 kHz), 4-wire SPI (10 MHz), 3-wire SPI, or 8-bit Parallel |
| **Default I2C address** | `0x3C` (`SA0` / `DC` LOW) / `0x3D` (`SA0` / `DC` HIGH) |
| **Current draw** | ~15 mA (all pixels ON) / < 10 µA (sleep mode) |

## Pinout

### Standard 4-Pin I2C OLED Module Breakout

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` | Power | Ground (0 V) |
| 2 | `VCC` | Power | Supply Voltage (+3.3 V to +5.0 V regulated) |
| 3 | `SCL` / `SCK` | Digital Input | I2C Serial Clock Line |
| 4 | `SDA` | Digital I/O | I2C Serial Data Line |

### Standard 7-Pin SPI OLED Module Breakout

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` | Power | Ground (0 V) |
| 2 | `VCC` | Power | Supply Voltage (+3.3 V to +5.0 V) |
| 3 | `D0` / `CLK` | Digital Input | SPI Clock Line (`SCLK`) |
| 4 | `D1` / `MOSI` | Digital Input | SPI Data Line (`MOSI`) |
| 5 | `RES` / `RST` | Digital Input | Hardware Reset pin (Active-LOW) |
| 6 | `DC` / `A0` | Digital Input | Data / Command Control pin (`LOW`: Command, `HIGH`: Data) |
| 7 | `CS` | Digital Input | SPI Chip Select pin (Active-LOW) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Logic Voltage | `VDD` | 1.65 | 2.8 | 3.3 | V | Bare IC rating |
| OLED Driving Voltage | `VCC_OLED` | 7.0 | 7.5 | 9.0 | V | Generated internally via Charge Pump |
| Operating Current (50% pixels) | `IDD` | — | 9.0 | 12.0 | mA | Display ON, 50% brightness |
| Operating Current (100% pixels) | `IDD` | — | 15.0 | 25.0 | mA | Display ON, 100% white pixels |
| Sleep Current | `ISLEEP` | — | 1.0 | 10.0 | µA | Command `0xAE` (Display OFF) |
| I2C Clock Frequency | `fSCL` | 0 | 100 | 400 | kHz | Fast-Mode I2C |
| SPI Clock Frequency | `fSCLK` | 0 | — | 10 | MHz | 4-wire SPI mode |

## Memory & addressing modes

The internal $128 \times 64$ bit Graphic Display Data RAM (GDDRAM) is divided into **8 pages** (Page 0 to Page 7). Each page consists of 128 columns, where 1 column byte represents 8 vertical pixels (LSB at the top, MSB at the bottom).

### Memory Addressing Modes

1. **Page Addressing Mode (Default `0x02`):** Access is restricted within a single page. After reading/writing a column byte, the column pointer increments automatically until Column 127, then wraps back to Column 0 of the *same* page.
2. **Horizontal Addressing Mode (`0x00`):** After reaching Column 127, the column pointer resets to 0 and the page pointer increments automatically to the next page. Ideal for fast full-frame buffer updates.
3. **Vertical Addressing Mode (`0x01`):** Advances vertically through pages at the same column before advancing to the next column.

## Essential initialization commands

| Command Code | Name | Description |
|---|---|---|
| `0xAE` | Display OFF | Turn off OLED panel (sleep mode) |
| `0x8D`, `0x14` | Charge Pump Enable | Enable internal DC-DC charge pump (Required for display output!) |
| `0x20`, `0x00` | Set Memory Mode | Set addressing mode to Horizontal Mode (`0x00`) |
| `0xDA`, `0x12` | Set COM Pins | Configure COM pin hardware layout (Use `0x12` for 128x64, `0x02` for 128x32) |
| `0x81`, `0xCF` | Set Contrast | Set 256-step brightness contrast control (`0x00` min to `0xFF` max) |
| `0xA1` | Segment Remap | Flip display horizontally (`A0` normal, `A1` inverted) |
| `0xC8` | COM Scan Direction | Flip display vertically (`C0` normal, `C8` inverted) |
| `0xAF` | Display ON | Power on OLED panel |

## Wiring

### I2C Mode (Arduino Uno)

| SSD1306 Module Pin | :i-lucide-move-right: | Arduino Uno Pin | Notes |
|---|---|---|---|
| `GND` | | `GND` | Ground |
| `VCC` | | `5V` (or `3.3V`) | Supply Power |
| `SCL` | | `A5` / `SCL` | I2C Clock |
| `SDA` | | `A4` / `SDA` | I2C Data |

## Common mistakes

- **Forgetting to enable Charge Pump during initialization:** If the charge pump command sequence (`0x8D` followed by `0x14`) is omitted, the OLED panel remains completely blank even though communication succeeds.
- **Incorrect I2C address (`0x3C` vs `0x3D`):** Most 0.96" modules use 7-bit address `0x3C`. However, some manufacturers solder the `SA0` address select resistor to `VCC`, changing the address to `0x3D`. Run an I2C scanner if the display fails to initialize.
- **Applying 128x64 settings to a 128x32 panel:** Using 128x64 display configuration parameters on a 128x32 OLED results in stretched line spacing and alternating blank rows. Update the COM pins command (`0xDA`) to `0x02` for 32-row panels.

## Notes

- **Burn-in prevention:** Static graphics left on an OLED display indefinitely will cause permanent pixel degradation (burn-in). Use a screen saver routine or send Display OFF (`0xAE`) after long periods of inactivity.
