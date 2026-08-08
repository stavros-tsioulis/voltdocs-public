## Overview

The **BME280** is a 3-in-1 digital environmental sensor manufactured by Bosch Sensortec. It measures ambient temperature, relative humidity, and barometric pressure with high precision, fast response times, and low power consumption.

It is widely used in weather stations, IoT environmental monitoring nodes, home automation systems (ESPHome, Home Assistant), and altitude tracking devices (altimeters). Breakout modules include an onboard 3.3V LDO regulator and level shifter circuitry for 3.3V/5V microcontroller compatibility over I2C or SPI.

## Quick reference

| | |
|---|---|
| **Module VCC** | 3.3 V to 5.0 V DC (onboard LDO) |
| **Chip VDD / VDDIO** | 1.71 V to 3.6 V DC |
| **Communication interfaces** | I2C (up to 3.4 MHz), 3-wire / 4-wire SPI (up to 10 MHz) |
| **Default I2C address** | `0x76` (SDO = LOW) / `0x77` (SDO = HIGH) |
| **Temperature range** | $-40^\circ\text{C}$ to $+85^\circ\text{C}$ ($\pm 0.5\text{ }^\circ\text{C}$ accuracy) |
| **Humidity range** | 0% to 100% RH ($\pm 3\%\text{ RH}$ accuracy, 1 s response time) |
| **Pressure range** | 300 hPa to 1100 hPa ($\pm 1.0\text{ hPa}$ absolute accuracy) |

## Pinout

### Standard 6-Pin Breakout Module Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SCL` / `SCK` | Digital Input | I2C Serial Clock / SPI Clock pin |
| 4 | `SDA` / `SDI` | Digital I/O | I2C Serial Data / SPI Serial Data Input |
| 5 | `CSB` / `CS` | Digital Input | Chip Select pin (`HIGH` = I2C mode, `LOW` = SPI mode) |
| 6 | `SDO` / `ADR` | Digital I/O | I2C Address select pin / SPI Serial Data Output |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Chip) | $V_{DD}$ | 1.71 | 1.8 | 3.6 | V | DC |
| Supply Current (Humidity) | $I_{DD,H}$ | — | 340 | — | µA | 1 Hz humidity forced mode |
| Supply Current (Pressure) | $I_{DD,P}$ | — | 714 | — | µA | 1 Hz pressure forced mode |
| Sleep Current | $I_{DD,SL}$ | — | 0.1 | 0.3 | µA | Sleep mode |
| Temperature Resolution | $T_{res}$ | — | 0.01 | — | °C | 20-bit output |
| Relative Humidity Resolution | $H_{res}$ | — | 0.008 | — | % RH | 16-bit output |
| Pressure Resolution | $P_{res}$ | — | 0.0018 | — | hPa | 20-bit output (0.18 m altitude resolution) |

## Communication & Registers

### Mode Selection & Addresses

- **I2C Mode:** `CSB` pin pulled `HIGH` (or left floating with internal pull-up).
  - Address `0x76`: `SDO` pin connected to `GND`.
  - Address `0x77`: `SDO` pin connected to `VCC`.
- **SPI Mode:** `CSB` pin pulled `LOW` by microcontroller during transactions.

### Key Registers

| Address | Register | Access | Description |
|---|---|---|---|
| `0xD0` | `ID` | R | Chip Identification (returns `0x60` for BME280) |
| `0xE0` | `RESET` | W | Software reset (write `0xB6` to reset) |
| `0xF2` | `CTRL_HUM` | R/W | Humidity oversampling control (must write before `CTRL_MEAS`) |
| `0xF4` | `CTRL_MEAS` | R/W | Pressure & Temperature oversampling and sensor mode select |
| `0xF5` | `CONFIG` | R/W | Rate, IIR filter constant, and 3-wire SPI select |
| `0xF7`–`0xFC` | `DATA` | R | Burst read 6 bytes: Pressure [F7:F9], Temp [FA:FC], Humidity [FD:FE] |

> [!NOTE]
> BME280 vs BMP280 Identification:
> - **BME280** (`ID` register `0xD0` = `0x60`): Measures Temperature, Pressure, and **Humidity**.
> - **BMP280** (`ID` register `0xD0` = `0x58`): Measures Temperature and Pressure **only** (no humidity sensor).

## Wiring

| BME280 Breakout Pin | → | Microcontroller (Arduino Uno / ESP32) | Notes |
|---|---|---|---|
| `VCC` | | `3.3V` (or `5V`) | Power supply |
| `GND` | | `GND` | Ground |
| `SCL` | | `SCL` (A5 on Uno, GPIO22 on ESP32) | I2C Clock |
| `SDA` | | `SDA` (A4 on Uno, GPIO21 on ESP32) | I2C Data |

## Common mistakes

- **Confusing BME280 with BMP280:** Both sensors share near-identical 6-pin breakout board layouts. However, BMP280 lacks the humidity sensing element. Checking register `0xD0` (`0x60` vs `0x58`) confirms the exact chip.
- **Wrong default I2C address in code:** Many Arduino/ESPHome libraries default to `0x77`, whereas common purple BME280 breakouts hardwire `SDO` to GND, selecting address `0x76`.
- **Writing `CTRL_HUM` after `CTRL_MEAS`:** According to the Bosch datasheet, changes to `CTRL_HUM` (`0xF2`) only take effect after writing to `CTRL_MEAS` (`0xF4`). Software must write `0xF2` before `0xF4`.

## Notes

- Barometric pressure varies with altitude according to the hypsometric formula:
  $$\text{Altitude (m)} = 44330 \times \left(1 - \left(\frac{P_{measured}}{P_{sea\_level}}\right)^{1/5.255}\right)$$
