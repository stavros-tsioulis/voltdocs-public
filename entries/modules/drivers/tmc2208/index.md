## Overview

The **TMC2208** (TMC2208-LA) is an advanced 2-phase stepper motor driver IC manufactured by Trinamic (Analog Devices), widely used as a drop-in **SilentStepStick** breakout module for 3D printers (Ender 3, Prusa, Marlin/Klipper mainboards), CNC machines, and precision motion control robotics.

Equipped with Trinamic's patented **StealthChop2** silent chopper technology, the TMC2208 eliminates audible stepper motor hum and high-pitched whining during standstill and slow movements. It supports motor supply voltages from **4.75V to 36V DC**, continuous phase currents up to **1.2A RMS** ($2.0\text{A}$ peak), **MicroPlyer 1/256-microstep interpolation**, and a single-wire **UART interface** for software-based current scaling, microstep setting, and diagnostic monitoring.

## Quick reference

| | |
|---|---|
| **Motor Supply Voltage (`VM`)** | 4.75 V to 36 V DC |
| **Logic Supply Voltage (`VIO`)** | 3.0 V to 5.25 V DC (3.3V and 5V compatible) |
| **Phase Current Rating** | $1.2\text{ A}_{\text{RMS}}$ continuous ($2.0\text{ A}$ peak) |
| **Microstep Resolutions** | 1, 1/2, 1/4, 1/8, 1/16 (Interpolated to 1/256 via MicroPlyer) |
| **Chopper Modes** | StealthChop2 (Silent PWM) & SpreadCycle (High dynamic torque) |
| **Configuration Modes** | Standalone OTP/MS1/MS2 pins OR Single-Wire UART Interface |
| **Current Control** | Internal VREF Potentiometer OR UART Digital Scaling |
| **Package** | 28-pin QFN ($5 \times 5\text{ mm}$) / SilentStepStick 16-pin Module |

## Pinout (SilentStepStick 16-Pin Breakout Header)

```
                       ┌─────────────┐
                 [EN] 1│ 1        16│ [VM] (Motor Power 4.75-36V)
                [MS1] 2│            │15 [GND] (Motor Power GND)
                [MS2] 3│  TMC2208   │14 [2B] (Motor Phase B)
                [PDN] 4│ SilentStep │13 [2A] (Motor Phase B)
               [UART] 5│   Stick    │12 [1A] (Motor Phase A)
                [NC]  6│            │11 [1B] (Motor Phase A)
               [STEP] 7│            │10 [VIO] (Logic Power 3.3/5V)
                [DIR] 8│            │9  [GND] (Logic Power GND)
                       └─────────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `EN` | Input | Enable Motor Driver (Low = Enable outputs; High = Disable) |
| 2 | `MS1` | Input | Microstep Select Pin 1 (Pullup/Pulldown to GND/VIO) |
| 3 | `MS2` | Input | Microstep Select Pin 2 (Pullup/Pulldown to GND/VIO) |
| 4/5 | `PDN_UART` | I/O | Single-Wire UART Pin / Power Down Input |
| 7 | `STEP` | Input | Step Pulse Input (Rising edge triggers microstep) |
| 8 | `DIR` | Input | Direction Input (High/Low sets rotation direction) |
| 10 | `VIO` | Power | Logic Power Supply (+3.0V to +5.25V DC) |
| 11–14 | `1B, 1A, 2A, 2B` | Output | Motor Phase Connections (Phase A: 1A/1B, Phase B: 2A/2B) |
| 15 | `GND` | Power | Power Ground |
| 16 | `VM` | Power | Motor Power Supply (+4.75V to +36V DC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Motor Supply Voltage | $V_M$ | 4.75 | 24.0 | 36.0 | V | DC |
| Logic Supply Voltage | $V_{IO}$ | 3.0 | 3.3/5.0| 5.25 | V | DC |
| Continuous Current per Phase| $I_{RMS}$ | — | 1.2 | 1.4 | A | $T_A = 25^\circ\text{C}$ with cooling |
| Peak Output Current | $I_{PEAK}$ | — | — | 2.0 | A | Short peak duration |
| RDS(on) MOSFET Switch | $R_{DS(on)}$| — | 280 | 320 | mΩ | $V_{VM} = 24\text{V}, T_J = 25^\circ\text{C}$ |
| Step Frequency | $f_{STEP}$ | — | — | 500 | kHz | STEP input pin |

## Current Adjustment via $V_{REF}$ Potentiometer

In standalone mode, the maximum phase current $I_{RMS}$ is set via the small onboard potentiometer ($V_{REF}$):

$$ I_{RMS} = \frac{V_{REF}}{1.414} \times 0.71 \approx V_{REF} \times 0.5 \text{ (Amps)} $$

$$\text{For example, setting } V_{REF} = 1.6\text{V} \implies I_{RMS} \approx 0.8\text{A}.$$

## Common mistakes

- **Disconnecting motor while driver is powered:** Disconnecting a stepper motor connector while $V_M$ power is applied creates inductive back-EMF spikes that destroy the internal MOSFETs.
- **Forgetting motor bulk decoupling capacitor:** Always place a **$100\ \mu\text{F}$ electrolytic capacitor** between $V_M$ and $GND$ directly near the driver module pins to absorb voltage spikes.
- **Overheating without a heatsink:** Running currents above $0.8\text{A}$ without attaching an aluminum heatsink and cooling fan will trigger thermal shutdown ($150^\circ\text{C}$).

## Notes

- **TMC2208 vs A4988 vs TMC2209:** A4988 is loud with 1/16 microstepping; TMC2208 adds silent StealthChop2 and 1/256 interpolation; TMC2209 adds StallGuard4 sensorless homing and higher continuous current capability ($1.7\text{A}$ RMS).
