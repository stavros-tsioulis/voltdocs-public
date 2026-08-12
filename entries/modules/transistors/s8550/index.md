## Overview

The **S8550** (SS8550) is a low-voltage, high-current PNP bipolar junction transistor (BJT) manufactured by Micro Commercial Components (MCC), Changjiang Electronics, and generic semiconductor foundries. Packaged in a compact **TO-92 enclosure**, it is ubiquitous in low-cost consumer electronics, toys, and beginner Arduino / Raspberry Pi component starter kits.

Optimized for high-current low-voltage switching, the S8550 handles continuous collector currents up to **$-700\text{ mA}$** (peak pulsed currents up to $-1.5\text{ A}$) at collector-emitter voltages up to **$-25\text{ Volts}$**. It is the direct PNP complementary transistor to the **S8050**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | Low-Voltage High-Current PNP BJT |
| **Package** | TO-92 (Flat face front, leads pointing down) |
| **Collector-Emitter Voltage ($V_{CEO}$)**| $-25\text{ V}$ max |
| **Collector-Base Voltage ($V_{CBO}$)**   | $-40\text{ V}$ max |
| **Continuous Collector Current ($I_C$)**| $-700\text{ mA}$ continuous ($-1500\text{ mA}$ peak) |
| **DC Current Gain ($h_{FE}$)** | 120 to 400 (Ranks: B: 120–200, C: 160–300, D: 200–400) |
| **Transition Frequency ($f_T$)** | $150\text{ MHz}$ min |
| **Power Dissipation ($P_D$)** | $625\text{ mW}$ ($T_A = 25^\circ\text{C}$) |

## Pinout (TO-92 Package)

Looking at the **flat face** of the TO-92 package with leads pointing down:

```
        ┌─────────────┐
        │    S8550    │  (Flat Package Face)
        └─┬───┬───┬───┘
          1   2   3
          E   B   C
```

| Pin | Name | Description |
|---|---|---|
| 1 | `EMITTER` (`E`) | Emitter terminal (High-side power rail $+V_{CC}$) |
| 2 | `BASE` (`B`) | Base terminal (Active LOW control input via base resistor) |
| 3 | `COLLECTOR` (`C`) | Collector terminal (Load output connection) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Voltage | $V_{CEO}$ | -25 | — | — | V | $I_C = -1\text{mA}, I_B = 0$ |
| Collector Cutoff Current | $I_{CBO}$ | — | — | -100 | nA | $V_{CB} = -35\text{V}, I_E = 0$ |
| DC Current Gain (Rank D) | $h_{FE}$ | 200 | — | 400 | — | $V_{CE} = -1\text{V}, I_C = -50\text{mA}$ |
| DC Current Gain ($I_C=500\text{mA}$)| $h_{FE}$ | 50 | — | — | — | $V_{CE} = -1\text{V}, I_C = -500\text{mA}$ |
| Collector Saturation Volts| $V_{CE(sat)}$| — | -200 | -600 | mV | $I_C = -500\text{mA}, I_B = -50\text{mA}$ |

## Common mistakes

- **Exceeding $-25\text{V}$ collector breakdown voltage:** The S8550 is specifically a **low-voltage** PNP transistor ($V_{CEO} = -25\text{V}$). Do not use it on $36\text{V}$ or $48\text{V}$ power rails; use a 2N2907A ($-60\text{V}$) or BC327 ($-45\text{V}$) instead.
- **Forgetting base current limiting resistor:** Always place a series resistor between the MCU pin and the S8550 Base to limit base current.

## Notes

- **S8550 vs S8050:** S8550 is PNP (high-side switch); S8050 is its complementary NPN pair (low-side switch). Both offer $700\text{ mA}$ current capacity in TO-92.
