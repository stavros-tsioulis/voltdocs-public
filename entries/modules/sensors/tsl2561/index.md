## Overview

The **TSL2561** is a light-to-digital converter IC manufactured by ams OSRAM (formerly TAOS). It converts light intensity into a digital signal output capable of direct I2C interface.

Unlike standard cadmium-sulfide (CdS) photoresistors or single-diode light sensors, the TSL2561 contains **two integrating photodiodes**: Channel 0 detects broadband light (visible plus infrared), while Channel 1 detects infrared light only. Subtracting IR spectrum data from Channel 0 yields a precise human-eye spectral response ($0.1\text{ to }40,000+\text{ lux}$) under varying light sources (incandescent, fluorescent, sunlight).

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 2.7 V to 3.6 V DC (3.3 V nominal) |
| **Dynamic range** | 0.1 lux to 40,000+ lux |
| **ADC resolution** | 16-bit dual Integrating ADCs |
| **Gain selection** | $1\times$ (low gain) or $16\times$ (high gain) |
| **Integration time** | 13.7 ms, 101 ms, or 402 ms (programmable) |
| **Communication interface** | I2C (address selectable: `0x29`, `0x39`, `0x49`) |
| **Operating current** | 240 µA active, 3.2 µA power-down |

## Pinout

### Standard 6-Pin Breakout Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+2.7 V to +3.6 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `3VI` | Power Output | 3.3V Output / Input |
| 4 | `ADDR` | Digital Input | I2C Slave Address selection pin |
| 5 | `INT` | Digital Output | Active-LOW Interrupt output pin |
| 6 | `SDA` | Digital I/O | I2C Serial Data line |
| 7 | `SCL` | Digital Input | I2C Serial Clock input |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 2.7 | 3.0 | 3.6 | V | DC |
| Active Supply Current | $I_{DD}$ | — | 240 | 600 | µA | Active conversion mode |
| Power-Down Current | $I_{PD}$ | — | 3.2 | 15 | µA | Power-down state |
| Full Scale Output | $FS$ | — | 65535 | — | Counts | 16-bit ADC max |
| Dark Current (Ch 0 / Ch 1) | $I_{dark}$ | — | 0 | 5 | LSB | $T_A = 25^\circ\text{C}$, 402 ms integration |
| I2C Clock Frequency | $f_{SCL}$ | 0 | 100 | 400 | kHz | Fast Mode |

## I2C Addressing & Command Structure

### Address Pin Configuration (`ADDR` / `SELECT` Pin)

| `ADDR` Pin Connection | I2C Address (Hex) |
|---|---|
| Floating (Left open) | `0x39` (Default) |
| Tied to `GND` | `0x29` |
| Tied to `VCC` | `0x49` |

### Command Register Byte (`COMMAND` Register `0x80`)

All I2C register accesses must send a Command Byte where Bit 7 is set to `1` (`0x80`).
- **Word protocol bit (Bit 5 = 1):** Read 2 consecutive bytes (LSB, MSB) in a single transaction (e.g. `0xAC` to read Channel 0 Word).

### Key Registers

| Register | Address | Description |
|---|---|---|
| `CONTROL` | `0x80` | Power control (`0x03` = Power ON, `0x00` = Power OFF) |
| `TIMING` | `0x81` | Gain select (Bit 4: `0` = 1x, `1` = 16x) & Integration time (Bits [1:0]: `00` = 13.7ms, `01` = 101ms, `10` = 402ms) |
| `DATA0LOW` / `HIGH` | `0x8C` / `0x8D` | Channel 0 broadband data (16-bit LSB/MSB) |
| `DATA1LOW` / `HIGH` | `0x8E` / `0x8F` | Channel 1 infrared data (16-bit LSB/MSB) |

## Wiring

| TSL2561 Breakout Pin | → | Microcontroller (Arduino Uno / ESP32) |
|---|---|---|
| `VCC` | | `3.3V` (or `5V` if breakout includes 3.3V LDO) |
| `GND` | | `GND` |
| `SDA` | | `SDA` (A4 on Uno, GPIO21 on ESP32) |
| `SCL` | | `SCL` (A5 on Uno, GPIO22 on ESP32) |

## Common mistakes

- **Forgetting to set Bit 7 (0x80) on register reads:** Failing to set bit 7 on the command byte causes the TSL2561 to ignore register read commands.
- **Sensor saturation in direct sunlight:** In high-light conditions (outdoors), leaving Gain at $16\times$ or Integration time at 402 ms causes ADC values to max out at 65535. Software should automatically switch Gain to $1\times$ and Integration time to 13.7 ms under bright light.
- **Powering bare chip with 5V:** The TSL2561 IC max supply rating is 3.6V. Only feed 5V if using a breakout board with an onboard 3.3V regulator.

## Notes

- Calculate Lux from raw counts: $Ratio = \frac{\text{Channel 1}}{\text{Channel 0}}$, then apply ams empirical Lux calculation coefficients based on ratio ranges.
