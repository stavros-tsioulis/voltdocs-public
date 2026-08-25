## Overview

The **FQP27P06** is a -60V -27A P-channel enhancement mode power MOSFET manufactured by onsemi (originally Fairchild Semiconductor). Built using proprietary planar stripe **QFET** DMOS technology and housed in an industry-standard **TO-220AB** through-hole package, it delivers low on-state resistance and superior switching performance.

Featuring a drain-source breakdown voltage ($V_{DSS}$) of **$-60\text{V}$**, a continuous drain current rating of **$-27\text{A}$** ($-108\text{A}$ pulsed), an on-resistance of **$70\text{ m}\Omega$ at $V_{GS} = -10\text{V}$**, and a maximum power dissipation of **$120\text{ Watts}$** at $T_C = 25^\circ\text{C}$ ($\theta_{JC} = 1.04^\circ\text{C/W}$), the FQP27P06 is the standard high-current P-channel companion to the popular **FQP30N06L**. It is widely employed in **$12\text{V}/24\text{V}$ automotive high-side load switching, discrete full-bridge DC motor drivers, high-power audio amplifier power stages, solar charge controllers, and battery disconnect circuits**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | P-Channel QFET Power MOSFET |
| **Package** | TO-220AB (3-pin through-hole) |
| **Drain-Source Breakdown Voltage ($V_{DSS}$)**| **$-60\text{ V}$ max** |
| **Gate-Source Voltage ($V_{GSS}$)** | **$\pm 25\text{ V}$ max** |
| **Continuous Drain Current ($I_D$)** | **$-27.0\text{ A}$** ($T_C = 25^\circ\text{C}$) / **$-19.1\text{ A}$** ($T_C = 100^\circ\text{C}$) |
| **Pulsed Drain Current ($I_{DM}$)** | **$-108\text{ A}$** |
| **On-Resistance ($R_{DS(on)}$ at $-10\text{V}$)**| **$70\text{ m}\Omega$ max** ($55\text{ m}\Omega$ typ) at $I_D = -13.5\text{A}$ |
| **Gate Threshold Voltage ($V_{GS(th)}$)** | **$-2.0\text{ V}$ to $-4.0\text{ V}$** ($V_{GS} = -10\text{V}$ recommended for full saturation) |
| **Total Power Dissipation ($P_D$)** | **$120\text{ Watts}$** ($T_C = 25^\circ\text{C}$ with heatsink) |
| **Operating Junction Temperature** | **$-55^\circ\text{C}$ to $+175^\circ\text{C}$** |
| **Complementary N-Channel Pair** | **FQP30N06 / FQP30N06L** |

## Pinout (TO-220AB Package - G-D-S Standard)

Looking at the **front labeled face** with leads pointing downward:

```
        ┌──────────────┐
        │  O  [Metal]  │ ── Tab is internally connected to Pin 2 (Drain)
        ├──────────────┤
        │   FQP27P06   │
        └─┬────┬────┬──┘
          1    2    3
          G    D    S
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GATE (G)` | Control Input | Gate control terminal (Pull LOW relative to Source to turn ON) |
| 2 (Tab) | `DRAIN (D)` | Power Terminal | Drain output (Connected to switched load; internally bonded to tab) |
| 3 | `SOURCE (S)` | Power Terminal | Source input (Connected to positive supply rail, e.g. $+12\text{V} \dots +24\text{V}$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Drain-Source Breakdown | $V_{(BR)DSS}$ | -60 | — | — | V | $I_D = -250\ \mu\text{A}, V_{GS} = 0\text{V}$ |
| Gate Threshold Voltage | $V_{GS(th)}$ | -2.0 | -2.9 | -4.0 | V | $V_{DS} = V_{GS}, I_D = -250\ \mu\text{A}$ |
| Zero Gate Voltage Drain Current | $I_{DSS}$ | — | — | -1.0 | µA | $V_{DS} = -60\text{V}, V_{GS} = 0\text{V}$ |
| Gate-Body Leakage Current | $I_{GSS}$ | — | — | $\pm 100$ | nA | $V_{GS} = \pm 25\text{V}, V_{DS} = 0\text{V}$ |
| Static Drain-Source On-Resistance | $R_{DS(on)}$ | — | 55 | 70 | mΩ | $V_{GS} = -10\text{V}, I_D = -13.5\text{A}$ |
| Forward Transconductance | $g_{FS}$ | 10 | 15 | — | S | $V_{DS} = -30\text{V}, I_D = -13.5\text{A}$ |
| Total Gate Charge | $Q_g$ | — | 33 | 43 | nC | $V_{GS} = -10\text{V}, V_{DS} = -48\text{V}, I_D = -27\text{A}$ |
| Input Capacitance | $C_{iss}$ | — | 1100 | 1400 | pF | $V_{DS} = -25\text{V}, f = 1.0\text{MHz}$ |

## Typical Application Circuit: 12V / 24V High-Side Power Switch with NPN Driver

In high-side load switching, a small NPN transistor (e.g. 2N3904) pulls the P-channel gate LOW to turn the load ON:

```
  +12V to +24V DC Main Supply ────────────────────┬─────────► [Pin 3: SOURCE]
                                                  │              FQP27P06
                                           [ 10kΩ Pull-Up ]      [Pin 2: DRAIN] ───► [ + 10A DC Motor / Load - ]
                                                  │                 │                      │
                                                  ├─────────► [Pin 1: GATE]                │
                                                  │                                        │
                                            [ COLLECTOR ]                                  │
  MCU GPIO (3.3V / 5V) ───[ 1kΩ Resistor ]──► Base of 2N3904                               │
                                            [ EMITTER ]                                    │
                                                  │                                        │
  System Ground (0V) ─────────────────────────────┴────────────────────────────────────────┴── Common Ground Return
```

## Comparison: FQP27P06 vs IRF9540N

| Parameter | FQP27P06 | IRF9540N |
|---|---|---|
| **$V_{DSS}$ Voltage** | **$-60\text{ V}$** | **$-100\text{ V}$** |
| **Current ($I_D$)** | **$-27\text{ A}$** | $-23\text{ A}$ |
| **On-Resistance ($R_{DS(on)}$)**| **$70\text{ m}\Omega$ (Lower Loss)** | $117\text{ m}\Omega$ |
| **Power Dissipation ($P_D$)** | $120\text{ W}$ | $140\text{ W}$ |
| **Optimal System Voltage** | **$12\text{V} \dots 24\text{V}$ Systems** | $36\text{V} \dots 48\text{V}$ Systems |

## Common mistakes

- **Attempting to drive directly from a 3.3V/5V microcontroller pin on a 12V/24V supply:** A P-channel MOSFET turns OFF only when its Gate voltage equals its Source voltage ($V_{GS} = 0\text{V}$). If Source is at $+12\text{V}$ and an MCU pin outputs $+5\text{V}$, $V_{GS} = -7\text{V}$, leaving the transistor fully ON! An intermediate NPN transistor or open-drain buffer is **required** for level translation.

## Notes

- **Suffix Guide:** `FQP27P06` is standard through-hole TO-220AB; `FQI27P06` is I2PAK; `FQB27P06` is D2PAK surface-mount.
