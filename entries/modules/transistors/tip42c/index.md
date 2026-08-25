## Overview

The **TIP42C** is a -100V -6A silicon power PNP bipolar junction transistor manufactured by STMicroelectronics, onsemi, and Texas Instruments. Housed in an industry-standard **TO-220AB** through-hole package, it serves as the official complementary PNP counterpart to the **TIP41C**.

Featuring a collector-emitter breakdown voltage ($V_{CEO}$) of **$-100\text{V}$**, a continuous collector current rating of **$-6.0\text{A}$** ($-10.0\text{A}$ pulsed), and a power dissipation capability of **$65\text{ Watts}$** at $T_C = 25^\circ\text{C}$, the TIP42C delivers double the current capacity of the 3A TIP32C. Paired with the TIP41C, it is widely utilized in **discrete 50W–100W Class AB hi-fi audio power amplifiers, linear bipolar split-rail bench power supplies, heavy solenoid controllers, and reversible DC motor H-bridge drivers**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | High-Current Silicon PNP Power BJT |
| **Package** | TO-220AB (3-pin through-hole) |
| **Collector-Emitter Breakdown ($V_{CEO}$)**| **$-100\text{ V}$ max** (TIP42C grade) |
| **Collector-Base Breakdown ($V_{CBO}$)** | **$-100\text{ V}$ max** |
| **Continuous Collector Current ($I_C$)** | **$-6.0\text{ A}$ max** ($-10.0\text{ A}$ pulsed) |
| **Base Current ($I_B$)** | **$-2.0\text{ A}$ max** |
| **DC Current Gain ($h_{FE}$)** | **$15$ to $75$** ($I_C = -3.0\text{A}, V_{CE} = -4.0\text{V}$) / $\ge 30$ at $-0.3\text{A}$ |
| **Collector Saturation ($V_{CE(sat)}$)** | **$-1.5\text{ V}$ max** at $I_C = -6.0\text{A}, I_B = -600\text{mA}$ |
| **Total Power Dissipation ($P_D$)** | **$65\text{ Watts}$** ($T_C = 25^\circ\text{C}$ with heatsink) / $2.0\text{ W}$ free air |
| **Transition Frequency ($f_T$)** | **$3.0\text{ MHz}$ min** |
| **Complementary NPN Pair** | **TIP41C** (100V 6A NPN) |

## Pinout (TO-220AB Package - B-C-E Standard)

Looking at the **front labeled face** with leads pointing downward:

```
        ┌──────────────┐
        │  O  [Metal]  │ ── Tab is internally connected to Pin 2 (Collector)
        ├──────────────┤
        │    TIP42C    │
        └─┬────┬────┬──┘
          1    2    3
          B    C    E
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `BASE (B)` | Base Input | Base control input (Driven with base current via driver transistor) |
| 2 (Tab) | `COLLECTOR (C)` | Power Collector | Collector terminal (Internally connected to metal mounting tab) |
| 3 | `EMITTER (E)` | Power Emitter | Emitter output (Connected to positive power rail or load) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$ | -100 | — | — | V | $I_C = -30\text{mA}, I_B = 0$ |
| Collector-Base Breakdown | $V_{(BR)CBO}$ | -100 | — | — | V | $I_C = -1.0\text{mA}, I_E = 0$ |
| Emitter-Base Breakdown | $V_{(BR)EBO}$ | -5.0 | — | — | V | $I_E = -1.0\text{mA}, I_C = 0$ |
| Collector Cutoff Current | $I_{CEO}$ | — | — | -700 | µA | $V_{CE} = -60\text{V}, I_B = 0$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 30 | — | — | — | $I_C = -0.3\text{A}, V_{CE} = -4.0\text{V}$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 15 | — | 75 | — | $I_C = -3.0\text{A}, V_{CE} = -4.0\text{V}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | — | -1.5 | V | $I_C = -6.0\text{A}, I_B = -600\text{mA}$ |
| Base-Emitter On Voltage | $V_{BE(on)}$ | — | — | -2.0 | V | $I_C = -6.0\text{A}, V_{CE} = -4.0\text{V}$ |

## Voltage Grade Breakdown

| Part Number | $V_{CEO}$ Breakdown | $V_{CBO}$ Breakdown | Application Suitability |
|---|---|---|---|
| **TIP42** | $-40\text{ V}$ | $-40\text{ V}$ | Low-voltage 12V DC circuits |
| **TIP42A** | $-60\text{ V}$ | $-60\text{ V}$ | 24V DC systems |
| **TIP42B** | $-80\text{ V}$ | $-80\text{ V}$ | 36V DC audio amplifiers |
| **TIP42C** | **$-100\text{ V}$** | **$-100\text{ V}$** | **Universal / High-Voltage (Standard Stocked Part)** |

## Comparison: TIP42C vs TIP32C vs TIP127

| Parameter | TIP32C | TIP42C | TIP127 |
|---|---|---|---|
| **Device Type** | Single Power BJT | **Single Power BJT** | Darlington Pair |
| **$V_{CEO}$ Voltage** | $-100\text{ V}$ | **$-100\text{ V}$** | $-100\text{ V}$ |
| **Max Current ($I_C$)** | $-3.0\text{ A}$ | **$-6.0\text{ A}$ (Double Current)** | $-5.0\text{ A}$ |
| **Gain ($h_{FE}$)** | $25 \dots 50$ | **$15 \dots 75$** | $\ge 1000$ (High Gain) |
| **Saturation $V_{CE(sat)}$**| $-1.2\text{ V}$ | **$-1.5\text{ V}$ (at -6A)** | $-2.0\text{ V}$ (Higher Loss) |

## Common mistakes

- **Attempting to drive directly from an MCU output:** At high load currents ($I_C = -4\text{A}$), the base requires $I_B \approx -200\text{mA} \dots -400\text{mA}$. Driving base current directly from an MCU output pin will damage the pin or leave the transistor starved for current. Always use a pre-driver BJT (like the **BD140** or **2N3906**).
- **Heatsink tab insulation:** The metal tab is internally connected to Pin 2 (Collector). When mounting complementary TIP41C and TIP42C pairs on a shared heatsink, use **mica/silicone insulating pads and nylon shoulder bushings**.

## Notes

- **Suffix Guide:** `TIP42C` is standard TO-220; `TIP42CG` denotes lead-free RoHS compliance; `TIP41C` is the complementary NPN partner.
