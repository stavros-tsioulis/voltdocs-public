## Overview

The **DRV8848** (packaged in a 16-pin HTSSOP **DRV8848PWP** with exposed thermal pad) is a dual full-bridge motor driver IC manufactured by Texas Instruments. Designed for battery-powered or low-voltage robotics, toy motors, and office automation, it drives **two brushed DC motors**, **one bipolar stepper motor**, or solenoids from a supply voltage of **$4.0\text{ V}$ to $18.0\text{ V}$**.

Each H-bridge output delivers up to **$2.0\text{ A}$ peak** ($1.0\text{ A}$ continuous RMS) current. Bridges can also be connected in parallel to drive a single DC motor at up to **$2.0\text{ A}$ RMS continuous** current.

## Quick reference

| | |
|---|---|
| **Driver Type** | Dual Full-Bridge PWM Motor Driver |
| **Package** | HTSSOP-16 PowerPAD (PWP) / Adafruit Breakout Board |
| **Motor Supply Voltage ($V_M$)** | $4.0\text{ V}$ to $18.0\text{ V}$ DC |
| **Continuous RMS Current** | $1.0\text{ A}$ per bridge ($2.0\text{ A}$ in parallel single-motor mode) |
| **Peak Output Current** | Up to $2.0\text{ A}$ peak per bridge |
| **FET On-Resistance ($R_{DS(ON)}$)**| $0.51\ \Omega$ (High-side + Low-side combined at $25^\circ\text{C}$) |
| **Current Control** | Internal PWM current regulation set by `VREF` and `AISEN`/`BISEN` |
| **Protection Features** | Overcurrent Protection (OCP), Short-Circuit, Undervoltage (UVLO), Thermal Shutdown |

## Pinout (HTSSOP-16 Package)

```
        ┌──────────────┐
  AISEN ─│ 1         16 │─ AIN1
  AOUT1 ─│ 2         15 │─ AIN2
     VM ─│ 3   EP    14 │─ GND
  AOUT2 ─│ 4         13 │─ VREF
  BOUT2 ─│ 5         12 │─ ~nSLEEP~
   VINT ─│ 6         11 │─ ~nFAULT~
  BOUT1 ─│ 7         10 │─ BIN2
  BISEN ─│ 8          9 │─ BIN1
        └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `AISEN` | Bridge A current sense pin (Connect resistor to GND or tie to GND if unused) |
| 2 | `AOUT1` | Bridge A motor output 1 |
| 3 | `VM` | Motor supply voltage (+4.0V to +18.0V DC) |
| 4 | `AOUT2` | Bridge A motor output 2 |
| 5 | `BOUT2` | Bridge B motor output 2 |
| 6 | `VINT` | Internal regulator bypass output (Connect 2.2µF ceramic cap to GND) |
| 7 | `BOUT1` | Bridge B motor output 1 |
| 8 | `BISEN` | Bridge B current sense pin (Connect resistor to GND or tie to GND if unused) |
| 9 | `BIN1` | Bridge B logic PWM input 1 |
| 10 | `BIN2` | Bridge B logic PWM input 2 |
| 11 | `~nFAULT~` | Active-LOW open-drain fault indicator output |
| 12 | `~nSLEEP~` | Sleep mode input (Active-LOW: LOW = Sleep/Low-power, HIGH = Enabled) |
| 13 | `VREF` | Analog voltage reference input for current regulation threshold |
| 14 | `GND` | Ground reference (Solder central Thermal Pad to PCB GND) |
| 15 | `AIN2` | Bridge A logic PWM input 2 |
| 16 | `AIN1` | Bridge A logic PWM input 1 |

## Bridge Control Logic Truth Table (Each Bridge)

| `xIN1` | `xIN2` | `xOUT1` | `xOUT2` | Function / Operating Mode |
|---|---|---|---|---|
| Low (`0`) | Low (`0`) | High-Z | High-Z | **Coast** (Outputs disabled) |
| Low (`0`) | High (`1`) | Low | High | **Reverse** |
| High (`1`) | Low (`0`) | High | Low | **Forward** |
| High (`1`) | High (`1`) | Low | Low | **Brake** (Slow decay) |

## Internal Current Regulation Formula

The internal current regulation trip point ($I_{TRIP}$) for each bridge is set by the reference voltage on Pin 13 (`VREF`) and the sense resistor ($R_{SENSE}$) connected to `xISEN`:

$$ I_{TRIP} = \frac{V_{REF}}{6.6 \times R_{SENSE}} $$

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Motor Supply Voltage | $V_M$ | 4.0 | 12.0 | 18.0 | V | Operating supply |
| RMS Output Current | $I_{RMS}$ | — | 1.0 | — | A | Per bridge, $V_M = 12\text{V}, T_A = 25^\circ\text{C}$ |
| Peak Output Current | $I_{PEAK}$ | — | 2.0 | — | A | Per bridge |
| Sleep Current | $I_{SLEEP}$ | — | 1.5 | 5.0 | $\mu\text{A}$ | $\overline{nSLEEP} = 0\text{V}$ |
| Total MOSFET On-Resistance | $R_{DS(ON)}$ | — | 0.51 | 0.65 | $\Omega$ | High-side + Low-side |

## Common mistakes

- **Leaving ~nSLEEP~ floating:** Pin 12 ($\overline{nSLEEP}$) has an internal pull-down. Leaving it unconnected puts the driver into low-power sleep mode, disabling all outputs. Pull $\overline{nSLEEP}$ to $3.3\text{V}$ or $5\text{V}$ to enable operation.
- **Omitting 2.2µF cap on VINT pin:** Pin 6 (`VINT`) is the internal bypass rail for internal logic. Operating without a $2.2\ \mu\text{F}$ decoupling capacitor on `VINT` causes erratic gate drive switching.

## Notes

- **Parallel Mode for High Current:** Tie `AIN1` to `BIN1`, `AIN2` to `BIN2`, `AOUT1` to `BOUT1`, and `AOUT2` to `BOUT2` to drive a single large DC motor at up to $2.0\text{ A}$ continuous RMS current.
