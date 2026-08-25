## Overview

The **MIC4608** is a 600V half-bridge power MOSFET and IGBT gate driver IC manufactured by Microchip Technology (originally Micrel). Operating across a supply voltage range of **$5.5\text{V}$ to $16.0\text{V}$**, it provides robust gate drive capability ($1.0\text{A}$ source and $1.0\text{A}$ sink peak current) for driving high- and low-side N-channel MOSFETs in offline power converters, BLDC motor drives, and solar inverters.

A standout feature of the MIC4608 is its **State (`ST`) pin**, which selects between **Dual Independent Input Mode** (`ST = 0`, separate `HI` and `LI` inputs) and **Single PWM Input Mode** (`ST = 1`, single input controlling both outputs with built-in shoot-through protection). The IC integrates dual undervoltage lockout circuits (UVLO) with low quiescent currents and input low-pass filters to prevent glitching from high $dV/dt$ switching noise.

## Quick reference

| | |
|---|---|
| **Driver Type** | High and Low Side Half-Bridge Gate Driver IC |
| **Package** | 14-pin SOIC / 16-pin QFN (4mm × 4mm) |
| **High-Side Floating Offset ($V_{HS}$)** | Up to $+600\text{ V}$ DC max |
| **Gate Driver Supply Range ($V_{DD}$)** | $5.5\text{ V}$ to $16.0\text{ V}$ DC |
| **Output Peak Current** | $+1.0\text{ A}$ Source / $-1.0\text{ A}$ Sink |
| **Mode Selection (`ST` Pin)** | Low = Dual Independent Inputs (`HI`/`LI`) / High = Single PWM (`HI`) |
| **Logic Thresholds** | TTL/CMOS compatible ($3.3\text{V}$ and $5\text{V}$ logic compatible) |
| **Propagation Delay** | $400\text{ ns}$ typical |
| **Enable Control** | Active-HIGH `EN` input (internal pull-down) |

## Pinout (SOIC-14 Package)

```
        ┌──────────────┐
     EN ─│ 1         14 │─ NC
    VDD ─│ 2         13 │─ ST
     NC ─│ 3  MIC    12 │─ LO
     HB ─│ 4  4608   11 │─ VSS
     HO ─│ 5         10 │─ LI
     HS ─│ 6          9 │─ HI
     NC ─│ 7          8 │─ NC
         └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `EN` | Enable logic input (Active-HIGH: HIGH = Enabled, LOW = Shutdown/Both outputs OFF) |
| 2 | `VDD` | Low-side power supply input (+5.5V to +16.0V DC) |
| 3, 7, 8, 14 | `NC` | No internal connection (High-voltage safety creepage gap) |
| 4 | `HB` | High-side floating bootstrap supply pin |
| 5 | `HO` | High-side gate drive output |
| 6 | `HS` | High-side floating ground return / Half-bridge switching midpoint |
| 9 | `HI` | High-side logic input (Dual mode) / Single PWM input (Single PWM mode) |
| 10 | `LI` | Low-side logic input (Active in Dual mode, ignored in Single PWM mode) |
| 11 | `VSS` | Ground reference / Power ground return |
| 12 | `LO` | Low-side gate drive output |
| 13 | `ST` | Mode selection state input (LOW = Dual independent mode, HIGH = Single PWM mode) |

## Operating Mode Truth Table

### Dual Independent Mode (`ST = LOW`, `EN = HIGH`)

| `HI` | `LI` | `HO` (High-Side Gate) | `LO` (Low-Side Gate) | Bridge State |
|---|---|---|---|---|
| Low (`0`) | Low (`0`) | Low (OFF) | Low (OFF) | Both switches OFF |
| High (`1`) | Low (`0`) | High (ON) | Low (OFF) | High-Side ON |
| Low (`0`) | High (`1`) | Low (OFF) | High (ON) | Low-Side ON |
| High (`1`) | High (`1`) | Low (OFF) | Low (OFF) | **Cross-conduction lockout** (Both OFF) |

### Single PWM Mode (`ST = HIGH`, `EN = HIGH`)

| `HI` (PWM Input) | `HO` (High-Side Gate) | `LO` (Low-Side Gate) | Bridge State |
|---|---|---|---|
| Low (`0`) | Low (OFF) | High (ON) | Low-Side ON |
| High (`1`) | High (ON) | Low (OFF) | High-Side ON |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| High-Side Floating Supply Voltage | $V_{HB}$ | -0.3 | — | 620 | V | Relative to VSS |
| High-Side Floating Offset Voltage | $V_{HS}$ | -5.0 | — | 600 | V | Half-bridge midpoint |
| Supply Voltage | $V_{DD}$ | 5.5 | 12.0 | 16.0 | V | Operating range |
| Peak Output Sourcing Current | $I_{SRC}$ | 0.8 | 1.0 | — | A | $V_{DD} = 12\text{V}$ |
| Peak Output Sinking Current | $I_{SNK}$ | 0.8 | 1.0 | — | A | $V_{DD} = 12\text{V}$ |
| Turn-On / Turn-Off Delay | $t_{on}, t_{off}$| — | 400 | 600 | ns | $C_L = 1000\text{ pF}$ |
| Low-Side Output Rise Time | $t_r$ | — | 20 | 35 | ns | $C_L = 1000\text{ pF}$ |
| Low-Side Output Fall Time | $t_f$ | — | 20 | 35 | ns | $C_L = 1000\text{ pF}$ |
| Quiescent Current | $I_{DD}$ | — | 1.2 | 2.5 | mA | $V_{DD} = 12\text{V}, EN = 1$ |

## Common mistakes

- **Leaving EN floating:** The `EN` pin has an internal $300\text{ k}\Omega$ pull-down resistor. If left unconnected, the IC defaults to shutdown mode. Connect `EN` to logic HIGH ($3.3\text{V}$, $5\text{V}$, or $V_{DD}$) to activate outputs.
- **Ignoring the ST pin state:** Leaving `ST` floating defaults to Dual Mode (`ST = 0`). If intending to drive with a single PWM pin, tie `ST` directly to `VDD` or logic HIGH.
- **Inadequate decoupling on VDD:** Place a $1.0\ \mu\text{F} \dots 2.2\ \mu\text{F}$ low-ESR ceramic capacitor directly between Pin 2 (`VDD`) and Pin 11 (`VSS`).

## Notes

- **Anti-Shoot-Through Logic:** In Dual Mode (`ST = 0`), if both `HI` and `LI` are accidentally asserted HIGH simultaneously by software, internal interlocking circuits immediately force both `HO` and `LO` to LOW, protecting the power bridge from destruction.
