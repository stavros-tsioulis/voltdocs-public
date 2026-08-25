## Overview

The **IRFP250N** (IRFP250NPBF) is a high-power $200\text{V}$ $30\text{A}$ N-channel HEXFET power MOSFET manufactured by Infineon Technologies (originally International Rectifier). Housed in an oversized heavy-duty **TO-247AC** through-hole package with low thermal resistance ($\theta_{JC} = 0.70^\circ\text{C/W}$), it is engineered for power-hungry linear and high-voltage switching applications.

Boasting a drain-to-source breakdown rating of **$200\text{V}$**, continuous current handling of **$30\text{A}$ at $25^\circ\text{C}$**, a power dissipation capability of **$214\text{ Watts}$**, and a maximum on-resistance of **$75\text{ m}\Omega$ ($0.075\ \Omega$)**, the IRFP250N is famous in the audiophile and high-voltage hobby communities. It is the core active transistor in **Nelson Pass Class-A audio amplifiers (Pass Zen, Pass Aleph 30/60)**, resonant **ZVS induction heaters (Mazzilli oscillators)**, solid-state Tesla coils (SSTC), and DC electronic load banks.

## Quick reference

| | |
|---|---|
| **Transistor Type** | High-Power N-Channel HEXFET MOSFET |
| **Package** | TO-247AC (3-pin through-hole) |
| **Drain-Source Voltage ($V_{DSS}$)** | **$200\text{ V}$ max** |
| **Continuous Drain Current ($I_D$)** | **$30\text{ A}$** at $T_C = 25^\circ\text{C}$ ($21\text{ A}$ at $100^\circ\text{C}$) |
| **Pulsed Drain Current ($I_{DM}$)** | **$120\text{ A}$** |
| **On-Resistance ($R_{DS(on)}$ at 10V)**| **$75\text{ m}\Omega$ ($0.075\ \Omega$) max** |
| **Gate Threshold Voltage ($V_{GS(th)}$)**| **$2.0\text{ V}$ to $4.0\text{ V}$** (Standard $10\text{V} \dots 15\text{V}$ gate drive) |
| **Total Power Dissipation ($P_D$)** | **$214\text{ Watts}$** ($T_C = 25^\circ\text{C}$) |
| **Thermal Resistance ($\theta_{JC}$)**| **$0.70^\circ\text{C/W}$** (Junction-to-Case) |
| **Operating Junction Temp** | $-55^\circ\text{C}$ to $+175^\circ\text{C}$ |

## Pinout (TO-247AC Package)

Looking at the **front labeled face** with leads pointing downward:

```
        ┌──────────────────┐
        │   O   [Metal]    │ ── Tab is internally connected to Pin 2 (Drain)
        ├──────────────────┤
        │     IRFP250N     │
        │     TO-247AC     │
        └─┬──────┬──────┬──┘
          1      2      3
          G      D      S
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GATE` | Gate Input | Gate control terminal (Drive with $10\text{V} \dots 15\text{V}$ for full saturation) |
| 2 (Tab) | `DRAIN` | Power Drain | Drain switching terminal (Internally connected to heavy metal mounting tab) |
| 3 | `SOURCE`| Power Source | Source terminal (Connect to ground, source resistor, or negative rail) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Drain-Source Breakdown | $V_{(BR)DSS}$ | 200 | — | — | V | $V_{GS} = 0\text{V}, I_D = 250\ \mu\text{A}$ |
| Static Drain-Source $R_{DS(on)}$ | $R_{DS(on)}$ | — | — | 0.075 | Ω | $V_{GS} = 10\text{V}, I_D = 18\text{A}$ |
| Gate Threshold Voltage | $V_{GS(th)}$ | 2.0 | — | 4.0 | V | $V_{DS} = V_{GS}, I_D = 250\ \mu\text{A}$ |
| Total Gate Charge | $Q_g$ | — | 82 | 123 | nC | $V_{DS} = 160\text{V}, V_{GS} = 10\text{V}, I_D = 18\text{A}$ |
| Input Capacitance | $C_{iss}$ | — | 2159 | — | pF | $V_{DS} = 25\text{V}, f = 1.0\text{ MHz}$ |
| Thermal Resistance | $R_{\theta JC}$ | — | — | 0.70 | °C/W | Junction-to-Case |

## Typical Application: Nelson Pass "Zen" Class-A Single-Ended Amplifier

```
                       +35V to +45V Regulated Linear DC Supply
                                          │
                                 [ R_L: 8Ω 50W Power Resistor / Choke ]
                                          │
                                          ├───[ C_OUT: 2200µF 50V Audio Cap ]───► To Speaker
                                          │
                                   [Pin 2: DRAIN]
                                      IRFP250N
  Audio Input (via Preamp)         [Pin 1: GATE]
           │                              │
           ├───[ 1µF Poly Cap ]───────────┤
           │                              ├───[ 100kΩ Gate Bias Potentiometer (to +V)]
          GND                             │
                                   [Pin 3: SOURCE]
                                          │
                                          ├───[ R_S: 0.47Ω 10W Non-Inductive Resistor ]──┐
                                          │                                              │
                                         GND ────────────────────────────────────────────┴─── Common GND
```

## Common mistakes

- **Inadequate heatsink sizing in linear audio modes:** In Class-A amplifiers or electronic loads, the MOSFET operates continuously in its active linear region dissipating $50\text{W} \dots 100\text{W}$ of heat per transistor. A large extruded aluminum heatsink with thermal resistance $\le 0.5^\circ\text{C/W}$ (or active fan cooling) is mandatory.
- **Neglecting gate damping in high-frequency ZVS oscillators:** High input capacitance ($C_{iss} \approx 2160\text{ pF}$) can interact with stray lead inductance to trigger parasitic megahertz oscillations. Always place a **$10\ \Omega \dots 47\ \Omega$ carbon film resistor** directly against Pin 1 (Gate).

## Notes

- **Package Advantage:** TO-247 package has more than twice the thermal interface surface area of TO-220, drastically reducing case-to-heatsink thermal bottlenecking.
