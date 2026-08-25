## Overview

The **PN2907A** (and **PN2907**) is a high-speed general-purpose PNP bipolar junction transistor manufactured by onsemi, Fairchild, and STMicroelectronics. Housed in a through-hole **TO-92** plastic package with `Emitter - Base - Collector` (E-B-C) pinout, it represents the modern, breadboard-friendly plastic encapsulation of the historic **2N2907A** metal-can (TO-18) transistor.

Rated for a collector-emitter breakdown voltage ($V_{CEO}$) of **$-60\text{V}$**, a maximum continuous collector current of **$-600\text{ mA}$** ($-1.0\text{A}$ pulsed peak), and a transition frequency ($f_T$) of **$200\text{ MHz}$**, the PN2907A is the official PNP complement to the **PN2222A**. It is widely stocked in maker starter kits and university labs for **high-side relay switching, lamp drivers, audio preamplifiers, complementary push-pull output stages, and discrete logic gates**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | High-Speed General-Purpose Silicon PNP BJT |
| **Package** | TO-92 (3-pin through-hole) |
| **Collector-Emitter Breakdown ($V_{CEO}$)**| **$-60\text{ V}$ max** |
| **Collector-Base Breakdown ($V_{CBO}$)** | **$-60\text{ V}$ max** |
| **Continuous Collector Current ($I_C$)** | **$-600\text{ mA}$ max** ($-1.0\text{ A}$ pulsed) |
| **DC Current Gain ($h_{FE}$)** | **$100$ to $300$** ($I_C = -150\text{mA}, V_{CE} = -10\text{V}$) / $\ge 50$ at $-500\text{mA}$ |
| **Transition Frequency ($f_T$)** | **$200\text{ MHz}$ min** |
| **Total Power Dissipation ($P_D$)** | **$625\text{ mW}$** ($T_A = 25^\circ\text{C}$) |
| **Operating Temperature Range** | **$-55^\circ\text{C}$ to $+150^\circ\text{C}$** |
| **Complementary NPN Pair** | **PN2222A / 2N2222A** |

## Pinout (TO-92 Package - E-B-C Standard)

Looking at the **flat front face** with leads pointing downward:

```
        ┌──────────┐
        │  TO-92   │
        │ PN2907A  │
        └─┬───┬───┬┘
          1   2   3
          E   B   C
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `EMITTER (E)` | Emitter Terminal | Emitter (Connect to positive supply rail / $V_{CC}$) |
| 2 | `BASE (B)` | Base Terminal | Base control input (Driven with base current via series resistor) |
| 3 | `COLLECTOR (C)`| Collector Terminal| Collector output (Connected to high-side switched DC load) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$ | -60 | — | — | V | $I_C = -10\text{mA}, I_B = 0$ |
| Collector-Base Breakdown | $V_{(BR)CBO}$ | -60 | — | — | V | $I_C = -10\ \mu\text{A}, I_E = 0$ |
| Emitter-Base Breakdown | $V_{(BR)EBO}$ | -5.0 | — | — | V | $I_E = -10\ \mu\text{A}, I_C = 0$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 35 | — | — | — | $I_C = -0.1\text{mA}, V_{CE} = -10\text{V}$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 100 | — | 300 | — | $I_C = -150\text{mA}, V_{CE} = -10\text{V}$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 50 | — | — | — | $I_C = -500\text{mA}, V_{CE} = -10\text{V}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | — | -0.40 | V | $I_C = -150\text{mA}, I_B = -15\text{mA}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | — | -1.60 | V | $I_C = -500\text{mA}, I_B = -50\text{mA}$ |
| Base Saturation Voltage | $V_{BE(sat)}$ | — | — | -1.30 | V | $I_C = -150\text{mA}, I_B = -15\text{mA}$ |

## Typical Application Circuit: High-Side 5V Power Gate with NPN Driver

```
  +5V DC System Rail ─────────────────────────────┬─────────► [Pin 1: EMITTER]
                                                  │              PN2907A (PNP)
                                           [ 10kΩ Pull-Up ]      [Pin 3: COLLECTOR] ──► Switched +5V Power to Module
                                                  │                 │
                                                  ├─────────► [Pin 2: BASE]
                                                  │
                                            [ COLLECTOR ]
  MCU GPIO (3.3V / 5V) ───[ 1kΩ Resistor ]──► Base of PN2222A (NPN)
                                            [ EMITTER ]
                                                  │
  Common Ground (0V) ─────────────────────────────┴───────────────────────────────────► Ground
```

## Part Number & Package Equivalencies

| Part Number | Package | Notes |
|---|---|---|
| **2N2907A** | TO-18 (Metal Can) | Historic JEDEC metal hermetic package |
| **PN2907A** | TO-92 (Plastic) | Traditional plastic through-hole package |
| **MMBT2907A**| SOT-23 (SMD) | Surface-mount equivalent |

## Common mistakes

- **Assuming base resistor for 2N3906 is adequate at 500mA:** When switching higher current loads ($300\text{mA} \dots 500\text{mA}$), a standard $10\text{k}\Omega$ base resistor provides insufficient base drive ($I_B < 0.5\text{mA}$), keeping the transistor in active/linear mode. Ensure base drive is $I_B \approx I_C / 10$ to achieve full saturation.

## Notes

- **Suffix Guide:** `PN2907` is rated for $-40\text{V}$; `PN2907A` is the upgraded $-60\text{V}$ high-voltage part.
