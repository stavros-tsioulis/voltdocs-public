## Overview

The **TL074** is a high-speed, quad JFET-input operational amplifier manufactured by Texas Instruments and STMicroelectronics. Containing four independent, internally frequency-compensated operational amplifiers on a single monolithic silicon chip, the TL074 is one of the most widely deployed analog ICs in audio engineering, synthesizer design, and high-impedance signal conditioning.

With high-voltage JFET input transistors providing an input impedance of $10^{12}\text{ }\Omega$, an ultra-low input bias current of $65\text{ pA}$, a fast slew rate of $13\text{ V/}\mu\text{s}$, low harmonic distortion ($0.003\%$), and low noise ($18\text{ nV/}\sqrt{\text{Hz}}$), the TL074 is the standard component of choice for DIY Eurorack modular synthesizer voice modules, active state-variable audio filters, graphic equalizers, and multi-channel preamplifiers.

## Quick reference

| | |
|---|---|
| **Function** | Quad Low-Noise JFET-Input Operational Amplifier |
| **Supply Voltage (Single Supply)** | $6.0\text{ V}$ to $36.0\text{ V}$ DC |
| **Supply Voltage (Split Supply)** | $\pm 3.0\text{ V}$ to $\pm 18.0\text{ V}$ DC ($\pm 15.0\text{ V}$ standard) |
| **Op-Amp Channels** | 4 independent op-amps |
| **Gain Bandwidth Product (GBW)** | $3.0\text{ MHz}$ typ |
| **Slew Rate (SR)** | $13.0\text{ V/}\mu\text{s}$ typ |
| **Equivalent Input Noise** | $18.0\text{ nV/}\sqrt{\text{Hz}}$ at $1\text{ kHz}$ |
| **Input Bias Current ($I_B$)** | $65\text{ pA}$ typ ($200\text{ pA}$ max at $25^\circ\text{C}$) |
| **Input Offset Voltage ($V_{IO}$)** | $3.0\text{ mV}$ typ ($6.0\text{ mV}$ max) |
| **Total Harmonic Distortion (THD)** | $0.003\%$ typ ($f = 1\text{ kHz}, G = 1$) |
| **Supply Current (Total, 4 channels)**| $5.6\text{ mA}$ typ ($1.4\text{ mA}$ per channel) |
| **Packages** | 14-pin PDIP (N), SOIC-14 (D), TSSOP-14 (PW) |

## Pin configuration

### 14-Pin DIP / SOIC Package

