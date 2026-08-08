## Overview

The **ADXL345** is a small, thin, ultra-low power 3-axis MEMS accelerometer manufactured by Analog Devices. It measures static acceleration of gravity in tilt-sensing applications as well as dynamic acceleration resulting from motion, shock, or vibration.

It features high resolution up to 13 bits at $\pm 16\text{ g}$ ($4\text{ mg/LSB}$ scale factor maintained across all ranges), an integrated 32-level FIFO buffer, activity/inactivity monitoring, tap/double-tap detection, and free-fall detection.

## Quick reference

| | |
|---|---|
| **Module VCC** | 3.3 V to 5.0 V DC (onboard LDO) |
| **Chip VDD / VDDIO** | 2.0 V to 3.6 V DC |
| **Full-scale ranges** | $\pm 2\text{ g}, \pm 4\text{ g}, \pm 8\text{ g}, \pm 16\text{ g}$ (user selectable) |
| **ADC resolution** | 10-bit (fixed 10-bit at $\pm 2\text{g}$) up to 13-bit (FULL_RES mode) |
| **Sensitivity** | $3.9\text{ mg/LSB}$ (in FULL_RES mode) |
| **Communication interfaces** | I2C (up to 400 kHz), 3-wire / 4-wire SPI (up to 5 MHz) |
| **Default I2C address** | `0x53` (ALT ADDRESS = LOW) / `0x1D` (ALT ADDRESS = HIGH) |
| **Measurement current** | 145 µA active, 0.1 µA standby |

## Pinout

### Standard GY-291 Breakout Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `CS` | Digital Input | Chip Select (`HIGH` = I2C Mode, `LOW` = SPI Mode) |
| 4 | `INT1` | Digital Output | Programmable Interrupt 1 pin |
| 5 | `INT2` | Digital Output | Programmable Interrupt 2 pin |
| 6 | `SDO` / `ALT` | Digital I/O | SPI Data Output / I2C Alternate Address pin |
| 7 | `SDA` / `SDI` | Digital I/O | I2C Serial Data / SPI Serial Data Input |
| 8 | `SCL` / `SCLK` | Digital Input | I2C Serial Clock / SPI Serial Clock |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Chip Supply Voltage | $V_{DD}$ | 2.0 | 2.5 | 3.6 | V | DC |
| Measurement Current | $I_{DD}$ | — | 145 | 180 | µA | $V_{DD} = 2.5\text{ V}$, $ODR = 100\text{ Hz}$ |
| Standby Current | $I_{STB}$ | — | 0.1 | 0.5 | µA | Standby mode |
| Sensitivity (FULL_RES) | $S$ | 3.5 | 3.9 | 4.3 | mg/LSB | All $g$ ranges |
| Output Data Rate | $ODR$ | 0.1 | 100 | 3200 | Hz | Selectable via `BW_RATE` |
| Operating Temp Range | $T_{OP}$ | -40 | — | 85 | °C | |

## Key Registers

| Address | Register | Access | Reset | Description |
|---|---|---|---|---|
| `0x00` | `DEVID` | R | `0xE5` | Device ID register (returns `0xE5`) |
| `0x2D` | `POWER_CTL` | R/W | `0x00` | Power control (Set bit 3 `Measure` = 1 to enable measuring) |
| `0x2E` | `INT_ENABLE` | R/W | `0x00` | Interrupt enable control (Single/double tap, freefall, data ready) |
| `0x31` | `DATA_FORMAT` | R/W | `0x00` | Set range ($\pm 2g, \pm 4g, \pm 8g, \pm 16g$) & `FULL_RES` bit [3] |
| `0x32`–`0x37` | `DATAX0`..`DATAZ1` | R | `0x00` | Read 6 bytes for X, Y, Z acceleration data (LSB first) |

> [!NOTE]
> 16-bit Signed Data Assembly:
> Read 6 consecutive bytes starting at `DATAX0` (`0x32`). Combine bytes in Little-Endian format: `int16_t x = (int16_t)(data[1] << 8 | data[0]);`.

## Wiring

| ADXL345 Breakout | → | Microcontroller (Arduino Uno / ESP32) | Notes |
|---|---|---|---|
| `VCC` | | `3.3V` (or `5V`) | Power supply |
| `GND` | | `GND` | Ground |
| `CS` | | `VCC` (or 3.3V) | Must be pulled HIGH for I2C mode |
| `SDA` | | `SDA` (A4 on Uno, GPIO21 on ESP32) | I2C Data line |
| `SCL` | | `SCL` (A5 on Uno, GPIO22 on ESP32) | I2C Clock line |
| `SDO` | | `GND` | Pull LOW for address `0x53`, HIGH for `0x1D` |

## Common mistakes

- **Forgetting to set `POWER_CTL` Measure bit:** The ADXL345 powers up in standby mode (`0x00`). Software MUST write `0x08` to `POWER_CTL` (`0x2D`) to enable active measurement.
- **Leaving `CS` pin floating for I2C mode:** If `CS` is floating, electrical noise can pull `CS` LOW, causing the chip to switch into SPI mode and stop responding on the I2C bus.
- **Reading single bytes instead of multi-byte burst:** When reading `DATAX0` to `DATAZ1` over SPI, bit 6 (`MB` - Multiple Byte bit) in the instruction byte must be set to `1` to enable auto-increment address reads.

## Notes

- Free-fall detection triggers when total vector acceleration $\sqrt{X^2 + Y^2 + Z^2}$ drops below a user-configured threshold (typically $<0.5\text{ g}$) for a minimum duration.
