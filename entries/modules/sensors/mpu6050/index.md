## Overview

The **MPU-6050** is a widely used 6-axis MEMS MotionTracking device designed by InvenSense (now TDK). It integrates a 3-axis MEMS gyroscope, a 3-axis MEMS accelerometer, and an onboard hardware **Digital Motion Processor (DMP)** capable of performing complex 9-axis MotionFusion calculations when paired with an external magnetometer via its auxiliary I2C bus.

Commonly available on the low-cost **GY-521** breakout module (which includes a 3.3 V LDO regulator and I2C pull-up resistors), the MPU-6050 is the primary sensor choice for hobbyist drones, self-balancing robots, flight controllers, and motion-capture systems.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 2.375 V – 3.46 V (bare IC) / 3.3 V – 5.0 V (GY-521 module) |
| **Gyroscope full-scale range** | $\pm 250$, $\pm 500$, $\pm 1000$, $\pm 2000$ °/s (user selectable) |
| **Accelerometer full-scale range** | $\pm 2g$, $\pm 4g$, $\pm 8g$, $\pm 16g$ (user selectable) |
| **ADC resolution** | 16-bit analog-to-digital converters for each axis |
| **Interface** | Fast-Mode I2C (up to 400 kHz) |
| **Default I2C address** | `0x68` (`AD0` LOW or floating) / `0x69` (`AD0` HIGH) |
| **FIFO buffer** | 1024-byte hardware FIFO buffer |

## Pinout

### Standard GY-521 Breakout Module

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (3.3 V to 5 V; onboard MIC5205 3.3 V LDO regulator) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SCL` | Digital Input | I2C Primary Clock Line |
| 4 | `SDA` | Digital I/O | I2C Primary Data Line |
| 5 | `XDA` | Digital I/O | Auxiliary I2C Data Line (for external magnetometer) |
| 6 | `XCL` | Digital Output | Auxiliary I2C Clock Line |
| 7 | `AD0` | Digital Input | I2C Address Select Bit (`LOW`: 0x68, `HIGH`: 0x69) |
| 8 | `INT` | Digital Output | Programmable Interrupt Output pin (Active-HIGH) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | `VDD` | 2.375 | 3.3 | 3.46 | V | IC rating |
| Operating Current | `IDD` | — | 3.8 | 4.2 | mA | Gyro + Accel normal mode |
| Gyroscope Sensitivity (±250°/s) | `SEL_G250` | — | 131 | — | LSB/(°/s) | 16-bit ADC |
| Gyroscope Sensitivity (±2000°/s) | `SEL_G2000` | — | 16.4 | — | LSB/(°/s) | 16-bit ADC |
| Accelerometer Sensitivity (±2g) | `SEL_A2` | — | 16384 | — | LSB/g | 16-bit ADC |
| Accelerometer Sensitivity (±16g) | `SEL_A16` | — | 2048 | — | LSB/g | 16-bit ADC |
| Temperature Range | `TA` | -40 | — | +85 | °C | Ambient operating range |

## Register map

| Address | Register | Access | Reset | Description |
|---|---|---|---|---|
| `0x19` | `SMPLRT_DIV` | R/W | `0x00` | Sample Rate Divider ($f_{\text{sample}} = \frac{1\text{ kHz}}{1 + \text{SMPLRT\_DIV}}$) |
| `0x1A` | `CONFIG` | R/W | `0x00` | Digital Low Pass Filter (DLPF) and External Frame Sync config |
| `0x1B` | `GYRO_CONFIG` | R/W | `0x00` | Gyroscope Self-Test & Full-Scale Range Select (`FS_SEL`) |
| `0x1C` | `ACCEL_CONFIG` | R/W | `0x00` | Accelerometer Self-Test & Full-Scale Range Select (`AFS_SEL`) |
| `0x3B`–`0x40` | `ACCEL_XOUT_H..L` | R | — | 16-bit Accelerometer measurements (X, Y, Z) |
| `0x41`–`0x42` | `TEMP_OUT_H..L` | R | — | 16-bit Internal Temperature Sensor value |
| `0x43`–`0x48` | `GYRO_XOUT_H..L` | R | — | 16-bit Gyroscope measurements (X, Y, Z) |
| `0x6B` | `PWR_MGMT_1` | R/W | `0x40` | Power Management 1 (Sleep Mode control, Clock source select) |
| `0x75` | `WHO_AM_I` | R | `0x68` | 6-bit I2C Address verification register (returns `0x68`) |

## Wiring

| GY-521 Module | :i-lucide-move-right: | Microcontroller (Arduino Uno / ESP32) |
|---|---|---|
| `VCC` | | 5V (or 3.3V) |
| `GND` | | GND |
| `SCL` | | I2C SCL (A5 on Uno / GPIO22 on ESP32) |
| `SDA` | | I2C SDA (A4 on Uno / GPIO21 on ESP32) |
| `AD0` | | GND (Address `0x68`) |

## Common mistakes

- **Device stuck in Sleep Mode:** By default, the MPU-6050 powers up in Sleep Mode (`PWR_MGMT_1` register = `0x40`). You MUST clear bit 6 of register `0x6B` (write `0x00`) during setup to enable sensor measurements.
- **Reading raw values without dividing by sensitivity:** Raw 16-bit ADC integers must be divided by the LSB scale factor corresponding to the configured range (e.g. divide by 131.0 for gyro ±250°/s, divide by 16384.0 for accel ±2g).
- **Ignoring sensor calibration drift:** Gyroscope outputs exhibit zero-rate bias drift over time and temperature. A software zero-offset calibration routine must be run at startup while keeping the sensor completely still.

## Notes

- **Internal Temperature Formula:** Temperature in °C is computed from `TEMP_OUT` raw data via:
  $$\text{Temperature (°C)} = \frac{\text{TEMP\_OUT}}{340.0} + 36.53$$
