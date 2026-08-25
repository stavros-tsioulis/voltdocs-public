## Overview

The **BD136** is a classic medium-power complementary silicon PNP bipolar junction transistor manufactured by STMicroelectronics, onsemi, and NXP. Housed in a through-hole **TO-126 (SOT-32)** plastic package with a central mounting hole, it provides a rugged, heatsinkable alternative to small-signal PNP transistors.

Featuring a collector-emitter voltage ($V_{CEO}$) rating of **$-45\text{V}$**, a continuous collector current rating of **$-1.5\text{A}$** ($-3.0\text{A}$ pulsed peak), a transition frequency ($f_T$) of **$190\text{ MHz}$**, and up to **$12.5\text{ Watts}$** of power dissipation when mounted to a heatsink, the BD136 is the official PNP complement to the **BD135**. It is widely used in **complementary audio amplifier pre-driver and driver stages, high-side DC motor speed controllers, relay and solenoid switching, and linear power supply series-pass regulators**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | Medium-Power Complementary Silicon PNP BJT |
| **Package** | TO-126 / SOT-32 (3-pin through-hole with mounting hole) |
| **Collector-Emitter Breakdown ($V_{CEO}$)**| **$-45\text{ V}$ max** |
| **Collector-Base Breakdown ($V_{CBO}$)** | **$-45\text{ V}$ max** |
| **Continuous Collector Current ($I_C$)** | **$-1.5\text{ A}$ max** ($-3.0\text{ A}$ peak pulse) |
| **Base Current ($I_B$)** | **$-0.5\text{ A}$ max** |
| **DC Current Gain ($h_{FE}$)** | **$40$ to $250$** (BD136-10: 63–160, BD136-16: 100–250) |
| **Transition Frequency ($f_T$)** | **$190\text{ MHz}$ typ** ($> 50\text{ MHz}$ min) |
| **Power Dissipation ($P_D$)** | **$12.5\text{ Watts}$** ($T_C = 25^\circ\text{C}$ with heatsink) / $1.25\text{ W}$ in free air |
| **Complementary NPN Pair** | **BD135** (45V NPN) |

## Pinout (TO-126 / SOT-32 Package - E-C-B Standard)

Looking at the **printed front face** of the TO-126 package with leads pointing downward:

```
        ┌───────────────┐
        │   O [Mount]   │
        ├───────────────┤
        │     BD136     │
        └─┬─────┬─────┬─┘
          1     2     3
          E     C     B
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `EMITTER (E)` | Emitter Terminal | Emitter (Connect to positive supply rail or emitter resistor) |
| 2 | `COLLECTOR (C)`| Collector Terminal| Collector (Connected to switched load; internally bonded to rear metal tab) |
| 3 | `BASE (B)` | Base Terminal | Base control input (Driven with base current via series resistor or input stage) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$ | -45 | — | — | V | $I_C = -10\text{mA}, I_B = 0$ |
| Collector-Base Breakdown | $V_{(BR)CBO}$ | -45 | — | — | V | $I_C = -100\ \mu\text{A}, I_E = 0$ |
| Emitter-Base Breakdown | $V_{(BR)EBO}$ | -5.0 | — | — | V | $I_E = -10\ \mu\text{A}, I_C = 0$ |
| Collector Cutoff Current | $I_{CBO}$ | — | — | -100 | nA | $V_{CB} = -30\text{V}, I_E = 0$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 40 | — | 250 | — | $I_C = -150\text{mA}, V_{CE} = -2.0\text{V}$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 25 | — | — | — | $I_C = -500\text{mA}, V_{CE} = -2.0\text{V}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | — | -0.50 | V | $I_C = -500\text{mA}, I_B = -50\text{mA}$ |
| Base Saturation Voltage | $V_{BE(sat)}$ | — | — | -1.00 | V | $I_C = -500\text{mA}, I_B = -50\text{mA}$ |

## Comparison: BD136 vs BD138 vs BD140

| Parameter | BD136 | BD138 | BD140 |
|---|---|---|---|
| **$V_{CEO}$ Voltage** | **$-45\text{ V}$** | $-60\text{ V}$ | **$-80\text{ V}$** |
| **Max Current ($I_C$)** | $-1.5\text{ A}$ | $-1.5\text{ A}$ | $-1.5\text{ A}$ |
| **Transition Freq ($f_T$)**| $190\text{ MHz}$ | $190\text{ MHz}$ | $190\text{ MHz}$ |
| **Complementary NPN** | **BD135** | BD137 | **BD139** |

## Common mistakes

- **Assuming TO-92 (E-B-C) pinout:** The TO-126 BD136 uses the European standard **`Emitter - Collector - Base` (E-C-B)** sequence from left to right. Swapping the base and collector leads is the most common assembly error.
- **Mounting to a heatsink without electrical insulation:** The metal rear backing tab is internally bonded to Pin 2 (Collector). When mounting to a grounded chassis or shared heatsink, use a **silicone thermal pad and insulating bushing**.

## Notes

- **Gain Grouping:** Sub-grades are marked on the package: `-6` ($h_{FE} = 40 \dots 100$), `-10` ($h_{FE} = 63 \dots 160$), and `-16` ($h_{FE} = 100 \dots 250$).
