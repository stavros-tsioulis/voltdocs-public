## Overview

The **DRV8825** is a complete microstepping bipolar stepper motor driver IC manufactured by Texas Instruments, commonly populated on Pololu-form-factor ("StepStick") breakout carrier modules.

Serving as a higher-voltage and higher-current drop-in alternative to the A4988 driver, the DRV8825 supports motor supply voltages up to 45 V, delivers up to 1.5 A continuous current per phase without forced air cooling (and up to 2.2 A with heatsinking and airflow), and offers microstepping resolution down to 1/32-step. It features adjustable current limiting via an onboard potentiometer, built-in indexer logic for simple STEP/DIR control, and internal protection against overcurrent, short circuits, thermal shutdown, and undervoltage lockout.

## Quick reference

| | |
|---|---|
| **Motor supply voltage (`VMOT`)** | 8.2 V to 45.0 V DC |
| **Logic supply voltage (`VVR`)** | 2.5 V to 5.25 V DC (internal 3.3V regulator) |
| **Continuous current per phase** | 1.5 A (2.2 A max with heatsink/fan) |
| **Microstep resolutions** | Full, 1/2, 1/4, 1/8, 1/16, 1/32 step |
| **Control interface** | STEP / DIR pins (simple step and direction pulse) |
| **MOSFET $R_{DS(on)}$** | $300\text{ m}\Omega$ typical (high side + low side) |
| **Form factor** | 16-pin 0.1" DIP carrier module (Pololu pinout) |

## Pinout

The module features two 8-pin 0.1" headers matching standard StepStick / RAMPS sockets:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `ENABLE` | Digital Input | Active-Low driver enable. High = outputs disabled. |
| 2 | `M0` | Digital Input | Microstep resolution selector pin 0 |
| 3 | `M1` | Digital Input | Microstep resolution selector pin 1 |
| 4 | `M2` | Digital Input | Microstep resolution selector pin 2 |
| 5 | `RESET` | Digital Input | Active-Low device reset (must be tied High for normal operation) |
| 6 | `SLEEP` | Digital Input | Active-Low sleep mode input (must be tied High for normal operation) |
| 7 | `STEP` | Digital Input | Step pulse input. Rising edge advances motor one step/microstep. |
| 8 | `DIR` | Digital Input | Direction input. Logic High = clockwise, Low = counter-clockwise. |
| 9 | `GND` | Power | Logic & Ground reference (0 V) |
| 10 | `FAULT` | Digital Output | Active-Low open-drain fault output (overtemp/overcurrent flag) |
| 11 | `A1` | Motor Output | Bipolar stepper motor coil A phase 1 |
| 12 | `A2` | Motor Output | Bipolar stepper motor coil A phase 2 |
| 13 | `B2` | Motor Output | Bipolar stepper motor coil B phase 2 |
| 14 | `B1` | Motor Output | Bipolar stepper motor coil B phase 1 |
| 15 | `GND` | Power | Motor Ground reference |
| 16 | `VMOT` | Power | Motor supply voltage (+8.2 V to +45 V DC) |

## Microstep resolution selection

The microstep mode is selected via inputs `M0`, `M1`, and `M2`. All three pins have internal $100\text{ k}\Omega$ pull-down resistors (defaulting to Full-step when left floating):

| `M0` | `M1` | `M2` | Microstep Resolution |
|---|---|---|---|
| Low | Low | Low | Full step |
| High | Low | Low | 1/2 step |
| Low | High | Low | 1/4 step |
| High | High | Low | 1/8 step |
| Low | Low | High | 1/16 step |
| High | Low | High | **1/32 step** |
| Low | High | High | 1/32 step |
| High | High | High | 1/32 step |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Motor Supply Voltage | $V_{MOT}$ | 8.2 | 24.0 | 45.0 | V | Motor power rail |
| Logic Level Input High | $V_{IH}$ | 2.0 | 3.3 / 5.0 | 5.25 | V | `STEP`, `DIR`, `ENABLE`, `M0-M2` |
| Logic Level Input Low | $V_{IL}$ | -0.3 | 0 | 0.8 | V | `STEP`, `DIR`, `ENABLE`, `M0-M2` |
| Phase Current (Uncooled) | $I_{out}$ | — | 1.5 | 1.8 | A | Natural convection |
| Phase Current (Cooled) | $I_{out\_cooled}$ | — | 2.0 | 2.2 | A | Heatsink + forced air cooling |
| Minimum Pulse Width | $t_{STEP}$ | 1.9 | — | — | µs | `STEP` high/low pulse duration |
| Thermal Shutdown Temp | $T_{TSD}$ | 150 | 160 | 175 | °C | Junction temperature shutdown |

## Current limiting calibration ($V_{ref}$)

Before running a motor, the phase current limit must be set using the onboard trimmer potentiometer ($V_{ref}$ measured between the potentiometer metal wiper and `GND`):

$$ I_{trip} = \frac{V_{ref}}{2 \times R_{sense}} = \frac{V_{ref}}{2 \times 0.100\ \Omega} = 5 \times V_{ref} $$

*(Assuming standard $R_{sense} = 0.100\ \Omega$ current sense resistors on the module PCB)*

**Example:** To limit current to $1.0\text{ A}$ per phase:

$$ V_{ref} = 1.0\text{ A} \times 0.2 = 0.20\text{ V} = 200\text{ mV} $$

## Wiring

| DRV8825 Pin | → | Arduino / MCU | External Power | Notes |
|---|---|---|---|---|
| `VMOT` | | — | +12V to +36V DC | Motor power supply rail |
| `GND` (Motor) | | — | Power Supply GND | Bulk decoupling capacitor mandatory |
| `GND` (Logic) | | MCU GND | Power Supply GND | Shared ground reference |
| `STEP` | | Digital Pin (e.g. D3) | — | Step pulse signal |
| `DIR` | | Digital Pin (e.g. D4) | — | Direction signal |
| `RESET` & `SLEEP` | | — | — | **Connect `RESET` directly to `SLEEP`** |

> [!WARNING]
> LC Voltage Spike Hazard:
> - Connecting or disconnecting a stepper motor while the DRV8825 is powered will destroy the driver IC.
> - A bulk electrolytic decoupling capacitor (minimum $47\ \mu\text{F}$ to $100\ \mu\text{F}$, 50V rated) **MUST** be placed across `VMOT` and `GND` close to the module pins to suppress destructive ceramic capacitor LC voltage spikes.

## Common mistakes

- **Leaving `RESET` and `SLEEP` floating:** Both pins must be pulled High (or shorted together) for the driver to function. If left un-connected, the chip remains locked in sleep mode.
- **Hot-plugging motors:** Unplugging motor cables while `VMOT` power is connected causes inductive kickback spikes that instantly destroy the output MOSFET H-bridges.
- **Confusing DRV8825 orientation with A4988:** Although the DRV8825 fits in the same 16-pin socket, the potentiometer faces the **opposite direction** relative to `VMOT` compared to an A4988 StepStick. Plugging it in upside down shorts the power rails.

## Notes

- **A4988 vs DRV8825:** DRV8825 supports higher voltage (45V vs 35V), higher current (2.2A vs 2.0A max), higher microstepping (1/32 vs 1/16), and has a lower $R_{DS(on)}$ resulting in less heat generation at equivalent currents.
