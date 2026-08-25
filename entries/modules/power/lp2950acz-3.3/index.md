## Overview

The **LP2950ACZ-3.3** is a micropower low-dropout (LDO) positive voltage regulator manufactured by Texas Instruments (originally National Semiconductor). Housed in a standard 3-pin through-hole **TO-92** package, it provides a highly accurate, temperature-compensated **$+3.3\text{V}$ DC** output with an extremely low quiescent current ($75\ \mu\text{A}$ typ) and low dropout voltage ($380\text{ mV}$ at $100\text{mA}$).

The "A" grade suffix denotes premium **$\pm 0.5\%$ initial output voltage accuracy** at $25^\circ\text{C}$ ($\pm 1.0\%$ over temperature). With a maximum input voltage tolerance of **$30\text{V}$**, the LP2950ACZ-3.3 is tailored for battery-operated handheld devices, low-power sensor nodes, automotive auxiliary circuitry, and standby reference supplies powering 3.3V microcontrollers directly from 9V batteries, 12V adapters, or lithium cell packs.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Positive Low-Dropout (LDO) Linear Regulator |
| **Package** | TO-92 (3-pin through-hole) |
| **Output Voltage ($V_{OUT}$)** | $+3.3\text{ V}$ DC ($\pm 0.5\%$ initial accuracy) |
| **Input Voltage Range ($V_{IN}$)** | $3.8\text{ V}$ to $30.0\text{ V}$ DC |
| **Dropout Voltage ($V_{DROP}$)** | $50\text{ mV}$ typ at $1\text{mA}$ / $380\text{ mV}$ typ at $100\text{mA}$ |
| **Maximum Output Current ($I_{OUT}$)** | $100\text{ mA}$ continuous ($160\text{ mA}$ short-circuit limit) |
| **Quiescent Ground Current ($I_Q$)** | $75\ \mu\text{A}$ typical at light loads |
| **Operating Junction Temp** | $-40^\circ\text{C}$ to $+125^\circ\text{C}$ |

## Pinout (TO-92 Package)

Looking at the **flat front face** of the TO-92 package with leads pointing downward:

```
        ┌─────────┐
        │  TO-92  │
        │ LP2950  │
        │ ACZ-3.3 │
        └─┬───┬───┬─┘
          1   2   3
        VOUT GND VIN
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VOUT` | Power Output | Regulated $+3.3\text{ V}$ DC output (Requires minimum $1.0\ \mu\text{F}$ capacitor) |
| 2 | `GND` | Ground | Common system ground reference ($0\text{ V}$) |
| 3 | `VIN` | Power Input | Unregulated DC input ($+3.8\text{ V}$ to $+30.0\text{ V}$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Output Voltage ($25^\circ\text{C}$) | $V_{OUT}$ | 3.284 | 3.300 | 3.316 | V | $I_L = 100\ \mu\text{A}$ (A-grade) |
| Output Voltage (Full Temp) | $V_{OUT}$ | 3.267 | 3.300 | 3.333 | V | $-40^\circ\text{C} \le T_J \le +125^\circ\text{C}$ |
| Input Supply Voltage | $V_{IN}$ | 3.8 | — | 30.0 | V | Continuous operating DC |
| Line Regulation | $\Delta V_{OUT}$ | — | 0.04 | 0.2 | % | $3.8\text{V} \le V_{IN} \le 30\text{V}, I_L = 100\ \mu\text{A}$ |
| Load Regulation | $\Delta V_{OUT}$ | — | 0.1 | 0.3 | % | $100\ \mu\text{A} \le I_L \le 100\text{mA}$ |
| Dropout Voltage ($100\text{mA}$) | $V_{DROP}$ | — | 380 | 600 | mV | $\Delta V_{OUT} = 100\text{mV}, I_L = 100\text{mA}$ |
| Dropout Voltage ($1\text{mA}$) | $V_{DROP}$ | — | 50 | 80 | mV | $I_L = 1\text{mA}$ |
| Ground Quiescent Current | $I_Q$ | — | 75 | 120 | µA | $V_{IN} = 6\text{V}, I_L = 100\ \mu\text{A}$ |
| Peak Output Current | $I_{OUT(max)}$ | 110 | 160 | 250 | mA | $V_{OUT} = 0\text{V}$ (Short-circuit condition) |

## Typical Application Circuit

```
  Unregulated DC In (4.0V - 24V)
           │
           ├───[ C_IN: 1.0µF Tantalum/Ceramic ]───┐
           │                                      │
       [Pin 3: VIN]                               │
      LP2950ACZ-3.3                               │
       [Pin 2: GND] ──────────────────────────────┼─── Common System GND
       [Pin 1: VOUT]                              │
           │                                      │
           ├───[ C_OUT: 2.2µF - 10µF ESR 0.1Ω-5Ω ]─┘
           │
  Regulated +3.3V DC Output (Up to 100mA)
```

## Capacitor Selection & Stability

The LP2950 requires an output capacitor between `VOUT` and `GND` to maintain loop stability:
- **Minimum Capacitance:** $1.0\ \mu\text{F}$ (recommend $2.2\ \mu\text{F}$ to $10\ \mu\text{F}$).
- **ESR Requirements:** The equivalent series resistance (ESR) of the output capacitor must remain between **$0.1\ \Omega$ and $5.0\ \Omega$**.
- *Tip:* Solid tantalum or low-ESR electrolytic capacitors work ideally. If using ultra-low ESR multi-layer ceramic capacitors (MLCC with ESR $< 0.05\ \Omega$), place a small $0.5\ \Omega \dots 1.0\ \Omega$ series resistor in line with the capacitor to prevent LDO loop oscillation.

## Common mistakes

- **Using ultra-low ESR ceramic capacitors without series damping:** Pure MLCC capacitors with near-zero ESR can cause output ringing or high-frequency oscillation on classic PNP-pass LDOs like the LP2950.
- **Exceeding package thermal limits on high input voltages:** When powering a $100\text{mA}$ load from a $24\text{V}$ input, the power dissipated is $(24\text{V} - 3.3\text{V}) \times 0.1\text{A} = 2.07\text{ Watts}$. In a TO-92 package ($R_{\theta JA} \approx 160^\circ\text{C/W}$), this would overheat the die. Keep total dissipation in TO-92 below $0.5\text{ W}$.

## Notes

- **Pin-Compatible Equivalents:** LP2950CZ-3.3 (standard 1% grade), MCP1700-3302E/TO (ultra-low Iq CMOS LDO).
- **8-pin Variant:** The **LP2951** is the 8-pin SOIC/DIP companion featuring adjustable output, low-battery error flag, and logic shutdown.
