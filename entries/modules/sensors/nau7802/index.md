## Overview

The **NAU7802** is a 24-bit dual-channel precision Sigma-Delta Analog-to-Digital Converter (ADC) manufactured by Nuvoton Technology. Optimized for weigh scales, industrial process control, and force gauge measurement, it interfaces directly to wheatstone bridge strain-gauge load cells.

Integrating a low-noise Programmable Gain Amplifier (PGA with gains up to **$\times 128$**), dual differential input channels (Channels 1 and 2), a built-in low-dropout (LDO) voltage regulator for load cell excitation power, and an **$I^2C$ interface (`0x2A`)**, the NAU7802 serves as a modern, high-precision alternative to the bit-banged HX711 chip. It is natively supported by ESPHome, SparkFun Qwiic libraries, and Arduino.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 2.7 V to 5.5 V DC (3.3 V or 5.0 V nominal) |
| **Interface** | $I^2C$ (up to 400 kHz) |
| **Fixed $I^2C$ address** | `0x2A` |
| **ADC resolution** | 24-bit Sigma-Delta ADC ($23$-bit Effective ENOB at 10 SPS) |
| **Differential channels** | 2 differential input channels (Ch1 for load cell, Ch2 for 2nd cell / battery) |
| **Programmable Gain (PGA)**| $\times 1, \times 2, \times 4, \times 8, \times 16, \times 32, \times 64, \times 128$ |
| **Sample rates** | 10 SPS, 20 SPS, 40 SPS, 80 SPS, 320 SPS (Samples Per Second) |
| **Load cell excitation LDO**| Built-in programmable LDO regulator ($2.4\text{V}$ to $4.5\text{V}$ output) |

## Pinout

Breakout module header & Qwiic / STEMMA QT connectors:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply input (+2.7 V to +5.5 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 4 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 5 | `E+` / `AVDD` | Power Output | Excitation voltage output to load cell positive terminal |
| 6 | `E-` / `AGND` | Power Output | Excitation ground to load cell negative terminal |
| 7 | `A+` / `IN1P` | Analog Input | Channel 1 positive differential input (Green load cell wire) |
| 8 | `A-` / `IN1N` | Analog Input | Channel 1 negative differential input (White load cell wire) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.7 | 3.3 / 5.0 | 5.5 | V | DC |
| Active Operating Current| $I_{CC}$ | — | 2.1 | 3.0 | mA | Active conversion state |
| Power-Down Current | $I_{pd}$ | — | 1.0 | 5.0 | µA | Sleep mode |
| PGA Gain ($\times 128$) | $G_{128}$ | — | 128 | — | V/V | Full-scale input voltage $\pm 19.5\text{ mV}$ |
| Input Referred Noise | $V_{noise}$ | — | 50 | — | nV RMS | At 10 SPS, Gain $\times 128$ |
| Internal LDO Voltage | $V_{AVDD}$| 2.4 | 3.3 | 4.5 | V | Configurable excitation output |
| Offset Temp Drift | $Drift_{off}$| — | 5 | — | nV/°C | Temperature compensated |

## Load Cell Wiring (Standard 4-Wire Wheatstone Bridge)

| NAU7802 Terminal | → | Load Cell Wire Color | Function |
|---|---|---|---|
| `E+` | | Red Wire | Excitation Positive ($V_{EXC+}$) |
| `E-` | | Black Wire | Excitation Negative / Ground ($V_{EXC-}$) |
| `A+` | | Green Wire | Signal Positive ($V_{SIG+}$) |
| `A-` | | White Wire | Signal Negative ($V_{SIG-}$) |

## Wiring

| NAU7802 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |

## Example (SparkFun NAU7802 Arduino Library)

```cpp
#include <Wire.h>
#include "SparkFun_NAU7802_Arduino_Library.h"

NAU7802 myScale;

void setup() {
  Serial.begin(115200);
  Wire.begin();

  Serial.println("NAU7802 24-Bit Scale Test");

  if (!myScale.begin()) {
    Serial.println("NAU7802 not detected! Check I2C wiring.");
    while (1);
  }

  // Set gain to 128 for strain gauge load cell
  myScale.setGain(NAU7802_GAIN_128);
  // Set sample rate to 10 SPS for maximum noise filtering
  myScale.setSampleRate(NAU7802_SPS_10);
  // Calibrate internal ADC offset
  myScale.calibrateAFE();

  Serial.println("Scale initialized. Zeroing...");
}

void loop() {
  if (myScale.available()) {
    int32_t rawReading = myScale.getReading();
    Serial.print("Raw 24-bit ADC Reading: "); Serial.println(rawReading);
  }
  delay(100);
}
```

## Common mistakes

- **Comparing NAU7802 to HX711 libraries:** NAU7802 uses standard $I^2C$ (`0x2A`); HX711 uses a proprietary 2-pin bit-banged pulse-clock interface. Do not use HX711 Arduino libraries with the NAU7802.
- **Forgetting internal AFE calibration:** Call `calibrateAFE()` on power-up to remove internal ADC and PGA offset voltage errors before taring weight measurements.

## Notes

- **NAU7802 vs HX711 vs ADS1232:** NAU7802 uses $I^2C$ (freeing up GPIO pins) and includes programmable gain, channel switching, and internal LDO control in software.
