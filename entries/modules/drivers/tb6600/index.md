## Overview

The **TB6600** is an industrial-style enclosed microstepping stepper motor driver module based on Toshiba's motor driver ICs (originally the TB6600HG, and in modern production units, the TB67S109AFTG). Housed in a rugged black anodized aluminum heatsink casing, it is engineered for high-power NEMA 17, NEMA 23, and NEMA 24 bipolar stepper motor applications in DIY CNC routers, 3D printers, laser cutters, and heavy robotics.

The module features high-speed optocoupler isolation for pulse, direction, and enable inputs (protecting control electronics from motor EMI noise), DIP switch configuration for microstep resolution (up to 1/32 step) and peak output current limiting (from 0.5 A to 3.5 A / 4.0 A peak), and automatic half-current idle reduction to limit motor heating when stationary.

## Quick reference

| | |
|---|---|
| **Motor supply voltage (`VCC`)** | 9.0 V to 42.0 V DC (24 V to 36 V recommended) |
| **Peak output current** | 4.0 A (0.5 A to 3.5 A working current set by DIP switches) |
| **Logic signal voltage** | +5.0 V DC nominal (use inline $2\text{ k}\Omega$ resistor for 12V/24V PLC signals) |
| **Control inputs** | Optocoupler isolated `PUL` (Step), `DIR` (Direction), `ENA` (Enable) |
| **Microstep resolution** | 1 (Full), 2, 4, 8, 16, 32 microstep modes |
| **Enclosure** | Aluminum heatsink casing with screw-terminal blocks |

## Terminal blocks & connections

The driver module exposes two heavy-duty screw terminal blocks:

### Power & Motor Terminals (4-pin & 2-pin block)

| Terminal | Signal | Description |
|---|---|---|
| `VCC` / `DC+` | Motor Power | Positive DC motor power supply (+9 V to +42 V DC) |
| `GND` / `DC-` | Motor Ground | Power supply ground reference |
| `A+` | Motor Coil A+ | Phase A positive stepper motor lead |
| `A-` | Motor Coil A- | Phase A negative stepper motor lead |
| `B+` | Motor Coil B+ | Phase B positive stepper motor lead |
| `B-` | Motor Coil B- | Phase B negative stepper motor lead |

### Signal Input Terminals (6-pin block)

The signal interface uses high-speed optocouplers with differential positive/negative terminals:

| Terminal | Signal | Description |
|---|---|---|
| `PUL+` / `CLK+` | Pulse Input (+) | Step pulse signal positive line |
| `PUL-` / `CLK-` | Pulse Input (-) | Step pulse signal negative line |
| `DIR+` | Direction (+) | Direction signal positive line |
| `DIR-` | Direction (-) | Direction signal negative line |
| `ENA+` | Enable (+) | Offline enable signal positive line |
| `ENA-` | Enable (-) | Offline enable signal negative line |

## DIP switch settings

Onboard 6-position DIP switches configure microstepping resolution (SW1–SW3) and current limit (SW4–SW6):

### Microstep Resolution Selection (SW1, SW2, SW3)

| Microstep | Steps/Rev (1.8° Motor) | SW1 | SW2 | SW3 |
|---|---|---|---|---|
| Full (1) | 200 | OFF | OFF | OFF |
| 1/2 | 400 | ON | OFF | OFF |
| 1/2 (mode B) | 400 | OFF | ON | OFF |
| 1/4 | 800 | ON | ON | OFF |
| 1/8 | 1600 | OFF | OFF | ON |
| 1/16 | 3200 | ON | OFF | ON |
| **1/32** | 6400 | OFF | ON | ON |

### Current Limiting Selection (SW4, SW5, SW6)

| Output Current (Peak) | Output Current (RMS) | SW4 | SW5 | SW6 |
|---|---|---|---|---|
| 0.5 A | 0.4 A | ON | ON | ON |
| 1.0 A | 0.9 A | OFF | ON | ON |
| 1.5 A | 1.3 A | ON | OFF | ON |
| 2.0 A | 1.8 A | OFF | OFF | ON |
| 2.5 A | 2.2 A | ON | ON | OFF |
| 2.8 A | 2.5 A | OFF | ON | OFF |
| 3.0 A | 2.7 A | ON | OFF | OFF |
| **3.5 A (4.0A Peak)** | 3.2 A | OFF | OFF | OFF |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Motor Supply Voltage | $V_{CC}$ | 9.0 | 24.0 | 42.0 | V | DC power supply |
| Signal Input Voltage | $V_{SIG}$ | 4.5 | 5.0 | 5.5 | V | $5\text{ V}$ logic (use series resistor for 12/24V) |
| Optocoupler Forward Current | $I_{F\_opto}$ | 8.0 | 10.0 | 15.0 | mA | Per control signal |
| Max Step Pulse Frequency | $f_{PUL}$ | — | — | 200 | kHz | High-speed optocouplers |
| Pulse Width High | $t_{PUL\_high}$ | 2.5 | — | — | µs | Minimum pulse width |
| Operating Temperature | $T_{opr}$ | -10 | — | 45 | °C | Ambient air |

## Wiring configurations

### Common Cathode Wiring (Negative Pins Tied Together)

When driving from standard 5V MCU pins (Arduino / ESP32):

- Connect `PUL-`, `DIR-`, `ENA-` together and wire to MCU `GND`.
- Connect `PUL+` to MCU Step Pin (e.g. D2).
- Connect `DIR+` to MCU Direction Pin (e.g. D3).
- Leave `ENA+` unconnected (enabled by default) or wire to MCU Enable Pin.

### Common Anode Wiring (Positive Pins Tied Together)

- Connect `PUL+`, `DIR+`, `ENA+` together and wire to MCU `+5V`.
- Connect `PUL-` to MCU Step Pin (active-low drive).
- Connect `DIR-` to MCU Direction Pin (active-low drive).

> [!WARNING]
> High Voltage Signal Input Warning:
> - The internal optocouplers are sized for **5 V DC signals**. If driving the inputs directly from 12V or 24V PLC outputs, you **MUST** install an external current-limiting resistor ($1\text{ k}\Omega$ for 12V, $2\text{ k}\Omega$ for 24V) in series with each `+` signal line to prevent burning out the internal optocouplers.

## Common mistakes

- **Inverting DIP Switch Labels:** Printed tables on cheap clone modules often invert the interpretation of ON and OFF states. If motor steps seem erratic or current is too low, verify the ON arrow stamped on the dip switch body.
- **Disconnected Motor Wires:** Connecting or disconnecting motor leads (`A+`, `A-`, `B+`, `B-`) while $V_{CC}$ power is applied causes immediate inductive breakdown of the output bridge MOSFETs.
- **Forgetting Common Ground on Signal Lines:** Failing to connect the controller ground to `PUL-`/`DIR-` in common-cathode mode prevents current flow through the optocoupler LEDs.

## Notes

- **TB6600 vs TB67S109AFTG:** Original TB6600HG chips used older BiCMOS technology; modern "TB6600" modules almost universally utilize the newer Toshiba TB67S109AFTG IC, which runs cooler due to lower MOSFET $R_{DS(on)}$ resistance.
