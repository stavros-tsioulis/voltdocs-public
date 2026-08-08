## Overview

The **ULN2003A** (and 16-pin DIP **ULN2003**) is a 7-channel NPN Darlington transistor array IC manufactured by Texas Instruments, STMicroelectronics, and ON Semiconductor. Ubiquitously included in Arduino and Raspberry Pi starter kits (often pre-assembled on a small breakout board with 4 LED indicator lights to drive 5V 28BYJ-48 unipolar stepper motors), it acts as a high-current low-side switch driver for relays, solenoids, DC motors, and high-voltage displays.

Capable of sinking up to **$500\text{ mA}$ per channel** ($600\text{ mA}$ peak) at up to **$50\text{V}$ DC**, the ULN2003A integrates $2.7\ \text{k}\Omega$ series base resistors on each input channel (enabling direct 5V TTL and 3.3V CMOS microcontroller connection) alongside **common free-wheeling flyback clamp diodes** on pin 9 (`COM`).

## Quick reference

| | |
|---|---|
| **Driver Architecture** | 7 Independent NPN Darlington Transistor Pairs |
| **Package** | 16-Pin DIP / SOIC-16 / 28BYJ-48 Stepper Driver PCB |
| **Output Breakdown Voltage ($V_{CE}$)**| $50\text{ V}$ max |
| **Continuous Collector Current ($I_C$)**| $500\text{ mA}$ per channel (Parallelable for higher current) |
| **Input Base Resistor** | $2.7\ \text{k}\Omega$ internal series resistor (5V TTL/CMOS direct drive) |
| **Integrated Flyback Protection** | 7 Common-cathode clamp diodes connected to Pin 9 (`COM`) |
| **Output Saturation Voltage ($V_{CE(sat)}$)**| $1.1\text{ V}$ typical at $I_C = 200\text{ mA}, I_B = 350\ \mu\text{A}$ |

## Pinout (DIP-16 Package)

```
             ┌───┴───┐
        IN 1 ─┤ 1  16 ├─ OUT 1
        IN 2 ─┤ 2  15 ├─ OUT 2
        IN 3 ─┤ 3  14 ├─ OUT 3
        IN 4 ─┤ 4  13 ├─ OUT 4
        IN 5 ─┤ 5  12 ├─ OUT 5
        IN 6 ─┤ 6  11 ├─ OUT 6
        IN 7 ─┤ 7  10 ├─ OUT 7
         GND ─┤ 8   9 ├─ COM (Common Flyback Diode Catch)
             └───────┘
```

| Pin | Name | Description |
|---|---|---|
| 1–7 | `IN 1` – `IN 7` | Channel 1–7 input control pins (High = ON, Low = OFF) |
| 8 | `GND` | Common ground reference (0 V) |
| 9 | `COM` | Common cathode clamp diode connection (Connect to $+V_{LOAD}$) |
| 10–16 | `OUT 7` – `OUT 1` | Open-collector output channels (Low-side switch to GND) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Voltage | $V_{CE}$ | — | — | 50 | V | $I_C = 500\text{mA}$ |
| Input Voltage | $V_I$ | — | 5.0 | 30 | V | DC input |
| Continuous Collector Current| $I_C$ | — | — | 500 | mA | Single channel active |
| Peak Collector Current | $I_{CP}$ | — | — | 600 | mA | Short duty cycle pulse |
| Clamp Diode Reverse Volts| $V_R$ | — | — | 50 | V | Common catch diode |
| Clamp Diode Forward Current| $I_F$ | — | — | 500 | mA | Single diode forward |

## Internal Channel Schematics & Inductive Clamp Logic

Each of the 7 channels consists of a two-stage NPN Darlington pair:

```
  IN (Pin 1) ─── [2.7kΩ] ───┬─── [Collector Base] ─── Open-Collector OUT (Pin 16)
                             │                                 │
                            [NPN 1]                            │
                             │                            [10kΩ Resistor]
                             ├─── [Base NPN 2]                 │
                             │                                 │
                            [NPN 2] ───────────────────────────┴─── [COM Pin 9 Flyback Catch]
                             │
                            GND (Pin 8)
```

## Wiring (28BYJ-48 Stepper Motor Driver Board)

| ULN2003 Module Pin | → | Arduino / MCU | Motor / Load | Notes |
|---|---|---|---|---|
| `IN1` | | Digital D8 | | Drive Phase A |
| `IN2` | | Digital D9 | | Drive Phase B |
| `IN3` | | Digital D10 | | Drive Phase C |
| `IN4` | | Digital D11 | | Drive Phase D |
| `GND` | | GND | GND | System ground |
| `VCC` / `+` | | 5V / 12V DC | 5V 28BYJ-48 Motor | Power rail (also powers `COM` pin 9) |

## Example (Arduino Stepper Library Code)

```cpp
#include <Stepper.h>

// 2048 steps per revolution for 28BYJ-48 5V stepper
const int stepsPerRevolution = 2048;

// Initialize Stepper library on pins 8, 10, 9, 11 (Note 10 and 9 sequence)
Stepper myStepper(stepsPerRevolution, 8, 10, 9, 11);

void setup() {
  myStepper.setSpeed(10); // 10 RPM
  Serial.begin(9600);
  Serial.println("28BYJ-48 Stepper Motor Test with ULN2003");
}

void loop() {
  Serial.println("Clockwise rotation...");
  myStepper.step(stepsPerRevolution);
  delay(1000);

  Serial.println("Counter-clockwise rotation...");
  myStepper.step(-stepsPerRevolution);
  delay(1000);
}
```

## Common mistakes

- **Forgetting to connect Pin 9 (`COM`) to $+V_{LOAD}$ when driving relays/solenoids:** Pin 9 connects the internal flyback diodes across output channels. Leaving Pin 9 floating allows inductive back-EMF spikes to destroy the output Darlington transistors.
- **Exceeding total IC dissipation limit:** While each individual channel can sink $500\text{ mA}$, driving all 7 channels simultaneously at 500mA exceeds the $1.5\text{W}$ total DIP-16 package dissipation limit. Limit continuous total current to $\le 1.5\text{A}$ across all active channels.

## Notes

- **ULN2003A vs ULN2803A vs L293D:** ULN2003A has 7 channels (5V TTL compatible); ULN2803A has 8 channels; L293D has 4 half-H-bridge push-pull outputs for bi-directional motor control.
