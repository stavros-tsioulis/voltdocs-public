## Overview

The **MQ-135** is a broad-spectrum semiconductor air quality gas sensor manufactured by Winsen Electronics. It uses a tin-dioxide ($\text{SnO}_2$) sensitive layer whose electrical conductivity increases when exposed to hazardous airborne gases such as ammonia ($\text{NH}_3$), nitrogen oxides ($\text{NO}_x$), alcohol, benzene, smoke, and carbon dioxide ($\text{CO}_2$).

Breakout modules incorporate an internal micro-heater, an LM393 voltage comparator with an adjustable threshold potentiometer, a digital output pin (`DO`), and an analog output pin (`AO`) providing a voltage proportional to gas concentration.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 5.0 V $\pm 0.1\text{ V}$ DC (5V required for internal heater) |
| **Heater resistance ($R_H$)** | $31\text{ }\Omega \pm 3\text{ }\Omega$ |
| **Heater power consumption** | $\sim 800\text{ mW}$ ($160\text{ mA}$ current draw) |
| **Target gases** | Ammonia ($\text{NH}_3$), $\text{NO}_x$, Alcohol, Benzene, Smoke, $\text{CO}_2$ (estimated) |
| **Concentration range** | 10 ppm to 1000 ppm |
| **Outputs** | Analog voltage (`AO`: 0.1 V – 4.0 V) / Digital threshold (`DO`: TTL LOW when gas detected) |

## Pinout

### Standard 4-Pin Breakout Module

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+5.0 V DC required for internal heater coil) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `DO` | Digital Output | Digital threshold output (`HIGH` in clean air, goes `LOW` when gas exceeds threshold) |
| 4 | `AO` | Analog Output | Analog output voltage (0.1 V in clean air, increases up to ~4.5 V as gas concentration rises) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Sensor Circuit Voltage | $V_C$ | — | 5.0 | 5.0 | V | DC |
| Heater Voltage | $V_H$ | — | 5.0 | 5.0 | V | AC or DC |
| Load Resistance | $R_L$ | — | 20 | — | kΩ | Adjustable on breakout |
| Heater Resistance | $R_H$ | 28 | 31 | 34 | Ω | Room temperature ($20\text{ }^\circ\text{C}$) |
| Heater Power | $P_H$ | — | — | 800 | mW | $V_H = 5.0\text{ V}$ |
| Sensing Resistance | $R_S$ | 2 | — | 20 | kΩ | in 50 ppm $\text{NH}_3$ |
| Preheat Time | $t_{pre}$ | 24 | — | 48 | hours | Initial burn-in / stabilization |

## Sensitivity characteristics & calibration

The MQ-135 measures air quality by observing the resistance ratio $\frac{R_S}{R_0}$:
- $R_S$: Sensor resistance in target gas at various concentrations.
- $R_0$: Sensor resistance in clean air at specified temperature/humidity ($20\text{ }^\circ\text{C}$, 65% RH).

$$\text{Sensor Resistance } (R_S) = \left(\frac{V_C - V_{AO}}{V_{AO}}\right) \times R_L$$

To convert analog voltage ($V_{AO}$) to estimated gas concentration in PPM, calibrate $R_0$ in clean outdoor air ($\approx 415\text{ ppm }\text{CO}_2$ baseline), then apply the logarithmic power-law formula:

$$\text{PPM} = a \times \left(\frac{R_S}{R_0}\right)^b$$

where $a$ and $b$ are scaling factors derived from the Winsen datasheet curves for specific target gases.

## Wiring

| MQ-135 Module | → | Microcontroller (Arduino Uno / ESP32) | Notes |
|---|---|---|---|
| `VCC` | | `5V` | Must be 5V DC (3.3V will not heat element sufficiently) |
| `GND` | | `GND` | Ground |
| `AO` | | Analog Pin `A0` (or ESP32 `ADC1`) | Connects to ADC for quantitative measurement |
| `DO` | | Digital Pin `2` | Optional digital alarm threshold input |

> [!WARNING]
> High Current & Heating Hazard:
> - The MQ-135 internal heater draws up to **160 mA** continuous current. Do NOT power the sensor from a microcontroller's 3.3V rail or low-current GPIO pin.
> - The sensor body gets **warm to the touch** during normal operation. This is normal behavior required to burn off contaminants on the $\text{SnO}_2$ substrate.

## Common mistakes

- **Expecting true $\text{CO}_2$ measurement:** The MQ-135 is a metal-oxide semiconductor gas sensor, NOT an NDIR sensor. It estimates $\text{CO}_2$ as an equivalent proxy based on total volatile organic compounds (VOCs). Use NDIR sensors (such as **SCD30** or **SCD41**) for true carbon dioxide measurement.
- **Skipping preheat / burn-in period:** New MQ-135 sensors require a 24 to 48-hour initial burn-in period to stabilize baseline readings. Allow 3–5 minutes of preheating upon power-up before taking measurements.
- **Powering with 3.3V:** Operating the heater on 3.3V prevents the heating element from reaching its operating temperature, causing the sensor to output flat or erratic values.

## Notes

- Temperature and humidity affect sensor resistance $R_S$. For accurate indoor air quality monitoring, apply temperature compensation curves from the Winsen datasheet.
