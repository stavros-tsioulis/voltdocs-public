## Overview

The **AO3401** (and improved **AO3401A**) is a -30V -4.0A P-channel logic-level enhancement mode power MOSFET manufactured by Alpha & Omega Semiconductor. Housed in an industry-standard surface-mount **SOT-23** package, it is designed using advanced trench technology to achieve ultra-low on-resistance and low gate charge.

Providing a maximum on-state resistance of just **$55\text{ m}\Omega$ at $V_{GS} = -4.5\text{V}$** and fully specified down to **$V_{GS} = -2.5\text{V}$ ($85\text{ m}\Omega$)**, the AO3401 enables high-side switching directly from $3.3\text{V}$ or $5\text{V}$ microcontrollers. As the P-channel counterpart to the ubiquitous **AO3400**, the AO3401 is widely used in **battery-powered high-side power distribution switches, USB port power gating, low-loss reverse polarity protection circuits, and DC-DC converter output disconnect stages**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | P-Channel Logic-Level Enhancement Mode MOSFET |
| **Package** | SOT-23 (3-pin SMD) |
| **Drain-Source Breakdown Voltage ($V_{DSS}$)**| **$-30\text{ V}$ max** |
| **Gate-Source Voltage ($V_{GSS}$)** | **$\pm 12\text{ V}$ max** |
| **Continuous Drain Current ($I_D$)** | **$-4.0\text{ A}$** ($T_A = 25^\circ\text{C}$) / **$-3.5\text{ A}$** ($T_A = 70^\circ\text{C}$) |
| **Pulsed Drain Current ($I_{DM}$)** | **$-30\text{ A}$** |
| **On-Resistance ($R_{DS(on)}$ at $-10\text{V}$)**| **$44\text{ m}\Omega$ max** ($35\text{ m}\Omega$ typ) |
| **On-Resistance ($R_{DS(on)}$ at $-4.5\text{V}$)**| **$55\text{ m}\Omega$ max** ($43\text{ m}\Omega$ typ) |
| **On-Resistance ($R_{DS(on)}$ at $-2.5\text{V}$)**| **$85\text{ m}\Omega$ max** ($63\text{ m}\Omega$ typ) |
| **Gate Threshold Voltage ($V_{GS(th)}$)** | **$-0.7\text{ V}$ to $-1.3\text{ V}$** (Sub-2.5V Logic Direct Drive) |
| **Power Dissipation ($P_D$)** | **$1.4\text{ Watts}$** ($T_A = 25^\circ\text{C}$) |
| **Complementary N-Channel Pair** | **AO3400 / AO3400A** |

## Pinout (SOT-23 Package)

Looking at the **top of the SOT-23 package**:

```
           ┌───┴───┐
           │   3   │ ── Pin 3: DRAIN (D)
           │       │
           │ AO3401│
           └──┬─┬──┘
              1 2
       Pin 1: GATE (G)
       Pin 2: SOURCE (S)
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GATE (G)` | Control Input | Gate terminal (Driven LOW relative to Source to turn ON) |
| 2 | `SOURCE (S)` | Power Terminal | Source terminal (Connected to positive supply rail or battery positive) |
| 3 | `DRAIN (D)` | Power Terminal | Drain terminal (Connected to positive side of the switched load) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Drain-Source Breakdown | $V_{(BR)DSS}$ | -30 | — | — | V | $I_D = -250\ \mu\text{A}, V_{GS} = 0\text{V}$ |
| Gate Threshold Voltage | $V_{GS(th)}$ | -0.7 | -0.9 | -1.3 | V | $V_{DS} = V_{GS}, I_D = -250\ \mu\text{A}$ |
| Zero Gate Voltage Drain Current | $I_{DSS}$ | — | — | -1.0 | µA | $V_{DS} = -24\text{V}, V_{GS} = 0\text{V}$ |
| Gate-Body Leakage Current | $I_{GSS}$ | — | — | $\pm 100$ | nA | $V_{GS} = \pm 12\text{V}, V_{DS} = 0\text{V}$ |
| Static Drain-Source On-Resistance | $R_{DS(on)}$ | — | 35 | 44 | mΩ | $V_{GS} = -10\text{V}, I_D = -4.0\text{A}$ |
| Static Drain-Source On-Resistance | $R_{DS(on)}$ | — | 43 | 55 | mΩ | $V_{GS} = -4.5\text{V}, I_D = -3.5\text{A}$ |
| Static Drain-Source On-Resistance | $R_{DS(on)}$ | — | 63 | 85 | mΩ | $V_{GS} = -2.5\text{V}, I_D = -2.5\text{A}$ |
| Total Gate Charge | $Q_g$ | — | 11 | 14 | nC | $V_{GS} = -10\text{V}, V_{DS} = -15\text{V}, I_D = -4.0\text{A}$ |

## Typical Application Circuit: Ideal Diode / Reverse-Polarity Battery Protection

Using a P-channel MOSFET in place of a Schottky diode eliminates the $0.3\text{V} \dots 0.5\text{V}$ diode voltage drop, reducing power loss to milliwatts:

```
  +3.7V / +5V Power In ───────► [Pin 2: SOURCE]
                                    AO3401
  Common Ground (0V)   ───────► [Pin 1: GATE]   ───► [Pin 3: DRAIN] ───► Protected +Vout to Circuit
                                                         │
                                               [ 10µF Bypass Cap ]
                                                         │
  Common Ground (0V)   ──────────────────────────────────┴──────────────► Common Ground Return
```
*(When power is connected with correct polarity, $V_{GS} = -V_{IN}$, turning the channel fully ON with only $R_{DS(on)} \times I$ drop. If reverse polarity is connected, $V_{GS} > 0\text{V}$, remaining safely OFF).*

## Common mistakes

- **Exceeding the $\pm 12\text{V}$ Gate-Source ($V_{GSS}$) rating:** Unlike standard power MOSFETs with $\pm 20\text{V}$ gate limits, the AO3401 has an absolute maximum $V_{GS}$ limit of **$\pm 12\text{V}$**. When switching supplies above $12\text{V}$ (e.g. 24V rails), use a Zener diode (e.g. 10V) or voltage divider to limit $V_{GS}$.
- **Reversing Drain and Source:** Because power MOSFETs have an intrinsic body diode from Drain to Source, connecting Source to the load and Drain to $+V_{IN}$ allows current to continuously conduct through the forward-biased body diode even when the gate is turned OFF.

## Notes

- **Top Marking Code:** AO3401/AO3401A packages are commonly laser-marked with top codes **`A19T`**, **`AO1`**, or **`X1DV`**.
