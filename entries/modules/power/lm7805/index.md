## Overview

The **LM7805** (and TO-220 packaged **L7805CV** / **LM7805CT**) is the single most recognizable fixed linear voltage regulator IC in electronics history. Designed by Fairchild Semiconductor and produced by STMicroelectronics, Texas Instruments, and ON Semiconductor, it provides a stable, low-noise **$+5.0\text{V}$ DC power supply rail** from unregulated DC input voltages ranging from **$7.0\text{V}$ to $35.0\text{V}$**.

Capable of delivering continuous output currents of **$> 1.5\text{ Amperes}$** (with adequate heatsinking), the LM7805 includes internal thermal overload protection, short-circuit current limiting, and output transistor safe-area protection.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Fixed Positive Linear Voltage Regulator |
| **Package** | TO-220 (L7805CV) / TO-263 / DPAK |
| **Pinout (TO-220 Front)** | Pin 1: Input (`IN`), Pin 2: Ground (`GND`), Pin 3: Output (`OUT`) |
| **Fixed Output Voltage** | $+5.0\text{ V}$ DC ($\pm 4\%$ tolerance across temperature) |
| **Input Voltage Range ($V_{IN}$)**| $7.0\text{ V}$ min to $35.0\text{ V}$ max |
| **Dropout Voltage** | $2.0\text{ V}$ (Requires $V_{IN} \ge 7.0\text{V}$ for 5V output) |
| **Continuous Output Current ($I_{OUT}$)**| $> 1.5\text{ A}$ (with heatsink) |
| **Ripple Rejection Ratio** | $62\text{ dB} \dots 78\text{ dB}$ at $f = 120\text{ Hz}$ |

## Pinout (TO-220 Package)

Looking at the **front labeled face** of the TO-220 package with metal tab at top and leads pointing down:

```
        ┌──────────────┐
        │ [LM7805 Tab] │  (Metal Tab connected internally to Pin 2 GND)
        ├──────────────┤
        │    LM7805    │  (Front Face)
        └─┬────┬────┬──┘
          1    2    3
         IN   GND  OUT
```

| Pin | Name | Description |
|---|---|---|
| 1 | `IN` | Unregulated DC input voltage pin (+7.0V to +35V DC) |
| 2 | `GND` / `TAB` | Ground reference (0 V, connected to heatsink tab) |
| 3 | `OUT` | Fixed regulated +5.0V DC output pin |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Regulated Output Voltage| $V_{OUT}$ | 4.8 | 5.0 | 5.2 | V | $7.0\text{V} \le V_{IN} \le 20\text{V}, 5\text{mA} \le I_O \le 1.0\text{A}$ |
| Dropout Voltage | $V_d$ | — | 2.0 | 2.5 | V | $I_{OUT} = 1.0\text{A}, T_J = 25^\circ\text{C}$ |
| Peak Output Current | $I_{OS}$ | 1.5 | 2.2 | — | A | Short circuit peak current |
| Quiescent Current | $I_d$ | — | 4.2 | 8.0 | mA | $T_J = 25^\circ\text{C}$ |
| Quiescent Current Change| $\Delta I_d$ | — | — | 0.5 | mA | $5\text{mA} \le I_{OUT} \le 1.0\text{A}$ |
| Output Noise Voltage | $V_N$ | — | 40 | — | µV | $10\text{ Hz} \le f \le 100\text{ kHz}$ |

## Standard Circuit & Capacitors

```
       +V_IN Unregulated Input (7.0V - 35V DC)
          │
       [Pin 1: IN]
        LM7805
       [Pin 3: OUT] ──────────────┬─────────────── +5.0V Regulated DC Output
          │                       │
       [Pin 2: GND]          [ C2 = 0.1µF Ceramic ]
          │                       │
   [ C1 = 0.33µF Ceramic ]       GND
          │
         GND
```

- **Input Capacitor ($C_1 = 0.33\ \mu\text{F}$):** Required if the regulator is located more than 2 inches from the main power supply filter capacitors.
- **Output Capacitor ($C_2 = 0.1\ \mu\text{F}$):** Improves transient response and prevents high-frequency self-oscillation.

## Common mistakes

- **Supplying less than 7.0V input voltage:** The LM7805 has a $2.0\text{V}$ dropout voltage. Supplying only $5.5\text{V}$ or $6.0\text{V}$ $V_{IN}$ causes output voltage regulation to drop out below $5.0\text{V}$.
- **Overheating without a heatsink:** Dropping 12V to 5V at 1A creates $P_D = (12\text{V} - 5\text{V}) \times 1\text{A} = 7\text{ Watts}$ of heat. The TO-220 package will reach thermal shutdown ($\sim 150^\circ\text{C}$) in seconds without an external aluminum heatsink.

## Notes

- **LM78xx Series Family:** LM7805 (5V), LM7808 (8V), LM7809 (9V), LM7812 (12V), LM7815 (15V), LM7824 (24V). Negative voltage equivalents belong to the LM79xx series (e.g. LM7905).
