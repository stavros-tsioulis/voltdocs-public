## Overview

The **LM2904** (commonly **LM2904D** in SOIC-8 or **LM2904N** in DIP-8) is an automotive-grade dual operational amplifier IC manufactured by STMicroelectronics, Texas Instruments, and ON Semiconductor. Designed and qualified according to AEC-Q100 standards, it operates across an extended automotive temperature range of **$-40^\circ\text{C}$ to $+125^\circ\text{C}$**.

Sharing an identical pinout and internal architecture with the dual LM358 family, the LM2904 operates from single DC supplies of **$3.0\text{ V}$ to $26.0\text{ V}$** (up to $32.0\text{ V}$ for enhanced versions) with ground-sensing input capability, making it the preferred choice for automotive ECU sensor conditioning and industrial environments.

## Quick reference

| | |
|---|---|
| **Op-Amp Type** | Automotive-Grade AEC-Q100 Dual Operational Amplifier |
| **Package** | 8-Pin DIP (Through-Hole) / SOIC-8 / TSSOP-8 |
| **Supply Voltage Range ($V_{CC}$)** | $3.0\text{ V}$ to $26.0\text{ V}$ DC ($\pm 1.5\text{ V}$ to $\pm 13.0\text{ V}$ dual supply) |
| **Operating Temperature Range** | $-40^\circ\text{C}$ to $+125^\circ\text{C}$ (Full Automotive Grade) |
| **Gain Bandwidth Product (GBW)** | $1.1\text{ MHz}$ |
| **Slew Rate** | $0.6\text{ V}/\mu\text{s}$ |
| **Quiescent Supply Current** | $0.7\text{ mA}$ typical |

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
| 8 | `VCC` / `V+` | Positive power supply rail (+3.0V to +26.0V DC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage Range | $V_{CC}$ | 3.0 | 5.0 / 12.0 | 26.0 | V | Operational range |
| Input Offset Voltage | $V_{IO}$ | — | 2.0 | 7.0 | mV | Full temperature range |
| Input Bias Current | $I_{IB}$ | — | 20 | 100 | nA | $V_{CM} = 0\text{V}$ |
| Gain Bandwidth Product | $GBW$ | — | 1.1 | — | MHz | |
| Slew Rate | $SR$ | — | 0.6 | — | $\text{V}/\mu\text{s}$ | |
| Supply Current | $I_{CC}$ | — | 0.7 | 1.2 | mA | Both amplifiers ($I_O = 0$) |

## Common mistakes

- **Exceeding 26V on standard LM2904 versions:** While standard LM358 handles 32V, standard LM2904 parts specify a $26.0\text{ V}$ maximum operating limit. For $32\text{V}$ automotive systems, use the high-voltage **LM2904A** or **LM2904B** variants.
- **Ignoring upper output swing limitations:** Output voltage swing on a 12V automotive supply is limited to $\approx 10.5\text{ V}$ max ($V_{CC} - 1.5\text{V}$).

## Notes

- **AEC-Q100 Automotive Qualification:** Tested for high thermal cycling endurance and harsh automotive environments (under-hood ECUs, alternator noise rejection, 12V battery transients).
