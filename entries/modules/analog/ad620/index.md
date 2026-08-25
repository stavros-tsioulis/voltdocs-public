## Overview

The **AD620** (AD620AN / AD620AR) is the quintessential low-cost, high-accuracy monolithic instrumentation amplifier manufactured by Analog Devices. Replacing discrete three-op-amp instrumentation circuits with laser-trimmed monolithically matched internal resistors, it allows the user to program precise voltage gains from **$1$ to $10,000$** using just **a single external resistor ($R_G$)**.

Operating from dual power supplies ranging from **$\pm 2.3\text{V}$ to $\pm 18.0\text{V}$** (or single supplies from $+4.6\text{V}$ to $+36.0\text{V}$), the AD620 draws only **$1.3\text{ mA}$ maximum supply current** while achieving an exceptional common-mode rejection ratio of **$> 100\text{ dB}$ ($G = 10$)** and low input voltage noise of **$9\text{ nV}/\sqrt{\text{Hz}}$ at $1\text{ kHz}$**. It is universally employed in precision load-cell weight scales, strain gauge sensor interfaces, RTD temperature bridges, and medical bio-potential monitoring (ECG/EEG/EMG front-ends).

## Quick reference

| | |
|---|---|
| **Amplifier Type** | Monolithic 3-Op-Amp Precision Instrumentation Amplifier |
| **Package** | 8-pin PDIP (AD620ANZ) / 8-pin SOIC (AD620ARZ) |
| **Gain Range** | $G = 1$ to $10,000$ (Set by single resistor $R_G$) |
| **Gain Formula** | $R_G = 49.4\text{ k}\Omega / (G - 1)$ |
| **Supply Voltage Range** | $\pm 2.3\text{ V}$ to $\pm 18.0\text{ V}$ split (or $+4.6\text{V}$ to $+36\text{V}$ single) |
| **Common-Mode Rejection Ratio ($CMRR$)** | $100\text{ dB}$ min ($G = 10$) / $130\text{ dB}$ typ ($G = 100$) |
| **Input Offset Voltage ($V_{OS}$)** | $50\ \mu\text{V}$ max ($0.6\ \mu\text{V/}^\circ\text{C}$ drift) |
| **Input Bias Current ($I_B$)** | $1.0\text{ nA}$ maximum ($0.5\text{ nA}$ typical) |
| **Bandwidth ($-3\text{dB}$)** | $120\text{ kHz}$ ($G = 100$) / $1.0\text{ MHz}$ ($G = 1$) |
| **Quiescent Current** | $0.9\text{ mA}$ typical / $1.3\text{ mA}$ maximum |

## Pinout (DIP-8 / SOIC-8 Package)

```
        ┌──────────────┐
   -RG  ─│ 1          8 │─ +RG
   -IN  ─│ 2   AD     7 │─ +VS
   +IN  ─│ 3   620    6 │─ OUTPUT
   -VS  ─│ 4          5 │─ REF
        └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `-RG` | Gain setting resistor negative terminal |
| 2 | `-IN` | Inverting differential analog signal input |
| 3 | `+IN` | Non-inverting differential analog signal input |
| 4 | `-VS` | Negative power supply rail ($-2.3\text{V}$ to $-18.0\text{V}$ or GND) |
| 5 | `REF` | Output reference voltage pin (Connect to Ground or $V_{ADC}/2$ for level-shifting) |
| 6 | `OUTPUT` | Single-ended amplified analog output voltage |
| 7 | `+VS` | Positive power supply rail ($+2.3\text{V}$ to $+18.0\text{V}$) |
| 8 | `+RG` | Gain setting resistor positive terminal |

## Gain Selection & Resistor Values

The gain is programmed by selecting resistor $R_G$ placed between Pin 1 and Pin 8 according to the formula:

$$ G = 1 + \frac{49.4\text{ k}\Omega}{R_G} \iff R_G = \frac{49.4\text{ k}\Omega}{G - 1} $$

| Desired Gain ($G$) | Exact Calculated $R_G$ | Nearest 1% Standard Resistor | Nearest 0.1% Standard Resistor |
|---|---|---|---|
| **1** | $\infty$ (Open circuit) | None (Pins 1 & 8 left open) | None |
| **10** | $5.489\text{ k}\Omega$ | $5.49\text{ k}\Omega$ | $5.49\text{ k}\Omega$ |
| **50** | $1.008\text{ k}\Omega$ | $1.00\text{ k}\Omega$ | $1.01\text{ k}\Omega$ |
| **100** | $498.99\ \Omega$ | $499\ \Omega$ | $499\ \Omega$ |
| **500** | $98.99\ \Omega$ | $100\ \Omega$ | $98.8\ \Omega$ |
| **1000** | $49.45\ \Omega$ | $49.9\ \Omega$ | $49.3\ \Omega$ |

## Standard Wheatstone Bridge Interface Circuit

```
             +V_EXC Bridge Excitation (+5.0V)
                   │
             ┌─────┴─────┐
             │           │
           [ R1 ]      [ R2 ]
             │           │
             ├───────────┼──────────[Pin 2: -IN]
             │           │           AD620
      [ Strain Gauge ] [ R3 ]        │
             │           │           [Pin 1: -RG] ──[ R_G ]── [Pin 8: +RG]
             ├───────────┴──────────[Pin 3: +IN]
             │                       │
            GND                     [Pin 5: REF] ──────────── GND (or 2.5V Offset)
                                     │
                                    [Pin 6: OUTPUT] ───────── Analog Out to ADC
