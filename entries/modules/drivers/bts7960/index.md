## Overview

The **BTS7960** (BTS7960B) is a fully integrated, high-current half-bridge motor driver IC from Infineon's **NovalithIC™** family. Housed in a 7-pin TO-263 power package (and widely popularized on pre-assembled **IBT-2 dual BTS7960 43A motor driver modules**), it combines a P-channel high-side power MOSFET, an N-channel low-side power MOSFET, and an integrated driver circuit into a single thermal package.

With a nominal current rating of up to **$43\text{ A}$ peak** and ultra-low combined on-state path resistance of just **$16\text{ m}\Omega$ typical**, the BTS7960 easily handles heavy 12V–24V brushed DC motors, electric scooters, e-bike winches, robotic actuators, and high-power linear actuators. It integrates analog current sense feedback (`IS`), overtemperature protection, short-circuit current limiting, undervoltage lockout, and adjustable slew-rate control up to **$25\text{ kHz}$ PWM**.

## Quick reference

| | |
|---|---|
| **Driver Type** | High-Current Half-Bridge Motor Driver (NovalithIC™) |
| **Package** | TO-263-7 (D2PAK-7) / IBT-2 Module (2× BTS7960) |
| **Motor Supply Voltage ($V_S$)**| $6.0\text{ V}$ to $27.0\text{ V}$ DC (Survival up to $40\text{V}$) |
| **Continuous Current Rating** | $15.0\text{ A} \dots 20.0\text{ A}$ (with aluminum heatsink and active cooling) |
| **Peak / Stall Current Limit** | $43.0\text{ A}$ typical internal current limit |
| **Total MOSFET On-Resistance ($R_{ON}$)** | $16\text{ m}\Omega$ typical ($9\text{ m}\Omega$ high-side + $7\text{ m}\Omega$ low-side at $25^\circ\text{C}$) |
| **PWM Switching Frequency** | Up to $25\text{ kHz}$ |
| **Logic Supply Voltage ($V_{CC}$)**| $4.5\text{ V}$ to $5.5\text{ V}$ DC ($3.3\text{V}$ logic compatible inputs) |
| **Diagnostics & Sensing** | Current sense analog output (`IS`) with proportional current mirror + Fault flag |

## Pinout (TO-263-7 IC Package)

```
        ┌──────────────┐
    OUT ─│ 1          7 │─ IS
    OUT ─│ 2    TAB   6 │─ SR
     VS ─│ 3   (OUT)  5 │─ INH
    GND ─│ 4            │
        └───────────────┘
          (Pin 8 is IN)
```

| Pin | Name | Description |
|---|---|---|
| 1, 2 | `OUT` | Half-bridge power output (connected internally to Tab) |
| 3 | `VS` | Motor power supply input (+6.0V to +27.0V DC) |
| 4 | `GND` | Logic and low-side power ground return |
| 5 | `INH` | Inhibit / Enable input (Active-HIGH: HIGH = Enabled, LOW = Standby/High-Z) |
| 6 | `SR` | Slew rate adjustment pin (Connect resistor to GND to tune switching speed) |
| 7 | `IS` | Current sensing analog output and diagnostic fault flag |
| 8 (Lead) | `IN` | Logic PWM input (HIGH = High-Side ON, LOW = Low-Side ON) |

## Common IBT-2 Dual-Driver Module Pinout

The ubiquitous **IBT-2 module** pairs two BTS7960 ICs together to create a complete full H-bridge with screw terminals:

```
    IBT-2 Logic Control Header:
    ┌──────────────────────────────┐
    │ [VCC]  [GND]                 │  VCC: +5V Logic, GND: Ground
    │ [R_EN] [L_EN]                │  R_EN / L_EN: Forward / Reverse Bridge Enables (Tie HIGH)
    │ [RPWM] [LPWM]                │  RPWM / LPWM: Forward / Reverse MCU PWM speed inputs
    │ [R_IS] [L_IS]                │  R_IS / L_IS: Current sense analog outputs
    └──────────────────────────────┘
```

| Module Pin | Description | MCU Connection (Arduino) |
|---|---|---|
| `VCC` | +5V logic supply | 5V pin |
| `GND` | Ground reference | GND |
| `R_EN` | Right/Forward half-bridge enable | Digital Pin (or tie to 5V) |
| `L_EN` | Left/Reverse half-bridge enable | Digital Pin (or tie to 5V) |
| `RPWM` | Forward PWM speed control input | PWM Pin (e.g. Pin 5) |
| `LPWM` | Reverse PWM speed control input | PWM Pin (e.g. Pin 6) |
| `R_IS` | Forward current sense mirror | Analog Input (e.g. A0) |
| `L_IS` | Reverse current sense mirror | Analog Input (e.g. A1) |

## Control Logic (IBT-2 Module)

| `R_EN` | `L_EN` | `RPWM` | `LPWM` | Motor Behavior |
|---|---|---|---|---|
| `0` | `0` | X | X | **Coast / Standby** (High-Z) |
| `1` | `1` | `0` | `0` | **Brake to Ground** (Slow decay) |
| `1` | `1` | PWM | `0` | **Forward** (Speed proportional to PWM duty cycle) |
| `1` | `1` | `0` | PWM | **Reverse** (Speed proportional to PWM duty cycle) |
| `1` | `1` | `1` | `1` | **Brake to Ground** |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Motor Supply Voltage | $V_S$ | 6.0 | 12.0 | 27.0 | V | Normal operation |
| Peak Current Limit | $I_{CL}$ | 33 | 43 | 55 | A | $T_J = 25^\circ\text{C}$ |
| High-Side On-Resistance | $R_{ON(HS)}$ | — | 9.0 | 16.0 | $\text{m}\Omega$ | $I_{OUT} = 9.0\text{A}, T_J = 25^\circ\text{C}$ |
| Low-Side On-Resistance | $R_{ON(LS)}$ | — | 7.0 | 14.0 | $\text{m}\Omega$ | $I_{OUT} = 9.0\text{A}, T_J = 25^\circ\text{C}$ |
| Current Sense Ratio ($I_{OUT} / I_{IS}$)| $k_{ILIS}$ | — | 8500 | — | — | Current mirror scale factor |
| Quiescent Current (Standby)| $I_{VS(std)}$ | — | 7.0 | 20.0 | $\mu\text{A}$ | $INH = 0\text{V}$ |

## Common mistakes

- **Assuming 43A is continuous without active cooling:** The 43A rating is the silicon pulse/short-circuit limit. Continuous DC operation beyond $12\text{A} \dots 15\text{A}$ produces substantial heat; always ensure thermal paste contact with an aluminum heatsink and forced-air cooling.
- **Forgetting to pull both R_EN and L_EN HIGH:** The enable pins (`R_EN`, `L_EN`) must both be asserted HIGH. If either is LOW, that side of the H-bridge floats in high impedance, preventing bidirectional current flow.
- **Switching both RPWM and LPWM simultaneously at high duty cycles:** Alternating between forward and reverse without a deadtime gap or brake state can induce inductive back-EMF spikes that exceed the $40\text{V}$ maximum rating. Place a $100\ \mu\text{F} \dots 1000\ \mu\text{F}$ low-ESR electrolytic capacitor across the motor supply ($B+/B-$).

## Notes

- **Current Sensing Formula:** The current on pin `IS` is proportional to the high-side MOSFET current: $I_{IS} = I_{OUT} / 8500$. Connecting a $1\text{ k}\Omega$ sense resistor to ground produces $V_{IS} = I_{OUT} \times 1000 / 8500 \approx 0.117\text{ V per Ampere}$.
