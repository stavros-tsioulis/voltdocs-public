## Overview

The **A733** (officially **2SA733** or **KSA733**) is a general-purpose PNP bipolar junction transistor originally developed by NEC and Toshiba, and manufactured globally by onsemi (Fairchild) and UTC. Housed in a through-hole **TO-92** plastic package, it is the official PNP complement to the ubiquitous **C945 (2SC945)** transistor.

Featuring a collector-emitter breakdown voltage ($V_{CEO}$) of **$-50\text{V}$**, continuous collector current of **$-150\text{ mA}$**, a transition frequency ($f_T$) of **$180\text{ MHz}$**, and ultra-low noise figure ($NF \approx 0.5\text{ dB}$), the A733 is universally found in Asian consumer electronics, imported DIY kits, audio preamplifiers, discrete multivibrators, and power supply control stages.

## Quick reference

| | |
|---|---|
| **Transistor Type** | General-Purpose Audio / High-Frequency Switching PNP BJT |
| **Package** | TO-92 (3-pin through-hole) / SOT-23 |
| **Collector-Emitter Breakdown ($V_{CEO}$)**| **$-50\text{ V}$ max** |
| **Collector-Base Breakdown ($V_{CBO}$)** | **$-60\text{ V}$ max** |
| **Continuous Collector Current ($I_C$)** | **$-150\text{ mA}$ max** |
| **DC Current Gain ($h_{FE}$)** | **$70$ to $700$** (Classified by gain rank: R, Q, P, K) |
| **Transition Frequency ($f_T$)** | **$180\text{ MHz}$ typ** ($100\text{ MHz}$ min) |
| **Noise Figure ($NF$)** | **$0.5\text{ dB}$ typ** ($3.0\text{ dB}$ max at $1\text{kHz}$) |
| **Total Power Dissipation ($P_D$)** | **$250\text{ mW} \dots 400\text{ mW}$** |
| **Complementary NPN Pair** | **C945 (2SC945)** |
| **Pinout Standard (Japanese JIS)**| **`E - C - B`** (Pin 1: Emitter, Pin 2: Collector, Pin 3: Base) |

## Pinout (TO-92 Package - Japanese JIS Standard)

Looking at the **flat front face** with leads pointing downward:

```
        ┌─────────┐
        │  TO-92  │
        │  A733   │
        └─┬───┬───┬─┘
          1   2   3
          E   C   B
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `EMITTER (E)` | Emitter Terminal | Emitter (Connect to positive supply rail or emitter degeneration resistor) |
| 2 | `COLLECTOR (C)`| Collector Terminal| Collector (Center lead; connected to load or negative rail) |
| 3 | `BASE (B)` | Base Terminal | Base control input (Right lead; driven with base current) |

*(Note: Standard Japanese 2SA733 parts follow `E-C-B`. However, certain Western variants like Fairchild's KSA733C with a "C" suffix use `E-B-C`. Always check with a component tester or datasheet).*

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$ | -50 | — | — | V | $I_C = -1.0\text{mA}, I_B = 0$ |
| Collector-Base Breakdown | $V_{(BR)CBO}$ | -60 | — | — | V | $I_C = -100\ \mu\text{A}, I_E = 0$ |
| Emitter-Base Breakdown | $V_{(BR)EBO}$ | -5.0 | — | — | V | $I_E = -10\ \mu\text{A}, I_C = 0$ |
| Collector Cutoff Current | $I_{CBO}$ | — | — | -100 | nA | $V_{CB} = -60\text{V}, I_E = 0$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 70 | 200 | 700 | — | $I_C = -1.0\text{mA}, V_{CE} = -6.0\text{V}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | -0.10 | -0.30 | V | $I_C = -100\text{mA}, I_B = -10\text{mA}$ |
| Transition Frequency | $f_T$ | 100 | 180 | — | MHz | $I_C = -10\text{mA}, V_{CE} = -6.0\text{V}$ |
| Noise Figure | $NF$ | — | 0.5 | 3.0 | dB | $I_C = -0.1\text{mA}, V_{CE} = -6\text{V}, f = 1\text{kHz}$ |

## $h_{FE}$ Classification Ranks

| Rank | $h_{FE}$ Range | Application Suitability |
|---|---|---|
| **R** | $40 \dots 80$ | General digital switching |
| **Q** | $70 \dots 140$ | High-speed logic switching |
| **P** | **$120 \dots 240$** | **Standard audio driver (Most Common)** |
| **K** | **$200 \dots 400$** | **High-gain audio preamplifiers** |

## Common mistakes

- **Swapping with 2N3906 or BC557 without checking pinout:**
  - **A733 (2SA733 JIS):** `Emitter - Collector - Base` (Pin 1: E, Pin 2: C, Pin 3: B)
  - **2N3906 (USA):** `Emitter - Base - Collector` (Pin 1: E, Pin 2: B, Pin 3: C)
  - **BC557 (Europe):** `Collector - Base - Emitter` (Pin 1: C, Pin 2: B, Pin 3: E)
  *Always verify pin ordering before replacing transistors in imported circuits.*

## Notes

- **Naming Convention:** `2SA733` is the full Japanese Industrial Standard (JIS) part number; `A733` is the standard top-mark abbreviation printed on the physical TO-92 body; `KSA733` is the onsemi/Fairchild part number.
