## Overview

The **HDC1080** is a low-power, high-accuracy digital relative humidity and temperature sensor manufactured by Texas Instruments. Housed in a ultra-compact $3.0 \times 3.0\text{ mm}$ 6-pin WSON package, it measures relative humidity from **$0\%\text{ to }100\%\text{ RH}$** and ambient temperature from **$-40^\circ\text{C}\text{ to }+125^\circ\text{C}$**.

Featuring typical accuracies of **$\pm 2\%\ \text{RH}$** and **$\pm 0.2^\circ\text{C}$**, 14-bit ADC resolution, an integrated heating element (for condensation removal), and an $I^2C$ interface (`0x40`), the HDC1080 draws an average of just **$1.3\ \mu\text{A}$ at 1 Hz sampling** ($700\text{ nA}$ in sleep mode). It is ideal for battery-powered environmental monitoring, smart thermostats, and weather stations.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VDD`)** | 2.7 V to 5.5 V DC (3.3 V or 5.0 V nominal) |
| **Interface** | $I^2C$ (up to 400 kHz) |
| **Fixed $I^2C$ address** | `0x40` |
| **Humidity range & accuracy**| $0\%\text{ to }100\%\text{ RH}$ ($\pm 2\%\ \text{RH}$ typical) |
| **Temperature range & accuracy**| $-40^\circ\text{C}\text{ to }+125^\circ\text{C}$ ($\pm 0.2^\circ\text{C}$ typical) |
| **ADC resolution** | 14-bit (configurable to 11-bit or 8-bit in register `0x02`) |
| **Internal heater** | Software-controlled integrated heating element for de-fogging |
| **Average power draw** | $1.3\ \mu\text{A}$ at 1 sample/sec / $700\text{ nA}$ sleep |

## Pinout

Breakout module 4-pin header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply power input (+2.7 V to +5.5 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 4 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 2.7 | 3.3 / 5.0 | 5.5 | V | DC |
| Active Conversion Current| $I_{active}$| — | 210 | 300 | µA | Active sampling |
| Sleep Current | $I_{sleep}$ | — | 0.7 | 1.1 | µA | Sleep state |
| Temp Accuracy ($20^\circ\text{C}\dots 60^\circ\text{C}$)| $T_{acc}$ | -0.2 | $\pm 0.2$ | +0.2 | °C | Typical accuracy |
| RH Accuracy ($20\%\dots 80\%$)| $RH_{acc}$ | -2.0 | $\pm 2.0$ | +2.0 | % RH | Typical accuracy at $25^\circ\text{C}$ |
| Conversion Time (14-bit)| $t_{conv}$ | — | 6.5 (T) / 6.5 (RH) | — | ms | Dual measurement |

## Data Calculations & Math

- **Temperature Register (`0x00`):**

$$ \text{Temperature } (^\circ\text{C}) = \left( \frac{\text{Raw 16-bit Temp Register}}{65536} \right) \times 165.0 - 40.0 $$

- **Humidity Register (`0x01`):**

$$ \text{Relative Humidity } (\%\text{ RH}) = \left( \frac{\text{Raw 16-bit RH Register}}{65536} \right) \times 100.0\% $$

## Wiring

| HDC1080 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |

## Example (ClosedCube_HDC1080 Library)

```cpp
#include <Wire.h>
#include "ClosedCube_HDC1080.h"

ClosedCube_HDC1080 hdc1080;

void setup() {
  Serial.begin(115200);
  Wire.begin();

  Serial.println("TI HDC1080 Temp & Humidity Sensor Test");
  
  // Default I2C Address 0x40
  hdc1080.begin(0x40);

  Serial.print("Device Manufacturer ID: 0x");
  Serial.println(hdc1080.readManufacturerId(), HEX);
}

void loop() {
  float temp = hdc1080.readTemperature();
  float humidity = hdc1080.readHumidity();

  Serial.print("Temperature: "); Serial.print(temp); Serial.print(" °C | ");
  Serial.print("Humidity: "); Serial.print(humidity); Serial.println(" % RH");

  delay(2000);
}
```

## Common mistakes

- **Forgetting I2C bus address:** HDC1080 has a fixed hardcoded $I^2C$ address (`0x40`). Sharing the bus with other fixed `0x40` devices (such as the HTU21D or INA219) causes $I^2C$ bus conflicts.
- **Self-heating from onboard heater:** The HDC1080 includes an internal heating element (bit 13 in Configuration register `0x02`). Keep the heater **OFF** during normal environmental sensing to avoid $+5^\circ\text{C}\dots +10^\circ\text{C}$ temperature measurement errors. Enable the heater only briefly to evaporate water condensation.

## Notes

- **HDC1080 vs HDC2080 vs HTU21D:** HDC1080 is $\pm 2\%\ \text{RH}$ accurate over $I^2C$; HDC2080 is the updated ultra-low-power version ($50\text{ nA}$ sleep); HTU21D is TE Connectivity's equivalent sensor.
