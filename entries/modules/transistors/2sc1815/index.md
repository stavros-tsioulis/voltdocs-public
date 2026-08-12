## Overview

The **2SC1815** (often stamped simply as **C1815**) is a legendary general-purpose NPN bipolar junction transistor (BJT) manufactured originally by Toshiba and widely produced across the electronics industry. Enclosed in a standard **TO-92 package**, it is one of the most famous small-signal transistors in Japanese and Asian consumer electronics history.

Designed for low-noise audio frequency amplification, signal switching, relay drivers, and oscillator circuits, the 2SC1815 handles collector-emitter voltages up to **$50\text{ Volts}$** and continuous collector currents up to **$150\text{ mA}$**. It is commonly paired with its PNP complementary counterpart, the **2SA1015**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | NPN Bipolar Junction Transistor (BJT) |
| **Package** | TO-92 (Flat face front, leads pointing down) |
| **Collector-Emitter Voltage ($V_{CEO}$)**| $50\text{ V}$ max |
| **Collector-Base Voltage ($V_{CBO}$)**   | $60\text{ V}$ max |
| **Emitter-Base Voltage ($V_{EBO}$)**   | $5.0\text{ V}$ max |
| **Continuous Collector Current ($I_C$)**| $150\text{ mA}$ continuous ($500\text{ mA}$ pulsed) |
| **DC Current Gain ($h_{FE}$)** | 70 to 700 (Ranks: O: 70–140, Y: 120–240, GR: 200–400, BL: 350–700) |
| **Transition Frequency ($f_T$)** | $80\text{ MHz}$ min ($250\text{ MHz}$ typical) |

## Pinout (TO-92 Package)

Looking at the **flat face** of the TO-92 package with leads pointing down:

```
        ┌─────────────┐
        │   C1815     │  (Flat Package Face)
        └─┬───┬───┬───┘
          1   2   3
          E   C   B
```

| Pin | Name | Description |
|---|---|---|
| 1 | `EMITTER` (`E`) | Emitter terminal (Ground reference 0 V) |
| 2 | `COLLECTOR` (`C`) | Collector terminal (Load connection) |
| 3 | `BASE` (`B`) | Base terminal (Control input via current-limiting resistor) |

> [!WARNING]
> Pinout Warning: 2SC1815 vs 2N3904 / BC547 Pinouts!
> - **2SC1815 (TO-92):** Pin 1 = Emitter, Pin 2 = Collector, Pin 3 = Base (**E-C-B**).
> - **2N3904 (TO-92):** Pin 1 = Emitter, Pin 2 = Base, Pin 3 = Collector (**E-B-C**).
> - **BC547 (TO-92):** Pin 1 = Collector, Pin 2 = Base, Pin 3 = Emitter (**C-B-E**).
> - Substituting a 2SC1815 for a 2N3904 or BC547 without checking the pinout will result in wrong lead connections!

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Voltage | $V_{CEO}$ | 50 | — | — | V | $I_C = 1\text{mA}, I_B = 0$ |
| Collector Cutoff Current | $I_{CBO}$ | — | — | 100 | nA | $V_{CB} = 60\text{V}, I_E = 0$ |
| DC Current Gain | $h_{FE}$ | 70 | — | 700 | — | $V_{CE} = 6\text{V}, I_C = 2\text{mA}$ |
| Collector Saturation Volts | $V_{CE(sat)}$| — | 0.1 | 0.25 | V | $I_C = 100\text{mA}, I_B = 10\text{mA}$ |
| Base Saturation Voltage | $V_{BE(sat)}$| — | — | 1.0 | V | $I_C = 100\text{mA}, I_B = 10\text{mA}$ |
| Power Dissipation | $P_C$ | — | — | 400 | mW | $T_A = 25^\circ\text{C}$ |

## Common mistakes

- **Assuming E-B-C pinout:** Japanese 2S-series TO-92 BJTs (like 2SC1815 and 2SA1015) use **E-C-B** pin layout (Pin 1 Emitter, Pin 2 Collector, Pin 3 Base). Beginners swapping 2SC1815 with Western 2N3904 (E-B-C) or European BC547 (C-B-E) often miswire the Base and Collector.
- **Omitting Base resistor ($R_B$):** BJTs are current-driven devices. Connecting an MCU GPIO pin directly to the Base destroys the base-emitter junction ($V_{BE} \approx 0.7\text{V}$). Always include a series Base resistor (e.g. $1\text{ k}\Omega$ to $10\text{ k}\Omega$).

## Notes

- **2SC1815 vs 2SA1015:** 2SC1815 is NPN; 2SA1015 is its complementary PNP counterpart used in push-pull audio stages.
