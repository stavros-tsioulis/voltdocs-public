## Overview

The **MPSA92** (and **KSP92** / **MMBTA92**) is an industry-standard ultra-high-voltage small-signal PNP bipolar junction transistor manufactured by onsemi, Fairchild, Central Semiconductor, and STMicroelectronics. Available in a through-hole **TO-92** plastic package and surface-mount **SOT-23** package with standard `Emitter - Base - Collector` (E-B-C) pinout, it is built specifically for extreme high-voltage switching and amplification.

Featuring a massive collector-emitter breakdown voltage ($V_{CEO}$) rating of **$-300\text{V}$** ($-300\text{V}$ $V_{CBO}$), a continuous collector current rating of **$-500\text{ mA}$**, and a transition frequency ($f_T$) of **$50\text{ MHz}$**, the MPSA92 is the undisputed complementary PNP pair to the iconic **MPSA42**. It is celebrated across the maker and retrocomputing community as the premier **high-side anode switch for multiplexed $170\text{V} \dots 200\text{V}$ Nixie tube clocks, neon indicator arrays, gas discharge displays, CRT video drivers, and high-voltage constant current active loads**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | Ultra-High-Voltage Small-Signal Silicon PNP BJT |
| **Package** | TO-92 (3-pin through-hole) / SOT-23 (MMBTA92) |
| **Collector-Emitter Breakdown ($V_{CEO}$)**| **$-300\text{ V}$ max** |
| **Collector-Base Breakdown ($V_{CBO}$)** | **$-300\text{ V}$ max** |
| **Emitter-Base Breakdown ($V_{EBO}$)** | **$-5.0\text{ V}$ max** |
| **Continuous Collector Current ($I_C$)** | **$-500\text{ mA}$ max** |
| **DC Current Gain ($h_{FE}$)** | **$40$ to $200$** ($I_C = -10\text{mA}, V_{CE} = -10\text{V}$) / $\ge 25$ at $-30\text{mA}$ |
| **Transition Frequency ($f_T$)** | **$50\text{ MHz}$ min** |
| **Collector Saturation ($V_{CE(sat)}$)** | **$-0.50\text{ V}$ max** at $I_C = -20\text{mA}, I_B = -2.0\text{mA}$ |
| **Total Power Dissipation ($P_D$)** | **$625\text{ mW}$** ($T_A = 25^\circ\text{C}$) |
| **Complementary NPN Pair** | **MPSA42 / KSP42** (300V NPN BJT) |

## Pinout (TO-92 Package - E-B-C Standard)

Looking at the **flat front face** with leads pointing downward:

```
        ┌─────────┐
        │  TO-92  │
        │ MPSA92  │
        └─┬───┬───┬─┘
          1   2   3
          E   B   C
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `EMITTER (E)` | Emitter Terminal | Emitter (Connect to $+170\text{V} \dots +200\text{V}$ high-voltage anode supply rail) |
| 2 | `BASE (B)` | Base Terminal | Base control input (Pulled down via resistor to turn transistor ON) |
| 3 | `COLLECTOR (C)`| Collector Terminal| Collector output (Connect to high-voltage load / Nixie tube anode) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$ | -300 | — | — | V | $I_C = -1.0\text{mA}, I_B = 0$ |
| Collector-Base Breakdown | $V_{(BR)CBO}$ | -300 | — | — | V | $I_C = -100\ \mu\text{A}, I_E = 0$ |
| Emitter-Base Breakdown | $V_{(BR)EBO}$ | -5.0 | — | — | V | $I_E = -100\ \mu\text{A}, I_C = 0$ |
| Collector Cutoff Current | $I_{CBO}$ | — | — | -250 | nA | $V_{CB} = -200\text{V}, I_E = 0$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 25 | — | — | — | $I_C = -1.0\text{mA}, V_{CE} = -10\text{V}$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 40 | — | 200 | — | $I_C = -10\text{mA}, V_{CE} = -10\text{V}$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 25 | — | — | — | $I_C = -30\text{mA}, V_{CE} = -10\text{V}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | — | -0.50 | V | $I_C = -20\text{mA}, I_B = -2.0\text{mA}$ |
| Base Saturation Voltage | $V_{BE(sat)}$ | — | — | -0.90 | V | $I_C = -20\text{mA}, I_B = -2.0\text{mA}$ |

## Typical Application: +170V High-Side Nixie Tube Anode Multiplexer

In multiplexed Nixie tube clocks, an MPSA42 NPN pulls the base of the MPSA92 PNP LOW to switch the $+170\text{V}$ anode rail to the selected tube:

```
  +170V DC High-Voltage Boost Rail ───────────────┬─────────► [Pin 1: EMITTER]
                                                  │              MPSA92 (PNP)
                                           [ 47kΩ Pull-Up ]      [Pin 3: COLLECTOR] ──► To Nixie Tube Anode
                                                  │                 │
                                                  ├─────────► [Pin 2: BASE]
                                                  │
                                            [ 220kΩ Resistor ]
                                                  │
                                           [ Pin 3: COLLECTOR ]
  MCU GPIO (3.3V / 5V) ───[ 10kΩ Resistor ]──► Base (Pin 2) of MPSA42 (NPN)
                                           [ Pin 1: EMITTER ]
                                                  │
  System Ground (0V) ─────────────────────────────┴───────────────────────────────► Ground
```

## Comparison: MPSA92 vs 2N5401 vs 2N3906

| Parameter | 2N3906 | 2N5401 | MPSA92 |
|---|---|---|---|
| **$V_{CEO}$ Breakdown** | $-40\text{ V}$ | $-150\text{ V}$ | **$-300\text{ V}$ (Nixie Standard)** |
| **Max Current ($I_C$)** | $-200\text{ mA}$ | **$-600\text{ mA}$** | $-500\text{ mA}$ |
| **Transition Freq ($f_T$)**| $250\text{ MHz}$ | $100\text{ MHz}$ | $50\text{ MHz}$ |
| **Complementary NPN** | 2N3904 | 2N5551 | **MPSA42** |

## Common mistakes

- **Omitting the anode pull-up resistor:** In high-side switching, the base of the MPSA92 must be tied to the $+170\text{V}$ rail through a pull-up resistor ($47\text{k}\Omega \dots 100\text{k}\Omega$) so that the base voltage equals the emitter voltage when the lower NPN driver is turned off. Without this pull-up, leakage current will cause the Nixie tube digits to ghost or faintly glow.

## Notes

- **Suffix Guide:** `MPSA92` is standard TO-92; `KSP92` is the Fairchild/onsemi tape-and-reel catalog designation; `MMBTA92` is the SOT-23 SMD version.
