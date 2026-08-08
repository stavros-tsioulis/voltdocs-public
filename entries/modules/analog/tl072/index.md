## Overview

The **TL072** (TL072CP / TL072CD) is an industry-standard low-noise JFET-input dual operational amplifier manufactured by Texas Instruments, STMicroelectronics, and ON Semiconductor. Incorporating high-voltage JFET and bipolar transistors on a single monolithic chip, it provides extremely low input bias currents ($65\text{ pA}$ typical) and input offset currents.

Featuring a high slew rate of **13 V/µs**, a **3 MHz gain-bandwidth product**, low harmonic distortion ($0.003\%$), and low noise ($18\text{ nV}/\sqrt{\text{Hz}}$), the TL072 is ubiquitous in high-fidelity audio preamplifiers, active equalizer filters, audio mixers, modular synthesizers, and guitar effects pedals.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC+ / VCC-`)** | $\pm 3.0\text{V}$ to $\pm 18.0\text{V}$ (Split) or $+6.0\text{V}$ to $+36.0\text{V}$ (Single) |
| **Gain Bandwidth Product (GBW)** | $3.0\text{ MHz}$ typical |
| **Slew Rate** | $13.0\text{ V}/\mu\text{s}$ typical |
| **Equivalent Input Noise Voltage** | $18\text{ nV}/\sqrt{\text{Hz}}$ at $f = 1\text{kHz}$ |
| **Input Bias Current** | $65\text{ pA}$ typical (JFET input stage) |
| **Quiescent Current** | $1.4\text{ mA}$ per amplifier channel |
| **Package** | 8-pin DIP / SOIC-8 / TSSOP-8 |

## Pinout (DIP-8 Package)

```
             ┌───┴───┐
       1OUT 1│ 1   8 │ VCC+
       1-IN 2│       │ 7 2OUT
       1+IN 3│ TL072 │ 6 2-IN
       VCC- 4│       │ 5 2+IN
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `1OUT` | Output | Amplifier Channel 1 Output |
| 2 | `1-IN` | Input | Amplifier Channel 1 Inverting Input |
| 3 | `1+IN` | Input | Amplifier Channel 1 Non-Inverting Input |
| 4 | `VCC-` | Power | Negative Supply Voltage (or GND in single-supply mode) |
| 5 | `2+IN` | Input | Amplifier Channel 2 Non-Inverting Input |
| 6 | `2-IN` | Input | Amplifier Channel 2 Inverting Input |
| 7 | `2OUT` | Output | Amplifier Channel 2 Output |
| 8 | `VCC+` | Power | Positive Supply Voltage (+3.0V to +18.0V DC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | $\pm 3.0$ | $\pm 15.0$ | $\pm 18.0$ | V | Split supply |
| Input Offset Voltage | $V_{IO}$ | — | 3.0 | 6.0 | mV | $V_{CC} = \pm 15\text{V}, T_A = 25^\circ\text{C}$ |
| Input Bias Current | $I_{IB}$ | — | 65 | 200 | pA | $V_{CC} = \pm 15\text{V}$ |
| Large Signal Voltage Gain | $A_{VD}$ | 25 | 200 | — | V/mV | $V_{CC} = \pm 15\text{V}, R_L = 2\text{k}\Omega$ |
| Common Mode Rejection Ratio | $CMRR$ | 70 | 100 | — | dB | $V_{CC} = \pm 15\text{V}$ |
| Total Harmonic Distortion | $THD$ | — | 0.003 | — | % | $f = 1\text{kHz}, A_{VD} = 1$ |

## Typical Application Circuit (Inverting Audio Preamplifier)

```
                       +15V [Pin 8: VCC+]
                        │
                        ├─────────────────┐
                        │                 │
  Audio In ───[10µF]───[R_in 10k]──┬─────[R_fb 100k]──┐
                                   │                  │
                                [Pin 2: 1-IN]         │
                                [Pin 1: 1OUT] ────────┴───[10µF]──► Audio Out
                                [Pin 3: 1+IN]
                                   │
                                  GND
                        │
                       -15V [Pin 4: VCC-]
```

$$\text{Voltage Gain:} \quad A_V = -\frac{R_{fb}}{R_{in}} = -\frac{100\text{ k}\Omega}{10\text{ k}\Omega} = -10 \quad (20\text{ dB})$$

## Common mistakes

- **Phase Inversion when input voltage approaches negative rail ($V_{CC-}$):** JFET-input op-amps like the TL072 exhibit phase inversion if the input voltage falls within approximately $3\text{V}$ of the negative supply rail ($V_{CC-}$). If an input dips too low, the output instantly flips to the positive supply rail.
- **Operating on single 5V logic supply:** The TL072 is **not** a low-voltage or rail-to-rail op-amp. It requires at least $6\text{V}$ total supply span ($\pm 3\text{V}$ or $+6\text{V}$). Attempting to power a TL072 from a $5\text{V}$ single supply leaves almost zero usable input common-mode range.
- **Unused second channel inputs left floating:** Leaving pins 5, 6, and 7 of the second op-amp floating will cause high-frequency self-oscillation and draw excessive supply current. Connect the unused second channel as a unity-gain buffer ($2OUT$ connected to $2-IN$, $2+IN$ connected to ground or virtual ground).

## Notes

- **TL071 vs TL072 vs TL074:** TL071 is a single op-amp (DIP-8); TL072 is a dual op-amp (DIP-8); TL074 is a quad op-amp (DIP-14).
- **TL072 vs TL082 vs NE5532:** TL072 is selected for low noise audio; TL082 has higher noise; NE5532 is bipolar (higher drive current into low impedance loads, but higher input bias current).
