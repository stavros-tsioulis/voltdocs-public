## Overview

The **IRFZ44N** is a widely used high-power N-channel Enhancement Mode Power MOSFET IC manufactured by Infineon (formerly International Rectifier). Encapsulated in a heavy-duty **TO-220AB package**, it is a mainstay in high-current DC motor controllers, H-bridge motor drivers, solar battery charge controllers, automotive power switches, and DC-to-DC converters.

Rated for a drain-source voltage ($V_{DSS}$) of **$55\text{ Volts}$** and continuous drain current ($I_D$) of **$49\text{ Amperes}$** at $25^\circ\text{C}$, the IRFZ44N achieves an ultra-low turn-on resistance ($R_{DS(on)}$) of **$17.5\ \text{m}\Omega$** when driven with a standard **$10\text{V}$ gate-source voltage ($V_{GS}$)**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | N-Channel Enhancement Mode Power MOSFET |
| **Package** | TO-220AB (Metal Tab connected internally to Drain) |
| **Drain-Source Voltage ($V_{DSS}$)**| $55\text{ V}$ max |
| **Continuous Drain Current ($I_D$)**| $49\text{ A}$ at $T_C = 25^\circ\text{C}$ ($35\text{ A}$ at $T_C = 100^\circ\text{C}$) |
| **Pulsed Drain Current ($I_{DM}$)** | $160\text{ A}$ peak pulse current |
| **Gate Threshold Voltage ($V_{GS(th)}$)**| $2.0\text{ V}$ min to $4.0\text{ V}$ max |
| **On-State Resistance ($R_{DS(on)}$)**| $17.5\ \text{m}\Omega$ max at $V_{GS} = 10\text{V}, I_D = 25\text{A}$ |
| **Total Gate Charge ($Q_g$)** | $63\text{ nC}$ max at $V_{GS} = 10\text{V}$ |
| **Power Dissipation ($P_D$)** | $94\text{ W}$ at $T_C = 25^\circ\text{C}$ |

## Pinout (TO-220AB Package)

Looking at the **front labeled face** of the TO-220 package with metal tab at top and leads pointing down:

```
        ┌───────────────┐
        │ [IRFZ44N Tab] │  (Metal Tab connected internally to Pin 2 DRAIN)
        ├───────────────┤
        │    IRFZ44N    │  (Front Package Face)
        └─┬────┬────┬───┘
          1    2    3
          G    D    S
```

| Pin | Name | Description |
|---|---|---|
| 1 | `GATE` (`G`) | Gate control terminal |
| 2 | `DRAIN` (`D`) / `TAB` | Drain terminal (Low-side load connection, connected to metal tab) |
| 3 | `SOURCE` (`S`) | Source terminal (Ground reference 0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Drain-Source Breakdown Volts| $V_{(BR)DSS}$| 55 | — | — | V | $V_{GS} = 0\text{V}, I_D = 250\ \mu\text{A}$ |
| Gate Threshold Voltage | $V_{GS(th)}$| 2.0 | — | 4.0 | V | $V_{DS} = V_{GS}, I_D = 250\ \mu\text{A}$ |
| Drain-Source Leakage | $I_{DSS}$ | — | — | 25 | µA | $V_{DS} = 55\text{V}, V_{GS} = 0\text{V}$ |
| Gate-Source Forward Leakage| $I_{GSS}$ | — | — | 100 | nA | $V_{GS} = 20\text{V}$ |
| Thermal Resistance (Junction-to-Case)| $R_{\theta JC}$| — | — | 1.5 | °C/W | $T_C = 25^\circ\text{C}$ |

## Standard Low-Side MOSFET Switching Circuit

```
                      +12V - 48V DC Power Supply Rail
                             │
                      [ DC Motor / Solenoid Load ]
                             │
       Gate Control          ├─────────── [Pin 2: DRAIN]
   (10V MOSFET Gate Driver)  │               IRFZ44N
            │                │            [Pin 3: SOURCE]
     [ R1 = 220Ω ] ────── [Pin 1: GATE]      │
            │                │              GND
     [ R2 = 10kΩ ]          GND
            │
           GND
```

## Common mistakes

- **Driving directly from 3.3V or 5V MCU pins:** The IRFZ44N is a **standard-gate MOSFET** requiring **$V_{GS} = 10\text{V}$** to fully saturate into its $17.5\ \text{m}\Omega$ state. Driving it directly from a 3.3V or 5V GPIO pin leaves the channel partially open in the linear region, causing high $R_{DS(on)}$ resistance, severe voltage drops, and rapid thermal destruction. Use a logic-level MOSFET (like the **IRLZ44N**) or a gate driver transistor (like 2N2222) for 3.3V/5V microcontroller control.
- **Forgetting flyback protection diodes on inductive loads:** Switching inductive loads (motors, solenoids, relays) causes negative back-EMF spikes. Add an external flyback diode (e.g. 1N4007 or SS34) in parallel across the load.

## Notes

- **IRFZ44N vs IRLZ44N:** IRFZ44N requires $10\text{V}$ gate drive ($V_{GS(th)} = 2\text{V}\dots 4\text{V}$); IRLZ44N is logic-level requiring only $3.3\text{V}\dots 5\text{V}$ gate drive ($V_{GS(th)} = 1\text{V}\dots 2\text{V}$).
