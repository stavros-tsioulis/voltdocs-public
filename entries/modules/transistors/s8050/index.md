## Overview

The **S8050** (and SMD SOT-23 variant marked **J3Y**) is a low-voltage, high-current NPN silicon Bipolar Junction Transistor (BJT) housed in a 3-pin TO-92 plastic package. Widely included in Elegoo, SunFounder, and generic Arduino starter kits alongside its PNP complementary counterpart (the S8550), it is designed for driving small DC motors, relays, buzzers, and high-brightness LEDs.

Optimized for higher current handling than standard small-signal BJTs (such as the 2N3904 or BC547), the S8050 supports a continuous **collector current ($I_C$) of $700\text{ mA}$** ($1.5\text{ A}$ peak pulse) with a **$25\text{V}$ collector-emitter breakdown voltage ($V_{CEO}$)** and high DC current gain ($h_{FE} = 120 \dots 400$).

## Quick reference

| | |
|---|---|
| **Transistor type** | NPN Bipolar Junction Transistor (BJT) |
| **Package** | TO-92 (EBC) / SOT-23 SMD (Marked `J3Y`) |
| **Pinout (TO-92 Front)** | Pin 1: Emitter (`E`), Pin 2: Base (`B`), Pin 3: Collector (`C`) |
| **Collector-Emitter Voltage ($V_{CEO}$)**| $25\text{ V}$ max |
| **Collector-Base Voltage ($V_{CBO}$)** | $40\text{ V}$ max |
| **Continuous Collector Current ($I_C$)**| $700\text{ mA}$ max ($1.5\text{ A}$ peak) |
| **DC Current Gain ($h_{FE}$)** | $120\text{ to }400$ (Rank D: 160–300, Rank E: 200–400) |
| **Collector Saturation Volts ($V_{CE(sat)}$)**| $0.5\text{ V}$ max (at $I_C = 500\text{ mA}, I_B = 50\text{ mA}$) |
| **Total Power Dissipation ($P_D$)** | $1000\text{ mW}$ ($1.0\text{ W}$) max |

## Pinout (TO-92 Package)

Looking at the **flat printed face** of the TO-92 package with leads pointing downwards:

```
        ┌─────────┐
        │  S8050  │  (Flat Face Front)
        └─┬───┬───┬─┘
          1   2   3
          E   B   C
```

| Pin | Name | Description |
|---|---|---|
| 1 | `Emitter` (`E`) | Connected to ground reference (0 V) |
| 2 | `Base` (`B`) | Control input (connected to MCU GPIO via base resistor) |
| 3 | `Collector` (`C`) | Connected to negative side of switched DC load |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Voltage | $V_{CEO}$ | 25 | — | — | V | $I_C = 1\text{ mA}, I_B = 0$ |
| Collector-Base Voltage | $V_{CBO}$ | 40 | — | — | V | $I_C = 100\ \mu\text{A}, I_E = 0$ |
| Emitter-Base Voltage | $V_{EBO}$ | 5.0 | — | — | V | $I_E = 100\ \mu\text{A}, I_C = 0$ |
| Collector Current Continuous| $I_C$ | — | — | 700 | mA | DC continuous |
| Collector Saturation Volts | $V_{CE(sat)}$| — | 0.2 | 0.5 | V | $I_C = 500\text{ mA}, I_B = 50\text{ mA}$ |
| Base Saturation Voltage | $V_{BE(sat)}$| — | 0.9 | 1.2 | V | $I_C = 500\text{ mA}, I_B = 50\text{ mA}$ |
| Transition Frequency | $f_T$ | 150 | — | — | MHz | $V_{CE} = 10\text{V}, I_C = 50\text{ mA}$ |

## Low-Side Switch Circuit & Base Resistor Calculation

To drive a 300 mA small DC motor or 5V relay coil from a 5V microcontroller GPIO pin:

```
       +5V DC Power Rail
          │
        [DC MOTOR / RELAY] (5V, 300mA Load)
          │
          ├──────────────┐
          │              │
       [Collector]  [1N4007 Flyback Diode]
        S8050 BJT        │
       [Emitter] ────────┴─────── GND (0V Common Ground)
          │
        [Base]
          │
       [150Ω] (Base Resistor)
          │
     Arduino Digital Output Pin (5V)
```

$$ I_B = \frac{I_C}{\beta_{sat}} = \frac{300\text{ mA}}{10} = 30\text{ mA} $$

$$ R_B = \frac{V_{GPIO} - V_{BE(sat)}}{I_B} = \frac{5.0\text{V} - 0.8\text{V}}{0.030\text{A}} = \frac{4.2\text{V}}{0.030\text{A}} = 140\ \Omega $$

*(Use a standard $150\ \Omega$ or $220\ \Omega$ base resistor for 5V logic).*

## Common mistakes

- **Mixing up S8050 (NPN) and S8550 (PNP):** Elegoo starter kit component bags frequently include both S8050 and S8550 transistors in identical TO-92 packages. S8050 is **NPN** (switches low-side to GND); S8550 is **PNP** (switches high-side to $V_{CC}$).
- **Forgetting flyback protection on motors:** Inductive back-EMF voltage spikes generated when switching off DC motors will exceed the $25\text{V}\ V_{CEO}$ rating, causing collector-emitter breakdown. Always place a 1N4007 flyback diode across inductive loads.

## Notes

- **S8050 vs 2N2222 vs 2N3904:** S8050 handles up to $700\text{ mA}$ at $25\text{V}$; PN2222A handles up to $600\text{ mA}$ at $40\text{V}$; 2N3904 handles up to $200\text{ mA}$ at $40\text{V}$.
