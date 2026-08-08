## Overview

The **MPU-6050** is a 6-axis MotionTracking sensor manufactured by InvenSense (now TDK). It combines a 3-axis MEMS gyroscope, a 3-axis MEMS accelerometer, an internal temperature sensor, and an onboard hardware **Digital Motion Processor (DMP)** on a single silicon die.

Breakout boards (such as the GY-521) include an onboard 3.3 V low-dropout (LDO) regulator, enabling safe operation with 5 V or 3.3 V microcontrollers, along with I2C pull-up resistors and decoupling capacitors.

## Quick reference

| | |
|---|---|
| **Module VCC** | 3.3 V to 5.0 V DC (onboard LDO) |
| **Sensor VDD (chip)** | 2.375 V to 3.46 V DC |
| **Communication interface** | I2C (up to 400 kHz Fast Mode) |
| **I2C address** | `0x68` (AD0 = LOW) / `0x69` (AD0 = HIGH) |
| **Gyroscope range** | $\pm 250, \pm 500, \pm 1000, \pm 2000\text{ }^\circ/\text{s}$ |
| **Accelerometer range** | $\pm 2\text{ g}, \pm 4\text{ g}, \pm 8\text{ g}, \pm 16\text{ g}$ |
| **ADC resolution** | 16-bit (per axis for gyro & accel) |

## Pinout

### Standard GY-521 Breakout Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage input (+3.3 V to +5.0 V) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SCL` | Digital Input | I2C Clock line |
| 4 | `SDA` | Digital I/O | I2C Data line |
| 5 | `XDA` | Digital I/O | Auxiliary I2C Data line (master for external magnetometer) |
| 6 | `XCL` | Digital Output | Auxiliary I2C Clock line |
| 7 | `AD0` | Digital Input | I2C Address select (`LOW` = `0x68`, `HIGH` = `0x69`) |
| 8 | `INT` | Digital Output | Interrupt output pin (Active-HIGH, programmable) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Chip Supply Voltage | $V_{DD}$ | 2.375 | 3.3 | 3.46 | V | |
| Operating Current | $I_{DD}$ | — | 3.8 | 4.2 | mA | Gyro + Accel active |
| Sleep Current | $I_{sleep}$ | — | 5 | 10 | µA | Sleep mode enabled |
| Gyro Full Scale Range | $FS_{GYRO}$ | $\pm 250$ | — | $\pm 2000$ | °/s | User selectable |
| Gyro Sensitivity | $S_{GYRO}$ | 16.4 | — | 131 | LSB/(°/s) | $131 \text{ at } \pm 250^\circ/\text{s}$, $16.4 \text{ at } \pm 2000^\circ/\text{s}$ |
| Accel Full Scale Range | $FS_{ACCEL}$ | $\pm 2$ | — | $\pm 16$ | g | User selectable |
| Accel Sensitivity | $S_{ACCEL}$ | 2048 | — | 16384 | LSB/g | $16384 \text{ at } \pm 2\text{g}$, $2048 \text{ at } \pm 16\text{g}$ |
| Temperature Range | $T_{OP}$ | -40 | — | 85 | °C | |

## Register map

| Address | Register | Access | Reset | Description |
|---|---|---|---|---|
| `0x1B` | `GYRO_CONFIG` | R/W | `0x00` | Gyroscope full scale select (`FS_SEL` bits [4:3]) |
| `0x1C` | `ACCEL_CONFIG` | R/W | `0x00` | Accelerometer full scale select (`AFS_SEL` bits [4:3]) |
| `0x3B` | `ACCEL_XOUT_H` | R | `0x00` | Accelerometer X-axis High byte (Read 6 bytes for X,Y,Z) |
| `0x41` | `TEMP_OUT_H` | R | `0x00` | Temperature High byte (Read 2 bytes) |
| `0x43` | `GYRO_XOUT_H` | R | `0x00` | Gyroscope X-axis High byte (Read 6 bytes for X,Y,Z) |
| `0x6B` | `PWR_MGMT_1` | R/W | `0x40` | Power management 1 (Bit 6 `SLEEP` = 1 on reset) |
| `0x75` | `WHO_AM_I` | R | `0x68` | I2C Device ID register (returns `0x68`) |

## Wiring

| GY-521 (MPU-6050) | → | Microcontroller (Arduino Uno / ESP32) | Notes |
|---|---|---|---|
| `VCC` | | `5V` (or `3.3V`) | Power input to onboard 3.3V regulator |
| `GND` | | `GND` | Ground |
| `SCL` | | `SCL` (A5 on Uno, GPIO22 on ESP32) | I2C Clock |
| `SDA` | | `SDA` (A4 on Uno, GPIO21 on ESP32) | I2C Data |
| `AD0` | | `GND` | Pull LOW for address `0x68`, HIGH for `0x69` |

> [!WARNING]
> The MPU-6050 powers up in **SLEEP mode** (`PWR_MGMT_1` = `0x40`). Software MUST clear the sleep bit by writing `0x00` to register `0x6B` before sensor readings will update.

## Common mistakes

- **Forgetting to wake the chip:** Sensor outputs will remain static zero or frozen values if `PWR_MGMT_1` register (`0x6B`) is not written with `0x00` upon initialization.
- **Incorrect 16-bit signed integer conversion:** Accelerometer and gyroscope data registers are 16-bit two's complement numbers stored in Big-Endian format (`HIGH` byte first). Re-assemble bytes using `(int16_t)((high << 8) | low)`.
- **Gyroscope drift:** Raw gyroscope values accumulate integration drift over time. Combine accelerometer and gyroscope readings using a **Complementary Filter** or **Kalman Filter**, or use the DMP.

## Notes

- Temperature calculation formula: $\text{Temperature in } ^\circ\text{C} = \frac{\text{TEMP\_OUT}}{340} + 36.53$.
