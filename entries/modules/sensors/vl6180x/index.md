## Overview

The **VL6180X** is STMicroelectronics' 1st-generation FlightSense 3-in-1 smart optical module. Packaged in a compact $4.8 \times 2.8\text{ mm}$ optical LGA housing, it integrates an **850 nm VCSEL laser emitter**, a Time-of-Flight (ToF) proximity rangefinder, and a high-accuracy 16-bit **Ambient Light Sensor (ALS)**.

Unlike IR intensity proximity sensors that are heavily affected by target color or reflectivity, the VL6180X measures the precise round-trip flight time of light. It measures short-range distance from **$0\text{ mm}$ to $100\text{ mm}$** ($10\text{ cm}$ nominal, up to $400\text{ mm}$ under dark conditions) with 1 mm resolution, alongside ambient lux levels from **$0.1\text{ Lux}$ to $100,000\text{ Lux}$** over $I^2C$ (**`0x29`**).

## Quick reference

| | |
|---|---|
| **Operating voltage (`VIN`)** | 3.3 V to 5.0 V DC (breakout includes 3.3V LDO regulator) |
| **IC supply voltage (`VDD`)** | 2.6 V to 3.0 V DC (2.8 V nominal) |
| **Interface** | $I^2C$ Fast-Mode (up to 400 kHz) |
| **Default $I^2C$ address** | `0x29` |
| **Proximity Range** | $0\text{ mm}$ to $100\text{ mm}$ ($0\text{ to }10\text{ cm}$ standard, up to $40\text{ cm}$) |
| **Ambient Light Sensor (ALS)**| $0.1\text{ Lux}$ to $100,000\text{ Lux}$ (16-bit output) |
| **Laser Emitter** | 850 nm VCSEL (Class 1 Eye Safe) |
| **Distance Resolution** | 1.0 mm absolute distance accuracy |
| **Control Pins** | `SHDN` / `GPIO0` (Active-Low shutdown), `GPIO1` (Interrupt output) |

## Pinout

Breakout module 6-pin header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VIN` | Power | Supply power input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 4 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 5 | `GPIO0` / `SHDN`| Digital Input | Active-Low shutdown input |
| 6 | `GPIO1`| Digital Output | Active-Low programmable interrupt output |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{VIN}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with LDO |
| Ranging Current | $I_{ranging}$| — | 15 | 25 | mA | Active 10 Hz ranging |
| Standby Current | $I_{sd}$ | — | 1.0 | 5.0 | µA | `SHDN` tied to GND |
| Proximity Distance Range| $Dist$ | 0 | — | 100 | mm | Standard target (100% white) |
| ALS Measurement Range | $ALS$ | 0.1 | — | 100000 | Lux | High dynamic range |
| Convergence Time | $t_{conv}$ | — | 10 | 15 | ms | Distance measurement cycle |

## Distance vs Ambient Light Dual Operation

The VL6180X contains two independent sensor subsystems:
1. **Time-of-Flight Rangefinder:** Measures distance in millimeters regardless of target reflectance (black paper vs white paper vs mirror).
2. **Ambient Light Photodiode:** Measures environmental illuminance (Lux) with internal gain selection ($1.0 \times \dots 40.0 \times$).

## Wiring

| VL6180X Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VIN` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |

## Example (Adafruit_VL6180X Library)

```cpp
#include <Wire.h>
#include "Adafruit_VL6180X.h"

Adafruit_VL6180X vl = Adafruit_VL6180X();

void setup() {
  Serial.begin(115200);
  Serial.println("Adafruit VL6180X ToF & ALS Test");

  if (!vl.begin()) {
    Serial.println("Failed to find VL6180X sensor! Check I2C wiring.");
    while (1);
  }
}

void loop() {
  float lux = vl.readLux(VL6180X_ALS_GAIN_5);
  uint8_t range = vl.readRange();
  uint8_t status = vl.readRangeStatus();

  if (status == VL6180X_ERROR_NONE) {
    Serial.print("Distance: "); Serial.print(range); Serial.print(" mm | ");
  }
  Serial.print("Ambient Light: "); Serial.print(lux); Serial.println(" Lux");

  delay(200);
}
```

## Common mistakes

- **Expecting long-range distance (> 10 cm):** The VL6180X is optimized for short-range precision ($0\dots 10\text{ cm}$). For longer distances up to 2m or 4m, use the VL53L0X or VL53L1X instead.
- **Forgetting address collision with other ToF sensors:** VL6180X uses fixed address `0x29`, colliding with VL53L0X and VL53L1X if placed on the same $I^2C$ bus without using `XSHUT`/`SHDN` pin re-addressing sequences.

## Notes

- **VL6180X vs VL53L0X vs VCNL4010:** VL6180X measures 0–10 cm ToF + Lux; VL53L0X measures 30 mm–2000 mm ToF; VCNL4010 measures IR reflection amplitude.
