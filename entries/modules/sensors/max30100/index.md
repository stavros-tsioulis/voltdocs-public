## Overview

The **MAX30100** is an integrated pulse oximetry and heart-rate monitor IC manufactured by Maxim Integrated (Analog Devices). Designed for wearable health monitors, fitness trackers, and medical diagnostic equipment, it measures arterial blood oxygen saturation ($\text{SpO}_2\%$) and heart rate (BPM) from finger or earlobe contact over an $I^2C$ bus (`0x57`).

Housed in a tiny 14-pin optical package, the MAX30100 combines two internal LEDs (**660 nm Red** and **880 nm Infrared**), a high-sensitivity photodetector, ambient light cancellation circuitry, and a low-noise **16-bit Delta-Sigma ADC**.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.0 V DC (breakout module with 1.8V LDO) |
| **IC supply voltage (`VDD`)** | 1.7 V to 2.0 V DC (1.8 V nominal) |
| **LED supply voltage (`VLED`)**| 3.1 V to 5.25 V DC (3.3 V or 5.0 V nominal) |
| **Interface** | $I^2C$ (Fast Mode up to 400 kHz) |
| **Fixed $I^2C$ address** | `0x57` |
| **Integrated LEDs** | 660 nm Red & 880 nm Infrared |
| **ADC resolution** | 16-bit (up to 65,536 counts per channel) |
| **Sample rate range** | 50 SPS to 1,000 SPS (Samples Per Second) |
| **Internal FIFO buffer** | 16-sample FIFO buffer |

## Pinout

Standard 5-pin breakout module header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VIN` | Power | Supply power input (+3.3 V to +5.0 V DC) |
| 2 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 3 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 4 | `INT` | Digital Output | Active-Low interrupt output pin |
| 5 | `GND` | Power | Ground reference (0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{VIN}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with LDO |
| Active Supply Current | $I_{CC}$ | — | 0.6 | 1.2 | mA | Continuous sampling state |
| Shutdown Current | $I_{sd}$ | — | 0.7 | 2.0 | µA | Software shutdown mode |
| Red LED Peak Wavelength | $\lambda_{Red}$| 650 | 660 | 670 | nm | Oxygenated blood absorption |
| IR LED Peak Wavelength | $\lambda_{IR}$ | 870 | 880 | 890 | nm | Deoxygenated blood absorption |
| LED Current Range | $I_{LED}$ | 0.0 | — | 50.0 | mA | Programmable 4-bit DAC ($0\dots 50\text{ mA}$) |

## Photoplethysmography (PPG) & $\text{SpO}_2$ Math

1. **Heart Rate (BPM):** During cardiac systole, blood surges through finger capillaries, absorbing more IR light. Measuring AC periodic peak intervals on the IR channel yields heart rate in Beats Per Minute.
2. **Blood Oxygen Saturation ($\text{SpO}_2\%$):** Oxygenated hemoglobin ($\text{HbO}_2$) absorbs more Infrared light ($880\text{ nm}$); deoxygenated hemoglobin ($\text{Hb}$) absorbs more Red light ($660\text{ nm}$).

$$ R = \frac{(AC_{Red} / DC_{Red})}{(AC_{IR} / DC_{IR})} $$

$$ \text{SpO}_2\% = 110 - (25 \times R) $$

## Wiring

| MAX30100 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VIN` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |

> [!WARNING]
> Purple PCB LDO Resistor Bug Fix:
> - Cheap purple MAX30100 breakout PCBs contain a manufacturing error: $4.7\text{ k}\Omega$ pull-up resistors are erroneously connected to the $1.8\text{V}$ rail instead of $3.3\text{V}$, pulling $I^2C$ lines down and causing $I^2C$ bus read timeouts on 3.3V/5V MCUs.
> - Remove or replace the $4.7\text{ k}\Omega$ resistor network on purple boards, or use the updated green/black MAX30102 modules.

## Example (Arduino `MAX30100_PulseOximeter` Library)

```cpp
#include <Wire.h>
#include "MAX30100_PulseOximeter.h"

#define REPORTING_PERIOD_MS 1000

PulseOximeter pox;
uint32_t lastReportTime = 0;

void onBeatDetected() {
  Serial.println("Heartbeat pulse detected!");
}

void setup() {
  Serial.begin(115200);
  Serial.println("Initializing MAX30100 Pulse Oximeter...");

  if (!pox.begin()) {
    Serial.println("MAX30100 FAILED to initialize! Check wiring & I2C voltage.");
    while (1);
  }

  pox.setOnBeatDetectedCallback(onBeatDetected);
}

void loop() {
  // Update sensor readings continuously
  pox.update();

  if (millis() - lastReportTime > REPORTING_PERIOD_MS) {
    Serial.print("Heart Rate: "); Serial.print(pox.getHeartRate()); Serial.print(" BPM");
    Serial.print(" | SpO2: "); Serial.print(pox.getSpO2()); Serial.println(" %");
    lastReportTime = millis();
  }
}
```

## Common mistakes

- **Applying excessive finger pressure:** Pressing hard onto the sensor flattens skin capillaries, stopping blood flow and resulting in zero AC pulse detection. Rest finger gently over the optical window.
- **Ambient light interference:** Bright room lights flicker at 50/60 Hz, introducing noise into photodiode readings. Shield finger under dark cloth for clinical accuracy.

## Notes

- **MAX30100 vs MAX30102:** MAX30100 uses older 1.8V/3.3V optics and 16-bit resolution; MAX30102 features updated 18-bit ADC, higher SNR, and improved glass cover thermal insulation.
