## Overview

The **LT1083** (and TO-220 / TO-3P packaged **LT1083CT** / **LT1083CP**) is a 3-terminal low-dropout (LDO) positive adjustable linear voltage regulator engineered by Linear Technology (now Analog Devices). Designed to deliver up to **$7.5\text{ A}$ continuous output current**, it offers a massive current upgrade over standard LM317 regulators while slashing required input-to-output headroom down to **$1.0\text{ V}$ typical ($1.5\text{ V}$ maximum at full 7.5A load)**.

The output voltage is continuously adjustable from **$1.25\text{ V}$ to $30.0\text{ V}$** using two external resistors. Because of its outstanding ripple rejection, minimal noise, and high current capability, the LT1083 is a staple in linear laboratory bench power supplies, high-end audio power amplifier heater rails, microprocessor supplies, and post-regulators for switching supplies.

## Quick reference

| | |
|---|---|
| **Regulator Type** | High-Current Low-Dropout Positive Adjustable Regulator |
| **Package** | TO-220 (LT1083CT) / TO-3P (LT1083CP) / TO-247 / TO-3 |
| **Pinout (Front View)** | Pin 1: Adjust (`ADJ`), Pin 2: Output (`OUT`), Pin 3: Input (`IN`) |
| **Adjustable Output Range** | $1.25\text{ V}$ to $30.0\text{ V}$ DC |
| **Maximum Output Current** | $7.5\text{ A}$ (with adequate heatsinking) |
| **Dropout Voltage** | $1.0\text{ V}$ typ / $1.5\text{ V}$ max at $I_{OUT} = 7.5\text{ A}$ |
| **Internal Reference Voltage ($V_{REF}$)**| $1.250\text{ V}$ ($\pm 1\%$ trimmed accuracy) |
| **Line / Load Regulation** | $0.015\%$ Line / $0.1\%$ Load regulation |
| **Minimum Required Load** | $10\text{ mA}$ minimum load current |

## Pinout (TO-220 / TO-3P Package)

Looking at the **front labeled face** with leads pointing down and metal heatsink tab at the top:

```
        ┌──────────────┐
        │ [LT1083 Tab] │  (Metal Tab connected internally to Pin 2 OUT)
        ├──────────────┤
        │    LT1083    │  (Front Face)
        └─┬────┬────┬──┘
          1    2    3
         ADJ  OUT   IN
```

| Pin | Name | Description |
|---|---|---|
| 1 | `ADJ` | Voltage adjustment pin (Connects to feedback resistor divider) |
| 2 | `OUT` / `TAB` | Regulated DC voltage output (connected to heatsink tab) |
| 3 | `IN` | Unregulated DC input voltage |

> [!WARNING]
> On the LT1083 (unlike the LM78xx series), the **metal mounting tab is connected to Pin 2 (`OUT`)**, not Ground (`GND`). When mounting to a grounded metal chassis or heatsink, electrical mica/silicone insulators and an insulating shoulder washer are mandatory.

## Standard Adjustable Voltage Circuit

```
       +V_IN Unregulated Input
          │
       [Pin 3: IN]
        LT1083
       [Pin 2: OUT] ──────────────┬─────────────── +V_OUT Regulated DC Output
          │                       │
       [Pin 1: ADJ]          [ R1 = 121Ω 1% ]
          │                       │
          ├───────────────────────┘
          │
     [ R2 Pot / Resistor ]
          │
         GND
```

### Output Voltage Formula

The output voltage is set by the ratio of $R_1$ and $R_2$, referenced to the internal $1.25\text{V}$ bandgap voltage:

$$ V_{OUT} = 1.25\text{V} \times \left(1 + \frac{R_2}{R_1}\right) + (I_{ADJ} \times R_2) $$

Because the adjust pin current ($I_{ADJ} \approx 50\ \mu\text{A}$) is negligible, choosing $R_1 = 121\ \Omega$ simplifies the calculation:

$$ V_{OUT} \approx 1.25\text{V} \times \left(1 + \frac{R_2}{R_1}\right) $$

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Reference Voltage | $V_{REF}$ | 1.238 | 1.250 | 1.262 | V | $I_O = 10\text{mA}, T_J = 25^\circ\text{C}$ |
| Dropout Voltage | $V_d$ | — | 1.0 | 1.3 | V | $I_O = 4.0\text{A}$ |
| Dropout Voltage (Full Load) | $V_d$ | — | 1.3 | 1.5 | V | $I_O = 7.5\text{A}, T_J = 25^\circ\text{C}$ |
| Current Limit | $I_{LIMIT}$ | 8.0 | 9.5 | — | A | $(V_{IN} - V_{OUT}) \le 10\text{V}$ |
| Adjust Pin Current | $I_{ADJ}$ | — | 50 | 100 | $\mu\text{A}$ | Operating current |
| Minimum Load Current | $I_{L(MIN)}$ | — | 5.0 | 10.0 | mA | $(V_{IN} - V_{OUT}) \le 25\text{V}$ |
| Ripple Rejection Ratio | $PSRR$ | 60 | 75 | — | dB | $f = 120\text{ Hz}, C_{ADJ} = 25\ \mu\text{F}$ |

## Common mistakes

- **Omitting output capacitor or using high-ESR capacitor:** The LT1083 requires a minimum output capacitor of $10\ \mu\text{F}$ (tantalum or low-ESR electrolytic) for control loop stability. Without an output capacitor, the regulator will oscillate.
- **Shorting heatsink tab to chassis ground:** The tab is `OUT`, not `GND`. Bolting directly to a grounded chassis shorts the output directly to ground, triggering current limiting.
- **Extreme thermal dissipation at high input differentials:** Stepping down $18\text{V}$ to $5\text{V}$ at $7.5\text{A}$ produces $P_D = (18 - 5) \times 7.5 = 97.5\text{ Watts}$. Even a large heatsink will struggle with $100\text{W}$. Keep $(V_{IN} - V_{OUT})$ small ($2\text{V} \dots 4\text{V}$) for high-current applications.

## Notes

- **Family Hierarchy:** The LT108x family shares identical pinouts and characteristics across different current tiers: **LT1083** ($7.5\text{A}$), **LT1084** ($5.0\text{A}$), **LT1085** ($3.0\text{A}$), and **LT1086** ($1.5\text{A}$).
