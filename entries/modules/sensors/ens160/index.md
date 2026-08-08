## Overview

The **ENS160** is a digital multi-gas indoor air quality (IAQ) sensor manufactured by ScioSense (formerly ams OSRAM environmental sensors). Built on TrueMEMS technology with **4 independent metal-oxide (MOX) micro-hotplate sensing elements**, it provides high resistance to siloxane contamination and chemical poisoning.

Processing raw MOX gas resistance data internally with an embedded ASIC algorithm, the ENS160 computes three calibrated air quality metrics directly over $I^2C$ or SPI:
1. **Air Quality Index (AQI 1–5):** According to German UBA indoor air quality guidelines.
2. **Total Volatile Organic Compounds (TVOC):** $0\text{ to }65,000\text{ ppb}$.
3. **Equivalent $\text{CO}_2$ ($\text{eCO}_2$):** $400\text{ to }65,000\text{ ppm}$.

It is widely deployed on SparkFun Qwiic, Adafruit STEMMA QT, and ESPHome environmental nodes for HVAC ventilation control and smart home air monitors.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.0 V DC (breakout with 1.8V LDO & level shifters) |
| **IC supply voltage (`VDD`)** | 1.71 V to 1.98 V DC (1.8 V nominal) |
| **Interface** | $I^2C$ (up to 1.0 MHz) & SPI (up to 10 MHz) |
| **Default $I^2C$ address** | `0x53` (`ADDR` pin High / un-connected) |
| **Alternate $I^2C$ address** | `0x52` (`ADDR` pin Low to GND) |
| **Air Quality Index (AQI)** | 1 (Excellent) to 5 (Unhealthy) |
| **TVOC range** | 0 ppb to 65,000 ppb |
| **$\text{eCO}_2$ range** | 400 ppm to 65,000 ppm |
| **Warm-up time** | 3 minutes initial heating / 1 hour full baseline stabilization |

## Pinout

Breakout module header & STEMMA QT / Qwiic connectors:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `SCL` / `SCLK` | Digital Input | $I^2C$ Serial Clock / SPI Clock |
| 4 | `SDA` / `MOSI` | Digital Input / Output | $I^2C$ Serial Data / SPI Data In |
| 5 | `MISO` | Digital Output | SPI Data Out (in SPI mode) |
| 6 | `CS` | Digital Input | Chip Select (High = $I^2C$ mode, Low = SPI mode) |
| 7 | `ADDR` | Digital Input | $I^2C$ Address select (High = `0x53`, Low = `0x52`) |
| 8 | `INT` | Digital Output | Active-Low interrupt output (data ready trigger) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{CC}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with LDO |
| Active Supply Current | $I_{CC}$ | — | 29.0 | 35.0 | mA | Continuous 4-hotplate heating |
| Low Power Current | $I_{lp}$ | — | 0.9 | — | mA | Low power pulse mode |
| Deep Sleep Current | $I_{sleep}$ | — | 5 | — | µA | Reset state |
| TVOC Range | $TVOC$ | 0 | — | 65000 | ppb | Parts per billion |
| $\text{eCO}_2$ Range | $eCO_2$ | 400 | — | 65000 | ppm | Equivalent $\text{CO}_2$ estimate |
| AQI Rating Range | $AQI$ | 1 | — | 5 | — | 1 = Excellent, 5 = Unhealthy |
| Operating Temperature | $T_{opr}$ | -40 | — | 85 | °C | Ambient air |

## Temperature & Humidity Compensation

The ENS160 allows writing current ambient temperature ($T$ in $^\circ\text{C}$) and relative humidity ($RH$ in $\%$) values into compensation registers **`0x13`** and **`0x15`**. Passing live temperature/humidity readings (from an paired AHT20, SHT31, or BME280 sensor) ensures max accuracy under varying climate conditions:

$$ \text{Register } 0x13\text{ (Temp)} = (T_{C} + 273.15) \times 64 $$

$$ \text{Register } 0x15\text{ (RH)} = RH_{\%} \times 512 $$

## Wiring

| ENS160 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Module includes 1.8V LDO |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |
| `CS`  | | 3.3V / 5V | 3.3V | **Pull High for $I^2C$ mode** |

## Example (ScioSense / SparkFun ENS160 Library)

```cpp
#include <Wire.h>
#include "SparkFun_ENS160.h"

SparkFun_ENS160 myENS;

void setup() {
  Serial.begin(115200);
  Wire.begin();

  Serial.println("ENS160 Multi-Gas Sensor Test");

  if (!myENS.begin(0x53)) { // Default address 0x53
    Serial.println("ENS160 not found! Check CS and ADDR pins.");
    while (1);
  }

  // Set operating mode to Standard In-Air Operation (0x02)
  myENS.setMode(ENS160_OPMODE_STD);
  Serial.println("ENS160 initialized. Warming up...");
}

void loop() {
  if (myENS.checkDataStatus()) {
    Serial.print("AQI Index (1-5): "); Serial.print(myENS.getAQI());
    Serial.print(" | TVOC: "); Serial.print(myENS.getTVOC()); Serial.print(" ppb");
    Serial.print(" | eCO2: "); Serial.print(myENS.getECO2()); Serial.println(" ppm");
  }

  delay(2000);
}
```

## Common mistakes

- **Leaving `CS` floating:** Pull `CS` High to 3.3V for $I^2C$ operation. Floating `CS` drops the IC into SPI mode.
- **Reading during initial 3-minute warm-up:** The MOX micro-hotplates require 3 minutes after power-on to reach operating temperatures ($200^\circ\text{C}\dots 400^\circ\text{C}$). Readings during the first 180 seconds indicate `WARMUP` status.

## Notes

- **ENS160 vs CCS811 vs SGP30:** ENS160 features 4 independent MOX hotplates (vs 1 on CCS811) and higher siloxane immunity.
