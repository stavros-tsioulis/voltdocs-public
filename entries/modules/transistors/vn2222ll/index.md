## Overview

The **VN2222LL** is a small-signal N-channel enhancement-mode vertical DMOS FET manufactured by Microchip Technology (originally Supertex), Siliconix, and Diodes Incorporated. Housed in a through-hole **TO-92** package, its part number was deliberately coined as a MOSFET counterpart to the iconic 2N2222 bipolar transistor.

Rated for a drain-to-source voltage of **$60\text{V}$**, continuous drain current of **$230\text{ mA}$** ($1.0\text{A}$ pulsed), and a low gate threshold voltage of **$0.6\text{V} \dots 2.4\text{V}$**, the VN2222LL provides sub-$10\text{ns}$ high-speed switching with zero DC base current. It is widely employed as a pin-compatible alternative to the **2N7000** for **miniature $5\text{V}/12\text{V}$ relay drivers, LED indicators, bidirectional logic level converters ($3.3\text{V} \leftrightarrow 5\text{V}$), and analog signal muting gates**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | Small-Signal N-Channel Vertical DMOS FET |
| **Package** | TO-92 (3-pin through-hole) |
| **Drain-Source Voltage ($V_{DSS}$)** | $60\text{ V}$ max |
| **Continuous Drain Current ($I_D$)** | **$230\text{ mA}$** ($0.23\text{ A}$) continuous / $1.0\text{ A}$ pulsed |
| **On-Resistance ($R_{DS(on)}$ at 10V)**| **$7.5\ \Omega$ max** |
| **On-Resistance ($R_{DS(on)}$ at 4.5V)**| **$10.0\ \Omega$ max** |
| **Gate Threshold Voltage ($V_{GS(th)}$)**| **$0.6\text{ V}$ to $2.4\text{ V}$** (Direct 3.3V and 5V logic compatible) |
| **Turn-On Delay Time ($t_{d(on)}$)** | **$< 10\text{ ns}$** (High-speed switching) |
| **Total Power Dissipation ($P_D$)** | $1.0\text{ Watt}$ |
| **Operating Temp Range** | $-55^\circ\text{C}$ to $+150^\circ\text{C}$ |

## Pinout (TO-92 Package - S-G-D Standard)

Looking at the **flat front face** with leads pointing downward:

```
        ┌─────────┐
        │  TO-92  │
        │VN2222LL │
        └─┬───┬───┬─┘
          1   2   3
          S   G   D
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `SOURCE`| Power Source | Source terminal (Connect to common ground / $0\text{ V}$) |
| 2 | `GATE` | Gate Input | Gate control terminal (High-impedance logic voltage input) |
| 3 | `DRAIN` | Power Drain | Drain switching terminal (Connect to switched load) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Drain-Source Breakdown | $V_{(BR)DSS}$ | 60 | — | — | V | $V_{GS} = 0\text{V}, I_D = 10\ \mu\text{A}$ |
| Static Drain-Source $R_{DS(on)}$ | $R_{DS(on)}$ | — | 4.0 | 7.5 | Ω | $V_{GS} = 10\text{V}, I_D = 500\text{mA}$ |
| Static Drain-Source $R_{DS(on)}$ | $R_{DS(on)}$ | — | 5.5 | 10.0 | Ω | $V_{GS} = 4.5\text{V}, I_D = 200\text{mA}$ |
| Gate Threshold Voltage | $V_{GS(th)}$ | 0.6 | 1.5 | 2.4 | V | $V_{DS} = V_{GS}, I_D = 1.0\text{mA}$ |
| Drain-Source Leakage | $I_{DSS}$ | — | — | 10 | µA | $V_{DS} = 60\text{V}, V_{GS} = 0\text{V}$ |
| Gate-Body Leakage | $I_{GSS}$ | — | — | $\pm 100$ | nA | $V_{GS} = \pm 20\text{V}, V_{DS} = 0\text{V}$ |
| Input Capacitance | $C_{ISS}$ | — | 45 | 60 | pF | $V_{DS} = 25\text{V}, V_{GS} = 0\text{V}, f = 1\text{MHz}$ |

## Typical Relay Driver Circuit (3.3V / 5V MCU Control)

```
                       +5V / +12V DC Relay Supply
                                   │
                           [ + Relay Coil - ]
                                   │
                                   ├───[ 1N4148 / 1N4007 Flyback Diode ]───┐
                                   │   (Anode to Drain, Cathode to +V)     │
                             [Pin 3: DRAIN]                                │
                                VN2222LL                                   │
  MCU GPIO (3.3V / 5.0V)     [Pin 2: GATE]                                 │
          │                        │                                       │
          ├───[ 100Ω Resistor ]────┤                                       │
          │                        ├───[ 100kΩ Pull-Down Resistor ]────────┤
         GND                       │                                       │
                             [Pin 1: SOURCE]                               │
                                   │                                       │
                                  GND ─────────────────────────────────────┴─── Common GND
```

## Comparison: VN2222LL vs 2N7000 vs BS170

| Parameter | VN2222LL | 2N7000 | BS170 |
|---|---|---|---|
| **$V_{DSS}$ Breakdown** | $60\text{ V}$ | $60\text{ V}$ | $60\text{ V}$ |
| **Max Current ($I_D$)** | **$230\text{ mA}$** | $200\text{ mA}$ | $500\text{ mA}$ |
| **$R_{DS(on)}$ at 10V** | **$7.5\ \Omega$** | $5.0\ \Omega$ | $5.0\ \Omega$ |
| **TO-92 Pinout (Flat Face)**| **`S - G - D`** | `S - G - D` | `D - G - S` (Reversed!) |
| **Power Dissipation** | **$1.0\text{ W}$** | $0.4\text{ W}$ | $0.83\text{ W}$ |

## Common mistakes

- **Confusing TO-92 pinouts with BS170:** While the VN2222LL and 2N7000 share the `Source - Gate - Drain` (S-G-D) lead sequence, the **BS170** reverses Drain and Source (`Drain - Gate - Source`). Always verify pinouts before substituting.
- **Switching heavy loads exceeding 250mA:** Small-signal TO-92 MOSFETs have a channel resistance of $5\ \Omega \dots 10\ \Omega$. Trying to switch a $1.0\text{A}$ motor will cause excessive $I^2 R$ heating ($P = 1^2 \times 7.5 = 7.5\text{W}$) and vaporize the TO-92 package. For loads $> 500\text{mA}$, use a power MOSFET like the **IRLML6344** or **FQP30N06L**.

## Notes

- **Suffix Guide:** `LL` designates low-leakage plastic TO-92; `-G` designates RoHS green molding compound.
