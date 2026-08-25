## Overview

The **2N5551** (and its surface-mount version **MMBT5551**) is a high-voltage NPN bipolar junction transistor manufactured by onsemi, Fairchild, STMicroelectronics, and Central Semiconductor. Housed in a through-hole **TO-92** plastic package with standard `Emitter - Base - Collector` (E-B-C) pinout, it is a staple component in electronics assortment kits when higher breakdown voltages are needed.

Rated for a collector-emitter breakdown voltage ($V_{CEO}$) of **$160\text{V}$** ($180\text{V}$ $V_{CBO}$) and a continuous collector current of **$600\text{ mA}$**, the 2N5551 is engineered for circuits operating far beyond the $40\text{V}$ limit of the standard 2N3904. It is widely used in **discrete audio power amplifier differential input and voltage amplifier stages (VAS), high-voltage logic level shifters, telecom line interfaces, relay drivers on 48V telecom/industrial rails, and linear regulator pass-transistor pre-drivers**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | High-Voltage Small-Signal NPN BJT |
| **Package** | TO-92 (3-pin through-hole) / SOT-23 (MMBT5551) |
| **Collector-Emitter Voltage ($V_{CEO}$)**| **$160\text{ V}$ max** |
| **Collector-Base Voltage ($V_{CBO}$)** | **$180\text{ V}$ max** |
| **Continuous Collector Current ($I_C$)** | **$600\text{ mA}$ max** |
| **DC Current Gain ($h_{FE}$)** | **$80$ to $250$** ($I_C = 10\text{mA}, V_{CE} = 5.0\text{V}$) |
| **Transition Frequency ($f_T$)** | **$100\text{ MHz} \dots 300\text{ MHz}$** |
| **Total Power Dissipation ($P_D$)** | $625\text{ mW}$ ($T_A = 25^\circ\text{C}$) |
| **Complementary PNP Pair** | **2N5401** (160V PNP) |
| **Operating Temp Range** | $-55^\circ\text{C}$ to $+150^\circ\text{C}$ |

## Pinout (TO-92 Package - E-B-C Standard)

Looking at the **flat front face** with leads pointing downward:

```
        ┌─────────┐
        │  TO-92  │
        │ 2N5551  │
        └─┬───┬───┬─┘
          1   2   3
          E   B   C
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `EMITTER` | Emitter Terminal | Emitter (Connect to ground or emitter degeneration resistor) |
| 2 | `BASE` | Base Terminal | Base control input (Driven with current via series base resistor) |
| 3 | `COLLECTOR`| Collector Terminal| Collector output (Connected to switched high-voltage load or supply rail) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$ | 160 | — | — | V | $I_C = 1.0\text{mA}, I_B = 0$ |
| Collector-Base Breakdown | $V_{(BR)CBO}$ | 180 | — | — | V | $I_C = 100\ \mu\text{A}, I_E = 0$ |
| Emitter-Base Breakdown | $V_{(BR)EBO}$ | 6.0 | — | — | V | $I_E = 10\ \mu\text{A}, I_C = 0$ |
| Collector Cutoff Current | $I_{CBO}$ | — | — | 50 | nA | $V_{CB} = 120\text{V}, I_E = 0$ |
| DC Current Gain | $h_{FE}$ | 80 | — | 250 | — | $I_C = 10\text{mA}, V_{CE} = 5.0\text{V}$ |
| DC Current Gain | $h_{FE}$ | 30 | — | — | — | $I_C = 50\text{mA}, V_{CE} = 5.0\text{V}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | — | 0.20 | V | $I_C = 50\text{mA}, I_B = 5.0\text{mA}$ |
| Base Saturation Voltage | $V_{BE(sat)}$ | — | — | 1.00 | V | $I_C = 50\text{mA}, I_B = 5.0\text{mA}$ |

## Typical Application: High-Voltage 48V/100V Relay Driver / Level Shifter

```
                       +48V Industrial / Telecom DC Rail
                                    │
                            [ + Relay Coil - ]
                                    │
                                    ├───[ 1N4007 High-Voltage Flyback Diode ]───┐
                                    │   (Anode to Collector, Cathode to +48V)   │
                              [Pin 3: COLLECTOR]                                │
                                  2N5551                                        │
  MCU GPIO (3.3V / 5.0V)      [Pin 2: BASE]                                     │
          │                         │                                           │
          ├───[ 2.2kΩ Resistor ]────┤                                           │
          │                         ├───[ 10kΩ Base Pull-Down Resistor ]────────┤
         GND                        │                                           │
                              [Pin 1: EMITTER]                                  │
                                    │                                           │
                                   GND ─────────────────────────────────────────┴─── Common GND
```

## Comparison: 2N5551 vs 2N3904 vs MPSA42

| Parameter | 2N3904 | 2N5551 | MPSA42 |
|---|---|---|---|
| **$V_{CEO}$ Breakdown** | $40\text{ V}$ | **$160\text{ V}$** | **$300\text{ V}$** |
| **Max Current ($I_C$)** | $200\text{ mA}$ | **$600\text{ mA}$** | $500\text{ mA}$ |
| **Gain ($h_{FE}$)** | $100 \dots 300$ | $80 \dots 250$ | $40 \dots 200$ |
| **Transition Freq ($f_T$)**| $300\text{ MHz}$ | $100 \dots 300\text{ MHz}$ | $50\text{ MHz}$ |
| **Complementary PNP** | 2N3906 | **2N5401** | **MPSA92** |

## Common mistakes

- **Exceeding the 6V reverse emitter-base breakdown voltage ($V_{EBO}$):** Like most BJTs, applying more than $-6.0\text{V}$ between base and emitter causes zener breakdown and irreversibly degrades transistor current gain.
- **Using 2N3904 formulas for base drive in 100V switching circuits:** In high-voltage switching, ensure adequate base drive current ($I_B \approx I_C / 10$) so the transistor saturates fully to $V_{CE(sat)} \le 0.2\text{V}$, preventing thermal destruction under load.

## Notes

- **Suffix Guide:** `2N5550` is a $140\text{V}$ rated variant; `2N5551` is the full $160\text{V}$ part; `MMBT5551` is the SOT-23 surface-mount equivalent.
