## Overview

The **VL53L1X** is STMicroelectronics' 2nd-generation FlightSense Time-of-Flight (ToF) laser ranging sensor. Improving significantly upon the earlier VL53L0X (which was limited to 2 meters), the VL53L1X extends maximum absolute distance measurement up to **4.0 meters (4000 mm)** while operating at sampling rates up to **50 Hz**.

Featuring a **940 nm VCSEL (Vertical Cavity Surface Emitting Laser)** class-1 emitter, an integrated Single Photon Avalanche Diode (SPAD) detector array, and programmable **Region of Interest (ROI)** control (allowing users to reduce the $27^\circ$ Field of View down to $16^\circ$ or create multi-zone spatial gesture grids), the VL53L1X outputs millimeter-accurate distance readings over $I^2C$ (**`0x29`**).

## Quick reference

| | |
|---|---|
| **Operating voltage (`VIN`)** | 3.3 V to 5.0 V DC (breakout module with 3.3V LDO regulator) |
| **IC supply voltage (`AVDD`)**| 2.6 V to 3.5 V DC (3.3 V nominal) |
| **Interface** | $I^2C$ (Fast-Mode up to 400 kHz) |
| **Default $I^2C$ address** | `0x29` (Software programmable to any 7-bit address) |
| **Distance Range** | $40\text{ mm}$ to $4000\text{ mm}$ ($4\text{ meters}$) |
| **Ranging Distance Modes** | Short ($0\dots 1.3\text{m}$), Medium ($0\dots 3.0\text{m}$), Long ($0\dots 4.0\text{m}$) |
| **Laser Emitter** | $940\text{ nm}$ VCSEL (Eye-safe Class 1 laser) |
| **Full Field of View (FOV)** | $27^\circ$ (Programmable ROI array downsizing to $16^\circ$) |
| **Max Ranging Speed** | Up to 50 Hz (20 ms timing budget) |
| **Control Pins** | `XSHUT` (Active-Low shutdown / address reset pin) |

## Pinout

Breakout module header & Qwiic / STEMMA QT connectors:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VIN` | Power | Supply power input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 4 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 5 | `XSHUT`| Digital Input | Active-Low shutdown input (Pull Low for hardware reset / I2C re-addressing) |
| 6 | `GPIO1`| Digital Output | Active-Low interrupt output (New data sample ready) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{VIN}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with LDO |
| Active Ranging Current | $I_{CC}$ | — | 20 | 32 | mA | Active 50 Hz ranging |
| Shutdown Current | $I_{sd}$ | — | 5.0 | 15.0 | µA | `XSHUT` tied to GND |
| Short Distance Range | $Dist_{short}$| 40 | — | 1300 | mm | High ambient light resistance |
| Long Distance Range | $Dist_{long}$ | 40 | — | 4000 | mm | Dark room / low ambient light |
| Distance Accuracy (Short)| $Acc_{short}$| -20 | $\pm 5$ | +20 | mm | Within 0 to 1300 mm range |

## Short vs Long Distance Ranging Modes

- **Short Distance Mode ($0\text{ -- }1.3\text{ m}$):** Immune to strong ambient sunlight outdoor interference up to 200,000 Lux.
- **Medium Distance Mode ($0\text{ -- }3.0\text{ m}$):** Balanced indoors/outdoors mode.
- **Long Distance Mode ($0\text{ -- }4.0\text{ m}$):** Achieves maximum 4-meter range under indoor lighting or dark environments.

## Wiring

| VL53L1X Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VIN` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |
| `XSHUT`| | Digital D4 | GPIO 16 | Optional shutdown / re-addressing pin |

## Example (Pololu VL53L1X Library)

```cpp
#include <Wire.h>
#include <VL53L1X.h>

VL53L1X sensor;

void setup() {
  Serial.begin(115200);
  Wire.begin();
  Wire.setClock(400000); // 400 kHz Fast I2C

  sensor.setTimeout(500);
  if (!sensor.init()) {
    Serial.println("Failed to detect VL53L1X sensor! Check I2C wiring.");
    while (1);
  }

  // Use Long distance mode and 50ms timing budget
  sensor.setDistanceMode(VL53L1X::Long);
  sensor.setMeasurementTimingBudget(50000);
  sensor.startContinuous(50);
}

void loop() {
  uint16_t distance_mm = sensor.read();

  if (sensor.timeoutOccurred()) {
    Serial.println("VL53L1X Read Timeout!");
  } else {
    Serial.print("Distance: "); Serial.print(distance_mm); Serial.println(" mm");
  }
}
```

## Common mistakes

- **Leaving protective cover sticker over the lens:** VL53L1X breakout modules ship with an ultra-thin yellow/orange protective film cover over the optical aperture. Failing to peel off this film causes constant $10\text{ mm}$ false ranging readings.
- **Conflating VL53L0X and VL53L1X libraries:** While both chips use default $I^2C$ address `0x29`, the internal register maps of the VL53L1X are completely different from the VL53L0X. Use dedicated `VL53L1X` libraries.

## Notes

- **VL53L1X vs VL53L0X vs VL53L5CX:** VL53L0X (2m range single-zone); **VL53L1X (4m range single-zone with ROI customization)**; VL53L5CX (8x8 multizone 64-pixel ToF matrix).
