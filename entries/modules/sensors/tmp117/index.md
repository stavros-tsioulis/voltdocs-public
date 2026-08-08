## Overview

The **TMP117** is a 16-bit high-precision digital temperature sensor manufactured by Texas Instruments. Designed to meet ASTM E1112 and ISO 80601 medical thermometer standards, it delivers an unprecedented accuracy of **$\pm 0.1^\circ\text{C}$** across $-20^\circ\text{C}$ to $+50^\circ\text{C}$ without requiring user calibration.

With a resolution of **$0.0078125^\circ\text{C}$** ($1/128^\circ\text{C}$ per LSB), 100% factory calibration traceable to NIST standards, ultra-low power consumption ($3.5\ \mu\text{A}$ at 1 Hz active duty cycle), and $I^2C$ communication, the TMP117 is used in clinical fever thermometers, precision environmental monitoring, cold-chain logistics, and ESPHome environmental nodes.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 1.8 V to 5.5 V DC |
| **Interface** | $I^2C$ / SMBus (up to 400 kHz) |
| **Default $I^2C$ address** | `0x48` (`ADD0` pin to GND) |
| **Configurable addresses** | 4 addresses (`0x48` GND, `0x49` VCC, `0x4A` SDA, `0x4B` SCL) |
| **Accuracy ($-20^\circ\text{C}$ to $+50^\circ\text{C}$)**| $\pm 0.1^\circ\text{C}$ max |
| **Accuracy ($-40^\circ\text{C}$ to $+100^\circ\text{C}$)**| $\pm 0.2^\circ\text{C}$ max |
| **Resolution** | 16-bit ($0.0078125^\circ\text{C}$ per LSB) |
| **Medical Standards** | Meets ASTM E1112 & ISO 80601-2-56 clinical specifications |
| **Operating current** | $3.5\ \mu\text{A}$ at 1 Hz duty cycle / $150\text{ nA}$ shutdown |

## Pinout

Breakout module header & STEMMA QT connector:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+1.8 V to +5.5 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 4 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 5 | `ADD0` | Digital Input | $I^2C$ Address select pin |
| 6 | `ALERT` | Digital Output | Programmable active-high/low temperature alert output |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 1.8 | 3.3 / 5.0 | 5.5 | V | DC |
| Temperature Accuracy (Medical)| $T_{acc1}$ | -0.1 | $\pm 0.05$ | +0.1 | °C | $-20^\circ\text{C} \le T \le +50^\circ\text{C}$ |
| Temperature Accuracy (Full) | $T_{acc2}$ | -0.3 | $\pm 0.15$ | +0.3 | °C | $-55^\circ\text{C} \le T \le +150^\circ\text{C}$ |
| Temperature Resolution | $T_{res}$ | — | 0.0078125| — | °C/LSB | 16-bit 2's complement |
| Conversion Time (Default 8x) | $t_{conv}$ | — | 15.5 | 17.5 | ms | Built-in 8-sample averaging |
| Supply Current (Active) | $I_{active}$| — | 135 | 175 | µA | Continuous conversion state |
| Supply Current (1 Hz Duty) | $I_{avg}$ | — | 3.5 | 6.0 | µA | 1 Hz conversion with sleep |

## Data Format & Math

The temperature register (`0x00`) returns a 16-bit 2's complement signed integer:

$$ \text{Temperature } (^\circ\text{C}) = \text{Raw 16-bit Signed Integer} \times 0.0078125^\circ\text{C} $$

$$ \text{Temperature } (^\circ\text{C}) = \frac{\text{Raw 16-bit Signed Integer}}{128} $$

## Wiring

| TMP117 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |

## Example (Adafruit_TMP117 Library)

```cpp
#include <Wire.h>
#include <Adafruit_TMP117.h>
#include <Adafruit_Sensor.h>

Adafruit_TMP117 tmp117;

void setup() {
  Serial.begin(115200);
  while (!Serial) delay(10);

  Serial.println("Adafruit TMP117 High-Precision Temp Sensor Test");

  if (!tmp117.begin(0x48)) { // Default address 0x48
    Serial.println("Failed to find TMP117 chip! Check wiring.");
    while (1);
  }

  Serial.println("TMP117 found!");
}

void loop() {
  sensors_event_t temp;
  tmp117.getEvent(&temp);

  Serial.print("High-Precision Temperature: ");
  Serial.print(temp.temperature, 4); // Print 4 decimal places
  Serial.println(" °C");

  delay(1000);
}
```

## Common mistakes

- **Thermal conduction from host PCB / MCU:** Placing the TMP117 close to heat-generating components (microcontrollers, linear voltage regulators, power LEDs) causes heat to conduct through copper ground planes, distorting ambient temperature readings by $+1^\circ\text{C}$ to $+3^\circ\text{C}$. Use PCB thermal isolation cutouts (air slots) around the sensor package.
- **Reading raw integer without division:** The LSB resolution is $0.0078125^\circ\text{C}$ ($1/128$). Divide raw 16-bit signed integers by `128.0` to calculate Celsius.

## Notes

- **TMP117 vs DS18B20 vs BME280:** TMP117 offers medical-grade $\pm 0.1^\circ\text{C}$ accuracy (vs DS18B20's $\pm 0.5^\circ\text{C}$ and BME280's $\pm 0.5^\circ\text{C}$).
