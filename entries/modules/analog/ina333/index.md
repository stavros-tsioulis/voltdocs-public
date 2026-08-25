## Overview

The **INA333** (INA333AIDGKT / INA333AIDR) is an ultra-low-power, zero-drift precision instrumentation amplifier engineered by Texas Instruments. Designed for battery-operated medical devices, wearable biosignal monitors, and portable 3.3V/5V microcontroller systems, it draws an astonishingly low **$50\ \mu\text{A}$ quiescent current** while operating down to a single supply voltage of **$1.8\text{ V}$**.

Utilizing a 3-op-amp architecture with patented internal auto-zeroing topology, the INA333 delivers true **rail-to-rail output voltage swing** (within $50\text{ mV}$ of the power rails), an ultra-low input offset voltage of **$25\ \mu\text{V}$ maximum** with practically zero drift ($0.1\ \mu\text{V/}^\circ\text{C}$), and high common-mode rejection of **$100\text{ dB}$ ($G \ge 10$)**. A single external resistor ($R_G$) programs precise voltage gains from **$1$ to $1000$**.

## Quick reference

| | |
|---|---|
| **Amplifier Type** | MicroPower Zero-Drift Rail-to-Rail Instrumentation Amplifier |
| **Package** | 8-pin VSSOP (MSOP-8) / 8-pin SOIC / 8-pin WSON (3mm × 3mm) |
| **Gain Range** | $G = 1$ to $1000$ (Set by single resistor $R_G$) |
| **Gain Formula** | $G = 1 + 100\text{ k}\Omega / R_G \iff R_G = 100\text{ k}\Omega / (G - 1)$ |
| **Supply Voltage Range** | $+1.8\text{ V}$ to $+5.5\text{ V}$ single supply (or $\pm 0.9\text{V}$ to $\pm 2.75\text{V}$ split) |
| **Quiescent Current** | $50\ \mu\text{A}$ typical ($75\ \mu\text{A}$ maximum) |
| **Input Offset Voltage ($V_{OS}$)** | $25\ \mu\text{V}$ max ($0.1\ \mu\text{V/}^\circ\text{C}$ drift) |
| **Input Bias Current ($I_B$)** | $70\text{ pA}$ typical / $200\text{ pA}$ maximum |
| **Output Architecture** | Rail-to-Rail Output ($V_{OL} \le 50\text{ mV}, V_{OH} \ge V_+ - 50\text{ mV}$) |
| **Common-Mode Rejection ($CMRR$)** | $100\text{ dB}$ min ($G \ge 10$) / $115\text{ dB}$ typ |

## Pinout (VSSOP-8 / SOIC-8 Package)

```
        ┌──────────────┐
    RG  ─│ 1          8 │─ RG
  VIN-  ─│ 2   INA    7 │─ V+
  VIN+  ─│ 3   333    6 │─ VOUT
    V-  ─│ 4          5 │─ REF
        └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1, 8 | `RG` | Gain setting resistor terminals (Connect single resistor $R_G$) |
| 2 | `VIN-` | Inverting differential analog signal input |
| 3 | `VIN+` | Non-inverting differential analog signal input |
| 4 | `V-` | Negative supply terminal (Connect to GND for single-supply operation) |
| 5 | `REF` | Output reference voltage pin (Connect to $V_{DD}/2$ for single-supply bipolar signals) |
| 6 | `VOUT` | Rail-to-rail single-ended amplified output voltage |
| 7 | `V+` | Positive power supply rail (+1.8V to +5.5V DC) |

## Gain Selection & Resistor Values

The gain is set by two internal $50\text{ k}\Omega$ feedback resistors:

$$ G = 1 + \frac{100\text{ k}\Omega}{R_G} \iff R_G = \frac{100\text{ k}\Omega}{G - 1} $$

| Desired Gain ($G$) | Exact Calculated $R_G$ | Nearest 1% Standard Resistor | Nearest 0.1% Standard Resistor |
|---|---|---|---|
| **1** | $\infty$ (Open circuit) | None (Pins 1 & 8 left open) | None |
| **10** | $11.111\text{ k}\Omega$ | $11.3\text{ k}\Omega$ | $11.1\text{ k}\Omega$ |
| **50** | $2.041\text{ k}\Omega$ | $2.05\text{ k}\Omega$ | $2.05\text{ k}\Omega$ |
| **100** | $1.010\text{ k}\Omega$ | $1.02\text{ k}\Omega$ | $1.01\text{ k}\Omega$ |
| **500** | $200.40\ \Omega$ | $200\ \Omega$ | $200\ \Omega$ |
| **1000** | $100.10\ \Omega$ | $100\ \Omega$ | $100\ \Omega$ |

## Single-Supply ECG / Biosignal Circuit (3.3V)

```
        +3.3V Single Supply
           │
     ┌─────┴──────────────────────┐
     │                            │
   [ V+ Pin 7 ]              [ 1.65V Mid-Supply Ref Buffer ]
     INA333                       │
   [Pin 5: REF] ──────────────────┘
   [Pin 2: VIN-] ──[ 10k ]──[ Lead RA (Right Arm) ]
   [Pin 3: VIN+] ──[ 10k ]──[ Lead LA (Left Arm) ]
   [Pin 1: RG ] ────[ R_G = 1.02kΩ (Gain=100) ]──── [Pin 8: RG]
   [Pin 6: VOUT] ───────────────────────────────── Analog Output to MCU ADC (0V - 3.3V)
   [Pin 4: V-  ]
           │
          GND
