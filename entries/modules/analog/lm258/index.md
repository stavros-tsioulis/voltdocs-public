## Overview

The **LM258** (commonly **LM258N** in DIP-8 or **LM258D** in SOIC-8) is an industrial-grade dual operational amplifier IC manufactured by Texas Instruments, STMicroelectronics, and ON Semiconductor. It consists of two independent, high-gain, internally frequency-compensated operational amplifiers designed to operate from a single power supply over a wide voltage range (**$3.0\text{ V}$ to $32.0\text{ V}$**).

As the **industrial temperature version** of the standard commercial LM358, the LM258 operates across **$-25^\circ\text{C}$ to $+85^\circ\text{C}$** with identical schematic pinouts, low supply current consumption ($0.5\text{ mA}$ typical), and ground-sensing input common-mode range.

## Quick reference

| | |
|---|---|
| **Op-Amp Type** | Industrial Dual General-Purpose Operational Amplifier |
| **Package** | 8-Pin DIP (Through-Hole) / SOIC-8 / VSSOP-8 |
| **Supply Voltage Range ($V_{CC}$)** | $3.0\text{ V}$ to $32.0\text{ V}$ DC ($\pm 1.5\text{ V}$ to $\pm 16.0\text{ V}$ dual supply) |
| **Operating Temperature Range** | $-25^\circ\text{C}$ to $+85^\circ\text{C}$ |
| **Gain Bandwidth Product (GBW)** | $1.0\text{ MHz}$ |
| **Slew Rate** | $0.5\text{ V}/\mu\text{s}$ |
| **Quiescent Supply Current** | $0.5\text{ mA}$ typical (Independent of supply voltage) |

## Pinout (Standard Dual Op-Amp 8-Pin Package)

```
        ┌──────────┐
  1OUT ─│ 1      8 │─ VCC
  1IN- ─│ 2      7 │─ 2OUT
  1IN+ ─│ 3      6 │─ 2IN-
   GND ─│ 4      5 │─ 2IN+
        └──────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `1OUT` | Operational Amplifier 1 output |
| 2 | `1IN-` | Operational Amplifier 1 inverting input |
| 3 | `1IN+` | Operational Amplifier 1 non-inverting input |
| 4 | `GND` / `V-` | Ground reference (0 V) or negative supply rail |
| 5 | `2IN+` | Operational Amplifier 2 non-inverting input |
| 6 | `2IN-` | Operational Amplifier 2 inverting input |
| 7 | `2OUT` | Operational Amplifier 2 output |
| 8 | `VCC` / `V+` | Positive power supply rail (+3.0V to +32.0V DC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage Range | $V_{CC}$ | 3.0 | 5.0 / 15.0 | 32.0 | V | Operational range |
| Input Offset Voltage | $V_{IO}$ | — | 2.0 | 5.0 | mV | $T_A = 25^\circ\text{C}$ |
| Input Bias Current | $I_{IB}$ | — | 20 | 50 | nA | $V_{CM} = 0\text{V}$ |
| Large Signal Voltage Gain | $A_{VD}$ | 25 | 100 | — | V/mV | $V_{CC} = 15\text{V}, R_L \ge 2\text{k}\Omega$ |
| Common-Mode Rejection | $CMRR$ | 65 | 80 | — | dB | |
| Supply Current | $I_{CC}$ | — | 0.5 | 1.0 | mA | Both amplifiers ($I_O = 0$) |

## Common mistakes

- **Expecting Rail-to-Rail Output:** The LM258 output can swing down to $0\text{ V}$ (ground-sensing input stage), but its upper voltage output limit is restricted to approximately $V_{CC} - 1.5\text{V}$. On a $+5\text{ V}$ supply, the maximum output voltage is $\approx +3.5\text{ V}$.
- **Crossover distortion in precision AC circuits:** Like LM358, the LM258 class-B output stage produces crossover distortion around 0V when driving AC signals. Add a $10\text{ k}\Omega$ pull-down resistor from output to GND to bias the output transistor into class-A.

## Notes

- **LM258 vs LM358 vs LM158:** LM358 ($0^\circ\text{C} \dots 70^\circ\text{C}$ commercial), LM258 ($-25^\circ\text{C} \dots 85^\circ\text{C}$ industrial), LM158 ($-55^\circ\text{C} \dots 125^\circ\text{C}$ military).
