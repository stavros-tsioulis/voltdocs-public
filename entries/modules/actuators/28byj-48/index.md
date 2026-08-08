## Overview

The **28BYJ-48** is a 5V DC 4-phase 5-wire unipolar geared stepper motor. It is almost universally paired with a **ULN2003 Darlington Transistor Array** driver breakout board in beginner electronics, Arduino, and Raspberry Pi starter kits.

The motor incorporates an internal 1/64 gear reduction gearbox that produces high torque ($>300\text{ g}\cdot\text{cm}$) at slow rotational speeds. The ULN2003 driver board accepts 3.3V or 5V logic inputs (`IN1`–`IN4`) to energize the motor coils and includes 4 status LEDs to visualize stepping sequences.

## Quick reference

| | |
|---|---|
| **Motor operating voltage** | 5.0 V DC (nominal) |
| **Coil resistance** | $50\text{ }\Omega \pm 7\%$ per phase |
| **Internal step angle** | 5.625° / 64 = 0.08789° per output shaft step |
| **Gearbox reduction ratio** | 1:64 (exact ratio: $\frac{64}{1}$ or $63.6839:1$) |
| **Steps per full revolution** | 2048 steps (full-step) / 4096 steps (half-step) |
| **Pull-in torque** | $> 300\text{ g}\cdot\text{cm}$ (at 100 Hz frequency) |
| **Driver IC** | ULN2003A (7-channel Darlington transistor array) |
| **Driver input logic** | 3.3 V to 5.0 V TTL/CMOS Compatible |

## Terminals & cable pinout

### Motor 5-Pin JST Connector (Plugs into ULN2003 board)

| Pin | Wire Color | Coil Connection | Description |
|---|---|---|---|
| 1 | Blue | Coil 1 (Phase A) | Driven by ULN2003 `OUT1` |
| 2 | Pink | Coil 2 (Phase B) | Driven by ULN2003 `OUT2` |
| 3 | Yellow | Coil 3 (Phase C) | Driven by ULN2003 `OUT3` |
| 4 | Orange | Coil 4 (Phase D) | Driven by ULN2003 `OUT4` |
| 5 | Red | Common Positive (`COM`) | Connects to +5V power supply rail |

### ULN2003 Driver Board Pins

| Pin | Name | Type | Description |
|---|---|---|---|
| 1–4 | `IN1` – `IN4` | Digital Input | Logic inputs from microcontroller (Active-HIGH) |
| 5 | `GND` | Power | Common Ground (0 V) |
| 6 | `VCC` / `+` | Power | Motor power supply (+5 V to +12 V DC) |
| Jumper | `ON/OFF` | Power Jumper | Enables power to the ULN2003 chip and indicator LEDs |

## Electrical & mechanical specifications

### Electrical Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Operating Voltage | $V_{CC}$ | 4.5 | 5.0 | 5.5 | V | DC |
| Phase Current | $I_{phase}$ | — | 160 | 240 | mA | 2 coils energized simultaneously |
| Coil Resistance | $R_{phase}$ | 46.5 | 50.0 | 53.5 | Ω | At $25^\circ\text{C}$ |
| Insulated Resistance | $R_{ins}$ | 10 | — | — | MΩ | 500 V DC |
| Max Pull-in Frequency | $f_{pull}$ | 500 | — | — | Hz | No load |
| Max No-load Frequency | $f_{free}$ | 900 | — | — | Hz | No load |

### Mechanical Specifications

| Parameter | Value | Unit | Notes |
|---|---|---|---|
| Motor Diameter | 28.0 | mm | Cylindrical housing |
| Output Shaft Diameter | 5.0 | mm | D-shaft (flatted) |
| Gear Reduction | 1:64 | — | Internal spur gear train |
| Noise Level | $< 35$ | dB | At 120 Hz operating frequency |
| Temperature Rise | $< 40$ | K | At 120 Hz, 5V DC supply |

## Stepping sequences

### 4-Step Sequence (Full-Step / High Torque)

| Step | `IN1` | `IN2` | `IN3` | `IN4` |
|---|---|---|---|---|
| 1 | **HIGH** | **HIGH** | LOW | LOW |
| 2 | LOW | **HIGH** | **HIGH** | LOW |
| 3 | LOW | LOW | **HIGH** | **HIGH** |
| 4 | **HIGH** | LOW | LOW | **HIGH** |

### 8-Step Sequence (Half-Step / Smooth Motion — 4096 steps/rev)

| Step | `IN1` | `IN2` | `IN3` | `IN4` |
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

| ULN2003 Driver Board | → | Microcontroller / Power Supply | Notes |
|---|---|---|---|
| `IN1` | | Digital Pin `8` (GPIO output) | Phase A control |
| `IN2` | | Digital Pin `9` (GPIO output) | Phase B control |
| `IN3` | | Digital Pin `10` (GPIO output) | Phase C control |
| `IN4` | | Digital Pin `11` (GPIO output) | Phase D control |
| `GND` | | Common Ground (`GND`) | Connect to MCU GND and Power Supply GND |
| `VCC` / `+` | | External `+5V` Power Supply | Power supply (do not use Arduino 5V pin) |

> [!WARNING]
> Inductive Spike & Thermal Warning:
> - ULN2003 inputs are active HIGH: driving an input HIGH turns ON the internal Darlington transistor, pulling the corresponding motor coil pin to Ground.
> - De-energize all coils (`IN1`–`IN4` = LOW) when the motor is stopped to prevent continuous current draw ($240\text{ mA}$) and overheating.

## Common mistakes

- **Powering motor directly from microcontroller 5V rail:** Energizing 2 coils draws up to 240 mA, which causes supply voltage droop and resets the microcontroller.
- **Leaving coils energized when stopped:** Unlike bipolar stepper drivers with automatic current reduction, keeping inputs HIGH when idle wastes power and heats up the motor.
- **Stepping too fast at startup:** Attempting to start stepping at frequencies above 500 Hz without a frequency acceleration ramp will cause the motor to hum and stall without rotating.

## Notes

- Exact gear ratio is $\frac{3125}{49} \approx 63.6839:1$. For precise $360^\circ$ rotation without cumulative positional drift over long periods, use $4075.7728$ steps per revolution in half-step mode.
