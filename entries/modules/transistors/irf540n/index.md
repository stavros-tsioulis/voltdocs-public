## Overview

The **IRF540N** is an advanced N-channel power HEXFET MOSFET manufactured by Infineon Technologies (formerly International Rectifier). Packaged in a heavy-duty **TO-220AB package**, it utilizes advanced processing technology to achieve extremely low on-resistance per silicon area.

Capable of withstanding drain-source voltages up to **$100\text{ Volts}$** and carrying continuous drain currents up to **$33\text{ Amps}$** (with pulsed currents up to $110\text{ A}$), the IRF540N is a standard choice for high-power DC motor drivers, H-bridge speed controllers, audio amplifiers, DC-DC buck/boost converters, and heavy solenoid switching.

## Quick reference

| | |
|---|---|
| **Transistor Type** | N-Channel Power HEXFET MOSFET |
| **Package** | TO-220AB (Metal tab connected to DRAIN) |
| **Drain-Source Voltage ($V_{DSS}$)**| $100\text{ V}$ max |
| **Continuous Drain Current ($I_D$)**| $33\text{ A}$ at $T_C = 25^\circ\text{C}$ ($23\text{ A}$ at $T_C = 100^\circ\text{C}$) |
| **Pulsed Drain Current ($I_{DM}$)**| $110\text{ A}$ |
| **Gate Threshold Voltage ($V_{GS(th)}$)**| $2.0\text{ V}$ min to $4.0\text{ V}$ max ($3.0\text{ V}$ typical) |
| **On-State Resistance ($R_{DS(on)}$)**| $44\text{ m}\Omega$ max at $V_{GS} = 10\text{V}, I_D = 16\text{A}$ |
| **Total Power Dissipation ($P_D$)** | $130\text{ W}$ ($T_C = 25^\circ\text{C}$) |

## Pinout (TO-220AB Package)

Looking at the **front labeled face** of the TO-220 package with leads pointing down:

```
        ┌─────────────┐
        │   O   [TAB] │  (Metal Mounting Tab = DRAIN)
        ├─────────────┤
        │   IRF540N   │  (Front Package Face)
        └─┬───┬───┬───┘
          1   2   3
          G   D   S
```

| Pin | Name | Description |
|---|---|---|
| 1 | `GATE` (`G`) | Gate control input |
| 2 | `DRAIN` (`D`) | Drain terminal (Internal connection to metal tab) |
| 3 | `SOURCE` (`S`) | Source terminal (Ground reference 0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Drain-Source Breakdown Volts| $V_{(BR)DSS}$| 100 | — | — | V | $V_{GS} = 0\text{V}, I_D = 250\ \mu\text{A}$ |
| Gate Threshold Voltage | $V_{GS(th)}$| 2.0 | 3.0 | 4.0 | V | $V_{DS} = V_{GS}, I_D = 250\ \mu\text{A}$ |
| Drain-to-Source Leakage | $I_{DSS}$ | — | — | 25 | µA | $V_{DS} = 100\text{V}, V_{GS} = 0\text{V}$ |
| On-Resistance ($V_{GS}=10\text{V}$)| $R_{DS(on)}$| — | 35 | 44 | mΩ | $V_{GS} = 10\text{V}, I_D = 16\text{A}$ |
| Total Gate Charge | $Q_g$ | — | 47 | 71 | nC | $I_D = 16\text{A}, V_{DS} = 80\text{V}, V_{GS} = 10\text{V}$ |

## High-Power Low-Side DC Motor Driver Circuit

```
      +12V to +48V Motor Supply Rail
                │
                ├─── ( + ) Motor Terminal
             [Motor]
                ├─── ( - ) Motor Terminal ───┬─── [Pin 2 & Tab: DRAIN]
                │                            │          IRF540N
        ┌───────┴──────┐             [Flyback Diode]
        │ 1N5408 Diode │             [ (1N5408)    ]
        └───────┬──────┘             └───────┬─── [Pin 3: SOURCE] ─── GND
                │                            │
  MCU GPIO ────┴─── [Resistor 220Ω] ─────────┴─── [Pin 1: GATE]
                                                  │
                                          [ 10kΩ Pull-down to GND ]
```

## Common mistakes

- **Attempting to drive directly from 3.3V GPIO pins:** The IRF540N is a **standard-level MOSFET** requiring $V_{GS} = 10\text{V}$ to fully turn on. At $V_{GS} = 3.3\text{V}$ or $5.0\text{V}$, the channel is only partially open, resulting in high $R_{DS(on)}$ and severe overheating under heavy load. Use a gate driver IC or a logic-level MOSFET like the **IRLZ44N**.
- **Forgetting a flyback diode on inductive loads:** Switching motors, relays, or solenoids generates inductive voltage spikes ($V = L \cdot \frac{di}{dt}$) that exceed the $100\text{V}$ breakdown voltage. Always connect a fast-recovery diode across the load.

## Notes

- **IRF540N vs IRLZ44N vs IRFZ44N:** IRF540N is 100V 33A standard gate ($10\text{V}$); IRFZ44N is 55V 49A standard gate ($10\text{V}$); IRLZ44N is 55V 47A logic-level gate ($3.3\text{V}/5\text{V}$).
