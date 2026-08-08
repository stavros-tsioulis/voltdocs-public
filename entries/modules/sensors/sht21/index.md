## Overview

The **SHT21** is a high-accuracy digital relative humidity and temperature sensor manufactured by Sensirion. Built on Sensirion's proprietary **CMOSens technology**, it integrates a capacitive humidity sensor element, a bandgap temperature sensor, and a 14-bit ADC inside a compact $3.0 \times 3.0\text{ mm}$ 6-pin DFN package.

Delivering typical accuracies of **$\pm 2\%\ \text{RH}$** and **$\pm 0.3^\circ\text{C}$**, user-configurable resolution (12-bit RH / 14-bit Temp down to 8-bit / 11-bit), CRC-8 checksum verification, an internal heating element, and an $I^2C$ interface (**`0x40`**), the SHT21 draws a standby current of just **$0.15\ \mu\text{A}$**.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VIN`)** | 3.3 V to 5.0 V DC (breakout with 3.3V LDO regulator) |
| **IC supply voltage (`VDD`)** | 2.1 V to 3.6 V DC (3.3 V nominal) |
| **Interface** | $I^2C$ Fast-Mode (up to 400 kHz) |
| **Fixed $I^2C$ address** | `0x40` |
| **Humidity range & accuracy**| $0\%\text{ to }100\%\text{ RH}$ ($\pm 2\%\ \text{RH}$ typical) |
| **Temperature range & accuracy**| $-40^\circ\text{C}\text{ to }+125^\circ\text{C}$ ($\pm 0.3^\circ\text{C}$ typical) |
| **Resolution options** | 12-bit RH / 14-bit Temp (Default) or 8-bit RH / 11-bit Temp |
| **Internal heater** | Onboard programmable heater for diagnostic testing |
| **Standby current** | $0.15\ \mu\text{A}$ typical at $VDD = 3.0\text{V}$ |

## Pinout

Breakout module 4-pin header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply power input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 4 | `SCL` | Digital Input | $I^2C$ Serial Clock |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{VIN}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with LDO |
| Active Measurement Current| $I_{CC}$ | — | 150 | 330 | µA | Active sampling |
| Sleep Current | $I_{sd}$ | — | 0.15 | 0.4 | µA | Sleep mode |
| Temp Accuracy ($0^\circ\text{C}\dots 60^\circ\text{C}$)| $T_{acc}$ | -0.3 | $\pm 0.3$ | +0.3 | °C | At $25^\circ\text{C}$ |
| RH Accuracy ($20\%\dots 80\%$)| $RH_{acc}$ | -2.0 | $\pm 2.0$ | +2.0 | % RH | At $25^\circ\text{C}$ |
| Measuring Time (14-bit Temp)| $t_{temp}$ | — | 66 | 85 | ms | Max resolution |
| Measuring Time (12-bit RH) | $t_{rh}$ | — | 22 | 29 | ms | Max resolution |

## $I^2C$ Command Opcodes & Math

- **Hold Master Mode Temp:** `0xE3`
- **Hold Master Mode RH:** `0xE5`
- **No Hold Master Mode Temp:** `0xF3`
- **No Hold Master Mode RH:** `0xF5`

### Temperature Calculation ($^\circ\text{C}$)

$$ \text{Temperature } (^\circ\text{C}) = -46.85 + 175.72 \times \left( \frac{\text{Raw 16-bit Temp Register \& 0xFFFC}}{65536} \right) $$

### Relative Humidity Calculation ($\%\text{ RH}$)

$$ \text{Relative Humidity } (\%\text{ RH}) = -6.0 + 125.0 \times \left( \frac{\text{Raw 16-bit RH Register \& 0xFFFC}}{65536} \right) $$

## Wiring

| SHT21 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |

## Example (SHT21 Arduino Library)

```cpp
#include <Wire.h>
#include "SHT21.h"

SHT21 sht;

void setup() {
  Serial.begin(115200);
  Wire.begin();

  Serial.println("Sensirion SHT21 Sensor Test");
  sht.begin();
}

void loop() {
  float temp = sht.getTemperature();
  float humidity = sht.getHumidity();

  Serial.print("Temperature: "); Serial.print(temp); Serial.print(" °C | ");
  Serial.print("Humidity: "); Serial.print(humidity); Serial.println(" % RH");

  delay(1000);
}
```

## Common mistakes

- **Leaving $I^2C$ lines un-pulled:** SHT21 requires $4.7\text{ k}\Omega$ pull-up resistors on `SDA` and `SCL`.
- **Forgetting $I^2C$ address `0x40` collision:** SHT21 shares fixed address `0x40` with HTU21D and HDC1080.

## Notes

- **Sensirion SHT Series Evolution:** SHT11 (1-Wire-like protocol) $\rightarrow$ **SHT21 ($I^2C$ 0x40)** $\rightarrow$ SHT31 ($I^2C$ 0x44/0x45) $\rightarrow$ SHT40 ($I^2C$ 0x44 ultra-low power).
