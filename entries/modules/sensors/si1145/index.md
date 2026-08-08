## Overview

The **SI1145** is a multi-band optical ambient light, UV index, and proximity sensor manufactured by Silicon Labs. Used in weather station monitors, outdoor solar trackers, and smart wearables, it provides calibrated **Solar UV Index readings ($0\dots 11+$)** without requiring a costly true-UV filter.

Instead of directly measuring weak UV photons, the SI1145 calculates the UV Index using an internal algorithmic formula based on simultaneous measurements from integrated **Visible Light and Infrared (IR) photodiodes**. It also supports 3-LED driving channels for multi-axis proximity sensing ($0\text{ to }50\text{ cm}$) over an $I^2C$ bus (**`0x60`**).

## Quick reference

| | |
|---|---|
| **Operating voltage (`VIN`)** | 3.3 V to 5.0 V DC (breakout module with 3.3V LDO regulator) |
| **IC supply voltage (`VDD`)** | 1.71 V to 3.6 V DC (3.3 V nominal) |
| **Interface** | $I^2C$ (up to 400 kHz) |
| **Fixed $I^2C$ address** | `0x60` |
| **Measured Spectrum** | Visible Light, Infrared ($850\text{ nm}$), and Algorithmic Solar UV Index |
| **UV Index Range** | 0 to 11+ (calibrated UV index rating) |
| **Proximity Range** | $0\text{ to }50\text{ cm}$ (when paired with external IR LED driver) |
| **Standby Current** | $500\text{ nA}$ ($0.5\ \mu\text{A}$) |

## Pinout

Breakout module 6-pin header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VIN` | Power | Supply power input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 4 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 5 | `INT` | Digital Output | Active-Low interrupt output pin |
| 6 | `LED` | Output | Programmable IR LED sink driver output |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{VIN}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with LDO |
| Active Supply Current | $I_{CC}$ | — | 500 | 800 | µA | Active sampling |
| Standby Current | $I_{sd}$ | — | 0.5 | 2.0 | µA | Sleep state |
| UV Index Resolution | $Res_{UV}$ | — | 0.01 | — | UV Index | Calculated UV index output |
| Visible Photodiode Peak | $\lambda_{vis}$| — | 540 | — | nm | Visible light peak |
| IR Photodiode Peak | $\lambda_{IR}$ | — | 850 | — | nm | Infrared light peak |

## UV Index Calculation Math

The SI1145 returns raw 16-bit integers for `Visible`, `IR`, and `UV Index`:

$$ \text{Solar UV Index} = \frac{\text{Raw 16-Bit UV Register Value}}{100.0} $$

*(Example: A raw UV register reading of `250` corresponds to a Solar UV Index of **2.5**).*

## Wiring

| SI1145 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VIN` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |

## Example (Adafruit_SI1145 Library)

```cpp
#include <Wire.h>
#include "Adafruit_SI1145.h"

Adafruit_SI1145 uv = Adafruit_SI1145();

void setup() {
  Serial.begin(115200);
  Serial.println("Adafruit SI1145 Light & UV Sensor Test");

  if (!uv.begin()) {
    Serial.println("Could not find SI1145 sensor! Check I2C wiring.");
    while (1);
  }

  Serial.println("SI1145 Initialized.");
}

void loop() {
  float visible = uv.readVisible();
  float ir = uv.readIR();
  float uvIndex = uv.readUV() / 100.0;

  Serial.print("Visible: "); Serial.print(visible);
  Serial.print(" | IR: "); Serial.print(ir);
  Serial.print(" | UV Index: "); Serial.println(uvIndex);

  delay(1000);
}
```

## Common mistakes

- **Testing indoors under LED/Fluorescent lights:** Indoor artificial lights emit virtually zero UV radiation. The algorithmic UV index calculation will return `0.0`. Test outdoors under direct sunlight.
- **Forgetting to divide raw UV integer by 100:** The `readUV()` register returns integer counts multiplied by 100. Always divide by `100.0` to obtain standard UV Index values.

## Notes

- **SI1145 vs VEML6070 vs LTR390:** SI1145 calculates UV index algorithmically from IR/Vis photodiodes; VEML6070 measures UVA directly; LTR390 measures direct UV and Lux.
