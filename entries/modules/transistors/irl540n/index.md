## Overview

The **IRL540N** (IRL540NPBF) is a 100V, 36A N-channel logic-level HEXFET power MOSFET manufactured by Infineon Technologies (formerly International Rectifier) in a through-hole **TO-220AB** package. It serves as the logic-level gate counterpart to the classic IRF540N.

While standard-gate MOSFETs like the IRF540N require a full $10\text{V}$ gate voltage ($V_{GS}$) to saturate, the IRL540N features a tailored low gate threshold voltage ($V_{GS(th)} = 1.0\text{V} \dots 2.0\text{V}$). It achieves an on-resistance of **$56\text{ m}\Omega$ at $V_{GS} = 5.0\text{V}$** and **$77\text{ m}\Omega$ at $V_{GS} = 4.0\text{V}$**, making it the premier choice when high breakdown voltage ($100\text{V}$) is needed to switch $24\text{V}$, $36\text{V}$, or $48\text{V}$ DC industrial loads, high-power solenoid valves, and e-bike accessories directly from $3.3\text{V}$ and $5.0\text{V}$ microcontroller pins.

## Quick reference

| | |
|---|---|
| **Transistor Type** | N-Channel Logic-Level Enhancement Mode MOSFET (HEXFET) |
| **Package** | TO-220AB (Pin 1: Gate, Pin 2: Drain/Tab, Pin 3: Source) |
| **Drain-Source Voltage ($V_{DSS}$)** | $100\text{ V}$ max |
| **Continuous Drain Current ($I_D$)** | $36\text{ A}$ at $T_C = 25^\circ\text{C}$ ($25\text{ A}$ at $100^\circ\text{C}$) |
| **Gate Threshold Voltage ($V_{GS(th)}$)** | $1.0\text{ V}$ min to $2.0\text{ V}$ max |
| **On-Resistance ($R_{DS(on)}$)** | $44\text{ m}\Omega$ at $10\text{V}$ / $56\text{ m}\Omega$ at $5\text{V}$ / $77\text{ m}\Omega$ at $4\text{V}$ |
| **Pulsed Drain Current ($I_{DM}$)** | $140\text{ A}$ |
| **Total Power Dissipation ($P_D$)** | $140\text{ W}$ ($T_C = 25^\circ\text{C}$) |

## Terminal identification

```
        ┌─────────┐
        │  TO-220 │
        │ IRL540N │
        └─┬───┬───┬─┘
          1   2   3
          G   D   S
```

| Pin | Terminal | Description |
|---|---|---|
| 1 | `Gate` (`G`) | Gate control input (Connect to MCU GPIO via $220\ \Omega$ series resistor) |
| 2 / Tab | `Drain` (`D`) | High-voltage load switching terminal / Tab (Connect to load negative return) |
| 3 | `Source` (`S`) | Source terminal (Connect to Common System Ground 0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Drain-Source Breakdown Voltage | $V_{(BR)DSS}$ | 100 | — | — | V | $V_{GS} = 0\text{V}, I_D = 250\ \mu\text{A}$ |
| Gate Threshold Voltage | $V_{GS(th)}$ | 1.0 | — | 2.0 | V | $V_{DS} = V_{GS}, I_D = 250\ \mu\text{A}$ |
| On-Resistance ($V_{GS} = 10\text{V}$) | $R_{DS(on)}$ | — | — | 44 | mΩ | $V_{GS} = 10\text{V}, I_D = 18\text{A}$ |
| On-Resistance ($V_{GS} = 5.0\text{V}$) | $R_{DS(on)}$ | — | — | 56 | mΩ | $V_{GS} = 5.0\text{V}, I_D = 18\text{A}$ |
| On-Resistance ($V_{GS} = 4.0\text{V}$) | $R_{DS(on)}$ | — | — | 77 | mΩ | $V_{GS} = 4.0\text{V}, I_D = 15\text{A}$ |
| Total Gate Charge | $Q_g$ | — | 48 | 74 | nC | $I_D = 18\text{A}, V_{DS} = 80\text{V}, V_{GS} = 5.0\text{V}$ |
| Turn-On Delay Time | $t_{d(on)}$ | — | 11 | — | ns | $V_{DD} = 50\text{V}, I_D = 18\text{A}, R_G = 5.1\ \Omega$ |
| Turn-Off Delay Time | $t_{d(off)}$ | — | 44 | — | ns | $V_{DD} = 50\text{V}, I_D = 18\text{A}, R_G = 5.1\ \Omega$ |

## Typical circuits

### High-Voltage (24V–48V) Load Switch Circuit

```
        +24V / +36V / +48V Power Supply
           │
         [ High-Voltage DC Motor / Heavy Solenoid / Actuator ]
           │
           ├─── [ Flyback Diode (e.g. 1N5408 / UF4007) ]
           │
        [Pin 2: DRAIN]
         IRL540N
        [Pin 3: SOURCE] ─── GND (Common System Ground)
           │
        [Pin 1: GATE] ◄───[ R_gate = 220Ω ]───◄ MCU GPIO / PWM (3.3V or 5V)
           │
        [ R_pulldown = 100kΩ ]
           │
          GND
```

## Selection & substitutes

| Part Number | $V_{DSS}$ | $I_D$ | $R_{DS(on)}$ at 5V | Target Applications |
|---|---|---|---|---|
| **IRL540N** | **$100\text{ V}$** | $36\text{ A}$ | $56\text{ m}\Omega$ | High voltage (24V–48V) logic-level switching |
| **IRLZ44N** | $55\text{ V}$ | $47\text{ A}$ | $22\text{ m}\Omega$ | Medium voltage (12V–24V), lower on-resistance |
| **IRF540N** | $100\text{ V}$ | $33\text{ A}$ | $44\text{ m}\Omega$ (at 10V) | Standard gate; **requires 10V gate drive** |

## Common mistakes

- **Substituting an IRF540N for an IRL540N:** The "F" version requires $10\text{V}$ on the gate. When driven directly by a $3.3\text{V}$ or $5\text{V}$ MCU, an IRF540N does not fully turn on, acting as a high-resistance heater under heavy loads.
- **Forgetting a high-voltage flyback diode on 24V/48V inductive loads:** High voltage back-EMF from large inductive coils will easily spike past the $100\text{V}$ breakdown rating ($V_{DSS}$) if not clamped with an appropriate fast-recovery diode (such as UF4007).

## Notes

- **IRL540N vs IRF540N:** "L" denotes **Logic-Level** gate ($V_{GS(th)} = 1.0\text{--}2.0\text{V}$); "F" denotes standard 10V gate threshold.
