## Overview

The **SG90** is a ubiquitous 9-gram analog micro servo motor manufactured by TowerPro. It features nylon plastic gears, an internal DC coreless motor, a feedback potentiometer, and control electronics inside a compact translucent plastic enclosure.

It is widely bundled in beginner robotics kits and hobby projects for controlling robot arms, camera gimbals, steering mechanisms, and micro actuators using a standard 50 Hz Pulse-Width Modulation (PWM) signal.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 4.8 V to 6.0 V DC (5 V nominal) |
| **Stall torque** | $1.8\text{ kg}\cdot\text{cm}$ (at 4.8 V) |
| **Operating speed** | 0.12 s / 60° (at 4.8 V) |
| **Rotation range** | ~180° total travel |
| **Control signal** | PWM (50 Hz / 20 ms frame period) |
| **Pulse width range** | 500 µs (0°) to 2400 µs (180°) |
| **Weight** | 9 g |

## Terminals & cable wiring

The SG90 servo terminates in a 3-pin 0.1" (2.54 mm) female JR/Futaba connector cable:

| Pin | Cable Color | Signal | Description |
|---|---|---|---|
| 1 | Brown / Black | `GND` | Ground (0 V) |
| 2 | Red | `VCC` | Power supply (+4.8 V to +6.0 V) |
| 3 | Orange / Yellow | `PWM` | Position control signal (50 Hz PWM) |

## Electrical & mechanical specifications

### Electrical Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Operating Voltage | $V_{CC}$ | 4.8 | 5.0 | 6.0 | V | DC |
| Idle Current | $I_{idle}$ | — | 5 | 10 | mA | $V_{CC} = 5.0\text{ V}$, static position |
| Running Current | $I_{run}$ | 100 | 220 | 350 | mA | $V_{CC} = 5.0\text{ V}$, moving under light load |
| Stall Current | $I_{stall}$ | 500 | 650 | 800 | mA | $V_{CC} = 5.0\text{ V}$, shaft locked |
| Dead Band Width | $t_{db}$ | — | 7 | 10 | µs | PWM pulse resolution limit |

### Mechanical Specifications

| Parameter | Value | Unit | Notes |
|---|---|---|---|
| Dimensions | 23.0 × 12.2 × 29.0 | mm | $L \times W \times H$ excluding mounting tabs |
| Weight | 9.0 | g | Bare servo |
| Cable Length | ~250 | mm | 3-wire ribbon cable |
| Gear Type | Nylon Plastic | — | POM gear set |
| Bearing | Bushing | — | Plastic shaft sleeve |

## Control signal timing

The SG90 is controlled by sending a **50 Hz PWM signal** (20 ms period). The duration of the positive pulse determines the target shaft position:

- **500 µs (0.5 ms pulse):** Neutral position $0^\circ$
- **1500 µs (1.5 ms pulse):** Center position $90^\circ$
- **2400 µs (2.4 ms pulse):** Maximum position $180^\circ$

```
          ┌─┐                                         ┌─┐
          │ │ (0.5ms to 2.4ms)                        │ │
          │ │                                         │ │
     ─────┘ └─────────────────────────────────────────┘ └─────
     ◄─────────────────── 20 ms (50 Hz) ─────────────►
```

## Drive requirements & wiring

| SG90 Connector | → | Power Supply / MCU | Notes |
|---|---|---|---|
| Red (`VCC`) | | External 5 V Power Supply | **Do NOT power from MCU GPIO or 3.3V pin** |
| Brown (`GND`) | | Common Ground (`GND`) | Must connect external supply GND to MCU GND |
| Orange (`PWM`) | | Microcontroller PWM Pin | GPIO pin output (e.g. Arduino D9, ESP32 GPIO18) |

> [!WARNING]
> Stall Current Power Spike Hazard:
> - Driving an SG90 directly from an Arduino 5V pin or 3.3V rail can draw over **650 mA** during motor movement or stall. This causes voltage brownouts, resetting the MCU.
> - Always power servos from an **external 5 V DC power supply** capable of supplying at least 1 A per servo, with a shared ground line to the microcontroller.

## Common mistakes

- **Powering from MCU 5V rail:** Under load, sudden motor current spikes drop the supply rail, causing random MCU resets and corrupted serial communication.
- **Forgetting common ground:** Connecting servo `VCC` to an external battery without connecting external `GND` to microcontroller `GND` results in erratic jitter.
- **Driving past mechanical end-stops:** Sending pulse widths below 450 µs or above 2450 µs forces the internal potentiometer into mechanical hard stops, stripping the delicate nylon gears.

## Notes

- For higher torque or heavy mechanical loads, consider metal-gear upgrades such as the **MG90S** (pin-compatible drop-in replacement).
