## Overview

The **SG90** is a ubiquitous 9-gram analog micro servo motor original designed by TowerPro and manufactured by numerous generic vendors. It combines a small DC coreless motor, plastic reduction gearbox, potentiometer feedback, and control electronics into a compact 9g translucent plastic casing.

Controlled via a standard 50 Hz Pulse Width Modulation (PWM) signal, the SG90 rotates its output shaft to a target angular position from 0° to 180°. It is bundled in almost every beginner Arduino and Raspberry Pi starter kit for driving robotic arms, pan-tilt camera mounts, and steering linkages.

## Quick reference

| | |
|---|---|
| **Operating voltage** | 4.8 V – 6.0 V (5.0 V nominal) |
| **Stall torque** | 1.8 kg·cm (25 oz-in) at 4.8 V |
| **Operating speed** | 0.12 s / 60° (4.8 V) $\rightarrow$ ~500°/s |
| **Rotation range** | 180° (0° to 180°) |
| **Control Signal** | 50 Hz PWM (20 ms period, 1.0 ms to 2.0 ms high pulse width) |
| **Weight / Dimensions** | 9 g (0.32 oz) / $22.2 \times 11.8 \times 31.0\text{ mm}$ |

## Terminals & contacts

### Standard 3-Pin JR / Futaba Female Cable

| Lead Color | Name | Type | Description |
|---|---|---|---|
| Brown / Black | `GND` | Power | Ground (0 V) |
| Red | `VCC` / `5V` | Power | Servo Motor Supply Voltage (+4.8 V to +6.0 V) |
| Orange / Yellow | `PWM` / `SIG` | Digital Input | Control Signal Input pin (3.3V or 5V logic compatible) |

## Electrical specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Operating Voltage | `VCC` | 4.8 | 5.0 | 6.0 | V | DC supply |
| Idle Current | `IIDLE` | — | 5 | 10 | mA | Stopped at target position |
| Running Current | `IRUN` | — | 150 | 200 | mA | No-load continuous movement |
| Stall Current | `ISTALL` | — | 650 | 800 | mA | Motor shaft locked at 5 V |
| Dead Band Width | `tDB` | — | 10 | 15 | µs | Position control tolerance |

## Mechanical specifications

| Parameter | Value | Unit | Notes |
|---|---|---|---|
| Weight | 9 | g | Casing + motor (excluding connector wire) |
| Dimensions | $22.2 \times 11.8 \times 31.0$ | mm | Excluding mounting ears and horn shaft |
| Gear Type | Nylon Plastic | — | 5-stage reduction gear train |
| Horn Connector | 21-tooth spline | — | Supplied with single, double, and cross arms |
| Cable Length | 250 | mm | 3-wire ribbon cable with 2.54mm pitch header |

## Drive requirements & control timing

> [!WARNING]
> Do NOT power the SG90 servo motor directly from a microcontroller's 5V pin when driving multiple servos or moving heavy loads. Peak stall currents of 650+ mA per motor can cause MCU power rails to drop, triggering Brown-Out Resets (BOR). Use an external 5V 2A power supply with shared GND.

### PWM Pulse Protocol (50 Hz / 20 ms Period)

The angular position of the output horn is determined by the duration of a positive high pulse sent every 20 milliseconds (50 Hz):

- **0° Position:** 1.0 ms pulse width (5% duty cycle)
- **90° (Center) Position:** 1.5 ms pulse width (7.5% duty cycle)
- **180° Position:** 2.0 ms pulse width (10% duty cycle)

```
       1.0 ms - 2.0 ms
       +---+
       |   |
+------+   +-----------------------+  (Period = 20 ms / 50 Hz)
```

> [!NOTE]
> Cheap clone SG90 motors may require pulse width ranges extended slightly to ~0.5 ms (0°) up to ~2.4 ms (180°) to reach their full mechanical stops.

## Wiring

| SG90 Lead | :i-lucide-move-right: | External 5V Power Supply | Microcontroller |
|---|---|---|---|
| Brown / Black (`GND`) | | `GND` | `GND` (Common Ground) |
| Red (`VCC`) | | `+5V Output` | — |
| Orange (`SIG`) | | — | PWM Pin (e.g. Pin `9` on Arduino) |

## Common mistakes

- **Omission of common ground:** Connecting the servo power supply to external 5V without tying the external `GND` to the microcontroller `GND` causes erratic jitter and uncontrolled movement.
- **Forcing horn beyond mechanical stops:** Overdriving the PWM pulse width beyond the motor's physical limit (> 180°) forces the gears against hard plastic stops, drawing stall current (~800 mA) and stripping nylon gear teeth.
- **Driving with high-frequency PWM:** Standard digital PWM pins configured for default >490 Hz rates (e.g. Arduino `analogWrite`) will damage the servo amplifier board. Always use specialized hardware servo libraries (`Servo.h`, ESP32 `MCPWM`) set strictly to 50 Hz.

## Notes

- **MG90S Upgrade:** For applications requiring higher torque (~2.2 kg·cm) and indestructible metal gears, the **MG90S** is a drop-in size-compatible replacement for the SG90.
