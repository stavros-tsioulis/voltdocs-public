## Overview

The **VL53L0X** is a second-generation Time-of-Flight (ToF) laser-ranging module manufactured by STMicroelectronics under their *FlightSense* trademark. Unlike traditional IR triangulation sensors or ultrasonic rangefinders, the VL53L0X measures the precise time taken by emitted photons to bounce off an object and return to an array of Single Photon Avalanche Diodes (SPADs).

Equipped with an invisible 940 nm Vertical-Cavity Surface-Emitting Laser (VCSEL) emitter, the VL53L0X measures absolute distances up to **2.0 meters** ($2000\text{ mm}$) with millimeter precision, completely independent of target color, surface reflectivity, or ambient lighting conditions. It is the go-to distance sensor for mini sumo robots, drone altitude sensing, gesture recognition, and obstacle avoidance.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.0 V DC (breakout with onboard LDO) |
| **IC supply voltage (`VDD`)** | 2.6 V to 3.5 V DC (2.8 V nominal) |
| **Interface** | $I^2C$ (Fast Mode up to 400 kHz) |
| **Default $I^2C$ address** | `0x29` (Software programmable at runtime) |
| **Ranging distance** | 30 mm to 2000 mm (up to 1200 mm in standard mode) |
| **Emitter wavelength** | 940 nm VCSEL (Class 1 Eye-Safe Laser) |
| **Current consumption** | 20 mA active ranging / $5\ \mu\text{A}$ standby |
| **Field of View (FoV)** | 25° conical FOV |

## Pinout

Standard 6-pin 0.1" (2.54 mm) breakout module header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 4 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 5 | `GPIO1` / `INT` | Digital Output | Programmable interrupt output pin (1.8V to 2.8V logic) |
| 6 | `XSHUT` / `SHDN` | Digital Input | Active-Low shutdown input (pull low to disable IC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{CC}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power input with LDO |
| Active Supply Current | $I_{CC}$ | 10 | 19 | 40 | mA | Active ranging state |
| Standby Current | $I_{sb}$ | — | 5 | 10 | µA | `XSHUT` held Low |
| Ranging Distance (Indoor) | $D_{in}$ | 30 | — | 2000 | mm | White target 88% reflectance |
| Ranging Distance (Outdoor) | $D_{out}$ | 30 | — | 800 | mm | High ambient sunlight ($20\text{ kLux}$) |
| Ranging Accuracy | $D_{acc}$ | -3% | $\pm 3\%$ | +3% | — | In dark / indoor environment |
| VCSEL Emitter Peak | $\lambda_{peak}$ | 930 | 940 | 950 | nm | Invisible Class 1 laser |
| Measurement Timing Budget | $t_{budget}$ | 20 | 33 | 200 | ms | Configurable trade-off |

## $I^2C$ Address Configuration for Multiple Sensors

The VL53L0X uses a fixed hardware $I^2C$ power-on address of **`0x29`**. To connect multiple VL53L0X sensors to a single $I^2C$ bus:

1. Connect the `XSHUT` pin of every VL53L0X sensor to a separate GPIO pin on the microcontroller.
2. Hold all `XSHUT` pins Low at startup to place all sensors in hardware shutdown.
3. Bring the `XSHUT` pin of Sensor #1 High to boot it up.
4. Send an $I^2C$ software command to reassign Sensor #1's address (e.g. to `0x30`).
5. Bring Sensor #2's `XSHUT` pin High and reassign its address to `0x31`. Repeat for each sensor.

## Wiring

| VL53L0X Pin | → | Arduino Uno | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V | 3.3V | Onboard regulator converts to 2.8V |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |
| `XSHUT` | | Digital Pin D4 | GPIO 16 | Internal pull-up to 2.8V; drive Low for shutdown |
| `GPIO1` | | Unused | Unused | Interrupt output (optional) |

> [!WARNING]
> Protective liner notice:
> - New VL53L0X breakout modules ship with an **orange or yellow protective plastic film** stuck over the optical aperture window.
> - Leaving this protective film attached results in constant false readings of 0–50 mm caused by laser light scattering back into the SPAD array. **Remove the film before testing!**

## Example

```cpp
#include <Wire.h>
#include "Adafruit_VL53L0X.h"

Adafruit_VL53L0X lox = Adafruit_VL53L0X();

void setup() {
  Serial.begin(115200);
  while (!Serial) { delay(1); }

  Serial.println("Initializing VL53L0X ToF sensor...");
  if (!lox.begin()) {
    Serial.println("Failed to boot VL53L0X! Check wiring/protective film.");
    while (1);
  }
  Serial.println("VL53L0X online.");
}

void loop() {
  VL53L0X_RangingMeasurementData_t measure;
  
  lox.rangingTest(&measure, false); // Pass 'true' to get debug data

  if (measure.RangeStatus != 4) {  // Phase 4 = Out of range
    Serial.print("Distance: ");
    Serial.print(measure.RangeMilliMeter);
    Serial.println(" mm");
  } else {
    Serial.println("Out of range (>2000 mm)");
  }

  delay(100);
}
```

## Common mistakes

- **Leaving the optical protective cover film on:** Results in permanent 20–50 mm readings due to internal reflection.
- **Forgetting `XSHUT` state handling when using multiple sensors:** Restarting the MCU resets all VL53L0X sensors back to the default `0x29` address, breaking $I^2C$ communication until re-initialized sequentially.
- **Over-ranging in high ambient sunlight:** Direct sunlight contains intense 940 nm infrared radiation that floods the SPAD detector, reducing maximum range down to ~800 mm.

## Notes

- **VL53L0X vs HC-SR04:** Unlike ultrasonic sensors, the VL53L0X has no minimum blind spot (reads from 30 mm down to 0 mm), is completely silent, and is unaffected by soft acoustic-absorbing fabrics or tilted surfaces.
