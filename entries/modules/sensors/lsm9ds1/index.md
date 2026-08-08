## Overview

The **LSM9DS1** is a 9-degrees-of-freedom (9-DoF) System-in-Package (SiP) motion sensor manufactured by STMicroelectronics. It combines a 3-axis digital accelerometer, a 3-axis digital gyroscope, and a 3-axis digital magnetometer into a single $3.5 \times 3.0\text{ mm}$ package.

Outputting 16-bit resolution data over $I^2C$ or SPI, the LSM9DS1 enables full 3D orientation tracking (heading, pitch, and roll) using sensor-fusion algorithms (like Madgwick or Mahony filters). It is standard equipment in robotics navigation, drone AHRS flight controllers, virtual reality controllers, and space/satellite payload tracking.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.0 V DC (breakout module with LDO) |
| **IC supply voltage (`VDD`)** | 1.9 V to 3.6 V DC |
| **Interface** | $I^2C$ (up to 400 kHz) & 3-Wire / 4-Wire SPI (up to 10 MHz) |
| **$I^2C$ Address (Accel/Gyro)**| `0x6B` (Default; `0x6A` alternate) |
| **$I^2C$ Address (Magnetometer)**| `0x1E` (Default; `0x1C` alternate) |
| **Accel ranges** | $\pm 2g, \pm 4g, \pm 8g, \pm 16g$ |
| **Gyro ranges** | $\pm 245\text{ dps}, \pm 500\text{ dps}, \pm 2000\text{ dps}$ |
| **Mag ranges** | $\pm 4\text{ Gauss}, \pm 8\text{ Gauss}, \pm 12\text{ Gauss}, \pm 16\text{ Gauss}$ |
| **Current draw** | 4.6 mA active (all 9 axes enabled) / $4\ \mu\text{A}$ power-down |

## Pinout

Breakout modules expose a 10-pin or 12-pin 0.1" (2.54 mm) header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SCL` / `SPC` | Digital Input | $I^2C$ Clock / SPI Clock |
| 4 | `SDA` / `SDI` | Digital Input / Output | $I^2C$ Data / SPI Serial Data Input |
| 5 | `CSAG` | Digital Input | Chip Select for Accel/Gyro (High = $I^2C$ mode) |
| 6 | `CSM` | Digital Input | Chip Select for Magnetometer (High = $I^2C$ mode) |
| 7 | `SDOAG` | Digital Output | $I^2C$ Address Bit for Accel/Gyro (Low = `0x6A`, High = `0x6B`) |
| 8 | `SDOM` | Digital Output | $I^2C$ Address Bit for Magnetometer (Low = `0x1C`, High = `0x1E`) |
| 9 | `INT1` | Digital Output | Interrupt 1 line (Accel/Gyro) |
| 10 | `INT_M` | Digital Output | Interrupt line (Magnetometer) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{CC}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with LDO |
| Active Supply Current | $I_{CC}$ | — | 4.6 | 6.0 | mA | Accel + Gyro + Mag active |
| Accel Sensitivity ($\pm 2g$) | $S_{acc}$ | — | 0.061 | — | mg/LSB | 16-bit output |
| Gyro Sensitivity ($\pm 245\text{ dps}$)| $S_{gyro}$ | — | 8.75 | — | mdps/LSB | 16-bit output |
| Mag Sensitivity ($\pm 4\text{ Gauss}$) | $S_{mag}$ | — | 0.14 | — | mGauss/LSB | 16-bit output |
| Max Accel ODR | $f_{ODR\_acc}$ | 14.9 | — | 952 | Hz | Configurable |
| Max Gyro ODR | $f_{ODR\_gyro}$| 14.9 | — | 952 | Hz | Configurable |
| Max Mag ODR | $f_{ODR\_mag}$ | 0.625| — | 80 | Hz | Configurable |

## Dual $I^2C$ Devices in One Package

The LSM9DS1 contains **two distinct $I^2C$ sub-devices** inside the same silicon package:
1. **Accelerometer & Gyroscope engine:** Default $I^2C$ address **`0x6B`** (`WHO_AM_I` register `0x0F` returns `0x68`).
2. **Magnetometer engine:** Default $I^2C$ address **`0x1E`** (`WHO_AM_I_M` register `0x0F` returns `0x3D`).

## Wiring

| LSM9DS1 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Module includes 3.3V regulator |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |
| `CSAG`| | 3.3V / 5V | 3.3V | **Pull High for $I^2C$ mode** |
| `CSM` | | 3.3V / 5V | 3.3V | **Pull High for $I^2C$ mode** |

## Example

```cpp
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_LSM9DS1.h>

Adafruit_LSM9DS1 lsm = Adafruit_LSM9DS1();

void setup() {
  Serial.begin(115200);
  Serial.println("LSM9DS1 9-DOF test");

  // Initialize I2C mode
  if (!lsm.begin()) {
    Serial.println("Could not find LSM9DS1! Check CSAG and CSM pins.");
    while (1);
  }
  Serial.println("LSM9DS1 initialized successfully.");
  
  lsm.setupAccel(lsm.LSM9DS1_ACCELRANGE_2G);
  lsm.setupMag(lsm.LSM9DS1_MAGGAIN_4GAUSS);
  lsm.setupGyro(lsm.LSM9DS1_GYROSCALE_245DPS);
}

void loop() {
  lsm.read();
  
  sensors_event_t a, m, g, temp;
  lsm.getEvent(&a, &m, &g, &temp);

  Serial.print("Accel X: "); Serial.print(a.acceleration.x); Serial.print(" m/s^2\t");
  Serial.print("Gyro X: "); Serial.print(g.gyro.x); Serial.print(" rad/s\t");
  Serial.print("Mag X: "); Serial.print(m.magnetic.x); Serial.println(" uT");

  delay(200);
}
```

## Common mistakes

- **Leaving `CSAG` or `CSM` floating:** Leaving either Chip Select pin unconnected drops the corresponding sub-device into SPI mode, making address `0x6B` or `0x1E` unresponsive over $I^2C$.
- **Not performing magnetometer hard-iron calibration:** Nearby metal, battery leads, or PCB ground planes induce static magnetic offsets. Software calibration must compute offset vectors ($V_x, V_y, V_z$) to center magnetometer readings.

## Notes

- **LSM9DS1 vs MPU9250:** The LSM9DS1 is STMicroelectronics' primary competitor to the InvenSense MPU9250 9-DoF IMU.
