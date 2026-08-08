## Overview

The **TCRT5000** is a reflective optical sensor manufactured by Vishay Intertechnology. It houses a 950 nm infrared emitting diode (LED) and an NPN phototransistor detector side-by-side in a blue daylight-blocking plastic casing.

When an object or reflective surface passes in front of the sensor ($0.2\text{ mm to }15\text{ mm}$ distance), infrared light from the LED bounces back into the phototransistor, driving it into conduction. It is universally used in line-following robot cars (detecting black electrical tape on white floors), shaft encoders, and paper-edge detection.

## Quick reference

| | |
|---|---|
| **Module VCC** | 3.3 V to 5.0 V DC |
| **Peak Operating Distance** | **2.5 mm** ($0.2\text{ mm to }15\text{ mm}$ total range) |
| **IR Emitter Wavelength** | 950 nm |
| **IR Emitter Forward Voltage** | 1.25 V (requires series current limiting resistor $180\text{ }\Omega$ to $220\text{ }\Omega$ on 5V) |
| **Phototransistor Max Collector Current** | 100 mA |
| **Daylight Blocking Filter** | Integrated blue optical filter blocks ambient visible light |
| **Breakout Outputs** | Analog Voltage (`AO`) / Digital Threshold (`DO` via LM393) |

## Pinout

### Standard 4-Pin Breakout PCB Module

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `DO` | Digital Output | Digital threshold output (`HIGH` over non-reflective black surface, `LOW` over reflective white surface) |
| 4 | `AO` | Analog Output | Analog voltage output proportional to reflected IR light intensity |

### Component Level Pinout (TCRT5000 Package)

- **Anode (`A`) / Cathode (`K`):** Blue housing IR LED connections.
- **Collector (`C`) / Emitter (`E`):** Black housing NPN Phototransistor connections.

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Emitter Forward Voltage | $V_F$ | 1.0 | 1.25 | 1.5 | V | $I_F = 60\text{ mA}$ |
| Emitter Forward Current | $I_F$ | — | 30 | 60 | mA | Continuous DC |
| Collector Light Current | $I_{CA}$ | 0.2 | 1.0 | — | mA | $V_{CE} = 5\text{ V}$, $D = 2.5\text{ mm}$, Kodak neutral card |
| Peak Sensing Distance | $d_{opt}$ | — | 2.5 | — | mm | Optimum reflection distance |
| Day Filter Wavelength | $\lambda_p$ | — | 950 | — | nm | Peak spectral sensitivity |
| Operating Temperature | $T_{amb}$ | -25 | — | 85 | °C | |

## Reflectivity Principles (Line Following)

| Surface Type | IR Light Reflection | Phototransistor State | Analog Output Voltage (`AO`) | Digital Output (`DO`) |
|---|---|---|---|---|
| **White / Reflective Surface** | High Reflection | Conducting (ON) | **LOW** ($\approx 0.1\text{ V}$ – $0.5\text{ V}$) | **LOW** |
| **Black / Non-Reflective Tape** | Low / Absorbed | Off (Cutoff) | **HIGH** ($\approx V_{CC}$) | **HIGH** |
| **No Surface (Air Gap)** | Zero Reflection | Off (Cutoff) | **HIGH** ($\approx V_{CC}$) | **HIGH** |

## Wiring

| TCRT5000 Module Pin | → | Microcontroller (Arduino Uno / ESP32) |
|---|---|---|
| `VCC` | | `5V` (or `3.3V`) |
| `GND` | | `GND` |
| `DO` | | Digital GPIO Pin (e.g. D2 for line detection) |
| `AO` | | Analog Input Pin `A0` (optional for fine reflectivity gradient) |

## Common mistakes

- **Mounting too far from the ground:** The optimum detection height for line-following robots is **$2\text{ mm to }3\text{ mm}$** above the surface. Mounting the sensor $>15\text{ mm}$ high results in total loss of reflection signal.
- **Connecting bare TCRT5000 component without resistors:** Connecting the IR LED directly to 5V without a $220\text{ }\Omega$ series resistor burns out the IR LED immediately.
- **Ambient light interference:** Direct sunlight contains strong 950 nm IR radiation. Shield the sensor underside from direct outdoor sunlight.

## Notes

- The onboard LM393 potentiometer adjusts the switching threshold sensitivity between black tape and white background.
