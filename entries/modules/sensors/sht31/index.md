## Overview

The **SHT31** (part of Sensirion's SHT3x series including SHT30, SHT31, and SHT35) is a high-accuracy digital humidity and temperature sensor. Built on Sensirion's CMOSens MEMS technology, it integrates a capacitive humidity sensor, a bandgap temperature sensor, an analog-to-digital converter, and signal processing circuitry on a single chip.

With outstanding precision ($\pm 0.2^\circ\text{C}$ temperature accuracy, $\pm 2\%\text{ RH}$ humidity accuracy), low power consumption, an onboard heating element to clear internal condensation, programmable threshold ALERT outputs, and dual $I^2C$ address options (`0x44` / `0x45`), the SHT31 is widely regarded as the gold standard environmental sensor for precision HVAC control, weather stations, laboratory datalogging, and industrial IoT nodes.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 2.15 V to 5.5 V DC |
| **Interface** | $I^2C$ (up to 1 MHz Fast Mode Plus) |
| **Default $I^2C$ address** | `0x44` (`ADDR` pin Low / un-connected) |
| **Alternate $I^2C$ address** | `0x45` (`ADDR` pin High to `VCC`) |
| **Temperature accuracy** | $\pm 0.2^\circ\text{C}$ (typ. from $0^\circ\text{C}$ to $65^\circ\text{C}$) |
| **Humidity accuracy** | $\pm 2.0\%\text{ RH}$ (typ. from $0\%$ to $100\%\text{ RH}$) |
| **Current consumption** | $0.8\text{ mA}$ active / $0.2\ \mu\text{A}$ standby |
| **Special features** | Onboard internal heater, hardware ALERT interrupt pin |

## Pinout

Breakout modules expose a 5-pin or 6-pin 0.1" (2.54 mm) header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply input (+2.15 V to +5.5 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 4 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 5 | `ALR` / `ALERT` | Digital Output | Programmable interrupt alert output pin (leave open if unused) |
| 6 | `ADR` / `ADDR` | Digital Input | $I^2C$ Address select (Low = `0x44`, High = `0x45`) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.15 | 3.3 / 5.0 | 5.5 | V | DC |
| Active Supply Current | $I_{CC}$ | — | 0.8 | 1.5 | mA | During $I^2C$ conversion |
| Standby Current | $I_{sb}$ | — | 0.2 | 2.0 | µA | Idle state |
| Heater Power Dissipation | $P_{heat}$ | — | 3.3 | 8.0 | mW | Internal heater enabled at 3.3V |
| Temp Accuracy (SHT31) | $T_{acc}$ | -0.2 | $\pm 0.2$ | +0.2 | °C | $0^\circ\text{C} \le T \le 65^\circ\text{C}$ |
| Humidity Accuracy (SHT31) | $RH_{acc}$ | -2.0 | $\pm 2.0$ | +2.0 | % RH | $0\% \le RH \le 100\%$ |
| Measurement Duration | $t_{meas}$ | 2.5 | 4.5 | 15.0 | ms | Low / Medium / High repeatability |

## $I^2C$ Commands & CRC-8

The SHT31 uses 16-bit command codes (`MSB` followed by `LSB`):

| Command (16-bit) | Description |
|---|---|
| `0x2C06` | Clock Stretching enabled, High repeatability measurement |
| `0x2400` | Clock Stretching disabled, High repeatability measurement |
| `0x306D` | Software Reset (`SOFTRESET`) |
| `0x3070` | Heater Enable (`HEATER_ON`) |
| `0x3066` | Heater Disable (`HEATER_OFF`) |
| `0xE000` | Read Status Register |

When reading 6 measurement bytes from the sensor (2 bytes $RH$, 1 byte CRC, 2 bytes Temp, 1 byte CRC), valid data must be checked using the polynomial $X^8 + X^5 + X^4 + 1$ (`0x31`, init `0xFF`).

### Conversion Formulas

$$ \text{Temperature } (^\circ\text{C}) = -45 + 175 \times \left( \frac{S_T}{2^{16} - 1} \right) $$

$$ \text{Relative Humidity (\% RH)} = 100 \times \left( \frac{S_{RH}}{2^{16} - 1} \right) $$

## Wiring

| SHT31 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Native 2.15V–5.5V support |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |
| `ADDR` | | GND | GND | Connect to GND for `0x44`, VCC for `0x45` |

## Example

```cpp
#include <Wire.h>
#include "Adafruit_SHT31.h"

Adafruit_SHT31 sht31 = Adafruit_SHT31();

void setup() {
  Serial.begin(9600);
  while (!Serial) delay(10);

  Serial.println("Initializing SHT31 sensor...");
  // Default address 0x44
  if (!sht31.begin(0x44)) {
    Serial.println("Could not find SHT31! Check wiring.");
    while (1) delay(10);
  }
  Serial.println("SHT31 initialized.");
}

void loop() {
  float t = sht31.readTemperature();
  float h = sht31.readHumidity();

  if (!isnan(t) && !isnan(h)) {
    Serial.print("Temp: "); Serial.print(t); Serial.print(" °C | ");
    Serial.print("Humidity: "); Serial.print(h); Serial.println(" %RH");
  } else {
    Serial.println("Failed to read from SHT31");
  }

  delay(2000);
}
```

## Common mistakes

- **Leaving internal heater running continuously:** The integrated heating element is intended strictly for drying out condensation in high-humidity environments. Leaving the heater turned on during normal measurements causes self-heating errors of $+3^\circ\text{C}$ to $+5^\circ\text{C}$.
- **I2C address collision:** Connecting multiple SHT31 sensors without pulling the `ADDR` pin High on the second unit results in bus collisions at address `0x44`.
- **Ignoring CRC bytes:** Neglecting CRC validation on noisy $I^2C$ lines can lead to erroneous spike readings.

## Notes

- **SHT30 vs SHT31 vs SHT35:** All three parts share identical pinouts and command codes. SHT30 is the budget variant ($\pm 3\% \text{ RH}$), SHT31 is standard grade ($\pm 2\% \text{ RH}$), and SHT35 is high-precision grade ($\pm 1.5\% \text{ RH}$).