```

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Offset Voltage | $V_{OS}$ | — | 10 | 25 | $\mu\text{V}$ | $G = 100, T_A = 25^\circ\text{C}$ |
| Input Offset Voltage Drift | $dV_{OS}/dT$ | — | 0.05 | 0.1 | $\mu\text{V/}^\circ\text{C}$ | $-40^\circ\text{C} \le T_A \le 125^\circ\text{C}$ |
| Input Bias Current | $I_B$ | — | 70 | 200 | pA | $T_A = 25^\circ\text{C}$ |
| Common-Mode Rejection Ratio | $CMRR$ | 100 | 115 | — | dB | $G \ge 10, V_{CM} = 0.1\text{V} \dots V_+ - 0.1\text{V}$ |
| Bandwidth ($-3\text{dB}$)| $BW$ | — | 35 | — | kHz | $G = 10$ |
| Slew Rate | $SR$ | — | 0.16 | — | $\text{V/}\mu\text{s}$ | $G = 1 \dots 100$ |
| Output Low Swing | $V_{OL}$ | — | 20 | 50 | mV | $R_L = 10\text{ k}\Omega$ to $V_+/2$ |
| Output High Swing | $V_{OH}$ | $V_+ - 50\text{mV}$ | $V_+ - 20\text{mV}$ | — | V | $R_L = 10\text{ k}\Omega$ to $V_+/2$ |
| Quiescent Current | $I_Q$ | — | 50 | 75 | $\mu\text{A}$ | $T_A = 25^\circ\text{C}$ |

## Common mistakes

- **Exceeding input common-mode range ($V_{CM}$) on single supply:** The input common-mode voltage range extends from $(V-) + 0.1\text{V}$ to $(V+) - 0.1\text{V}$. Operating inputs below ground or within $100\text{mV}$ of the supply rail will introduce non-linearities.
- **Using high-impedance divider for REF pin:** Pin 5 (`REF`) sets the baseline output level. Driving `REF` from an unbuffered resistor divider impairs internal resistor matching, severely reducing common-mode rejection. Always use an active op-amp buffer (like OPA333 or TLV9001) to drive `REF`.
- **Forgetting that the gain formula uses 100kΩ:** Unlike the AD620 ($49.4\text{ k}\Omega$) and INA128 ($50\text{ k}\Omega$), the INA333 uses $100\text{ k}\Omega$ ($2 \times 50\text{ k}\Omega$). Using an AD620 gain resistor will result in roughly half the intended gain.

## Notes

- **Zero-Drift Architecture:** The internal auto-zeroing topology continuously removes $1/f$ low-frequency flicker noise, making the INA333 exceptionally accurate for sub-Hz biomedical and strain measurements.
