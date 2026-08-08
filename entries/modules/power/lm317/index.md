## Overview

The **LM317** (and TO-220 packaged **LM317T**) is an iconic 3-terminal adjustable positive linear voltage regulator designed by Bob Dobkin for National Semiconductor (now Texas Instruments). Staple of benchtop variable DC power supplies, battery chargers, and DIY electronics projects, it delivers over **$1.5\text{ Amperes}$ of output current** over an adjustable output range of **$1.25\text{V}$ to $37.0\text{V}$**.

Requiring only two external resistors to set the output voltage, the LM317 features built-in internal current limiting, thermal overload shutdown, and safe-area compensation.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Adjustable Positive Linear Voltage Regulator |
| **Package** | TO-220 (LM317T) / TO-263 / SOT-223 |
| **Pinout (TO-220 Front)** | Pin 1: Adjust (`ADJ`), Pin 2: Output (`OUT`), Pin 3: Input (`IN`) |
| **Output Voltage Range** | $1.25\text{ V}$ to $37.0\text{ V}$ DC |
| **Input-Output Voltage Differential ($V_{IN} - V_{OUT}$)**| $3.0\text{ V}$ min to $40.0\text{ V}$ max |
| **Continuous Output Current ($I_{OUT}$)**| $> 1.5\text{ A}$ (with adequate heatsink) |
| **Reference Voltage ($V_{REF}$)**| $1.25\text{ V}$ (between `OUT` and `ADJ` pins) |
| **Line / Load Regulation**| $0.01\%/\text{V}$ line regulation / $0.1\%$ load regulation |

## Pinout (TO-220 Package)

Looking at the **front labeled face** of the TO-220 package with metal tab at top and leads pointing down:

```
        ┌─────────────┐
        │ [LM317T Tab]│  (Metal Tab connected internally to Pin 2 OUT)
        ├─────────────┤
        │    LM317    │  (Front Face)
        └─┬───┬───┬───┘
          1   2   3
         ADJ OUT IN
```

| Pin | Name | Description |
|---|---|---|
| 1 | `ADJ` | Voltage adjustment feedback pin |
| 2 | `OUT` / `TAB` | Regulated DC output voltage pin (connected to tab) |
| 3 | `IN` | Unregulated DC input voltage pin |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input-Output Voltage Diff | $V_I - V_O$ | 3.0 | — | 40 | V | $I_{OUT} = 1.5\text{A}$ |
| Reference Voltage | $V_{REF}$ | 1.20 | 1.25 | 1.30 | V | $3.0\text{V} \le V_I - V_O \le 40\text{V}$ |
| Peak Output Current | $I_{CL}$ | 1.5 | 2.2 | 3.4 | A | $V_I - V_O \le 15\text{V}$ |
| Minimum Load Current | $I_{L(min)}$| — | 3.5 | 10.0 | mA | To maintain regulation |
| Adjust Pin Current | $I_{ADJ}$ | — | 50 | 100 | µA | Constant bias current |
| Ripple Rejection Ratio | $RR$ | 66 | 80 | — | dB | $f = 120\text{ Hz}, C_{ADJ} = 10\ \mu\text{F}$ |

## Voltage Adjustment Math & Basic Circuit

```
       +V_IN Unregulated Input (e.g. 12V - 24V DC)
          │
       [Pin 3: IN]
        LM317T
       [Pin 2: OUT] ──────────────┬─────────────── +V_OUT Regulated DC Output
          │                       │
          ├─── [ R1 = 240Ω ] ─────┤
          │                       │
       [Pin 1: ADJ]          [ C2 = 1µF ]
          │                       │
     [ R2 = Potentiometer ]      GND
          │
         GND
```

$$ V_{OUT} = V_{REF} \times \left( 1 + \frac{R_2}{R_1} \right) + (I_{ADJ} \times R_2) $$

Given $V_{REF} = 1.25\text{V}$ and $R_1 = 240\ \Omega$ ($I_{ADJ} \approx 50\ \mu\text{A}$ is negligible):

$$ V_{OUT} \approx 1.25\text{V} \times \left( 1 + \frac{R_2}{240\ \Omega} \right) $$

### Example Resistor Calculations

- **5.0V Output:** Set $R_2 = 720\ \Omega$ (Standard $750\ \Omega$).
- **12.0V Output:** Set $R_2 = 2064\ \Omega$ (Standard $2.0\text{ k}\Omega + 68\ \Omega$).

## Common mistakes

- **Operating without a heatsink at high voltage drops:** Linear regulators dissipate power as heat: $P_D = (V_{IN} - V_{OUT}) \times I_{OUT}$. Dropping 24V to 5V at 1A creates $19\text{ Watts}$ of heat, instantly triggering thermal shutdown without a large TO-220 heatsink.
- **Forgetting minimum 10 mA load current:** If $R_1$ is selected higher than $240\ \Omega$ (e.g. $1\text{ k}\Omega$) and no load is connected, the output voltage will float up toward $V_{IN}$ due to insufficient minimum load current.

## Notes

- **LM317 vs LM7805 vs LM2596:** LM317 is an adjustable linear regulator; LM7805 is a fixed 5V linear regulator; LM2596 is a high-efficiency buck switching regulator.
