## Overview

The **OP27** is an industry-standard precision, low-noise operational amplifier manufactured by Analog Devices (originally designed by Precision Monolithics Inc. / PMI). Available in an 8-pin **DIP-8** through-hole and **SOIC-8** surface-mount package, it combines ultra-low input noise voltage (**$3.0\text{ nV}/\sqrt{\text{Hz}}$ at $1\text{ kHz}$**), exceptional DC precision (**$10\ \mu\text{V}$ input offset voltage**, $0.2\ \mu\text{V}/^\circ\text{C}$ drift), and an $8.0\text{ MHz}$ gain bandwidth product.

Unlike high-speed uncompensated amplifiers that require minimum gains of 5 (such as the OP37), the OP27 is internally frequency-compensated for **unity-gain stability** ($A_V = 1$). It is a benchmark component in high-end audio preamplifiers, precision strain gauge / bridge amplifiers, thermocouple sensors, low-frequency medical instrumentation (EEG/ECG front ends), and high-resolution 16-bit to 24-bit ADC driver buffers.

## Quick reference

| | |
|---|---|
| **Op-Amp Channels** | 1 (Single Precision Op-Amp) |
| **Package** | 8-pin DIP / SOIC-8 |
| **Supply Voltage Range** | $\pm 4.0\text{ V}$ to $\pm 18.0\text{ V}$ (Dual) / $+8.0\text{ V}$ to $+36.0\text{ V}$ (Single) |
| **Input Voltage Noise ($e_n$)** | $3.0\text{ nV}/\sqrt{\text{Hz}}$ typ ($3.8\text{ nV}/\sqrt{\text{Hz}}$ max) at $1\text{ kHz}$ |
| **Low-Frequency Noise ($0.1\text{Hz} \dots 10\text{Hz}$)**| $80\text{ nV}_{p-p}$ typical |
| **Input Offset Voltage ($V_{OS}$)** | $10\ \mu\text{V}$ typ ($25\ \mu\text{V}$ max for E grade) |
| **Gain Bandwidth Product (GBW)** | $8.0\text{ MHz}$ |
| **Slew Rate ($SR$)** | $2.8\text{ V}/\mu\text{s}$ |
| **Stability** | Unity Gain Stable ($A_V \ge +1$) |

## Pinout (DIP-8 / SOIC-8 Package)

```
             ┌───┴───┐
     VO-TRIM 1│ 1   8 │ VO-TRIM
         -IN 2│       │ 7 V+
         +IN 3│  OP27 │ 6 OUT
          V- 4│       │ 5 NC
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1, 8 | `VO-TRIM` | Analog Input | Offset voltage nulling pins (Connect across $10\text{ k}\Omega$ trim pot wiper to $V+$ if trimming) |
| 2 | `-IN` | Analog Input | Inverting signal input |
| 3 | `+IN` | Analog Input | Non-inverting signal input |
| 4 | `V-` | Power | Negative power supply rail (e.g. $-15\text{ V}$ or $0\text{ V}$) |
| 5 | `NC` | No Connect | No internal connection |
| 6 | `OUT` | Analog Output | Op-amp output |
| 7 | `V+` | Power | Positive power supply rail (e.g. $+15\text{ V}$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Offset Voltage | $V_{OS}$ | — | 10 | 25 | µV | $T_A = 25^\circ\text{C}, V_S = \pm 15\text{V}$ (E Grade) |
| Offset Voltage Temp Drift | $TCV_{OS}$| — | 0.2 | 0.6 | µV/°C | $-40^\circ\text{C} \le T_A \le +85^\circ\text{C}$ |
| Input Bias Current | $I_B$ | — | $\pm 10$ | $\pm 40$ | nA | $V_{CM} = 0\text{V}$ |
| Input Offset Current | $I_{OS}$ | — | 7 | 35 | nA | $V_{CM} = 0\text{V}$ |
| Input Noise Voltage Density | $e_n$ | — | 3.0 | 3.8 | nV/√Hz| $f = 1\text{ kHz}$ |
| Gain Bandwidth Product | $GBW$ | — | 8.0 | — | MHz | $f = 100\text{ kHz}, A_{VO} \ge 10^6$ |
| Slew Rate | $SR$ | 1.7 | 2.8 | — | V/µs | $R_L \ge 2\text{ k}\Omega, C_L = 15\text{ pF}$ |
| Common-Mode Rejection | $CMRR$ | 114 | 126 | — | dB | $V_{CM} = \pm 11\text{V}$ |
| Power Supply Rejection | $PSRR$ | 110 | 120 | — | dB | $V_S = \pm 4.5\text{V} \dots \pm 18\text{V}$ |
| Quiescent Supply Current | $I_S$ | — | 3.0 | 4.0 | mA | $V_O = 0\text{V}$ |

## Typical circuits

### Precision Ultra-Low-Noise AC Preamplifier

```
                 +15V
                  │
                [Pin 7: V+]
  Signal In ───[ C1: 10µF ]───► [Pin 3: +IN]
                                   OP27
                                [Pin 6: OUT] ────┬────[ C2: 10µF ]───► Amplified Out
                                [Pin 4: V-]      │
                                  │            [ Rf: 9.9kΩ 0.1% ]
                                 -15V            │
                ┌────────────────────────────────┴───► [Pin 2: -IN]
                │
              [ Rg: 100Ω 0.1% ]
                │
              [ Cg: 47µF Bipolar ]
                │
               GND
```

*Voltage Gain: $A_V = 1 + \frac{R_f}{R_g} = 1 + \frac{9.9\text{ k}\Omega}{100\ \Omega} = 100\times\ (+40\text{ dB})$.*

## Common mistakes

- **Using high resistor values with bipolar inputs:** Because the OP27 is a bipolar input op-amp, its input noise current is $0.4\text{ pA}/\sqrt{\text{Hz}}$. Using feedback resistors $> 10\text{ k}\Omega$ will cause the resistor thermal Johnson noise and input current noise to dominate over the op-amp's ultra-quiet $3\text{ nV}/\sqrt{\text{Hz}}$ voltage noise. Keep source/feedback resistances below $2\text{ k}\Omega$.
- **Confusing OP27 with OP37:** OP27 is unity-gain compensated ($A_V \ge 1$ stable); OP37 is decompensated for higher speed ($63\text{ MHz}$ GBW, $17\text{ V}/\mu\text{s}$ slew rate) but is **unstable at gains below 5**.
- **Missing supply decoupling:** Low-noise precision op-amps require clean local power. Place $0.1\ \mu\text{F}$ ceramic and $10\ \mu\text{F}$ tantalum bypass capacitors directly between Pin 7 ($V+$) / Pin 4 ($V-$) and Ground.

## Notes

- **Pin-Compatible Modern Equivalents:** OPA227 (Texas Instruments / Burr-Brown), LT1007 (Linear Technology), AD797 (Ultra-low 0.9nV noise).
