## Overview

The **IRF9540** (and advanced **IRF9540N**) is a -100V -23A P-channel HEXFET power MOSFET manufactured by Infineon (originally International Rectifier), Vishay, and STMicroelectronics. Housed in an industry-standard **TO-220AB** through-hole package, it is the world's most famous through-hole high-voltage P-channel power MOSFET.

Providing a high drain-source breakdown voltage rating of **$-100\text{V}$**, a continuous drain current rating of **$-23\text{A}$** ($-76\text{A}$ pulsed peak), and an on-state resistance of **$117\text{ m}\Omega$ at $V_{GS} = -10\text{V}$** with **$140\text{ Watts}$** of power dissipation capability ($\theta_{JC} = 1.1^\circ\text{C/W}$), the IRF9540 is the undisputed P-channel companion to the iconic **IRF540N**. It is widely employed in **complementary MOSFET Class AB audio power amplifiers, full-bridge reversible DC motor drivers, high-side power distribution switches for 24V/48V systems, and solar battery cutoff circuits**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | P-Channel HEXFET Power MOSFET |
| **Package** | TO-220AB (3-pin through-hole) |
| **Drain-Source Breakdown Voltage ($V_{DSS}$)**| **$-100\text{ V}$ max** |
| **Gate-Source Voltage ($V_{GSS}$)** | **$\pm 20\text{ V}$ max** |
| **Continuous Drain Current ($I_D$)** | **$-23\text{ A}$** ($T_C = 25^\circ\text{C}$) / **$-16\text{ A}$** ($T_C = 100^\circ\text{C}$) |
| **Pulsed Drain Current ($I_{DM}$)** | **$-76\text{ A}$** |
| **On-Resistance ($R_{DS(on)}$ at $-10\text{V}$)**| **$117\text{ m}\Omega$ max** ($95\text{ m}\Omega$ typ) at $I_D = -11\text{A}$ |
| **Gate Threshold Voltage ($V_{GS(th)}$)** | **$-2.0\text{ V}$ to $-4.0\text{ V}$** ($V_{GS} = -10\text{V}$ recommended for full conduction) |
| **Total Power Dissipation ($P_D$)** | **$140\text{ Watts}$** ($T_C = 25^\circ\text{C}$ with heatsink) |
| **Operating Temperature Range** | **$-55^\circ\text{C}$ to $+175^\circ\text{C}$** |
| **Complementary N-Channel Pair** | **IRF540N / IRF540** |

## Pinout (TO-220AB Package - G-D-S Standard)

Looking at the **front labeled face** with leads pointing downward:

```
        ┌──────────────┐
        │  O  [Metal]  │ ── Tab is internally connected to Pin 2 (Drain)
        ├──────────────┤
        │   IRF9540N   │
        └─┬────┬────┬──┘
          1    2    3
          G    D    S
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GATE (G)` | Control Input | Gate control terminal (Pull LOW relative to Source to turn ON) |
| 2 (Tab) | `DRAIN (D)` | Power Terminal | Drain output (Connected to switched load; internally bonded to tab) |
| 3 | `SOURCE (S)` | Power Terminal | Source input (Connected to positive power rail, e.g. $+24\text{V} \dots +48\text{V}$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Drain-Source Breakdown | $V_{(BR)DSS}$ | -100 | — | — | V | $I_D = -250\ \mu\text{A}, V_{GS} = 0\text{V}$ |
| Gate Threshold Voltage | $V_{GS(th)}$ | -2.0 | — | -4.0 | V | $V_{DS} = V_{GS}, I_D = -250\ \mu\text{A}$ |
| Zero Gate Voltage Drain Current | $I_{DSS}$ | — | — | -25 | µA | $V_{DS} = -100\text{V}, V_{GS} = 0\text{V}$ |
| Gate-Body Leakage Current | $I_{GSS}$ | — | — | $\pm 100$ | nA | $V_{GS} = \pm 20\text{V}, V_{DS} = 0\text{V}$ |
| Static Drain-Source On-Resistance | $R_{DS(on)}$ | — | 95 | 117 | mΩ | $V_{GS} = -10\text{V}, I_D = -11\text{A}$ |
| Forward Transconductance | $g_{FS}$ | 5.3 | — | — | S | $V_{DS} = -50\text{V}, I_D = -11\text{A}$ |
| Total Gate Charge | $Q_g$ | — | 64 | 97 | nC | $V_{GS} = -10\text{V}, V_{DS} = -80\text{V}, I_D = -11\text{A}$ |
| Input Capacitance | $C_{iss}$ | — | 1300 | — | pF | $V_{DS} = -25\text{V}, f = 1.0\text{MHz}$ |

## Typical Application: Complementary Push-Pull MOSFET Power Amplifier (Class AB)

```
                            +35V to +45V Positive Power Supply
                                          │
                                   [Pin 3: SOURCE]
                                      IRF9540N (P-Channel)
  Audio VAS Input ────────────────►[Pin 1: GATE]
                                   [Pin 2: DRAIN]
                                          │
                                          ├───► Audio Output (to Speaker via 0.22Ω Resistor)
                                          │
                                   [Pin 2: DRAIN]
  Audio VAS Input ────────────────►[Pin 1: GATE]
                                      IRF540N (N-Channel)
                                   [Pin 3: SOURCE]
                                          │
                            -35V to -45V Negative Power Supply
```

## Comparison: IRF9540N vs FQP27P06

| Parameter | FQP27P06 | IRF9540N |
|---|---|---|
| **$V_{DSS}$ Voltage** | $-60\text{ V}$ | **$-100\text{ V}$ (Higher Voltage Margin)** |
| **Max Current ($I_D$)** | **$-27\text{ A}$** | $-23\text{ A}$ |
| **On-Resistance ($R_{DS(on)}$)**| **$70\text{ m}\Omega$** | $117\text{ m}\Omega$ |
| **Power Dissipation ($P_D$)** | $120\text{ W}$ | **$140\text{ W}$** |
| **Complementary N-Channel** | FQP30N06L | **IRF540N** |

## Common mistakes

- **Attempting 3.3V/5V logic-level gate drive without a driver:** The IRF9540 requires a gate-to-source voltage of **$V_{GS} = -10\text{V}$** to achieve its rated $117\text{m}\Omega$ on-resistance. Applying only $-3.3\text{V}$ or $-5\text{V}$ leaves the transistor in its linear region, causing extreme overheating under load.
- **Forgetting that the metal mounting tab is connected to Drain:** In TO-220 power MOSFETs, the tab is internally connected to Pin 2 (Drain). When mounting multiple MOSFETs to a shared heatsink, always use **insulating mica/silicone pads and nylon washers**.

## Notes

- **Suffix Guide:** `IRF9540` is the original IR part ($19\text{A}$); `IRF9540N` is the upgraded HEXFET generation ($23\text{A}$); `IRF9540NPBF` indicates lead-free RoHS compliance.
