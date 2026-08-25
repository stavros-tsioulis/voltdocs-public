## Overview

The **MIC5219-3.3** (MIC5219-3.3YM5) is a high-performance, ultra-low-noise fixed +3.3V low dropout (LDO) linear regulator manufactured by Microchip Technology (originally Micrel). Housed in a miniature 5-pin SOT-23 package, it delivers up to **$500\text{ mA}$ peak output current** ($250\text{ mA}$ continuous) with an exceptionally low dropout voltage of **$10\text{ mV}$ at light loads and $350\text{ mV}$ at $500\text{ mA}$**.

Featuring an internal reference bypass (`BYP`) pin, connecting a tiny $470\text{ pF}$ ceramic capacitor reduces output spectral noise density to just **$260\text{ nV}/\sqrt{\text{Hz}}$**. The IC incorporates zero-current shutdown mode ($< 1\ \mu\text{A}$), reverse battery polarity protection, overcurrent limiting, and thermal overload protection. It is a favored power regulator on Adafruit breakout boards, Arduino Pro Mini clones, GPS modules, LoRa nodes, and precision analog sensor front-ends.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Ultra-Low-Noise Low-Dropout Linear Regulator (LDO) |
| **Package** | 5-pin SOT-23 (SOT-23-5) / 8-pin MSOP |
| **Fixed Output Voltage** | $+3.3\text{ V}$ DC ($\pm 1\%$ initial accuracy) |
| **Input Voltage Range ($V_{IN}$)** | $2.5\text{ V}$ to $12.0\text{ V}$ DC (Operates up to $+20\text{V}$ absolute max) |
| **Peak Output Current** | $500\text{ mA}$ peak ($250\text{ mA}$ continuous thermal) |
| **Dropout Voltage** | $10\text{ mV}$ at $100\ \mu\text{A}$ / $350\text{ mV}$ at $500\text{ mA}$ |
| **Noise Spectral Density** | $260\text{ nV}/\sqrt{\text{Hz}}$ with $470\text{ pF}$ bypass cap |
| **Quiescent Current** | $80\ \mu\text{A}$ at light load / $< 0.1\ \mu\text{A}$ in shutdown |
| **Enable Control** | Logic-compatible active-HIGH `EN` pin |

## Pinout (SOT-23-5 Package)

```
        ┌─────────────┐
    IN ─│ 1         5 │─ OUT
   GND ─│ 2           │
    EN ─│ 3         4 │─ BYP (Noise Bypass)
        └─────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `IN` | Unregulated DC supply input (+2.5V to +12.0V DC) |
| 2 | `GND` | Ground reference (0 V) |
| 3 | `EN` | Enable / Shutdown control (HIGH = Enabled, LOW/Open = Shutdown) |
| 4 | `BYP` | Noise bypass pin (Connect 470pF ceramic cap to GND; leave floating if unused) |
| 5 | `OUT` | Regulated fixed +3.3V DC voltage output |

## Standard Circuit & Capacitors

```
       +V_IN (3.6V - 12V DC)
          │
       [Pin 1: IN]
        MIC5219-3.3
       [Pin 5: OUT] ──────────────┬─────────────── +3.3V Regulated DC Output
          │                       │
       [Pin 2: GND]          [ C_OUT = 2.2µF Ceramic/Tantalum ]
          │                       │
   [ C_IN = 1.0µF Ceramic ]      GND
          │
       [Pin 3: EN ] ─── +V_IN (or MCU GPIO)
       [Pin 4: BYP] ───[ C_BYP = 470pF ]─── GND
```

- **Input Capacitor ($C_{IN} = 1.0\ \mu\text{F}$):** Required if the regulator is more than 4 inches from the main power source.
- **Output Capacitor ($C_{OUT} = 2.2\ \mu\text{F} \dots 10\ \mu\text{F}$):** Ceramic or tantalum capacitor required for control loop stability (ESR $< 5\ \Omega$).
- **Bypass Capacitor ($C_{BYP} = 470\text{ pF}$):** Ceramic capacitor connected from Pin 4 to GND to suppress reference amplifier noise.

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Output Voltage Accuracy | $V_{OUT}$ | 3.267 | 3.300 | 3.333 | V | $I_O = 100\ \mu\text{A}, T_A = 25^\circ\text{C}$ |
| Dropout Voltage | $V_{DO}$ | — | 10 | 50 | mV | $I_{OUT} = 100\ \mu\text{A}$ |
| Dropout Voltage (Full Load) | $V_{DO}$ | — | 350 | 500 | mV | $I_{OUT} = 500\text{ mA}$ |
| Peak Output Current | $I_{PK}$ | 500 | 700 | — | mA | $V_{OUT} \ge 3.1\text{V}$ |
| Quiescent Ground Current | $I_{GND}$ | — | 80 | 150 | $\mu\text{A}$ | $I_{OUT} = 100\ \mu\text{A}$ |
| Ground Current at Full Load | $I_{GND}$ | — | 6.0 | 12.0 | mA | $I_{OUT} = 500\text{ mA}$ |
| Shutdown Current | $I_{SD}$ | — | 0.01 | 1.0 | $\mu\text{A}$ | $V_{EN} \le 0.4\text{V}$ |
| Power Supply Rejection Ratio | $PSRR$ | — | 75 | — | dB | $f = 120\text{ Hz}, C_{OUT} = 10\ \mu\text{F}$ |

## Common mistakes

- **Leaving EN floating:** Pin 3 (`EN`) does not have an internal pull-up. Leaving it disconnected causes the regulator to float into low-power shutdown. Tie `EN` directly to `IN` for always-on operation.
- **Overheating the tiny SOT-23 package at high continuous currents:** SOT-23 packages have a thermal resistance $\theta_{JA} \approx 220^\circ\text{C/W}$. Stepping down $9\text{V}$ (e.g. from a 9V battery) to $3.3\text{V}$ at $150\text{mA}$ creates $P_D = (9 - 3.3) \times 0.15 = 0.855\text{ W}$, resulting in a $\Delta T = 0.855 \times 220 \approx 188^\circ\text{C}$ temperature rise that instantly triggers thermal shutdown. Keep continuous loads $< 150\text{ mA}$ when input voltage exceeds $5\text{V}$.

## Notes

- **Reverse Battery Protection:** The MIC5219 includes internal reverse polarity protection, protecting both the regulator and the downstream circuitry if a battery is connected backwards.
