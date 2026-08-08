## Overview

The **TSL2591** (TSL25911FN) is an ultra-high dynamic range digital ambient light sensor (ALS) manufactured by ams OSRAM (formerly TAOS). Built as the advanced successor to the popular TSL2561, it features a massive **$600,000,000 : 1$ dynamic range**, measuring light levels from sub-lux starlight/moonlight (**$188\ \mu\text{Lux}$** minimum detectable signal) up to full bright sunlight (**88,000 Lux**).

The TSL2591 incorporates dual integrating photodiodes:
- **Channel 0 (`CH0`):** Full-spectrum diode (detects both Visible and Infrared light).
- **Channel 1 (`CH1`):** Infrared diode (detects Infrared light only).

By calculating the difference between channels in software, the sensor accurately models the human eye photopic response curve while allowing independent IR spectrum intensity measurement over $I^2C$ (`0x29`).

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.0 V DC (breakout module includes 3.3V LDO regulator) |
| **IC supply voltage (`VDD`)** | 2.7 V to 3.6 V DC (3.3 V nominal) |
| **Interface** | $I^2C$ (Fast Mode up to 400 kHz) |
| **Fixed $I^2C$ address** | `0x29` |
| **Dynamic range** | 600,000,000 : 1 |
| **Lux range** | $188\ \mu\text{Lux}$ ($0.000188\text{ Lux}$) to 88,000 Lux |
| **Resolution** | 16-bit dual-channel digital count outputs (0 to 65,535 counts) |
| **Programmable Gain** | Low ($\times 1$), Med ($\times 25$), High ($\times 428$), Max ($\times 9876$) |
| **Programmable Integration Time**| 100 ms, 200 ms, 300 ms, 400 ms, 500 ms, 600 ms |

## Pinout

STEMMA QT / Qwiic 4-pin connector & 0.1" header pins:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VIN` / `VCC` | Power | Supply input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 4 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 5 | `INT` | Digital Output | Active-Low interrupt output (programmable lux thresholds) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{CC}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with LDO |
| Active Supply Current | $I_{DD}$ | — | 250 | 350 | µA | Active integration state |
| Shutdown Current | $I_{sd}$ | — | 3.0 | 5.0 | µA | Software shutdown mode |
| Min Detectable Lux | $Lux_{min}$| — | 0.000188 | — | Lux | Max Gain ($\times 9876$), $t_{int} = 600\text{ ms}$ |
| Max Detectable Lux | $Lux_{max}$| — | 88000 | — | Lux | Low Gain ($\times 1$), $t_{int} = 100\text{ ms}$ |
| Peak Sensitivity Wavelength| $\lambda_p$| — | 630 (CH0) / 850 (CH1) | — | nm | Visible and IR peaks |

## Gain Settings & Integration Time Table

| Gain Setting | Multiplier Symbol | Typical Application |
|---|---|---|
| `TSL2591_GAIN_LOW` | $\times 1$ | Bright direct sunlight (up to 88,000 Lux) |
| `TSL2591_GAIN_MED` | $\times 25$ | Standard indoor room lighting |
| `TSL2591_GAIN_HIGH` | $\times 428$ | Dim indoor lighting / overcast shade |
| `TSL2591_GAIN_MAX` | $\times 9876$ | Extremely dark environments / moonlight / starlight |

## Lux Calculation Math

$$ \text{Lux} = \left( \frac{CH0 - CH1}{\text{Gain} \times \text{Integration Time (s)}} \right) \times C_{LUX\_DF} $$

Where $C_{LUX\_DF} = 408.0$ (Lux Device Factor constant for TSL2591).

## Wiring

| TSL2591 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VIN` | | 5V / 3.3V | 3.3V | Module includes 3.3V LDO |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |

## Example (Adafruit_TSL2591 Library)

```cpp
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include "Adafruit_TSL2591.h"

Adafruit_TSL2591 tsl = Adafruit_TSL2591(2591); // Pass sensor ID

void setup() {
  Serial.begin(9600);
  Serial.println("Adafruit TSL2591 Light Sensor Test");

  if (!tsl.begin()) {
    Serial.println("TSL2591 not found! Check wiring.");
    while (1);
  }
  
  // Configure gain and integration time
  tsl.setGain(TSL2591_GAIN_MED);      // 25x gain
  tsl.setTiming(TSL2591_INTEGRATIONTIME_100MS); // 100 ms integration
}

void loop() {
  // Read combined 32-bit channel data (CH0 and CH1)
  uint32_t lum = tsl.getFullLuminosity();
  uint16_t ir = lum >> 16;
  uint16_t full = lum & 0xFFFF;
  uint16_t visible = full - ir;

  float lux = tsl.calculateLux(full, ir);

  Serial.print("IR: "); Serial.print(ir);
  Serial.print(" | Full Spectrum: "); Serial.print(full);
  Serial.print(" | Visible: "); Serial.print(visible);
  Serial.print(" | Calculated Lux: "); Serial.println(lux);

  delay(1000);
}
```

## Common mistakes

- **I2C Address Collision:** TSL2591 has a fixed hardcoded $I^2C$ address (`0x29`).
- **Saturation in direct sunlight:** Operating at Medium or High gain under full sunlight causes 16-bit register saturation (65,535 count cap). When full-spectrum readings hit 65,535, lower the gain setting to `TSL2591_GAIN_LOW` ($\times 1$).

## Notes

- **TSL2591 vs TSL2561:** TSL2591 offers $600,000,000 : 1$ dynamic range (vs $1,000,000 : 1$ for TSL2561), higher max Lux ($88,000$ vs $40,000$), and improved sub-lux sensitivity.
