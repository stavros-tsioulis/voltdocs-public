## Overview

The **PT2399** (commonly supplied in a 16-pin DIP package) is a legendary CMOS digital audio echo/delay processor IC manufactured by Princeton Technology Corp. Iconic among DIY audio builders, guitar effect pedal designers (such as delay, reverb, and chorus pedals), and karaoke equipment manufacturers, it integrates an ADC, DAC, **44K-bit SRAM memory**, and an internal VCO clock on a single chip.

By adjusting a single external resistor connected to the `VCO` frequency pin (Pin 6) to ground, the PT2399 generates continuous analog audio delays ranging from **$31\text{ ms}$ to over $340\text{ ms}$** with low total harmonic distortion ($\text{THD} < 0.5\%$).

## Quick reference

| | |
|---|---|
| **Audio Function** | Digital Echo / Delay Audio Processor |
| **Package** | 16-Pin DIP (Through-Hole) / SOIC-16 |
| **Supply Voltage Range ($V_{CC}$)** | $4.5\text{ V}$ to $5.5\text{ V}$ DC ($5.0\text{ V}$ nominal) |
| **Internal Memory** | $44\text{ Kbit}$ SRAM shift register |
| **Delay Time Range** | $31.2\text{ ms}$ (at $R_{VCO} = 1\text{k}\Omega$) to $342\text{ ms}$ (at $R_{VCO} = 27.5\text{k}\Omega$) |
| **Signal-to-Noise Ratio (SNR)** | $90\text{ dB}$ typical |
| **Total Harmonic Distortion (THD)** | $0.4\%$ typical (at $V_{IN} = 0.5\text{Vrms}, 31.2\text{ms}$ delay) |

## Pinout (16-Pin DIP Package)

```
        ┌──────────────┐
    VCC ─│ 1         16 │─ LPF1_IN
    REF ─│ 2         15 │─ LPF1_OUT
   AGND ─│ 3         14 │─ LPF2_OUT
   DGND ─│ 4         13 │─ LPF2_IN
  CLK_O ─│ 5         12 │─ OP2_OUT
    VCO ─│ 6         11 │─ OP2_IN
    CC1 ─│ 7         10 │─ OP1_IN
    CC0 ─│ 8          9 │─ OP1_OUT
        └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `VCC` | Digital $+5.0\text{V}$ power supply input |
| 2 | `REF` | Analog reference voltage output ($\frac{1}{2} V_{CC}$) |
| 3 | `AGND` | Analog ground reference |
| 4 | `DGND` | Digital ground reference |
| 5 | `CLK_O` | Internal VCO clock test output |
| 6 | `VCO` | Delay time adjustment pin (Resistor $R_{VCO}$ connected to GND sets delay) |
| 7 | `CC1` | Current control 1 integration capacitor connection |
| 8 | `CC0` | Current control 0 integration capacitor connection |
| 9 | `OP1_OUT` | Internal Op-Amp 1 output |
| 10 | `OP1_IN` | Internal Op-Amp 1 inverting input |
| 11 | `OP2_IN` | Internal Op-Amp 2 inverting input |
| 12 | `OP2_OUT` | Internal Op-Amp 2 output |
| 13 | `LPF2_IN` | Low-pass filter 2 input pin |
| 14 | `LPF2_OUT` | Low-pass filter 2 output pin |
| 15 | `LPF1_OUT` | Low-pass filter 1 output pin |
| 16 | `LPF1_IN` | Low-pass filter 1 input pin |

## Delay Time vs VCO Resistance ($R_{VCO}$)

| Resistor $R_{VCO}$ (Pin 6 to GND) | Clock Frequency ($f_{CLK}$) | Delay Time ($t_D$) | Total Harmonic Distortion (THD) |
|---|---|---|---|
| $0.5\ \text{k}\Omega$ | $22.6\ \text{MHz}$ | $31.2\ \text{ms}$ | $0.4\%$ |
| $2.0\ \text{k}\Omega$ | $11.4\ \text{MHz}$ | $62.0\ \text{ms}$ | $0.5\%$ |
| $5.0\ \text{k}\Omega$ | $5.33\ \text{MHz}$ | $132.6\ \text{ms}$ | $0.8\%$ |
| $10.0\ \text{k}\Omega$ | $2.84\ \text{MHz}$ | $248.5\ \text{ms}$ | $1.0\%$ |
| $20.0\ \text{k}\Omega$ | $1.73\ \text{MHz}$ | $342.0\ \text{ms}$ | $2.5\%$ |

## Typical Application Circuit (Guitar Delay Pedal Core)

```
                       ┌─────────────────────────┐
    Analog Audio IN ─> │ Pin 16: LPF1_IN         │
                       │          PT2399         │
    Delay Potentiometer│                         │
    (10kΩ + 1kΩ) ────> │ Pin 6: VCO              │
                       │                         │
                       │ Pin 14: LPF2_OUT        │ ───> Delayed Audio OUT
                       └─────────────────────────┘
```

## Common mistakes

- **Using a resistance below $1\ \text{k}\Omega$ on Pin 6 (`VCO`):** Reducing $R_{VCO}$ below $1\ \text{k}\Omega$ overclocks the internal VCO memory controller, causing the PT2399 to lock up or latch into a muted state on startup. Always place a $1\ \text{k}\Omega$ fixed resistor in series with any delay potentiometer.
- **Connecting AGND and DGND without proper PCB routing:** Connect Pin 3 (`AGND`) and Pin 4 (`DGND`) together directly at the IC pins to prevent digital clock noise bleeding into the high-gain analog audio path.

## Notes

- **Analog Lo-Fi Character:** At longer delay times ($> 200\text{ ms}$), the PT2399 introduces warm, lo-fi analog-like degradation and clock noise, which DIY pedal builders highly prize for tape-echo and vintage delay pedal designs.
