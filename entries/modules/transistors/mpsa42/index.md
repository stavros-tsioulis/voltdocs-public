## Overview

The **MPSA42** (and its SMD variant **MMBTA42**) is an ultra-high-voltage NPN bipolar junction transistor manufactured by onsemi, Fairchild, STMicroelectronics, and Central Semiconductor. Housed in a through-hole **TO-92** plastic package with `Emitter - Base - Collector` (E-B-C) pinout, it is legendary across the retro-electronics and DIY maker community as the standard discrete driver for **Nixie tubes**.

Engineered with a massive collector-emitter breakdown voltage ($V_{CEO}$) of **$300\text{V}$** and a continuous collector current of **$500\text{ mA}$**, the MPSA42 easily tolerates the $170\text{V} \dots 200\text{V}$ DC anode supply rails required to ionize neon gas inside vintage cold-cathode display tubes (IN-12, IN-14, IN-18, Z566M). It is universally used in **Nixie tube clocks, neon indicator drivers, vacuum fluorescent display (VFD) filament drivers, electroluminescent (EL) wire inverters, and high-voltage strobe trigger circuits**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | Ultra-High-Voltage Small-Signal NPN BJT |
| **Package** | TO-92 (3-pin through-hole) / SOT-23 (MMBTA42) / SOT-223 (PZTA42) |
| **Collector-Emitter Voltage ($V_{CEO}$)**| **$300\text{ V}$ max** |
| **Collector-Base Voltage ($V_{CBO}$)** | **$300\text{ V}$ max** |
| **Continuous Collector Current ($I_C$)** | **$500\text{ mA}$ max** |
| **DC Current Gain ($h_{FE}$)** | **$40$ to $200$** ($I_C = 10\text{mA}, V_{CE} = 10\text{V}$) |
| **Transition Frequency ($f_T$)** | **$50\text{ MHz}$ min** |
| **Total Power Dissipation ($P_D$)** | $625\text{ mW}$ ($T_A = 25^\circ\text{C}$) |
| **Complementary PNP Pair** | **MPSA92** (300V PNP) |
| **Operating Temp Range** | $-55^\circ\text{C}$ to $+150^\circ\text{C}$ |

## Pinout (TO-92 Package - E-B-C Standard)

Looking at the **flat front face** with leads pointing downward:

```
        ┌─────────┐
        │  TO-92  │
        │ MPSA42  │
        └─┬───┬───┬─┘
          1   2   3
          E   B   C
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `EMITTER` | Emitter Terminal | Emitter (Connect to ground / $0\text{ V}$) |
| 2 | `BASE` | Base Terminal | Base control input (Driven from 3.3V/5V MCU GPIO via series resistor) |
| 3 | `COLLECTOR`| Collector Terminal| Collector output (Connected directly to Nixie tube cathode or high-voltage load) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$ | 300 | — | — | V | $I_C = 1.0\text{mA}, I_B = 0$ |
| Collector-Base Breakdown | $V_{(BR)CBO}$ | 300 | — | — | V | $I_C = 100\ \mu\text{A}, I_E = 0$ |
| Emitter-Base Breakdown | $V_{(BR)EBO}$ | 6.0 | — | — | V | $I_E = 100\ \mu\text{A}, I_C = 0$ |
| Collector Cutoff Current | $I_{CBO}$ | — | — | 100 | nA | $V_{CB} = 200\text{V}, I_E = 0$ |
| DC Current Gain | $h_{FE}$ | 40 | — | — | — | $I_C = 1.0\text{mA}, V_{CE} = 10\text{V}$ |
| DC Current Gain | $h_{FE}$ | 40 | — | 200 | — | $I_C = 10\text{mA}, V_{CE} = 10\text{V}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | — | 0.50 | V | $I_C = 20\text{mA}, I_B = 2.0\text{mA}$ |
| Base Saturation Voltage | $V_{BE(sat)}$ | — | — | 0.90 | V | $I_C = 20\text{mA}, I_B = 2.0\text{mA}$ |

## Typical Nixie Tube Cathode Driver Circuit

In a microcontroller-driven Nixie clock (e.g. ESP32, Arduino, or 74HC595 shift register), ten MPSA42 transistors drive the decimal digit cathodes ($0 \dots 9$):

```
                        +170V to +180V High-Voltage DC Supply
                                          │
                                [ Anode Resistor: 22kΩ 1W ]
                                          │
                                   [ Nixie Tube Anode ]
                                   [   '0' '1' ... '9']
                                        │ (e.g. Digit 7 Cathode)
                                        │
                                 [Pin 3: COLLECTOR]
                                      MPSA42
  MCU GPIO (3.3V / 5.0V)          [Pin 2: BASE]
          │                             │
          ├───[ 4.7kΩ - 10kΩ Resistor ]─┤
          │                             ├───[ 100kΩ Pull-Down Resistor ]──┐
         GND                            │                                 │
                                  [Pin 1: EMITTER]                        │
                                        │                                 │
                                       GND ───────────────────────────────┴─── Common GND
```

## Comparison: MPSA42 vs 2N5551 vs KSP42

| Parameter | MPSA42 | 2N5551 | 2N3904 |
|---|---|---|---|
| **$V_{CEO}$ Voltage** | **$300\text{ V}$** | $160\text{ V}$ | $40\text{ V}$ |
| **Max Current ($I_C$)** | **$500\text{ mA}$** | $600\text{ mA}$ | $200\text{ mA}$ |
| **Nixie (180V) Safe** | **Yes** | No ($160\text{V}$ breakdown is too close) | **No (Destructive Breakdown)** |
| **Transition Freq ($f_T$)**| $50\text{ MHz}$ | $100 \dots 300\text{ MHz}$ | $300\text{ MHz}$ |

## Common mistakes

- **Using standard 40V/60V BJTs (2N3904, BC547) for Nixie tubes:** Nixie cathodes float up to $100\text{V} \dots 170\text{V}$ when extinguished. Using standard 40V transistors causes avalanche breakdown, causing ghosting numerals and immediate destruction of the transistor. Always use **$300\text{V}$ MPSA42** (or K155ID1 / 74141 decoder driver ICs).
- **Omitting base resistors:** Connecting a microcontroller GPIO directly to Pin 2 (Base) without a current-limiting resistor ($4.7\text{k}\Omega \dots 10\text{k}\Omega$) will draw excessive current from the MCU pin and damage the I/O port.

## Notes

- **Complementary Pair:** `MPSA92` is the exact 300V PNP complementary transistor used for high-side switching in multiplexed Nixie display matrices.
