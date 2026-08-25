## Overview

The **MJE2955T** is a -60V -10A silicon power PNP bipolar junction transistor manufactured by onsemi and STMicroelectronics. Housed in a through-hole **TO-220AB** plastic package, it was engineered as the direct plastic-package equivalent of the historic **2N2955 / MJ2955** metal TO-3 diamond-case power transistor.

Providing a collector-emitter breakdown voltage ($V_{CEO}$) of **$-60\text{V}$**, a high continuous collector current rating of **$-10.0\text{A}$**, and a massive power dissipation capability of **$75\text{ Watts}$** at $T_C = 25^\circ\text{C}$ ($\theta_{JC} = 1.67^\circ\text{C/W}$), the MJE2955T serves as the official PNP complement to the **MJE3055T**. Together, the MJE3055T/MJE2955T pair is the industry benchmark for **high-power complementary Class AB audio amplifiers (40W–100W), dual-polarity laboratory power supply series-pass stages, and high-current DC motor speed controllers**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | High-Power Silicon PNP Power BJT |
| **Package** | TO-220AB (3-pin through-hole) |
| **Collector-Emitter Breakdown ($V_{CEO}$)**| **$-60\text{ V}$ max** |
| **Collector-Base Breakdown ($V_{CBO}$)** | **$-70\text{ V}$ max** |
| **Continuous Collector Current ($I_C$)** | **$-10.0\text{ A}$ max** |
| **Base Current ($I_B$)** | **$-6.0\text{ A}$ max** |
| **DC Current Gain ($h_{FE}$)** | **$20$ to $100$** ($I_C = -4.0\text{A}, V_{CE} = -4.0\text{V}$) / $\ge 5$ at $-10\text{A}$ |
| **Collector Saturation ($V_{CE(sat)}$)** | **$-1.1\text{ V}$ max** ($I_C = -4.0\text{A}, I_B = -400\text{mA}$) / $-3.0\text{V}$ at $-10\text{A}$ |
| **Total Power Dissipation ($P_D$)** | **$75\text{ Watts}$** ($T_C = 25^\circ\text{C}$ with heatsink) / $1.75\text{ W}$ free air |
| **Transition Frequency ($f_T$)** | **$2.0\text{ MHz}$ min** |
| **Thermal Resistance ($\theta_{JC}$)**| **$1.67^\circ\text{C/W}$** (Junction-to-Case) |
| **Complementary NPN Pair** | **MJE3055T** (60V 10A NPN) |

## Pinout (TO-220AB Package - B-C-E Standard)

Looking at the **front labeled face** with leads pointing downward:

```
        ┌──────────────┐
        │  O  [Metal]  │ ── Tab is internally connected to Pin 2 (Collector)
        ├──────────────┤
        │   MJE2955T   │
        └─┬────┬────┬──┘
          1    2    3
          B    C    E
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `BASE (B)` | Base Input | Base control input (Driven with base current via driver transistor) |
| 2 (Tab) | `COLLECTOR (C)` | Power Collector | Collector terminal (Internally connected to metal mounting tab) |
| 3 | `EMITTER (E)` | Power Emitter | Emitter terminal (Connect to positive supply rail or output resistor) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$ | -60 | — | — | V | $I_C = -30\text{mA}, I_B = 0$ |
| Collector-Base Breakdown | $V_{(BR)CBO}$ | -70 | — | — | V | $I_C = -1.0\text{mA}, I_E = 0$ |
| Emitter-Base Breakdown | $V_{(BR)EBO}$ | -5.0 | — | — | V | $I_E = -1.0\text{mA}, I_C = 0$ |
| Collector Cutoff Current | $I_{CEO}$ | — | — | -700 | µA | $V_{CE} = -30\text{V}, I_B = 0$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 20 | — | 100 | — | $I_C = -4.0\text{A}, V_{CE} = -4.0\text{V}$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 5 | — | — | — | $I_C = -10.0\text{A}, V_{CE} = -4.0\text{V}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | — | -1.1 | V | $I_C = -4.0\text{A}, I_B = -400\text{mA}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | — | -3.0 | V | $I_C = -10.0\text{A}, I_B = -3.3\text{A}$ |
| Base-Emitter On Voltage | $V_{BE(on)}$ | — | — | -1.8 | V | $I_C = -4.0\text{A}, V_{CE} = -4.0\text{V}$ |

## Typical Application: 60W Hi-Fi Complementary Audio Power Amplifier Output Stage

```
                            +35V Positive DC Power Rail
                                         │
                                  [Pin 2: COLLECTOR]
                                     MJE3055T (NPN)
  From Driver (BD139) ───────────►[Pin 1: BASE]
                                  [Pin 3: EMITTER]
                                         │
                                         ├───[ 0.22Ω 5W Resistor ]───┐
                                         │                           ├────► Audio Output (to 8Ω Speaker)
                                         ├───[ 0.22Ω 5W Resistor ]───┘
                                  [Pin 3: EMITTER]
  From Driver (BD140) ───────────►[Pin 1: BASE]
                                     MJE2955T (PNP)
                                  [Pin 2: COLLECTOR]
                                         │
                            -35V Negative DC Power Rail
```

## Comparison: MJE2955T vs MJ2955 vs TIP42C

| Parameter | MJE2955T | MJ2955 | TIP42C |
|---|---|---|---|
| **Package** | **TO-220AB (Plastic)** | TO-3 (Metal Diamond) | TO-220AB (Plastic) |
| **$V_{CEO}$ Voltage** | $-60\text{ V}$ | $-60\text{ V}$ | **$-100\text{ V}$** |
| **Max Current ($I_C$)** | **$-10\text{ A}$** | $-15\text{ A}$ | $-6.0\text{ A}$ |
| **Power Dissipation ($P_D$)**| **$75\text{ W}$** | $115\text{ W}$ | $65\text{ W}$ |
| **Complementary NPN** | **MJE3055T** | 2N3055 | TIP41C |

## Common mistakes

- **Driving base directly without a pre-driver transistor:** At high currents ($I_C = -4\text{A}$), the base requires $I_B \approx -400\text{mA}$. Always use a pre-driver transistor (such as the **BD140** or **TIP32C**) to supply base current.
- **Operating without a heavy heatsink:** When delivering continuous audio or linear power, thermal dissipation can exceed $30\text{W} \dots 50\text{W}$. Always use a large heatsink with thermal paste and insulating mica/silicone mounting kits.

## Notes

- **Suffix Guide:** `MJE2955T` is standard TO-220; `MJE2955TG` denotes lead-free RoHS compliance; `MJE3055T` is the complementary NPN partner.
