## Overview

The **BD139** is an iconic 80V 1.5A medium-power complementary silicon NPN bipolar junction transistor manufactured by STMicroelectronics, onsemi, and NXP. Housed in a through-hole **TO-126 (SOT-32)** plastic package with a central mounting screw hole, it has achieved legendary status across the audio engineering and DIY enthusiast community.

Featuring a collector-emitter breakdown voltage ($V_{CEO}$) of **$80\text{V}$**, a continuous collector current rating of **$1.5\text{A}$** ($3.0\text{A}$ peak pulse), a high transition frequency ($f_T$) of **$190\text{ MHz}$**, and linear gain across a broad current range, the BD139 (paired with its PNP complement **BD140**) is the gold standard for **hi-fi audio power amplifier push-pull driver stages, discrete Class-A headphone amplifiers (e.g. JLH 1969 / Lehmann clones), active Vbe multiplier thermal bias servos, and linear laboratory power supplies**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | Medium-Power Complementary Silicon NPN BJT |
| **Package** | TO-126 / SOT-32 (3-pin through-hole with mounting hole) |
| **Collector-Emitter Voltage ($V_{CEO}$)**| **$80\text{ V}$ max** |
| **Collector-Base Voltage ($V_{CBO}$)** | **$80\text{ V}$ max** ($100\text{ V}$ peak) |
| **Continuous Collector Current ($I_C$)** | **$1.5\text{ A}$ max** ($3.0\text{ A}$ peak pulse) |
| **Base Current ($I_B$)** | **$0.5\text{ A}$ max** |
| **DC Current Gain ($h_{FE}$)** | **$40$ to $250$** (BD139-10: 63–160, BD139-16: 100–250) |
| **Transition Frequency ($f_T$)** | **$190\text{ MHz}$ typ** ($> 50\text{ MHz}$ min) |
| **Power Dissipation ($P_D$)** | **$12.5\text{ Watts}$** ($T_C = 25^\circ\text{C}$ with heatsink) / $1.25\text{ W}$ in free air |
| **Complementary PNP Pair** | **BD140** (80V PNP) |

## Pinout (TO-126 / SOT-32 Package - E-C-B Standard)

Looking at the **printed front face** of the TO-126 package with leads pointing downward:

```
        ┌───────────────┐
        │   O [Mount]   │
        ├───────────────┤
        │     BD139     │
        └─┬─────┬─────┬─┘
          1     2     3
          E     C     B
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `EMITTER` | Emitter Terminal | Emitter (Connect to ground, emitter resistor, or output node) |
| 2 | `COLLECTOR`| Collector Terminal| Collector (Connected to positive supply rail or load; internally tied to tab) |
| 3 | `BASE` | Base Terminal | Base control input (Driven with base current via audio VAS stage or resistor) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$ | 80 | — | — | V | $I_C = 10\text{mA}, I_B = 0$ |
| Collector-Base Breakdown | $V_{(BR)CBO}$ | 80 | — | — | V | $I_C = 100\ \mu\text{A}, I_E = 0$ |
| Emitter-Base Breakdown | $V_{(BR)EBO}$ | 5.0 | — | — | V | $I_E = 10\ \mu\text{A}, I_C = 0$ |
| Collector Cutoff Current | $I_{CBO}$ | — | — | 100 | nA | $V_{CB} = 30\text{V}, I_E = 0$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 40 | — | 250 | — | $I_C = 150\text{mA}, V_{CE} = 2.0\text{V}$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 25 | — | — | — | $I_C = 500\text{mA}, V_{CE} = 2.0\text{V}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | — | 0.50 | V | $I_C = 500\text{mA}, I_B = 50\text{mA}$ |
| Base Saturation Voltage | $V_{BE(sat)}$ | — | — | 1.00 | V | $I_C = 500\text{mA}, I_B = 50\text{mA}$ |

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

## Comparison: BD139 vs TIP31C vs 2N2222A

| Parameter | 2N2222A | BD139 | TIP31C |
|---|---|---|---|
| **Package** | TO-92 / TO-18 | **TO-126 (Heatsinkable)**| TO-220 |
| **$V_{CEO}$ Voltage** | $40\text{ V}$ | **$80\text{ V}$** | $100\text{ V}$ |
| **Max Current ($I_C$)** | $600\text{ mA}$ | **$1.5\text{ A}$** | $3.0\text{ A}$ |
| **Transition Freq ($f_T$)**| $300\text{ MHz}$ | **$190\text{ MHz}$** | $3\text{ MHz}$ |
| **Audio Linearity** | Moderate | **Excellent (Hi-Fi Standard)** | Power Only |

## Common mistakes

- **Misidentifying the E-C-B pinout:** Unlike TO-92 American parts (`E-B-C`), TO-126 transistors have the **Collector in the center** (`Emitter - Collector - Base`).
- **Mounting to a heatsink without electrical insulation:** The metal rear backing tab of the TO-126 is internally bonded to Pin 2 (Collector). In split-rail audio amplifiers, connecting the collector tab directly to an earthed chassis heatsink will short out the power rail. Use a **mica or sil-pad insulator and nylon mounting washer**.

## Notes

- **Vbe Multiplier Thermal Tracking:** The central mounting hole allows the BD139 to be bolted directly on top of main output power transistors (2N3055 / 2SC5200) to provide thermal feedback that eliminates thermal runaway.
