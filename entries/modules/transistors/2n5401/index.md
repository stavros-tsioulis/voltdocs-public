## Overview

The **2N5401** (and its surface-mount version **MMBT5401**) is an industry-standard high-voltage small-signal PNP bipolar junction transistor manufactured by onsemi, Fairchild, Central Semiconductor, and STMicroelectronics. Housed in a through-hole **TO-92** plastic package with standard `Emitter - Base - Collector` (E-B-C) pinout, it is engineered for high-voltage amplification and switching.

Featuring an exceptionally high collector-emitter breakdown voltage ($V_{CEO}$) of **$-150\text{V}$** ($-160\text{V}$ $V_{CBO}$), a continuous collector current rating of **$-600\text{ mA}$**, and a transition frequency ($f_T$) of **$100\text{ MHz} \dots 300\text{ MHz}$**, the 2N5401 is the standard PNP complementary pair to the **2N5551**. It is widely employed in **hi-fi audio power amplifier Voltage Amplification Stages (VAS) and differential input pairs, 48V telecom line interfaces (on-hook/off-hook switches), gas discharge display drivers, high-voltage active constant-current sources, and industrial level shifters**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | High-Voltage Small-Signal Silicon PNP BJT |
| **Package** | TO-92 (3-pin through-hole) / SOT-23 (MMBT5401) |
| **Collector-Emitter Breakdown ($V_{CEO}$)**| **$-150\text{ V}$ max** |
| **Collector-Base Breakdown ($V_{CBO}$)** | **$-160\text{ V}$ max** |
| **Emitter-Base Breakdown ($V_{EBO}$)** | **$-5.0\text{ V}$ max** |
| **Continuous Collector Current ($I_C$)** | **$-600\text{ mA}$ max** |
| **DC Current Gain ($h_{FE}$)** | **$50$ to $240$** ($I_C = -10\text{mA}, V_{CE} = -5.0\text{V}$) / $\ge 50$ at $-50\text{mA}$ |
| **Transition Frequency ($f_T$)** | **$100\text{ MHz}$ min** ($100\text{ MHz} \dots 300\text{ MHz}$ typ) |
| **Total Power Dissipation ($P_D$)** | **$625\text{ mW}$** ($T_A = 25^\circ\text{C}$) |
| **Operating Temperature Range** | **$-55^\circ\text{C}$ to $+150^\circ\text{C}$** |
| **Complementary NPN Pair** | **2N5551** (160V NPN BJT) |

## Pinout (TO-92 Package - E-B-C Standard)

Looking at the **flat front face** with leads pointing downward:

```
        ┌─────────┐
        │  TO-92  │
        │ 2N5401  │
        └─┬───┬───┬─┘
          1   2   3
          E   B   C
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `EMITTER (E)` | Emitter Terminal | Emitter (Connect to positive supply rail or emitter degeneration resistor) |
| 2 | `BASE (B)` | Base Terminal | Base control input (Driven with base current via input stage or bias network) |
| 3 | `COLLECTOR (C)`| Collector Terminal| Collector output (Connected to negative rail or load) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$ | -150 | — | — | V | $I_C = -1.0\text{mA}, I_B = 0$ |
| Collector-Base Breakdown | $V_{(BR)CBO}$ | -160 | — | — | V | $I_C = -100\ \mu\text{A}, I_E = 0$ |
| Emitter-Base Breakdown | $V_{(BR)EBO}$ | -5.0 | — | — | V | $I_E = -10\ \mu\text{A}, I_C = 0$ |
| Collector Cutoff Current | $I_{CBO}$ | — | — | -50 | nA | $V_{CB} = -120\text{V}, I_E = 0$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 50 | — | — | — | $I_C = -1.0\text{mA}, V_{CE} = -5.0\text{V}$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 50 | — | 240 | — | $I_C = -10\text{mA}, V_{CE} = -5.0\text{V}$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 50 | — | — | — | $I_C = -50\text{mA}, V_{CE} = -5.0\text{V}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | — | -0.20 | V | $I_C = -10\text{mA}, I_B = -1.0\text{mA}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | — | -0.50 | V | $I_C = -50\text{mA}, I_B = -5.0\text{mA}$ |
| Base Saturation Voltage | $V_{BE(sat)}$ | — | — | -1.00 | V | $I_C = -50\text{mA}, I_B = -5.0\text{mA}$ |

## Typical Application: High-Voltage Audio Power Amplifier VAS Stage

In high-power audio amplifiers operating from $\pm 45\text{V}$ rails, the 2N5401 provides the high-voltage gain stage without risk of breakdown:

```
                            +45V Positive Supply Rail
                                        │
                                 [Pin 1: EMITTER]
                                    2N5401 (PNP)
  From Differential Input Stage ─►[Pin 2: BASE]
                                 [Pin 3: COLLECTOR]
                                        │
                                        ├───► Drive Signal to Driver / Output Stage (BD139 / BD140)
                                        │
                                 [ Constant Current Source / Active Load (2N5551) ]
                                        │
                            -45V Negative Supply Rail
```

## Comparison: 2N5401 vs 2N3906 vs MPSA92

| Parameter | 2N3906 | 2N5401 | MPSA92 |
|---|---|---|---|
| **$V_{CEO}$ Voltage** | $-40\text{ V}$ (Low Voltage) | **$-150\text{ V}$ (High Voltage)** | **$-300\text{ V}$ (Ultra High Voltage)** |
| **Max Current ($I_C$)** | $-200\text{ mA}$ | **$-600\text{ mA}$** | $-500\text{ mA}$ |
| **Transition Freq ($f_T$)**| $250\text{ MHz}$ | **$100\text{ MHz} \dots 300\text{ MHz}$**| $50\text{ MHz}$ |
| **Complementary NPN** | 2N3904 | **2N5551** | MPSA42 |

## Common mistakes

- **Treating as a low-voltage PNP (like 2N3906) for heavy current loads:** While the 2N5401 withstands 150V, its maximum power dissipation in free air is $625\text{mW}$. When dropping high voltages (e.g. $100\text{V}$) across the transistor, keeping current below $5\text{mA}$ is essential to avoid thermal destruction ($P = 100\text{V} \times 5\text{mA} = 500\text{mW}$).
- **Overlooking polarity in PNP circuits:** Remember that the Emitter of a PNP connects to the more positive voltage rail, and current flows *out* of the Base to turn the transistor ON.

## Notes

- **Suffix Guide:** `2N5401TA` indicates ammo-pack tape through-hole packaging; `MMBT5401` is the surface-mount SOT-23 equivalent.
