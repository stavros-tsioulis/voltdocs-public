## Overview

The **MQ-2** is a semiconductor gas sensor manufactured by Winsen Electronics. It uses a tin-dioxide ($\text{SnO}_2$) sensitive layer whose electrical conductivity increases in the presence of combustible gases and smoke.

Breakout modules incorporate an internal internal micro-heater, an LM393 voltage comparator IC with a sensitivity adjustment potentiometer, a digital switching output (`DO`), and an analog output (`AO`) producing a voltage proportional to gas concentration.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 5.0 V $\pm 0.1\text{ V}$ DC (5V required for internal heater) |
| **Heater resistance ($R_H$)** | $31\text{ }\Omega \pm 3\text{ }\Omega$ |
| **Heater power consumption** | $\sim 800\text{ mW}$ ($160\text{ mA} \text{ current draw}$) |
| **Target gases** | LPG, Propane, Methane, Hydrogen, Alcohol, Smoke |
| **Concentration range** | 300 ppm to 10,000 ppm (combustible gases) |
| **Outputs** | Analog voltage (`AO`: 0.1 V – 4.0 V) / Digital threshold (`DO`: TTL LOW when gas detected) |

## Pinout

### Standard 4-Pin Breakout Module

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+5 V DC required for internal heater coil) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `DO` | Digital Output | Digital Output (`HIGH` in clean air, goes `LOW` when gas concentration exceeds threshold set by potentiometer) |
| 4 | `AO` | Analog Output | Analog Output voltage (0.1 V in clean air, increases up to ~4.5 V as gas concentration rises) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Sensor Circuit Voltage | $V_C$ | — | 5.0 | 5.0 | V | DC |
| Heater Voltage | $V_H$ | — | 5.0 | 5.0 | V | AC or DC |
| Load Resistance | $R_L$ | — | 20 | — | kΩ | Adjustable on breakout |
| Heater Resistance | $R_H$ | 28 | 31 | 34 | Ω | Room temperature ($20\text{ }^\circ\text{C}$) |
| Heater Power | $P_H$ | — | — | 800 | mW | $V_H = 5.0\text{ V}$ |
| Sensing Resistance | $R_S$ | 2 | — | 20 | kΩ | in 2000 ppm $C_3H_8$ (Propane) |
| Preheat Time | $t_{pre}$ | 24 | — | 48 | hours | Initial burn-in / stabilization |

## Sensitivity characteristics & calibration

The MQ-2 measures gas concentration by observing the resistance ratio $\frac{R_S}{R_0}$:
- $R_S$: Sensor resistance in target gas at various concentrations.
- $R_0$: Sensor resistance in clean air at specified temperature/humidity ($20\text{ }^\circ\text{C}$, 65% RH).

$$\text{Sensor Resistance } (R_S) = \left(\frac{V_C - V_{AO}}{V_{AO}}\right) \times R_L$$

To convert analog voltage ($V_{AO}$) to estimated gas concentration in PPM, calibrate $R_0$ in clean air, then apply the logarithmic power-law formula:

$$\log_{10}(\text{PPM}) = \frac{\log_{10}(R_S / R_0) - b}{m}$$

where $m$ and $b$ are derived from the datasheet's sensitivity characteristic curve for the specific target gas (e.g. LPG or Methane).

## Wiring

| MQ-2 Module | → | Microcontroller (Arduino Uno / ESP32) | Notes |
|---|---|---|---|
| `VCC` | | `5V` | Must be 5V DC (3.3V will not heat element sufficiently) |
| `GND` | | `GND` | Ground |
| `AO` | | Analog Pin `A0` (or ESP32 `ADC1`) | Connects to ADC for quantitative measurement |
| `DO` | | Digital Pin `2` | Optional digital alarm threshold input |

> [!WARNING]
> High Current & Heating Hazard:
> - The MQ-2 internal heater draws up to **160 mA** continuous current. Do NOT power the sensor from a microcontroller's 3.3V rail or low-current GPIO pin.
> - The sensor body gets **warm to the touch** during normal operation. This is normal behavior required to burn off contaminants on the $\text{SnO}_2$ substrate.

## Common mistakes

- **Skipping preheat / burn-in period:** New MQ-2 sensors require a 24 to 48-hour initial burn-in period to stabilize baseline readings. Even after initial burn-in, allow 1–3 minutes of preheating upon power-up before taking measurements.
- **Powering with 3.3V:** Operating the heater on 3.3V prevents the heating element from reaching its operating temperature ($300\text{ }^\circ\text{C}$ to $400\text{ }^\circ\text{C}$ internal), causing the sensor to output flat or erratic values.
- **Expecting non-selective gas detection:** The MQ-2 is a general semiconductor gas sensor. It cannot distinguish between LPG, Propane, Methane, or Smoke when multiple gases are present simultaneously.

## Notes

- **Environmental Compensation:** Temperature and humidity significantly affect $R_S$. For accurate measurements outdoors or across seasons, ambient temperature/humidity compensation curves from the Winsen datasheet should be applied in software.
