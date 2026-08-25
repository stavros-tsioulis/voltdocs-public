## Overview

The **LF356** (LF356N / LF356M) is an iconic monolithic JFET-input operational amplifier developed by National Semiconductor (now Texas Instruments). As the wide-bandwidth, fast-settling flagship of the pioneering **BI-FET™** technology series, it integrates high-voltage JFETs on the same die with standard bipolar transistors to achieve low input bias currents ($30\text{ pA}$ typical) without sacrificing high-frequency response.

With a **$5.0\text{ MHz}$ gain bandwidth product**, a slew rate of **$12.0\text{ V/}\mu\text{s}$**, and an ultra-fast settling time of **$1.5\ \mu\text{s}$ to $0.01\%$**, the LF356 has maintained a loyal following for decades in modular synthesizer circuits (analog VCOs, VCFs, and envelope generators), precision sample-and-hold amplifiers, logarithmic amplifiers, high-impedance electrometers, and DAC current-to-voltage converters.

## Quick reference

| | |
|---|---|
| **Amplifier Type** | Monolithic BI-FET™ JFET-Input Operational Amplifier |
| **Package** | 8-pin PDIP (LF356N) / 8-pin SOIC (LF356M) / TO-99 Metal Can |
| **Gain Bandwidth Product** | $5.0\text{ MHz}$ typical |
| **Slew Rate** | $12.0\text{ V/}\mu\text{s}$ typical ($7.5\text{ V/}\mu\text{s}$ minimum) |
| **Settling Time (to 0.01%)** | $1.5\ \mu\text{s}$ ($10\text{V}$ step) |
| **Input Bias Current ($I_B$)** | $30\text{ pA}$ typical / $200\text{ pA}$ maximum ($T_A = 25^\circ\text{C}$) |
| **Input Voltage Noise ($e_n$)** | $12\text{ nV}/\sqrt{\text{Hz}}$ at $1\text{ kHz}$ |
| **Supply Voltage Range** | $\pm 5.0\text{ V}$ to $\pm 18.0\text{ V}$ split (or $+10\text{V}$ to $+36\text{V}$ single) |
| **Supply Current** | $5.0\text{ mA}$ typical / $10.0\text{ mA}$ maximum |

## Pinout (DIP-8 / SOIC-8 Package)

```
        ┌──────────────┐
  BAL1  ─│ 1          8 │─ NC
   IN-  ─│ 2   LF     7 │─ V+
   IN+  ─│ 3   356    6 │─ OUT
    V-  ─│ 4          5 │─ BAL2
        └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `BAL1` | Offset balance terminal 1 (Connect $25\text{ k}\Omega$ trim pot wiper to V-) |
| 2 | `IN-` | Inverting analog input (JFET high-impedance gate) |
| 3 | `IN+` | Non-inverting analog input (JFET high-impedance gate) |
| 4 | `V-` | Negative power supply rail ($-5\text{V}$ to $-18\text{V}$ or GND) |
| 5 | `BAL2` | Offset balance terminal 2 |
| 6 | `OUT` | Analog operational amplifier output |
| 7 | `V+` | Positive power supply rail ($+5\text{V}$ to $+18\text{V}$) |
| 8 | `NC` | No internal connection |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Slew Rate | $SR$ | 7.5 | 12.0 | — | $\text{V/}\mu\text{s}$ | $V_S = \pm 15\text{V}, A_V = 1$ |
| Small-Signal Bandwidth | $GBW$ | — | 5.0 | — | MHz | $V_S = \pm 15\text{V}, T_A = 25^\circ\text{C}$ |
| Settling Time to 0.01% | $t_s$ | — | 1.5 | — | $\mu\text{s}$ | $10\text{V}$ step, $A_V = -1$ |
| Input Offset Voltage | $V_{OS}$ | — | 3.0 | 10.0 | mV | $R_S \le 10\text{ k}\Omega$ |
| Input Bias Current | $I_B$ | — | 30 | 200 | pA | $T_A = 25^\circ\text{C}$ |
| Equivalent Input Noise | $e_n$ | — | 12 | 15 | $\text{nV}/\sqrt{\text{Hz}}$ | $f = 1\text{ kHz}$ |
| Common-Mode Rejection Ratio | $CMRR$ | 80 | 100 | — | dB | $V_{CM} = \pm 10\text{V}$ |
| Supply Current | $I_{CC}$ | — | 5.0 | 10.0 | mA | $V_S = \pm 15\text{V}$ |

## Common mistakes

- **JFET Input Phase Reversal:** When input voltages approach the negative supply rail ($V_-$), internal JFET drains can become forward-biased, inverting the output phase. In analog synth integrators and buffer circuits, clamp inputs with Schottky diodes or ensure signal swings remain within $\pm 11\text{V}$ on $\pm 15\text{V}$ rails.
- **Overlooking power dissipation:** Drawing $5\text{ mA} \dots 8\text{ mA}$ quiescent current on $\pm 15\text{V}$ supplies means the package dissipates $\approx 200\text{ mW}$ statically, causing the package to feel noticeably warm to the touch. This self-heating increases input bias current slightly.
- **Grounding the offset balance pins:** Pins 1 and 5 are internal balance nodes. Grounding them unbalances the internal differential stage. Leave unconnected unless actively trimming offset with a $25\text{ k}\Omega$ potentiometer tied to Pin 4 ($V_-$).

## Notes

- **BI-FET Series Family:**
  - **LF355:** Low supply current ($2.0\text{ mA}$), $2.5\text{ MHz}$ bandwidth.
  - **LF356:** Wide bandwidth ($5.0\text{ MHz}$), fast settling ($1.5\ \mu\text{s}$), $5.0\text{ mA}$ supply current.
  - **LF357:** Decompensated high-gain wideband version ($20\text{ MHz}$, $50\text{ V/}\mu\text{s}$, stable for $A_V \ge 5$).
