## Overview

The **INA128** (INA128P / INA128U) is a low-power, general-purpose precision instrumentation amplifier designed by Burr-Brown (now Texas Instruments). Built upon the classic 3-op-amp instrumentation topology with internal laser-trimmed thin-film resistors, it allows designers to configure precise gains from **$1$ to $10,000$** using **a single external resistor ($R_G$)**.

Operating from power supplies spanning **$\pm 2.25\text{V}$ to $\pm 18.0\text{V}$**, the INA128 consumes only **$700\ \mu\text{A}$ quiescent current** while delivering an exceptional **$120\text{ dB}$ minimum CMRR** ($G = 100$). A critical differentiator of the INA128 is its rugged **$\pm 40\text{V}$ input overvoltage protection**, allowing the device to withstand harsh industrial signal lines, sensor fault conditions, and accidental power rail cross-wiring without external clamping diodes.

## Quick reference

| | |
|---|---|
| **Amplifier Type** | Precision 3-Op-Amp Monolithic Instrumentation Amplifier |
| **Package** | 8-pin PDIP (INA128P) / 8-pin SOIC (INA128U) |
| **Gain Range** | $G = 1$ to $10,000$ (Set by single resistor $R_G$) |
| **Gain Formula** | $G = 1 + 50\text{ k}\Omega / R_G \iff R_G = 50\text{ k}\Omega / (G - 1)$ |
| **Supply Voltage Range** | $\pm 2.25\text{ V}$ to $\pm 18.0\text{ V}$ split (or $+4.5\text{V}$ to $+36\text{V}$ single) |
| **Common-Mode Rejection Ratio ($CMRR$)** | $120\text{ dB}$ min ($G = 100$) / $125\text{ dB}$ typ |
| **Input Protection** | $\pm 40\text{ V}$ continuous overvoltage without damage |
| **Input Offset Voltage ($V_{OS}$)** | $50\ \mu\text{V}$ max ($0.5\ \mu\text{V/}^\circ\text{C}$ drift) |
| **Bandwidth ($-3\text{dB}$)** | $200\text{ kHz}$ ($G = 100$) / $1.3\text{ MHz}$ ($G = 1$) |
| **Quiescent Current** | $700\ \mu\text{A}$ typical ($750\ \mu\text{A}$ maximum) |

## Pinout (DIP-8 / SOIC-8 Package)

```
        ┌──────────────┐
    RG  ─│ 1          8 │─ RG
   -IN  ─│ 2   INA    7 │─ V+
   +IN  ─│ 3   128    6 │─ Vo (Output)
    V-  ─│ 4          5 │─ Ref
        └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1, 8 | `RG` | Gain setting resistor terminals (Connect single resistor $R_G$) |
| 2 | `-IN` | Inverting differential analog signal input (Protected to $\pm 40\text{V}$) |
| 3 | `+IN` | Non-inverting differential analog signal input (Protected to $\pm 40\text{V}$) |
| 4 | `V-` | Negative power supply rail ($-2.25\text{V}$ to $-18.0\text{V}$ or GND) |
| 5 | `Ref` | Output reference voltage pin (Sets output offset reference) |
| 6 | `Vo` | Single-ended amplified analog output voltage |
| 7 | `V+` | Positive power supply rail ($+2.25\text{V}$ to $+18.0\text{V}$) |

## Gain Selection & Resistor Values

The gain equation is governed by two internal $25\text{ k}\Omega$ precision resistors:

$$ G = 1 + \frac{50\text{ k}\Omega}{R_G} \iff R_G = \frac{50\text{ k}\Omega}{G - 1} $$

| Desired Gain ($G$) | Exact Calculated $R_G$ | Nearest 1% Standard Resistor | Nearest 0.1% Standard Resistor |
|---|---|---|---|
| **1** | $\infty$ (Open circuit) | None (Pins 1 & 8 left open) | None |
| **10** | $5.555\text{ k}\Omega$ | $5.62\text{ k}\Omega$ | $5.56\text{ k}\Omega$ |
| **50** | $1.020\text{ k}\Omega$ | $1.02\text{ k}\Omega$ | $1.02\text{ k}\Omega$ |
| **100** | $505.05\ \Omega$ | $511\ \Omega$ | $505\ \Omega$ |
| **500** | $100.20\ \Omega$ | $100\ \Omega$ | $100\ \Omega$ |
| **1000** | $50.05\ \Omega$ | $49.9\ \Omega$ | $50.0\ \Omega$ |

## Standard Bridge Circuit

```
             +V_EXC Bridge Excitation (+5.0V)
                   │
             ┌─────┴─────┐
             │           │
           [ R1 ]      [ R2 ]
             │           │
             ├───────────┼──────────[Pin 2: -IN]
             │           │           INA128
      [ Bridge Sensor ] [ R3 ]       │
             │           │           [Pin 1: RG] ────[ R_G ]──── [Pin 8: RG]
             ├───────────┴──────────[Pin 3: +IN]
             │                       │
            GND                     [Pin 5: Ref] ──────────── GND (or 2.5V Offset)
                                     │
                                    [Pin 6: Vo] ───────────── Analog Out to ADC
```

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Gain Non-Linearity | $NL$ | — | 0.001 | 0.005 | % | $G = 1 \dots 100, R_L = 10\text{ k}\Omega$ |
| Input Offset Voltage | $V_{OSI}$ | — | 25 | 50 | $\mu\text{V}$ | $G = 1000, T_A = 25^\circ\text{C}$ |
| Input Bias Current | $I_B$ | — | 2.0 | 5.0 | nA | $T_A = 25^\circ\text{C}$ |
| Common-Mode Rejection Ratio | $CMRR$ | 120 | 125 | — | dB | $G = 100, V_{CM} = \pm 10\text{V}$ |
| Slew Rate | $SR$ | — | 4.0 | — | $\text{V/}\mu\text{s}$ | $G = 1 \dots 100$ |
| Output Voltage Swing (Positive) | $V_{OH}$ | $+V - 1.4$ | $+V - 0.9$ | — | V | $R_L = 10\text{ k}\Omega$ |
| Output Voltage Swing (Negative) | $V_{OL}$ | — | $-V + 0.8$ | $-V + 1.2$ | V | $R_L = 10\text{ k}\Omega$ |
| Input Overvoltage Limit | $V_{IN(MAX)}$| — | — | $\pm 40$ | V | Continuous differential/common-mode |

## Common mistakes

- **Comparing gain formulas with AD620:** The AD620 uses $49.4\text{ k}\Omega$, whereas the INA128 uses $50.0\text{ k}\Omega$. Using AD620 resistor values in an INA128 circuit produces a $\approx 1.2\%$ gain error.
- **Driving single supply with inputs near ground:** On a single $+5\text{V}$ supply, the input common-mode voltage range is limited to $+1.9\text{V} \dots +3.4\text{V}$. Connecting a ground-referenced thermocouple will clip the input buffer stages. Use **INA333** for rail-to-rail single-supply operation.
- **Unbuffered reference voltage on Pin 5:** The `Ref` pin must be driven with a source impedance $< 10\ \Omega$. A high-impedance resistor divider directly connected to `Ref` degrades the common-mode rejection ratio. Always buffer with an op-amp.

## Notes

- **Sibling Part (INA129):** The **INA129** is the $49.4\text{ k}\Omega$ gain-equation companion to the INA128, designed for exact resistor interchangeability with the AD620.
