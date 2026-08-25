## Overview

The **TIP41C** is a 100V 6A silicon power NPN bipolar junction transistor manufactured by STMicroelectronics, onsemi, and Texas Instruments. Housed in an industry-standard **TO-220AB** through-hole package, it is the higher-current counterpart to the ubiquitous 3A **TIP31C**.

Featuring a collector-emitter breakdown voltage ($V_{CEO}$) of **$100\text{V}$**, a continuous collector current rating of **$6.0\text{A}$** ($10.0\text{A}$ pulsed), and a power dissipation capability of **$65\text{ Watts}$** at $T_C = 25^\circ\text{C}$, the TIP41C delivers double the current-handling capacity of the TIP31C with identical pinout and package footprint. Paired with its complementary PNP power transistor **TIP42C**, it is widely used in **linear laboratory bench power supplies (0–30V 3A–5A series-pass regulators), 50W–100W discrete Class AB audio power amplifiers, relay and solenoid banks, and DC motor H-bridge speed controllers**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | High-Current Silicon NPN Power BJT |
| **Package** | TO-220AB (3-pin through-hole) |
| **Collector-Emitter Voltage ($V_{CEO}$)**| **$100\text{ V}$ max** (TIP41C grade) |
| **Collector-Base Voltage ($V_{CBO}$)** | **$100\text{ V}$ max** |
| **Continuous Collector Current ($I_C$)** | **$6.0\text{ A}$ max** ($10.0\text{ A}$ pulsed) |
| **Base Current ($I_B$)** | **$2.0\text{ A}$ max** |
| **DC Current Gain ($h_{FE}$)** | **$15$ to $75$** ($I_C = 3.0\text{A}, V_{CE} = 4.0\text{V}$) / $\ge 30$ at $0.3\text{A}$ |
| **Collector Saturation ($V_{CE(sat)}$)** | **$1.5\text{ V}$ max** at $I_C = 6.0\text{A}, I_B = 600\text{mA}$ |
| **Total Power Dissipation ($P_D$)** | **$65\text{ Watts}$** ($T_C = 25^\circ\text{C}$ with heatsink) / $2.0\text{ W}$ free air |
| **Transition Frequency ($f_T$)** | **$3.0\text{ MHz}$ min** |
| **Complementary PNP Pair** | **TIP42C** (100V 6A PNP) |

## Pinout (TO-220AB Package - B-C-E Standard)

Looking at the **front labeled face** with leads pointing downward:

```
        ┌──────────────┐
        │  O  [Metal]  │ ── Tab is internally connected to Pin 2 (Collector)
        ├──────────────┤
        │    TIP41C    │
        └─┬────┬────┬──┘
          1    2    3
          B    C    E
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `BASE` | Base Input | Base control input (Driven with base current via pre-driver BJT or op-amp stage) |
| 2 (Tab) | `COLLECTOR` | Power Collector | Collector terminal (Internally connected to metal mounting tab) |
| 3 | `EMITTER` | Power Emitter | Emitter output (Connect to load, ground, or negative rail) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$ | 100 | — | — | V | $I_C = 30\text{mA}, I_B = 0$ |
| Collector-Base Breakdown | $V_{(BR)CBO}$ | 100 | — | — | V | $I_C = 1.0\text{mA}, I_E = 0$ |
| Emitter-Base Breakdown | $V_{(BR)EBO}$ | 5.0 | — | — | V | $I_E = 1.0\text{mA}, I_C = 0$ |
| Collector Cutoff Current | $I_{CEO}$ | — | — | 700 | µA | $V_{CE} = 60\text{V}, I_B = 0$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 30 | — | — | — | $I_C = 0.3\text{A}, V_{CE} = 4.0\text{V}$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 15 | — | 75 | — | $I_C = 3.0\text{A}, V_{CE} = 4.0\text{V}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | — | 1.5 | V | $I_C = 6.0\text{A}, I_B = 600\text{mA}$ |
| Base-Emitter On Voltage | $V_{BE(on)}$ | — | — | 2.0 | V | $I_C = 6.0\text{A}, V_{CE} = 4.0\text{V}$ |

## Voltage Grade Breakdown

| Part Number | $V_{CEO}$ Breakdown | $V_{CBO}$ Breakdown | Application Suitability |
|---|---|---|---|
| **TIP41** | $40\text{ V}$ | $40\text{ V}$ | Low-voltage 12V DC circuits |
| **TIP41A** | $60\text{ V}$ | $60\text{ V}$ | 24V DC systems |
| **TIP41B** | $80\text{ V}$ | $80\text{ V}$ | 36V DC audio amplifiers |
| **TIP41C** | **$100\text{ V}$** | **$100\text{ V}$** | **Universal / High-Voltage (Standard Stocked Part)** |

## Comparison: TIP41C vs TIP31C vs TIP122

| Parameter | TIP31C | TIP41C | TIP122 |
|---|---|---|---|
| **Device Type** | Single Power BJT | **Single Power BJT** | Darlington Pair |
| **$V_{CEO}$ Voltage** | $100\text{ V}$ | **$100\text{ V}$** | $100\text{ V}$ |
| **Max Current ($I_C$)** | $3.0\text{ A}$ | **$6.0\text{ A}$ (Double Current)** | $5.0\text{ A}$ |
| **Gain ($h_{FE}$)** | $25 \dots 50$ | **$15 \dots 75$** | $\ge 1000$ (High Gain) |
| **Saturation $V_{CE(sat)}$**| $1.2\text{ V}$ | **$1.5\text{ V}$ (at 6A)** | $2.0\text{ V}$ (Higher Loss) |

## Common mistakes

- **Attempting direct microcontroller drive without a pre-driver:** At $I_C = 4\text{A}$, with $h_{FE} \approx 20$, the base requires $200\text{mA}$ of base drive current — far exceeding the $20\text{mA} \dots 40\text{mA}$ maximum pin output capability of an Arduino or STM32. Always use a small-signal pre-driver transistor (such as **2N3904** or **BD139**) or use a Darlington like the **TIP122**.
- **Assuming metal tab is isolated from the circuit:** In all standard TO-220 power BJTs, the metal tab is internally connected to Pin 2 (Collector). When mounting to a shared heatsink, use a **silicone thermal pad and insulating screw bushing**.

## Notes

- **Suffix Guide:** `TIP41C` is standard TO-220; `TIP41CG` denotes lead-free RoHS compliance; `TIP42C` is the complementary PNP partner.
