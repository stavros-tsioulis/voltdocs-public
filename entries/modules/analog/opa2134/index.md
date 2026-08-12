## Overview

The **OPA2134** (commonly **OPA2134PA** in DIP-8 or **OPA2134UA** in SOIC-8) is a legendary SoundPlus™ FET-input dual audio operational amplifier manufactured by Texas Instruments (originally Burr-Brown). Iconic among audiophiles and DIY audio builders, its true FET-input stage provides ultra-low input bias current (**$5\text{ pA}$**) while delivering ultra-low distortion ($\text{THD+N} = \mathbf{0.00008\%}$).

Featuring a fast slew rate of **$20\text{ V}/\mu\text{s}$**, an $8\text{ MHz}$ gain bandwidth, and high output drive capacity into $600\ \Omega$ loads, the OPA2134 is widely used in high-end headphone amplifiers, active crossover networks, studio mixing consoles, and phono preamp stages.

## Quick reference

| | |
|---|---|
| **Op-Amp Type** | SoundPlus™ FET-Input Dual Audio Operational Amplifier |
| **Package** | 8-Pin DIP (Through-Hole) / SOIC-8 |
| **Supply Voltage Range ($V_{CC}$)** | $\pm 2.5\text{ V}$ to $\pm 18.0\text{ V}$ ($5.0\text{ V}$ to $36.0\text{ V}$ single supply) |
| **THD+N** | $0.00008\%$ typical ($f = 1\text{kHz}, R_L = 2\text{k}\Omega$) |
| **Input Bias Current** | $5.0\text{ pA}$ typical (FET Input) |
| **Input Voltage Noise** | $8.0\text{ nV}/\sqrt{\text{Hz}}$ at $f = 1\text{kHz}$ |
| **Slew Rate** | $20.0\text{ V}/\mu\text{s}$ |
| **Gain Bandwidth Product (GBW)** | $8.0\text{ MHz}$ |

## Pinout (Standard Dual Op-Amp 8-Pin Package)

```
        ┌──────────┐
  OUT A ─│ 1      8 │─ V+
  -IN A ─│ 2      7 │─ OUT B
  +IN A ─│ 3      6 │─ -IN B
     V- ─│ 4      5 │─ +IN B
        └──────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `OUT A` | Operational Amplifier A output |
| 2 | `-IN A` | Operational Amplifier A inverting input |
| 3 | `+IN A` | Operational Amplifier A non-inverting input |
| 4 | `V-` / `GND` | Negative power supply rail ($-15\text{V}$ for dual supply, $0\text{V}$ for single supply) |
| 5 | `+IN B` | Operational Amplifier B non-inverting input |
| 6 | `-IN B` | Operational Amplifier B inverting input |
| 7 | `OUT B` | Operational Amplifier B output |
| 8 | `V+` | Positive power supply rail ($+15\text{V}$ for dual supply) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage Range | $V_{CC}$ | $\pm 2.5$ | $\pm 15$ | $\pm 18$ | V | Dual supply range |
| Total Harmonic Distortion | $\text{THD+N}$ | — | 0.00008 | — | % | $f = 1\text{kHz}, V_{OUT} = 3\text{Vrms}, R_L = 2\text{k}\Omega$ |
| Input Bias Current | $I_{B}$ | — | 5 | 100 | pA | $V_{CM} = 0\text{V}$ |
| Input Noise Density | $e_n$ | — | 8.0 | — | $\text{nV}/\sqrt{\text{Hz}}$ | $f = 1\text{kHz}$ |
| Slew Rate | $SR$ | 15 | 20 | — | $\text{V}/\mu\text{s}$ | $R_L = 2\text{k}\Omega$ |
| Gain Bandwidth Product | $GBW$ | — | 8.0 | — | MHz | |
| Quiescent Current | $I_Q$ | — | 4.0 | 5.0 | mA | Per amplifier ($I_O = 0$) |

## Common mistakes

- **Leaving inputs floating in high-impedance circuits:** Because the FET inputs consume virtually zero bias current ($5\text{ pA}$), an unconnected input pin will drift to a supply rail, saturating the output. Always provide a DC path to ground (e.g. $100\text{k}\Omega \dots 1\text{M}\Omega$ resistor).
- **Substituted into low-voltage 3.3V circuits:** The OPA2134 requires at least $5.0\text{ V}$ ($\pm 2.5\text{ V}$) for linear operation. Do not use in 3.3V single-supply systems.

## Notes

- **SoundPlus Audio Pedigree:** Designed specifically by Burr-Brown for audio, offering warm, natural sonic reproduction with virtually zero crossover distortion.
