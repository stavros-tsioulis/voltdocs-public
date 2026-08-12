## Overview

The **TIP32C** is a general-purpose PNP power bipolar junction transistor (BJT) manufactured by STMicroelectronics and ON Semiconductor. Enclosed in a **TO-220AB package**, it is designed for medium-power linear voltage regulators, audio power amplifiers, motor speed control, and high-side DC load switching.

Supporting collector-emitter voltages up to **$-100\text{ Volts}$** and continuous collector currents up to **$-3.0\text{ Amps}$** (with peak currents up to $-5.0\text{ A}$), the TIP32C is the direct PNP complementary power transistor to the **TIP31C**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | PNP Power Bipolar Junction Transistor |
| **Package** | TO-220AB (Metal tab connected to COLLECTOR) |
| **Collector-Emitter Voltage ($V_{CEO}$)**| $-100\text{ V}$ max |
| **Collector-Base Voltage ($V_{CBO}$)**   | $-100\text{ V}$ max |
| **Continuous Collector Current ($I_C$)**| $-3.0\text{ A}$ continuous ($-5.0\text{ A}$ peak) |
| **Base Current ($I_B$)** | $-1.0\text{ A}$ max |
| **DC Current Gain ($h_{FE}$)** | 25 to 50 at $I_C = -1.0\text{A}$ ($10\dots50$ at $I_C = -3.0\text{A}$) |
| **Transition Frequency ($f_T$)** | $3.0\text{ MHz}$ min |
| **Power Dissipation ($P_D$)** | $40\text{ W}$ ($T_C = 25^\circ\text{C}$) / $2.0\text{ W}$ ($T_A = 25^\circ\text{C}$) |

## Pinout (TO-220AB Package)

Looking at the **front labeled face** of the TO-220 package with leads pointing down:

```
        ┌─────────────┐
        │   O   [TAB] │  (Metal Mounting Tab = COLLECTOR)
        ├─────────────┤
        │   TIP32C    │  (Front Package Face)
        └─┬───┬───┬───┘
          1   2   3
          B   C   E
```

| Pin | Name | Description |
|---|---|---|
| 1 | `BASE` (`B`) | Base control input |
| 2 | `COLLECTOR` (`C`) | Collector terminal (Connected internally to tab) |
| 3 | `EMITTER` (`E`) | Emitter terminal (High-side power rail $+V_{CC}$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$| -100 | — | — | V | $I_C = -30\text{mA}, I_B = 0$ |
| DC Current Gain ($I_C=-1\text{A}$)| $h_{FE}$ | 25 | — | 50 | — | $V_{CE} = -4\text{V}, I_C = -1\text{A}$ |
| DC Current Gain ($I_C=-3\text{A}$)| $h_{FE}$ | 10 | — | 50 | — | $V_{CE} = -4\text{V}, I_C = -3\text{A}$ |
| Collector Saturation Volts| $V_{CE(sat)}$| — | — | -1.2 | V | $I_C = -3\text{A}, I_B = -375\text{mA}$ |
| Base-Emitter Voltage | $V_{BE(on)}$ | — | — | -1.8 | V | $V_{CE} = -4\text{V}, I_C = -3\text{A}$ |

## Common mistakes

- **Driving directly from MCU GPIO on high-voltage supply rails:** With $h_{FE} \approx 25$, switching a $-3\text{A}$ load requires an $I_B$ base current of $\sim 100\text{ mA}$, far beyond an MCU GPIO pin limit ($20\text{ mA}$). Use an NPN pre-driver transistor (such as 2N3904 or BC337).
- **Omitting heatsink under continuous load:** At $2\text{A}$ output current, $V_{CE(sat)}$ power dissipation reaches $\sim 2.4\text{ Watts}$. A heatsink is necessary to avoid thermal damage.

## Notes

- **TIP32 vs TIP32A vs TIP32B vs TIP32C:** TIP32 (-40V), TIP32A (-60V), TIP32B (-80V), TIP32C (-100V). The "C" suffix version is the most common because it handles higher DC supply voltages.
