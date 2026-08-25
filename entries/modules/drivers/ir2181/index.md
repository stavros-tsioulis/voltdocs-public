## Overview

The **IR2181** (and lead-free **IR2181PBF** / **IRS2181PBF**) is a high-voltage, high-speed power MOSFET and IGBT half-bridge gate driver IC manufactured by Infineon Technologies (originally International Rectifier). It bridges the gap between ultra-compact 8-pin low-power drivers (such as the IR2101 / IR2103) and bulky 14-pin high-current drivers (such as the IR2110) by delivering a robust **$1.9\text{ A}$ source / $2.3\text{ A}$ sink drive current** directly inside a compact **8-pin PDIP or 8-pin SOIC** package.

Fully operational up to high-side voltages of **$+600\text{ V}$**, the IR2181 features independent high-side (`HIN`) and low-side (`LIN`) logic inputs with Schmitt-trigger inputs compatible down to $3.3\text{V}$ logic levels. It includes matched propagation delays for high-frequency switching, undervoltage lockout on both output channels, and negative transient immunity on the $V_S$ switching pin.

## Quick reference

| | |
|---|---|
| **Driver Type** | High and Low Side Half-Bridge Gate Driver IC |
| **Package** | 8-pin PDIP (IR2181) / 8-pin SOIC (IR2181S) / 14-pin PDIP (IR21814) |
| **High-Side Floating Offset ($V_S$)** | Up to $+600\text{ V}$ DC max |
| **Gate Driver Supply Range ($V_{CC}$)** | $10.0\text{ V}$ to $20.0\text{ V}$ DC |
| **Output Peak Current** | $+1.9\text{ A}$ Source / $-2.3\text{ A}$ Sink peak |
| **Turn-On / Turn-Off Delay** | $t_{on} = 180\text{ ns}$ / $t_{off} = 220\text{ ns}$ typical |
| **Delay Matching** | $\le 40\text{ ns}$ maximum between channels |
| **Logic Compatibility** | $3.3\text{ V}$, $5.0\text{ V}$, and $15.0\text{ V}$ CMOS / LSTTL inputs |
| **Low-Side Input Polarity** | Non-inverting (in-phase: `LIN = 1` turns `LO` ON) |

## Pinout (DIP-8 / SOIC-8 Package)

```
        ┌──────────────┐
    VCC ─│ 1          8 │─ VB
    HIN ─│ 2          7 │─ HO
    LIN ─│ 3          6 │─ VS
    COM ─│ 4          5 │─ LO
        └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `VCC` | Low-side fixed supply voltage and logic supply input (+10V to +20V DC) |
| 2 | `HIN` | Logic input for high-side gate driver output (In-phase with `HO`) |
| 3 | `LIN` | Logic input for low-side gate driver output (In-phase with `LO`) |
| 4 | `COM` | Logic and low-side power ground return |
| 5 | `LO` | Low-side gate drive output (2.3A sink) |
| 6 | `VS` | High-side floating supply return (Half-bridge switching node / MOSFET source) |
| 7 | `HO` | High-side gate drive output (1.9A source) |
| 8 | `VB` | High-side floating bootstrap supply voltage pin |

## Input / Output Logic Truth Table

Both inputs are **in-phase (non-inverting)**:

| `HIN` | `LIN` | `HO` (High-Side Gate) | `LO` (Low-Side Gate) | Bridge State |
|---|---|---|---|---|
| Low (`0`) | Low (`0`) | Low (OFF) | Low (OFF) | **Both MOSFETs OFF** (High-Z midpoint) |
| High (`1`) | Low (`0`) | High (ON) | Low (OFF) | **High-Side ON** (Midpoint pulled to high voltage rail) |
| Low (`0`) | High (`1`) | Low (OFF) | High (ON) | **Low-Side ON** (Midpoint pulled to GND) |
| High (`1`) | High (`1`) | High (ON) | High (ON) | **Shoot-Through Warning** (MCU deadtime required!) |

> [!WARNING]
> Because `HIN` and `LIN` operate independently, asserting both inputs HIGH simultaneously will turn ON both high- and low-side switches. Always program adequate deadtime in microcontroller software or timer peripherals.

## Standard Application Circuit

```
                      +V_BUS High Voltage (Up to 600V DC)
                         │
                         ├───────────┐ [D_BOOT Ultra-Fast]
                         │           │
                         │          ┌┴┐
                         │          │▲│
                         │          └┬┘
                         │           │
                     [Pin 1: VCC]    │
                       IR2181        │
                     [Pin 8: VB] ────┴──────┐
                         │                  │
                     [Pin 7: HO] ─[R_G1]─┐ [C_BOOT 0.1µF-1.0µF]
                         │               │  │
                         │             ┌─┴──┴─┐  [Q1 High-Side N-MOSFET]
                     [Pin 6: VS] ──────┤  S   │
                         │             └──┬───┘
                         │                ├──────────── Half-Bridge Output
                         │                │
                     [Pin 5: LO] ─[R_G2]─┐│
                         │               ││
                         │             ┌─┴┴───┐  [Q2 Low-Side N-MOSFET]
                     [Pin 4: COM] ─────┤  S   │
                         │             └──┬───┘
                        GND               │
                                         GND
