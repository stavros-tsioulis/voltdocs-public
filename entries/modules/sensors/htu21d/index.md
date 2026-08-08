## Overview

The **HTU21D** (and HTU21DF variant with PTFE filter membrane) is a digital relative humidity and temperature sensor manufactured by TE Connectivity (formerly Measurement Specialties). Housed in a tiny $3.0 \times 3.0\text{ mm}$ 6-pin DFN package, it is widely used in weather stations, home automation HVAC controllers, and medical equipment.

Delivering typical accuracies of **$\pm 2\%\ \text{RH}$** and **$\pm 0.3^\circ\text{C}$**, user-programmable resolution (12-bit RH / 14-bit Temp down to 8-bit / 11-bit), CRC-8 checksum verification, an onboard heating element, and an $I^2C$ interface (**`0x40`**), the HTU21D draws an ultra-low standby current of **$0.14\ \mu\text{A}$**.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.0 V DC (breakout includes 3.3V LDO regulator) |
| **IC supply voltage (`VDD`)** | 1.5 V to 3.6 V DC (3.3 V nominal) |
| **Interface** | $I^2C$ Fast-Mode (up to 400 kHz) |
| **Fixed $I^2C$ address** | `0x40` |
| **Humidity range & accuracy**| $0\%\text{ to }100\%\text{ RH}$ ($\pm 2\%\ \text{RH}$ typical) |
| **Temperature range & accuracy**| $-40^\circ\text{C}\text{ to }+125^\circ\text{C}$ ($\pm 0.3^\circ\text{C}$ typical) |
| **Resolution options** | 12-bit RH / 14-bit Temp (Default) or 8-bit RH / 11-bit Temp |
| **Internal heater** | Onboard programmable heater for sensor diagnostic & de-fogging |
| **Standby current** | $0.14\ \mu\text{A}$ typical at $VDD = 3.0\text{V}$ |

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
| Active Current | $I_{CC}$ | — | 450 | 500 | µA | Active conversion state |
| Standby Current | $I_{sd}$ | — | 0.14 | 0.5 | µA | Sleep mode |
| RH Accuracy ($20\%\dots 80\%$)| $RH_{acc}$ | -2.0 | $\pm 2.0$ | +2.0 | % RH | At $25^\circ\text{C}$ |
| Temp Accuracy ($0^\circ\text{C}\dots 60^\circ\text{C}$)| $T_{acc}$ | -0.3 | $\pm 0.3$ | +0.3 | °C | At $25^\circ\text{C}$ |
| Measuring Time (14-bit Temp)| $t_{temp}$ | — | 44 | 50 | ms | Max resolution |
| Measuring Time (12-bit RH) | $t_{rh}$ | — | 14 | 16 | ms | Max resolution |

## $I^2C$ Command Opcodes & Math

- **Trigger Temperature Measure (Hold Master):** `0xE3`
- **Trigger Humidity Measure (Hold Master):** `0xE5`
- **Trigger Temperature Measure (No Hold):** `0xF3`
- **Trigger Humidity Measure (No Hold):** `0xF5`

### Temperature Calculation ($^\circ\text{C}$)

$$ \text{Temperature } (^\circ\text{C}) = -46.85 + 175.72 \times \left( \frac{\text{Raw 16-bit Temp Register \& 0xFFFC}}{65536} \right) $$

### Humidity Calculation ($\%\text{ RH}$)

$$ \text{Relative Humidity } (\%\text{ RH}) = -6.0 + 125.0 \times \left( \frac{\text{Raw 16-bit RH Register \& 0xFFFC}}{65536} \right) $$

## Wiring

| HTU21D Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VIN` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |

## Example (Adafruit_HTU21DF Library)

```cpp
#include <Wire.h>
#include "Adafruit_HTU21DF.h"

Adafruit_HTU21DF htu = Adafruit_HTU21DF();

void setup() {
  Serial.begin(115200);
  Serial.println("Adafruit HTU21D-F Humidity & Temp Test");

  if (!htu.begin()) {
    Serial.println("Couldn't find HTU21D-F sensor! Check I2C wiring.");
    while (1);
  }
}

void loop() {
  float temp = htu.readTemperature();
  float rel_hum = htu.readHumidity();

  Serial.print("Temp: "); Serial.print(temp); Serial.print(" °C | ");
  Serial.print("Humidity: "); Serial.print(rel_hum); Serial.println(" % RH");

  delay(1000);
}
```

## Common mistakes

- **Holding finger near sensor element:** Human skin radiates moisture ($\ge 70\%\text{ RH}$) and thermal heat. Keep hands clear of the small white PTFE sensor filter while taking ambient room measurements.
- **Forgetting I2C bus address collision:** HTU21D uses fixed address `0x40`, which collides with HDC1080 and Si7021 sensors if placed on the same $I^2C$ bus.

## Notes

- **HTU21D vs Si7021 vs SHT31:** HTU21D is fully command-compatible with the Si7021; SHT31 offers higher accuracy ($\pm 1.5\%\text{ RH}$) and configurable $I^2C$ addresses (`0x44`/`0x45`).
