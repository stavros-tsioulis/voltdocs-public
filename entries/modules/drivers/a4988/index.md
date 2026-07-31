## Overview

The **A4988** is a complete DMOS microstepping motor driver IC with built-in translator, designed by Allegro MicroSystems. It operates bipolar stepper motors in full-, half-, quarter-, eighth-, and sixteenth-step modes at motor voltages up to 35 V and output currents up to $\pm 2\text{ A}$.

Popularized by the 16-pin **Pololu-style carrier board** used in RAMPS 3D printer controller shields, CNC routers, and robotics builds, the A4988 simplifies stepper control down to two basic pins: `STEP` (pulse to take a step) and `DIR` (high/low for direction).

## Quick reference

| | |
|---|---|
| **Motor supply voltage (`VMOT`)** | 8.0 V – 35.0 V |
| **Logic supply voltage (`VDD`)** | 3.0 V – 5.5 V |
| **Continuous output current** | 1.0 A per phase without heat sink (up to 2.0 A with active cooling) |
| **Microstep resolution** | Full, 1/2, 1/4, 1/8, 1/16 microstepping |
| **Current control** | Adjustable current limiting via onboard potentiometer (`VREF`) |
| **Protection** | Thermal shutdown, under-voltage lockout, crossover-current protection |

## Pinout

### Standard 16-Pin Carrier Module (Pololu Form Factor)

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `EN` / `ENABLE` | Digital Input | Logic Input (Active-LOW: Enables output drivers; `HIGH` disables outputs) |
| 2 | `MS1` | Digital Input | Microstep resolution selection input 1 |
| 3 | `MS2` | Digital Input | Microstep resolution selection input 2 |
| 4 | `MS3` | Digital Input | Microstep resolution selection input 3 |
| 5 | `RESET` | Digital Input | Active-LOW reset input (Tied to `SLEEP` for normal operation) |
| 6 | `SLEEP` | Digital Input | Active-LOW sleep input (Disables internal circuitry to minimize power) |
| 7 | `STEP` | Digital Input | Step pulse input (Stepping occurs on rising edge) |
| 8 | `DIR` | Digital Input | Direction control input (`HIGH`: Clockwise, `LOW`: Counter-clockwise) |
| 9 | `GND` | Power | Logic Ground (0 V) |
| 10 | `VDD` | Power | Logic Supply Voltage (+3.0 V to +5.5 V) |
| 11 | `1B` | Motor Output | Bipolar Stepper Motor Coil B (Phase 2) |
| 12 | `1A` | Motor Output | Bipolar Stepper Motor Coil B (Phase 2) |
| 13 | `2A` | Motor Output | Bipolar Stepper Motor Coil A (Phase 1) |
| 14 | `2B` | Motor Output | Bipolar Stepper Motor Coil A (Phase 1) |
| 15 | `GND` | Power | Motor Power Ground |
| 16 | `VMOT` | Power | Motor Power Supply (+8.0 V to +35.0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Motor Supply Voltage | `VMOT` | 8.0 | — | 35.0 | V | Decoupled with 100 µF cap |
| Logic Supply Voltage | `VDD` | 3.0 | 5.0 | 5.5 | V | Digital logic supply |
| Continuous Output Current | `IOUT` | — | 1.0 | 2.0 | A | $V_{DD} = 5\text{ V}$, heatsink required > 1A |
| Reference Input Voltage | `VREF` | 0.0 | — | 2.5 | V | Sets current limit |
| Minimum Step High/Low Pulse | `tWH`, `tWL` | 1.0 | — | — | µs | `STEP` pulse width timing |
| Thermal Shutdown Temp | `TSD` | — | 165 | — | °C | Automatic thermal cutoff |

## Microstep resolution truth table

Microstep modes are configured by setting logic levels on `MS1`, `MS2`, and `MS3`.

| MS1 | MS2 | MS3 | Microstep Resolution | Step Angle (1.8° Motor) |
|---|---|---|---|---|
| LOW | LOW | LOW | Full Step | 1.8° |
| HIGH | LOW | LOW | Half Step (1/2) | 0.9° |
| LOW | HIGH | LOW | Quarter Step (1/4) | 0.45° |
| HIGH | HIGH | LOW | Eighth Step (1/8) | 0.225° |
| HIGH | HIGH | HIGH | Sixteenth Step (1/16) | 0.1125° |

> [!NOTE]
> `MS1`, `MS2`, and `MS3` have internal 100 kΩ pull-down resistors; leaving them disconnected selects Full Step mode.

## Setting the current limit (`VREF`)

To protect stepper motors from overheating, adjust the current limit via the onboard potentiometer before connecting the motor:

$$\text{Current Limit} (I_{trip}) = \frac{V_{\text{REF}}}{8 \times R_s}$$

Where $R_s$ is the current sense resistor value on the module (typically $0.05\ \Omega$ or $0.1\ \Omega$).
- For $R_s = 0.10\ \Omega$: $V_{\text{REF}} = I_{\text{limit}} \times 0.8$
- For $R_s = 0.05\ \Omega$: $V_{\text{REF}} = I_{\text{limit}} \times 0.4$

## Wiring

| A4988 Carrier Pin | → | Arduino Uno Pin | External Component |
|---|---|---|---|
| `VMOT` | | — | Motor Power `+12V` / `+24V` (with 100 µF Cap to GND) |
| `GND` (Pin 15) | | — | Motor Power Ground |
| `VDD` | | `5V` | Logic Power |
| `GND` (Pin 9) | | `GND` | Common Logic Ground |
| `STEP` | | Pin `3` | Step pulse output |
| `DIR` | | Pin `4` | Direction signal output |
| `RESET` | | `SLEEP` | Connected together to keep driver active |
| `1A`, `1B`, `2A`, `2B` | | — | Bipolar Stepper Motor Wires |

> [!WARNING]
> Always add a **100 µF electrolytic decoupling capacitor** close to the `VMOT` and `GND` pins. Disconnecting or connecting a motor while the driver is powered will destroy the A4988 IC via inductive voltage spikes.

## Common mistakes

- **Disconnecting motor wires while powered:** Disconnecting a stepper motor while `VMOT` is energized produces massive inductive back-EMF spikes (> 50 V) that instantly destroy the driver's output MOSFETs.
- **Forgetting to bridge RESET and SLEEP:** `RESET` and `SLEEP` are floating input pins. If left disconnected, the driver stays in sleep mode and ignores step pulses. Connect `RESET` directly to `SLEEP`.
- **Operating without heatsink at > 1A:** The A4988 module generates significant heat. Driving currents above 1.0 A per phase without an aluminum heatsink and cooling fan triggers thermal shutdown.
