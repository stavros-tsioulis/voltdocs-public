## Overview

The **DMG2305UX** (DMG2305UX-7) is a -20V -4.2A ultra-low on-resistance P-channel logic-level power MOSFET manufactured by Diodes Incorporated. Housed in a compact **SOT-23** surface-mount package, it is specifically engineered for ultra-low-voltage gate drive applications.

Featuring guaranteed on-resistance specifications down to **$V_{GS} = -1.5\text{V}$** ($125\text{ m}\Omega$), **$V_{GS} = -1.8\text{V}$** ($82\text{ m}\Omega$), and just **$41\text{ m}\Omega$ at $V_{GS} = -4.5\text{V}$**, the DMG2305UX delivers high current conduction even when driven by low-voltage $1.8\text{V}$ microcontroller GPIOs or single-cell lithium chemistry nearing complete depletion ($3.0\text{V}$). It is standard equipment in **wearable electronics, IoT sensor nodes, smartphone power management, USB Type-C load switches, and battery reverse-polarity protection circuits**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | P-Channel Sub-1.8V Logic-Level MOSFET |
| **Package** | SOT-23 (3-pin SMD) |
| **Drain-Source Breakdown Voltage ($V_{DSS}$)**| **$-20\text{ V}$ max** |
| **Gate-Source Voltage ($V_{GSS}$)** | **$\pm 8\text{ V}$ max** |
| **Continuous Drain Current ($I_D$)** | **$-4.2\text{ A}$** ($T_A = 25^\circ\text{C}$) / **$-3.3\text{ A}$** ($T_A = 70^\circ\text{C}$) |
| **Pulsed Drain Current ($I_{DM}$)** | **$-25\text{ A}$** |
| **On-Resistance ($R_{DS(on)}$ at $-4.5\text{V}$)**| **$41\text{ m}\Omega$ max** ($32\text{ m}\Omega$ typ) |
| **On-Resistance ($R_{DS(on)}$ at $-2.5\text{V}$)**| **$55\text{ m}\Omega$ max** ($41\text{ m}\Omega$ typ) |
| **On-Resistance ($R_{DS(on)}$ at $-1.8\text{V}$)**| **$82\text{ m}\Omega$ max** ($55\text{ m}\Omega$ typ) |
| **On-Resistance ($R_{DS(on)}$ at $-1.5\text{V}$)**| **$125\text{ m}\Omega$ max** ($70\text{ m}\Omega$ typ) |
| **Gate Threshold Voltage ($V_{GS(th)}$)** | **$-0.4\text{ V}$ to $-1.0\text{ V}$** (Sub-1.8V Logic Compatible) |
| **Power Dissipation ($P_D$)** | **$0.9\text{ W} \dots 1.4\text{ W}$** |

## Pinout (SOT-23 Package)

Looking at the **top of the SOT-23 package**:

```
           ┌───┴───┐
           │   3   │ ── Pin 3: DRAIN (D)
           │       │
           │ 2305  │
           └──┬─┬──┘
              1 2
       Pin 1: GATE (G)
       Pin 2: SOURCE (S)
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GATE (G)` | Control Input | Gate terminal (Driven LOW relative to Source to turn ON) |
| 2 | `SOURCE (S)` | Power Terminal | Source terminal (Connected to positive supply rail / Li-ion battery) |
| 3 | `DRAIN (D)` | Power Terminal | Drain terminal (Connected to switched DC load) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Drain-Source Breakdown | $V_{(BR)DSS}$ | -20 | — | — | V | $I_D = -250\ \mu\text{A}, V_{GS} = 0\text{V}$ |
| Gate Threshold Voltage | $V_{GS(th)}$ | -0.4 | -0.65 | -1.0 | V | $V_{DS} = V_{GS}, I_D = -250\ \mu\text{A}$ |
| Zero Gate Voltage Drain Current | $I_{DSS}$ | — | — | -1.0 | µA | $V_{DS} = -16\text{V}, V_{GS} = 0\text{V}$ |
| Gate-Body Leakage Current | $I_{GSS}$ | — | — | $\pm 100$ | nA | $V_{GS} = \pm 8\text{V}, V_{DS} = 0\text{V}$ |
| Static Drain-Source On-Resistance | $R_{DS(on)}$ | — | 32 | 41 | mΩ | $V_{GS} = -4.5\text{V}, I_D = -4.2\text{A}$ |
| Static Drain-Source On-Resistance | $R_{DS(on)}$ | — | 41 | 55 | mΩ | $V_{GS} = -2.5\text{V}, I_D = -3.3\text{A}$ |
| Static Drain-Source On-Resistance | $R_{DS(on)}$ | — | 55 | 82 | mΩ | $V_{GS} = -1.8\text{V}, I_D = -2.0\text{A}$ |
| Static Drain-Source On-Resistance | $R_{DS(on)}$ | — | 70 | 125 | mΩ | $V_{GS} = -1.5\text{V}, I_D = -1.0\text{A}$ |
| Total Gate Charge | $Q_g$ | — | 6.0 | 9.0 | nC | $V_{GS} = -4.5\text{V}, V_{DS} = -10\text{V}, I_D = -4.2\text{A}$ |

## Typical Application Circuit: 1.8V/3.3V High-Side Load Switch with N-Channel Driver

```
  +3.3V / +1.8V Power Rail ───────────────────────┬─────────► [Pin 2: SOURCE]
                                                  │              DMG2305UX
                                          [ 100kΩ Pull-Up ]      [Pin 3: DRAIN] ──► Switched Power to Sensor
                                                  │                 │
                                                  ├─────────► [Pin 1: GATE]
                                                  │
                                            [ DRAIN (D) ]
  MCU GPIO (1.8V / 3.3V) ───[ 1kΩ ]───► Gate of 2N7002 / AO3400 (N-Channel)
                                            [ SOURCE (S) ]
                                                  │
  System Ground (0V) ─────────────────────────────┴───────────────────────────────► Ground
```

## Comparison: DMG2305UX vs AO3401A

| Parameter | DMG2305UX | AO3401A |
|---|---|---|
| **$V_{DSS}$ Breakdown** | $-20\text{ V}$ | **$-30\text{ V}$** |
| **Max $V_{GS}$ Rating** | $\pm 8\text{ V}$ | **$\pm 12\text{ V}$** |
| **$R_{DS(on)}$ at $-4.5\text{V}$**| **$41\text{ m}\Omega$** | $55\text{ m}\Omega$ |
| **$R_{DS(on)}$ at $-1.8\text{V}$**| **$82\text{ m}\Omega$ (Guaranteed)**| Unspecified |
| **Ideal Application** | **$1.8\text{V}$ wearable / IoT power** | $5\text{V}/12\text{V}$ general load switch |

## Common mistakes

- **Exceeding the $\pm 8\text{V}$ gate voltage limit:** The ultra-thin gate oxide that allows $1.5\text{V}$ operation has a strict maximum breakdown rating of **$\pm 8\text{V}$**. Connecting the gate to a $12\text{V}$ supply will permanently puncture the gate dielectric.
- **Operating without a gate pull-up resistor:** In high-side switching circuits, an open microcontroller GPIO pin during boot-up or deep sleep will leave the gate floating, causing the MOSFET to partially conduct and overheat. Always include a **$10\text{k}\Omega \dots 100\text{k}\Omega$ pull-up resistor** between Gate (Pin 1) and Source (Pin 2).

## Notes

- **Top Marking Code:** The DMG2305UX package is marked with top marking code **`25U`** or **`25D`**.
