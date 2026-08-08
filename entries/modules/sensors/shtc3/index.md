## Overview

The **SHTC3** is a compact, ultra-low-power digital relative humidity and temperature sensor engineered by Sensirion. Housed in a miniature $2.0 \times 2.0\text{ mm}$ 4-pin DFN package, it is designed specifically for battery-driven wearables, smartphones, smart tags, and low-power IoT sensor nodes.

Delivering typical accuracies of **$\pm 2.0\%\ \text{RH}$** and **$\pm 0.2^\circ\text{C}$**, the SHTC3 operates across a wide supply voltage range of **$1.62\text{V}$ to $3.6\text{V}$ DC**. It features an automated low-power sleep mode drawing only **$0.15\ \mu\text{A}$**, fast wakeup times ($240\ \mu\text{s}$), and an $I^2C$ interface (**`0x70`**).

## Quick reference

| | |
|---|---|
| **Operating voltage (`VIN`)** | 3.3 V to 5.0 V DC (breakout module with 3.3V LDO regulator) |
| **IC supply voltage (`VDD`)** | 1.62 V to 3.6 V DC (3.3 V nominal) |
| **Interface** | $I^2C$ Fast-Mode (up to 400 kHz) |
| **Fixed $I^2C$ address** | `0x70` |
| **Humidity range & accuracy**| $0\%\text{ to }100\%\text{ RH}$ ($\pm 2.0\%\ \text{RH}$ typical) |
| **Temperature range & accuracy**| $-40^\circ\text{C}\text{ to }+125^\circ\text{C}$ ($\pm 0.2^\circ\text{C}$ typical) |
| **Wakeup time** | $240\ \mu\text{s}$ from sleep mode to active measurement |
| **Sleep supply current** | $0.15\ \mu\text{A}$ ($150\text{ nA}$) |

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
| Active Current | $I_{CC}$ | — | 270 | 430 | µA | Active measurement |
| Sleep Current | $I_{sleep}$ | — | 0.15 | 0.6 | µA | Sleep mode |
| Temp Accuracy ($10^\circ\text{C}\dots 55^\circ\text{C}$)| $T_{acc}$ | -0.2 | $\pm 0.2$ | +0.2 | °C | Typical accuracy |
| RH Accuracy ($20\%\dots 80\%$)| $RH_{acc}$ | -2.0 | $\pm 2.0$ | +2.0 | % RH | At $25^\circ\text{C}$ |
| High Precision Measure Time| $t_{meas}$ | — | 10.8 | 12.1 | ms | Normal power mode |

## $I^2C$ Commands & Calculations

- **Wakeup Command:** `0x3517` (Must send before reading measurements).
- **Sleep Command:** `0xB098` (Puts chip into $150\text{ nA}$ sleep mode).
- **Measure Normal Power (Clock Stretching):** `0x7CA2`
- **Measure Low Power (Clock Stretching):** `0x6458`

### Temperature Calculation ($^\circ\text{C}$)

$$ \text{Temperature } (^\circ\text{C}) = -45.0 + 175.0 \times \left( \frac{\text{Raw 16-bit Temp Register}}{65536} \right) $$

### Relative Humidity Calculation ($\%\text{ RH}$)

$$ \text{Relative Humidity } (\%\text{ RH}) = 100.0 \times \left( \frac{\text{Raw 16-bit RH Register}}{65536} \right) $$

## Wiring

| SHTC3 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VIN` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |

## Example (SparkFun SHTC3 Arduino Library)

```cpp
#include <Wire.h>
#include "SparkFun_SHTC3.h"

SHTC3 mySHTC3;

void setup() {
  Serial.begin(115200);
  Wire.begin();

  Serial.println("SparkFun SHTC3 Sensor Test");

  while (mySHTC3.begin() != SHTC3_Status_Nominal) {
    Serial.println("SHTC3 initialization failed! Retrying...");
    delay(1000);
  }
}

void loop() {
  SHTC3_Status_TypeDef status = mySHTC3.update();

  if (status == SHTC3_Status_Nominal) {
    Serial.print("Temperature: "); Serial.print(mySHTC3.toDegC()); Serial.print(" °C | ");
    Serial.print("Humidity: "); Serial.print(mySHTC3.toPercent()); Serial.println(" % RH");
  }

  delay(2000);
}
```

## Common mistakes

- **Forgetting to send Wakeup command (`0x3517`):** The SHTC3 boots into sleep mode to conserve battery power. Sending measurement commands without issuing a Wakeup command results in NACK responses over $I^2C$.
- **Expecting address `0x40`:** Unlike the SHT21, HTU21D, or HDC1080, the SHTC3 uses $I^2C$ address **`0x70`**.

## Notes

- **SHTC3 vs SHT40:** SHTC3 uses $I^2C$ address `0x70` and requires manual Wake/Sleep commands; SHT40 uses address `0x44` and auto-sleeps.
