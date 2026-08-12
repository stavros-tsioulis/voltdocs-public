## Overview

The **2SA1015** (often stamped as **A1015**) is a classic general-purpose PNP bipolar junction transistor (BJT) manufactured originally by Toshiba. Packaged in a compact **TO-92 plastic housing**, it is one of the most widely used small-signal PNP transistors in Japanese and Asian audio and consumer electronics.

Designed for low-noise audio frequency amplification, small-signal high-side switching, and LED drive circuits, the 2SA1015 operates with collector-emitter voltages up to **$-50\text{ Volts}$** and continuous collector currents up to **$-150\text{ mA}$**. It is the direct PNP complementary transistor to the **2SC1815**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | PNP Bipolar Junction Transistor (BJT) |
| **Package** | TO-92 (Flat face front, leads pointing down) |
| **Collector-Emitter Voltage ($V_{CEO}$)**| $-50\text{ V}$ max |
| **Collector-Base Voltage ($V_{CBO}$)**   | $-50\text{ V}$ max |
| **Emitter-Base Voltage ($V_{EBO}$)**   | $-5.0\text{ V}$ max |
| **Continuous Collector Current ($I_C$)**| $-150\text{ mA}$ continuous ($-500\text{ mA}$ peak) |
| **DC Current Gain ($h_{FE}$)** | 70 to 400 (Ranks: O: 70–140, Y: 120–240, GR: 200–400) |
| **Transition Frequency ($f_T$)** | $80\text{ MHz}$ min ($200\text{ MHz}$ typical) |

## Pinout (TO-92 Package)

Looking at the **flat face** of the TO-92 package with leads pointing down:

```
        ┌─────────────┐
        │   A1015     │  (Flat Package Face)
        └─┬───┬───┬───┘
          1   2   3
          E   C   B
```

| Pin | Name | Description |
|---|---|---|
| 1 | `EMITTER` (`E`) | Emitter terminal (High-side power rail $+V_{CC}$) |
| 2 | `COLLECTOR` (`C`) | Collector terminal (Load output connection) |
| 3 | `BASE` (`B`) | Base terminal (Active LOW control input via base resistor) |

> [!WARNING]
> Pinout Warning: 2SA1015 Japanese E-C-B Pinout!
> - **2SA1015 (TO-92):** Pin 1 = Emitter, Pin 2 = Collector, Pin 3 = Base (**E-C-B**).
> - **2N2907 (TO-92):** Pin 1 = Emitter, Pin 2 = Base, Pin 3 = Collector (**E-B-C**).
> - **BC557 (TO-92):** Pin 1 = Collector, Pin 2 = Base, Pin 3 = Emitter (**C-B-E**).

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Voltage | $V_{CEO}$ | -50 | — | — | V | $I_C = -1\text{mA}, I_B = 0$ |
| Collector Cutoff Current | $I_{CBO}$ | — | — | -100 | nA | $V_{CB} = -50\text{V}, I_E = 0$ |
| DC Current Gain | $h_{FE}$ | 70 | — | 400 | — | $V_{CE} = -6\text{V}, I_C = -2\text{mA}$ |
| Collector Saturation Volts| $V_{CE(sat)}$| — | -100 | -300 | mV | $I_C = -100\text{mA}, I_B = -10\text{mA}$ |
| Base Saturation Voltage | $V_{BE(sat)}$| — | -850 | -1100| mV | $I_C = -100\text{mA}, I_B = -10\text{mA}$ |
| Power Dissipation | $P_C$ | — | — | 400 | mW | $T_A = 25^\circ\text{C}$ |

## Common mistakes

- **Miswiring pin leads when substituting for Western BJTs:** The 2SA1015 uses Japanese E-C-B pinout. Plugging a 2SA1015 directly into a PCB footprint designed for 2N2907 (E-B-C) or BC557 (C-B-E) causes wrong pin connections.

## Notes

- **2SA1015 vs 2SC1815:** 2SA1015 is PNP; 2SC1815 is its complementary NPN pair used in audio preamplifier input stages and push-pull output drivers.
