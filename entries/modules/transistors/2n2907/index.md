## Overview

The **2N2907** (2N2907A / PN2907A) is a high-speed PNP general-purpose bipolar junction transistor (BJT) manufactured by ON Semiconductor, Microchip, and STMicroelectronics. It is the direct PNP complementary transistor to the iconic **2N2222** NPN transistor.

Enclosed in a **TO-92 plastic package** (PN2907), **TO-18 metal can** (2N2907), or **SOT-23 SMD** package (MMBT2907), it handles collector-emitter voltages up to **$-60\text{ Volts}$** and continuous collector currents up to **$-600\text{ mA}$** (with peak currents up to $-1.0\text{ A}$). It is widely used for high-side power switching, LED drivers, push-pull audio stages, and core memory logic.

## Quick reference

| | |
|---|---|
| **Transistor Type** | PNP Bipolar Junction Transistor (BJT) |
| **Package** | TO-92 (PN2907A) / TO-18 (2N2907A) / SOT-23 (MMBT2907A) |
| **Collector-Emitter Voltage ($V_{CEO}$)**| $-60\text{ V}$ max |
| **Collector-Base Voltage ($V_{CBO}$)**   | $-60\text{ V}$ max |
| **Continuous Collector Current ($I_C$)**| $-600\text{ mA}$ continuous ($-1000\text{ mA}$ peak) |
| **DC Current Gain ($h_{FE}$)** | 100 to 300 (at $I_C = -150\text{mA}, V_{CE} = -10\text{V}$) |
| **Transition Frequency ($f_T$)** | $200\text{ MHz}$ min ($300\text{ MHz}$ typical) |
| **Power Dissipation ($P_D$)** | $625\text{ mW}$ ($T_A = 25^\circ\text{C}$, TO-92) |

## Pinout (TO-92 Package — PN2907A)

Looking at the **flat face** of the TO-92 package with leads pointing down:

```
        ┌─────────────┐
        │   PN2907A   │  (Flat Package Face)
        └─┬───┬───┬───┘
          1   2   3
          E   B   C
```

| Pin | Name | Description |
|---|---|---|
| 1 | `EMITTER` (`E`) | Emitter terminal (High-side power rail $+V_{CC}$) |
| 2 | `BASE` (`B`) | Base terminal (Active LOW control input via base resistor) |
| 3 | `COLLECTOR` (`C`) | Collector terminal (Output to load) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$| -60 | — | — | V | $I_C = -10\text{mA}, I_B = 0$ |
| DC Current Gain | $h_{FE}$ | 100 | — | 300 | — | $V_{CE} = -10\text{V}, I_C = -150\text{mA}$ |
| DC Current Gain (High $I_C$) | $h_{FE}$ | 50 | — | — | — | $V_{CE} = -10\text{V}, I_C = -500\text{mA}$ |
| Collector Saturation Volts| $V_{CE(sat)}$| — | -200 | -400 | mV | $I_C = -150\text{mA}, I_B = -15\text{mA}$ |
| Base Saturation Voltage | $V_{BE(sat)}$| — | -900 | -1300| mV | $I_C = -150\text{mA}, I_B = -15\text{mA}$ |

## Common mistakes

- **Using PNP as low-side switch:** PNP transistors are designed for **high-side switching** (Emitter connected to $+V_{CC}$, Collector connected to Load). When using a PNP as a high-side switch with a $+12\text{V}$ power rail, a $3.3\text{V}$ or $5\text{V}$ MCU pin cannot turn the transistor OFF because $V_{BE}$ remains $12\text{V} - 5\text{V} = 7\text{V} > 0.7\text{V}$. Use an NPN pre-driver transistor.

## Notes

- **2N2907 vs 2N2222:** 2N2907 is PNP (high-side switch); 2N2222 is NPN (low-side switch). They are designed as complementary pairs for push-pull output stages.
