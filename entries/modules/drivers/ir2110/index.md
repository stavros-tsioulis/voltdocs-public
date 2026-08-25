## Overview

The **IR2110** (and lead-free **IR2110PBF** / **IRS2110PBF**) is the industry-standard high-voltage, high-speed power MOSFET and IGBT half-bridge driver IC originally pioneered by International Rectifier (now Infineon Technologies). Packaged in a 14-pin PDIP or 16-pin wide SOIC, it features independent high- and low-side referenced output channels capable of driving half-bridges up to **$+500\text{V}$** with **$2.0\text{A}$ peak sourcing and $2.0\text{A}$ peak sinking** drive capability.

A key design feature of the IR2110 is its separate logic supply rail (`VDD`) and separate logic ground (`VSS`), allowing the IC's input stages to interface seamlessly with $3.3\text{V}$ and $5\text{V}$ CMOS or LSTTL microcontrollers while output gate stages switch between $10\text{V}$ and $20\text{V}$. Propagation delays are matched down to $10\text{ ns}$, making the IR2110 the classic driver of choice for induction heaters, Tesla coils, full-bridge DC-DC converters, motor inverters, and switch-mode audio amplifiers.

## Quick reference

| | |
|---|---|
| **Driver Type** | High and Low Side Half-Bridge Gate Driver IC |
| **Package** | 14-pin PDIP / 16-pin wide SOIC |
| **High-Side Floating Offset ($V_S$)** | Up to $+500\text{ V}$ DC max |
| **Gate Driver Supply Range ($V_{CC}$)** | $10.0\text{ V}$ to $20.0\text{ V}$ DC |
| **Logic Supply Range ($V_{DD}$)** | $3.3\text{ V}$ to $20.0\text{ V}$ DC ($3.3\text{V}$ / $5\text{V}$ logic compatible) |
| **Peak Output Current** | $+2.0\text{ A}$ Source / $-2.0\text{ A}$ Sink |
| **Turn-On / Turn-Off Delay** | $t_{on} = 120\text{ ns}$ / $t_{off} = 94\text{ ns}$ typical |
| **Delay Matching** | $10\text{ ns}$ typical between high and low channels |
| **Shutdown Input** | Dedicated active-HIGH shutdown (`SD`) pin |

## Pin Configuration (14-Pin PDIP Package)

```
         ┌──────────────┐
     LO ─│ 1         14 │─ NC
    COM ─│ 2         13 │─ VSS
    VCC ─│ 3         12 │─ LIN
     NC ─│ 4  IR     11 │─ SD
     VS ─│ 5  2110   10 │─ HIN
     VB ─│ 6          9 │─ VDD
     HO ─│ 7          8 │─ NC
         └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `LO` | Low-side gate drive output (2.0A peak) |
| 2 | `COM` | Low-side power ground return |
| 3 | `VCC` | Low-side driver supply input (+10V to +20V DC) |
| 4, 8, 14 | `NC` | No connection (Provides high-voltage safety creepage gap) |
| 5 | `VS` | High-side floating supply return (Half-bridge midpoint) |
| 6 | `VB` | High-side floating bootstrap supply voltage pin |
| 7 | `HO` | High-side gate drive output (2.0A peak) |
| 9 | `VDD` | Logic supply input (+3.3V to +15V, references VSS) |
| 10 | `HIN` | Logic input for high-side gate driver (In-phase with `HO`) |
| 11 | `SD` | Logic input for shutdown (Active-HIGH: HIGH = Both outputs OFF) |
| 12 | `LIN` | Logic input for low-side gate driver (In-phase with `LO`) |
| 13 | `VSS` | Logic ground return (Connects to MCU ground) |

## Control Logic Truth Table

Inputs `HIN` and `LIN` operate independently:

| `HIN` | `LIN` | `SD` (Shutdown) | `HO` (High-Side Gate) | `LO` (Low-Side Gate) | Bridge State |
|---|---|---|---|---|---|
| X | X | High (`1`) | Low (OFF) | Low (OFF) | **Shutdown (Both OFF)** |
| Low (`0`) | Low (`0`) | Low (`0`) | Low (OFF) | Low (OFF) | **Both MOSFETs OFF** |
| High (`1`) | Low (`0`) | Low (`0`) | High (ON) | Low (OFF) | **High-Side ON** |
| Low (`0`) | High (`1`) | Low (`0`) | Low (OFF) | High (ON) | **Low-Side ON** |
| High (`1`) | High (`1`) | Low (`0`) | High (ON) | High (ON) | **Shoot-through** (Microcontroller deadtime required!) |

> [!WARNING]
> The IR2110 does **not** feature internal cross-conduction prevention. Setting `HIN = 1` and `LIN = 1` simultaneously will turn ON both bridge MOSFETs, causing a dead short across the power rail. Generate deadtime in software.

## Standard Application Circuit

```
                      +V_BUS High Voltage (Up to 500V DC)
                         │
                         ├───────────┐ [D_BOOT Ultra-Fast]
                         │           │
                         │          ┌┴┐
                         │          │▲│
                         │          └┬┘
                         │           │
                     [Pin 3: VCC]    │
                       IR2110        │
                     [Pin 6: VB] ────┴──────┐
                         │                  │
                     [Pin 7: HO] ─[R_G1]─┐ [C_BOOT 0.1µF-1.0µF]
                         │               │  │
                         │             ┌─┴──┴─┐  [Q1 High-Side N-MOSFET]
                     [Pin 5: VS] ──────┤  S   │
                         │             └──┬───┘
                         │                ├──────────── Half-Bridge Output
                         │                │
                     [Pin 1: LO] ─[R_G2]─┐│
                         │               ││
                         │             ┌─┴┴───┐  [Q2 Low-Side N-MOSFET]
                     [Pin 2: COM] ─────┤  S   │
                         │             └──┬───┘
                        GND               │
                                         GND
