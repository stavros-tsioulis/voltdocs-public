## Overview

The **TC4429** (TC4429CPA) is a single, high-speed, inverting MOSFET and IGBT gate driver integrated circuit manufactured by Microchip Technology (originally TelCom Semiconductor). It is the direct inverting functional companion to the TC4420, capable of sourcing and sinking up to **$6.0\text{ A}$ peak** current to rapidly charge and discharge heavy power MOSFET gate capacitances across a supply range of **$4.5\text{ V}$ to $18.0\text{ V}$**.

With identical high-speed switching dynamics—**$25\text{ ns}$ rise and fall times** into a $2500\text{ pF}$ load and propagation delays under **$55\text{ ns}$**—the TC4429 is widely utilized to drive P-channel high-side MOSFET gates (where driving the gate LOW turns the transistor ON), push-pull pulse transformers, resonant inverter stages, and complementary power stages when paired alongside the non-inverting TC4420. It features built-in latch-up protection against reverse inductive currents exceeding $1.5\text{ A}$ and tolerates negative input swings down to $-5\text{ V}$.

## Quick reference

| | |
|---|---|
| **Driver Type** | High-Current Inverting Low-Side / P-Channel Gate Driver |
| **Output Configuration** | Inverting (`IN` = HIGH $\rightarrow$ `OUTPUT` = LOW) |
| **Supply Voltage Range ($V_{DD}$)** | $4.5\text{ V}$ to $18.0\text{ V}$ DC ($20\text{ V}$ absolute max) |
| **Peak Output Current** | $6.0\text{ A}$ peak (Source / Sink) |
| **Rise / Fall Time ($t_r / t_f$)** | $25\text{ ns}$ typical ($C_L = 2500\text{ pF}$) |
| **Propagation Delay ($t_{D1} / t_{D2}$)** | $55\text{ ns}$ typical ($C_L = 2500\text{ pF}$) |
| **Output Impedance ($R_{OUT}$)** | $2.5\,\Omega$ high-state / $1.5\,\Omega$ low-state typical |
| **Input Logic Thresholds** | TTL/CMOS compatible with internal hysteresis ($V_{IH} = 2.4\text{V}, V_{IL} = 0.8\text{V}$) |
| **Reverse Current Latch-Up Immunity** | Withstands $> 1.5\text{ A}$ reverse inductive kickback |
| **Packages** | 8-pin DIP (CPA), SOIC-8 (COA/EOA), 5-pin TO-220 (CAT) |

## Pin configuration

### 8-Pin DIP / SOIC Package

