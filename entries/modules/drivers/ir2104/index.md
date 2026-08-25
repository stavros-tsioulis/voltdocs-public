## Overview

The **IR2104** (and modern lead-free **IRS2104PBF** / **IRS2104STRPBF**) is a high-voltage, high-speed half-bridge power MOSFET and IGBT gate driver IC manufactured by Infineon Technologies (originally International Rectifier). It is the single-input, shutdown-enabled companion to the IR2103, designed to drive a complementary high- and low-side N-channel MOSFET pair in half-bridge converters, motor drivers, DC-DC buck stages, and class-D audio amplifiers.

Unlike dual-input drivers, the IR2104 accepts a **single logic input (`IN`)** that automatically drives high-side (`HO`) and low-side (`LO`) outputs in complementary antiphase, with internal cross-conduction shoot-through protection and a fixed **$520\text{ ns}$ internal deadtime**. An active-LOW shutdown pin (`~SD~`) allows instantly turning off both outputs to put the half-bridge in a high-impedance coast state.

## Quick reference

| | |
|---|---|
| **Driver Type** | High and Low Side Half-Bridge Gate Driver IC |
| **Package** | 8-lead PDIP (IR2104) / 8-lead SOIC (IR2104S) |
| **High-Side Floating Offset ($V_S$)** | Up to $+600\text{ V}$ DC max |
| **Gate Driver Supply Range ($V_{CC}$)** | $10.0\text{ V}$ to $20.0\text{ V}$ DC |
| **Output Peak Current** | $+130\text{ mA}$ Source / $-270\text{ mA}$ Sink typical ($+210\text{ mA} / -360\text{ mA}$ test) |
| **Internal Deadtime** | $520\text{ ns}$ typical (built-in shoot-through protection) |
| **Turn-On / Turn-Off Delay** | $t_{on} = 680\text{ ns}$ / $t_{off} = 150\text{ ns}$ typical |
| **Shutdown Delay** | $t_{sd} = 160\text{ ns}$ typical |
| **Logic Compatibility** | $3.3\text{ V}$, $5.0\text{ V}$, and $15.0\text{ V}$ CMOS / LSTTL inputs |
| **Control Style** | Single PWM input (`IN`) + Active-LOW Enable/Shutdown (`~SD~`) |

## Pinout (DIP-8 / SOIC-8 Package)

```
        ┌──────────────┐
    VCC ─│ 1          8 │─ VB
     IN ─│ 2          7 │─ HO
   ~SD~ ─│ 3          6 │─ VS
    COM ─│ 4          5 │─ LO
        └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `VCC` | Low-side fixed supply voltage and logic supply input (+10V to +20V DC) |
| 2 | `IN` | Single logic input for complementary gate drive (Controls HO and LO) |
| 3 | `~SD~` | Active-LOW shutdown control input (LOW = Shutdown/Both OFF, HIGH = Enabled) |
| 4 | `COM` | Logic and low-side power ground return |
| 5 | `LO` | Low-side gate drive output |
| 6 | `VS` | High-side floating supply return (Half-bridge switching node / MOSFET source) |
| 7 | `HO` | High-side gate drive output |
| 8 | `VB` | High-side floating bootstrap supply voltage pin |

## Input / Output Logic Truth Table

| `~SD~` (Shutdown) | `IN` (Input) | `HO` (High-Side Gate) | `LO` (Low-Side Gate) | Half-Bridge State |
|---|---|---|---|---|
| Low (`0`) | X (Don't Care) | Low (OFF) | Low (OFF) | **Shutdown / High-Z** (Both switches OFF) |
| High (`1`) | Low (`0`) | Low (OFF) | High (ON) | **Low-Side ON** (Midpoint pulled to GND) |
| High (`1`) | High (`1`) | High (ON) | Low (OFF) | **High-Side ON** (Midpoint pulled to VBUS) |

> [!NOTE]
> Transitions between `IN = 0` and `IN = 1` enforce an internal $520\text{ ns}$ deadtime during which both `HO` and `LO` are held LOW, preventing simultaneous conduction.

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
                       IR2104        │
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

- **Bootstrap Diode ($D_{BOOT}$):** Ultra-fast recovery diode ($t_{rr} < 50\text{ ns}$, e.g. UF4007 or ES1J) rated for $\ge V_{BUS} \times 1.2$.
- **Bootstrap Capacitor ($C_{BOOT}$):** Ceramic or low-ESR film capacitor ($0.1\ \mu\text{F} \dots 1.0\ \mu\text{F}$, $\ge 25\text{V}$) recharged every cycle when `LO` conducts and $V_S$ drops to ground.

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
| Shutdown Propagation Delay | $t_{sd}$ | — | 160 | 220 | ns | $V_S = 600\text{V}$ |
| Deadtime | $DT$ | 400 | 520 | 650 | ns | Internal matched delay |

## Common mistakes

- **Leaving ~SD~ floating:** Pin 3 (`~SD~`) has an internal pull-down resistor. If left unconnected, the driver remains in permanent shutdown with both outputs disabled. Pull `~SD~` to logic HIGH ($3.3\text{V}$ or $5\text{V}$) to enable the driver.
- **Attempting 100% High-Side Duty Cycle ($IN = 1$ static):** The bootstrap capacitor only charges when the low-side switch is ON ($IN = 0$). Holding `IN = 1` continuously will cause $V_B - V_S$ to decay below the undervoltage threshold ($UVLO \approx 8.2\text{V}$), turning off `HO`.
- **Using slow silicon rectifier diodes for bootstrap:** Standard diodes (1N4001–1N4007) take microseconds to turn off, feeding high-voltage bus energy backwards into $V_{CC}$ during $V_S$ rising edges. Always use ultra-fast or SiC Schottky diodes.

## Notes

- **Comparison with IR2103:** The IR2103 provides separate inputs for high-side (`HIN`) and low-side (`~LIN~`) channels, allowing independent asymmetric duty cycles, whereas the IR2104 simplifies microcontroller drive by using a single PWM line (`IN`) with a dedicated shutdown line (`~SD~`).
