## Overview

The **LF351** (LF351N / LF351DT) is a low-cost, high-speed single operational amplifier featuring internally trimmed JFET input transistors, manufactured by Texas Instruments and STMicroelectronics (originally developed by National Semiconductor). Designed as an economical, pin-compatible high-speed upgrade over legacy bipolar op-amps like the LM741, it offers an exceptionally high input impedance of **$10^{12}\ \Omega$** ($1\text{ T}\Omega$) and a typical input bias current of just **$50\text{ pA}$**.

With an internally compensated **$4.0\text{ MHz}$ gain bandwidth product** and a fast **$13.0\text{ V/}\mu\text{s}$ slew rate**, the LF351 settles rapidly with low harmonic distortion. It is widely used in high-impedance buffer stages, active audio tone controls, sample-and-hold circuits, peak detectors, and photodiode transimpedance amplifiers.

## Quick reference

| | |
|---|---|
| **Amplifier Type** | Single JFET-Input Operational Amplifier |
| **Package** | 8-pin PDIP (LF351N) / 8-pin SOIC (LF351D) |
| **Gain Bandwidth Product** | $4.0\text{ MHz}$ typical |
| **Slew Rate** | $13.0\text{ V/}\mu\text{s}$ ($16.0\text{ V/}\mu\text{s}$ typical) |
| **Input Impedance** | $10^{12}\ \Omega$ ($1\text{ T}\Omega$) |
| **Input Bias Current ($I_B$)** | $50\text{ pA}$ typical / $200\text{ pA}$ maximum ($T_A = 25^\circ\text{C}$) |
| **Supply Voltage Range** | $\pm 5.0\text{ V}$ to $\pm 18.0\text{ V}$ split (or $+10\text{V}$ to $+36\text{V}$ single) |
| **Supply Current** | $1.8\text{ mA}$ typical / $3.4\text{ mA}$ maximum |
| **Total Harmonic Distortion ($THD$)**| $< 0.02\%$ ($f = 1\text{ kHz}, A_V = 1$) |

## Pinout (DIP-8 / SOIC-8 Package)

```
        ┌──────────────┐
  BAL1  ─│ 1          8 │─ NC
   IN-  ─│ 2   LF     7 │─ V+
   IN+  ─│ 3   351    6 │─ OUT
    V-  ─│ 4          5 │─ BAL2
        └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `BAL1` | Offset null / balance terminal 1 (Connect $10\text{ k}\Omega$ trim pot wiper to V-) |
| 2 | `IN-` | Inverting analog input (JFET high-impedance gate) |
| 3 | `IN+` | Non-inverting analog input (JFET high-impedance gate) |
| 4 | `V-` | Negative power supply rail ($-5\text{V}$ to $-18\text{V}$ or GND) |
| 5 | `BAL2` | Offset null / balance terminal 2 |
| 6 | `OUT` | Analog operational amplifier output |
| 7 | `V+` | Positive power supply rail ($+5\text{V}$ to $+18\text{V}$) |
| 8 | `NC` | No internal connection |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Slew Rate | $SR$ | — | 13.0 | 16.0 | $\text{V/}\mu\text{s}$ | $V_S = \pm 15\text{V}, A_V = 1$ |
| Unity Gain Bandwidth | $GBW$ | 3.0 | 4.0 | — | MHz | $V_S = \pm 15\text{V}, T_A = 25^\circ\text{C}$ |
| Input Offset Voltage | $V_{OS}$ | — | 5.0 | 10.0 | mV | $R_S \le 10\text{ k}\Omega$ |
| Input Bias Current | $I_B$ | — | 50 | 200 | pA | $T_A = 25^\circ\text{C}$ |
| Large-Signal Voltage Gain | $A_{VD}$ | 25 | 100 | — | V/mV | $V_O = \pm 10\text{V}, R_L \ge 2\text{ k}\Omega$ |
| Common-Mode Rejection Ratio | $CMRR$ | 70 | 100 | — | dB | $V_{CM} = \pm 10\text{V}$ |
| Supply Current | $I_{CC}$ | — | 1.8 | 3.4 | mA | $V_S = \pm 15\text{V}$ |

## Common mistakes

- **JFET Input Phase Reversal (Latch-up):** If the input common-mode voltage is driven too close to the negative rail ($V_-$), JFET input stages can experience phase reversal, flipping the output to the positive rail and causing system latch-up. Keep inputs at least $3\text{V}$ above $V_-$.
- **High temperature bias current increase:** While JFET input bias current is tiny at room temperature ($50\text{ pA}$ at $25^\circ\text{C}$), it doubles every $10^\circ\text{C}$, reaching several nanoamperes above $70^\circ\text{C}$.
- **Unused offset null pins left connected to signal lines:** Pins 1 and 5 are internal balance nodes connected directly to the input diff-pair current mirrors. Leave pins 1 and 5 floating if offset nulling is not needed; never connect them to ground or signal lines.

## Notes

- **Single vs Dual:** The LF351 is the single op-amp variant; the **LF353** (and TL072/TL082) provides dual JFET op-amps in the same family.
