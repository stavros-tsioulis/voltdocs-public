## Overview

The **IRLML2502** (IRLML2502TRPBF) is an N-channel logic-level HEXFET power MOSFET manufactured by Infineon Technologies (formerly International Rectifier). Housed in a subminiature **SOT-23 (Micro3)** surface-mount package, it provides exceptionally low on-resistance and high current capability from low gate drive voltages.

With a drain-source voltage rating of **$20\text{ V}$**, continuous drain current of up to **$4.2\text{ A}$**, and an $R_{DS(on)}$ of just **$45\text{ m}\Omega$ at $V_{GS} = 4.5\text{V}$** (and $80\text{ m}\Omega$ at $2.5\text{V}$), the IRLML2502 is tailored for battery-powered IoT devices, Li-ion battery protection boards, high-side/low-side load switches, and small DC motor or solenoid actuators driven directly by 3.3V or 2.5V microcontrollers.

## Quick reference

| | |
|---|---|
| **Transistor Type** | N-Channel Logic-Level Enhancement Mode MOSFET |
| **Package** | SOT-23 (Micro3 / TO-236AB) |
| **Drain-Source Voltage ($V_{DSS}$)** | $20\text{ V}$ max |
| **Continuous Drain Current ($I_D$)** | $4.2\text{ A}$ at $V_{GS} = 4.5\text{V}$ ($3.4\text{ A}$ at $70^\circ\text{C}$) |
| **Gate Threshold Voltage ($V_{GS(th)}$)** | $0.6\text{ V}$ min to $1.2\text{ V}$ max |
| **On-Resistance ($R_{DS(on)}$)** | $45\text{ m}\Omega$ max at $4.5\text{V}$ / $80\text{ m}\Omega$ max at $2.5\text{V}$ |
| **Pulsed Drain Current ($I_{DM}$)** | $33\text{ A}$ |
| **Total Power Dissipation ($P_D$)** | $1.25\text{ W}$ at $T_A = 25^\circ\text{C}$ ($0.8\text{ W}$ at $70^\circ\text{C}$) |

## Terminal identification

Looking at the top of the SOT-23 package with the single top pin and two lower pins:

```
               ┌─────────┐
               │    3    │  (DRAIN)
               └─┐     ┌─┘
                 │ 2502  │
               ┌─┘     └─┐
               │ 1     2 │
               └─────────┘
             (GATE)   (SOURCE)
```

| Pin | Terminal | Description |
|---|---|---|
| 1 | `GATE` (`G`) | Gate control input (Connect to MCU GPIO via series resistor) |
| 2 | `SOURCE` (`S`) | Source terminal (Connect to Ground 0 V) |
| 3 | `DRAIN` (`D`) | Drain terminal (Connect to load negative return) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Drain-Source Breakdown Voltage | $V_{(BR)DSS}$ | 20 | — | — | V | $V_{GS} = 0\text{V}, I_D = 250\ \mu\text{A}$ |
| Gate Threshold Voltage | $V_{GS(th)}$ | 0.6 | — | 1.2 | V | $V_{DS} = V_{GS}, I_D = 250\ \mu\text{A}$ |
| On-Resistance ($V_{GS} = 4.5\text{V}$) | $R_{DS(on)}$ | — | 35 | 45 | mΩ | $V_{GS} = 4.5\text{V}, I_D = 4.2\text{A}$ |
| On-Resistance ($V_{GS} = 2.5\text{V}$) | $R_{DS(on)}$ | — | 60 | 80 | mΩ | $V_{GS} = 2.5\text{V}, I_D = 2.1\text{A}$ |
| Total Gate Charge | $Q_g$ | — | 8.0 | 12.0 | nC | $V_{GS} = 4.5\text{V}, V_{DS} = 16\text{V}, I_D = 4.2\text{A}$ |
| Turn-On Delay Time | $t_{d(on)}$ | — | 6.4 | — | ns | $V_{DD} = 10\text{V}, I_D = 1.0\text{A}, R_G = 6\ \Omega$ |
| Turn-Off Delay Time | $t_{d(off)}$ | — | 31 | — | ns | $V_{DD} = 10\text{V}, I_D = 1.0\text{A}, R_G = 6\ \Omega$ |

## Typical circuits

### Low-Side Load Switch (3.3V Microcontroller Control)

```
        +5V / +12V Power Rail
           │
         [ LOAD (LED Strip / DC Motor / Solenoid) ]
           │
           ├─── [ Flyback Diode 1N4148 / 1N4001 across inductive load ]
           │
        [Pin 3: DRAIN]
         IRLML2502
        [Pin 2: SOURCE] ─── GND
           │
        [Pin 1: GATE] ◄───[ R_gate = 100Ω ]───◄ MCU GPIO (3.3V / 5V)
           │
        [ R_pulldown = 100kΩ ]
           │
          GND
```

## Selection & substitutes

| Part Number | Package | $V_{DSS}$ | $I_D$ | $R_{DS(on)}$ at 4.5V | Notes |
|---|---|---|---|---|---|
| **IRLML2502** | SOT-23 | $20\text{ V}$ | $4.2\text{ A}$ | $45\text{ m}\Omega$ | Low gate threshold, high efficiency |
| **AO3400A** | SOT-23 | $30\text{ V}$ | $5.7\text{ A}$ | $33\text{ m}\Omega$ | Higher voltage and current rating |
| **BSS138** | SOT-23 | $50\text{ V}$ | $0.22\text{ A}$ | $3.5\ \Omega$ | Signal switching & I2C level shifter only |

## Common mistakes

- **Exceeding the $\pm 12\text{V}$ Gate-Source limit ($V_{GS}$):** Standard power MOSFETs tolerate $\pm 20\text{V}$ on the gate, but the subminiature gate oxide of the IRLML2502 has an absolute maximum rating of **$\pm 12\text{V}$**. Never connect the gate directly to $15\text{V}$ or $24\text{V}$ supplies without a voltage divider or Zener clamp.
- **Missing gate pull-down resistor:** During MCU boot/reset, GPIO pins default to high-impedance inputs. Without a $100\text{ k}\Omega$ pull-down resistor to ground, static charge on the gate will cause the MOSFET to partially turn ON.
- **Ignoring PCB thermal copper dissipation:** While rated for $4.2\text{ A}$, maintaining continuous currents $> 2.5\text{ A}$ in a tiny SOT-23 package requires adequate PCB copper pour attached to Pin 3 (`DRAIN`) to prevent overheating ($R_{\theta JA} = 100^\circ\text{C/W}$).

## Notes

- **Suffix Identification:** The standard lead-free production part number is **IRLML2502TRPBF** (supplied on tape and reel).