```

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Gain Non-Linearity | $NL$ | — | 10 | 40 | ppm | $G = 1 \dots 100, R_L = 10\text{ k}\Omega$ |
| Input Offset Voltage (Laser Trimmed) | $V_{OSI}$ | — | 30 | 50 | $\mu\text{V}$ | $G = 1000, T_A = 25^\circ\text{C}$ |
| Input Offset Current | $I_{OS}$ | — | 0.3 | 0.5 | nA | $T_A = 25^\circ\text{C}$ |
| Common-Mode Rejection Ratio | $CMRR$ | 93 | 100 | — | dB | $G = 10, V_{CM} = \pm 10\text{V}$ |
| Common-Mode Rejection ($G = 100$) | $CMRR$ | 110 | 130 | — | dB | $G = 100, V_{CM} = \pm 10\text{V}$ |
| Slew Rate | $SR$ | — | 1.2 | — | $\text{V/}\mu\text{s}$ | $G = 1 \dots 100$ |
| Output Voltage Swing (Positive) | $V_{OH}$ | $+VS - 1.4$ | $+VS - 1.1$ | — | V | $R_L = 2\text{ k}\Omega$ |
| Output Voltage Swing (Negative) | $V_{OL}$ | — | $-VS + 1.2$ | $-VS + 1.5$ | V | $R_L = 2\text{ k}\Omega$ |

## Common mistakes

- **Leaving no DC return path for input bias currents:** Because the AD620 inputs are bipolar transistors, both `+IN` and `-IN` must have a DC resistive path to ground ($COM$). Connecting AC-coupled capacitors or a floating thermocouple directly to the inputs causes charge accumulation, driving the amplifier into saturation. Connect a $100\text{ k}\Omega \dots 1\text{ M}\Omega$ resistor from each input to ground.
- **Driving the output outside headroom limits on single supply:** The AD620 is not a rail-to-rail op-amp. On a single $+5\text{V}$ supply (with $-V_S = \text{GND}$), output voltage swing is limited to $+1.5\text{V} \dots +3.8\text{V}$. For true $0\text{V} \dots 5\text{V}$ single-supply operation, use the **INA333**.
- **Leaving the REF pin floating:** Pin 5 (`REF`) sets the zero-reference voltage for the output ($V_{OUT} = G \times (V_+ - V_-) + V_{REF}$). Leaving `REF` floating causes unpredictable output offsets. Tie `REF` to ground (dual supply) or to a low-impedance mid-supply reference ($2.5\text{V}$).

## Notes

- **Reference Pin Drive:** Always drive the `REF` pin with a low-impedance source (such as an op-amp buffer or ground plane). Adding series resistance to `REF` directly degrades the common-mode rejection ratio.
