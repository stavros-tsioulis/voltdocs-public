## Overview

The **LM324** (and DIP-14 **LM324N**) is an industry-standard quad operational amplifier IC manufactured by Texas Instruments, STMicroelectronics, and ON Semiconductor. Containing **four independent, high-gain, internally frequency-compensated op-amps** in a single 14-pin package, it is a staple of analog active filters, multi-channel comparator systems, audio mixers, and sensor signal conditioning arrays.

Designed to operate from either a **single supply ($3.0\text{V}$ to $32.0\text{V}$ DC)** or **split supplies ($\pm 1.5\text{V}$ to $\pm 16.0\text{V}$)**, the common-mode input range of each channel includes Ground ($0\text{V}$).

## Quick reference

| | |
|---|---|
| **Op-Amp Channels** | 4 Independent Operational Amplifiers |
| **Package** | 14-pin DIP (LM324N) / SOIC-14 / TSSOP-14 |
| **Single Supply Voltage Range** | $3.0\text{ V}$ to $32.0\text{ V}$ DC |
| **Split Supply Voltage Range** | $\pm 1.5\text{ V}$ to $\pm 16.0\text{ V}$ DC |
| **Gain-Bandwidth Product (GBW)**| $1.2\text{ MHz}$ |
| **Slew Rate** | $0.5\text{ V}/\mu\text{s}$ |
| **Input Offset Voltage** | $2.0\text{ mV}$ typical / $5.0\text{ mV}$ max |
| **Quiescent Current** | $800\ \mu\text{A}$ total (across all 4 channels) |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
      OUT 1 ─┤ 1  14 ├─ OUT 4
     -IN 1  ─┤ 2  13 ├─ -IN 4
     +IN 1  ─┤ 3  12 ├─ +IN 4
       VCC  ─┤ 4  11 ├─ GND (-VCC)
     +IN 2  ─┤ 5  10 ├─ +IN 3
     -IN 2  ─┤ 6   9 ├─ -IN 3
      OUT 2 ─┤ 7   8 ├─ OUT 3
             └───────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `OUT 1` | Op-Amp 1 Output |
| 2 | `-IN 1` | Op-Amp 1 Inverting Input |
| 3 | `+IN 1` | Op-Amp 1 Non-Inverting Input |
| 4 | `VCC` | Positive Power Supply Input (+3.0V to +32V DC) |
| 5 | `+IN 2` | Op-Amp 2 Non-Inverting Input |
| 6 | `-IN 2` | Op-Amp 2 Inverting Input |
| 7 | `OUT 2` | Op-Amp 2 Output |
| 8 | `OUT 3` | Op-Amp 3 Output |
| 9 | `-IN 3` | Op-Amp 3 Inverting Input |
| 10 | `+IN 3` | Op-Amp 3 Non-Inverting Input |
| 11 | `GND` / `-VCC` | Ground reference (0 V) or Negative Power Supply ($-\text{V}_{CC}$) |
| 12 | `+IN 4` | Op-Amp 4 Non-Inverting Input |
| 13 | `-IN 4` | Op-Amp 4 Inverting Input |
| 14 | `OUT 4` | Op-Amp 4 Output |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Single Supply Voltage | $V_{CC}$ | 3.0 | 5.0 | 32.0 | V | DC |
| Total Quiescent Current | $I_{CC}$ | — | 800 | 1200 | µA | All 4 channels, no load |
| Input Offset Voltage | $V_{IO}$ | — | 2.0 | 5.0 | mV | $T_A = 25^\circ\text{C}$ |
| Input Bias Current | $I_{IB}$ | — | 45 | 100 | nA | $V_{CM} = 0\text{V}$ |
| Large Signal Voltage Gain| $A_{VD}$ | 25 | 100 | — | V/mV | $V_{CC} = 15\text{V}, R_L \ge 2\text{k}\Omega$ |
| Channel Separation | $CS$ | — | 120 | — | dB | $f = 1\text{ kHz} \dots 20\text{ kHz}$ |

## Common mistakes

- **Leaving unused op-amp channels floating:** Leaving unused op-amps floating causes high-frequency self-oscillations that inject noise onto the power rails. Connect `-IN` to `OUT` (unity-gain follower configuration) and tie `+IN` to ground or a fixed DC voltage.
- **Exceeding $V_{CC} - 1.5\text{V}$ output swing:** Like the LM358, the LM324 is not a rail-to-rail output op-amp. At a single $5.0\text{V}$ supply, maximum output voltage swings to $\sim 3.5\text{V}$.

## Notes

- **LM324 vs LM358 vs TL074:** LM324 is a quad version of the LM358; TL074 is a quad JFET-input low-noise audio op-amp.
