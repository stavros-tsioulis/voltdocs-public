## Overview

The **RFP30N06LE** is a classic 60V, 30A N-channel logic-level power MOSFET manufactured by onsemi (formerly Intersil / Harris Semiconductor / Fairchild) in a through-hole **TO-220AB** package. Built using the proprietary **MegaFET** manufacturing process, it was engineered specifically to achieve full saturation and low on-resistance from low gate-source voltages.

With a maximum $R_{DS(on)}$ of **$47\text{ m}\Omega$ at $V_{GS} = 5.0\text{V}$** and a low gate threshold voltage ($V_{GS(th)} = 1.0\text{V} \dots 2.0\text{V}$), the RFP30N06LE gained iconic status as the go-to MOSFET in early SparkFun tutorials, the *Arduino Cookbook*, and maker robotics projects for driving 12V DC motors, automotive relays, and high-brightness LED arrays directly from 5V microcontroller GPIOs.

## Quick reference

| | |
|---|---|
| **Transistor Type** | N-Channel Logic-Level Power MOSFET (MegaFET) |
| **Package** | TO-220AB (Pin 1: Gate, Pin 2: Drain/Tab, Pin 3: Source) |
| **Drain-Source Voltage ($V_{DSS}$)** | $60\text{ V}$ max |
| **Continuous Drain Current ($I_D$)** | $30\text{ A}$ at $T_C = 25^\circ\text{C}$ ($21\text{ A}$ at $100^\circ\text{C}$) |
| **Gate Threshold Voltage ($V_{GS(th)}$)** | $1.0\text{ V}$ min to $2.0\text{ V}$ max |
| **On-Resistance ($R_{DS(on)}$)** | $47\text{ m}\Omega$ max at $V_{GS} = 5.0\text{V}, I_D = 30\text{A}$ |
| **Pulsed Drain Current ($I_{DM}$)** | $75\text{ A}$ |
| **Total Power Dissipation ($P_D$)** | $96\text{ W}$ ($T_C = 25^\circ\text{C}$) |

## Terminal identification

```
        ┌─────────┐
        │  TO-220 │
        │ P30N06LE│
        └─┬───┬───┬─┘
          1   2   3
          G   D   S
```

| Pin | Terminal | Description |
|---|---|---|
| 1 | `Gate` (`G`) | Gate control input (Connect to MCU GPIO via $220\ \Omega$ series resistor) |
| 2 / Tab | `Drain` (`D`) | High-power load switching terminal / Tab (Connect to load negative return) |
| 3 | `Source` (`S`) | Source terminal (Connect to Common System Ground 0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Drain-Source Breakdown Voltage | $V_{(BR)DSS}$ | 60 | — | — | V | $V_{GS} = 0\text{V}, I_D = 250\ \mu\text{A}$ |
| Gate-Source Threshold Voltage | $V_{GS(th)}$ | 1.0 | — | 2.0 | V | $V_{DS} = V_{GS}, I_D = 250\ \mu\text{A}$ |
| On-Resistance ($V_{GS} = 5.0\text{V}$) | $R_{DS(on)}$ | — | — | 47 | mΩ | $V_{GS} = 5.0\text{V}, I_D = 30\text{A}$ |
| Gate-to-Source Breakdown Volts | $V_{GSS}$ | $\pm 10$ | — | — | V | Maximum gate oxide voltage limit |
| Turn-On Delay Time | $t_{d(on)}$ | — | 20 | — | ns | $V_{DD} = 30\text{V}, I_D = 30\text{A}, R_G = 50\ \Omega$ |
| Turn-Off Delay Time | $t_{d(off)}$ | — | 85 | — | ns | $V_{DD} = 30\text{V}, I_D = 30\text{A}, R_G = 50\ \Omega$ |

## Typical circuits

### Microcontroller Motor Switching Circuit (5V / 3.3V Logic)

```
        +12V / +24V Motor Supply
           │
         [ DC MOTOR ]
           │
           ├─── [ Flyback Diode 1N4007 across Motor ]
           │
        [Pin 2: DRAIN]
         RFP30N06LE
        [Pin 3: SOURCE] ─── GND (Common System Ground)
           │
        [Pin 1: GATE] ◄───[ R_gate = 220Ω ]───◄ Arduino / MCU GPIO Pin
           │
        [ R_pulldown = 10kΩ ]
           │
          GND
```

## Selection & substitutes

| Part Number | $V_{DSS}$ | $I_D$ | $R_{DS(on)}$ at 5V | Notes |
|---|---|---|---|---|
| **RFP30N06LE** | $60\text{ V}$ | $30\text{ A}$ | $47\text{ m}\Omega$ | Classic MegaFET part from early tutorials |
| **FQP30N06L** | $60\text{ V}$ | $32\text{ A}$ | $45\text{ m}\Omega$ | Modern planar QFET drop-in replacement |
| **IRLZ44N** | $55\text{ V}$ | $47\text{ A}$ | $22\text{ m}\Omega$ | Lower on-resistance, higher current capability |

## Common mistakes

- **Exceeding the $\pm 10\text{V}$ Gate-Source limit ($V_{GS}$):** Unlike standard MOSFETs that permit $\pm 20\text{V}$ on the gate, the thinner gate oxide of the RFP30N06LE has an absolute maximum rating of **$\pm 10\text{V}$**. Never connect the gate directly to a 12V or 24V supply.
- **Omitting the flyback diode with inductive loads:** Switching an inductive load (motor, relay, solenoid) without a reverse-biased flyback diode across the load will generate high-voltage inductive spikes that exceed the $60\text{V}$ breakdown limit, destroying the MOSFET.

## Notes

- **Suffix Identification:** The "LE" suffix indicates **Logic-Level** gate threshold with enhanced ESD gate protection.
