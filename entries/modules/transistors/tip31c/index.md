## Overview

The **TIP31C** is a general-purpose NPN power bipolar junction transistor (BJT) manufactured by STMicroelectronics and ON Semiconductor. Packaged in a robust **TO-220AB enclosure**, it is designed for medium-power linear voltage regulators, audio power amplifiers, motor speed controls, and high-voltage DC load switching.

Supporting collector-emitter voltages up to **$100\text{ Volts}$** and continuous collector currents up to **$3.0\text{ Amps}$** (with peak currents up to $5.0\text{ A}$), the TIP31C is frequently paired with its PNP complementary power transistor, the **TIP32C**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | NPN Power Bipolar Junction Transistor |
| **Package** | TO-220AB (Metal tab connected to COLLECTOR) |
| **Collector-Emitter Voltage ($V_{CEO}$)**| $100\text{ V}$ max |
| **Collector-Base Voltage ($V_{CBO}$)**   | $100\text{ V}$ max |
| **Continuous Collector Current ($I_C$)**| $3.0\text{ A}$ continuous ($5.0\text{ A}$ peak) |
| **Base Current ($I_B$)** | $1.0\text{ A}$ max |
| **DC Current Gain ($h_{FE}$)** | 25 to 50 at $I_C = 1.0\text{A}$ ($10\dots50$ at $I_C = 3.0\text{A}$) |
| **Transition Frequency ($f_T$)** | $3.0\text{ MHz}$ min |
| **Power Dissipation ($P_D$)** | $40\text{ W}$ ($T_C = 25^\circ\text{C}$) / $2.0\text{ W}$ ($T_A = 25^\circ\text{C}$) |

## Pinout (TO-220AB Package)

Looking at the **front labeled face** of the TO-220 package with leads pointing down:

```
        ┌─────────────┐
        │   O   [TAB] │  (Metal Mounting Tab = COLLECTOR)
        ├─────────────┤
        │   TIP31C    │  (Front Package Face)
        └─┬───┬───┬───┘
          1   2   3
          B   C   E
```

| Pin | Name | Description |
|---|---|---|
| 1 | `BASE` (`B`) | Base control input |
| 2 | `COLLECTOR` (`C`) | Collector terminal (Connected internally to tab) |
| 3 | `EMITTER` (`E`) | Emitter terminal (Ground reference 0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$| 100 | — | — | V | $I_C = 30\text{mA}, I_B = 0$ |
| DC Current Gain ($I_C=1\text{A}$)| $h_{FE}$ | 25 | — | 50 | — | $V_{CE} = 4\text{V}, I_C = 1\text{A}$ |
| DC Current Gain ($I_C=3\text{A}$)| $h_{FE}$ | 10 | — | 50 | — | $V_{CE} = 4\text{V}, I_C = 3\text{A}$ |
| Collector Saturation Volts| $V_{CE(sat)}$| — | — | 1.2 | V | $I_C = 3\text{A}, I_B = 375\text{mA}$ |
| Base-Emitter Voltage | $V_{BE(on)}$ | — | — | 1.8 | V | $V_{CE} = 4\text{V}, I_C = 3\text{A}$ |

## Common mistakes

- **Expecting high gain from an MCU GPIO pin:** Unlike Darlington transistors (such as TIP120 with $h_{FE} \ge 1000$), the TIP31C has a relatively low DC current gain ($h_{FE} \approx 25$). To switch a $1.0\text{ A}$ load, the Base requires $I_B \approx 40\text{ mA}$, which exceeds the safe pin current limit of most microcontrollers ($20\text{ mA}$). Use a pre-driver transistor (e.g. 2N3904) or a Darlington/MOSFET.
- **Operating without a heatsink at high power levels:** When conducting $2\text{A}$, $V_{CE(sat)}$ power dissipation reaches $\sim 2.4\text{ Watts}$. A heatsink is necessary to prevent thermal shutdown.

## Notes

- **TIP31 vs TIP31A vs TIP31B vs TIP31C:** TIP31 (40V), TIP31A (60V), TIP31B (80V), TIP31C (100V). The "C" suffix version is the most common because it covers all lower voltage requirements.
