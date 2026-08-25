## Overview

The **IRLML6344** (IRLML6344TRPBF) is an ultra-low on-resistance N-channel logic-level power MOSFET manufactured by Infineon Technologies (originally International Rectifier). Housed in an industry-standard miniature 3-lead **SOT-23 (Micro3)** surface-mount package, it provides exceptional current-handling capability in ultra-compact PCB layouts.

Rated for a drain-to-source breakdown voltage of **$30\text{V}$** and a continuous drain current up to **$5.0\text{A}$**, the IRLML6344 is distinguished by its sub-logic gate threshold ($V_{GS(th)} = 0.5\text{V} \dots 1.1\text{V}$) and ultra-low on-resistance: **$22\text{ m}\Omega$ at $10\text{V}$**, **$29\text{ m}\Omega$ at $4.5\text{V}$**, and **$37\text{ m}\Omega$ at $2.5\text{V}$**. It can be driven directly to full saturation from **$1.8\text{V}$, $2.5\text{V}$, $3.3\text{V}$, or $5.0\text{V}$ microcontroller GPIO pins** without requiring level-shifting gate drivers, making it the premier choice for **micro-drone motor drivers, DC solenoid actuators, 3.3V battery power switches, and addressable LED power gating**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | N-Channel Logic-Level Power MOSFET |
| **Package** | SOT-23-3 (Micro3) SMD |
| **Drain-Source Voltage ($V_{DSS}$)** | $30\text{ V}$ max |
| **Continuous Drain Current ($I_D$)** | **$5.0\text{ A}$** at $T_A = 25^\circ\text{C}$ ($4.0\text{ A}$ at $70^\circ\text{C}$) |
| **Pulsed Drain Current ($I_{DM}$)** | **$20.0\text{ A}$** |
| **On-Resistance ($R_{DS(on)}$ at 4.5V)**| **$29\text{ m}\Omega$ ($0.029\ \Omega$) max** |
| **On-Resistance ($R_{DS(on)}$ at 2.5V)**| **$37\text{ m}\Omega$ ($0.037\ \Omega$) max** |
| **Gate Threshold Voltage ($V_{GS(th)}$)**| **$0.5\text{ V}$ to $1.1\text{ V}$** (Sub-logic threshold) |
| **Total Gate Charge ($Q_g$)** | $4.0\text{ nC}$ typ ($6.0\text{ nC}$ max) |
| **Power Dissipation ($P_D$)** | $1.3\text{ Watts}$ (on standard 1-inch FR-4 copper pad) |

## Pinout (SOT-23-3 Package)

Looking at the top surface of the SOT-23 package with two leads on the bottom and one lead on the top:

```
           ┌───────────┐
           │ 3: DRAIN  │
           └───┬───┬───┘
               │   │
           ┌───┴───┴───┐
           │ IRLML6344 │
           └───┬───┬───┘
               │   │
           ┌───┴───┴───┐
           │ 1: GATE   │ 2: SOURCE
           └───────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GATE` | Gate Input | Gate control terminal (Connect to MCU GPIO via $100\ \Omega$ series resistor) |
| 2 | `SOURCE`| Power Source | Source terminal (Connect to system Ground / $0\text{ V}$) |
| 3 | `DRAIN` | Power Drain | Drain switching terminal (Connect to negative terminal of switched load) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Drain-Source Breakdown | $V_{(BR)DSS}$ | 30 | — | — | V | $V_{GS} = 0\text{V}, I_D = 250\ \mu\text{A}$ |
| Static Drain-Source $R_{DS(on)}$ | $R_{DS(on)}$ | — | 17 | 22 | mΩ | $V_{GS} = 10\text{V}, I_D = 5.0\text{A}$ |
| Static Drain-Source $R_{DS(on)}$ | $R_{DS(on)}$ | — | 22 | 29 | mΩ | $V_{GS} = 4.5\text{V}, I_D = 4.0\text{A}$ |
| Static Drain-Source $R_{DS(on)}$ | $R_{DS(on)}$ | — | 28 | 37 | mΩ | $V_{GS} = 2.5\text{V}, I_D = 2.0\text{A}$ |
| Gate Threshold Voltage | $V_{GS(th)}$ | 0.5 | 0.8 | 1.1 | V | $V_{DS} = V_{GS}, I_D = 25\ \mu\text{A}$ |
| Zero Gate Voltage Current | $I_{DSS}$ | — | — | 1.0 | µA | $V_{DS} = 24\text{V}, V_{GS} = 0\text{V}$ |
| Gate-Body Leakage Current | $I_{GSS}$ | — | — | $\pm 100$ | nA | $V_{GS} = \pm 12\text{V}$ |
| Diode Forward Voltage | $V_{SD}$ | — | — | 1.2 | V | $I_S = 1.3\text{A}, V_{GS} = 0\text{V}$ |

## Typical Low-Side Switching Circuit (3.3V / 1.8V MCU Control)

```
                       +12V DC Motor / Solenoid / LED Strip Supply
                                   │
                               [ + Load - ]
                                   │
                                   ├───[ Flyback Diode (e.g. 1N5819) ]───┐
                                   │   (Anode to Drain, Cathode to +12V)  │
                             [Pin 3: DRAIN]                              │
                               IRLML6344                                 │
  MCU GPIO (1.8V - 3.3V)     [Pin 1: GATE]                               │
          │                        │                                     │
          ├───[ 100Ω Resistor ]────┤                                     │
          │                        ├───[ 10kΩ Pull-Down Resistor ]───────┤
         GND                       │                                     │
                             [Pin 2: SOURCE]                             │
                                   │                                     │
                                  GND ───────────────────────────────────┴─── Common GND
```

## Comparison: IRLML6344 vs IRLML2502 vs 2N7002

| Parameter | IRLML6344 | IRLML2502 | 2N7002 |
|---|---|---|---|
| **$V_{DSS}$ Voltage** | **$30\text{ V}$** | $20\text{ V}$ | $60\text{ V}$ |
| **Continuous Current ($I_D$)** | **$5.0\text{ A}$** | $4.2\text{ A}$ | $0.115\text{ A}$ ($115\text{mA}$) |
| **$R_{DS(on)}$ at 4.5V** | **$29\text{ m}\Omega$ ($0.029\ \Omega$)** | $45\text{ m}\Omega$ | $5000\text{ m}\Omega$ ($5.0\ \Omega$) |
| **$R_{DS(on)}$ at 2.5V** | **$37\text{ m}\Omega$** | $80\text{ m}\Omega$ | Not Specified (High) |

## Common mistakes

- **Exceeding the $\pm 12\text{V}$ maximum gate voltage ($V_{GS}$):** Sub-logic MOSFETs have thin gate oxide layers. The absolute maximum gate-to-source rating is **$\pm 12\text{V}$** (unlike standard 20V gates). Never connect the gate directly to a 12V or 24V supply.
- **Omitting thermal copper heatsinking for high continuous currents:** While the silicon die is rated for 5A, continuous loads above $2.5\text{A}$ require adequate PCB copper pour attached to Pin 3 (Drain) to dissipate heat without exceeding $150^\circ\text{C}$.

## Notes

- **Suffix Guide:** `TRPBF` denotes Tape & Reel Lead-Free packaging.
