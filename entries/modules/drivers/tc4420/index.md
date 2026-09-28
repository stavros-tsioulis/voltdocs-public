## Overview

The **TC4420** (TC4420CPA) is a single, high-speed, non-inverting MOSFET and IGBT gate driver IC manufactured by Microchip Technology (originally TelCom Semiconductor). Designed to translate low-power digital logic pulses into high-current switching signals, the TC4420 can source and sink up to **$6.0\text{ A}$ peak** current while driving heavy capacitive loads across a supply range of **$4.5\text{ V}$ to $18.0\text{ V}$**.

With exceptionally matched rise and fall times of just **$25\text{ ns}$** into a large $2500\text{ pF}$ load and a propagation delay under **$55\text{ ns}$**, the TC4420 drastically minimizes MOSFET switching transition losses in high-frequency switch-mode power supplies (SMPS), motor controllers, class-D audio amplifiers, induction heaters, and pulse-forming networks. Its inputs can tolerate negative input spikes down to $-5\text{ V}$, and the output stage is latch-up proof against reverse inductive kickback currents up to $1.5\text{ A}$.

## Quick reference

| | |
|---|---|
| **Driver Type** | High-Current Non-Inverting Low-Side Gate Driver |
| **Output Configuration** | Non-Inverting (`IN` = HIGH $\rightarrow$ `OUTPUT` = HIGH) |
| **Supply Voltage Range ($V_{DD}$)** | $4.5\text{ V}$ to $18.0\text{ V}$ DC ($20\text{ V}$ absolute max) |
| **Peak Output Current** | $6.0\text{ A}$ peak (Source / Sink) |
| **Rise / Fall Time ($t_r / t_f$)** | $25\text{ ns}$ typical ($C_L = 2500\text{ pF}$) |
| **Propagation Delay ($t_{D1} / t_{D2}$)** | $55\text{ ns}$ typical ($C_L = 2500\text{ pF}$) |
| **Output Impedance ($R_{OUT}$)** | $2.5\,\Omega$ high-state / $1.5\,\Omega$ low-state typical |
| **Input Logic Thresholds** | TTL/CMOS compatible with internal hysteresis ($V_{IH} = 2.4\text{V}, V_{IL} = 0.8\text{V}$) |
| **Reverse Current Latch-Up Immunity** | Withstands $> 1.5\text{ A}$ reverse current without damage |
| **Packages** | 8-pin DIP (CPA), SOIC-8 (COA/EOA), 5-pin TO-220 (CAT) |

## Pin configuration

### 8-Pin DIP / SOIC Package

