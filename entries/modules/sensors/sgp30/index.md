## Overview

The **SGP30** is a digital multi-pixel metal-oxide (MOX) gas sensor designed by Sensirion for indoor air quality (IAQ) applications. Integrating four sensing elements on a single chip inside a $2.45 \times 2.45\text{ mm}$ DFN package, it outputs calibrated Total Volatile Organic Compounds (TVOC in ppb) and equivalent carbon dioxide ($\text{eCO}_2$ in ppm) measurements over $I^2C$.

Featuring Sensirion's *CMOSens* technology and proprietary dynamic baseline compensation algorithms, the SGP30 resists long-term siloxane contamination and sensor drift. It is widely used in smart home air purifiers, HVAC ventilation systems, ESPHome nodes, and indoor environmental monitors.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.0 V DC (breakout with onboard 1.8V LDO) |
| **IC supply voltage (`VDD`)** | 1.62 V to 1.98 V DC (1.8 V nominal) |
| **Interface** | $I^2C$ (up to 400 kHz) |
| **$I^2C$ Address** | `0x58` (Fixed) |
| **$\text{eCO}_2$ measurement range** | 400 ppm to 60,000 ppm |
| **TVOC measurement range** | 0 ppb to 60,000 ppb |
| **Measurement rate** | 1.0 Hz (1 measurement per second) |
| **Active current draw** | 48.2 mA at 1.8V (continuous heater operation) |

## Pinout

Standard 4-pin 0.1" (2.54 mm) header or Qwiic / STEMMA QT connector:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SCL` | Digital Input | $I^2C$ Serial Clock (1.8V logic; module includes level shifter) |
| 4 | `SDA` | Digital Input / Output | $I^2C$ Serial Data (1.8V logic; module includes level shifter) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{CC}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with 1.8V LDO |
| Operating Current | $I_{CC}$ | — | 48.2 | 55.0 | mA | Active heating & measurement |
| Sleep Current | $I_{sleep}$ | — | 2.0 | 10.0 | µA | Low power sleep |
| $\text{eCO}_2$ Range | $eCO_2$ | 400 | — | 60000 | ppm | Equivalent $\text{CO}_2$ |
| TVOC Range | $TVOC$ | 0 | — | 60000 | ppb | Total Volatile Organic Compounds |
| Sampling Rate | $f_{sample}$ | — | 1.0 | — | Hz | Recommended sampling interval |
| Baseline Persistence | $t_{base}$ | — | 12 | 24 | hours | Baseline save interval |
| Operating Temperature | $T_{opr}$ | -40 | — | 85 | °C | Ambient air |

## $I^2C$ Commands & Protocol

The SGP30 uses 16-bit command words (`0x58` address):

| Command (16-bit) | Name | Description |
|---|---|---|
| `0x2003` | `IAQ_init` | Initialize IAQ measurement algorithms and baseline |
| `0x2008` | `IAQ_measure` | Trigger TVOC and $\text{eCO}_2$ reading (returns 6 bytes: 2B $\text{eCO}_2$ + CRC, 2B TVOC + CRC) |
| `0x2015` | `get_baseline` | Read current algorithm baseline values (save to EEPROM) |
| `0x201E` | `set_baseline` | Restore saved baseline values on boot |
| `0x2061` | `set_humidity` | Write absolute humidity value ($\text{g/m}^3$) for compensation |

## Wiring

| SGP30 Pin | → | Arduino Uno | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Module includes 1.8V LDO |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |

## Example

```cpp
#include <Wire.h>
#include "Adafruit_SGP30.h"

Adafruit_SGP30 sgp;

void setup() {
  Serial.begin(115200);
  Serial.println("SGP30 test");

  if (!sgp.begin()) {
    Serial.println("Sensor not found :(");
    while (1);
  }
  Serial.print("Found SGP30 serial #");
  Serial.print(sgp.serialnumber[0], HEX);
  Serial.print(sgp.serialnumber[1], HEX);
  Serial.println(sgp.serialnumber[2], HEX);
}

void loop() {
  if (!sgp.IAQmeasure()) {
    Serial.println("Measurement failed");
    return;
  }
  Serial.print("TVOC: "); Serial.print(sgp.TVOC); Serial.print(" ppb\t");
  Serial.print("eCO2: "); Serial.print(sgp.eCO2); Serial.println(" ppm");

  delay(1000);
}
```

## Common mistakes

- **Not polling at 1.0 Hz:** The SGP30 internal baseline algorithm expects `IAQmeasure()` to be called at exact 1-second intervals. Irregular polling distorts TVOC and $\text{eCO}_2$ readings.
- **Lost baseline on power cycle:** During the first 15 seconds after `IAQ_init()`, the sensor outputs fixed dummy readings (400 ppm $\text{eCO}_2$ / 0 ppb TVOC). After 12 hours of continuous operation, application code should save the baseline (`get_baseline`) to non-volatile flash memory and restore it on reboot (`set_baseline`).
- **Powering bare SGP30 IC with 3.3V or 5V:** The raw SGP30 IC is rated strictly for 1.8V. Only bare chips require an external 1.8V regulator; breakout boards handle this onboard.

## Notes

- **SGP30 vs CCS811:** SGP30 features wider measurement ranges (up to 60,000 ppm vs 8,192 ppm) and faster baseline convergence.
