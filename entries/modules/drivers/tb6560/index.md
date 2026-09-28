## Overview

The **TB6560** (specifically the TB6560AHQ / TB6560AFG) is a monolithic bipolar stepper motor driver IC manufactured by Toshiba, housed in a heavy-tab 25-pin multi-watt package (HZIP25). It served as the foundation for an entire generation of DIY CNC routers, mill retrofits, plasma tables, and 3D printing equipment.

Designed to drive medium-to-large high-torque NEMA 17, NEMA 23, and NEMA 24 bipolar stepper motors, the TB6560 delivers up to $3.0\text{ A}$ continuous ($3.5\text{ A}$ peak) current per phase across a motor supply voltage span from $4.5\text{ V}$ to $34.0\text{ V}$ DC. It incorporates an internal decoder supporting 1-phase, 2-phase, 1-2 phase, and microstepping down to 1/16-step excitation modes, alongside programmable current decay (0%, 25%, 50%, 100%) and torque attenuation (100%, 75%, 50%, 20%).

In hobbyist and industrial automation contexts, the chip is most commonly encountered on dedicated single-axis breakout driver modules (the popular "TB6560 3A Red/Blue Driver Board") and multi-axis DB25 parallel-port CNC controller shields. These modules integrate high-speed optocouplers (`6N137` / `PC817`) for full galvanic isolation between delicate microcontroller or PC parallel-port lines and noisy motor power rails.

## Quick reference

| Parameter | Value | Notes |
|---|---|---|
| **Motor Supply Voltage ($V_{MA}/V_{MB}$)** | $4.5\text{ V}$ to $34.0\text{ V}$ DC | Absolute maximum $40.0\text{ V}$ |
| **Logic Supply Voltage ($V_{DD}$)** | $4.5\text{ V}$ to $5.5\text{ V}$ DC | Strictly required before motor power |
| **Peak Output Current** | $3.5\text{ A}$ | Peak allowable winding surge |
| **Rated Continuous Current** | $3.0\text{ A}$ | With heatsink and forced-air cooling |
| **Microstep Resolutions** | Full (1/1), Half (1/2), 1/4, 1/8, 1/16 | Configured via `M1`, `M2` inputs |
| **Decay Modes** | 0% (Fast), 25%, 50%, 100% (Slow) | Configured via `DCY1`, `DCY2` inputs |
| **MOSFET $R_{DS(ON)}$** | $600\text{ m}\Omega$ typical | High-side + low-side total at $25^\circ\text{C}$ |
| **Control Signal Interface** | Optocoupled `CLK`, `CW`, `ENABLE` | Compatible with $3.3\text{V}$ and $5\text{V}$ logic levels |

## Terminals

### Single-axis CNC driver module screw terminals

On standalone single-axis TB6560 CNC breakout modules, connections are made via heavy-duty industrial screw terminal blocks:

| Terminal | Label | Type | Description |
|---|---|---|---|
| 1 | `CLK+` (`PUL+`) | Opto Input | Pulse / Step positive optocoupler cathode/anode |
| 2 | `CLK-` (`PUL-`) | Opto Input | Pulse / Step negative optocoupler terminal |
| 3 | `CW+` (`DIR+`) | Opto Input | Direction positive optocoupler cathode/anode |
| 4 | `CW-` (`DIR-`) | Opto Input | Direction negative optocoupler terminal |
| 5 | `EN+` | Opto Input | Driver enable positive terminal (active-low or active-high configurable) |
| 6 | `EN-` | Opto Input | Driver enable negative terminal |
| 7 | `A+` | Motor Output | Stepper motor phase A lead 1 |
| 8 | `A-` | Motor Output | Stepper motor phase A lead 2 |
| 9 | `B+` | Motor Output | Stepper motor phase B lead 1 |
| 10 | `B-` | Motor Output | Stepper motor phase B lead 2 |
| 11 | `GND` | Power | Motor power supply ground ($0\text{ V}$) |
| 12 | `+24V` (`VCC`) | Power | Motor supply voltage ($+12\text{ V}$ to $+32\text{ V}$ DC) |

### TB6560AHQ IC Pinout (25-pin HZIP25)

