## Overview

The **BME688** is a 4-in-1 digital environmental sensor manufactured by Bosch Sensortec. Housed in a $3.0 \times 3.0\text{ mm}$ 8-pin LGA package, it integrates individual sensors for **gas**, **barometric pressure**, **relative humidity**, and **ambient temperature** over $I^2C$ or SPI.

As the AI-enhanced successor to the popular BME680, the BME688 features an upgraded metal-oxide (MOX) gas sensor capable of customized multi-step heater profiling. Paired with Bosch's **BSEC 2.0 (Bosch Software Environmental Cluster)** AI software suite and **BME AI Studio**, the sensor can train machine-learning models to detect specific gas compositions, food spoilage, forest fire smoke, Volatile Organic Compounds (VOCs), Volatile Sulfur Compounds (VSCs), and indoor air quality (IAQ 0–500 index).

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.0 V DC (breakout with 3.3V LDO) |
| **IC supply voltage (`VDD`)** | 1.71 V to 3.6 V DC (1.8 V or 3.3 V nominal) |
| **Interface** | $I^2C$ (up to 3.4 MHz) & 3-Wire / 4-Wire SPI (up to 10 MHz) |
| **Default $I^2C$ address** | `0x77` (`SDO` pin High to 3.3V) |
| **Alternate $I^2C$ address** | `0x76` (`SDO` pin Low to GND) |
| **Sensors** | Gas MOX, Barometric Pressure, Humidity, Temperature |
| **Air Quality Output** | Index of Air Quality (IAQ 0–500), $\text{eCO}_2$ (ppm), bVOCe ($\text{ppm}$) |
| **Operating current** | $3.9\text{ mA}$ (gas heater active) / $0.15\ \mu\text{A}$ sleep |

## Pinout

Breakout modules expose a 6-pin 0.1" (2.54 mm) header or Qwiic / STEMMA QT connector:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `SCL` / `SCK` | Digital Input | $I^2C$ Serial Clock / SPI Clock |
| 4 | `SDA` / `SDI` | Digital Input / Output | $I^2C$ Serial Data / SPI Serial Data Input |
| 5 | `SDO` / `ADR` | Digital Output | SPI Data Out / $I^2C$ Address Select (Low = `0x76`, High = `0x77`) |
| 6 | `CS` | Digital Input | SPI Chip Select (High = $I^2C$ mode, Low = SPI mode) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{CC}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with LDO |
| Active Supply Current | $I_{CC}$ | — | 3.9 | 12.0 | mA | Gas sensor heater active |
| Sleep Current | $I_{sleep}$ | — | 0.15 | 1.0 | µA | Sleep mode |
| Temperature Range | $T_{range}$ | -40 | — | 85 | °C | Accuracy $\pm 0.5^\circ\text{C}$ at $25^\circ\text{C}$ |
| Pressure Range | $P_{range}$ | 300 | — | 1100 | hPa | Absolute accuracy $\pm 0.6\text{ hPa}$ |
| Humidity Range | $H_{range}$ | 0 | — | 100 | % RH | Accuracy $\pm 3\%\text{ RH}$ |
| Gas Sensor Response Time | $t_{gas}$ | — | $<1$ | — | s | Response to VOC gas step |

## BSEC 2.0 AI Algorithm Outputs

When using Bosch's pre-compiled **BSEC 2.0** firmware library:

- **IAQ Index (0–500):** 0–50 (Excellent), 51–100 (Good), 101–150 (Lightly polluted), 151–200 (Moderately polluted), 201–300 (Heavily polluted), 301–500 (Extremely polluted).
- **$\text{eCO}_2$ Equivalent (ppm):** 400 ppm to 5000+ ppm estimate.
- **bVOCe Equivalent (ppm):** Breath VOC equivalent concentration.
- **AI Classification Accuracy:** Percentage confidence (0–100%) for custom trained gas profiles (e.g. coffee vs vanilla, fresh food vs spoiled food).

## Wiring

| BME688 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Module includes 3.3V LDO |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |
| `CS`  | | 3.3V / 5V | 3.3V | **Pull High for $I^2C$ mode** |

## Example (Arduino BSEC 2.0 Library)

```cpp
#include <Wire.h>
#include "bsec2.h"

Bsec2 bsec;

void newDataCallback(const bme68xData data, const bsecOutputs outputs, Bsec2 bsec) {
  if (!outputs.nOutputs) return;

  for (uint8_t i = 0; i < outputs.nOutputs; i++) {
    const bsecData output = outputs.output[i];
    if (output.sensor_id == BSEC_OUTPUT_IAQ) {
      Serial.print("IAQ Index: "); Serial.print(output.signal);
      Serial.print(" (Accuracy: "); Serial.print(output.accuracy); Serial.println(")");
    } else if (output.sensor_id == BSEC_OUTPUT_CO2_EQUIVALENT) {
      Serial.print("eCO2: "); Serial.print(output.signal); Serial.println(" ppm");
    } else if (output.sensor_id == BSEC_OUTPUT_RAW_TEMPERATURE) {
      Serial.print("Temperature: "); Serial.print(output.signal); Serial.println(" °C");
    }
  }
}

void setup() {
  Serial.begin(115200);
  Wire.begin();

  bsecSensor sensorList[] = {
    BSEC_OUTPUT_IAQ,
    BSEC_OUTPUT_CO2_EQUIVALENT,
    BSEC_OUTPUT_RAW_TEMPERATURE
  };

  if (!bsec.begin(BME68X_I2C_ADDR_HIGH, Wire)) {
    Serial.println("BME688 BSEC init failed! Check wiring.");
    while (1);
  }

  bsec.updateSubscription(sensorList, ARRAY_LEN(sensorList), BSEC_SAMPLE_RATE_LP);
  bsec.attachCallback(newDataCallback);
  Serial.println("BME688 BSEC initialized successfully.");
}

void loop() {
  bsec.run();
}
```

## Common mistakes

- **Leaving `CS` floating in $I^2C$ mode:** Pull `CS` High to 3.3V to lock the IC into $I^2C$ mode; floating `CS` causes random drops into SPI mode.
- **Self-heating offset:** The internal MOX gas heater warms up the sensor silicon package, adding a $+1.5^\circ\text{C}$ to $+2.5^\circ\text{C}$ temperature bias. The BSEC software automatically subtracts this offset.

## Notes

- **BME688 vs BME680 vs BME280:** BME280 measures Temp/Humidity/Pressure (no gas); BME680 adds basic VOC gas sensing; BME688 adds customizable multi-step heater profiles and BME AI Studio machine learning.
