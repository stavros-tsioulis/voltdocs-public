## Overview

The **FQP30N06L** is a 60V, 32A N-channel logic-level power MOSFET manufactured by onsemi (originally Fairchild Semiconductor) using proprietary planar stripe **QFET** technology. Housed in a through-hole **TO-220** package, it is designed for low on-resistance, fast switching performance, and low gate charge.

Because of its low gate threshold voltage ($V_{GS(th)} = 1.0\text{V} \dots 2.5\text{V}$), the FQP30N06L can be switched directly from $3.3\text{V}$ and $5.0\text{V}$ microcontroller outputs (Arduino, ESP32, Raspberry Pi Pico) without requiring a separate high-voltage gate driver IC. It is widely used in hobby robotics for DC motor PWM speed control, solenoid and relay driving, and 12V/24V LED strip dimming.

## Quick reference

| | |
|---|---|
| **Transistor Type** | N-Channel Logic-Level Enhancement Mode MOSFET (QFET) |
| **Package** | TO-220 (Pin 1: Gate, Pin 2: Drain/Tab, Pin 3: Source) |
| **Drain-Source Voltage ($V_{DSS}$)** | $60\text{ V}$ max |
| **Continuous Drain Current ($I_D$)** | $32\text{ A}$ at $T_C = 25^\circ\text{C}$ ($22.6\text{ A}$ at $100^\circ\text{C}$) |
| **Gate Threshold Voltage ($V_{GS(th)}$)** | $1.0\text{ V}$ min to $2.5\text{ V}$ max |
| **On-Resistance ($R_{DS(on)}$)** | $35\text{ m}\Omega$ max at $V_{GS} = 10\text{V}$ / $45\text{ m}\Omega$ max at $V_{GS} = 5\text{V}$ |
| **Pulsed Drain Current ($I_{DM}$)** | $128\text{ A}$ |
| **Total Power Dissipation ($P_D$)** | $79\text{ W}$ ($T_C = 25^\circ\text{C}$) |

## Terminal identification

```
        ┌─────────┐
        │  TO-220 │
        │ 30N06L  │
        └─┬───┬───┬─┘
          1   2   3
          G   D   S
```

| Pin | Terminal | Description |
|---|---|---|
| 1 | `Gate` (`G`) | Gate control input (Connect to MCU GPIO via current-limiting resistor) |
| 2 / Tab | `Drain` (`D`) | Drain terminal / Heatsink Tab (Connect to load negative return) |
| 3 | `Source` (`S`) | Source terminal (Connect to Common System Ground 0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Drain-Source Breakdown Voltage | $V_{(BR)DSS}$ | 60 | — | — | V | $V_{GS} = 0\text{V}, I_D = 250\ \mu\text{A}$ |
| Gate Threshold Voltage | $V_{GS(th)}$ | 1.0 | — | 2.5 | V | $V_{DS} = V_{GS}, I_D = 250\ \mu\text{A}$ |
| On-Resistance ($V_{GS} = 10\text{V}$) | $R_{DS(on)}$ | — | 27 | 35 | mΩ | $V_{GS} = 10\text{V}, I_D = 16\text{A}$ |
| On-Resistance ($V_{GS} = 5\text{V}$) | $R_{DS(on)}$ | — | 35 | 45 | mΩ | $V_{GS} = 5\text{V}, I_D = 16\text{A}$ |
| Total Gate Charge | $Q_g$ | — | 15 | 20 | nC | $V_{DS} = 48\text{V}, I_D = 32\text{A}, V_{GS} = 5\text{V}$ |
| Turn-On Delay Time | $t_{d(on)}$ | — | 15 | 40 | ns | $V_{DD} = 30\text{V}, I_D = 16\text{A}, R_G = 25\ \Omega$ |
| Turn-Off Delay Time | $t_{d(off)}$ | — | 40 | 90 | ns | $V_{DD} = 30\text{V}, I_D = 16\text{A}, R_G = 25\ \Omega$ |

## Typical circuits

### Microcontroller PWM Low-Side Driver (12V/24V Load)

```
        +12V / +24V DC Supply
           │
         [ LOAD (Motor / Solenoid / High-Power LED) ]
           │
           ├─── [ Flyback Diode 1N4007 across Inductive Load ]
           │
        [Pin 2: DRAIN]
         FQP30N06L
        [Pin 3: SOURCE] ─── GND (Common System Ground)
           │
        [Pin 1: GATE] ◄───[ R_gate = 220Ω ]───◄ MCU PWM Output (3.3V / 5V)
           │
        [ R_pulldown = 10kΩ ]
           │
          GND
```

## Selection & substitutes

| Part Number | $V_{DSS}$ | $I_D$ | $R_{DS(on)}$ at 5V | Notes |
|---|---|---|---|---|
| **FQP30N06L** | $60\text{ V}$ | $32\text{ A}$ | $45\text{ m}\Omega$ | QFET planar technology, low gate charge |
| **IRLZ44N** | $55\text{ V}$ | $47\text{ A}$ | $22\text{ m}\Omega$ | Higher current rating, lower $R_{DS(on)}$ |
| **RFP30N06LE** | $60\text{ V}$ | $30\text{ A}$ | $47\text{ m}\Omega$ | Classic MegaFET equivalent |

## Common mistakes

- **Driving with standard MOSFETs (IRF series):** Standard IRF3205 or IRF540N MOSFETs require $10\text{V}$ gate voltage to fully saturate. Driving them from a $3.3\text{V}$ or $5.0\text{V}$ Arduino pin leaves them partially conductive, generating heavy heat under load. Always verify the **"L"** (Logic-Level) designation.
- **Floating Gate without a pull-down resistor:** During microcontroller startup or reset, GPIO pins are in a high-impedance floating state. Without a $10\text{ k}\Omega$ pull-down resistor to Ground on the Gate, ambient electrostatic charge can turn the MOSFET partially on, causing motor twitching or unwanted power delivery.

## Notes

- **Suffix Identification:** The "L" in FQP30N06L denotes **Logic-Level** gate threshold; FQP30N06 (without L) is the standard 10V-gate version.
