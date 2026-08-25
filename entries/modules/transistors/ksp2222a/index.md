## Overview

The **KSP2222A** is a high-current, high-speed general-purpose NPN bipolar junction transistor manufactured by onsemi (originally Fairchild Semiconductor). Housed in an industry-standard **TO-92** through-hole plastic package with `Emitter - Base - Collector` (E-B-C) pinout, it represents the modern commercial manufacturing designation for the world-famous **2N2222A / PN2222A**.

Delivering a collector-emitter breakdown voltage ($V_{CEO}$) of **$40\text{V}$**, a maximum continuous collector current of **$600\text{ mA}$** ($1.0\text{A}$ pulsed), and a rapid transition frequency ($f_T$) of **$300\text{ MHz}$**, the KSP2222A provides high current-gain bandwidth and low saturation resistance. It is standard equipment for **driving $5\text{V}$ and $12\text{V}$ relays, DC motors, solenoids, high-current LED strings, audio output stages, and RF oscillator circuits**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | High-Current General-Purpose NPN BJT |
| **Package** | TO-92 (3-pin through-hole) |
| **Collector-Emitter Voltage ($V_{CEO}$)**| **$40\text{ V}$ max** |
| **Collector-Base Voltage ($V_{CBO}$)** | **$75\text{ V}$ max** |
| **Continuous Collector Current ($I_C$)** | **$600\text{ mA}$ max** ($1.0\text{ A}$ pulsed) |
| **DC Current Gain ($h_{FE}$)** | **$100$ to $300$** ($I_C = 150\text{mA}, V_{CE} = 10\text{V}$) / $> 40$ at $500\text{mA}$ |
| **Transition Frequency ($f_T$)** | **$300\text{ MHz}$ min** |
| **Total Power Dissipation ($P_D$)** | $625\text{ mW}$ ($T_A = 25^\circ\text{C}$) |
| **Complementary PNP Pair** | **KSP2907A** (40V PNP) |
| **Pinout Standard** | **`E - B - C`** (Pin 1: Emitter, Pin 2: Base, Pin 3: Collector) |

## Pinout (TO-92 Package - E-B-C Standard)

Looking at the **flat front face** with leads pointing downward:

```
        ┌──────────┐
        │  TO-92   │
        │ KSP2222A │
        └─┬───┬───┬┘
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
| Collector-Emitter Breakdown | $V_{(BR)CEO}$ | 40 | — | — | V | $I_C = 10\text{mA}, I_B = 0$ |
| Collector-Base Breakdown | $V_{(BR)CBO}$ | 75 | — | — | V | $I_C = 10\ \mu\text{A}, I_E = 0$ |
| Emitter-Base Breakdown | $V_{(BR)EBO}$ | 6.0 | — | — | V | $I_E = 10\ \mu\text{A}, I_C = 0$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 35 | — | — | — | $I_C = 0.1\text{mA}, V_{CE} = 10\text{V}$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 100 | — | 300 | — | $I_C = 150\text{mA}, V_{CE} = 10\text{V}$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 40 | — | — | — | $I_C = 500\text{mA}, V_{CE} = 10\text{V}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | — | 0.30 | V | $I_C = 150\text{mA}, I_B = 15\text{mA}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | — | 1.00 | V | $I_C = 500\text{mA}, I_B = 50\text{mA}$ |
| Output Capacitance | $C_{obo}$ | — | — | 8.0 | pF | $V_{CB} = 10\text{V}, f = 1.0\text{MHz}$ |

## Part Number Equivalencies

| Part Number | Package | Notes |
|---|---|---|
| **2N2222A** | TO-18 (Metal Can) | Historic JEDEC metal hermetic package |
| **PN2222A** | TO-92 (Plastic) | Traditional plastic through-hole package |
| **KSP2222A** | TO-92 (Plastic) | Fairchild / onsemi automated high-volume production part number |
| **MMBT2222A**| SOT-23 (SMD) | Surface-mount equivalent |

## Common mistakes

- **Treating as a logic-level MOSFET:** The KSP2222A is a bipolar junction transistor requiring a continuous **base current** ($I_B = I_C / 10$) to remain in full saturation. Omitting the base current-limiting resistor or providing insufficient drive current will prevent the transistor from fully turning on.

## Notes

- **Suffix Guide:** `BU` indicates bulk packaging; `TA` indicates ammo tape packaging; `TFR` indicates tape and reel.