```
             ┌───┴───┐
        VDD 1│ 1   8 │ VDD (Supply Voltage)
         IN 2│       │ 7 ~OUTPUT~ (Inverting Gate Drive)
         NC 3│ TC4429│ 6 ~OUTPUT~ (Inverting Gate Drive)
        GND 4│       │ 5 GND (Ground)
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1, 8 | `VDD` | Power Supply | Positive supply voltage ($+4.5\text{ V}$ to $+18.0\text{ V}$); tie together on PCB |
| 2 | `IN` | Digital Input | Inverting logic input; tolerant of inputs from $-5\text{ V}$ to $V_{DD} + 0.3\text{ V}$ |
| 3 | `NC` | Unconnected | No internal connection |
| 4, 5 | `GND` | Power / Ground | System ground reference; tie together on PCB |
| 6, 7 | `~OUTPUT~` | Power Output | High-current inverting gate drive output; tie together on PCB |

> [!NOTE]
> Like the TC4420, pins 1 and 8 (`VDD`), pins 4 and 5 (`GND`), and pins 6 and 7 (`~OUTPUT~`) must be connected in parallel on the circuit board to ensure minimal parasitic inductance and maximum current throughput.

## Functional description

### Truth Table

| Input (`IN`) | Output (`~OUTPUT~`) | Operating Mode |
|---|---|---|
| **`LOW`** ($< 0.8\text{ V}$) | **`HIGH`** ($\approx V_{DD}$) | High-side pull-up active (drives output to $V_{DD}$) |
| **`HIGH`** ($> 2.4\text{ V}$) | **`LOW`** ($\approx 0\text{ V}$) | Low-side pull-down active (discharges output to GND) |

### Complementary Operation with TC4420

When constructing half-bridge or push-pull converters, pairing one TC4420 (non-inverting) with one TC4429 (inverting) allows complementary high- and low-side switching signals to be generated from a single PWM command line (with appropriate deadtime delay networks to prevent cross-conduction shoot-through).

## Absolute maximum ratings

> [!WARNING]
> Stresses beyond these ratings cause permanent destruction. Input voltage must remain between $-5.0\text{ V}$ and $V_{DD} + 0.3\text{ V}$.

| Parameter | Symbol | Min | Max | Unit |
|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | — | $+20.0$ | V |
| Input Voltage | $V_{IN}$ | $-5.0$ | $V_{DD} + 0.3$ | V |
| Input Current ($V_{IN} > V_{DD}$) | $I_{IN}$ | — | $50$ | mA |
| Power Dissipation ($T_A \le 70^\circ\text{C}$, DIP-8) | $P_D$ | — | $730$ | mW |
| Operating Temperature Range | $T_A$ | $-40$ | $+85$ | °C |
| Storage Temperature Range | $T_{stg}$ | $-65$ | $+150$ | °C |

## Electrical characteristics

($4.5\text{ V} \le V_{DD} \le 18\text{ V}, T_A = 25^\circ\text{C}$ unless otherwise noted)

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Logic High Input Voltage | $V_{IH}$ | 2.4 | 1.8 | — | V | — |
| Logic Low Input Voltage | $V_{IL}$ | — | 1.3 | 0.8 | V | — |
| Input Current | $I_{IN}$ | $-10$ | — | $+10$ | µA | $0\text{ V} \le V_{IN} \le V_{DD}$ |
| High Output Voltage | $V_{OH}$ | $V_{DD} - 0.025$ | — | — | V | DC test, no load |
| Low Output Voltage | $V_{OL}$ | — | — | 0.025 | V | DC test, no load |
| Output Resistance (High) | $R_{OH}$ | — | 2.5 | 3.5 | Ω | $I_{OUT} = 10\text{ mA}, V_{DD} = 18\text{ V}$ |
| Output Resistance (Low) | $R_{OL}$ | — | 1.5 | 2.5 | Ω | $I_{OUT} = 10\text{ mA}, V_{DD} = 18\text{ V}$ |
| Peak Output Current | $I_{PK}$ | — | 6.0 | — | A | $V_{DD} = 18\text{ V}$ |
| Rise Time | $t_r$ | — | 25 | 35 | ns | $C_L = 2500\text{ pF}, V_{DD} = 18\text{ V}$ |
| Fall Time | $t_f$ | — | 25 | 35 | ns | $C_L = 2500\text{ pF}, V_{DD} = 18\text{ V}$ |
| Propagation Delay 1 | $t_{D1}$ | — | 55 | 75 | ns | $C_L = 2500\text{ pF}, V_{DD} = 18\text{ V}$ |
| Propagation Delay 2 | $t_{D2}$ | — | 55 | 75 | ns | $C_L = 2500\text{ pF}, V_{DD} = 18\text{ V}$ |
| Quiescent Power Supply Current | $I_S$ | — | 0.45 | 1.5 | mA | $V_{IN} = 0\text{ V}, V_{DD} = 18\text{ V}$ |

## Typical application circuit: High-Side P-Channel MOSFET Driver

Because P-channel power MOSFETs require their gates to be pulled LOW to turn ON, the inverting logic of the TC4429 simplifies high-side load switching from active-high microcontroller control signals.

```
       +12V Power Bus (VDD)
       ────────────────────────┬──────────────────────────────────────────┬─────── +12V
                               │                                          │
                             ┌─┴──┐ 4.7µF                              ┌──┴──┐ Source
                             │    │ Tantalum                           │ Q1  │ PMOS (IRF9540)
                             └─┬──┘                                  ┌─┴─────┴─┐
                               │                                     │ Gate    │
                             ┌─┴──┐ 0.1µF                            │         │
                             │    │ Ceramic (MLCC)                   └──┬───┬──┘
                             └─┬──┘                                     │   │ Drain
                               │                                        │   │
                               ├───────────────────────┬─────────┐      │   ├───> Switched +12V
                               │                       │         │      │   │     Load Output
                             ┌─┴──┐                  ┌─┴──┐      │      │   │
                             │ 1  │(VDD)             │ 8  │(VDD) │     ┌┴┐  │
                             │    └──────────────────┘    │      │     │ │  │
                             │                            │      │     │ │10k
       Microcontroller       │           TC4429           │      │     └┬┘  │
     ┌─────────────────┐     │                            │      │      │   │
     │      Enable OUT ┼─────┤ 2 (IN)            (~OUT) 7 ├──┬───┼──────┴───┘
     │   (HIGH = ON)   │     │                   (~OUT) 6 ├──┘   │ Rg (10Ω)
     │                 │     │ 4 (GND)            5 (GND) │      │
     │             GND ┼─────┴───┬───────────────────┬────┘      │
     └─────────────────┘         │                   │           │
                               ┌─┴───────────────────┴───────────┴───┐
                               │             Power Ground            │
                               │                 GND                 │
                               └─────────────────────────────────────┘
```

### Operation
When the microcontroller outputs a logic **`HIGH`** on `Enable OUT`, the TC4429 output swings **`LOW`** to ground, pulling the P-channel gate $12\text{ V}$ below its source ($V_{GS} = -12\text{ V}$) and driving $Q_1$ into hard saturation. When `Enable OUT` goes **`LOW`**, the TC4429 drives the gate back to $+12\text{ V}$ ($V_{GS} = 0\text{ V}$), cleanly turning the transistor OFF.

## Design considerations & common mistakes

- **Power Decoupling Proximity:** Just like the TC4420, the TC4429 draws instantaneous $6.0\text{ A}$ current pulses from $V_{DD}$. Solder a $4.7\,\mu\text{F} \dots 10\,\mu\text{F}$ low-ESR capacitor in parallel with a $0.1\,\mu\text{F}$ ceramic capacitor immediately across pins 1/8 and 4/5.
- **Power-On Output State:** When power is first applied, if the input pin (pin 2) is held LOW or left floating, the inverting output will immediately snap **`HIGH`** ($+12\text{ V}$). Ensure microcontrollers hold lines defined during bootup.
- **Pin Paralleling:** Always parallel pins 1 & 8 to $V_{DD}$, pins 4 & 5 to GND, and pins 6 & 7 to the gate trace to maintain low impedance.
