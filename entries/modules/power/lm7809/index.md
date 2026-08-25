## Overview

The **LM7809** (and TO-220 packaged **L7809CV** / **LM7809CT**) is a 3-terminal fixed positive linear voltage regulator IC manufactured by STMicroelectronics, Texas Instruments, and ON Semiconductor. It delivers a stable, ultra-low-noise **$+9.0\text{V}$ DC power supply rail** from unregulated DC input voltages ranging from **$11.5\text{V}$ to $35.0\text{V}$**.

The 9V output voltage makes the LM7809 an industry favorite for powering guitar effects pedals, battery-operated audio equipment (replacing 9V PP3 / 6F22 batteries with mains adapters), analog synthesizer modules, operational amplifier circuits, and wireless microphones. It provides built-in thermal overload protection, short-circuit current limiting, and safe operating area (SOA) protection.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Fixed Positive Linear Voltage Regulator |
| **Package** | TO-220 (L7809CV) / TO-263 / DPAK |
| **Pinout (TO-220 Front)** | Pin 1: Input (`IN`), Pin 2: Ground (`GND`), Pin 3: Output (`OUT`) |
| **Fixed Output Voltage** | $+9.0\text{ V}$ DC ($\pm 4\%$ tolerance across temperature) |
| **Input Voltage Range ($V_{IN}$)** | $11.5\text{ V}$ min to $35.0\text{ V}$ max |
| **Dropout Voltage** | $2.0\text{ V}$ typ (Requires $V_{IN} \ge 11.5\text{V}$ for full regulation) |
| **Continuous Output Current ($I_{OUT}$)** | $> 1.5\text{ A}$ (with adequate heatsink) |
| **Ripple Rejection Ratio** | $56\text{ dB} \dots 72\text{ dB}$ at $f = 120\text{ Hz}$ |

## Pinout (TO-220 Package)

Looking at the **front labeled face** of the TO-220 package with metal tab at top and leads pointing down:

```
        ┌──────────────┐
        │ [LM7809 Tab] │  (Metal Tab connected internally to Pin 2 GND)
        ├──────────────┤
        │    LM7809    │  (Front Face)
        └─┬────┬────┬──┘
          1    2    3
         IN   GND  OUT
```

| Pin | Name | Description |
|---|---|---|
| 1 | `IN` | Unregulated DC input voltage pin (+11.5V to +35.0V DC) |
| 2 | `GND` / `TAB` | Ground reference (0 V, connected internally to heatsink tab) |
| 3 | `OUT` | Fixed regulated +9.0V DC output pin |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Regulated Output Voltage | $V_{OUT}$ | 8.65 | 9.0 | 9.35 | V | $11.5\text{V} \le V_{IN} \le 24\text{V}, 5\text{mA} \le I_O \le 1.0\text{A}$ |
| Dropout Voltage | $V_d$ | — | 2.0 | 2.5 | V | $I_{OUT} = 1.0\text{A}, T_J = 25^\circ\text{C}$ |
| Peak Output Current | $I_{OS}$ | 1.5 | 2.2 | — | A | Short circuit peak current |
| Quiescent Current | $I_d$ | — | 4.3 | 8.0 | mA | $T_J = 25^\circ\text{C}$ |
| Quiescent Current Change | $\Delta I_d$ | — | — | 0.5 | mA | $5\text{mA} \le I_{OUT} \le 1.0\text{A}$ |
| Output Noise Voltage | $V_N$ | — | 58 | — | µV | $10\text{ Hz} \le f \le 100\text{ kHz}$ |

## Standard Circuit & Capacitors

```
       +V_IN Unregulated Input (11.5V - 35V DC)
          │
       [Pin 1: IN]
        LM7809
       [Pin 3: OUT] ──────────────┬─────────────── +9.0V Regulated DC Output
          │                       │
       [Pin 2: GND]          [ C2 = 0.1µF Ceramic ]
          │                       │
   [ C1 = 0.33µF Ceramic ]       GND
          │
         GND
```

- **Input Capacitor ($C_1 = 0.33\ \mu\text{F}$):** Suppresses line impedance instabilities and input voltage oscillation.
- **Output Capacitor ($C_2 = 0.1\ \mu\text{F}$):** Essential for high-frequency stability, load transient absorption, and ripple suppression in audio signal chains.

## Common mistakes

- **Supplying a 12V adapter with high ripple:** While $12\text{V}$ DC nominally exceeds $11.5\text{V}$, an unregulated 12V wall adapter under heavy load can experience ripple dips below $11.0\text{V}$, leading to audible 100Hz/120Hz hum in audio gear. Use at least $12.5\text{V} \dots 15\text{V}$ input for robust 9V regulation.
- **Guitar pedal center-negative barrel polarity errors:** Most 9V guitar effects pedals expect a center-negative $2.1\text{mm}$ barrel jack, whereas conventional DC power supplies are center-positive. Always double-check polarity wiring when building pedal power supplies.
- **Operating without heatsink at high input voltages:** Stepping down $24\text{V}$ to $9\text{V}$ at $500\text{mA}$ dissipates $(24\text{V} - 9\text{V}) \times 0.5\text{A} = 7.5\text{W}$, which will quickly cause thermal shutdown without a dedicated aluminum heatsink.

## Notes

- **Negative Complement:** The **LM7909** provides a matching $-9.0\text{V}$ output rail for symmetric $\pm 9\text{V}$ analog and audio instrumentation systems.
