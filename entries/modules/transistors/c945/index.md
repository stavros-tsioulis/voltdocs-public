## Overview

The **C945** (officially **2SC945** or **KSC945**) is a general-purpose NPN bipolar junction transistor originally developed by NEC and Toshiba, and manufactured globally by onsemi (Fairchild) and UTC. Housed in a through-hole **TO-92** plastic package, it is the undisputed "workhorse" NPN transistor of Asian electronics manufacturing — the Eastern hemisphere counterpart to the Western 2N3904 and European BC547.

Featuring a collector-emitter voltage ($V_{CEO}$) of **$50\text{V}$**, continuous collector current of **$150\text{ mA}$**, high transition frequency of **$300\text{ MHz}$**, and ultra-low noise figure ($NF \approx 0.5\text{ dB}$), the C945 is found in virtually every imported Chinese electronics assortment kit, PC ATX power supply auxiliary circuit, consumer AM/FM radio, LED flasher, and DIY hobbyist project.

## Quick reference

| | |
|---|---|
| **Transistor Type** | General-Purpose Audio / High-Frequency Switching NPN BJT |
| **Package** | TO-92 (3-pin through-hole) / SOT-23 |
| **Collector-Emitter Voltage ($V_{CEO}$)**| **$50\text{ V}$ max** |
| **Collector-Base Voltage ($V_{CBO}$)** | **$60\text{ V}$ max** |
| **Continuous Collector Current ($I_C$)** | **$150\text{ mA}$ max** |
| **DC Current Gain ($h_{FE}$)** | **$70$ to $700$** (Classified by gain rank: R, O, Y, GR, BL) |
| **Transition Frequency ($f_T$)** | **$300\text{ MHz}$ typ** ($150\text{ MHz}$ min) |
| **Noise Figure ($NF$)** | **$0.5\text{ dB}$ typ** ($3.0\text{ dB}$ max at $1\text{kHz}$) |
| **Total Power Dissipation ($P_D$)** | $400\text{ mW} \dots 625\text{ mW}$ |
| **Complementary PNP Pair** | **A733 (2SA733)** |
| **Pinout Standard (Japanese JIS)**| **`E - C - B`** (Pin 1: Emitter, Pin 2: Collector, Pin 3: Base) |

## Pinout (TO-92 Package - Japanese JIS Standard)

Looking at the **flat front face** with leads pointing downward:

```
        ┌─────────┐
        │  TO-92  │
        │  C945   │
        └─┬───┬───┬─┘
          1   2   3
          E   C   B
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `EMITTER` | Emitter Terminal | Emitter (Connect to ground or emitter degeneration resistor) |
| 2 | `COLLECTOR`| Collector Terminal| Collector (Center lead; connected to load or supply rail) |
| 3 | `BASE` | Base Terminal | Base control input (Right lead; driven with base current) |

*(Note: Standard Japanese 2SC945 parts follow `E-C-B`. However, certain Western-targeted variants like Fairchild's KSC945C with a "C" suffix use `E-B-C`. Always check with a multimeter or component tester).*

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$ | 50 | — | — | V | $I_C = 1.0\text{mA}, I_B = 0$ |
| Collector-Base Breakdown | $V_{(BR)CBO}$ | 60 | — | — | V | $I_C = 100\ \mu\text{A}, I_E = 0$ |
| Emitter-Base Breakdown | $V_{(BR)EBO}$ | 5.0 | — | — | V | $I_E = 10\ \mu\text{A}, I_C = 0$ |
| Collector Cutoff Current | $I_{CBO}$ | — | — | 100 | nA | $V_{CB} = 60\text{V}, I_E = 0$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 70 | 200 | 700 | — | $I_C = 1.0\text{mA}, V_{CE} = 6.0\text{V}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | 0.10 | 0.30 | V | $I_C = 100\text{mA}, I_B = 10\text{mA}$ |
| Transition Frequency | $f_T$ | 150 | 300 | — | MHz | $I_C = 10\text{mA}, V_{CE} = 6.0\text{V}$ |
| Noise Figure | $NF$ | — | 0.5 | 3.0 | dB | $I_C = 0.1\text{mA}, V_{CE} = 6\text{V}, f = 1\text{kHz}$ |

## $h_{FE}$ Classification Ranks

| Rank | $h_{FE}$ Range | Common Identifier |
|---|---|---|
| **R** | $40 \dots 80$ | Red |
| **O** | $70 \dots 140$ | Orange |
| **Y** | **$120 \dots 240$** | **Yellow (Most Common)** |
| **GR** | **$200 \dots 400$** | **Green (High Gain Audio)** |
| **BL** | $350 \dots 700$ | Blue (Super High Gain) |

## Common mistakes

- **Swapping with 2N3904 or BC547 without checking pinout:**
  - **C945 (2SC945 JIS):** `Emitter - Collector - Base` (Pin 1: E, Pin 2: C, Pin 3: B)
  - **2N3904 (USA):** `Emitter - Base - Collector` (Pin 1: E, Pin 2: B, Pin 3: C)
  - **BC547 (Europe):** `Collector - Base - Emitter` (Pin 1: C, Pin 2: B, Pin 3: E)
  *Directly plugging a C945 into a PCB designed for 2N3904 connects the Base to the Collector line, preventing the circuit from functioning.*

## Notes

- **Suffix Guide:** `2SC945` is the full Japanese Industrial Standard (JIS) part number; `C945` is the standard top-mark abbreviation printed on the physical TO-92 body; `KSC945` is the onsemi/Fairchild part number.
