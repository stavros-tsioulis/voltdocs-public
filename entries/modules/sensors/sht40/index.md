## Overview

The **SHT40** is Sensirion's 4th-generation industry-leading digital relative humidity and temperature sensor. Housed in a microscopic $1.5 \times 1.5\text{ mm}$ 4-pin DFN package, it delivers class-leading **$\pm 1.8\%\ \text{RH}$** humidity accuracy and **$\pm 0.2^\circ\text{C}$** temperature accuracy.

Operating across an extended supply range of **$1.08\text{V}$ to $3.6\text{V}$ DC** with a idle current of just **$80\text{ nA}$**, the SHT40 features an integrated variable-power internal heater ($200\text{ mW}$ max) for self-decontamination and condensation removal, 16-bit ADC output, and an $I^2C$ interface (**`0x44`** default).

## Quick reference

| | |
|---|---|
| **Operating voltage (`VIN`)** | 3.3 V to 5.0 V DC (breakout module with 3.3V LDO regulator) |
| **IC supply voltage (`VDD`)** | 1.08 V to 3.6 V DC (3.3 V nominal) |
| **Interface** | $I^2C$ Fast-Mode Plus (up to 1.0 MHz) |
| **Default $I^2C$ address** | `0x44` (SHT40-AD1B) / `0x45` (SHT40-BD1B) |
| **Humidity range & accuracy**| $0\%\text{ to }100\%\text{ RH}$ ($\pm 1.8\%\ \text{RH}$ typical) |
| **Temperature range & accuracy**| $-40^\circ\text{C}\text{ to }+125^\circ\text{C}$ ($\pm 0.2^\circ\text{C}$ typical) |
| **Variable power heater** | 3 power levels ($20\text{ mW}, 110\text{ mW}, 200\text{ mW}$) for condensation removal |
| **Idle supply current** | $80\text{ nA}$ ($0.08\ \mu\text{A}$) |

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
| Average Current (1 Hz sampling)| $I_{avg}$ | — | 0.4 | 1.0 | µA | Low repeatability mode |
| Idle Current | $I_{idle}$| — | 80 | 150 | nA | Sleep mode |
| Temp Accuracy ($15^\circ\text{C}\dots 40^\circ\text{C}$)| $T_{acc}$ | -0.2 | $\pm 0.2$ | +0.2 | °C | High precision mode |
| RH Accuracy ($20\%\dots 80\%$)| $RH_{acc}$ | -1.8 | $\pm 1.8$ | +1.8 | % RH | At $25^\circ\text{C}$ |
| High Precision Measure Time| $t_{meas}$ | — | 6.9 | 8.3 | ms | 16-bit measurement |

## $I^2C$ Commands & Conversion Formulas

- **Measure High Precision:** `0xFD` (6.9 ms conversion).
- **Measure Medium Precision:** `0xF6` (4.5 ms conversion).
- **Measure Low Precision:** `0xE0` (1.7 ms conversion).
- **Activate Heater ($200\text{ mW}$, 1 sec):** `0x39`

### Temperature Calculation ($^\circ\text{C}$)

$$ \text{Temperature } (^\circ\text{C}) = -45.0 + 175.0 \times \left( \frac{\text{Raw 16-bit Temp Register}}{65535} \right) $$

### Relative Humidity Calculation ($\%\text{ RH}$)

$$ \text{Relative Humidity } (\%\text{ RH}) = -6.0 + 125.0 \times \left( \frac{\text{Raw 16-bit RH Register}}{65535} \right) $$

*(Clamp RH output to $0\%\dots 100\%\text{ RH}$).*

## Wiring

| SHT40 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VIN` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |

## Example (Adafruit_SHT4x Library)

```cpp
#include <Wire.h>
#include "Adafruit_SHT4x.h"

Adafruit_SHT4x sht4 = Adafruit_SHT4x();

void setup() {
  Serial.begin(115200);
  Serial.println("Adafruit SHT40 Humidity & Temp Test");

  if (!sht4.begin()) {
    Serial.println("Couldn't find SHT40 sensor! Check I2C wiring.");
    while (1);
  }

  sht4.setPrecision(SHT4X_HIGH_PRECISION);
  sht4.setHeater(SHT4X_NO_HEATER);
}

void loop() {
  sensors_event_t humidity, temp;
  sht4.getEvent(&humidity, &temp);

  Serial.print("Temperature: "); Serial.print(temp.temperature); Serial.print(" °C | ");
  Serial.print("Humidity: "); Serial.print(humidity.relative_humidity); Serial.println(" % RH");

  delay(1000);
}
```

## Common mistakes

- **Leaving internal heater running continuously:** Running the $200\text{ mW}$ heater continuously causes heavy sensor self-heating ($+15^\circ\text{C}\dots +30^\circ\text{C}$ temperature bias). Use heater pulses for short 1-second intervals only.
- **Confusing conversion formulas with SHT31/SHT21:** The SHT40 uses updated temperature formula offsets ($-45.0 + 175.0 \times \dots$) compared to SHT31 ($-45.0 + 175.0$) and SHT21 ($-46.85 + 175.72$).

## Notes

- **Sensirion SHT40 Family:** SHT40 ($\pm 1.8\%\ \text{RH}$ standard grade), SHT41 ($\pm 1.5\%\ \text{RH}$ high accuracy), SHT45 ($\pm 1.0\%\ \text{RH}$ ultra-high precision).
