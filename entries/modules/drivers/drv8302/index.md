## Overview

The **DRV8302** (DRV8302DCAR) is an integrated 3-phase gate driver IC manufactured by Texas Instruments. It is the hardware-configured companion to the DRV8301, used extensively in VESC (Vedder Electronic Speed Controller) boards, electric skateboard controllers, e-bike drives, and high-power BLDC robotics.

Unlike the DRV8301 which uses SPI software registers, the DRV8302 configures overcurrent thresholds, amplifier gains, and PWM modes directly via physical **hardware pins** (`GAIN`, `M_PWM`, `M_OC`, `OC_ADJ`). Operating on **6.0V to 60.0V DC** ($2\text{S} \dots 14\text{S}$ LiPo batteries), it features a **1.5A step-down buck regulator**, two low-offset current-shunt amplifiers, and 6-channel PWM inputs.

## Quick reference

| | |
|---|---|
| **Power Supply Voltage (`PVDD`)**| 6.0 V to 60.0 V DC (65V absolute maximum) |
| **Gate Drive Current** | $1.7\text{ A}$ Peak Source / $2.3\text{ A}$ Peak Sink |
| **Control Mode** | Hardware Pin Configured (No SPI required) |
| **Integrated Buck Regulator** | Adjustable $1.5\text{ A}$ output (3.3V or 5.0V step-down supply) |
| **Current Sense Amplifiers** | 2x Independent differential current-shunt amplifiers ($10, 20, 40, 80\text{ V/V}$ selectable gain) |
| **Protection Features** | Overcurrent Protection (OCP), Overtemperature (OTS), Short-Circuit, UVLO |
| **Package** | 56-pin HTSSOP (PowerPAD down) |

## Hardware Configuration Pins

| Pin Name | Pin Function | Selectable States & Settings |
|---|---|---|
| `GAIN` | Amplifier Gain Select | GND = 10 V/V, 3.3V = 20 V/V, Open = 40 V/V, Reserved = 80 V/V |
| `M_PWM` | PWM Mode Input | GND = 6-channel PWM input mode; 3.3V = 3-channel PWM input mode |
| `M_OC` | Overcurrent Mode | GND = Cycle-by-cycle limiter; 3.3V = OCP Off; Open = Latch Shutoff |
| `OC_ADJ` | Overcurrent Threshold | Analog voltage set via resistor divider to GND |
| `nOCTW` | Fault Warning | Open-drain overcurrent & thermal warning output |
| `nFAULT` | Fault Shutdown | Open-drain fault interrupt output |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Operating Supply Voltage | $V_{PVDD}$ | 6.0 | 24.0/48.0| 60.0 | V | DC |
| Gate Drive Source Current| $I_{SOURCE}$| 1.0 | 1.7 | — | A | $V_{BST} - V_{SH} = 10\text{V}$ |
| Gate Drive Sink Current | $I_{SINK}$ | 1.3 | 2.3 | — | A | $V_{SH} = 10\text{V}$ |
| Current Sense Amp Gain | $G_{CSA}$ | 10 | 20 | 80 | V/V | Hardware pin setting via `GAIN` |
| Buck Output Current | $I_{BUCK}$ | — | 1.5 | — | A | Step-down converter |

## Common mistakes

- **Leaving `GAIN` or `M_OC` pins floating without checking default states:** Because DRV8302 relies on pin states instead of SPI registers, leaving configuration pins un-connected can trigger latching overcurrent modes. Always tie `GAIN`, `M_PWM`, and `M_OC` to hard logic levels.
- **High $di/dt$ switching noise on current-sense lines:** Ensure current-shunt traces (`SP1`/`SN1` and `SP2`/`SN2`) are routed as differential pairs away from high-current motor phases.

## Notes

- **DRV8302 vs DRV8301:** DRV8302 is hardware pin-configured (ideal for simple microcontrollers without SPI drivers); DRV8301 uses 4-wire SPI registers for software configuration and detailed fault diagnostics.
