## Overview

The **A4988** is a complete microstepping motor driver IC manufactured by Allegro MicroSystems. Popularized in the "StepStick" form factor, it is the standard stepper motor driver module used in 3D printers (RAMPS boards), CNC routers, laser cutters, and automated robotics.

It features adjustable current limiting, overcurrent protection, thermal shutdown, mixed decay mode, and an internal translator that simplifies motor control to just two input lines: `STEP` (direction pulses) and `DIR` (rotational direction).

## Quick reference

| | |
|---|---|
| **Motor load supply (`VMOT`)** | 8.0 V to 35.0 V DC |
| **Logic supply (`VDD`)** | 3.0 V to 5.5 V DC |
| **Continuous output current** | 1.0 A per phase (up to 2.0 A with active cooling / heatsink) |
| **Microstep resolution** | Full, 1/2, 1/4, 1/8, and 1/16 step modes |
| **Control interface** | Simple `STEP` and `DIR` pulse control |
| **Protection features** | Thermal shutdown, crossover-current protection, undervoltage lockout |

## Pinout

### Standard StepStick / Pololu Module Pinout

```
           ┌─────────┐
     EN ───│ 1    16 │─── VMOT
    MS1 ───│ 2    15 │─── GND (Motor)
    MS2 ───│ 3    14 │─── 2B
    MS3 ───│ 4    13 │─── 2A
  RST* ───│ 5    12 │─── 1A
  SLP* ───│ 6    11 │─── 1B
   STEP ───│ 7    10 │─── VDD
    DIR ───│ 8     9 │─── GND (Logic)
           └─────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `ENABLE` | Digital Input | Active-LOW driver enable (`LOW` = outputs enabled, `HIGH` = outputs disabled) |
| 2 | `MS1` | Digital Input | Microstep resolution selection pin 1 |
| 3 | `MS2` | Digital Input | Microstep resolution selection pin 2 |
| 4 | `MS3` | Digital Input | Microstep resolution selection pin 3 |
| 5 | `RESET` | Digital Input | Active-LOW reset pin (tied to `SLEEP` for normal operation) |
| 6 | `SLEEP` | Digital Input | Active-LOW sleep pin (`LOW` = sleep mode enabled, disables outputs) |
| 7 | `STEP` | Digital Input | Step pulse input (motor steps on LOW-to-HIGH rising edge) |
| 8 | `DIR` | Digital Input | Direction input (`LOW` = clockwise / direction 1, `HIGH` = counter-clockwise) |
| 9 | `GND` | Power | Logic ground (0 V) |
| 10 | `VDD` | Power | Logic supply voltage (+3.0 V to +5.5 V) |
| 11 | `1B` | Motor Output | Bipolar Stepper Coil 1 Phase B |
| 12 | `1A` | Motor Output | Bipolar Stepper Coil 1 Phase A |
| 13 | `2A` | Motor Output | Bipolar Stepper Coil 2 Phase A |
| 14 | `2B` | Motor Output | Bipolar Stepper Coil 2 Phase B |
| 15 | `GND` | Power | Motor power ground (0 V) |
| 16 | `VMOT` | Power | Motor power supply voltage (+8.0 V to +35.0 V DC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Motor Load Supply | $V_{MOT}$ | 8.0 | 24.0 | 35.0 | V | DC |
| Logic Supply Voltage | $V_{DD}$ | 3.0 | 5.0 | 5.5 | V | DC |
| Output Current | $I_{OUT}$ | -2.0 | — | 2.0 | A | Peak phase current |
| High-side FET $R_{DS(ON)}$ | $R_{DSH}$ | — | 300 | 430 | mΩ | $I_{OUT} = 1\text{ A}$, $T_J = 25^\circ\text{C}$ |
| Low-side FET $R_{DS(ON)}$ | $R_{DSL}$ | — | 300 | 430 | mΩ | $I_{OUT} = 1\text{ A}$, $T_J = 25^\circ\text{C}$ |
| Thermal Shutdown Temp | $T_{JTSD}$ | 155 | 165 | 175 | °C | Junction temperature |

## Microstep selection table

| `MS1` | `MS2` | `MS3` | Microstep Resolution | Step Angle (1.8° Motor) |
|---|---|---|---|---|
| `LOW` | `LOW` | `LOW` | **Full Step** | 1.8° |
| `HIGH` | `LOW` | `LOW` | **Half Step** (1/2) | 0.9° |
| `LOW` | `HIGH` | `LOW` | **Quarter Step** (1/4) | 0.45° |
| `HIGH` | `HIGH` | `LOW` | **Eighth Step** (1/8) | 0.225° |
| `HIGH` | `HIGH` | `HIGH` | **Sixteenth Step** (1/16) | 0.1125° |

## Current limiting calibration

Before running a motor, adjust the onboard potentiometer to limit max motor current ($I_{TripMAX}$):

$$V_{REF} = I_{TripMAX} \times 8 \times R_{S}$$

Where $R_S$ is the current sense resistor value on the module (typically $0.1\text{ }\Omega$ or $0.05\text{ }\Omega$, marked `R100` or `R050`).

Example for a 1.0 A current limit on a board with $R_S = 0.1\text{ }\Omega$ (`R100`):
$$V_{REF} = 1.0\text{ A} \times 8 \times 0.1\text{ }\Omega = 0.8\text{ V}$$

Measure $V_{REF}$ with a multimeter between ground and the metal wiper of the potentiometer.

## Wiring

| A4988 Module | → | Microcontroller / Power Supply / Motor |
|---|---|---|
| `VMOT` / `GND` (Motor) | | External Power Supply (12V/24V DC, $\ge 100\text{ }\mu\text{F}$ decoupling cap) |
| `VDD` / `GND` (Logic) | | Microcontroller `5V` (or `3.3V`) and `GND` |
| `STEP` | | Digital Output Pin (e.g. GPIO2) |
| `DIR` | | Digital Output Pin (e.g. GPIO3) |
| `RESET` & `SLEEP` | | **Tied together** (bridges reset and sleep for normal operation) |
| `1A`, `1B` | | Stepper Motor Coil 1 (Pair A) |
| `2A`, `2B` | | Stepper Motor Coil 2 (Pair B) |

> [!WARNING]
> LC Voltage Spike Danger:
> - **Disconnecting a motor while powered destroys the A4988.** Never connect or disconnect a stepper motor while the `VMOT` supply is active.
> - Always connect a **$100\text{ }\mu\text{F}$ electrolytic decoupling capacitor** across `VMOT` and `GND` close to the driver module to absorb destructive voltage spikes.

## Common mistakes

- **Missing $100\text{ }\mu\text{F}$ decoupling capacitor across `VMOT` and `GND`:** Without this capacitor, inductive voltage spikes when motor currents switch off can exceed 35V and instantly destroy the driver IC.
- **Leaving RESET or SLEEP pins floating:** Both `RESET` and `SLEEP` are active-LOW inputs. Floating pins cause the driver to enter sleep mode randomly. Connect `RESET` and `SLEEP` together with a jumper.
- **Unadjusted $V_{REF}$ potentiometer:** Turning power on without calibrating current limit can deliver excessive current, causing motor overheating, skipped steps, or thermal shutdown.

## Notes

- Thermal performance improves significantly when adding an aluminum heatsink on top of the IC chip and using forced airflow.
