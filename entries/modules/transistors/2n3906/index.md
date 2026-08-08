## Overview

The **2N3906** is the industry-standard general-purpose PNP Bipolar Junction Transistor (BJT) manufactured by ON Semiconductor, STMicroelectronics, and Fairchild. It is the direct complementary PNP pair to the 2N3904 NPN transistor, widely used for high-side power switching, push-pull audio amplifiers, and inverted digital control logic.

Housed in a 3-pin **TO-92 plastic package**, the 2N3906 is rated for a collector-emitter breakdown voltage ($V_{CEO}$) of **$-40\text{ Volts}$** and continuous collector current ($I_C$) of **$-200\text{ mA}$**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | General-Purpose PNP Bipolar Junction Transistor (BJT) |
| **Package** | TO-92 (Flat face front, leads pointing down) / SOT-23 (MMBT3906) |
| **Pinout (TO-92)** | Pin 1: Emitter (`E`), Pin 2: Base (`B`), Pin 3: Collector (`C`) — **E-B-C** |
| **Collector-Emitter Voltage ($V_{CEO}$)**| $-40\text{ V}$ max |
| **Collector-Base Voltage ($V_{CBO}$)**  | $-40\text{ V}$ max |
| **Continuous Collector Current ($I_C$)**| $-200\text{ mA}$ continuous |
| **DC Current Gain ($h_{FE}$)** | $100 \dots 300$ at $I_C = -10\text{mA}, V_{CE} = -1.0\text{V}$ |
| **Transition Frequency ($f_T$)** | $250\text{ MHz}$ min |
| **Power Dissipation ($P_D$)** | $625\text{ mW}$ at $T_A = 25^\circ\text{C}$ |

## Pinout (TO-92 Package)

Looking at the **flat face** of the TO-92 package with leads pointing down:

```
        ┌─────────────┐
        │   2N3906    │  (Flat Package Face)
        └─┬───┬───┬───┘
          1   2   3
          E   B   C
```

| Pin | Name | Description |
|---|---|---|
| 1 | `EMITTER` (`E`) | Emitter terminal (Connect to $+V_{CC}$ positive supply rail) |
| 2 | `BASE` (`B`) | Base input control terminal (Pull LOW to turn ON) |
| 3 | `COLLECTOR` (`C`) | Collector terminal (High-side load output) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector Breakdown Voltage| $V_{(BR)CEO}$| -40 | — | — | V | $I_C = -1.0\text{mA}, I_B = 0$ |
| Emitter Breakdown Voltage | $V_{(BR)EBO}$| -5.0| — | — | V | $I_E = -10\ \mu\text{A}, I_C = 0$ |
| Collector Saturation Volts| $V_{CE(sat)}$| — | -0.25| -0.4 | V | $I_C = -50\text{mA}, I_B = -5.0\text{mA}$ |
| Base Saturation Voltage | $V_{BE(sat)}$| -0.65| — | -0.95| V | $I_C = -50\text{mA}, I_B = -5.0\text{mA}$ |

## High-Side PNP Switching Circuit

In high-side PNP switching, the load is connected between the Collector pin and Ground. Pulling the Base pin **LOW (0V)** turns the 2N3906 ON, supplying positive power to the load:

```
        +5V DC Power Rail
             │
        [Pin 1: EMITTER]
         2N3906
        [Pin 3: COLLECTOR] ─── [ LED / Load ] ─── GND
             │
  MCU ── [ R_B = 1kΩ ] ─── [Pin 2: BASE]
```

*(Setting MCU pin to `LOW (0V)` turns PNP ON; setting MCU pin to `HIGH (5V)` turns PNP OFF).*

## Common mistakes

- **Attempting to switch high voltages ($V_{CC} > V_{MCU}$):** Switching a 12V high-side load with a 2N3906 using a 5V MCU pin will keep the transistor permanently ON. The $5\text{V}$ output from the MCU pin is $7\text{V}$ lower than the $12\text{V}$ Emitter, maintaining base-emitter forward bias. Use an NPN driver transistor (2N3904) to pull the 2N3906 base down to GND.
- **Forgetting base current limiting resistor:** Always place a series base resistor ($470\ \Omega \dots 1\ \text{k}\Omega$) between the GPIO pin and the Base to limit base current.

## Notes

- **2N3906 vs 2N3904:** 2N3906 is PNP (Active LOW high-side switch); 2N3904 is NPN (Active HIGH low-side switch).
