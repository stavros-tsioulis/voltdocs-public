## Overview

The **Si7021** is a high-precision CMOS relative humidity and temperature sensor IC manufactured by Silicon Labs. Housed in a $3.0 \times 3.0\text{ mm}$ 6-pin DFN package (frequently fitted with an optional protective hydrophobic PTFE membrane filter cover over the sensor opening), it is used in weather stations, HVAC environmental controls, and indoor air monitors.

Delivering typical accuracies of **$\pm 3\%\ \text{RH}$** and **$\pm 0.4^\circ\text{C}$**, 14-bit temperature / 12-bit humidity ADC resolution, an integrated heating element, and $I^2C$ output (**`0x40`**), the Si7021 draws a standby sleep current of just **$60\text{ nA}$**. It is fully command-compatible with the HTU21D.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VIN`)** | 3.3 V to 5.0 V DC (breakout module with 3.3V LDO regulator) |
| **IC supply voltage (`VDD`)** | 1.9 V to 3.6 V DC (3.3 V nominal) |
| **Interface** | $I^2C$ Fast-Mode (up to 400 kHz) |
| **Fixed $I^2C$ address** | `0x40` |
| **Humidity range & accuracy**| $0\%\text{ to }100\%\text{ RH}$ ($\pm 3.0\%\ \text{RH}$ typical) |
| **Temperature range & accuracy**| $-40^\circ\text{C}\text{ to }+125^\circ\text{C}$ ($\pm 0.4^\circ\text{C}$ typical) |
| **Protective Filter** | Optional factory-fitted PTFE hydrophobic film cover |
| **Standby current** | $60\text{ nA}$ ($0.06\ \mu\text{A}$) |

## Pinout

Breakout module 4-pin header:

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
| Active Current | $I_{CC}$ | — | 150 | 180 | µA | Active RH measurement |
| Standby Current | $I_{sd}$ | — | 0.06 | 0.6 | µA | Sleep mode |
| Temp Accuracy ($0^\circ\text{C}\dots 60^\circ\text{C}$)| $T_{acc}$ | -0.4 | $\pm 0.4$ | +0.4 | °C | Typical accuracy |
| RH Accuracy ($0\%\dots 80\%$)| $RH_{acc}$ | -3.0 | $\pm 3.0$ | +3.0 | % RH | At $25^\circ\text{C}$ |
| Conversion Time (12-bit RH)| $t_{rh}$ | — | 10 | 12 | ms | Standard mode |

## Data Calculations & Math

- **Temperature Calculation ($^\circ\text{C}$):**

$$ \text{Temperature } (^\circ\text{C}) = \left( \frac{175.72 \times \text{Raw 16-bit Temp Register}}{65536} \right) - 46.85 $$

- **Humidity Calculation ($\%\text{ RH}$):**

$$ \text{Relative Humidity } (\%\text{ RH}) = \left( \frac{125.0 \times \text{Raw 16-bit RH Register}}{65536} \right) - 6.0 $$

## Wiring

| Si7021 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VIN` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |

## Example (Adafruit_Si7021 Library)

```cpp
#include <Wire.h>
#include "Adafruit_Si7021.h"

Adafruit_Si7021 sensor = Adafruit_Si7021();

void setup() {
  Serial.begin(115200);
  Serial.println("Adafruit Si7021 Sensor Test");

  if (!sensor.begin()) {
    Serial.println("Couldn't find Si7021 sensor! Check I2C wiring.");
    while (1);
  }

  Serial.print("Found Si7021 Serial Number: 0x");
  Serial.println(sensor.readSerialNumber(), HEX);
}

void loop() {
  float temp = sensor.readTemperature();
  float humidity = sensor.readHumidity();

  Serial.print("Temperature: "); Serial.print(temp); Serial.print(" °C | ");
  Serial.print("Humidity: "); Serial.print(humidity); Serial.println(" % RH");

  delay(1000);
}
```

## Common mistakes

- **Peeling off the white PTFE filter protective sticker:** On Si7021 modules equipped with a white PTFE film cover over the sensor opening, **do not attempt to peel off the white film**. It is a breathable hydrophobic barrier that protects the capacitive sensor element from dust contamination while allowing water vapor to pass.
- **Address collision (`0x40`):** Si7021 shares $I^2C$ address `0x40` with HTU21D and HDC1080.

## Notes

- **Si7021 vs HTU21D vs SHT31:** Si7021 is command-compatible with HTU21D and includes an optional factory-fitted protective PTFE filter membrane.
