## Overview

The **HV9911** (HV9911NG-G) is an advanced universal high-voltage switch-mode LED driver controller IC manufactured by Microchip Technology (originally Supertex). Packaged in a **16-lead SOIC** or **24-lead QFN**, it features an internal high-voltage linear regulator capable of operating directly from **9.0V to 250.0V DC** power rails.

Unlike open-loop current regulators, the HV9911 implements **closed-loop peak current-mode control** combined with an internal **1.0A peak MOSFET gate driver (`GATE`)**. It supports multiple switching converter topologies—including **Buck**, **Boost**, **SEPIC**, and **Buck-Boost**—making it ideal for high-power industrial LED luminaires, automotive LED headlights, and offline AC-DC LED drivers.

## Quick reference

| | |
|---|---|
| **Input Supply Voltage (`VIN`)** | 9.0 V to 250.0 V DC (Internal high-voltage bias regulator) |
| **MOSFET Gate Drive (`GATE`)** | $1.0\text{ A}$ peak source/sink current gate driver |
| **Topologies Supported** | Buck, Boost, SEPIC, Buck-Boost |
| **Control Scheme** | Closed-Loop Peak Current-Mode Control |
| **Dimming Capabilities** | True DC Analog Dimming (`LD` pin) & High-Contrast PWM Dimming (`PWM_D` pin) |
| **Protection Features** | Closed-loop Over-Voltage Protection (OVP), Output Short-Circuit Protection |
| **Package** | 16-lead SOIC / 24-lead QFN |

## Pinout (SOIC-16 Package)

```
             ┌───┴───┐
        VDD 1│ 1   16│ VIN (+9V to +250V)
       GATE 2│       │15 NC
        GND 3│ HV9911│14 OVP (Over-Voltage Sense)
         CS 4│       │13 FDBK (Closed-Loop Feedback)
       COMP 5│       │12 PWMD (PWM Dimming Input)
         LD 6│       │11 REF (Internal Reference)
        RT 7│       │10 SYNC
       VDD 8│       │9  AVDD
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1, 8 | `VDD` | Power | Internal $7.7\text{V}$ Gate Drive Regulator Output |
| 2 | `GATE` | Output | External N-Channel MOSFET Gate Drive Output ($1.0\text{A}$ peak) |
| 3 | `GND` | Power | Power Ground Reference |
| 4 | `CS` | Input | Peak Current Sense Input |
| 5 | `COMP` | Output | Error Amplifier Compensation Node |
| 6 | `LD` | Input | Linear Analog Dimming Input ($0.2\text{V} \dots 1.5\text{V}$) |
| 7 | `RT` | Input | Switching Frequency Programming Resistor Pin |
| 10 | `SYNC` | Input | External Clock Synchronization Input |
| 11 | `REF` | Output | Internal $1.25\text{V}$ Precision Reference Voltage Output |
| 12 | `PWMD` | Input | PWM Dimming Logic Input (High = Enable output switch; Low = Disable) |
| 13 | `FDBK` | Input | Output Current Closed-Loop Feedback Input |
| 14 | `OVP` | Input | Over-Voltage Protection Input |
| 16 | `VIN` | Power | High-Voltage Input Supply (+9.0V to +250.0V DC) |

## High-Voltage Safety Warning

> [!CAUTION]
> High Voltage Hazard!
> The HV9911 operates directly from high-voltage DC rails up to **$250\text{V}$ DC**. Dangerous shock hazards exist across external N-FET drains, inductors, and LED string terminals. Exercise extreme caution during breadboarding and PCB debugging.

## Common mistakes

- **Leaving `PWMD` (Pin 12) un-connected:** `PWMD` logic input enables/disables the external MOSFET gate driver. Pull `PWMD` HIGH to `REF` (Pin 11) for continuous non-dimmed operation.
- **Inadequate decoupling on `VDD` (Pins 1 & 8):** The internal $7.7\text{V}$ LDO powers the 1A gate driver. Decouple `VDD` pins with a low-ESR $1.0\ \mu\text{F} \dots 4.7\ \mu\text{F}$ ceramic capacitor directly to `GND`.

## Notes

- **HV9911 vs HV9910B:** HV9910B uses open-loop current control; HV9911 uses closed-loop current control with a 1A gate driver, delivering superior LED current regulation accuracy over varying supply voltages.
