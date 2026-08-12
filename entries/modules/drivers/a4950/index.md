## Overview

The **A4950** (specifically **A4950ELPTR-T** in an 8-pin SOIC package with exposed thermal pad) is a high-performance $3.5\text{ A}$ peak, $40\text{ V}$ full-bridge DMOS PWM motor driver IC manufactured by Allegro MicroSystems. Designed for bidirectional pulse-width modulated (PWM) control of brushed DC motors, solenoids, and inductive loads, it is widely used in robotics, 3D printers, and custom PCB motor controls.

Featuring a low combined $R_{DS(ON)}$ of **$0.3\ \Omega$** (high-side + low-side MOSFET total), the A4950 integrates adjustable PWM current limiting, synchronous rectification, overcurrent protection (OCP), and thermal shutdown.

## Quick reference

| | |
|---|---|
| **Driver Type** | Full-Bridge DMOS PWM Brushed DC Motor Driver |
| **Package** | SOIC-8 EP (Exposed Thermal Pad) / Pololu Motor Breakout |
| **Motor Supply Voltage ($V_{BB}$)** | $8.0\text{ V}$ to $40.0\text{ V}$ DC |
| **Peak Output Current** | Up to $3.5\text{ A}$ peak ($R_{DS(ON)} = 0.3\ \Omega$) |
| **Control Logic** | 2-Pin PWM Input Interface (`IN1`, `IN2`) |
| **Current Limiting** | Internal PWM current control set by `VREF` and sense resistor `ISEN` |
| **Protection Features** | Overcurrent Protection (OCP), Undervoltage Lockout (UVLO), Thermal Shutdown |

## Pinout (SOIC-8 EP Package)

```
        ┌──────────┐
    GND ─│ 1      8 │─ OUT2
    IN2 ─│ 2  EP  7 │─ ISEN
    IN1 ─│ 3      6 │─ OUT1
   VREF ─│ 4      5 │─ VBB
        └──────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `GND` | Ground reference (connected to exposed pad underneath) |
| 2 | `IN2` | Logic PWM input 2 |
| 3 | `IN1` | Logic PWM input 1 |
| 4 | `VREF` | Analog reference voltage input setting internal PWM current limit threshold |
| 5 | `VBB` | Motor power supply input (+8.0V to +40.0V DC) |
| 6 | `OUT1` | Full-bridge DMOS output 1 (connected to motor terminal 1) |
| 7 | `ISEN` | Current sense node (connects low-side MOSFET sources to GND via sense resistor) |
| 8 | `OUT2` | Full-bridge DMOS output 2 (connected to motor terminal 2) |

## Control Logic Truth Table

| `IN1` | `IN2` | `OUT1` | `OUT2` | Function / Mode |
|---|---|---|---|---|
| Low (`0`) | Low (`0`) | High-Z | High-Z | **Coast** (Slow decay / Off) |
| Low (`0`) | High (`1`) | Low | High | **Reverse** |
| High (`1`) | Low (`0`) | High | Low | **Forward** |
| High (`1`) | High (`1`) | Low | Low | **Brake** (Fast decay) |

## Current Limiting Calculation

The maximum trip current ($I_{TRIP}$) for internal PWM current control is determined by the analog voltage on `VREF` and the value of the current sense resistor ($R_{SENSE}$) connected between `ISEN` (Pin 7) and `GND`:

$$ I_{TRIP} = \frac{V_{REF}}{10 \times R_{SENSE}} $$

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Motor Supply Voltage | $V_{BB}$ | 8.0 | 24.0 | 40.0 | V | Operational range |
| Output Peak Current | $I_{OUT}$ | — | 3.5 | — | A | Duty cycle dependent |
| Total Switch $R_{DS(ON)}$ | $R_{DS(ON)}$ | — | 0.30 | 0.45 | $\Omega$ | $I_{OUT} = 2.0\text{A}, T_J = 25^\circ\text{C}$ |
| Logic High Input Voltage | $V_{IN(1)}$ | 2.0 | — | — | V | `IN1`, `IN2` |
| Logic Low Input Voltage | $V_{IN(0)}$ | — | — | 0.8 | V | `IN1`, `IN2` |
| Overcurrent Trip Threshold | $I_{OCP}$ | 3.7 | 4.8 | 6.0 | A | Short-circuit protection |
| Quiescent Current | $I_{BB}$ | — | 3.0 | 5.0 | mA | Standby mode |

## Common mistakes

- **Leaving the thermal pad unsoldered:** High peak currents generate heat on the SOIC-8 package. Solder the bottom exposed pad (`EP`) to a ground copper plane on the PCB with thermal vias.
- **Tying VREF directly to 5V without setting current limit:** Connecting `VREF` directly to $5\text{ V}$ with a $0.1\ \Omega$ sense resistor sets $I_{TRIP} = 5.0\text{ A}$, exceeding the chip's continuous rating. Divide `VREF` down to set $I_{TRIP}$ safely to your motor's rated current.

## Notes

- **A4950 vs L298N:** The A4950 uses modern low-resistance MOSFETs ($0.3\ \Omega$ vs $3\ \Omega$ for L298N), generating far less heat and delivering higher current in a tiny fraction of the board area.
