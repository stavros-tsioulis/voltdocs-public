## Overview

The **IRLB8721** (IRLB8721PBF) is an exceptionally popular 30V, 62A N-channel logic-level power MOSFET manufactured by Infineon Technologies (formerly International Rectifier). Housed in a through-hole **TO-220AB** package, it is specifically optimized for ultra-low on-resistance and minimal gate charge ($Q_g = 8.4\text{ nC}$).

With an $R_{DS(on)}$ of just **$8.7\text{ m}\Omega$ at $V_{GS} = 10\text{V}$** and **$13.1\text{ m}\Omega$ at $V_{GS} = 4.5\text{V}$**, the IRLB8721 can switch tens of amperes of current with negligible heat generation and without requiring a bulky heatsink. Extensively featured in DIY electronics tutorials (Adafruit, SparkFun) and widely used across the 3D printing community (RepRap, RAMPS controller boards, Ender-3 upgrades) for **12V/24V heated beds, hotend heater cartridges**, high-current LED arrays, and brushed DC motor controllers driven directly by 3.3V and 5V microcontrollers.

## Quick reference

| | |
|---|---|
| **Transistor Type** | N-Channel Logic-Level Power MOSFET |
| **Package** | TO-220AB (Pin 1: Gate, Pin 2: Drain/Tab, Pin 3: Source) |
| **Drain-Source Voltage ($V_{DSS}$)** | $30\text{ V}$ max |
| **Continuous Drain Current ($I_D$)** | $62\text{ A}$ at $T_C = 25^\circ\text{C}$ ($44\text{ A}$ at $100^\circ\text{C}$) |
| **Gate Threshold Voltage ($V_{GS(th)}$)** | $1.35\text{ V}$ min to $2.35\text{ V}$ max |
| **On-Resistance ($R_{DS(on)}$)** | $8.7\text{ m}\Omega$ at $10\text{V}$ / $13.1\text{ m}\Omega$ at $4.5\text{V}$ |
| **Total Gate Charge ($Q_g$)** | $8.4\text{ nC}$ typical (Ultra-low gate capacitance) |
| **Total Power Dissipation ($P_D$)** | $65\text{ W}$ ($T_C = 25^\circ\text{C}$) |

## Terminal identification

```
        ┌─────────┐
        │  TO-220 │
        │ LB8721  │
        └─┬───┬───┬─┘
          1   2   3
          G   D   S
```

| Pin | Terminal | Description |
|---|---|---|
| 1 | `Gate` (`G`) | Gate control input (Connect to MCU GPIO via $100\ \Omega \dots 220\ \Omega$ series resistor) |
| 2 / Tab | `Drain` (`D`) | High-power load switching terminal / Tab (Connect to load negative return) |
| 3 | `Source` (`S`) | Source terminal (Connect to Common System Ground 0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Drain-Source Breakdown Voltage | $V_{(BR)DSS}$ | 30 | — | — | V | $V_{GS} = 0\text{V}, I_D = 250\ \mu\text{A}$ |
| Gate Threshold Voltage | $V_{GS(th)}$ | 1.35 | 1.80 | 2.35 | V | $V_{DS} = V_{GS}, I_D = 25\ \mu\text{A}$ |
| On-Resistance ($V_{GS} = 10\text{V}$) | $R_{DS(on)}$ | — | 6.5 | 8.7 | mΩ | $V_{GS} = 10\text{V}, I_D = 31\text{A}$ |
| On-Resistance ($V_{GS} = 4.5\text{V}$) | $R_{DS(on)}$ | — | 9.7 | 13.1 | mΩ | $V_{GS} = 4.5\text{V}, I_D = 25\text{A}$ |
| Gate-to-Drain Charge | $Q_{gd}$ | — | 3.5 | — | nC | $V_{DS} = 15\text{V}, V_{GS} = 4.5\text{V}, I_D = 25\text{A}$ |
| Total Gate Charge | $Q_g$ | — | 8.4 | 13 | nC | $V_{DS} = 15\text{V}, V_{GS} = 4.5\text{V}, I_D = 25\text{A}$ |
| Turn-On Delay Time | $t_{d(on)}$ | — | 11 | — | ns | $V_{DD} = 15\text{V}, I_D = 25\text{A}, R_G = 3.0\ \Omega$ |
| Turn-Off Delay Time | $t_{d(off)}$ | — | 11 | — | ns | $V_{DD} = 15\text{V}, I_D = 25\text{A}, R_G = 3.0\ \Omega$ |

## Typical circuits

### 3D Printer Heated Bed / High-Current Heater Controller (12V/24V)

At $10\text{ A}$ current draw (typical 12V 120W heated bed), power dissipation is only $P = I^2 \times R = 10^2 \times 0.0131 = 1.31\text{ W}$, allowing the MOSFET to run cool:

```
        +12V / +24V Heated Bed Supply
           │
         [ HEATED BED (120W - 250W) ]
           │
        [Pin 2: DRAIN]
         IRLB8721
        [Pin 3: SOURCE] ─── GND (Common System Ground)
           │
        [Pin 1: GATE] ◄───[ R_gate = 100Ω ]───◄ MCU Heated Bed PWM Pin
           │
        [ R_pulldown = 100kΩ ]
           │
          GND
```

## Selection & substitutes

| Part Number | $V_{DSS}$ | $I_D$ | $R_{DS(on)}$ at 4.5V | Key Advantage |
|---|---|---|---|---|
| **IRLB8721** | $30\text{ V}$ | $62\text{ A}$ | $13.1\text{ m}\Omega$ | Ultra-low gate charge ($8.4\text{ nC}$), fast switching |
| **IRLB8743** | $30\text{ V}$ | $150\text{ A}$ | $4.2\text{ m}\Omega$ | Even lower $R_{DS(on)}$ for extreme current loads ($> 20\text{A}$) |
| **IRLZ44N** | $55\text{ V}$ | $47\text{ A}$ | $25\text{ m}\Omega$ | Higher voltage rating ($55\text{V}$) |

## Common mistakes

- **Exceeding $30\text{V}$ maximum drain-source voltage:** Unlike $55\text{V}$ or $100\text{V}$ MOSFETs, the IRLB8721 has an absolute maximum $V_{DSS}$ of **$30\text{V}$**. Do not use it on $36\text{V}$ or $48\text{V}$ power systems (use the IRL540N instead).
- **Missing gate pull-down resistor:** Always install a $10\text{ k}\Omega \dots 100\text{ k}\Omega$ resistor between Gate and Source to hold the MOSFET in the OFF state while the microcontroller is powering up or flashing firmware.

## Notes

- **Suffix Identification:** The standard lead-free through-hole model is **IRLB8721PBF**.
