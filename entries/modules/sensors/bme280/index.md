## Overview

The **BME280** is a premium 3-in-1 digital environmental sensor developed by Bosch Sensortec. It integrates high-precision sensors for **relative humidity**, **barometric pressure**, and **ambient temperature** into a tiny 8-pin metal-lid LGA package.

Designed for low-power mobile applications, home automation climate nodes, and weather stations, the BME280 improves upon the BMP280 by adding a fast-response humidity sensor (1 second response time with $\pm 3\%\text{ RH}$ accuracy). It supports both I2C (up to 3.4 MHz) and 3-wire/4-wire SPI (up to 10 MHz) serial interfaces.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VDD`)** | 1.71 V – 3.6 V (3.3 V nominal; 5V breakout modules include LDO + level shifters) |
| **Humidity measurement range** | 0% to 100% RH ($\pm 3\%\text{ RH}$ accuracy, 1 s response time) |
| **Pressure measurement range** | 300 hPa to 1100 hPa ($\pm 1.0\text{ hPa}$ absolute accuracy, $\pm 0.12\text{ hPa}$ relative) |
| **Temperature measurement range** | $-40^\circ\text{C}$ to $+85^\circ\text{C}$ ($\pm 0.5^\circ\text{C}$ accuracy at $25^\circ\text{C}$) |
| **Current consumption** | 1.8 µA @ 1 Hz (Humidity + Pressure + Temp) / 0.1 µA in Sleep Mode |
| **Default I2C address** | `0x76` (`SDO` tied to GND) / `0x77` (`SDO` tied to VDD) |

## Pinout

### Standard 4-Pin / 6-Pin Breakout Module

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply Voltage Input (+3.3 V or +5.0 V on regulated modules) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SCL` / `SCK` | Digital Input | I2C Serial Clock Line / SPI Clock (`SCLK`) |
| 4 | `SDA` / `SDI` | Digital I/O | I2C Serial Data Line / SPI Master Out Data (`MOSI`) |
| 5 | `CSB` / `CS` | Digital Input | Chip Select (`HIGH` for I2C mode; `LOW` for SPI mode) |
| 6 | `SDO` | Digital I/O | I2C Address Select (`LOW`: 0x76, `HIGH`: 0x77) / SPI Data Out (`MISO`) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | `VDD` | 1.71 | 3.3 | 3.6 | V | IC Rating |
| Peak Current | `IDD_PEAK` | — | 714 | 1120 | µA | Pressure conversion active |
| Humidity Response Time | `tH_RESP` | — | 1 | — | s | 63% step response at $25^\circ\text{C}$ |
| Pressure Noise | `P_NOISE` | — | 0.2 | 1.3 | Pa | Ultra-high resolution mode |
| Temperature Resolution | `T_RES` | — | 0.01 | — | °C | 20-bit internal ADC output |
| I2C Bus Frequency | `fSCL` | 0 | 400 | 3400 | kHz | Fast-mode & High-speed mode |

## Register map

| Address | Register Name | Access | Description |
|---|---|---|---|
| `0x88`–`0xA1` | Trimming Coeffs | R | Factory calibration coefficients ($T_1..T_3, P_1..P_9$) |
| `0xE1`–`0xF0` | Humidity Coeffs | R | Factory calibration coefficients ($H_1..H_6$) |
| `0xD0` | `ID` | R | Chip Identification Register (Returns `0x60` for BME280) |
| `0xF2` | `CTRL_HUM` | R/W | Humidity Oversampling Control (`osrs_h[2:0]`) |
| `0xF4` | `CTRL_MEAS` | R/W | Temperature/Pressure Oversampling & Sensor Mode (`Sleep`/`Forced`/`Normal`) |
| `0xF5` | `CONFIG` | R/W | Standby Time, IIR Filter Coefficient, 3-wire SPI Enable |
| `0xF7`–`0xF9` | `PRESS_MSB..LSB` | R | Raw 20-bit Pressure Measurement ADC Value |
| `0xFA`–`0xFC` | `TEMP_MSB..LSB` | R | Raw 20-bit Temperature Measurement ADC Value |
| `0xFD`–`0xFE` | `HUM_MSB..LSB` | R | Raw 16-bit Humidity Measurement ADC Value |

## Wiring

| BME280 Module Pin | :i-lucide-move-right: | Microcontroller (Arduino Uno / ESP32) |
|---|---|---|
| `VCC` | | 3.3V (or 5V if module has 662K LDO) |
| `GND` | | GND |
| `SCL` | | I2C SCL (Pin `A5` on Uno / GPIO`22` on ESP32) |
| `SDA` | | I2C SDA (Pin `A4` on Uno / GPIO`21` on ESP32) |
| `CSB` | | Tie to `VCC` (Enables I2C Mode) |
| `SDO` | | Tie to `GND` (Address `0x76`) or `VCC` (`0x77`) |

## Common mistakes

- **Confusing BME280 and BMP280:** The BMP280 is pressure and temperature ONLY (it lacks a humidity sensor). The BME280 chip ID register (`0xD0`) returns `0x60`, whereas BMP280 returns `0x58`. If your code fails to read humidity, check if you accidentally bought a BMP280.
- **Reading raw ADC values without calibration formulas:** Raw ADC registers (`0xF7`–`0xFE`) return uncompensated integer data. You MUST read the factory calibration parameters from `0x88` and `0xE1` and apply Bosch's compensation equations to convert to real °C, hPa, and % RH.
- **Self-heating error in continuous measurement mode:** Operating the BME280 continuously at maximum sampling rates without filtering causes internal IC self-heating, skewing temperature readings higher by 1–2°C and humidity lower. Use Forced Mode or configure the internal IIR filter.

## Notes

- **Altitude Calculation Formula:** Barometric pressure can be converted to altitude above sea level using the hypsometric formula:
  $$\text{Altitude (m)} = 44330 \times \left(1 - \left(\frac{P_{\text{measured}}}{P_{\text{sea\_level}}}\right)^{\frac{1}{5.255}}\right)$$
