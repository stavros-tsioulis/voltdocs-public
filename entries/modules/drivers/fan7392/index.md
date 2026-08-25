## Overview

The **FAN7392** (available in 14-pin PDIP **FAN7392N** and 16-pin wide SOIC **FAN7392M**) is a high-current, monolithic high- and low-side gate driver IC manufactured by ON Semiconductor (originally Fairchild Semiconductor). Capable of operating at floating high-side voltages up to **$+600\text{V}$**, it provides an industry-leading **$\pm 3.0\text{A}$ peak drive current** ($3.0\text{A}$ source / $3.0\text{A}$ sink) with unmatched high-speed propagation delays ($130\text{ ns}$ turn-on).

Designed to serve as a direct high-power upgrade over legacy IR2110 drivers, the FAN7392 integrates proprietary high-voltage common-mode $dV/dt$ noise cancellation circuitry (immune to up to $50\text{ V/ns}$ transients), independent undervoltage lockout (UVLO) for both high- and low-side channels, cycle-by-cycle shutdown (`SD`) logic, and separated logic ground (`VSS`) and power ground (`COM`) for superior noise immunity in induction heaters, pure sine wave solar inverters, high-power DC motor drives, and SMPS power converters.

## Quick reference

| | |
|---|---|
| **Driver Type** | High and Low Side Half-Bridge Gate Driver IC |
| **Package** | 14-pin PDIP (FAN7392N) / 16-pin wide SOP (FAN7392M) |
| **High-Side Floating Offset ($V_S$)** | Up to $+600\text{ V}$ DC max |
| **Gate Driver Supply Range ($V_{CC}$)** | $10.0\text{ V}$ to $20.0\text{ V}$ DC |
| **Logic Supply Range ($V_{DD}$)** | $3.0\text{ V}$ to $20.0\text{ V}$ ($3.3\text{V}$ / $5\text{V}$ logic compatible) |
| **Output Peak Current** | $+3.0\text{ A}$ Source / $-3.0\text{ A}$ Sink peak |
| **Turn-On / Turn-Off Delay** | $t_{on} = 130\text{ ns}$ / $t_{off} = 150\text{ ns}$ typical |
| **Delay Matching** | $\le 25\text{ ns}$ maximum between channels |
| **Protection Features** | High- & Low-Side UVLO, Logic Shutdown (`SD`), $dV/dt$ noise immunity |

## Pin Configuration (14-Pin PDIP Package)

