## Overview

The **LM7815** (and TO-220 packaged **L7815CV** / **LM7815CT**) is a 3-terminal fixed positive linear voltage regulator IC manufactured by STMicroelectronics, Texas Instruments, and ON Semiconductor. It delivers a stable, low-noise **$+15.0\text{V}$ DC power supply rail** from unregulated DC input voltages ranging from **$17.5\text{V}$ to $35.0\text{V}$**.

Commonly paired with its negative counterpart, the **LM7915** ($-15\text{V}$), the LM7815 forms the classic $\pm 15\text{V}$ split power supply rail essential for high-fidelity audio preamplifiers, analog synthesizer modules, instrumentation op-amps, and active filters. It features internal thermal overload protection, short-circuit current limiting, and output transistor safe operating area (SOA) protection.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Fixed Positive Linear Voltage Regulator |
| **Package** | TO-220 (L7815CV) / TO-263 / DPAK |
| **Pinout (TO-220 Front)** | Pin 1: Input (`IN`), Pin 2: Ground (`GND`), Pin 3: Output (`OUT`) |
| **Fixed Output Voltage** | $+15.0\text{ V}$ DC ($\pm 4\%$ tolerance across temperature) |
| **Input Voltage Range ($V_{IN}$)** | $17.5\text{ V}$ min to $35.0\text{ V}$ max |
| **Dropout Voltage** | $2.0\text{ V}$ typ (Requires $V_{IN} \ge 17.5\text{V}$ for full regulation) |
| **Continuous Output Current ($I_{OUT}$)** | $> 1.5\text{ A}$ (with adequate heatsink) |
| **Ripple Rejection Ratio** | $54\text{ dB} \dots 70\text{ dB}$ at $f = 120\text{ Hz}$ |

## Pinout (TO-220 Package)

Looking at the **front labeled face** of the TO-220 package with metal tab at top and leads pointing down:

```
        ┌──────────────┐
        │ [LM7815 Tab] │  (Metal Tab connected internally to Pin 2 GND)
        ├──────────────┤
        │    LM7815    │  (Front Face)
        └─┬────┬────┬──┘
          1    2    3
         IN   GND  OUT
```

| Pin | Name | Description |
|---|---|---|
| 1 | `IN` | Unregulated DC input voltage pin (+17.5V to +35.0V DC) |
| 2 | `GND` / `TAB` | Ground reference (0 V, connected internally to heatsink tab) |
| 3 | `OUT` | Fixed regulated +15.0V DC output pin |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Regulated Output Voltage | $V_{OUT}$ | 14.4 | 15.0 | 15.6 | V | $17.5\text{V} \le V_{IN} \le 30\text{V}, 5\text{mA} \le I_O \le 1.0\text{A}$ |
| Dropout Voltage | $V_d$ | — | 2.0 | 2.5 | V | $I_{OUT} = 1.0\text{A}, T_J = 25^\circ\text{C}$ |
| Peak Output Current | $I_{OS}$ | 1.5 | 2.2 | — | A | Short circuit peak current |
| Quiescent Current | $I_d$ | — | 4.4 | 8.0 | mA | $T_J = 25^\circ\text{C}$ |
| Quiescent Current Change | $\Delta I_d$ | — | — | 0.5 | mA | $5\text{mA} \le I_{OUT} \le 1.0\text{A}$ |
| Output Noise Voltage | $V_N$ | — | 90 | — | µV | $10\text{ Hz} \le f \le 100\text{ kHz}$ |

## Standard Circuit & Capacitors

```
       +V_IN Unregulated Input (17.5V - 35V DC)
          │
       [Pin 1: IN]
        LM7815
       [Pin 3: OUT] ──────────────┬─────────────── +15.0V Regulated DC Output
          │                       │
       [Pin 2: GND]          [ C2 = 0.1µF Ceramic ]
          │                       │
   [ C1 = 0.33µF Ceramic ]       GND
          │
         GND
```

- **Input Capacitor ($C_1 = 0.33\ \mu\text{F}$):** Essential when the regulator is located more than a few inches from the bridge rectifier / bulk filter capacitor to prevent inductive oscillations.
- **Output Capacitor ($C_2 = 0.1\ \mu\text{F}$):** Ceramic or tantalum capacitor to improve transient response and ensure high-frequency stability.

## Common mistakes

- **Insufficient input headroom:** Supplying less than $17.5\text{V}$ input causes the regulator to drop out of regulation. Under heavy load ($1\text{A}$), input ripple valleys must not drop below $17.5\text{V}$.
- **Excessive thermal dissipation:** In a 24V-to-15V step-down at 1A, the power dissipated is $(24\text{V} - 15\text{V}) \times 1\text{A} = 9\text{ Watts}$. A TO-220 package without a heatsink will thermal throttle within seconds.
- **Confusing LM7815 and LM7915 pinouts:** The negative voltage complementary part (LM7915) has a completely different pinout (Pin 1: `GND`, Pin 2: `IN`, Pin 3: `OUT`, Tab: `IN`). Never assume 78xx and 79xx share the same pin assignments.

## Notes

- **Split Supply Pair:** Often deployed alongside the **LM7915** ($-15\text{V}$) to provide balanced $\pm 15\text{V}$ rails for operational amplifiers (such as TL072, NE5532, and OPA2134).