```

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| High-Side Floating Supply Voltage | $V_B$ | -0.3 | — | 625 | V | Relative to COM |
| High-Side Floating Offset Voltage | $V_S$ | $V_B - 25$ | — | $V_B + 0.3$ | V | Switching node |
| Low-Side Supply Voltage | $V_{CC}$ | 10.0 | — | 20.0 | V | Operating range |
| Logic High Input Threshold | $V_{IH}$ | 2.7 | — | — | V | $V_{CC} = 10\text{V} \dots 20\text{V}$ |
| Logic Low Input Threshold | $V_{IL}$ | — | — | 0.8 | V | $V_{CC} = 10\text{V} \dots 20\text{V}$ |
| Output High Short-Circuit Current | $I_{O+}$ | 1.4 | 1.9 | — | A | $V_O = 0\text{V}, V_{IN} = \text{High}, PW \le 10\ \mu\text{s}$ |
| Output Low Short-Circuit Current | $I_{O-}$ | 1.8 | 2.3 | — | A | $V_O = 15\text{V}, V_{IN} = \text{Low}, PW \le 10\ \mu\text{s}$ |
| Turn-On Propagation Delay | $t_{on}$ | — | 180 | 270 | ns | $V_S = 0\text{V}$ |
| Turn-Off Propagation Delay | $t_{off}$ | — | 220 | 330 | ns | $V_S = 600\text{V}$ |
| Turn-On Rise Time | $t_r$ | — | 40 | 60 | ns | $C_L = 1000\text{ pF}$ |
| Turn-Off Fall Time | $t_f$ | — | 20 | 35 | ns | $C_L = 1000\text{ pF}$ |

## Common mistakes

- **Assuming IR2181 has inverted LIN like IR2103:** In the IR2103, `~LIN~` is active-LOW. In the IR2181, `LIN` is **active-HIGH (non-inverting)**. Replacing an IR2103 with an IR2181 without updating low-side control logic will invert the low-side gate drive.
- **Negative voltage undershoot on VS during inductive switching:** Fast turn-off of the low-side MOSFET can drive $V_S$ below $COM$ ($< -5\text{V}$). Protect the IC by placing a fast recovery clamping diode from $COM$ to $V_S$ and a $3\ \Omega \dots 10\ \Omega$ series resistor into the $V_S$ pin.
- **Omitting low-ESR ceramic decoupling on VCC:** Sourcing $1.9\text{A}$ pulses into large MOSFET gates requires a low-ESR $1.0\ \mu\text{F} \dots 4.7\ \mu\text{F}$ ceramic capacitor directly across Pin 1 (`VCC`) and Pin 4 (`COM`).

## Notes

- **Comparison with IR2101 / IR2110:** The IR2181 delivers nearly the same drive current as the 14-pin IR2110 ($1.9\text{A}/2.3\text{A}$ vs $2.0\text{A}/2.0\text{A}$) but in a significantly smaller standard 8-pin footprint, making it ideal for compact PCB layouts.