| Pin | Name | Description | Pin | Name | Description |
|---|---|---|---|---|---|
| 1 | `NC` | No connection | 14 | `CW` | Clockwise / Direction input |
| 2 | `TQ1` | Torque setting input 1 | 15 | `MO` | Electrical angle monitor output |
| 3 | `TQ2` | Torque setting input 2 | 16 | `RESET` | Reset input (active-low) |
| 4 | `VMA` | Motor supply for phase A | 17 | `ENABLE` | Output enable input |
| 5 | `OUTA+` | Phase A non-inverting output | 18 | `OSC` | Chopper oscillator capacitor pin |
| 6 | `NFA` | Phase A current sense resistor | 19 | `VDD` | Logic supply ($+5\text{ V}$) |
| 7 | `OUTA-` | Phase A inverting output | 20 | `VMB` | Motor supply for phase B |
| 8 | `PGNDA` | Power ground for phase A | 21 | `OUTB+` | Phase B non-inverting output |
| 9 | `DCY1` | Decay setting input 1 | 22 | `NFB` | Phase B current sense resistor |
| 10 | `DCY2` | Decay setting input 2 | 23 | `OUTB-` | Phase B inverting output |
| 11 | `M1` | Microstep setting input 1 | 24 | `PGNDB` | Power ground for phase B |
| 12 | `M2` | Microstep setting input 2 | 25 | `SGND` | Signal ground reference |
| 13 | `CLK` | Clock / Step pulse input | FIN | `FIN` | Metal heatsink mounting tab |

## The technical core

### Microstepping configuration

Microstep resolution is set by logic inputs `M1` and `M2` (commonly mapped to DIP switches `S5` and `S6` on CNC boards):

| `M2` | `M1` | Excitation Mode | Step Angle Division |
|---|---|---|---|
| Low | Low | 1-2 Phase (Half Step A) | 1/2 step |
| Low | High | 4W1-2 Phase | **1/16 step** |
| High | Low | 2-Phase (Full Step) | 1/1 step |
| High | High | 2W1-2 Phase | 1/8 step |

*(Note: Certain module variants wire `M1` and `M2` differently; refer to the silkscreen printed on the aluminum heatsink enclosure).*

### Current decay mode selection

The chopper off-time decay characteristics are established via `DCY1` and `DCY2` (DIP switches `S3` and `S4`):

| `DCY2` | `DCY1` | Decay Mode | Characteristics |
|---|---|---|---|
| Low | Low | **0% (Fast Decay)** | Best current wave tracking at high step rates; higher audible hiss |
| Low | High | **25% Mixed Decay** | Recommended default for general-purpose CNC motion |
| High | Low | **50% Mixed Decay** | Smoother low-speed motion |
| High | High | **100% (Slow Decay)** | Lowest acoustic noise, but prone to current distortion at higher speeds |

### Torque scaling (running & holding current)

Inputs `TQ1` and `TQ2` scale the regulated peak current (DIP switches `S1` and `S2`):

| `TQ2` | `TQ1` | Current Scale Factor | Use Case |
|---|---|---|---|
| Low | Low | **100%** | Full torque running mode |
| Low | High | **75%** | Standard continuous operation |
| High | Low | **50%** | Light load or low-speed positioning |
| High | High | **20%** | Idle standby current / thermal reduction |

### Peak current calculation

Peak motor current $I_{out}$ is determined by the external current sensing resistors $R_{NF}$ (typically $0.22\ \Omega$ or $0.15\ \Omega$ high-wattage cement or metal-strip resistors) and the reference voltage $V_{ref}$:

$$ I_{out} = \frac{V_{ref}}{3 \times R_{NF}} \times \text{Torque}\% $$

On boards where $V_{ref}$ is derived from the $5\text{ V}$ rail via a voltage divider to produce $V_{ref} = 1.5\text{ V}$:
$$ I_{out} = \frac{1.5\text{ V}}{3 \times 0.22\ \Omega} = 2.27\text{ A peak (at 100\% torque)} $$

### Electrical specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Motor Supply Voltage | $V_M$ | 4.5 | 24.0 | 34.0 | V | Operating range |
| Logic Supply Voltage | $V_{DD}$ | 4.5 | 5.0 | 5.5 | V | Digital supply |
| Peak Output Current | $I_{PEAK}$ | — | — | 3.5 | A | $t_{w} \le 100\text{ ms}$ |
| Continuous Current | $I_{OUT}$ | — | 2.5 | 3.0 | A | Heatsink with fan |
| Output Saturation Resistance | $R_{ON}$ | — | 0.6 | 0.85 | $\Omega$ | $I_{OUT} = 2\text{ A}$ |
| Minimum Clock Pulse Width | $t_{CLK\_PW}$ | 1.0 | — | — | µs | `CLK` high or low duration |
| Optocoupler Propagation Delay | $t_{PD}$ | — | 0.2 | 1.0 | µs | On modules using `6N137` |
| Thermal Shutdown Temp | $T_{TSD}$ | 150 | 165 | 180 | °C | Silicon junction temp |

