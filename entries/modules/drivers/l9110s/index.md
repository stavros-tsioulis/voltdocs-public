## Overview

The **L9110S** (and DIP-8 variant **L9110**) is a two-channel push-pull power amplifier IC designed for controlling small DC motors and 2-phase 4-wire stepper motors. Operating over a wide voltage range of **2.5V to 12.0V DC**, each channel contains a full CMOS H-bridge capable of delivering up to **800mA continuous current** (up to 1.5A peak).

Most commonly sold as a low-cost $29\text{ mm} \times 23\text{ mm}$ dual-motor driver breakout PCB equipped with two 8-pin L9110S SOP-8 ICs and screw terminals, it is a favorite for budget 2WD and 4WD Arduino robot car projects, smart toys, and low-voltage actuators.

## Quick reference

| | |
|---|---|
| **Motor Supply Voltage (`VCC`)** | 2.5 V to 12.0 V DC |
| **Continuous Output Current** | $800\text{ mA}$ ($0.8\text{A}$) per channel |
| **Peak Output Current** | $1.5\text{ A}$ per channel |
| **Quiescent Supply Current** | $2.0\ \mu\text{A}$ typical |
| **Inputs** | 3.3V & 5V TTL/CMOS Compatible |
| **Channels** | 2 Independent H-Bridges (Motor A & Motor B) |
| **Package** | SOP-8 IC / Breakout Module with Screw Terminals |

## Pinout & Module Terminals

### SOP-8 Package IC (Single Channel H-Bridge)

```
         ┌───┴───┐
     OA 1│ 1   8 │ NC
    VCC 2│       │ 7 IA
     OB 3│L9110S │ 6 IB
    GND 4│       │ 5 NC
         └───────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `OA` | Output Terminal A (Connect to Motor lead 1) |
| 2 | `VCC` | Power Supply Input (+2.5V to +12V DC) |
| 3 | `OB` | Output Terminal B (Connect to Motor lead 2) |
| 4 | `GND` | Ground Reference (0 V) |
| 5, 8 | `NC` | Not Connected |
| 6 | `IB` | Control Logic Input B |
| 7 | `IA` | Control Logic Input A |

### Breakout Module Header Terminals

| Terminal | Function | Description |
|---|---|---|
| `VCC` | Power | Supply Voltage (+2.5V to +12V DC) |
| `GND` | Power | Common Ground (0 V) |
| `A-IA` | Input | Motor A Direction / Speed Control Input A |
| `A-IB` | Input | Motor A Direction / Speed Control Input B |
| `B-IA` | Input | Motor B Direction / Speed Control Input A |
| `B-IB` | Input | Motor B Direction / Speed Control Input B |
| `MOTOR A` | Output Screw Terminal | Output to DC Motor A |
| `MOTOR B` | Output Screw Terminal | Output to DC Motor B |

## Control Truth Table (Per Channel)

| IA Input | IB Input | Output OA | Output OB | Motor State |
|---|---|---|---|---|
| Low ($L$) | Low ($L$) | Low ($L$) | Low ($L$) | Off / Fast Brake |
| High ($H$) | Low ($L$) | High ($H$) | Low ($L$) | Forward |
| Low ($L$) | High ($H$) | Low ($L$) | High ($H$) | Reverse |
| High ($H$) | High ($H$) | High ($H$) | High ($H$) | Off / Fast Brake |

*PWM speed control is achieved by applying a PWM signal to one input pin while holding the other input LOW.*

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.5 | — | 12.0 | V | DC |
| Continuous Output Current | $I_{OUT}$ | — | — | 800 | mA | Single channel |
| Peak Output Current | $I_{PEAK}$ | — | 1.5 | — | A | Short duration |
| High Logic Input Voltage | $V_{IH}$ | 2.2 | — | $V_{CC}$ | V | TTL / CMOS compatible |
| Low Logic Input Voltage | $V_{IL}$ | 0 | — | 0.7 | V | TTL / CMOS compatible |
| Output Voltage High Drop | $V_{OH}$ | — | 0.2 | 0.5 | V | $I_{OUT} = 200\text{mA}$ |
| Output Voltage Low Drop | $V_{OL}$ | — | 0.1 | 0.3 | V | $I_{OUT} = 200\text{mA}$ |

## Wiring (Breakout Module to Arduino)

| L9110S Module Pin | → | Arduino / MCU | Notes |
|---|---|---|---|
| `VCC` | | 5V - 9V DC Battery | Motor power supply |
| `GND` | | GND | Common ground |
| `A-IA` | | Digital Pin D5 (PWM) | Motor A Direction / Speed |
| `A-IB` | | Digital Pin D6 (PWM) | Motor A Direction / Speed |
| `MOTOR A` | | DC Motor Leads | Screw terminal connection |

## Common mistakes

- **Exceeding the 12V maximum supply voltage:** The L9110S has no over-voltage protection. Powering the module from a 4S LiPo battery ($14.8\text{V} \dots 16.8\text{V}$) will burn out the internal MOSFETs immediately.
- **Motor stalling causing thermal shutdown:** Stalling small 130-size hobby motors at high voltages can draw $>1.2\text{A}$. Prolonged stall current will trigger thermal protection or permanently damage the SOP-8 chip.
- **Forgetting to tie Grounds together:** If motor power comes from an external battery pack, ensure the battery ground is connected to the microcontroller GND pin.

## Notes

- **L9110S vs L298N vs DRV8833:** L9110S is lower-voltage ($2.5\text{V} \dots 12\text{V}, 0.8\text{A}$) and extremely compact; L298N handles higher voltages ($up to 35\text{V}, 2\text{A}$) but suffers higher internal voltage drop ($2\text{V}\dots 3\text{V}$); DRV8833 uses MOSFETs with current limiting.
