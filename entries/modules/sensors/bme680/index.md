## Overview

The **BME680** is an advanced 4-in-1 digital environmental sensor manufactured by Bosch Sensortec. It integrates a metal-oxide (MOX) gas sensor for Volatile Organic Compound (VOC) air quality monitoring alongside high-precision relative humidity, barometric pressure, and ambient temperature sensors.

Designed for smart home air quality monitoring (ESPHome BSEC integration, Home Assistant), HVAC systems, and wearable devices, the gas sensor detects airborne VOCs (paints, lacquers, cleaning supplies, tobacco smoke), breath VOCs, and hydrogen sulfide.

## Quick reference

| | |
|---|---|
| **Module VCC** | 3.3 V to 5.0 V DC (onboard 3.3V LDO) |
| **Chip VDD / VDDIO** | 1.71 V to 3.6 V DC |
| **Gas sensor** | MOX gas sensor detecting Volatile Organic Compounds (VOCs) |
| **Indoor Air Quality (IAQ)** | 0 to 500 IAQ index (via Bosch BSEC software library) |
| **Temperature range** | $-40^\circ\text{C}$ to $+85^\circ\text{C}$ ($\pm 0.5\text{ }^\circ\text{C}$ accuracy) |
| **Humidity range** | 0% to 100% RH ($\pm 3.0\%\text{ RH}$ accuracy) |
| **Pressure range** | 300 hPa to 1100 hPa ($\pm 0.6\text{ hPa}$ absolute accuracy) |
| **Communication interfaces** | I2C (address `0x77` or `0x76`), 3-wire / 4-wire SPI |

## Pinout

### Standard 6-Pin Breakout Module Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SCL` / `SCK` | Digital Input | I2C Serial Clock / SPI Clock pin |
| 4 | `SDA` / `SDI` | Digital I/O | I2C Serial Data / SPI Serial Data Input |
| 5 | `CSB` / `CS` | Digital Input | Chip Select (`HIGH` = I2C mode, `LOW` = SPI mode) |
| 6 | `SDO` / `ADR` | Digital I/O | I2C Address select (`HIGH` = `0x77`, `LOW` = `0x76`) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Chip) | $V_{DD}$ | 1.71 | 1.8 | 3.6 | V | DC |
| Gas Sensor Heater Power | $P_{gas}$ | — | 12 | 18 | mW | Target heater temperature $300^\circ\text{C}$ |
| Response Time ($p$) | $t_{p}$ | — | 0.92 | — | s | Pressure measurement |
| Response Time ($h$) | $t_{h}$ | — | 2.0 | — | s | Humidity measurement |
| Response Time ($g$) | $t_{g}$ | — | $< 1.0$ | — | s | Gas measurement |
| I2C Clock Frequency | $f_{SCL}$ | 0 | — | 3400 | kHz | High-Speed Mode |

## MOX Gas Sensor Operation & Bosch BSEC

The BME680 gas sensor operates by heating an internal hot plate to temperatures between **$200^\circ\text{C}$ and $400^\circ\text{C}$** and measuring the resistance change of the metal-oxide sensing layer ($R_{gas}$ in $\Omega$).

- **Raw $R_{gas}$ Value:** $R_{gas}$ resistance increases in clean air and decreases in the presence of reducing VOC gases.
- **Bosch BSEC Software Library:** Raw $R_{gas}$ values fluctuate with temperature and humidity. Bosch provides the closed-source **BSEC (Bosch Software Environmental Cluster)** binary library to combine temperature, humidity, pressure, and gas resistance into a calibrated **Indoor Air Quality (IAQ)** index (0 = Excellent, 500 = Extremely Polluted).

## Wiring

| BME680 Breakout Pin | → | Microcontroller (Arduino Uno / ESP32) |
|---|---|---|
| `VCC` | | `3.3V` (or `5V`) |
| `GND` | | `GND` |
| `SCL` | | `SCL` (A5 on Uno, GPIO22 on ESP32) |
| `SDA` | | `SDA` (A4 on Uno, GPIO21 on ESP32) |

## Common mistakes

- **Expecting raw $R_{gas}$ to equal IAQ directly:** Raw $R_{gas}$ resistance varies significantly with relative humidity and temperature. Calculating true IAQ requires temperature/humidity compensation via the Bosch BSEC algorithm.
- **Self-heating shift in temperature readings:** Operating the MOX gas heater generates internal heat inside the tiny $3\times 3\text{ mm}$ package. Temperature readings will read $1\text{ to }2\text{ }^\circ\text{C}$ higher than ambient room temperature. Apply a temperature offset correction in software.
- **Skipping initial gas heater burn-in:** New BME680 sensors require a 48-hour continuous initial burn-in period to stabilize the MOX gas element.

## Notes

- BME680 vs BME280: The BME680 adds the MOX gas sensor to the temperature/humidity/pressure feature set of the BME280.