```
             ┌───┴───┐
        VDD 1│ 1   8 │ VDD (Supply Voltage)
         IN 2│       │ 7 OUTPUT (Gate Drive)
         NC 3│ TC4420│ 6 OUTPUT (Gate Drive)
        GND 4│       │ 5 GND (Ground)
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1, 8 | `VDD` | Power Supply | Positive supply voltage ($+4.5\text{ V}$ to $+18.0\text{ V}$); must be tied together on PCB |
| 2 | `IN` | Digital Input | Non-inverting logic input; tolerant of inputs from $-5\text{ V}$ to $V_{DD} + 0.3\text{ V}$ |
| 3 | `NC` | Unconnected | No internal connection |
| 4, 5 | `GND` | Power / Ground | System ground reference; must be tied together on PCB |
| 6, 7 | `OUTPUT` | Power Output | High-current gate drive output; must be tied together on PCB |

> [!NOTE]
> In the 8-pin package, pins 1 and 8 (`VDD`), pins 4 and 5 (`GND`), and pins 6 and 7 (`OUTPUT`) are internally paired. Paralleling these pin pairs with short, thick traces on the PCB halves lead package inductance and maximizes peak current capability.

## Functional description

### Truth Table

| Input (`IN`) | Output (`OUTPUT`) | Operating Mode |
|---|---|---|
| **`LOW`** ($< 0.8\text{ V}$) | **`LOW`** ($\approx 0\text{ V}$) | Low-side pull-down active (holds MOSFET gate discharged) |
| **`HIGH`** ($> 2.4\text{ V}$) | **`HIGH`** ($\approx V_{DD}$) | High-side pull-up active (rapidly charges MOSFET gate) |

- **High-Current Drive Capability:** Standard microcontrollers can only source or sink $10\text{ mA} \dots 30\text{ mA}$, requiring hundreds of nanoseconds or even microseconds to charge large power MOSFET gate capacitances ($Q_g \ge 50\text{ nC}$). The TC4420 delivers brief instantaneous bursts of up to $6.0\text{ A}$, snapping power MOSFETs through their resistive linear switching region in tens of nanoseconds.
- **Latch-Up Proof Construction:** High-current switching transients can easily force output voltages slightly below ground or above $V_{DD}$. The TC4420 uses heavily doped epitaxial isolation that guarantees complete immunity to latch-up for reverse currents up to $1.5\text{ A}$.

## Absolute maximum ratings

> [!WARNING]
> Stresses beyond these ratings cause permanent breakdown. Supply voltages above $20\text{ V}$ will destroy internal gate oxides.

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
| Quiescent Power Supply Current | $I_S$ | — | 0.45 | 1.5 | mA | $V_{IN} = 3.0\text{ V}, V_{DD} = 18\text{ V}$ |

## Typical application circuit: High-Frequency Power MOSFET Switch

```
       +12V Gate Supply (VDD)
       ────────────────────────┬──────────────────────────────────────────┐
                               │                                          │
                             ┌─┴──┐ 4.7µF                               ┌─┴──┐
                             │    │ Low-ESR Tantalum                    │ 1,8│ (VDD)
                             └─┬──┘                                   ┌─┴────┴──┐
                               │                                      │ TC4420  │
                             ┌─┴──┐ 0.1µF                             │         │
                             │    │ Ceramic (MLCC)                    │         │
                             └─┬──┘                                   │ 6,7     ├──[ 4.7Ω ]──┬── Gate
                               │                                      │ (OUTPUT)│    Rg       │
       Microcontroller         │                                      │         │            ┌┴┐ 100k
     ┌─────────────────┐       │                                      │         │            │ │ Pull-down
     │      PWM Output ┼───────┼──────────────────────────────────────┤ 2 (IN)  │            └┬┘
     │                 │       │                                      │         │             │
     │             GND ┼───────┴──────────────────────────────────────┤ 4,5(GND)│             │
     └─────────────────┘                                              └────┬────┘             │
                                                                           │                  │
                                                                           ▼                  ▼
                                                                      Power Ground       Power Ground
```

## Design considerations & common mistakes

- **Bypass Capacitance Proximity is Critical:** Delivering $6.0\text{ A}$ current pulses in $25\text{ ns}$ creates huge transient currents ($di/dt \approx 2.4 \times 10^8\text{ A/s}$). Always place a $4.7\,\mu\text{F} \dots 10\,\mu\text{F}$ low-ESR tantalum or large ceramic capacitor in parallel with a $0.1\,\mu\text{F}$ high-frequency ceramic capacitor within **$5\text{ mm}$** of pins 1 and 8 to pins 4 and 5. Insufficient bypass capacitance causes $V_{DD}$ supply collapse and gate ringing.
- **Trace Inductance Mitigation:** Route the gate drive trace from pins 6 & 7 to the power MOSFET gate as short and thick as possible, with an adjacent return ground trace on the layer immediately below it to minimize the inductive loop area.
- **Gate Resistor Selection ($R_g$):** A small gate damping resistor ($2.2\,\Omega \dots 10\,\Omega$) is recommended between the TC4420 output and the MOSFET gate to prevent high-frequency LC ringing between the gate trace inductance and the MOSFET input capacitance ($C_{iss}$).
- **Pair All Dual Pins:** Always solder pins 1 and 8 together to $V_{DD}$, pins 4 and 5 together to GND, and pins 6 and 7 together to the gate resistor on the PCB. Utilizing single pins halves current capability and doubles stray inductance.
