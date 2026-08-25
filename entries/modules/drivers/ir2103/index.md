## Overview

The **IR2103** (and its modern lead-free counterpart **IRS2103PBF** / **IRS2103STRPBF**) is a high-voltage, high-speed half-bridge power MOSFET and IGBT gate driver IC manufactured by Infineon Technologies (originally International Rectifier). It provides independent high- and low-side referenced output channels designed to drive two N-channel power MOSFETs or IGBTs in half-bridge, synchronous buck, full-bridge inverter, and BLDC motor drive topologies.

The high-side driver features a floating bootstrap channel capable of operating up to **$+600\text{V}$** relative to ground ($COM$), with high immune $dV/dt$ noise tolerance ($50\text{ V/ns}$). The IC incorporates internal cross-conduction prevention logic and matched propagation delays ($520\text{ ns}$ typical internal deadtime) to prevent catastrophic shoot-through current during switching.

## Quick reference

| | |
|---|---|
| **Driver Type** | High and Low Side Half-Bridge Gate Driver IC |
| **Package** | 8-lead PDIP (IR2103) / 8-lead SOIC (IR2103S) |
| **High-Side Floating Offset ($V_S$)** | Up to $+600\text{ V}$ DC max |
| **Gate Driver Supply Range ($V_{CC}$)** | $10.0\text{ V}$ to $20.0\text{ V}$ DC |
| **Output Peak Current** | $+130\text{ mA}$ Source / $-270\text{ mA}$ Sink typical ($+210\text{ mA} / -360\text{ mA}$ test) |
| **Internal Deadtime** | $520\text{ ns}$ typical (prevents shoot-through) |
| **Turn-On / Turn-Off Delay** | $t_{on} = 680\text{ ns}$ / $t_{off} = 150\text{ ns}$ typical |
| **Logic Compatibility** | $3.3\text{ V}$, $5.0\text{ V}$, and $15.0\text{ V}$ CMOS / LSTTL inputs |
| **Low-Side Input Polarity** | Inverted active-LOW ($\overline{LIN} = \text{LOW}$ turns $\text{LO}$ ON) |

## Pinout (DIP-8 / SOIC-8 Package)

```
        ┌──────────────┐
    VCC ─│ 1          8 │─ VB
    HIN ─│ 2          7 │─ HO
  ~LIN~ ─│ 3          6 │─ VS
    COM ─│ 4          5 │─ LO
        └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `VCC` | Low-side fixed supply voltage and logic supply input (+10V to +20V DC) |
| 2 | `HIN` | Logic input for high-side gate driver output (In-phase with `HO`) |
| 3 | `~LIN~` | Logic input for low-side gate driver output (Out-of-phase: active-LOW with `LO`) |
| 4 | `COM` | Logic and low-side power ground return |
| 5 | `LO` | Low-side gate drive output |
| 6 | `VS` | High-side floating supply return (Half-bridge switching node / MOSFET source) |
| 7 | `HO` | High-side gate drive output |
| 8 | `VB` | High-side floating bootstrap supply voltage pin |

## Input / Output Logic Truth Table

The low-side input (`~LIN~`) is **active-LOW**, making complementary driving with a single MCU PWM pin straightforward:

| `HIN` | `~LIN~` | `HO` (High-Side Gate) | `LO` (Low-Side Gate) | Bridge State |
|---|---|---|---|---|
| Low (`0`) | High (`1`) | Low (OFF) | Low (OFF) | **Both MOSFETs OFF** (High-Z midpoint) |
| High (`1`) | High (`1`) | High (ON) | Low (OFF) | **High-Side ON** (Midpoint pulled to high voltage rail) |
| Low (`0`) | Low (`0`) | Low (OFF) | High (ON) | **Low-Side ON** (Midpoint pulled to GND) |
| High (`1`) | Low (`0`) | Low (OFF) | Low (OFF) | **Shoot-through prevention** (Both outputs forced OFF) |

## Standard Half-Bridge Application Circuit

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
                       IR2103        │
                     [Pin 8: VB] ────┴──────┐
                         │                  │
                     [Pin 7: HO] ─[R_G1]─┐ [C_BOOT 0.1µF-1.0µF]
                         │               │  │
                         │             ┌─┴──┴─┐  [Q1 High-Side N-MOSFET]
                     [Pin 6: VS] ──────┤  S   │
                         │             └──┬───┘
                         │                ├──────────── Output / Motor / Inductor
                         │                │
                     [Pin 5: LO] ─[R_G2]─┐│
                         │               ││
                         │             ┌─┴┴───┐  [Q2 Low-Side N-MOSFET]
                     [Pin 4: COM] ─────┤  S   │
                         │             └──┬───┘
                        GND               │
                                         GND
```

