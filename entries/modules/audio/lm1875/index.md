## Overview

The **LM1875** (LM1875T) is a 20W monolithic high-fidelity audio power amplifier IC manufactured by Texas Instruments (originally National Semiconductor). Enclosed in a **5-lead TO-220 package**, it is famous in audiophile communities as the basis of the legendary **"Gainclone"** DIY hi-fi amplifier builds.

Delivering up to **20 Watts RMS into $4\ \Omega$ or $8\ \Omega$ speakers** with ultra-low Total Harmonic Distortion (**$\text{THD} = 0.015\%$** at 1 kHz), the LM1875 operates on split power supplies from **$\pm 8\text{V}$ to $\pm 30\text{V}$** (or single supply $16\text{V} \dots 60\text{V}$). It includes internal thermal shutdown protection and output short-circuit protection to ground and power rails.

## Quick reference

| | |
|---|---|
| **Amplifier Type** | Monolithic Hi-Fi Audio Power Amplifier |
| **Output Power** | $20\text{ W}_{\text{RMS}}$ into $4\ \Omega$ or $8\ \Omega$ load at $V_{CC} = \pm 25\text{V}$ |
| **THD + Noise** | $0.015\%$ typical at $1\text{ kHz}, 20\text{W}, 8\ \Omega$ |
| **Supply Voltage (Split Rail)** | $\pm 8.0\text{ V}$ to $\pm 30.0\text{ V}$ DC |
| **Supply Voltage (Single Rail)** | $16.0\text{ V}$ to $60.0\text{ V}$ DC |
| **Gain Bandwidth Product** | $5.5\text{ MHz}$ |
| **Slew Rate** | $8.0\text{ V}/\mu\text{s}$ |
| **PSRR (Power Supply Rejection)**| $94\text{ dB}$ |
| **Package** | 5-lead TO-220 (TO-220-5 Pentawatt) |

## Pinout (5-Lead TO-220 Package)

Looking at the **front labeled face** of the 5-lead package with leads pointing down:

```
        ┌─────────────┐
        │   O   [TAB] │  (Metal Mounting Tab = V- Supply Rail!)
        ├─────────────┤
        │   LM1875T   │  (Front Package Face)
        └─┬─┬─┬─┬─┬───┘
          1 2 3 4 5
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `+IN` | Input | Non-Inverting Audio Signal Input |
| 2 | `-IN` | Input | Inverting Feedback Input |
| 3 | `V-` | Power | Negative Power Supply Rail (Connect to $-V_{CC}$ or GND; Connected to Metal Tab!) |
| 4 | `OUT` | Output | Speaker Output Terminal |
| 5 | `V+` | Power | Positive Power Supply Rail ($+V_{CC}$) |

> [!WARNING]
> Metal Tab Warning: Metal Tab is connected to `V-`!
> The TO-220 metal tab is internally connected to **Pin 3 (`V-`)**. In a split-supply system ($\pm 25\text{V}$), the tab is at **$-25\text{V}$**, NOT ground. Always use a **mica or ceramic insulator** when bolting the LM1875 to a grounded metal heatsink.

## Classic Split-Supply Audio Amplifier Circuit (Gain = 21)

```
        Audio Input ───[1µF Film Cap]───┬─── [Pin 1: +IN]
                                        │
                                  [22kΩ to GND]
                                                              ┌─── R_feedback (22kΩ) ───┐
                                                              │                         │
                                    GND ───[10µF]───[1kΩ]─────┴─── [Pin 2: -IN]         │
                                                                       LM1875           │
  +25V DC Supply Rail ──────────────────────────────────────────── [Pin 5: V+]          │
                                                                                        ├─── Speaker Out (Pin 4) ───► ( + ) Speaker
  -25V DC Supply Rail ──────────────────────────────────────────── [Pin 3: V-] ─────────┤
                                                                                        └─── [Boucherot Cell: 2.2Ω + 0.1µF to GND]
```

## Common mistakes

- **Omitting the output Zobel / Boucherot network ($2.2\ \Omega + 0.1\ \mu\text{F}$):** High-gain power op-amps oscillate at RF frequencies into complex speaker wire inductance. Always connect a $2.2\ \Omega$ resistor in series with a $0.1\ \mu\text{F}$ ceramic capacitor from Output (Pin 4) to GND directly at the chip pins.
- **Insufficient heatsinking:** Dissipating $20\text{W}$ RMS output generates up to $15\text{W}$ of internal heat. Run the chip on a heavy aluminum heatsink ($R_{\theta JA} < 3^\circ\text{C/W}$).

## Notes

- **LM1875 vs TDA2030 / TDA2050:** LM1875 offers lower THD ($0.015\%$ vs $0.5\%$) and higher supply voltage capability ($60\text{V}$ vs $36\text{V}$), making it superior for hi-fi audio.
