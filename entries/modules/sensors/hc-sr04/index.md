## Overview

The **HC-SR04** is an ultrasonic distance ranging module. It provides 2 cm to 400 cm non-contact measurement capability with a ranging accuracy of up to 3 mm.

The module includes an ultrasonic transmitter transducer, a receiver transducer, and control circuitry. Sending a 10 µs pulse to the `Trig` pin causes the module to emit an 8-cycle burst of 40 kHz ultrasound and set the `Echo` pin HIGH. The duration of the `Echo` HIGH pulse is directly proportional to the time taken for the ultrasonic wave to travel to the target and reflect back.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 4.5 V to 5.5 V DC (5 V nominal) |
| **Operating current** | 15 mA active, $< 2\text{ mA}$ quiescent |
| **Ultrasonic frequency** | 40 kHz |
| **Ranging distance** | 2 cm to 400 cm (0.8 in to 157 in) |
| **Ranging accuracy** | 3 mm |
| **Measuring angle** | $< 15^\circ$ effective cone angle |
| **Trigger input signal** | 10 µs TTL pulse (`Trig`) |
| **Echo output signal** | 5V TTL pulse duration proportional to distance (`Echo`) |

## Pinout

### Standard 4-Pin Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+5.0 V DC) |
| 2 | `Trig` | Digital Input | Trigger input pin (Apply $\ge 10\text{ }\mu\text{s}$ HIGH pulse to start measurement) |
| 3 | `Echo` | Digital Output | Echo output pin (5V TTL HIGH pulse width = round-trip time) |
| 4 | `GND` | Power | Ground (0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 4.5 | 5.0 | 5.5 | V | DC |
| Active Supply Current | $I_{CC}$ | 10 | 15 | 20 | mA | During measurement |
| Quiescent Current | $I_{Q}$ | — | 2 | 3 | mA | Idle |
| Ranging Distance | $d$ | 2 | — | 400 | cm | |
| Measuring Angle | $\theta$ | — | 15 | 30 | ° | Target surface dependent |
| Trigger Pulse Width | $t_{trig}$ | 10 | — | — | µs | Minimum TTL pulse |
| Echo Pulse Width | $t_{echo}$ | 150 | — | 25000 | µs | $150\text{ }\mu\text{s} \approx 2.5\text{ cm}$, $25\text{ ms} \approx 4\text{ m}$ |
| Timeout Period | $t_{timeout}$ | — | 38 | — | ms | Out-of-range / no echo (~6.5 m equivalent) |

## Communication & Distance Calculation

1. Microcontroller holds `Trig` pin **HIGH for at least 10 µs**.
2. HC-SR04 automatically sends eight 40 kHz sound pulses and sets `Echo` HIGH.
3. Microcontroller measures the duration $t_{echo}$ (in microseconds) that `Echo` remains HIGH.
4. Calculate distance using the speed of sound in air ($v_{sound} \approx 343\text{ m/s} = 0.0343\text{ cm/}\mu\text{s}$ at $20^\circ\text{C}$):

$$\text{Distance (cm)} = \frac{t_{echo} \times 0.0343}{2} = \frac{t_{echo}}{58}$$

$$\text{Distance (inches)} = \frac{t_{echo}}{148}$$

```
Trig: ────┌─ 10µs ─┐──────────────────────────────────────────────────
          │        │
Echo: ────┴────────┴───┌─────────────── t_echo ───────────────┐────────
                       │                                       │
Sound:                 ░▒▓ 8x 40kHz Bursts ...                 │
```

## Wiring

| HC-SR04 Pin | → | Microcontroller (Arduino Uno / ESP32) | Notes |
|---|---|---|---|
| `VCC` | | `5V` | Must be 5V DC (3.3V will cause range reduction or failure) |
| `Trig` | | Digital Output Pin (e.g. GPIO5) | 5V TTL input (3.3V GPIO is generally accepted) |
| `Echo` | | Digital Input Pin (e.g. GPIO18 via Level Shifter) | **Outputs 5V TTL! Use resistor voltage divider for 3.3V MCUs** |
| `GND` | | `GND` | Ground |

> [!WARNING]
> 5V Echo Output Level Hazard:
> The `Echo` pin outputs a 5V TTL pulse. Connecting `Echo` directly to a 3.3V-only microcontroller pin (ESP32, ESP8266, Raspberry Pi) can damage the GPIO. Use a **voltage divider** (e.g. $1\text{ k}\Omega$ and $2\text{ k}\Omega$ resistors) to step down 5V to 3.3V.

## Common mistakes

- **Directly connecting 5V Echo to 3.3V GPIO pins:** Connecting `Echo` directly to an ESP32 or Raspberry Pi without a voltage divider or level shifter risks damaging the GPIO pin.
- **Powering from 3.3V:** Standard HC-SR04 modules require 5.0 V DC. Powering at 3.3V causes erratic ranging or limits maximum range to $<50\text{ cm}$. (Use 3.3V-compatible variants like **RCWL-1601** or **HC-SR04P** for native 3.3V systems).
- **Triggering too fast (< 60 ms intervals):** Triggering faster than 60 ms can cause ultrasonic echoes from previous pulses to interfere with the current measurement.
- **Soft / Angled target surfaces:** Sound waves reflect away from hard surfaces angled $>15^\circ$ or get absorbed by soft materials (fabrics, sponges), causing fake out-of-range timeouts.

## Notes

- Speed of sound varies with ambient temperature: $v_{sound} = 331.3 + 0.606 \times T\text{ }(^\circ\text{C})\text{ m/s}$. Compensation can be added in software using a temperature sensor.
