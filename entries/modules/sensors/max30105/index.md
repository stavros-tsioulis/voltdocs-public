## Overview

The **MAX30105** is a high-sensitivity optical sensor module manufactured by Maxim Integrated (Analog Devices). Optimized for particle sensing, smoke/fire alarm detection, and PPG biometric monitoring, it integrates **three internal LEDs** (Red 660 nm, Infrared 880 nm, Green 537 nm), a high-sensitivity photodetector, ambient light rejection optics, and a low-noise **18-bit Delta-Sigma ADC**.

While similar to biometrics-only chips like the MAX30102, the MAX30105 includes a **Green LED** that provides superior sensitivity for measuring smoke particles, airborne dust, and high-resolution heart-rate/pulse-oximetry ($SpO_2$) readings over $I^2C$ (`0x57`).

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.0 V DC (breakout includes 1.8V & 5V LDO regulators) |
| **IC supply voltage (`VDD`)** | 1.7 V to 2.0 V DC (1.8 V nominal) |
| **LED supply voltage (`VLED`)**| 3.1 V to 5.25 V DC (5.0 V nominal) |
| **Interface** | $I^2C$ (Fast Mode up to 400 kHz) |
| **Fixed $I^2C$ address** | `0x57` |
| **Integrated LEDs** | 660 nm Red, 880 nm Infrared, 537 nm Green |
| **ADC resolution** | 18-bit (up to 262,144 counts per channel) |
| **Programmable sample rate** | 50 SPS to 3,200 SPS (Samples Per Second) |
| **Internal FIFO buffer** | 32-sample FIFO buffer |

## Pinout

Breakout module header & Qwiic / STEMMA QT connectors:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VIN` | Power | Supply input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 4 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 5 | `INT` | Digital Output | Active-Low interrupt output (FIFO almost full / Data ready) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{VIN}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with LDO |
| Operating Current | $I_{CC}$ | — | 0.6 | 1.2 | mA | Continuous sampling state |
| Shutdown Current | $I_{sd}$ | — | 0.7 | 2.0 | µA | Software shutdown mode |
| LED Peak Wavelength (Red)| $\lambda_{Red}$| 650 | 660 | 670 | nm | Red pulse LED |
| LED Peak Wavelength (IR) | $\lambda_{IR}$ | 870 | 880 | 890 | nm | IR pulse LED |
| LED Peak Wavelength (Green)| $\lambda_{Green}$| 520 | 537 | 550 | nm | Green smoke/particle LED |
| LED Current Range | $I_{LED}$ | 0.0 | — | 50.0 | mA | Programmable 8-bit DAC ($0.2\text{ mA}$ step) |

## Multi-LED Optical Particle Detection Logic

- **Airborne Particle / Smoke Detection:** When dust or smoke enters the optical chamber, light emitted by the Red, IR, and Green LEDs scatters off particles onto the photodetector (Mie scattering).
- **Particle Size Discrimination:** The short wavelength of the **Green LED ($537\text{ nm}$)** scatters strongly off fine smoke particles ($\le 1.0\ \mu\text{m}$), whereas **IR ($880\text{ nm}$)** scatters off larger dust grains ($\ge 2.5\ \mu\text{m}$). Comparing channel ratios allows distinguishing smoke from dust.

## Wiring

| MAX30105 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VIN` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |

## Example (SparkFun MAX30105 Particle Sensor Library)

```cpp
#include <Wire.h>
#include "MAX30105.h"

MAX30105 particleSensor;

void setup() {
  Serial.begin(115200);
  Wire.begin();

  Serial.println("SparkFun MAX30105 Particle Sensor Test");

  if (!particleSensor.begin(Wire, I2C_SPEED_FAST)) {
    Serial.println("MAX30105 not found! Check I2C wiring.");
    while (1);
  }

  // Setup sensor for particle sensing: 411us pulse width, 100 SPS, 400x ADC range
  byte ledBrightness = 0x1F; // Options: 0=Off to 255=50mA
  byte sampleAverage = 4; // Options: 1, 2, 4, 8, 16, 32
  byte ledMode = 3; // Options: 1 = Red only, 2 = Red + IR, 3 = Red + IR + Green
  int sampleRate = 100; // Options: 50, 100, 200, 400, 800, 1000, 1600, 3200
  int pulseWidth = 411; // Options: 69, 118, 215, 411
  int adcRange = 4096; // Options: 2048, 4096, 8192, 16384

  particleSensor.setup(ledBrightness, sampleAverage, ledMode, sampleRate, pulseWidth, adcRange);
  Serial.println("MAX30105 Particle Sensor Active.");
}

void loop() {
  uint32_t red = particleSensor.getRed();
  uint32_t ir = particleSensor.getIR();
  uint32_t green = particleSensor.getGreen();

  Serial.print("Red: "); Serial.print(red);
  Serial.print(" | IR: "); Serial.print(ir);
  Serial.print(" | Green: "); Serial.println(green);

  delay(200);
}
```

## Common mistakes

- **Covering sensor glass with opaque enclosures:** The optical window must remain un-obstructed or protected by high-transmittance clear glass ($>90\%$ light transmission across $500\text{--}900\text{ nm}$).
- **Overdriving LED currents:** Operating all 3 LEDs at max current ($50\text{ mA}$) causes PCB thermal heating ($+2^\circ\text{C}\dots +4^\circ\text{C}$). Keep LED brightness values under $0x1F$ ($6.4\text{ mA}$) for continuous particle monitoring.

## Notes

- **MAX30105 vs MAX30102 vs MAX30100:** MAX30105 includes 3 LEDs (Red, IR, Green) for particle/smoke sensing; MAX30102 includes 2 LEDs (Red, IR) for pulse oximetry.
