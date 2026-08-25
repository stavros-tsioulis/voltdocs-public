## Overview

The **TIP127** (along with **TIP125** and **TIP126**) is a -100V -5A complementary silicon PNP power Darlington transistor manufactured by STMicroelectronics, onsemi, and Texas Instruments. Housed in an industry-standard **TO-220AB** through-hole package, it serves as the official PNP complement to the iconic **TIP122** (and TIP120/TIP121 series).

Monolithically integrating two cascaded PNP transistors in a Darlington configuration with built-in base-emitter bleed resistors and an integrated anti-parallel **damper protection diode**, the TIP127 provides high current gain ($h_{FE} \ge 1000$). It allows high-current $3\text{A} \dots 5\text{A}$ high-side inductive loads to be switched on $24\text{V} \dots 48\text{V}$ power rails using a modest base pull-down current of just a few milliamps. The TIP127 is standard equipment in **discrete high-power H-bridge bidirectional DC motor drivers, high-side automotive relay switches, audio amplifier power stages, and industrial solenoid controllers**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | Monolithic PNP Silicon Power Darlington BJT |
| **Package** | TO-220AB (3-pin through-hole) |
| **Collector-Emitter Breakdown ($V_{CEO}$)**| **$-100\text{ V}$ max (TIP127)** / **$-60\text{ V}$ max (TIP125)** |
| **Collector-Base Breakdown ($V_{CBO}$)** | **$-100\text{ V}$ max (TIP127)** / **$-60\text{ V}$ max (TIP125)** |
| **Continuous Collector Current ($I_C$)** | **$-5.0\text{ A}$ max** ($-8.0\text{ A}$ pulsed) |
| **Base Current ($I_B$)** | **$-0.12\text{ A}$** ($-120\text{ mA}$) |
| **DC Current Gain ($h_{FE}$)** | **$1000$ min** ($1000 \dots 5000$ at $I_C = -3.0\text{A}, V_{CE} = -3.0\text{V}$) |
| **Collector Saturation ($V_{CE(sat)}$)** | **$-2.0\text{ V}$ max** at $I_C = -3.0\text{A}$ ($-4.0\text{ V}$ max at $-5.0\text{A}$) |
| **Total Power Dissipation ($P_D$)** | **$65\text{ Watts}$** ($T_C = 25^\circ\text{C}$ with heatsink) / $2.0\text{ W}$ free air |
| **Integrated Components** | Base-Emitter Bleed Resistors + Flywheel Clamping Diode |
| **Complementary NPN Pair** | **TIP122 (100V NPN) / TIP120 (60V NPN)** |

## Pinout (TO-220AB Package - B-C-E Standard)

Looking at the **front labeled face** with leads pointing downward:

```
        ┌──────────────┐
        │  O  [Metal]  │ ── Tab is internally connected to Pin 2 (Collector)
        ├──────────────┤
        │    TIP127    │
        └─┬────┬────┬──┘
          1    2    3
          B    C    E
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `BASE (B)` | Base Input | Base control input (Driven LOW to turn ON via small NPN driver) |
| 2 (Tab) | `COLLECTOR (C)` | Power Collector | Collector output (Connected to load; internally bonded to metal tab) |
| 3 | `EMITTER (E)` | Power Emitter | Emitter terminal (Connected to positive supply rail, e.g. $+24\text{V} \dots +48\text{V}$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$ | -100 | — | — | V | $I_C = -30\text{mA}, I_B = 0$ (TIP127) |
| Collector-Emitter Breakdown | $V_{(BR)CEO}$ | -60 | — | — | V | $I_C = -30\text{mA}, I_B = 0$ (TIP125) |
| Collector-Base Breakdown | $V_{(BR)CBO}$ | -100 | — | — | V | $I_C = -1.0\text{mA}, I_E = 0$ (TIP127) |
| Emitter-Base Breakdown | $V_{(BR)EBO}$ | -5.0 | — | — | V | $I_E = -2.0\text{mA}, I_C = 0$ |
| Collector Cutoff Current | $I_{CEO}$ | — | — | -500 | µA | $V_{CE} = -50\text{V}, I_B = 0$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 1000 | — | — | — | $I_C = -0.5\text{A}, V_{CE} = -3.0\text{V}$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 1000 | — | — | — | $I_C = -3.0\text{A}, V_{CE} = -3.0\text{V}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | — | -2.0 | V | $I_C = -3.0\text{A}, I_B = -12\text{mA}$ |
| Base-Emitter On Voltage | $V_{BE(on)}$ | — | — | -2.5 | V | $I_C = -3.0\text{A}, V_{CE} = -3.0\text{V}$ |

## Typical Application Circuit: Discrete Full H-Bridge DC Motor Driver

In an H-bridge, two high-side TIP127 (PNP) Darlington transistors pair with two low-side TIP122 (NPN) Darlington transistors:

```
                            +24V Motor Power Rail
                                      │
                 ┌────────────────────┴────────────────────┐
                 │                                         │
          [Pin 3: EMITTER]                          [Pin 3: EMITTER]
            TIP127 (Left High)                        TIP127 (Right High)
  NPN ───►[Pin 1: BASE]                             [Pin 1: BASE]◄─── NPN
          [Pin 2: COLLECTOR]                        [Pin 2: COLLECTOR]
                 │                                         │
                 ├─────────[ + DC Motor - ]────────────────┤
                 │                                         │
          [Pin 2: COLLECTOR]                        [Pin 2: COLLECTOR]
            TIP122 (Left Low)                         TIP122 (Right Low)
  MCU ───►[Pin 1: BASE]                             [Pin 1: BASE]◄─── MCU
          [Pin 3: EMITTER]                          [Pin 3: EMITTER]
                 │                                         │
                 └────────────────────┬────────────────────┘
                                      │
                                  GND (0V)
```

## Voltage Breakdown Family Guide

| Part Number | Polarity | $V_{CEO}$ Voltage | Complementary NPN |
|---|---|---|---|
| **TIP125** | PNP Darlington | **$-60\text{ V}$** | **TIP120** |
| **TIP126** | PNP Darlington | **$-80\text{ V}$** | **TIP121** |
| **TIP127** | PNP Darlington | **$-100\text{ V}$ (Most Popular)** | **TIP122** |

## Common mistakes

- **Forgetting the ~2V Darlington saturation loss:** Like its NPN twin, $V_{CE(sat)} \approx 2.0\text{V}$ under load. Dissipated power ($P = 2.0\text{V} \times 3\text{A} = 6\text{W}$) requires a heatsink for continuous currents above $1.5\text{A}$.
- **Connecting base directly to MCU on 24V supply:** Never connect Pin 1 (Base) directly to an MCU GPIO when the Emitter is tied to $+24\text{V}$. Use a small NPN transistor (e.g. 2N3904) to pull the base LOW.

## Notes

- **Suffix Guide:** `TIP127` is standard TO-220; `TIP127G` denotes lead-free RoHS compliance.
