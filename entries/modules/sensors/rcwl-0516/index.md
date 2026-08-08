## Overview

The **RCWL-0516** is a low-cost microwave motion sensor module that utilizes Doppler radar technology to detect moving objects (human beings, pets, vehicles). It operates at a frequency of **~3.18 GHz** using an microstrip patch antenna and an RCWL-9196 processing chip.

Unlike Passive Infrared (PIR) sensors (such as the HC-SR501) which rely on thermal infrared heat radiation and line-of-sight vision, the RCWL-0516 can detect movement through thin walls, doors, glass, and plastic enclosures with a **360-degree omnidirectional detection zone** up to $7\text{ meters}$.

## Quick reference

| | |
|---|---|
| **Operating Voltage (`VIN`)** | 4.0 V to 28.0 V DC (5.0 V nominal) |
| **Operating Frequency** | ~3.18 GHz (S-band Doppler radar) |
| **Detection Distance** | 5 m to 7 m (omnidirectional spherical pattern) |
| **Detection Angle** | 360 degrees (no blind spots) |
| **Output Signal** | Digital 3.3V TTL `HIGH` (held for ~2 seconds upon motion trigger) |
| **Transmitting Power** | 20 mW (typical) / 30 mW (max) |
| **Onboard Regulator (`3V3`)** | Provides regulated 3.3V output (up to 100 mA) for external MCUs |
| **Light Sensor Pad (`CDS`)** | Solder pads to attach a CdS photoresistor to disable motion detection in daylight |

## Pinout

### Standard 5-Pin Module Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `3V3` | Power Output | Regulated +3.3 V DC output (from internal LDO, up to 100 mA) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `OUT` | Digital Output | Motion trigger output (Normally `0V`, goes `3.3V HIGH` for ~2s when motion is detected) |
| 4 | `VIN` | Power Input | Supply voltage (+4.0 V to +28.0 V DC) |
| 5 | `CDS` | Control Input | Disable pin (Disable motion output when pulled below 0.7V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{IN}$ | 4.0 | 5.0 | 28.0 | V | DC |
| Quiescent Current | $I_{CC}$ | 2.2 | 2.8 | 3.0 | mA | Active scanning mode |
| Operating Frequency | $f_{RF}$ | 3.10 | 3.18 | 3.30 | GHz | Doppler radar |
| Output Voltage High | $V_{OH}$ | 3.2 | 3.3 | 3.4 | V | $OUT = HIGH$ on motion |
| Output Voltage Low | $V_{OL}$ | 0 | 0 | 0.1 | V | $OUT = LOW$ no motion |
| Trigger Hold Time | $t_{delay}$ | 1.8 | 2.0 | 2.5 | s | Base pulse width |
| Detection Distance | $d_{range}$ | 5.0 | 7.0 | 9.0 | m | Line of sight in open space |

## Optional Component Modification Pads

The back of the RCWL-0516 PCB contains SMD solder pads for fine-tuning performance:
- **`C-TM` (Timing Capacitor Pad):** Adding a 0805 capacitor lengthens the default 2-second output pulse time ($t_{delay}$).
- **`R-GN` (Gain Resistor Pad):** Adding a $1\text{ M}\Omega$ resistor reduces detection range from 7m to ~5m.
- **`R-CDS` (Light Sensor Pull-up Pad):** Solder a $47\text{ k}\Omega$ to $100\text{ k}\Omega$ resistor when adding a CdS LDR to the `CDS` pin for night-only motion triggering.

## Wiring

| RCWL-0516 Pin | → | Microcontroller (Arduino Uno / ESP32) |
|---|---|---|
| `VIN` | | `5V` (or 4V–28V external power) |
| `GND` | | `GND` |
| `OUT` | | Digital GPIO Pin (e.g. D2 for interrupt reading) |

> [!WARNING]
> Placement & False Triggering Guidance:
> - **Proximity to Wi-Fi / Bluetooth Routers:** High-power 2.4 GHz Wi-Fi signals (such as ESP32 Wi-Fi antennas or home routers placed $<1\text{ meter}$ away) can cause continuous false triggers on the 3.18 GHz microwave receiver. Maintain at least $50\text{ cm}$ clearance from active Wi-Fi antennas.
> - **Metal Shielding:** Do NOT enclose the front or back of the sensor inside metal cases. Metal reflects RF microwave signals, creating a total blind spot. Plastic, acrylic, and wood enclosures are transparent to 3.18 GHz microwaves.

## Common mistakes

- **Mounting two RCWL-0516 modules next to each other:** Placing two active microwave radar sensors within 2 meters of each other causes mutual RF interference and false triggering. Space sensors $>3\text{ meters}$ apart.
- **Expectation of static presence detection:** Doppler radar detects relative motion (moving objects). An individual standing completely still will eventually stop triggering the Doppler frequency shift output.
- **Expecting line-of-sight boundaries:** The radar penetrates thin drywall and glass. Motion in an adjacent room will trigger the sensor unless shielded by metal.

## Notes

- Ideal replacement for PIR sensors in outdoor weather-sealed enclosures where lens condensation or wind heat currents cause false PIR triggers.
