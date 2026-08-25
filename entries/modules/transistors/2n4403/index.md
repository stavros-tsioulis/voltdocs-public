## Overview

The **2N4403** (and its surface-mount version **MMBT4403**) is a general-purpose PNP bipolar junction transistor manufactured by onsemi, Fairchild, STMicroelectronics, and Central Semiconductor. Housed in a through-hole **TO-92** plastic package with standard `Emitter - Base - Collector` (E-B-C) pinout, it serves as the official PNP complement to the **2N4401**.

Sharing the same physical footprint and $40\text{V}$ breakdown voltage as the classic 2N3906, the 2N4403 delivers a continuous collector current rating of **$-600\text{ mA}$** (three times the current of the 2N3906). Featuring a high transition frequency ($f_T$) of **$200\text{ MHz}$** and low saturation voltage ($V_{CE(sat)} \le -0.4\text{V}$ at $-150\text{mA}$), it is the premier choice for **high-side $5\text{V}/12\text{V}$ relay and lamp switching, complementary push-pull audio drivers, discrete H-bridges, and fast saturation switches**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | Higher-Current General-Purpose Silicon PNP BJT |
| **Package** | TO-92 (3-pin through-hole) / SOT-23 (MMBT4403) |
| **Collector-Emitter Breakdown ($V_{CEO}$)**| **$-40\text{ V}$ max** |
| **Collector-Base Breakdown ($V_{CBO}$)** | **$-40\text{ V}$ max** |
| **Continuous Collector Current ($I_C$)** | **$-600\text{ mA}$ max** |
| **DC Current Gain ($h_{FE}$)** | **$100$ to $300$** ($I_C = -150\text{mA}, V_{CE} = -2.0\text{V}$) / $\ge 20$ at $-500\text{mA}$ |
| **Transition Frequency ($f_T$)** | **$200\text{ MHz}$ min** |
| **Total Power Dissipation ($P_D$)** | **$625\text{ mW}$** ($T_A = 25^\circ\text{C}$) |
| **Complementary NPN Pair** | **2N4401** (40V 600mA NPN) |

## Pinout (TO-92 Package - E-B-C Standard)

Looking at the **flat front face** with leads pointing downward:

```
        ┌─────────┐
        │  TO-92  │
        │ 2N4403  │
        └─┬───┬───┬─┘
          1   2   3
          E   B   C
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `EMITTER (E)` | Emitter Terminal | Emitter (Connect to positive supply rail or emitter resistor) |
| 2 | `BASE (B)` | Base Terminal | Base control input (Driven with base current via series resistor) |
| 3 | `COLLECTOR (C)`| Collector Terminal| Collector output (Connected to high-side switched DC load) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$ | -40 | — | — | V | $I_C = -1.0\text{mA}, I_B = 0$ |
| Collector-Base Breakdown | $V_{(BR)CBO}$ | -40 | — | — | V | $I_C = -100\ \mu\text{A}, I_E = 0$ |
| Emitter-Base Breakdown | $V_{(BR)EBO}$ | -5.0 | — | — | V | $I_E = -100\ \mu\text{A}, I_C = 0$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 30 | — | — | — | $I_C = -0.1\text{mA}, V_{CE} = -1.0\text{V}$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 100 | — | 300 | — | $I_C = -150\text{mA}, V_{CE} = -2.0\text{V}$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 20 | — | — | — | $I_C = -500\text{mA}, V_{CE} = -2.0\text{V}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | — | -0.40 | V | $I_C = -150\text{mA}, I_B = -15\text{mA}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | — | -0.75 | V | $I_C = -500\text{mA}, I_B = -50\text{mA}$ |
| Base Saturation Voltage | $V_{BE(sat)}$ | -0.75 | — | -0.95 | V | $I_C = -150\text{mA}, I_B = -15\text{mA}$ |

## Typical Application Circuit: High-Side 12V 400mA Solenoid Switch

```
  +12V DC Supply ─────────────────────────────────┬─────────► [Pin 1: EMITTER]
                                                  │              2N4403 (PNP)
                                           [ 10kΩ Pull-Up ]      [Pin 3: COLLECTOR] ──► [ + 400mA Load - ] ──┐
                                                  │                 │                                         │
                                                  ├─────────► [Pin 2: BASE]                                   │
                                                  │                                                           │
                                            [ COLLECTOR ]                                                     │
  MCU GPIO (3.3V / 5V) ───[ 1kΩ Resistor ]──► Base of 2N3904 (NPN)                                            │
                                            [ EMITTER ]                                                       │
                                                  │                                                           │
  Common Ground (0V) ─────────────────────────────┴───────────────────────────────────────────────────────────┴── Ground Return
```

## Comparison: 2N4403 vs 2N3906 vs 2N2907A

| Parameter | 2N3906 | 2N4403 | 2N2907A |
|---|---|---|---|
| **Max Current ($I_C$)** | $-200\text{ mA}$ | **$-600\text{ mA}$** | $-600\text{ mA}$ |
| **$V_{CEO}$ Voltage** | $-40\text{ V}$ | **$-40\text{ V}$** | $-60\text{ V}$ |
| **Gain at 150mA** | Drops severely ($< 30$) | **High ($100 \dots 300$)** | High ($100 \dots 300$) |
| **Transition Freq ($f_T$)**| $250\text{ MHz}$ | **$200\text{ MHz}$** | $200\text{ MHz}$ |
| **Complementary NPN** | 2N3904 | **2N4401** | 2N2222A |

## Common mistakes

- **Driving directly from an MCU pin on supplies above VCC_MCU:** If the emitter of the 2N4403 is connected to $+12\text{V}$, an MCU GPIO driving $+5\text{V}$ leaves $V_{EB} = 7\text{V}$, forward-biasing the base-emitter junction and driving destructive current into the microcontroller's internal ESD protection diodes. Always use an intermediate NPN pull-down transistor or open-drain buffer for supplies $> 5\text{V}$.

## Notes

- **Suffix Guide:** `2N4402` is a lower gain ($h_{FE} = 50 \dots 150$) variant; `2N4403` is the full performance part; `MMBT4403` is the SOT-23 surface-mount package.
