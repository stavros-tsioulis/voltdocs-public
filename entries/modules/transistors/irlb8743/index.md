## Overview

The **IRLB8743** (IRLB8743PBF) is an ultra-low on-resistance 30V, 150A N-channel logic-level power MOSFET manufactured by Infineon Technologies (formerly International Rectifier) in a through-hole **TO-220AB** package.

Engineered with advanced trench technology, it achieves an extraordinarily low $R_{DS(on)}$ of **$3.2\text{ m}\Omega$ at $V_{GS} = 10\text{V}$** and **$4.2\text{ m}\Omega$ at $V_{GS} = 4.5\text{V}$**. Even when driven by $3.3\text{V}$ and $5.0\text{V}$ microcontrollers, it can switch massive continuous loads ($20\text{A} \dots 50\text{A}$) with virtually negligible conduction losses ($P_{diss} = I^2 \times R_{DS(on)} = 20^2 \times 0.0042 = 1.68\text{ W}$). It is the premier choice for high-power 3D printer heated beds, brushless/brushed DC motor speed controllers, electronic speed controllers (ESCs), and high-efficiency synchronous buck converters.

## Quick reference

| | |
|---|---|
| **Transistor Type** | N-Channel Logic-Level Power MOSFET |
| **Package** | TO-220AB (Pin 1: Gate, Pin 2: Drain/Tab, Pin 3: Source) |
| **Drain-Source Voltage ($V_{DSS}$)** | $30\text{ V}$ max |
| **Continuous Drain Current ($I_D$)** | $150\text{ A}$ (Silicon Limit, $T_C = 25^\circ\text{C}$) / $75\text{ A}$ (Package Limit) |
| **Gate Threshold Voltage ($V_{GS(th)}$)** | $1.35\text{ V}$ min to $2.35\text{ V}$ max |
| **On-Resistance ($R_{DS(on)}$)** | **$3.2\text{ m}\Omega$** at $10\text{V}$ / **$4.2\text{ m}\Omega$** at $4.5\text{V}$ |
| **Pulsed Drain Current ($I_{DM}$)** | $600\text{ A}$ |
| **Total Power Dissipation ($P_D$)** | $140\text{ W}$ ($T_C = 25^\circ\text{C}$) |

## Terminal identification

```
        ┌─────────┐
        │  TO-220 │
        │ LB8743  │
        └─┬───┬───┬─┘
          1   2   3
          G   D   S
```

| Pin | Terminal | Description |
|---|---|---|
| 1 | `Gate` (`G`) | Gate control input (Connect to MCU GPIO via $100\ \Omega$ series resistor) |
| 2 / Tab | `Drain` (`D`) | High-power load switching terminal / Tab (Connect to load negative return) |
| 3 | `Source` (`S`) | Source terminal (Connect to Common System Ground 0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Drain-Source Breakdown Voltage | $V_{(BR)DSS}$ | 30 | — | — | V | $V_{GS} = 0\text{V}, I_D = 250\ \mu\text{A}$ |
| Gate Threshold Voltage | $V_{GS(th)}$ | 1.35 | 1.80 | 2.35 | V | $V_{DS} = V_{GS}, I_D = 50\ \mu\text{A}$ |
| On-Resistance ($V_{GS} = 10\text{V}$) | $R_{DS(on)}$ | — | 2.5 | 3.2 | mΩ | $V_{GS} = 10\text{V}, I_D = 40\text{A}$ |
| On-Resistance ($V_{GS} = 4.5\text{V}$) | $R_{DS(on)}$ | — | 3.1 | 4.2 | mΩ | $V_{GS} = 4.5\text{V}, I_D = 32\text{A}$ |
| Gate-to-Drain Charge | $Q_{gd}$ | — | 8.8 | — | nC | $V_{DS} = 15\text{V}, V_{GS} = 4.5\text{V}, I_D = 32\text{A}$ |
| Total Gate Charge | $Q_g$ | — | 21 | 32 | nC | $V_{DS} = 15\text{V}, V_{GS} = 4.5\text{V}, I_D = 32\text{A}$ |
| Turn-On Delay Time | $t_{d(on)}$ | — | 19 | — | ns | $V_{DD} = 15\text{V}, I_D = 32\text{A}, R_G = 3.0\ \Omega$ |
| Turn-Off Delay Time | $t_{d(off)}$ | — | 17 | — | ns | $V_{DD} = 15\text{V}, I_D = 32\text{A}, R_G = 3.0\ \Omega$ |

## Typical circuits

### High-Current DC Motor / ESC Low-Side Driver (12V/24V up to 30A)

```
        +12V / +24V High-Current Supply
           │
         [ DC MOTOR (Up to 30A Continuous) ]
           │
           ├─── [ Schottky Flyback Diode (e.g. MBR20100CT) across Motor ]
           │
        [Pin 2: DRAIN]
         IRLB8743
        [Pin 3: SOURCE] ─── GND (Heavy Gauge Wire to Power Supply Negative)
           │
        [Pin 1: GATE] ◄───[ R_gate = 100Ω ]───◄ MCU PWM Output (3.3V / 5V)
           │
        [ R_pulldown = 100kΩ ]
           │
          GND
```

## Selection & substitutes

| Part Number | $V_{DSS}$ | Continuous $I_D$ | $R_{DS(on)}$ at 4.5V | Best Used For |
|---|---|---|---|---|
| **IRLB8743** | $30\text{ V}$ | **$150\text{ A}$ (75A pkg)** | **$4.2\text{ m}\Omega$** | Extreme current loads ($20\text{A} \dots 50\text{A}$) |
| **IRLB8721** | $30\text{ V}$ | $62\text{ A}$ | $13.1\text{ m}\Omega$ | Moderate high-current loads ($5\text{A} \dots 20\text{A}$), ultra-fast switching |
| **IRLZ44N** | $55\text{ V}$ | $47\text{ A}$ | $25\text{ m}\Omega$ | Higher voltage loads up to 48V |

## Common mistakes

- **Package lead current limit ($75\text{ A}$):** While the internal silicon die is rated for $150\text{ A}$, standard TO-220 wire bonds and terminal pins are limited to a maximum continuous current of **$75\text{ A}$**.
- **Exceeding $30\text{V}$ $V_{DSS}$ breakdown voltage:** The IRLB8743 must not be used on circuits exceeding 24V nominal (such as 36V or 48V e-bike batteries), as inductive spikes will exceed the $30\text{V}$ breakdown rating. Use the **IRL540N** (100V) for higher voltage supplies.

## Notes

- **Suffix Identification:** The standard lead-free model number is **IRLB8743PBF**.
