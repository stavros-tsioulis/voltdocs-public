## Overview

The **NCP1117ST33T3G** (NCP1117-3.3) is an automotive- and industrial-grade fixed +3.3V low dropout (LDO) positive linear voltage regulator manufactured by ON Semiconductor (onsemi). Serving as a high-reliability, pin-compatible alternative to the ubiquitous AMS1117-3.3 and LM1117-3.3, it delivers continuous output currents exceeding **$1.0\text{ A}$** with a low dropout voltage of **$1.07\text{ V}$ at $800\text{ mA}$ ($1.2\text{ V}$ maximum at $1.0\text{ A}$)**.

Capable of accepting input voltages up to **$20.0\text{ V}$**, the NCP1117 incorporates internal short-circuit current limiting, safe operating area (SOA) protection, and thermal shutdown circuitry. Packaged in an industry-standard **SOT-223** surface-mount footprint, it is widely utilized across microcontroller development boards (STM32, ESP32, Arduino), networking routers, industrial PLC interfaces, and point-of-load 3.3V sub-regulation.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Low-Dropout (LDO) Positive Linear Voltage Regulator |
| **Package** | SOT-223-3 (TO-261AA) / DPAK (TO-252) |
| **Fixed Output Voltage** | $+3.3\text{ V}$ DC ($\pm 1.0\%$ tolerance at $25^\circ\text{C}$) |
| **Input Voltage Range ($V_{IN}$)** | $4.5\text{ V}$ to $20.0\text{ V}$ DC (Survival up to $20\text{V}$) |
| **Dropout Voltage** | $1.07\text{ V}$ typical at $800\text{ mA}$ ($1.20\text{ V}$ max at $1.0\text{ A}$) |
| **Maximum Output Current** | $1.0\text{ A}$ continuous (with adequate PCB copper pour) |
| **Quiescent Current** | $4.7\text{ mA}$ typical ($10.0\text{ mA}$ maximum) |
| **Ripple Rejection ($PSRR$)** | $70\text{ dB}$ at $120\text{ Hz}$ |
| **Pinout (SOT-223 Front)** | Pin 1: Ground (`GND`), Pin 2/Tab: Output (`VOUT`), Pin 3: Input (`VIN`) |

## Pinout (SOT-223 Package)

Looking down at the **top face** of the SOT-223 package with 3 leads facing down and the large tab facing up:

```
          ┌─────────────┐
          │  TAB (VOUT) │  (Metal Tab connected internally to Pin 2 VOUT)
          ├─────────────┤
          │  NCP1117-33 │  (Top Face)
          └──┬───┬───┬──┘
             1   2   3
           GND VOUT VIN
```

| Pin | Name | Description |
|---|---|---|
| 1 | `GND` | Ground reference connection (0 V) |
| 2 | `VOUT` / `TAB` | Regulated +3.3V DC voltage output (connected to tab) |
| 3 | `VIN` | Unregulated DC input voltage (+4.5V to +20.0V DC) |

> [!WARNING]
> The large heatsink tab is **electrically tied to Pin 2 (`VOUT`)**, not Ground. Connect the tab to a dedicated $+3.3\text{V}$ copper plane on the PCB for heat dissipation; never connect the tab directly to a ground plane.

## Standard Circuit & Capacitors

```
       +V_IN Input (4.75V - 12V DC)
          │
       [Pin 3: VIN]
        NCP1117ST33T3G
       [Pin 2: VOUT] ──────────────┬─────────────── +3.3V Regulated Output (1.0A max)
          │                       │
       [Pin 1: GND]          [ C_OUT = 10µF Tantalum/Ceramic ]
          │                       │
   [ C_IN = 10µF Tantalum ]      GND
          │
         GND
```

- **Input Capacitor ($C_{IN} = 10\ \mu\text{F}$):** Required to filter inductive transients on power supply input traces.
- **Output Capacitor ($C_{OUT} = 10\ \mu\text{F}$):** Tantalum or low-ESR electrolytic capacitor required for control loop stability ($0.3\ \Omega \le \text{ESR} \le 22\ \Omega$).

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Output Voltage | $V_{OUT}$ | 3.267 | 3.300 | 3.333 | V | $I_O = 10\text{mA}, T_J = 25^\circ\text{C}$ |
| Line Regulation | $Reg_{line}$ | — | 1.0 | 6.0 | mV | $4.75\text{V} \le V_{IN} \le 15\text{V}, I_O = 10\text{mA}$ |
| Load Regulation | $Reg_{load}$ | — | 2.0 | 10.0 | mV | $10\text{mA} \le I_O \le 1.0\text{A}$ |
| Dropout Voltage | $V_{DO}$ | — | 1.07 | 1.20 | V | $I_O = 800\text{ mA}$ |
| Output Current Limit | $I_{CL}$ | 1.0 | 1.5 | — | A | $(V_{IN} - V_{OUT}) \le 12\text{V}$ |
| Quiescent Current | $I_Q$ | — | 4.7 | 10.0 | mA | $V_{IN} \le 15\text{V}$ |
| Temperature Stability | $T_S$ | — | 0.5 | — | % | $-40^\circ\text{C} \le T_J \le 125^\circ\text{C}$ |

## Common mistakes

- **Using ultra-low ESR ($< 0.1\ \Omega$) ceramic output capacitors without damping:** The internal NPN Darlington pass-transistor architecture requires a small amount of ESR ($0.3\ \Omega \dots 2.2\ \Omega$) in the output capacitor for loop phase margin. Connecting a modern ceramic capacitor with $< 0.05\ \Omega$ ESR can cause high-frequency oscillations unless a small $0.5\ \Omega$ resistor is placed in series with the ceramic cap (or a standard tantalum capacitor is used).
- **Overheating on 12V-to-3.3V conversion:** Stepping down $12\text{V}$ to $3.3\text{V}$ at $500\text{mA}$ dissipates $(12 - 3.3) \times 0.5 = 4.35\text{ Watts}$. An SOT-223 package with typical PCB thermal resistance ($\approx 65^\circ\text{C/W}$) can only dissipate $\approx 1.5\text{ Watts}$ before exceeding $150^\circ\text{C}$ junction temperature. Keep input voltages below $6.0\text{V}$ for continuous loads $> 500\text{ mA}$.

## Notes

- **Pin-to-Pin Compatibility:** The NCP1117 is an exact pin-for-pin drop-in replacement for the AMS1117, LM1117, and AZ1117 series, offering higher maximum input voltage ($20\text{V}$ vs $15\text{V}$) and tighter output voltage tolerance ($\pm 1\%$).
