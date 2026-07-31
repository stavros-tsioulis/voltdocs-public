## Overview

The **28BYJ-48** is an inexpensive, 5V DC 4-phase 5-wire unipolar geared stepper motor. It features an internal reduction gear train that trades rotation speed for high positioning torque, making it a staple motor in DIY robotics, automated blinds, and optical pan mechanisms.

Because microcontrollers cannot drive the motor coils directly, the 28BYJ-48 is almost always bundled with a **ULN2003** Darlington Transistor Array driver board. The driver board accepts 4 digital GPIO signals from a microcontroller, amplifies the current up to 500 mA per channel, and includes 4 status LEDs (`A`, `B`, `C`, `D`) to visualize active phase excitation.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 5.0 V DC (12V variants also exist) |
| **Motor type** | 4-Phase, 5-Wire Unipolar Stepper Motor |
| **Gear reduction ratio** | $1 : 64$ ($63.6839 : 1$ exact ratio) |
| **Steps per revolution (Full-step)** | 2048 steps ($0.176^\circ$ per step) |
| **Steps per revolution (Half-step)** | 4096 steps ($0.088^\circ$ per step) |
| **Coil DC resistance** | $50\ \Omega \pm 7\%$ per phase at $25^\circ\text{C}$ |
| **Pull-in torque** | $> 34.3\text{ mN}\cdot\text{m}$ ($> 350\text{ g}\cdot\text{cm}$) at 120 Hz |

## Pinout

### ULN2003 Driver Board Terminals

| Pin / Connector | Name | Type | Description |
|---|---|---|---|
| `IN1` | Phase A | Digital Input | Control input for Coil 1 (Blue wire) |
| `IN2` | Phase B | Digital Input | Control input for Coil 2 (Pink wire) |
| `IN3` | Phase C | Digital Input | Control input for Coil 3 (Yellow wire) |
| `IN4` | Phase D | Digital Input | Control input for Coil 4 (Orange wire) |
| `GND` | Ground | Power | Power Ground (0 V) |
| `5V-12V` | `VCC` | Power | Motor Supply Power (+5 V DC) |
| Jumper | On/Off | Jumper | Onboard power jumper to enable ULN2003 VCC rail |

### 5-Pin JST-XH Motor Connector Wire Map

| Wire Color | Terminal | Description |
|---|---|---|
| Red | Common (`VCC`) | Center-tap positive supply connected to +5 V |
| Blue | Coil 1 (`IN1`) | Phase A coil end |
| Pink | Coil 2 (`IN2`) | Phase B coil end |
| Yellow | Coil 3 (`IN3`) | Phase C coil end |
| Orange | Coil 4 (`IN4`) | Phase D coil end |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | `VCC` | 4.75 | 5.0 | 5.25 | V | Recommended motor voltage |
| Operating Current (1 phase ON) | `I1PH` | — | 100 | 120 | mA | $5.0\text{ V} / 50\ \Omega$ |
| Operating Current (2 phases ON) | `I2PH` | — | 200 | 240 | mA | Half-stepping peak current |
| Insulated Resistance | `RINS` | 10 | — | — | MΩ | 500V DC |
| Maximum Starting Frequency | `fSTART` | 500 | — | — | Hz | No load (Pull-in) |
| Maximum Operating Frequency | `fMAX` | 1000 | — | — | Hz | No load (Pull-out) |

## Phase excitation sequences

To rotate the motor shaft, activate the input pins `IN1`–`IN4` in sequence.

### Half-Stepping Sequence (8 Steps — Recommended for smooth movement)

| Step | IN1 (Blue) | IN2 (Pink) | IN3 (Yellow) | IN4 (Orange) |
|---|---|---|---|---|
| 1 | **HIGH** | LOW | LOW | LOW |
| 2 | **HIGH** | **HIGH** | LOW | LOW |
| 3 | LOW | **HIGH** | LOW | LOW |
| 4 | LOW | **HIGH** | **HIGH** | LOW |
| 5 | LOW | LOW | **HIGH** | LOW |
| 6 | LOW | LOW | **HIGH** | **HIGH** |
| 7 | LOW | LOW | LOW | **HIGH** |
| 8 | **HIGH** | LOW | LOW | **HIGH** |

## Wiring

| ULN2003 Board Pin | → | Arduino Uno Pin | External Power Supply |
|---|---|---|---|
| `IN1` | | Pin `8` | — |
| `IN2` | | Pin `9` | — |
| `IN3` | | Pin `10` | — |
| `IN4` | | Pin `11` | — |
| `GND` | | `GND` (Common) | Power Supply Ground |
| `5V-12V` | | — | Power Supply `+5V` (1A rating) |

## Common mistakes

- **Powering motor directly from Arduino 5V pin:** The motor draws 200–240 mA when half-stepping. Powering it from an Arduino's internal regulator or USB 5V rail can cause voltage dips and resets. Use an external 5V power supply.
- **Excessive stepping frequency:** The 28BYJ-48 cannot step faster than ~1000 Hz (approx 12–15 RPM output shaft speed) due to internal mechanical gear friction. Sending step pulses faster than 15 RPM causes the motor to vibrate and lose steps without rotating.
- **Leaving coils powered while stationary:** Unlike DC motors, stepper motors hold position by maintaining current through active coils. If your application does not require holding torque when stopped, write all 4 GPIO inputs `LOW` to prevent motor heating and battery drain.

## Notes

- **Exact Gear Ratio:** While advertised as 64:1, the actual gear train ratio inside the 28BYJ-48 is $\frac{32}{9} \times \frac{22}{11} \times \frac{26}{9} \times \frac{31}{10} = \frac{2584}{41} \approx 63.68395:1$.
