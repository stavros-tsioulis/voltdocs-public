## Overview

The **SGP40** is a digital Volatile Organic Compound (VOC) gas sensor manufactured by Sensirion. Housed in a $2.44 \times 2.44\text{ mm}$ 6-pin DFN package, it is designed for indoor air purifiers, HVAC ventilation fans, and smart home air quality monitors.

Built on Sensirion's **CMOSens MOX (Metal-Oxide)** technology with siloxane resistance, the SGP40 detects airborne organic chemicals, solvents, paints, cleaning agents, human breath emissions, and cigarette smoke. Paired with Sensirion's **VOC Index Algorithm**, it outputs a continuous **VOC Index ($0\text{ to }500$)** over $I^2C$ (**`0x59`**), where **100** represents normal clean ambient air baseline.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VIN`)** | 3.3 V to 5.0 V DC (breakout includes 3.3V LDO regulator) |
| **IC supply voltage (`VDD`)** | 1.7 V to 3.6 V DC (3.3 V nominal) |
| **Interface** | $I^2C$ Fast-Mode (up to 400 kHz) |
| **Fixed $I^2C$ address** | `0x59` |
| **Target Gases** | Volatile Organic Compounds (VOCs / Solvents / Alcohols / Smoke) |
| **VOC Index Range** | $0\text{ to }500$ ($100 = \text{Clean Air Baseline}$, $>200 = \text{Polluted Air}$) |
| **Warm-up Time** | 10 seconds fast warm-up |
| **Heater Power Draw** | $2.6\text{ mA}$ average operating current |
| **Sleep Current** | $3.0\ \mu\text{A}$ sleep mode |

## Pinout

Breakout module header & STEMMA QT / Qwiic connectors:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VIN` | Power | Supply power input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 4 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{VIN}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with LDO |
| Active Supply Current | $I_{CC}$ | — | 2.6 | 3.5 | mA | Continuous sampling state |
| Sleep Current | $I_{sd}$ | — | 3.0 | 10.0 | µA | Software sleep mode |
| VOC Index Resolution | $Res_{VOC}$| — | 1 | — | Index units | Range 0 to 500 |
| Response Time ($T_{90}$) | $t_{90}$ | — | < 10 | — | s | Step change in VOC concentration |
| Repeatability | $Rep$ | — | $\pm 5$ | — | Index units | At 100 Index baseline |

## VOC Index Algorithm & Temperature Compensation

The SGP40 raw output is a 16-bit **SRAW_VOC** tick count ($0\dots 65535$). Passing this value along with ambient Temperature and Relative Humidity into the Sensirion C++ / Python VOC Algorithm generates the normalized **VOC Index**:

- **VOC Index = 100:** Clean ambient air baseline (adaptive auto-zeroing).
- **VOC Index 100 – 200:** Mild VOC presence (cooking, perfume).
- **VOC Index 200 – 500:** Heavy VOC pollution (paints, solvents, heavy smoke).

## Wiring

| SGP40 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VIN` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |

## Example (Adafruit_SGP40 Library)

```cpp
#include <Wire.h>
#include "Adafruit_SGP40.h"

Adafruit_SGP40 sgp;

void setup() {
  Serial.begin(115200);
  Serial.println("Adafruit SGP40 VOC Sensor Test");

  if (!sgp.begin()) {
    Serial.println("SGP40 sensor not found! Check I2C wiring.");
    while (1);
  }

  Serial.println("SGP40 Initialized. Waiting 10s for warm-up...");
  delay(10000);
}

void loop() {
  // Read raw VOC tick count
  uint16_t sraw = sgp.measureRaw();
  
  // Calculate VOC Index (0 to 500) with default 25°C / 50% RH compensation
  int32_t voc_index = sgp.measureVocIndex();

  Serial.print("Raw SRAW_VOC: "); Serial.print(sraw);
  Serial.print(" | VOC Index: "); Serial.println(voc_index);

  delay(1000);
}
```

## Common mistakes

- **Interpreting VOC Index as absolute PPM/PPB:** The SGP40 outputs a relative **VOC Index (0 to 500)** relative to the recent 24-hour baseline. It does not output absolute concentration in PPM or PPB.
- **Forgetting I2C address `0x59`:** Unlike the SGP30 (`0x58`), the SGP40 uses $I^2C$ address **`0x59`**.

## Notes

- **SGP40 vs SGP30 vs SGP41:** SGP30 measures $eCO_2$ and $TVOC$; SGP40 measures $VOC\ Index$; SGP41 measures both $VOC\ Index$ and $NO_x\ Index$.