```
         ┌──────────────┐
     LO ─│ 1         14 │─ NC
    COM ─│ 2         13 │─ VSS
    VCC ─│ 3         12 │─ LIN
     NC ─│ 4  FAN    11 │─ SD
     VS ─│ 5  7392N  10 │─ HIN
     VB ─│ 6          9 │─ VDD
     HO ─│ 7          8 │─ NC
         └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `LO` | Low-side gate drive output (3.0A source/sink) |
| 2 | `COM` | Low-side power ground return / switching ground |
| 3 | `VCC` | Low-side gate drive supply voltage (+10V to +20V DC) |
| 4, 8, 14 | `NC` | No connection (Provides high-voltage creepage spacing) |
| 5 | `VS` | High-side floating supply offset / Half-bridge switching node |
| 6 | `VB` | High-side floating bootstrap supply voltage |
| 7 | `HO` | High-side gate drive output (3.0A source/sink) |
| 9 | `VDD` | Logic supply voltage (+3.3V to +15V, references VSS) |
| 10 | `HIN` | Logic input for high-side gate driver (In-phase with `HO`) |
| 11 | `SD` | Logic input for shutdown (Active-HIGH: HIGH = Both outputs OFF) |
| 12 | `LIN` | Logic input for low-side gate driver (In-phase with `LO`) |
| 13 | `VSS` | Logic ground return (Connects to microcontroller ground) |

## Control Logic Truth Table

Both `HIN` and `LIN` inputs are **non-inverting (in-phase)** with high noise threshold Schmitt triggers:

| `HIN` | `LIN` | `SD` (Shutdown) | `HO` (High-Side Gate) | `LO` (Low-Side Gate) | Bridge State |
|---|---|---|---|---|---|
| X | X | High (`1`) | Low (OFF) | Low (OFF) | **Shutdown (Both OFF)** |
| Low (`0`) | Low (`0`) | Low (`0`) | Low (OFF) | Low (OFF) | **Both MOSFETs OFF** |
| High (`1`) | Low (`0`) | Low (`0`) | High (ON) | Low (OFF) | **High-Side ON** |
| Low (`0`) | High (`1`) | Low (`0`) | Low (OFF) | High (ON) | **Low-Side ON** |
| High (`1`) | High (`1`) | Low (`0`) | High (ON) | High (ON) | **Simultaneous ON** (External deadtime required) |

> [!WARNING]
> Unlike drivers with internal cross-conduction lockouts, the FAN7392 permits independent control of both channels. Driving both `HIN = 1` and `LIN = 1` simultaneously will turn ON both high- and low-side switches. Always generate software deadtime in your microcontroller PWM generator.

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| High-Side Floating Supply Voltage | $V_B$ | -0.3 | — | 625 | V | Relative to COM |
| High-Side Floating Offset Voltage | $V_S$ | $V_B - 25$ | — | $V_B + 0.3$ | V | Half-bridge midpoint |
| Low-Side Supply Voltage | $V_{CC}$ | 10.0 | 15.0 | 20.0 | V | Operating range |
| Logic Supply Voltage | $V_{DD}$ | 3.0 | 5.0 | 20.0 | V | Operating range |
| Peak Output Sourcing Current | $I_{O+}$ | 2.5 | 3.0 | — | A | $V_O = 0\text{V}, V_{IN} = \text{High}, PW \le 10\ \mu\text{s}$ |
| Peak Output Sinking Current | $I_{O-}$ | 2.5 | 3.0 | — | A | $V_O = 15\text{V}, V_{IN} = \text{Low}, PW \le 10\ \mu\text{s}$ |
| Turn-On Propagation Delay | $t_{on}$ | 90 | 130 | 180 | ns | $V_S = 0\text{V}, C_L = 1000\text{ pF}$ |
| Turn-Off Propagation Delay | $t_{off}$ | 100 | 150 | 200 | ns | $V_S = 600\text{V}, C_L = 1000\text{ pF}$ |
| Turn-On Rise Time | $t_r$ | — | 25 | 50 | ns | $C_L = 1000\text{ pF}$ |
| Turn-Off Fall Time | $t_f$ | — | 20 | 45 | ns | $C_L = 1000\text{ pF}$ |

## Common mistakes

- **Leaving VDD unconnected or tied directly to VCC without level considerations:** Pin 9 (`VDD`) powers the input logic buffers. When driving from a $3.3\text{V}$ or $5\text{V}$ MCU, connect `VDD` to the MCU's $3.3\text{V} / 5\text{V}$ rail and `VSS` to MCU Ground. If tied directly to $15\text{V}$ $V_{CC}$, input switching thresholds will rise to $\approx 9.5\text{V}$, ignoring 3.3V/5V MCU GPIO signals.
- **Forgetting external deadtime in microcontroller PWM code:** Since the FAN7392 does not enforce internal cross-conduction interlocking, complementary PWM channels must be configured with hardware deadband (typically $300\text{ ns} \dots 500\text{ ns}$) in the MCU timer peripherals.
- **Connecting COM and VSS over noisy ground traces:** `COM` carries multi-ampere MOSFET gate return pulses, while `VSS` is the sensitive logic ground. Tie `COM` and `VSS` together only at a single star-ground point near the power supply.

## Notes

- **Drop-in Equivalent to IR2110:** The FAN7392 shares the exact 14-DIP / 16-SOIC footprint as the IR2110 / IR2113 while providing higher current capability ($3.0\text{A}$ vs $2.0\text{A}$) and lower propagation delay.
