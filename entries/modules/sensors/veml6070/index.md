## Overview

The **VEML6070** is an integrated CMOS digital ultraviolet (UV) light sensor IC manufactured by Vishay Intertechnology. Designed for solar UV index monitoring, weather stations, wearable sunburn indicators, and UV lamp verification, it detects solar **UVA spectrum radiation ($320\text{ nm}$ to $400\text{ nm}$)** with peak sensitivity at $355\text{ nm}$.

Housed in a compact $2.35 \times 1.8\text{ mm}$ OPLGA package, the VEML6070 integrates a photodiode array, low-noise pre-amplifier, 16-bit analog-to-digital converter, and an $I^2C$ interface. Uniquely, the VEML6070 utilizes **two consecutive $I^2C$ slave addresses**: **`0x38`** (reads LSB data byte and configures integration time) and **`0x39`** (reads MSB data byte).

## Quick reference

| | |
|---|---|
| **Operating voltage (`VDD`)** | 2.7 V to 5.5 V DC (3.3 V or 5.0 V nominal) |
| **Spectral Detection** | UVA spectrum ($320\text{ nm} \dots 400\text{ nm}$, peak $355\text{ nm}$) |
| **Interface** | $I^2C$ (up to 400 kHz) |
| **Dual $I^2C$ Addresses** | `0x38` (Command / LSB Data) & `0x39` (MSB Data) |
| **Integration Times** | $1/2T$ ($56.25\text{ ms}$), $1T$ ($112.5\text{ ms}$), $2T$ ($225\text{ ms}$), $4T$ ($450\text{ ms}$) |
| **ADC Resolution** | 16-bit digital output count ($0\dots 65,535$) |
| **Operating Current** | $100\ \mu\text{A}$ active / $1.0\ \mu\text{A}$ software shutdown |
| **ACK Interrupt Feature** | Programmable threshold interrupt output pin (`ACK`) |

## Pinout

Breakout module 5-pin header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VDD` | Power | Supply power input (+2.7 V to +5.5 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 4 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 5 | `ACK` | Digital Output | Active-Low threshold interrupt pin |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 2.7 | 3.3 / 5.0 | 5.5 | V | DC |
| Active Supply Current | $I_{DD}$ | — | 100 | 250 | µA | $VDD = 3.3\text{V}$, active sampling |
| Shutdown Current | $I_{sd}$ | — | 1.0 | 15.0 | µA | Software shutdown mode |
| UVA Peak Sensitivity | $\lambda_{peak}$| — | 355 | — | nm | Spectral response peak |
| UV Sensitivity (1T Mode) | $Sens$ | — | 5 | — | counts/$\mu\text{W/cm}^2$ | Solar simulator calibration |
| Integration Time (1T) | $t_{int\_1T}$| — | 112.5 | — | ms | RSET = 270 kΩ |

## Solar UV Index Calculation Table ($1T$ Integration Time)

| Raw 16-Bit UV Count Range | Solar UV Index Rating | Risk Level |
|---|---|---|
| 0 to 560 | 0 to 2 | Low |
| 561 to 1120 | 3 to 5 | Moderate |
| 1121 to 1493 | 6 to 7 | High |
| 1494 to 2054 | 8 to 10 | Very High |
| $> 2055$ | 11+ | Extreme |

## Wiring

| VEML6070 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VDD` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |

## Example (Adafruit_VEML6070 Library)

```cpp
#include <Wire.h>
#include "Adafruit_VEML6070.h"

Adafruit_VEML6070 uv = Adafruit_VEML6070();

void setup() {
  Serial.begin(115200);
  Serial.println("Adafruit VEML6070 UV Sensor Test");

  // Initialize in 1T Integration Mode
  uv.begin(VEML6070_1_T);
}

void loop() {
  uint16_t uv_reading = uv.readUV();

  Serial.print("Raw UV Reading: "); Serial.print(uv_reading); Serial.print(" | Risk: ");

  if (uv_reading <= 560) {
    Serial.println("Low (0-2)");
  } else if (uv_reading <= 1120) {
    Serial.println("Moderate (3-5)");
  } else if (uv_reading <= 1493) {
    Serial.println("High (6-7)");
  } else if (uv_reading <= 2054) {
    Serial.println("Very High (8-10)");
  } else {
    Serial.println("Extreme (11+)");
  }

  delay(1000);
}
```

## Common mistakes

- **Expecting $I^2C$ scanners to find only one address:** The VEML6070 responds to **two $I^2C$ addresses** (`0x38` and `0x39`). `0x38` handles commands/LSB data; `0x39` handles MSB data.
- **Glass window blocking UV rays:** Standard window glass blocks $90\%+$ of UVA and $99\%+$ of UVB rays. Test the sensor in direct outdoor sunlight or under a dedicated UV blacklight.

## Notes

- **VEML6070 vs VEML6075 vs SI1145:** VEML6070 measures UVA only; VEML6075 measures both UVA and UVB dual channels; SI1145 calculates UV index indirectly from IR/Visible photodiodes.