```
               ┌──────────┐
         1OUT ─┤ 1     14 ├─ 4OUT
         1IN- ─┤ 2     13 ├─ 4IN-
         1IN+ ─┤ 3     12 ├─ 4IN+
         VCC+ ─┤ 4     11 ├─ VCC- (or GND)
         2IN+ ─┤ 5     10 ├─ 3IN+
         2IN- ─┤ 6      9 ├─ 3IN-
         2OUT ─┤ 7      8 ├─ 3OUT
               └──────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `1OUT` | Analog Output | Output of operational amplifier 1 |
| 2 | `1IN-` | Analog Input | Inverting input of operational amplifier 1 |
| 3 | `1IN+` | Analog Input | Non-inverting input of operational amplifier 1 |
| 4 | `VCC+` | Power Supply | Positive DC power supply rail ($+V_S$, $+5\text{V} \dots +18\text{V}$) |
| 5 | `2IN+` | Analog Input | Non-inverting input of operational amplifier 2 |
| 6 | `2IN-` | Analog Input | Inverting input of operational amplifier 2 |
| 7 | `2OUT` | Analog Output | Output of operational amplifier 2 |
| 8 | `3OUT` | Analog Output | Output of operational amplifier 3 |
| 9 | `3IN-` | Analog Input | Inverting input of operational amplifier 3 |
| 10 | `3IN+` | Analog Input | Non-inverting input of operational amplifier 3 |
| 11 | `VCC-` | Power Supply | Negative DC power supply rail ($-V_S$, $-5\text{V} \dots -18\text{V}$) or Ground |
| 12 | `4IN+` | Analog Input | Non-inverting input of operational amplifier 4 |
| 13 | `4IN-` | Analog Input | Inverting input of operational amplifier 4 |
| 14 | `4OUT` | Analog Output | Output of operational amplifier 4 |

## Functional description

- **High Input Impedance:** JFET inputs eliminate loading errors on high-impedance sources (such as guitar pickups, piezoelectric sensors, and multi-megohm passive filter stages).
- **High Slew Rate:** At $13\text{ V/}\mu\text{s}$, the TL074 avoids slew-induced distortion (SID) across the full $20\text{ Hz}$ to $20\text{ kHz}$ audible spectrum even under large signal amplitudes, making it vastly superior to general-purpose bipolar op-amps like the LM324 ($0.5\text{ V/}\mu\text{s}$) for audio.
- **Internal Frequency Compensation:** Each of the four amplifiers is internally compensated for unity-gain stability without needing external compensation capacitors.

## Absolute maximum ratings

> [!WARNING]
> Stresses beyond these ratings cause permanent damage. Functional operation at these limits is not guaranteed.

| Parameter | Rating | Unit |
|---|---|---|
| Supply Voltage ($V_{CC+} - V_{CC-}$) | 36 ($\pm 18$) | V |
| Differential Input Voltage | $\pm 30$ | V |
| Input Voltage Range ($V_I$) | $\pm 15$ (not to exceed supply rails) | V |
| Output Short-Circuit Duration | Continuous | — |
| Operating Free-Air Temperature ($T_A$, TL074C) | 0 to 70 | °C |
| Operating Free-Air Temperature ($T_A$, TL074I) | -40 to 85 | °C |
| Storage Temperature Range | -65 to 150 | °C |

## Electrical characteristics

$V_{CC\pm} = \pm 15\text{ V}$, $T_A = 25^\circ\text{C}$, unless otherwise noted.

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Offset Voltage | $V_{IO}$ | — | 3.0 | 6.0 | mV | $R_S \le 10\text{ k}\Omega$ |
| Input Bias Current | $I_B$ | — | 65 | 200 | pA | $T_J = 25^\circ\text{C}$ |
| Input Offset Current | $I_{IO}$ | — | 5 | 100 | pA | $T_J = 25^\circ\text{C}$ |
| Large-Signal Voltage Gain | $A_{VD}$ | 50 | 200 | — | $\text{V/mV}$ | $R_L \ge 2\text{ k}\Omega, V_O = \pm 10\text{ V}$ |
| Common-Mode Rejection Ratio | $\text{CMRR}$ | 70 | 100 | — | dB | $V_{ICR} = \pm 11\text{ V}, R_S \le 10\text{ k}\Omega$ |
| Power Supply Rejection Ratio | $\text{PSRR}$ | 70 | 100 | — | dB | $V_{CC\pm} = \pm 9\text{ V}$ to $\pm 15\text{ V}$ |
| Output Voltage Swing | $V_{OM}$ | $\pm 12.0$ | $\pm 13.5$ | — | V | $R_L \ge 2\text{ k}\Omega$ |
| Slew Rate | $\text{SR}$ | 8.0 | 13.0 | — | $\text{V/}\mu\text{s}$ | $G = 1, R_L = 2\text{ k}\Omega, C_L = 100\text{ pF}$ |
| Gain Bandwidth Product | $\text{GBW}$ | — | 3.0 | — | MHz | $f = 100\text{ kHz}$ |
| Total Harmonic Distortion | $\text{THD}$ | — | 0.003 | — | % | $f = 1\text{ kHz}, V_O = 2\text{ V}_{RMS}$ |
| Supply Current (Total 4 Ch) | $I_{CC}$ | — | 5.6 | 10.0 | mA | $V_O = 0\text{ V}$, No load |

## Typical application

### 4-Stage State-Variable Active Audio Filter / Synthesizer VCF

A single TL074 IC provides all four op-amps required for an active state-variable filter topology (Summing Amp, Integrator 1, Integrator 2, Inverter), outputting simultaneous Low-Pass, High-Pass, Band-Pass, and Notch audio outputs with independent cutoff frequency and resonance ($Q$) controls.

```
                  ┌───────────────┐
  Audio In ───────┤ Op-Amp 1 (Sum)├───► High-Pass Output
                  └───────┬───────┘
                          │
                  ┌───────┴───────┐
                  │ Op-Amp 2 (Int)├───► Band-Pass Output
                  └───────┬───────┘
                          │
                  ┌───────┴───────┐
                  │ Op-Amp 3 (Int)├───► Low-Pass Output
                  └───────┬───────┘
                          │
                  ┌───────┴───────┐
                  │ Op-Amp 4 (Inv)│
                  └───────────────┘
```

## Common mistakes

- **JFET Input Phase Reversal:** If an input voltage is driven too close to the negative supply rail ($(V-) + 3\text{ V}$ or below), the input differential pair turns off, causing the op-amp output to instantly invert and snap to the positive rail ($V+$). In single-supply $0\text{V}/12\text{V}$ circuits, grounding an input triggers this phase inversion. Avoid driving inputs within $3\text{ V}$ of the negative rail, or use the modern phase-reversal-free **TL074H** variant.
- **Attempting Operation from Single 5V Supply:** The TL074 requires a minimum supply voltage of $6\text{ V}$ (ideally $\ge \pm 9\text{ V}$ to $\pm 15\text{ V}$). Operating from a single $5\text{ V}$ logic supply leaves less than $1\text{ V}$ of valid common-mode input range. For $3.3\text{ V}$ or $5\text{ V}$ rail-to-rail applications, choose the **MCP6004** instead.
- **Leaving Unused Op-Amp Channels Floating:** Leaving unused channels floating causes their high-gain outputs to oscillate rail-to-rail, drawing excess current and injecting high-frequency hash into adjacent active audio channels. Always configure unused channels as unity-gain voltage followers by tying the output to the inverting input (`OUT` $\rightarrow$ `-IN`) and connecting the non-inverting input (`+IN`) to half-supply ($V_{REF}$) or ground.

## Notes

- **TL07x Family:** **TL071** (single op-amp, DIP-8), **TL072** (dual op-amp, DIP-8), **TL074** (quad op-amp, DIP-14).
- **TL074 vs LM324:** The LM324 is tailored for low-cost DC control where inputs must reach 0V on a single supply, but its crossover distortion and slow $0.5\text{ V/}\mu\text{s}$ slew rate make it unsuitable for audio. The TL074 is tailored for low-distortion, high-slew AC audio signals on dual rails.
