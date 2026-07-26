## Overview

The **BMP280** is an absolute barometric pressure sensor designed specifically for mobile applications by Bosch Sensortec. It succeeds the BMP180 and offers higher accuracy, lower power consumption, and smaller footprint dimensions (2.0 mm × 2.5 mm × 0.95 mm LGA package).

The sensor integrates piezo-resistive pressure and temperature sensing elements, an analog-to-digital converter, and digital control circuitry supporting both **I2C** and 3-/4-wire **SPI** serial interfaces.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VDD`)** | 1.71 V – 3.6 V |
| **Pressure range** | 300 hPa – 1100 hPa (+9000 m to -500 m relative to sea level) |
| **Temperature range** | -40 °C to +85 °C |
| **Absolute pressure accuracy** | ±1.0 hPa (0 °C to 65 °C) |
| **Relative pressure accuracy** | ±0.12 hPa (equivalent to ±1 m altitude) |
| **I2C addresses** | `0x76` (SDO to GND) / `0x77` (SDO to VDD) |
| **Current draw** | 2.7 µA @ 1 Hz sampling / 0.1 µA sleep mode |

## Pinout

### Standard 6-Pin Breakout Module

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (1.8 V to 3.3 V; 5V if module has onboard 3.3V LDO) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SCL` / `SCK` | Digital Input | I2C Clock / SPI Serial Clock |
| 4 | `SDA` / `SDI` | Digital I/O | I2C Data / SPI Serial Data In |
| 5 | `CSB` | Digital Input | Chip Select (High = I2C mode; Low = SPI mode) |
| 6 | `SDO` | Digital Output | I2C Address Select (`GND`: 0x76, `VDD`: 0x77) / SPI Data Out |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Operating Voltage | `VDD` | 1.71 | 1.8 / 3.3 | 3.6 | V | IC supply |
| Peak Current | `IIDD` | — | 720 | 1120 | µA | During pressure measurement |
| Standby Current | `IDDSB` | — | 0.2 | 0.5 | µA | Standby mode |
| Temperature Resolution | `T_res` | — | 0.01 | — | °C | 16–20 bit output |
| Pressure Resolution | `P_res` | — | 0.016 | — | hPa | Ultra-high resolution mode |

## Register map

| Address | Register | Access | Reset | Description |
|---|---|---|---|---|
| `0x88` – `0xA1` | `calib00..calib25` | R | Factory | Trimming parameter coefficients ($dig\_T_1..T_3, dig\_P_1..P_9$) |
| `0xD0` | `id` | R | `0x58` | Chip ID register (reads `0x58` for BMP280) |
| `0xE0` | `reset` | W | `0x00` | Write `0xB6` to initiate soft reset |
| `0xF3` | `status` | R | `0x00` | Bit 3: `measuring`, Bit 0: `im_update` |
| `0xF4` | `ctrl_meas` | R/W | `0x00` | Temp/Pressure oversampling & power mode |
| `0xF5` | `config` | R/W | `0x00` | Standby time, IIR filter coefficient, 3-wire SPI |
| `0xF7` – `0xF9` | `press_msb..xlsb` | R | `0x80000` | 20-bit raw pressure data |
| `0xFA` – `0xFC` | `temp_msb..xlsb` | R | `0x80000` | 20-bit raw temperature data |

## Wiring (I2C Mode)

| BMP280 Breakout | → | Microcontroller (Arduino / ESP32) |
|---|---|---|
| `VCC` | | 3.3 V |
| `GND` | | GND |
| `SCL` | | I2C SCL |
| `SDA` | | I2C SDA |
| `CSB` | | VCC (Pulls HIGH to select I2C mode) |
| `SDO` | | GND (Selects default address `0x76`) |

## Common mistakes

- **Confusing BMP280 with BME280:** The BMP280 measures **Pressure and Temperature only**. The BME280 adds **Humidity** sensing (chip ID `0x60`). Drivers expecting humidity reading will fail or return zero on BMP280 (`0x58`).
- **Ignoring calibration registers:** Raw 20-bit pressure and temperature values from registers `0xF7`–`0xFC` must be processed using the factory calibration coefficients stored in registers `0x88`–`0xA1` via Bosch's polynomial compensation math.
- **Powering 3.3V-only breakouts with 5V:** Unregulated BMP280 modules lacking a 3.3V LDO will be damaged if connected directly to a 5V supply pin.

## Notes

- **Altitude calculation:** Relative altitude can be estimated using the hypsometric formula:
$$
h = 44330 \times \left(1 - \left(\frac{P}{P_0}\right)^{\frac{1}{5.255}}\right)
$$
where $P_0$ is sea level pressure (1013.25 hPa).