- **Bootstrap Diode ($D_{BOOT}$):** Must be an ultra-fast recovery diode (such as UF4007 or ES1J) rated for the full high-voltage bus ($V_{BUS} + 20\%$).
- **Bootstrap Capacitor ($C_{BOOT}$):** Low-ESR ceramic capacitor ($0.1\ \mu\text{F} \dots 1.0\ \mu\text{F}$, $\ge 25\text{V}$) charged when `LO` is active and $V_S$ is pulled to ground.

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| High-Side Floating Supply Voltage | $V_B$ | -0.3 | — | 625 | V | Relative to COM |
| High-Side Floating Offset Voltage | $V_S$ | $V_B - 25$ | — | $V_B + 0.3$ | V | Switching node |
| Low-Side Supply Voltage | $V_{CC}$ | 10.0 | — | 20.0 | V | Operating range |
| Logic High Input Threshold | $V_{IH}$ | 2.7 | — | — | V | $V_{CC} = 10\text{V} \dots 20\text{V}$ |
| Logic Low Input Threshold | $V_{IL}$ | — | — | 0.8 | V | $V_{CC} = 10\text{V} \dots 20\text{V}$ |
| Output High Short-Circuit Current | $I_{O+}$ | 130 | 210 | — | mA | $V_O = 0\text{V}, V_{IN} = \text{High}, PW \le 10\ \mu\text{s}$ |
| Output Low Short-Circuit Current | $I_{O-}$ | 270 | 360 | — | mA | $V_O = 15\text{V}, V_{IN} = \text{Low}, PW \le 10\ \mu\text{s}$ |
| Turn-On Propagation Delay | $t_{on}$ | — | 680 | 820 | ns | $V_S = 0\text{V}$ |
| Turn-Off Propagation Delay | $t_{off}$ | — | 150 | 220 | ns | $V_S = 600\text{V}$ |
| Deadtime | $DT$ | 400 | 520 | 650 | ns | Internal matched delay |

## Common mistakes

- **Forgetting that `~LIN~` is inverted:** Unlike drivers with active-high inputs on both channels (like IR2101), the IR2103 requires `~LIN~` to be driven **LOW** to turn on the low-side gate (`LO`). If connected to a standard active-high MCU pin without inverting logic, the low-side switch will remain continuously ON.
- **Operating at 100% High-Side Duty Cycle:** The floating bootstrap capacitor ($C_{BOOT}$) charges only when the switching node ($V_S$) is grounded by the low-side MOSFET. Continuous DC high-side conduction without periodic low-side switching causes the bootstrap capacitor to discharge, causing high-side gate drive failure via undervoltage lockout.
- **Using a standard rectifier diode for bootstrap:** A slow 1N4007 diode cannot reverse-recover fast enough during high-frequency switching ($> 20\text{ kHz}$), leading to massive reverse recovery current into the $V_{CC}$ rail and diode destruction. Always use an ultra-fast recovery diode ($t_{rr} < 75\text{ ns}$) like UF4007 or MUR120.
- **Negative voltage transients on `VS`:** Inductive switching can pull $V_S$ below $COM$ ground ($< -5\text{V}$), which can latch up the internal CMOS substrate. Add a low-forward-drop Schottky diode from $COM$ to $V_S$ and a small resistor ($3\ \Omega \dots 10\ \Omega$) in series with $V_S$.

## Notes

- **Drop-in Sibling (IR2104):** The **IR2104** uses the same 8-pin package but features a single input (`IN`) and an active-low shutdown (`~SD~`) pin instead of split `HIN` / `~LIN~` inputs.
