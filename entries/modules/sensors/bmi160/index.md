## Overview

The **BMI160** is an ultra-low power 16-bit 6-axis Inertial Measurement Unit (IMU) manufactured by Bosch Sensortec. Housed in a miniature $2.5 \times 3.0\text{ mm}$ 14-pin LGA package, it integrates a 3-axis accelerometer ($\pm 2g \dots \pm 16g$) and a 3-axis angular rate gyroscope ($\pm 125 \dots \pm 2000\text{ dps}$).

Engineered for mobile devices, wearables, and battery-powered IoT nodes, the BMI160 operates at a full active current of just **$950\ \mu\text{A}$** (both accelerometer and gyroscope enabled). It features an integrated 1024-byte hardware FIFO buffer, an autonomous step counter (pedometer), and hardware gesture recognition (any-motion, double-tap, orientation detection).

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.0 V DC (breakout with 3.3V LDO) |
| **IC supply voltage (`VDD`)** | 1.71 V to 3.6 V DC (1.8 V or 3.3 V nominal) |
| **Interface** | $I^2C$ (up to 1.0 MHz) & 3-Wire / 4-Wire SPI (up to 10 MHz) |
| **Default $I^2C$ address** | `0x68` (`SDO` pin Low to GND) |
| **Alternate $I^2C$ address** | `0x69` (`SDO` pin High to 3.3V) |
| **Accel ranges** | $\pm 2g, \pm 4g, \pm 8g, \pm 16g$ |
| **Gyro ranges** | $\pm 125\text{ dps}, \pm 250\text{ dps}, \pm 500\text{ dps}, \pm 1000\text{ dps}, \pm 2000\text{ dps}$ |
| **Active current draw** | $950\ \mu\text{A}$ active (Accel + Gyro) / $3\ \mu\text{A}$ suspend |

## Pinout

Standard 7-pin or 8-pin 0.1" (2.54 mm) breakout module header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `SCL` / `SCK` | Digital Input | $I^2C$ Serial Clock / SPI Clock |
| 4 | `SDA` / `SDI` | Digital Input / Output | $I^2C$ Serial Data / SPI Serial Data Input |
| 5 | `SDO` / `ADDR`| Digital Output | SPI Data Out / $I^2C$ Address Select (Low = `0x68`, High = `0x69`) |
| 6 | `CS` | Digital Input | SPI Chip Select (High = $I^2C$ mode, Low = SPI mode) |
| 7 | `INT1` | Digital Output | Interrupt line 1 (Motion / Tap / Step counter interrupt) |
| 8 | `INT2` | Digital Output | Interrupt line 2 (Data ready / FIFO watermark) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{CC}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with LDO |
| Active Supply Current | $I_{CC}$ | — | 950 | 1200 | µA | Accel + Gyro active |
| Low-Power Accel Current | $I_{acc\_lp}$| — | 18 | 30 | µA | 10 Hz sampling rate |
| Accel Sensitivity ($\pm 2g$) | $S_{acc}$ | — | 16384 | — | LSB/g | 16-bit 2's complement |
| Gyro Sensitivity ($\pm 250\text{ dps}$)| $S_{gyro}$ | — | 131.2 | — | LSB/dps | 16-bit 2's complement |
| FIFO Buffer Size | $FIFO$ | — | 1024 | — | Bytes | Configurable frame storage |

## $I^2C$ Register Access & Math

| Address | Register | Access | Description |
|---|---|---|---|
| `0x00` | `CHIP_ID` | Read | Returns `0xD1` (Chip ID for BMI160) |
| `0x0C`–`0x11` | `GYR_X/Y/Z` | Read | 16-bit signed Gyroscope data |
| `0x12`–`0x17` | `ACC_X/Y/Z` | Read | 16-bit signed Accelerometer data |
| `0x7E` | `CMD` | Write | Command register (`0x11` = Accel Normal, `0x15` = Gyro Normal) |

$$ \text{Accel (g)} = \frac{\text{Raw 16-bit Signed Value}}{16384} \quad (\text{at } \pm 2g \text{ range}) $$

$$ \text{Gyro (dps)} = \frac{\text{Raw 16-bit Signed Value}}{131.2} \quad (\text{at } \pm 250\text{ dps} \text{ range}) $$

## Wiring

| BMI160 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Module includes 3.3V LDO |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |
| `CS`  | | 3.3V / 5V | 3.3V | **Pull High for $I^2C$ mode** |

## Example (Arduino BMI160 Library)

```cpp
#include <Wire.h>
#include <BMI160Gen.h>

const int i2c_addr = 0x68;

void setup() {
  Serial.begin(115200);
  while (!Serial);

  Serial.println("Initializing BMI160 IMU...");
  BMI160.begin(BMI160Gen::I2C_MODE, i2c_addr);

  // Set ranges
  BMI160.setGyroRange(250);   // +/- 250 dps
  BMI160.setAccelerometerRange(2); // +/- 2g

  Serial.println("BMI160 initialized.");
}

void loop() {
  int gx, gy, gz;
  int ax, ay, az;

  // Read raw 16-bit sensor data
  BMI160.readMotionSensor(ax, ay, az, gx, gy, gz);

  float accelX = ax / 16384.0;
  float gyroX  = gx / 131.2;

  Serial.print("Accel X: "); Serial.print(accelX); Serial.print(" g\t");
  Serial.print("Gyro X: "); Serial.print(gyroX); Serial.println(" dps");

  delay(200);
}
```

## Common mistakes

- **Leaving `CS` floating in $I^2C$ mode:** Tie `CS` High to 3.3V to prevent random fallbacks into SPI mode.
- **Forgetting power-up command sequence (`0x7E`):** Unlike MPU6050, the BMI160 powers up in Suspend mode. The host MCU must write command `0x11` (Accel Normal) and `0x15` (Gyro Normal) to register `0x7E` to activate the sensors.

## Notes

- **BMI160 vs MPU6050:** BMI160 draws $<1\text{ mA}$ (vs MPU6050's $3.8\text{ mA}$), includes a 1024-byte hardware FIFO, and incorporates an integrated hardware pedometer.
