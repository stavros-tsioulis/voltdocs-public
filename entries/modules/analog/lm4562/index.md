## Overview

The **LM4562** (commonly **LM4562NA** in DIP-8 or **LM4562MA** in SOIC-8) is an ultra-low distortion, low-noise, high-slew-rate dual audio operational amplifier manufactured by Texas Instruments (originally National Semiconductor). Belonging to TI's high-fidelity audio series, it sets a benchmark for audio signal processing with a Total Harmonic Distortion plus Noise ($\text{THD+N}$) of just **$0.00003\%$**.

With an extremely low input noise density of **$2.7\text{ nV}/\sqrt{\text{Hz}}$**, a high gain-bandwidth product of **$55\text{ MHz}$**, and a fast slew rate of **$20\text{ V}/\mu\text{s}$**, the LM4562 is widely used as an op-amp rolling upgrade in DAC output stages, headphone amplifiers, phono preamplifiers, and high-end audio gear.

## Quick reference

| | |
|---|---|
| **Op-Amp Type** | Dual Ultra-Low Distortion High-Fidelity Audio Op-Amp |
| **Package** | 8-Pin DIP (Through-Hole) / SOIC-8 |
| **Supply Voltage Range ($V_{CC}$)** | $\pm 2.5\text{ V}$ to $\pm 17.0\text{ V}$ ($5.0\text{ V}$ to $34.0\text{ V}$ single supply) |
| **THD+N** | $0.00003\%$ typical ($f = 1\text{kHz}, R_L = 600\ \Omega$) |
| **Input Noise Voltage** | $2.7\text{ nV}/\sqrt{\text{Hz}}$ at $f = 1\text{kHz}$ |
| **Gain Bandwidth Product (GBW)** | $55\text{ MHz}$ |
| **Slew Rate** | $20\text{ V}/\mu\text{s}$ |
| **Output Drive Capability** | Drives $600\ \Omega$ loads to $V_{CC} - 1\text{V}$ rail-to-rail headroom |

## Pinout (Standard Dual Op-Amp 8-Pin Package)

```
        ┌──────────┐
  1OUT ─│ 1      8 │─ V+
  1IN- ─│ 2      7 │─ 2OUT
  1IN+ ─│ 3      6 │─ 2IN-
    V- ─│ 4      5 │─ 2IN+
        └──────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `1OUT` | Operational Amplifier 1 output |
| 2 | `1IN-` | Operational Amplifier 1 inverting input |
| 3 | `1IN+` | Operational Amplifier 1 non-inverting input |
| 4 | `V-` / `GND` | Negative power supply rail ($-15\text{V}$ for dual supply, $0\text{V}$ for single supply) |
| 5 | `2IN+` | Operational Amplifier 2 non-inverting input |
| 6 | `2IN-` | Operational Amplifier 2 inverting input |
| 7 | `2OUT` | Operational Amplifier 2 output |
| 8 | `V+` | Positive power supply rail ($+15\text{V}$ for dual supply) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage Range | $V_{CC}$ | $\pm 2.5$ | $\pm 15$ | $\pm 17$ | V | Dual supply range |
| Total Harmonic Distortion | $\text{THD+N}$ | — | 0.00003 | — | % | $f = 1\text{kHz}, V_{OUT} = 3\text{Vrms}, R_L = 600\Omega$ |
| Input Noise Density | $e_n$ | — | 2.7 | 4.0 | $\text{nV}/\sqrt{\text{Hz}}$ | $f = 1\text{kHz}$ |
| Slew Rate | $SR$ | 15 | 20 | — | $\text{V}/\mu\text{s}$ | $R_L = 2\text{k}\Omega$ |
| Gain Bandwidth Product | $GBW$ | — | 55 | — | MHz | $f = 100\text{kHz}$ |
| Open-Loop Voltage Gain | $A_{VD}$ | 110 | 140 | — | dB | $R_L = 600\Omega$ |
| Supply Current | $I_S$ | — | 10 | 12 | mA | Both amplifiers ($I_O = 0$) |

## Common mistakes

- **Leaving supply bypass capacitors off:** Because the LM4562 has a wide $55\text{ MHz}$ bandwidth, place $100\text{ nF}$ ceramic decoupling capacitors directly across Pin 8 (`V+`) to GND and Pin 4 (`V-`) to GND. Omitting supply bypass caps can induce high-frequency parasitic oscillation.
- **Operating on single 5V logic supply without biasing inputs:** The LM4562 is not a rail-to-rail input op-amp. When operating on a single +5V supply, input signals must be biased to mid-rail ($2.5\text{ V}$) to prevent input clipping.

## Notes

- **LME49720 Equivalence:** The LME49720 is functionally identical to the LM4562 (same silicon die packaged under TI/National's LME high-performance audio series).