```

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| High-Side Floating Supply Voltage | $V_B$ | -0.3 | — | 525 | V | Relative to COM |
| High-Side Floating Offset Voltage | $V_S$ | $V_B - 25$ | — | $V_B + 0.3$ | V | Switching node |
| Low-Side Supply Voltage | $V_{CC}$ | 10.0 | 15.0 | 20.0 | V | Operating range |
| Logic Supply Voltage | $V_{DD}$ | 3.3 | 5.0 | 20.0 | V | Operating range |
| Peak Output Sourcing Current | $I_{O+}$ | — | 2.0 | — | A | $V_O = 0\text{V}, V_{IN} = \text{High}, PW \le 10\ \mu\text{s}$ |
| Peak Output Sinking Current | $I_{O-}$ | — | 2.0 | — | A | $V_O = 15\text{V}, V_{IN} = \text{Low}, PW \le 10\ \mu\text{s}$ |
| Turn-On Propagation Delay | $t_{on}$ | — | 120 | 150 | ns | $V_S = 0\text{V}$ |
| Turn-Off Propagation Delay | $t_{off}$ | — | 94 | 125 | ns | $V_S = 500\text{V}$ |
| Turn-On Rise Time | $t_r$ | — | 25 | 35 | ns | $C_L = 1000\text{ pF}$ |
| Turn-Off Fall Time | $t_f$ | — | 17 | 25 | ns | $C_L = 1000\text{ pF}$ |

## Common mistakes

- **Leaving VDD floating or tying to 12V with 3.3V/5V MCU:** Pin 9 (`VDD`) powers the logic threshold comparators. Connect `VDD` directly to your MCU's supply ($3.3\text{V}$ or $5.0\text{V}$). Tying `VDD` to $12\text{V}$ or $15\text{V}$ sets the logic HIGH threshold to $9.5\text{V}$, preventing $3.3\text{V}$ microcontrollers from triggering the inputs.
- **Leaving SD floating:** Pin 11 (`SD`) has an internal pull-down resistor, but in high-noise environments (motor switching), noise pickup can trigger spurious shutdowns. Tie `SD` directly to `VSS` (Ground) if unused.
- **Undersized bootstrap capacitor for low switching frequencies:** At frequencies below $10\text{ kHz}$, the gate charge of large power MOSFETs will deplete a small $100\text{ nF}$ capacitor. Use a $1.0\ \mu\text{F} \dots 4.7\ \mu\text{F}$ low-ESR ceramic capacitor for low-frequency PWM.

## Notes

- **High-Voltage Variant (IR2113):** The **IR2113** is the $600\text{V}$ rated identical drop-in companion to the $500\text{V}$ rated IR2110.
