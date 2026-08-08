## Overview

The **MPU9250** is a 9-axis MotionTracking System in Package (SiP) manufactured by InvenSense (TDK). It combines two dies into a single $3\times 3\times 1\text{ mm}$ QFN package: an MPU6500 (containing a 3-axis 16-bit accelerometer and 3-axis 16-bit gyroscope) and an **AK8963** 3-axis 16-bit digital magnetometer (compass).

It replaces the legacy MPU6050 + HMC5883L dual-chip setups, providing complete 9-DOF orientation sensing for drones (INAV, Betaflight, ArduPilot), robotics, and VR motion tracking over I2C or high-speed SPI (up to 20 MHz).

## Quick reference

| | |
|---|---|
| **Module VCC** | 3.3 V to 5.0 V DC (onboard 3.3V LDO) |
| **Chip VDD / VDDIO** | 2.4 V to 3.6 V DC |
| **Degrees of Freedom (DOF)** | 9-DOF (3-axis Accel + 3-axis Gyro + 3-axis Magnetometer) |
| **Accelerometer Full-Scale Ranges** | $\pm 2g, \pm 4g, \pm 8g, \pm 16g$ |
| **Gyroscope Full-Scale Ranges** | $\pm 250, \pm 500, \pm 1000, \pm 2000^\circ\text{/s}$ |
| **Magnetometer Full-Scale Range** | $\pm 4900\text{ }\mu\text{T}$ (16-bit resolution, $0.6\text{ }\mu\text{T/LSB}$) |
| **Communication interfaces** | I2C (default `0x68`, alternate `0x69`, up to 400 kHz), SPI (up to 20 MHz) |
| **FIFO Buffer** | 512-byte FIFO buffer |

## Pinout

### Standard GY-9250 10-Pin Breakout Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SCL` / `SCLK` | Digital Input | I2C Serial Clock / SPI Serial Clock |
| 4 | `SDA` / `SDI` | Digital I/O | I2C Serial Data / SPI Data Input (MOSI) |
| 5 | `EDA` / `AUX_DA` | Digital I/O | Auxiliary I2C Data line (for external barometer) |
| 6 | `ECL` / `AUX_CL` | Digital Output | Auxiliary I2C Clock line |
| 7 | `AD0` / `SDO` | Digital I/O | I2C Address bit 0 (`LOW` = `0x68`, `HIGH` = `0x69`) / SPI Data Output (MISO) |
| 8 | `INT` | Digital Output | Interrupt output pin |
| 9 | `NCS` / `CS` | Digital Input | SPI Chip Select (`HIGH` = I2C Mode, `LOW` = SPI Mode) |
| 10 | `FSYNC` | Digital Input | Frame Sync input (tie to GND if unused) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Chip) | $V_{DD}$ | 2.4 | 3.0 | 3.6 | V | DC |
| Operating Current (9-axis) | $I_{DD}$ | — | 3.5 | 4.5 | mA | Full 9-axis active mode |
| Gyro Noise Density | $N_{gyro}$ | — | 0.01 | — | dps/√Hz | $f = 10\text{ Hz}$ |
| Accel Noise Density | $N_{accel}$ | — | 300 | — | µg/√Hz | |
| Mag Resolution | $RES_{mag}$ | — | 0.6 | — | µT/LSB | 16-bit mode |
| SPI Clock Frequency | $f_{SPI}$ | — | — | 20 | MHz | Read registers mode |

## Internal AK8963 Magnetometer I2C Bypass Setup

The internal AK8963 magnetometer is connected to an **auxiliary internal I2C bus** inside the MPU9250 package. To access the AK8963 directly from the host MCU:

1. Write `0x02` to register `0x37` (`INT_PIN_CFG` register: Bit 1 `BYPASS_EN = 1`).
2. The AK8963 magnetometer becomes directly accessible on the main I2C bus at **`0x0C`**.
3. Read AK8963 Device ID from register `0x00` of address `0x0C` (returns `0x48`).

## Wiring

| MPU9250 Breakout Pin | → | Microcontroller (Arduino / ESP32) |
|---|---|---|
| `VCC` | | `3.3V` (or `5V`) |
| `GND` | | `GND` |
| `SCL` | | `SCL` (A5 on Uno, GPIO22 on ESP32) |
| `SDA` | | `SDA` (A4 on Uno, GPIO21 on ESP32) |
| `NCS` | | `3.3V` (keep HIGH for I2C mode) |
| `AD0` | | `GND` (sets default I2C address `0x68`) |

## Common mistakes

- **Forgetting to enable I2C Bypass Mode:** Attempting to communicate with the AK8963 magnetometer at I2C address `0x0C` before enabling `BYPASS_EN` on register `0x37` will fail with I2C address errors.
- **Floating SPI Chip Select (`NCS`):** Leaving `NCS` disconnected can cause the MPU9250 to inadvertently drop out of I2C mode into SPI mode due to noise. Tie `NCS` to `VCC` when using I2C.
- **Reading AK8963 status register (`ST2`) omission:** After reading 6 bytes of magnetometer data (`0x03`–`0x08`), software **MUST read register `0x09` (`ST2`)** to unlock the data registers for the next measurement conversion.

## Notes

- For high-speed Flight Controller applications ($>1\text{ kHz}$ update loop), use 4-wire SPI mode instead of I2C.
