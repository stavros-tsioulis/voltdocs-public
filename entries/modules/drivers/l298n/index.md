## Overview

The **L298N** is an integrated monolithic dual full-bridge driver designed to accept standard TTL logic levels and drive inductive loads such as relays, solenoids, DC motors, and bipolar stepper motors.

The breakout module features an onboard 78M05 5V linear voltage regulator (which can supply power to external control circuitry when the motor supply voltage is between 7 V and 12 V), heavy-duty heat sink, screw terminal blocks for motor/power connections, and flyback protection diodes.

## Quick reference

| | |
|---|---|
| **Motor supply voltage (`VMS` / `VS`)** | 5 V – 35 V (IC maximum 46 V) |
| **Logic supply voltage (`VSS`)** | 4.5 V – 7 V (5.0 V typical) |
| **Peak output current** | 2.0 A per bridge (total 4.0 A) |
| **Continuous output current** | 2.0 A per channel (requires heat sink) |
| **Channels** | 2 independent H-bridges |
| **Control inputs** | TTL Compatible (`IN1`, `IN2`, `ENA` and `IN3`, `IN4`, `ENB`) |

## Pinout

### Standard Red L298N Breakout Module

| Terminal / Pin | Name | Type | Description |
|---|---|---|---|
| Screw Block 1 | `VMS` / `12V` | Power Input | Motor Power Supply (5 V – 35 V) |
| Screw Block 2 | `GND` | Power | Common Ground (Must be shared with MCU ground) |
| Screw Block 3 | `5V` | Power I/O | +5 V Logic Power (Output if jumper enabled; Input if jumper removed) |
| Screw Block 4 | `OUT1`, `OUT2` | Power Output | Motor A output terminals |
| Screw Block 5 | `OUT3`, `OUT4` | Power Output | Motor B output terminals |
| Header Pin 1 | `ENA` | Digital Input | Enable Motor A (PWM input for speed control; jumpered to 5V for full speed) |
| Header Pin 2 | `IN1` | Digital Input | Motor A direction control pin 1 |
| Header Pin 3 | `IN2` | Digital Input | Motor A direction control pin 2 |
| Header Pin 4 | `IN3` | Digital Input | Motor B direction control pin 1 |
| Header Pin 5 | `IN4` | Digital Input | Motor B direction control pin 2 |
| Header Pin 6 | `ENB` | Digital Input | Enable Motor B (PWM input for speed control; jumpered to 5V for full speed) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Motor Supply Voltage | $V_S$ | 5 | 12 | 35 | V | Module max (IC max 46 V) |
| Logic Supply Voltage | $V_{SS}$ | 4.5 | 5.0 | 7.0 | V | TTL Logic |
| Output Current | $I_O$ | — | — | 2.0 | A | Non-repetitive $t = 100\text{ }\mu\text{s}$ |
| Low-Level Input Voltage | $V_{IL}$ | -0.3 | — | 1.5 | V | TTL Low |
| High-Level Input Voltage | $V_{IH}$ | 2.3 | — | $V_{SS}$ | V | TTL High |
| Total Power Dissipation | $P_{tot}$ | — | — | 25 | W | $T_{case} = 75\text{ }^\circ\text{C}$ with heat sink |
| Voltage Drop per Bridge | $V_{CE(sat)}$ | — | 2.0 | 3.2 | V | Total drop ($V_{CEsat(H)} + V_{CEsat(L)}$ @ $1\text{ A}$) |

## Control logic truth table

| `ENA` / `ENB` | `IN1` / `IN3` | `IN2` / `IN4` | Motor State |
|---|---|---|---|
| `LOW` | `X` | `X` | Motor Stopped (Freewheel / Off) |
| `HIGH` | `HIGH` | `LOW` | Forward Rotation |
| `HIGH` | `LOW` | `HIGH` | Reverse Rotation |
| `HIGH` | `HIGH` | `HIGH` | Fast Motor Brake |
| `HIGH` | `LOW` | `LOW` | Fast Motor Brake |

## Wiring

### Dual DC Motor Wiring (Arduino Uno)

| L298N Module | → | External / Arduino Uno | Description |
|---|---|---|---|
| `12V` | | External Battery (+7V to +12V) | Motor power supply |
| `GND` | | Battery (-) & Arduino `GND` | Common ground reference |
| `5V` | | Arduino `5V` | Regulated 5V output (when jumper ON) |
| `IN1` | | Arduino Pin `9` | Motor A Direction |
| `IN2` | | Arduino Pin `8` | Motor A Direction |
| `ENA` | | Arduino Pin `10` (PWM) | Motor A Speed Control |
| `IN3` | | Arduino Pin `7` | Motor B Direction |
| `IN4` | | Arduino Pin `6` | Motor B Direction |
| `ENB` | | Arduino Pin `5` (PWM) | Motor B Speed Control |

> [!WARNING]
> High Voltage Regulator Jumper Rules:
> - **Motor supply $\le 12\text{ V}$:** Keep the onboard 5V regulator jumper **ON**. The `5V` terminal outputs regulated 5V to power the MCU.
> - **Motor supply $> 12\text{ V}$:** You **MUST REMOVE** the onboard 5V regulator jumper to avoid overheating the 78M05 IC. Supply separate 5V logic power to the `5V` terminal.

## Common mistakes

- **Forgetting common ground:** If the microcontroller ground is not connected to the L298N `GND` terminal, logic control signals (`IN1`–`IN4`) will have no reference point and motor operation will be erratic or unresponsive.
- **Underestimating internal voltage drop:** The internal bipolar Darlington transistors drop approximately $1.8\text{ V}$ to $3.2\text{ V}$ across the output. Sourcing a 6V motor from a 6V supply will only deliver $\sim 3.5\text{ V}$ to the motor terminals.
- **Overheating 5V regulator:** Leaving the 5V jumper ON when driving motors with 24V or 36V supplies will burn out the onboard 78M05 regulator due to high thermal dissipation ($(V_{in} - 5) \times I$).

## Notes

- **Flyback Protection:** Standard red L298N breakout modules include 8 onboard 1N4007 flyback diodes to clamp inductive voltage spikes generated when switching motor coils.
