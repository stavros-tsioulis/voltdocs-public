## Overview

The **VCNL4010** is a fully integrated proximity and ambient light sensor (ALS) manufactured by Vishay Intertechnology. Packaged in a compact $3.95 \times 3.95\text{ mm}$ QFN package, it combines an internal **$890\text{ nm}$ Infrared (IR) emitter LED**, an IR proximity photodiode, an ambient light photodiode matching the human eye response, and a 16-bit low-noise Delta-Sigma ADC over an $I^2C$ bus (`0x13`).

Designed to detect object reflection and distance from **$1\text{ mm}$ to $200\text{ mm}$**, the VCNL4010 features programmable IR LED drive currents ($10\text{ mA}$ to $200\text{ mA}$) and automatic $50\text{ Hz} / 60\text{ Hz}$ ambient light flicker rejection. It is widely used in smartphone screen proximity lock circuits, robot obstacle detection, and smart touchless switches.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.0 V DC (breakout includes 3.3V LDO regulator) |
| **IC supply voltage (`VDD`)** | 2.5 V to 3.6 V DC (3.3 V nominal) |
| **IR LED drive voltage (`IR_VCC`)**| 2.5 V to 5.0 V DC |
| **Interface** | $I^2C$ (Fast Mode up to 400 kHz) |
| **Fixed $I^2C$ address** | `0x13` |
| **Proximity distance range** | $1\text{ mm}$ to $200\text{ mm}$ ($0.04\text{"}$ to $8\text{"}$) |
| **IR Emitter Wavelength** | 890 nm |
| **Ambient Light Range** | 0.25 Lux to 16,383 Lux (16-bit count output) |
| **IR LED Drive Current** | 10 mA to 200 mA programmable in 10 mA steps |
| **Operating current** | $1.5\text{ mA}$ active / $1.5\ \mu\text{A}$ standby |

## Pinout

Breakout module header & STEMMA QT / Qwiic connectors:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VIN` | Power | Supply power input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 4 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 5 | `INT` | Digital Output | Active-Low interrupt output (programmable proximity threshold) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{VIN}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with LDO |
| Active Supply Current | $I_{CC}$ | — | 1.5 | 3.0 | mA | Continuous sampling state |
| Standby Current | $I_{sd}$ | — | 1.5 | 5.0 | µA | Software standby mode |
| IR Emitter Peak Wavelength| $\lambda_p$ | 870 | 890 | 910 | nm | IR LED peak emission |
| IR LED Current Programmable| $I_{LED}$ | 10 | — | 200 | mA | Configurable in register `0x83` |
| Ambient Light Resolution| $Res_{ALS}$ | — | 0.25 | — | Lux/count | 16-bit raw ALS count |

## Proximity & Ambient Light Registers

- **Command Register (`0x80`):** Enable proximity (`0x08`), enable ambient light (`0x04`), or start measurements.
- **IR LED Current Register (`0x83`):** Configures IR LED drive current ($0\dots 20 \times 10\text{ mA}$).
- **Ambient Light Data (`0x85`–`0x86`):** 16-bit ambient light count ($0\dots 65535$).
- **Proximity Data (`0x87`–`0x88`):** 16-bit proximity count (**Higher counts indicate CLOSER object distance**).

## Wiring

| VCNL4010 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VIN` | | 5V / 3.3V | 3.3V | Module includes 3.3V LDO |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |

## Example (Adafruit_VCNL4010 Library)

```cpp
#include <Wire.h>
#include "Adafruit_VCNL4010.h"

Adafruit_VCNL4010 vcnl;

void setup() {
  Serial.begin(115200);
  while (!Serial) delay(10);

  Serial.println("Adafruit VCNL4010 Proximity & ALS Test");

  if (!vcnl.begin()) {
    Serial.println("VCNL4010 not found! Check I2C wiring.");
    while (1);
  }

  // Set IR LED current to 200 mA for maximum proximity range
  vcnl.setLEDcurrent(20); // 20 * 10mA = 200mA

  Serial.println("VCNL4010 initialized.");
}

void loop() {
  uint16_t ambient = vcnl.readAmbient();
  uint16_t proximity = vcnl.readProximity();

  Serial.print("Ambient Light: "); Serial.print(ambient);
  Serial.print(" | Proximity Count: "); Serial.println(proximity);

  delay(200);
}
```

## Common mistakes

- **Interpreting proximity raw count as millimeters:** Proximity output is an uncalibrated 16-bit reflection count, not direct distance in mm. **Higher counts mean an object is CLOSER**.
- **Setting IR LED current too low:** Running at $10\text{ mA}$ limits effective proximity sensing to $<20\text{ mm}$. Set `setLEDcurrent(20)` ($200\text{ mA}$) for maximum $200\text{ mm}$ sensing range.

## Notes

- **VCNL4010 vs APDS-9960 vs VL53L0X:** VCNL4010 uses IR intensity reflection; APDS-9960 adds gesture recognition; VL53L0X uses Time-of-Flight (ToF) laser pulsing for millimeter-accurate absolute distance.
