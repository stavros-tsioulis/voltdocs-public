## Overview

The **2N3055** is a legendary complementary NPN silicon power transistor manufactured by ON Semiconductor and STMicroelectronics. Introduced originally by RCA in the 1960s, it is one of the most famous power semiconductors in history. Enclosed in a heavy-duty **TO-3 metal can package**, it offers high thermal dissipation and rugged reliability.

Supporting collector-emitter voltages up to **$60\text{ Volts}$**, continuous collector currents up to **$15\text{ Amps}$**, and a total power dissipation rating of **$115\text{ Watts}$** (at $T_C = 25^\circ\text{C}$), the 2N3055 is widely used in high-power linear bench supplies, high-fidelity class-AB audio power amplifiers, motor speed controllers, and DC power switches. Its PNP complementary counterpart is the **MJ2955**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | NPN Power Bipolar Junction Transistor |
| **Package** | TO-3 (Hermetic Metal Can — Case is connected to COLLECTOR) |
| **Collector-Emitter Voltage ($V_{CEO}$)**| $60\text{ V}$ max |
| **Collector-Base Voltage ($V_{CBO}$)**   | $100\text{ V}$ max |
| **Continuous Collector Current ($I_C$)**| $15.0\text{ A}$ continuous |
| **Base Current ($I_B$)** | $7.0\text{ A}$ max |
| **DC Current Gain ($h_{FE}$)** | 20 to 70 at $I_C = 4.0\text{A}$ ($h_{FE} \ge 5$ at $10\text{A}$) |
| **Transition Frequency ($f_T$)** | $2.5\text{ MHz}$ min |
| **Total Power Dissipation ($P_D$)** | $115\text{ W}$ at $T_C = 25^\circ\text{C}$ |

## Pinout (TO-3 Metal Can Package)

Looking at the **bottom pin side** of the TO-3 metal can with pins pointing toward you:

```
               ┌─────────────────┐
               │    ( ( O ) )    │  Mounting Hole 1
               │                 │
               │   (1)     (2)   │
               │    B       E    │
               │                 │
               │    ( ( O ) )    │  Mounting Hole 2
               └─────────────────┘
           Metal Case = ( C ) COLLECTOR
```

| Pin | Name | Description |
|---|---|---|
| 1 | `BASE` (`B`) | Base terminal (Thinner pin, off-center offset left) |
| 2 | `EMITTER` (`E`) | Emitter terminal (Thinner pin, off-center offset right) |
| Case | `COLLECTOR` (`C`) | Outer metal case and mounting holes (Collector terminal) |

> [!WARNING]
> Metal Case Warning: Case is live Collector!
> The TO-3 metal outer case is internally tied directly to the **Collector**. When mounting a 2N3055 onto a metal heatsink, always use a **mica or silicone insulating washer** and non-conductive mounting shoulder bushings to prevent shorting the Collector to ground.

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Sustaining Voltage | $V_{CEO(sus)}$| 60 | — | — | V | $I_C = 200\text{mA}, I_B = 0$ |
| DC Current Gain ($I_C=4\text{A}$)| $h_{FE}$ | 20 | — | 70 | — | $V_{CE} = 4\text{V}, I_C = 4\text{A}$ |
| DC Current Gain ($I_C=10\text{A}$)| $h_{FE}$ | 5 | — | — | — | $V_{CE} = 4\text{V}, I_C = 10\text{A}$ |
| Collector Saturation Volts| $V_{CE(sat)}$| — | 1.1 | 3.0 | V | $I_C = 10\text{A}, I_B = 3.3\text{A}$ |
| Base-Emitter On Voltage | $V_{BE(on)}$ | — | — | 1.8 | V | $V_{CE} = 4\text{V}, I_C = 4\text{A}$ |

## Common mistakes

- **Forgetting base drive requirements at high collector currents:** At $I_C = 10\text{A}$, $h_{FE}$ drops to 5-10, requiring a base current $I_B \ge 1\text{A}$ to saturate. Always use a driver transistor (such as a TIP31C or BD139) to supply sufficient base drive.
- **Shorting collector to heatsink:** Mounting the TO-3 case onto a grounded chassis without a mica insulator creates an immediate short circuit on the high-voltage supply rail.

## Notes

- **2N3055 vs MJ2955:** 2N3055 is NPN; MJ2955 is its complementary PNP counterpart used in push-pull power output stages.
