## Overview

The **MG996R** is a standard-size, high-torque RC servo motor manufactured by TowerPro. It features a complete metal gear train, dual ball bearings on the output shaft, and an upgraded internal PCB with a redesigned IC driver circuit providing greater deadband accuracy and positioning stability compared to its predecessor (the MG995).

Delivering up to $11\text{ kg}\cdot\text{cm}$ of stall torque at 6.0 V, the MG996R is widely used in robotic arms, hexapod walkers, steering mechanisms for 1/10-scale RC cars, large pan-tilt camera mounts, and mechanical automation projects.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 4.8 V to 7.2 V DC (6.0 V recommended) |
| **Stall torque** | $9.4\text{ kg}\cdot\text{cm}$ (at 4.8V) / $11.0\text{ kg}\cdot\text{cm}$ (at 6.0V) |
| **Operating speed** | 0.17 s / 60° (at 4.8V) / 0.14 s / 60° (at 6.0V) |
| **Rotation range** | ~180° total mechanical travel |
| **Control signal** | PWM (50 Hz / 20 ms frame period) |
| **Pulse width range** | 500 µs (0°) to 2400 µs (180°) |
| **Weight** | 55 g |

## Terminals & cable wiring

The MG996R uses a standard 3-pin 0.1" (2.54 mm) female JR/Futaba connector:

| Pin | Cable Color | Signal | Description |
|---|---|---|---|
| 1 | Brown / Black | `GND` | Ground (0 V) |
| 2 | Red | `VCC` | Power supply (+4.8 V to +7.2 V DC) |
| 3 | Orange / Yellow | `PWM` | Position control signal (50 Hz PWM) |

## Electrical & mechanical specifications

### Electrical Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Operating Voltage | $V_{CC}$ | 4.8 | 6.0 | 7.2 | V | DC supply |
| Running Current (No Load) | $I_{run}$ | 170 | 200 | 250 | mA | $V_{CC} = 6.0\text{ V}$, static motion |
| Running Current (Loaded) | $I_{load}$ | 500 | 700 | 900 | mA | Under mechanical load |
| Stall Current | $I_{stall}$ | 1.2 | 1.4 | 2.5 | A | $V_{CC} = 6.0\text{ V}$, shaft locked |
| Dead Band Width | $t_{db}$ | — | 5 | 8 | µs | Position resolution threshold |

### Mechanical Specifications

| Parameter | Value | Unit | Notes |
|---|---|---|---|
| Dimensions | 40.7 × 19.7 × 42.9 | mm | Standard servo form factor |
| Weight | 55.0 | g | Bare motor with wire |
| Cable Length | 300 | mm | 3-wire ribbon cable |
| Gear Type | Brass & Aluminum Metal | — | Full metal gear set |
| Bearing | Dual Ball Bearings | — | Output shaft support |

## Control signal timing

The MG996R uses a **50 Hz PWM control signal** (20 ms period). The pulse width determines the output horn angle:

- **500 µs (0.5 ms):** Position $0^\circ$
- **1500 µs (1.5 ms):** Position $90^\circ$ (Neutral Center)
- **2400 µs (2.4 ms):** Position $180^\circ$

```
          ┌─┐                                         ┌─┐
          │ │ (0.5ms to 2.4ms)                        │ │
          │ │                                         │ │
     ─────┘ └─────────────────────────────────────────┘ └─────
     ◄─────────────────── 20 ms (50 Hz) ─────────────►
```

## Drive requirements & wiring

| Servo Connector | → | External Power Supply / MCU | Notes |
|---|---|---|---|
| Red (`VCC`) | | External 5 V to 6 V DC Supply (2A+ rated) | **Never power from MCU 5V pin** |
| Brown (`GND`) | | Common Ground (`GND`) | Connect power supply GND to MCU GND |
| Orange (`PWM`) | | Microcontroller PWM Pin | GPIO control pin (3.3V or 5V logic) |

> [!WARNING]
> High current demand hazard:
> - Stall current for a single MG996R can reach **2.5 A** at 6.0 V. Driving multiple MG996R servos simultaneously requires a dedicated high-current regulated power supply (e.g. 5V/6V 5A+ UBEC or switching power supply).
> - Attempting to power an MG996R directly from an Arduino 5V pin or USB port will cause immediate microcontroller resets, serial disconnects, or potential damage to onboard regulators.

## Common mistakes

- **Powering from MCU 5V rail:** The 1.4A+ running inrush current resets the microcontroller as soon as the motor starts moving.
- **Floating ground line:** Omitting the ground connection between the external servo power supply and the microcontroller leads to erratic motor jitter.
- **Forcing mechanical stops:** Driving pulse widths beyond the physical endstops ($<450\ \mu\text{s}$ or $>2450\ \mu\text{s}$) stalls the motor continuously, rapidly heating the internal MOSFETs and draining battery power.

## Notes

- **MG995 vs MG996R:** The MG996R was introduced specifically to fix the wide deadband, slow response, and positioning overshoot of the older MG995 model.
