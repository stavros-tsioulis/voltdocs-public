## Overview

The **PN2222A** (and its metal-can variant **2N2222A**) is a ubiquitous NPN silicon Bipolar Junction Transistor (BJT) housed in a 3-pin TO-92 plastic package. Found in virtually every electronics starter kit (Elegoo, SparkFun, Adafruit), it is used for low-power signal amplification and low-side digital switching of small DC loads (relays, piezo buzzers, small DC motors, LEDs).

Capable of handling a **$40\text{V}$ collector-emitter breakdown voltage ($V_{CEO}$)** and up to **$600\text{ mA}$ continuous collector current ($I_C$)**, the PN2222A provides high DC current gain ($h_{FE} = 100 \dots 300$) and fast switching speeds up to $300\text{ MHz}$.

## Quick reference

| | |
|---|---|
| **Transistor type** | NPN Bipolar Junction Transistor (BJT) |
| **Package** | TO-92 (TO-226AA) Plastic Package |
| **Pinout (PN2222 TO-92)** | Pin 1: Emitter (`E`), Pin 2: Base (`B`), Pin 3: Collector (`C`) |
| **Collector-Emitter Voltage ($V_{CEO}$)**| $40\text{ V}$ max |
| **Collector-Base Voltage ($V_{CBO}$)** | $75\text{ V}$ max |
| **Continuous Collector Current ($I_C$)**| $600\text{ mA}$ max |
| **DC Current Gain ($h_{FE}$)** | $100\text{ to }300$ (at $I_C = 150\text{ mA}, V_{CE} = 10\text{V}$) |
| **Collector Saturation Volts ($V_{CE(sat)}$)**| $0.3\text{ V}$ max (at $I_C = 150\text{ mA}, I_B = 15\text{ mA}$) |
| **Transition Frequency ($f_T$)** | $300\text{ MHz}$ min |

## Pinout (TO-92 Package)

Looking at the **flat face** of the TO-92 package with leads pointing downwards:

```
        ┌─────────┐
        │  PN2222 │  (Flat Face Front)
        └─┬───┬───┬─┘
          1   2   3
          E   B   C
```

| Pin | Name | Description |
|---|---|---|
| 1 | `Emitter` (`E`) | Connected to ground (or negative side of load circuit) |
| 2 | `Base` (`B`) | Control input (connected to MCU GPIO via base resistor) |
| 3 | `Collector` (`C`) | Connected to negative terminal of load (switched low-side) |

> [!IMPORTANT]
> Pinout Pin Order Note:
> - Standard plastic **PN2222 / PN2222A (TO-92)** pinout order is **E-B-C** (Emitter, Base, Collector).
> - Metal-can **2N2222 / 2N2222A (TO-18)** pinout order is **E-B-C** with the tab next to Emitter. Always verify pin configuration with a multimeter or component tester before powering up.

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Voltage | $V_{CEO}$ | 40 | — | — | V | $I_C = 10\text{ mA}, I_B = 0$ |
| Collector-Base Voltage | $V_{CBO}$ | 75 | — | — | V | $I_C = 10\ \mu\text{A}, I_E = 0$ |
| Emitter-Base Voltage | $V_{EBO}$ | 6.0 | — | — | V | $I_E = 10\ \mu\text{A}, I_C = 0$ |
| Continuous Collector Current| $I_C$ | — | — | 600 | mA | Continuous DC |
| Saturation Voltage | $V_{CE(sat)}$| — | 0.2 | 0.3 | V | $I_C = 150\text{ mA}, I_B = 15\text{ mA}$ |
| Base Saturation Voltage | $V_{BE(sat)}$| 0.6 | 0.85 | 1.2 | V | $I_C = 150\text{ mA}, I_B = 15\text{ mA}$ |
| Total Power Dissipation | $P_D$ | — | — | 625 | mW | Ambient $T_A = 25^\circ\text{C}$ |

## Low-Side Switch Circuit & Base Resistor Math

To switch a 200mA load (such as a 5V relay coil) from an Arduino 5V digital pin:

```
       +5V DC Power Rail
          │
        [RELAY COIL] (5V, 200mA Load)
          │
          ├──────────────┐
          │              │
       [Collector]  [1N4007 Flyback Diode]
       PN2222 BJT        │
       [Emitter] ────────┴─────── GND (0V Common Ground)
          │
        [Base]
          │
       [1kΩ] (Base Resistor)
          │
     Arduino Digital Output Pin (5V)
```

### Base Resistor Calculation ($R_B$)

To drive the BJT into saturation ($V_{CE(sat)} \le 0.3\text{V}$), enforce a forced saturation gain $\beta_{sat} \approx 10$:

$$ I_B = \frac{I_C}{\beta_{sat}} = \frac{200\text{ mA}}{10} = 20\text{ mA} $$

$$ R_B = \frac{V_{GPIO} - V_{BE(sat)}}{I_B} = \frac{5.0\text{V} - 0.7\text{V}}{0.020\text{A}} = \frac{4.3\text{V}}{0.020\text{A}} = 215\ \Omega $$

*(A standard $220\ \Omega$ or $330\ \Omega$ base resistor ensures reliable saturation mode switching).*

## Common mistakes

- **Omitting the Base Resistor:** Connecting a 5V MCU GPIO pin directly to the BJT Base pin creates a short circuit through the forward-biased internal Base-Emitter PN junction ($V_{BE} \approx 0.7\text{V}$), destroying the MCU pin. Always include a $220\ \Omega \dots 1\ \text{k}\Omega$ base resistor.
- **Exceeding 600mA Collector Current:** Attempting to drive high-current motors ($>600\text{ mA}$) causes overheating and thermal runaway. Use a MOSFET (such as the IRLZ44N) for loads requiring $>500\text{ mA}$.

## Notes

- **PN2222 vs 2N3904 vs BC547:** PN2222 handles up to $600\text{ mA}$; 2N3904 and BC547 handle up to $200\text{ mA}$.
