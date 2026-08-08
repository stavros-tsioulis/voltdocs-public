## Overview

The **MQ-7** is a semiconductor gas sensor manufactured by Winsen Electronics specifically designed to detect toxic **Carbon Monoxide (CO)** gas concentrations in air ($20\text{ to }2000\text{ ppm}$).

Unlike general gas sensors (such as MQ-2 or MQ-135) that operate at a constant 5V heater voltage, the MQ-7 requires a **high-low temperature cycling protocol**: heating at 5.0 V for 60 seconds (cleaning phase) followed by heating at 1.4 V for 90 seconds (measurement phase). CO gas concentration is read at the end of the 1.4 V measurement phase.

## Quick reference

| | |
|---|---|
| **High heater voltage ($V_{H,high}$)** | 5.0 V DC (60 seconds cleaning cycle) |
| **Low heater voltage ($V_{H,low}$)** | 1.4 V DC (90 seconds measurement cycle) |
| **Circuit voltage ($V_C$)** | 5.0 V $\pm 0.1\text{ V}$ DC |
| **Heater resistance ($R_H$)** | $33\text{ }\Omega \pm 3\text{ }\Omega$ |
| **Average heater power** | ~350 mW (cycled) |
| **Target gas** | Carbon Monoxide (CO) |
| **Detection range** | 20 ppm to 2000 ppm CO |
| **Outputs** | Analog voltage (`AO`) / Digital threshold (`DO` via LM393) |

## Pinout

### Standard 4-Pin Breakout Module

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+5.0 V DC for circuit and high-cycle heater) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `DO` | Digital Output | Digital comparator output (`HIGH` clean, `LOW` on CO alarm) |
| 4 | `AO` | Analog Output | Analog output voltage (measured during 1.4V phase) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| High Heater Voltage | $V_{H,high}$ | 4.9 | 5.0 | 5.1 | V | 60 seconds cleaning cycle |
| Low Heater Voltage | $V_{H,low}$ | 1.35 | 1.4 | 1.45 | V | 90 seconds measurement cycle |
| Sensing Resistance | $R_S$ | 2 | — | 20 | kΩ | in 100 ppm CO |
| Sensitivity Ratio | $\alpha$ | 0.25 | — | 0.5 | — | $R_S\text{(100ppm CO)} / R_S\text{(clean air)}$ |
| Cycle Heating Time | $t_{cycle}$ | — | 150 | — | s | 60s @ 5V + 90s @ 1.4V |
| Operating Temperature | $T_{OP}$ | -20 | — | 50 | °C | |
| Operating Humidity | $RH_{OP}$ | — | — | 95 | % RH | Non-condensing |

## Temperature Cycling Protocol & Timing

To measure CO accurately without cross-sensitivity to other gases, software or hardware PWM must cycle the heater element:

```
V_Heater  ───┐ 5.0V (60s Cleaning) ┌─── 1.4V (90s Measure) ───┐ 5.0V ...
             └─────────────────────┘                           └───────
Time      ◄─────── 60 sec ────────►◄───────── 90 sec ─────────►
                                                      ▲
                                            Read Analog Voltage (AO) Here
```

1. **Cycle 1 (Cleaning Phase):** Apply $V_H = 5.0\text{ V}$ for **60 seconds**. The high temperature burns off stored contaminants and adsorbed gases from the tin-dioxide substrate. Do not read measurements during this phase.
2. **Cycle 2 (Measurement Phase):** Lower $V_H$ to **1.4 V** (using PWM duty cycle $\sim 28\%$ on a 5V supply) for **90 seconds**.
3. **Read Sensor:** Read analog voltage on `AO` during the last 5 seconds of the 1.4 V low-voltage phase.

## Wiring

| MQ-7 Module Pin | → | Microcontroller / Driver | Notes |
|---|---|---|---|
| `VCC` (Circuit) | | `5V` DC | Powers sensor circuit and comparator |
| `GND` | | `GND` | Ground |
| `AO` | | Analog Input Pin `A0` | Measure voltage during 1.4V phase |
| `Heater VCC` | | Transistor / MOSFET PWM Pin | Cycle heater between 5V (100% PWM) and 1.4V (28% PWM) |

> [!WARNING]
> Life-Safety Warning:
> The MQ-7 is an educational/hobbyist sensor. It is **NOT rated for life-safety CO alarm systems** or commercial building safety compliance. Always use certified commercial CO detectors for human life safety.

## Common mistakes

- **Operating continuously at 5.0V:** Running the heater constantly at 5.0V prevents the sensor from detecting CO gas effectively and causes false baseline readings.
- **Reading analog output during the 5.0V phase:** Measurements taken during the 60-second 5.0V cleaning phase measure burned-off contaminants rather than actual CO concentration.
- **Skipping initial 24-hour burn-in:** New MQ-7 sensors require a 24 to 48-hour continuous preheat period before initial calibration to establish a stable baseline $R_0$.

## Notes

- Calculate CO PPM: $R_S = \frac{V_C - V_{AO}}{V_{AO}} \times R_L$, then apply the Winsen logarithmic formula: $\text{PPM} = 100 \times \left(\frac{R_S}{R_0}\right)^{-1.5}$.
