## Overview

The **MJE3055T** is a 60V 10A silicon power NPN bipolar junction transistor manufactured by onsemi and STMicroelectronics. Housed in a through-hole **TO-220AB** package, it was engineered as the direct plastic-package equivalent of the historic **2N3055** metal TO-3 diamond-case power transistor.

Providing a collector-emitter breakdown voltage ($V_{CEO}$) of **$60\text{V}$**, a high continuous collector current rating of **$10.0\text{A}$**, and a massive power dissipation capability of **$75\text{ Watts}$** at $T_C = 25^\circ\text{C}$ ($\theta_{JC} = 1.67^\circ\text{C/W}$), the MJE3055T delivers the rugged performance of a 2N3055 in a modern, PCB-friendly form factor. Paired with its PNP complement **MJE2955T**, it is the industry standard for **linear laboratory DC bench power supplies (series-pass regulators), high-power audio amplifiers (30W–80W Class AB/B outputs), heavy DC motor speed controllers, and magnetic actuator drivers**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | High-Power Silicon NPN Power BJT |
| **Package** | TO-220AB (3-pin through-hole) |
| **Collector-Emitter Voltage ($V_{CEO}$)**| **$60\text{ V}$ max** |
| **Collector-Base Voltage ($V_{CBO}$)** | **$70\text{ V}$ max** |
| **Continuous Collector Current ($I_C$)** | **$10.0\text{ A}$ max** |
| **Base Current ($I_B$)** | **$6.0\text{ A}$ max** |
| **DC Current Gain ($h_{FE}$)** | **$20$ to $100$** ($I_C = 4.0\text{A}, V_{CE} = 4.0\text{V}$) / $\ge 5$ at $10\text{A}$ |
| **Collector Saturation ($V_{CE(sat)}$)** | **$1.1\text{ V}$ max** ($I_C = 4.0\text{A}, I_B = 400\text{mA}$) / $3.0\text{V}$ at $10\text{A}$ |
| **Total Power Dissipation ($P_D$)** | **$75\text{ Watts}$** ($T_C = 25^\circ\text{C}$ with heatsink) / $1.75\text{ W}$ free air |
| **Transition Frequency ($f_T$)** | **$2.0\text{ MHz}$ min** |
| **Thermal Resistance ($\theta_{JC}$)**| **$1.67^\circ\text{C/W}$** (Junction-to-Case) |
| **Complementary PNP Pair** | **MJE2955T** (60V 10A PNP) |

## Pinout (TO-220AB Package - B-C-E Standard)

Looking at the **front labeled face** with leads pointing downward:

```
        ┌──────────────┐
        │  O  [Metal]  │ ── Tab is internally connected to Pin 2 (Collector)
        ├──────────────┤
        │   MJE3055T   │
        └─┬────┬────┬──┘
          1    2    3
          B    C    E
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `BASE` | Base Input | Base control input (Driven with base current via driver transistor) |
| 2 (Tab) | `COLLECTOR` | Power Collector | Collector terminal (Internally connected to metal mounting tab) |
| 3 | `EMITTER` | Power Emitter | Emitter output (Connect to output rail or current-sense resistor) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$ | 60 | — | — | V | $I_C = 30\text{mA}, I_B = 0$ |
| Collector-Base Breakdown | $V_{(BR)CBO}$ | 70 | — | — | V | $I_C = 1.0\text{mA}, I_E = 0$ |
| Emitter-Base Breakdown | $V_{(BR)EBO}$ | 5.0 | — | — | V | $I_E = 1.0\text{mA}, I_C = 0$ |
| Collector Cutoff Current | $I_{CEO}$ | — | — | 700 | µA | $V_{CE} = 30\text{V}, I_B = 0$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 20 | — | 100 | — | $I_C = 4.0\text{A}, V_{CE} = 4.0\text{V}$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 5 | — | — | — | $I_C = 10.0\text{A}, V_{CE} = 4.0\text{V}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | — | 1.1 | V | $I_C = 4.0\text{A}, I_B = 400\text{mA}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | — | 3.0 | V | $I_C = 10.0\text{A}, I_B = 3.3\text{A}$ |
| Base-Emitter On Voltage | $V_{BE(on)}$ | — | — | 1.8 | V | $I_C = 4.0\text{A}, V_{CE} = 4.0\text{V}$ |

## Typical Application: 0–30V 5A Linear Bench Power Supply Series-Pass Stage

```
      Unregulated +35V DC Filtered Rail (from Transformer + Bridge)
                                  │
                           [Pin 2: COLLECTOR]
                              MJE3055T
  Driver Transistor        [Pin 1: BASE]
  (e.g. BD139 / TIP31C)           │
          │                       │
          └───────────────────────┤
                                  │
                           [Pin 3: EMITTER]
                                  │
                                  ├───[ 0.1Ω 5W Current Sense Resistor ]───► Regulated +0-30V Output (Up to 5A)
                                  │
                                 GND ──────────────────────────────────────► Power Supply Return (0V)
```

## Comparison: MJE3055T vs 2N3055 vs TIP3055

| Parameter | MJE3055T | 2N3055 | TIP3055 |
|---|---|---|---|
| **Package** | **TO-220AB (Plastic)** | TO-3 (Metal Diamond) | TO-247 / TO-218 (Large Plastic) |
| **$V_{CEO}$ Voltage** | $60\text{ V}$ | $60\text{ V}$ | $60\text{ V}$ |
| **Max Current ($I_C$)** | **$10\text{ A}$** | $15\text{ A}$ | $15\text{ A}$ |
| **Power Dissipation ($P_D$)**| **$75\text{ W}$** | $115\text{ W}$ | $90\text{ W}$ |
| **Mounting Style** | **Single Screw on PCB**| 2 Screws + Sockets | Single Screw Heavy |

## Common mistakes

- **Underestimating base current requirements at high loads:** With $h_{FE} \approx 20$ at $4\text{A}$, the base requires $I_B \approx 200\text{mA} \dots 400\text{mA}$. The base cannot be driven directly by an op-amp or microcontroller; always use a medium-power pre-driver transistor (such as the **BD139** or **TIP31C**) in a Darlington or Sziklai pair configuration.
- **Operating without a substantial heatsink:** At $5\text{A}$ load with $10\text{V}$ drop across the regulator, power dissipation is $P = 50\text{ Watts}$. A heavy extruded aluminum heatsink with thermal compound and silicone insulator is essential.

## Notes

- **Suffix Guide:** `MJE3055T` is standard TO-220; `MJE3055TG` denotes lead-free RoHS compliance; `MJE2955T` is the complementary PNP partner.