## Usage

### Wiring to an Arduino / CNC controller (common-cathode configuration)

Connect all negative optocoupler inputs (`CLK-`, `CW-`, `EN-`) together to the microcontroller ground (`GND`). Connect the positive terminals to MCU digital I/O pins:

| TB6560 Terminal | → | Microcontroller / Controller | Power Supply |
|---|---|---|---|
| `CLK+` (`PUL+`) | | MCU Digital Pin (Step Pulse) | — |
| `CW+` (`DIR+`) | | MCU Digital Pin (Direction) | — |
| `EN+` | | MCU Digital Pin (Driver Enable) | — |
| `CLK-`, `CW-`, `EN-` | | MCU Ground (`GND`) | — |
| `+24V` (`VCC`) | | — | $+12\text{V}$ to $+30\text{V}$ DC ($>5\text{A}$) |
| `GND` (Power) | | — | DC Supply Power Ground |
| `A+`, `A-` | | Stepper Motor Coil Phase A | — |
| `B+`, `B-` | | Stepper Motor Coil Phase B | — |

> [!CAUTION]
> Catastrophic Failure Hazard — Power Sequencing Rule:
> **The $+5\text{ V}$ logic supply ($V_{DD}$) MUST be energized before or simultaneously with the motor power supply ($V_M$).**
> - If motor voltage ($24\text{ V} - 34\text{ V}$) is applied while the internal logic rail ($5\text{ V}$) is unpowered, the internal MOSFET gate drivers float into partial turn-on states, causing immediate cross-conduction shoot-through across the H-bridge.
> - This shoot-through destroys the TB6560 IC in milliseconds with smoke, scorching, and audible pops.
> - Always power your CNC logic / breakout board power supply before turning on the heavy motor power supply! When powering down, disconnect motor power first.

### Arduino step-pulse generation

```cpp
// Single-Axis TB6560 Stepper Controller Test
const int pinPulse  = 9;
const int pinDir    = 8;
const int pinEnable = 7;

void setup() {
  pinMode(pinPulse, OUTPUT);
  pinMode(pinDir, OUTPUT);
  pinMode(pinEnable, OUTPUT);

  // Enable driver: high level illuminates optocoupler
  digitalWrite(pinEnable, HIGH);
  digitalWrite(pinDir, HIGH);
  delay(100); // Allow optocouplers to settle
}

void loop() {
  // Rotate forward: 1600 microsteps (1 rev at 1/8 step on 1.8-deg motor)
  digitalWrite(pinDir, HIGH);
  for (int i = 0; i < 1600; i++) {
    digitalWrite(pinPulse, HIGH);
    delayMicroseconds(5); // Minimum 1 us pulse width for 6N137 optocoupler
    digitalWrite(pinPulse, LOW);
    delayMicroseconds(400);
  }
  delay(1000);

  // Rotate reverse
  digitalWrite(pinDir, LOW);
  for (int i = 0; i < 1600; i++) {
    digitalWrite(pinPulse, HIGH);
    delayMicroseconds(5);
    digitalWrite(pinPulse, LOW);
    delayMicroseconds(400);
  }
  delay(1000);
}
```

## Common mistakes

- **Violating power-up sequencing:** Powering the high-voltage motor rail before the 5V logic supply is the number one cause of blown TB6560 drivers worldwide.
- **Flipping DIP switches while powered:** Changing current or microstep DIP switches while motor power is applied causes inductive transient spikes that can puncture the IC internal gates. Always disconnect power before altering DIP switches.
- **Unplugging motor cables while energized:** Stepper motor coils store inductive energy; disconnecting a motor wire under load causes an inductive kick that immediately breaks down the output MOSFETs.
- **Using slow optocouplers for high pulse rates:** Cheap cloned boards often replace fast `6N137` optocouplers ($10\text{ Mbit/s}$) with sluggish `PC817` optocouplers ($t_r \approx 10\ \mu\text{s}$). Sluggish optocouplers distort pulses at high frequencies, causing skipped steps. Adding a $1\text{ k}\Omega$ pull-up resistor to the opto collector or replacing the optocoupler fixes this issue.

## Notes

- **Successor (TB6600):** Toshiba developed the TB6600 (and TB67S109) to replace the TB6560. The TB6600 raises the maximum motor voltage to $42\text{ V}$, peak current to $4.0\text{ A}$, and incorporates improved internal sequencing logic that eliminates the TB6560's fatal power-on shoot-through vulnerability.
