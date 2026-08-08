## Overview

The **BNO055** is a 9-degree-of-freedom (9-DOF) System in Package (SiP) orientation sensor manufactured by Bosch Sensortec. It integrates a 3-axis 14-bit accelerometer, a 3-axis 16-bit gyroscope, a 3-axis geomagnetic sensor, and an internal 32-bit ARM Cortex-M0+ microcontroller running Bosch's **BSX3.0 FusionLib** sensor fusion software.

Unlike traditional raw IMUs (such as MPU6050) that require complex external Kalman filtering software on the host MCU, the BNO055 processes raw sensor signals onboard and outputs absolute orientation directly in **Quaternions**, **Euler angles** (Heading, Roll, Pitch), or **Rotation Matrices**.

## Quick reference

| | |
|---|---|
| **Module VCC** | 3.3 V to 5.0 V DC (onboard LDO) |
| **Chip VDD / VDDIO** | 2.4 V to 3.6 V DC |
| **Degrees of Freedom (DOF)** | 9-DOF (3-axis Accel + 3-axis Gyro + 3-axis Magnetometer) |
| **Onboard Coprocessor** | 32-bit ARM Cortex-M0+ running BSX3.0 sensor fusion algorithm |
| **Direct Output Data** | Quaternions, Euler Angles, Rotation Matrix, Gravity Vector, Linear Accel |
| **Communication interfaces** | I2C (default `0x28` or `0x29`, up to 400 kHz), UART |
| **Active current draw** | 12.5 mA (Fusion Mode), 40 µA (Suspend Mode) |

## Pinout

### Standard BNO055 Breakout Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VIN` | Power | Supply voltage (+3.3 V to +5.0 V DC) |
| 2 | `3VO` | Power Output | Regulated +3.3 V output from onboard LDO |
| 3 | `GND` | Power | Ground (0 V) |
| 4 | `SDA` | Digital I/O | I2C Serial Data line |
| 5 | `SCL` | Digital Input | I2C Serial Clock line (Requires I2C Clock Stretching!) |
| 6 | `RST` | Digital Input | Active-LOW Hardware Reset pin |
| 7 | `ADR` | Digital Input | I2C Address select (`LOW` = `0x28`, `HIGH` = `0x29`) |
| 8 | `INT` | Digital Output | Interrupt output pin |
| 9 | `PS0` | Digital Input | Protocol Select pin 0 (`LOW` for I2C) |
| 10 | `PS1` | Digital Input | Protocol Select pin 1 (`LOW` for I2C) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 2.4 | 3.0 | 3.6 | V | DC |
| Operating Current (NDOF) | $I_{DD}$ | — | 12.5 | 15.0 | mA | Full 9-DOF sensor fusion mode |
| Suspend Current | $I_{susp}$ | — | 40 | 50 | µA | Suspend mode |
| Accel Range | $FS_{acc}$ | $\pm 2$ | — | $\pm 16$ | g | Programmable |
| Gyro Range | $FS_{gyro}$ | $\pm 125$ | — | $\pm 2000$ | °/s | Programmable |
| Mag Field Range | $FS_{mag}$ | — | $\pm 1300$ | — | µT | Microtesla |
| Euler Angle Resolution | $RES_{euler}$ | — | 0.0625 | — | ° | $1/16\text{ degree per LSB}$ |
| Quaternion Resolution | $RES_{quat}$ | — | 1/16384 | — | LSB | Unit quaternion |

## Operating modes & Register map

### Key Operating Modes (`OPR_MODE` Register `0x3D`)

| Mode Hex | Mode Name | Description |
|---|---|---|
| `0x00` | `CONFIGMODE` | Configuration Mode (Required to modify sensor settings) |
| `0x08` | `IMU` | 6-DOF fusion (Accel + Gyro; relative orientation, fast) |
| `0x0B` | `NDOF_FMC_OFF` | 9-DOF fusion without Fast Magnetometer Calibration |
| `0x0C` | `NDOF` | Full 9-DOF absolute orientation fusion (Euler / Quaternion) |

### Key Output Registers (Page 0)

| Address | Register | Description |
|---|---|---|
| `0x00` | `CHIP_ID` | Reads `0xA0` (BNO055 identification byte) |
| `0x1A`..`0x1F` | `EUL_HEADING` / `ROLL` / `PITCH` | Read Euler angles ($1\text{ LSB} = 1/16^\circ$) |
| `0x20`..`0x27` | `QUA_DATA_W`..`Z` | Read 16-bit Quaternion vector ($w, x, y, z$) |
| `0x35` | `GRV_DATA` | Gravity Vector output ($1\text{ LSB} = 1\text{ m/s}^2$) |
| `0x39` | `SYS_STATUS` | System status code |
| `0x35` | `CALIB_STAT` | Calibration status byte (Bits [7:6] Sys, [5:4] Gyro, [3:2] Accel, [1:0] Mag) |

## Wiring

| BNO055 Breakout Pin | → | Microcontroller (Arduino Uno / ESP32) |
|---|---|---|
| `VIN` | | `5V` (or `3.3V`) |
| `GND` | | `GND` |
| `SDA` | | `SDA` (A4 on Uno, GPIO21 on ESP32) |
| `SCL` | | `SCL` (A5 on Uno, GPIO22 on ESP32) |
| `ADR` | | `GND` (for default I2C address `0x28`) |

> [!WARNING]
> Requires I2C Clock Stretching Support:
> The BNO055 internal Cortex-M0+ processor uses **I2C Clock Stretching** while processing sensor fusion calculations. Some microcontrollers (such as ESP8266 or early Raspberry Pi hardware I2C drivers) do not handle clock stretching properly. Use software I2C (bit-banging) or adjust clock speeds if I2C read timeouts occur.

## Common mistakes

- **Not waiting for sensor calibration:** On cold boot, the internal fusion engine reports calibration status `0` for system, gyro, accel, and mag. Perform a "figure-8" movement in air to calibrate the magnetometer and achieve `CALIB_STAT = 0xFF` (3/3 calibration across all sensors).
- **Modifying registers while in NDOF fusion mode:** Register changes (like changing units or axis mapping) are IGNORED unless the chip is first placed into `CONFIGMODE` (`0x00`).
- **Ignoring I2C Clock Stretching:** If the host MCU forces I2C clock cycles without monitoring SCL stretching, data bytes will be corrupted.

## Notes

- Euler angles suffer from **Gimbal Lock** at $\pm 90^\circ$ pitch. For 3D orientation in 360° space, always use 4-element **Quaternions** (`QUA_DATA`).
