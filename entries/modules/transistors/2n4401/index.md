## Overview

The **2N4401** (and its surface-mount version **MMBT4401**) is a general-purpose NPN bipolar junction transistor manufactured by onsemi, Fairchild, STMicroelectronics, and Central Semiconductor. Housed in a through-hole **TO-92** package with standard `Emitter - Base - Collector` (E-B-C) lead configuration, it is widely stocked as the direct step-up upgrade to the standard 2N3904.

While sharing the same pinout, casing, and $40\text{V}$ voltage rating as the 2N3904, the 2N4401 is rated for a continuous collector current of **$600\text{ mA}$** (three times greater than the 2N3904's $200\text{mA}$ limit). Featuring a transition frequency ($f_T$) of **$250\text{ MHz}$** and low saturation voltage ($V_{CE(sat)} \le 0.4\text{V}$ at $500\text{mA}$), it is the go-to through-hole transistor for **driving $5\text{V}/12\text{V}$ mechanical relays, high-intensity LED arrays, piezoelectric buzzers, small DC toy motors, and high-speed saturation switches**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | Higher-Current General-Purpose NPN BJT |
| **Package** | TO-92 (3-pin through-hole) / SOT-23 (MMBT4401) |
| **Collector-Emitter Voltage ($V_{CEO}$)**| **$40\text{ V}$ max** |
| **Collector-Base Voltage ($V_{CBO}$)** | **$60\text{ V}$ max** |
| **Continuous Collector Current ($I_C$)** | **$600\text{ mA}$ max** ($1.0\text{ A}$ pulsed) |
| **DC Current Gain ($h_{FE}$)** | **$100$ to $300$** ($I_C = 150\text{mA}, V_{CE} = 1.0\text{V}$) / $> 40$ at $500\text{mA}$ |
| **Transition Frequency ($f_T$)** | **$250\text{ MHz}$ min** |
| **Total Power Dissipation ($P_D$)** | $625\text{ mW}$ ($T_A = 25^\circ\text{C}$) |
| **Complementary PNP Pair** | **2N4403** (40V PNP) |
| **Operating Temp Range** | $-55^\circ\text{C}$ to $+150^\circ\text{C}$ |

## Pinout (TO-92 Package - E-B-C Standard)

Looking at the **flat front face** with leads pointing downward:

```
        ┌─────────┐
        │  TO-92  │
        │ 2N4401  │
        └─┬───┬───┬─┘
          1   2   3
          E   B   C
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `EMITTER` | Emitter Terminal | Emitter (Connect to ground or common return / $0\text{ V}$) |
| 2 | `BASE` | Base Terminal | Base control input (Driven with current via series resistor) |
| 3 | `COLLECTOR`| Collector Terminal| Collector output (Connected to switched DC load or supply rail) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$ | 40 | — | — | V | $I_C = 1.0\text{mA}, I_B = 0$ |
| Collector-Base Breakdown | $V_{(BR)CBO}$ | 60 | — | — | V | $I_C = 100\ \mu\text{A}, I_E = 0$ |
| Emitter-Base Breakdown | $V_{(BR)EBO}$ | 6.0 | — | — | V | $I_E = 100\ \mu\text{A}, I_C = 0$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 60 | — | — | — | $I_C = 1.0\text{mA}, V_{CE} = 1.0\text{V}$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 100 | — | 300 | — | $I_C = 150\text{mA}, V_{CE} = 1.0\text{V}$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 40 | — | — | — | $I_C = 500\text{mA}, V_{CE} = 2.0\text{V}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | — | 0.40 | V | $I_C = 500\text{mA}, I_B = 50\text{mA}$ |
| Base Saturation Voltage | $V_{BE(sat)}$ | 0.75 | — | 1.20 | V | $I_C = 500\text{mA}, I_B = 50\text{mA}$ |

## Typical Application Circuit: 12V 400mA Solenoid Driver

```
                       +12V DC Supply
                             │
                     [ + Solenoid / Relay Coil - ]
                             │
                             ├───[ 1N4007 Flyback Catch Diode ]────┐
                             │   (Anode to Collector, Cathode to +12V)
                       [Pin 3: COLLECTOR]                          │
                            2N4401                                 │
  MCU GPIO (3.3V / 5V) [Pin 2: BASE]                               │
          │                  │                                     │
          ├───[ 470Ω - 1kΩ ]─┤                                     │
          │                  ├───[ 10kΩ Base Pull-Down Resistor ]──┤
         GND                 │                                     │
                       [Pin 1: EMITTER]                            │
                             │                                     │
                            GND ───────────────────────────────────┴─── Common GND
```

## Comparison: 2N4401 vs 2N3904 vs 2N2222A

| Parameter | 2N3904 | 2N4401 | 2N2222A |
|---|---|---|---|
| **Max Current ($I_C$)** | $200\text{ mA}$ | **$600\text{ mA}$** | $600\text{ mA}$ |
| **$V_{CEO}$ Voltage** | $40\text{ V}$ | **$40\text{ V}$** | $40\text{ V}$ |
| **Gain at 150mA** | Drops severely ($< 30$) | **High ($100 \dots 300$)** | High ($100 \dots 300$) |
| **Transition Freq ($f_T$)**| $300\text{ MHz}$ | **$250\text{ MHz}$** | $300\text{ MHz}$ |
| **Complementary PNP** | 2N3906 | **2N4403** | 2N2907A |

## Common mistakes

- **Assuming base resistor for 2N3904 works identically at 500mA:** When switching heavy loads ($300\text{mA} \dots 500\text{mA}$), standard $4.7\text{k}\Omega \dots 10\text{k}\Omega$ base resistors will starve the base of current, leaving the transistor in active/linear mode where it dissipates several watts. For a $500\text{mA}$ load, provide at least $30\text{mA} \dots 50\text{mA}$ of base drive ($R_B \approx 100\ \Omega \dots 220\ \Omega$) or use a MOSFET (like **2N7000** or **IRLML6344**).

## Notes

- **Suffix Guide:** `2N4400` is a lower-gain ($h_{FE} = 40 \dots 120$) variant; `2N4401` is the full performance part; `MMBT4401` is the SOT-23 surface-mount package.
