## Overview

The **VEML7700** is a 16-bit high-accuracy digital ambient light sensor (ALS) manufactured by Vishay Semiconductors. Designed for display brightness control, backlight dimming, and weather station monitoring, it features Vishay's proprietary *Filtron* technology, which matches the spectral response of the human eye (peak $550\text{ nm}$).

Offering an extreme dynamic range from **0.0036 Lux to 120,000 Lux** (resolving sub-lux moonlight up to direct full sunlight), programmable gain settings ($\frac{1}{8}, \frac{1}{4}, 1, 2$), adjustable integration times ($25\text{ ms}$ to $800\text{ ms}$), and $I^2C$ communication, the VEML7700 is widely used on Adafruit and ESPHome sensor nodes.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.0 V DC (breakout with 3.3V LDO) |
| **IC supply voltage (`VDD`)** | 2.5 V to 3.6 V DC (3.3 V nominal) |
| **Interface** | $I^2C$ (Standard 100 kHz / Fast 400 kHz) |
| **Fixed $I^2C$ address** | `0x10` |
| **Dynamic range** | 0.0036 Lux to 120,000 Lux |
| **Resolution** | 16-bit digital output |
| **Operating current** | $45\ \mu\text{A}$ active / $0.5\ \mu\text{A}$ shutdown |

## Pinout

Standard 4-pin 0.1" (2.54 mm) header or Qwiic / STEMMA QT connector:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 4 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{CC}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with LDO |
| Active Supply Current | $I_{DD}$ | — | 45 | 100 | µA | Integration time 100 ms |
| Shutdown Current | $I_{sd}$ | — | 0.5 | 1.0 | µA | Software shutdown |
| Minimum Resolution | $Lux_{min}$| — | 0.0036 | — | Lux/digit | Gain = 2, $t_{int} = 800\text{ ms}$ |
| Maximum Measurable Lux | $Lux_{max}$| — | 120000 | — | Lux | Gain = $\frac{1}{8}$, $t_{int} = 25\text{ ms}$ |
| Peak Sensitivity Wavelength| $\lambda_p$| — | 550 | — | nm | Matches human photopic eye response |

## $I^2C$ Register Map

The VEML7700 uses 16-bit register words (`0x10` address):

| Command (8-bit) | Register Name | Access | Reset | Description |
|---|---|---|---|---|
| `0x00` | `ALS_CONF` | R/W | `0x0001` | Configuration: Gain, Integration Time, Persistence, Shutdown |
| `0x01` | `ALS_WH` | R/W | `0x0000` | High Threshold Window for interrupt |
| `0x02` | `ALS_WL` | R/W | `0x0000` | Low Threshold Window for interrupt |
| `0x04` | `ALS_DATA` | Read | — | 16-bit raw ALS illuminance data |
| `0x05` | `WHITE_DATA` | Read | — | 16-bit raw White channel data |

## Lux Calculation & Gain Multipliers

$$ \text{Lux} = \text{Raw ALS Code} \times \text{Resolution Scale Factor} $$

For default settings ($\text{Gain} = 1$, $\text{Integration Time} = 100\text{ ms}$), the resolution multiplier is **$0.0576\text{ Lux/digit}$**.

High-lux nonlinear compensation formula (for raw Lux $> 1000$):

$$ \text{Lux}_{corrected} = 6.0135 \times 10^{-13} \times L^4 - 9.3924 \times 10^{-9} \times L^3 + 8.1488 \times 10^{-5} \times L^2 + 1.0023 \times L $$

## Wiring

| VEML7700 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Module includes 3.3V LDO |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |

## Example

```cpp
#include <Wire.h>
#include "Adafruit_VEML7700.h"

Adafruit_VEML7700 veml = Adafruit_VEML7700();

void setup() {
  Serial.begin(9600);
  while (!Serial) delay(10);

  Serial.println("Initializing VEML7700...");
  if (!veml.begin()) {
    Serial.println("VEML7700 not found! Check wiring.");
    while (1);
  }
  Serial.println("VEML7700 online.");

  veml.setGain(VEML7700_GAIN_1);
  veml.setIntegrationTime(VEML7700_IT_100MS);
}

void loop() {
  float lux = veml.readLux();
  Serial.print("Ambient Light: ");
  Serial.print(lux);
  Serial.println(" Lux");

  delay(1000);
}
```

## Common mistakes

- **I2C address collision:** VEML7700 uses a fixed hardcoded address (`0x10`). Connecting multiple VEML7700 sensors to the same $I^2C$ bus requires an $I^2C$ multiplexer (such as TCA9548A).
- **Clipping in bright outdoor sunlight:** At default gain ($\times 1$), raw output clips at ~3,700 Lux. For outdoor solar measurements, set gain to $\frac{1}{8}$ (`VEML7700_GAIN_1_8`) and integration time to $25\text{ ms}$.

## Notes

- **VEML7700 vs BH1750:** VEML7700 offers significantly higher sensitivity ($0.0036\text{ Lux}$ vs $1.0\text{ Lux}$) and wider dynamic range.
