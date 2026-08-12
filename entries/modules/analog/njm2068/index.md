## Overview

The **NJM2068** (commonly **NJM2068D** in an 8-pin DIP package) is a low-noise, high-slew-rate dual operational amplifier manufactured by New Japan Radio (NJR / Nisshinbo Micro Devices). Designed specifically for audio preamplifiers, active equalizer networks, and mixing consoles, it offers superior noise performance compared to classic 4558 and 072 op-amps.

Featuring an equivalent input noise voltage of **$0.44\ \mu\text{Vrms}$**, a gain-bandwidth product of **$27\text{ MHz}$**, and a slew rate of **$6.0\text{ V}/\mu\text{s}$**, the NJM2068 is widely deployed in commercial audio equipment and DIY audio preamps.

## Quick reference

| | |
|---|---|
| **Op-Amp Type** | Low-Noise High-Slew-Rate Dual Audio Operational Amplifier |
| **Package** | 8-Pin DIP (Through-Hole) / DMP-8 / SSOP-8 |
| **Supply Voltage Range ($V_{CC}$)** | $\pm 4.0\text{ V}$ to $\pm 18.0\text{ V}$ ($8.0\text{ V}$ to $36.0\text{ V}$ single supply) |
| **Equivalent Input Noise Voltage** | $0.44\ \mu\text{Vrms}$ typical ($R_S = 2.2\text{k}\Omega$, RIAA filter) |
| **Gain Bandwidth Product (GBW)** | $27\text{ MHz}$ (at $f = 10\text{kHz}$) / $19\text{ MHz}$ unity gain |
| **Slew Rate** | $6.0\text{ V}/\mu\text{s}$ |
| **THD** | $0.001\%$ typical ($f = 1\text{kHz}, V_O = 5\text{Vrms}$) |

## Pinout (Standard Dual Op-Amp 8-Pin Package)

```
        ┌──────────┐
  A OUT ─│ 1      8 │─ V+
  A -IN ─│ 2      7 │─ B OUT
  A +IN ─│ 3      6 │─ B -IN
     V- ─│ 4      5 │─ B +IN
        └──────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `A OUTPUT` | Operational Amplifier A output |
| 2 | `A -INPUT` | Operational Amplifier A inverting input |
| 3 | `A +INPUT` | Operational Amplifier A non-inverting input |
| 4 | `V-` / `GND` | Negative power supply rail ($-15\text{V}$ for dual supply, $0\text{V}$ for single supply) |
| 5 | `B +INPUT` | Operational Amplifier B non-inverting input |
| 6 | `B -INPUT` | Operational Amplifier B inverting input |
| 7 | `B OUTPUT` | Operational Amplifier B output |
| 8 | `V+` | Positive power supply rail ($+15\text{V}$ for dual supply) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage Range | $V^+/V^-$ | $\pm 4.0$ | $\pm 15$ | $\pm 18$ | V | Dual supply range |
| Input Offset Voltage | $V_{IO}$ | — | 0.3 | 3.0 | mV | $R_S \le 10\text{k}\Omega$ |
| Input Bias Current | $I_{IB}$ | — | 150 | 500 | nA | |
| Equivalent Input Noise | $V_{NI}$ | — | 0.44 | — | $\mu\text{Vrms}$ | $R_S = 2.2\text{k}\Omega$, RIAA filter |
| Slew Rate | $SR$ | — | 6.0 | — | $\text{V}/\mu\text{s}$ | $R_L \ge 2\text{k}\Omega$ |
| Gain Bandwidth Product | $GBW$ | — | 27 | — | MHz | $f = 10\text{kHz}$ |
| Operating Current | $I_{CC}$ | — | 5.0 | 7.0 | mA | Both channels ($I_O = 0$) |

## Common mistakes

- **Operating below 8V total supply:** The NJM2068 requires at least $\pm 4.0\text{ V}$ ($\ge 8.0\text{ V}$ single supply) for full internal biasing. Running off a 5V single supply causes severe distortion.
- **High source impedance noise:** Because the NJM2068 uses BJT input transistors, its input bias currents can generate voltage noise across high-resistance feedback networks ($>100\text{k}\Omega$). Keep feedback resistors below $10\text{k}\Omega$ for best noise performance.

## Notes

- **NJM2068 vs RC4558:** The NJM2068 offers 6x higher slew rate ($6\text{V}/\mu\text{s}$ vs $1\text{V}/\mu\text{s}$) and 9x higher bandwidth ($27\text{MHz}$ vs $3\text{MHz}$) than standard 4558 dual op-amps.
