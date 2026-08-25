## Overview

The **BD140** is an iconic -80V -1.5A medium-power complementary silicon PNP bipolar junction transistor manufactured by STMicroelectronics, onsemi, and NXP. Housed in a through-hole **TO-126 (SOT-32)** plastic package with a central mounting screw hole, it is globally celebrated as the premier audio driver PNP transistor.

Featuring a collector-emitter breakdown voltage ($V_{CEO}$) of **$-80\text{V}$**, a continuous collector current rating of **$-1.5\text{A}$** ($-3.0\text{A}$ pulsed peak), a high transition frequency ($f_T$) of **$190\text{ MHz}$**, and linear gain tracking, the BD140 is the official complementary PNP pair to the **BD139**. Together, the BD139/BD140 complementary pair is the undisputed industry standard for **hi-fi audio power amplifier push-pull driver stages, discrete Class-A headphone amplifiers (e.g. JLH 1969 / Lehmann clones), active audio preamplifiers, and dual-rail laboratory power supplies**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | Medium-Power Complementary Silicon PNP BJT |
| **Package** | TO-126 / SOT-32 (3-pin through-hole with mounting hole) |
| **Collector-Emitter Breakdown ($V_{CEO}$)**| **$-80\text{ V}$ max** |
| **Collector-Base Breakdown ($V_{CBO}$)** | **$-80\text{ V}$ max** ($-100\text{ V}$ peak) |
| **Continuous Collector Current ($I_C$)** | **$-1.5\text{ A}$ max** ($-3.0\text{ A}$ peak pulse) |
| **Base Current ($I_B$)** | **$-0.5\text{ A}$ max** |
| **DC Current Gain ($h_{FE}$)** | **$40$ to $250$** (BD140-10: 63–160, BD140-16: 100–250) |
| **Transition Frequency ($f_T$)** | **$190\text{ MHz}$ typ** ($> 50\text{ MHz}$ min) |
| **Power Dissipation ($P_D$)** | **$12.5\text{ Watts}$** ($T_C = 25^\circ\text{C}$ with heatsink) / $1.25\text{ W}$ in free air |
| **Complementary NPN Pair** | **BD139** (80V NPN) |

## Pinout (TO-126 / SOT-32 Package - E-C-B Standard)

Looking at the **printed front face** of the TO-126 package with leads pointing downward:

```
        ┌───────────────┐
        │   O [Mount]   │
        ├──────────────┤
        │     BD140     │
        └─┬─────┬─────┬─┘
          1     2     3
          E     C     B
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `EMITTER (E)` | Emitter Terminal | Emitter (Connect to positive supply rail or output summing resistor) |
| 2 | `COLLECTOR (C)`| Collector Terminal| Collector (Connected to negative power rail; internally bonded to rear metal tab) |
| 3 | `BASE (B)` | Base Terminal | Base control input (Driven with audio VAS output signal) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$ | -80 | — | — | V | $I_C = -10\text{mA}, I_B = 0$ |
| Collector-Base Breakdown | $V_{(BR)CBO}$ | -80 | — | — | V | $I_C = -100\ \mu\text{A}, I_E = 0$ |
| Emitter-Base Breakdown | $V_{(BR)EBO}$ | -5.0 | — | — | V | $I_E = -10\ \mu\text{A}, I_C = 0$ |
| Collector Cutoff Current | $I_{CBO}$ | — | — | -100 | nA | $V_{CB} = -30\text{V}, I_E = 0$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 40 | — | 250 | — | $I_C = -150\text{mA}, V_{CE} = -2.0\text{V}$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 25 | — | — | — | $I_C = -500\text{mA}, V_{CE} = -2.0\text{V}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | — | -0.50 | V | $I_C = -500\text{mA}, I_B = -50\text{mA}$ |
| Base Saturation Voltage | $V_{BE(sat)}$ | — | — | -1.00 | V | $I_C = -500\text{mA}, I_B = -50\text{mA}$ |

## Typical Application: Complementary Push-Pull Audio Buffer (Class AB)

```
                            +15V to +24V Positive Supply Rail
                                          │
                                   [Pin 2: COLLECTOR]
                                      BD139 (NPN)
  Audio Input (from Op-Amp)        [Pin 3: BASE]
           │                              │
           ├───[ 1N4148 Diode Bias 1 ]────┤
           │                              │
           │                       [Pin 1: EMITTER]
           │                              │
           │                              ├───[ 0.47Ω 2W Emitter Resistor ]───┐
           │                                                                  ├────► Audio Output (Speaker / Headphones)
           │                              ┌───[ 0.47Ω 2W Emitter Resistor ]───┘
           │                       [Pin 1: EMITTER]
           │                              │
           └───[ 1N4148 Diode Bias 2 ]────┤
                                      BD140 (PNP)
                                   [Pin 3: BASE]
                                          │
                                   [Pin 2: COLLECTOR]
                                          │
                            -15V to -24V Negative Supply Rail
```

## Comparison: BD140 vs TIP42C vs 2N2907A

| Parameter | 2N2907A | BD140 | TIP42C |
|---|---|---|---|
| **Package** | TO-92 / TO-18 | **TO-126 (Heatsinkable)**| TO-220 |
| **$V_{CEO}$ Voltage** | $-40\text{ V}$ | **$-80\text{ V}$** | $-100\text{ V}$ |
| **Max Current ($I_C$)** | $-600\text{ mA}$ | **$-1.5\text{ A}$** | $-6.0\text{ A}$ |
| **Transition Freq ($f_T$)**| $200\text{ MHz}$ | **$190\text{ MHz}$** | $3\text{ MHz}$ |
| **Audio Linearity** | Moderate | **Excellent (Hi-Fi Standard)** | Power Only |

## Common mistakes

- **Misidentifying the E-C-B pinout:** Unlike American TO-92 transistors (`E-B-C`), TO-126 transistors place the **Collector in the center** (`Emitter - Collector - Base`).
- **Mounting to a heatsink without electrical insulation:** The metal rear backing tab of the TO-126 is internally bonded to Pin 2 (Collector). In split-rail audio amplifiers, connecting the collector tab directly to an earthed heatsink will short out the negative power rail. Use a **mica or sil-pad insulator and nylon mounting bushing**.

## Notes

- **Suffix Guide:** `-10` ($h_{FE} = 63 \dots 160$) and `-16` ($h_{FE} = 100 \dots 250$) are the preferred gain classifications for balanced audio driver stages.
