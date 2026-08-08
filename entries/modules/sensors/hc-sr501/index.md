## Overview

The **HC-SR501** is an automatic pyroelectric infrared (PIR) motion sensor module based on the BISS0001 micro-power PIR processing IC. It detects motion by sensing changes in infrared radiation (heat) emitted by human bodies, animals, or objects passing across its field of view.

The module features a hemispherical white Fresnel lens that focuses IR radiation onto dual internal pyroelectric sensor elements. Onboard potentiometers allow users to adjust detection sensitivity (3 m to 7 m range) and output delay time (0.5 s to 300 s), while a jumper selects between single and repeatable trigger modes.

## Quick reference

| | |
|---|---|
| **Supply voltage (`VCC`)** | 4.5 V to 20.0 V DC (5 V nominal) |
| **Output logic level** | 3.3 V TTL (`HIGH` when motion detected, `LOW` when idle) |
| **Quiescent current** | $< 50\text{ }\mu\text{A}$ |
| **Sensing distance** | Adjustable 3 m to 7 m |
| **Sensing angle** | $< 120^\circ$ cone angle |
| **Delay time** | Adjustable 0.5 s to 300 s |
| **Trigger mode** | Jumper-selectable: Non-repeatable (`L`) / Repeatable (`H`) |

## Pinout

### Standard 3-Pin Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+4.5 V to +20.0 V DC) |
| 2 | `OUT` | Digital Output | Motion detection output (3.3 V HIGH on motion, 0 V LOW idle) |
| 3 | `GND` | Power | Ground (0 V) |

### Controls & Jumpers

- **Sensitivity Potentiometer (`Sx` / `SENS`):** Turn clockwise to increase sensing distance (up to ~7 m); counter-clockwise to decrease (~3 m).
- **Delay Time Potentiometer (`Tx` / `TIME`):** Turn clockwise to increase output pulse duration (up to 300 s); counter-clockwise to decrease (~0.5 s).
- **Trigger Mode Jumper (`L` / `H`):**
  - **`H` (Repeatable / Retriggerable):** Output remains HIGH as long as continuous motion is detected within the delay period.
  - **`L` (Single / Non-repeatable):** Output goes HIGH for the set delay duration, then goes LOW regardless of ongoing motion.

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 4.5 | 5.0 | 20.0 | V | DC |
| Output HIGH Voltage | $V_{OH}$ | — | 3.3 | — | V | Motion detected |
| Output LOW Voltage | $V_{OL}$ | — | 0.0 | — | V | Idle / no motion |
| Quiescent Current | $I_{Q}$ | — | 50 | 65 | µA | $V_{CC} = 5.0\text{ V}$ |
| Detection Angle | $\theta$ | — | — | 120 | ° | Cone angle with Fresnel lens |
| Detection Range | $d$ | 3 | — | 7 | m | Adjustable via potentiometer |
| Output Delay Time | $t_d$ | 0.5 | — | 300 | s | Adjustable via potentiometer |
| Inhibit / Block Time | $t_{block}$ | — | 2.5 | — | s | Dead time between triggers |

## Wiring

| HC-SR501 Pin | → | Microcontroller (Arduino / ESP32) | Notes |
|---|---|---|---|
| `VCC` | | `5V` (or 4.5V–20V external supply) | Onboard 3.3V LDO requires $\ge 4.5\text{ V}$ input |
| `OUT` | | Digital Input Pin (e.g. GPIO4) | 3.3V TTL signal (safe for 3.3V ESP32 / Pi GPIO) |
| `GND` | | `GND` | Ground |

> [!NOTE]
> Warm-up / Initialization Period:
> Upon initial power-up, the HC-SR501 requires **30 to 60 seconds** to calibrate to background thermal radiation. During this period, the output pin may toggle randomly 1 to 3 times. Ignore sensor readings during the first minute after powering on.

## Common mistakes

- **Powering from 3.3V rail:** The module contains an onboard 3.3V LDO regulator (e.g. 7133). Supplying 3.3V to `VCC` causes the regulator to drop out, producing erratic triggers or a completely non-responsive output. Always feed `VCC` with $\ge 4.5\text{ V}$.
- **Ignoring the 2.5-second block time:** After outputting a LOW signal, the BISS0001 IC enforces a ~2.5 second inhibit time during which no motion can trigger the sensor. Rapid motion testing will appear to miss triggers.
- **Placing near heat / draft sources:** Air conditioners, direct sunlight, heating vents, or high-power warm components can create thermal air currents that false-trigger PIR sensors.

## Notes

- The 3.3V output level makes the `OUT` signal directly compatible with 3.3V microcontrollers (ESP32, ESP8266, Raspberry Pi) without needing level shifters.
