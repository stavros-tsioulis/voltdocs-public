## Overview

The **REG1117-3.3** is an 800 mA Low-Dropout (LDO) positive linear voltage regulator originally designed by Burr-Brown and manufactured by Texas Instruments. It provides a stable, fixed **+3.3 V DC output rail** from input voltages up to 15 V, delivering up to 800 mA of load current with a typical dropout voltage of 1.1 V (1.2 V maximum at full load).

Packaged in surface-mount **SOT-223 (DCY)**, **TO-263 (DDPAK)**, and **TO-252 (DPAK)** outlines, the REG1117 family features internal current limiting and thermal overload circuitry. It is widely employed as a pin-compatible alternative to the AMS1117-3.3, LM1117-3.3, and NCP1117-3.3 on microcontroller boards, industrial modules, and embedded peripherals requiring tight line/load regulation.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Low-Dropout (LDO) Positive Linear Regulator |
| **Package** | SOT-223 (4-lead DCY) / TO-263 (3-lead KTT) / TO-252 (3-lead KVU) |
| **Pinout (SOT-223 Top View)** | Pin 1: Ground (`GND`), Pin 2: Output (`VOUT`), Pin 3: Input (`VIN`), Tab: `VOUT` |
| **Fixed Output Voltage** | $+3.3\text{ V}$ DC ($\pm 1.0\%$ accuracy at $25^\circ\text{C}$, $\pm 1.5\%$ over full temp) |
| **Input Voltage Range ($V_{IN}$)** | $4.5\text{ V}$ to $15.0\text{ V}$ DC |
| **Dropout Voltage** | $1.2\text{ V}$ max at $I_{OUT} = 800\text{ mA}$ ($1.1\text{ V}$ typical) |
| **Continuous Output Current ($I_{OUT}$)** | $800\text{ mA}$ max (thermal limit dependent) |
| **Ripple Rejection (PSRR)** | $62\text{ dB} \dots 72\text{ dB}$ at $f = 120\text{ Hz}$ |

## Pinout (SOT-223 Package)

Looking at the **top face** of the SOT-223 package with the large metal tab at the top and the three leads pointing down:

```
        ┌───────────────┐
        │ [REG1117 Tab] │  (Metal Tab connected internally to Pin 2 VOUT)
        ├───────────────┤
        │  REG1117-3.3  │  (Top Package Face)
        └─┬────┬────┬───┘
          1    2    3
         GND  VOUT VIN
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` / `ADJ` | Power | Ground reference (0 V) for fixed 3.3V versions (Adjust pin on adjustable models) |
| 2 | `VOUT` / `TAB` | Power Output | Regulated +3.3V DC output pin (electrically connected to the heatsink tab) |
| 3 | `VIN` | Power Input | Unregulated DC input voltage pin (+4.5V to +15.0V DC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Output Voltage | $V_{OUT}$ | 3.267 | 3.300 | 3.333 | V | $I_{OUT} = 10\text{ mA}, V_{IN} = 4.8\text{ V}, T_J = 25^\circ\text{C}$ |
| Output Voltage (Full Temp) | $V_{OUT}$ | 3.250 | 3.300 | 3.350 | V | $0 \le I_{OUT} \le 800\text{ mA}, 4.75\text{ V} \le V_{IN} \le 10\text{ V}$ |
| Dropout Voltage | $V_{DO}$ | — | 1.1 | 1.2 | V | $I_{OUT} = 800\text{ mA}, T_J = 25^\circ\text{C}$ |
| Current Limit | $I_{LIM}$ | 900 | 1200 | 1500 | mA | $V_{IN} - V_{OUT} = 5\text{ V}$ |
| Quiescent Current | $I_Q$ | — | 5.0 | 10.0 | mA | $V_{IN} = 5.0\text{ V}, I_{OUT} = 0\text{ mA}$ |
| Line Regulation | $Reg_{line}$ | — | 0.1 | 0.2 | % | $4.75\text{ V} \le V_{IN} \le 12.0\text{ V}, I_{OUT} = 10\text{ mA}$ |
| Load Regulation | $Reg_{load}$ | — | 0.2 | 0.4 | % | $V_{IN} = 4.8\text{ V}, 10\text{ mA} \le I_{OUT} \le 800\text{ mA}$ |

## Typical Application Circuit

```
       +5V USB / Unregulated DC
           │
        [Pin 3: VIN]
        ┌─────────────┐
        │ REG1117-3.3 │
        └─────────────┘
        [Pin 2: VOUT] ────────────┬─────────────── +3.3V Regulated Output
           │                      │
        [Pin 1: GND]        [ C2: 10µF Tantalum ]
           │                      │
    [ C1: 10µF Tantalum ]        GND
           │
          GND
```

> [!IMPORTANT]
> **Output Capacitor & ESR Stability Guidelines:**
> - The REG1117 requires a **minimum $10\ \mu\text{F}$ output capacitor** (tantalum or electrolytic) to guarantee internal amplifier loop stability across load steps.
> - When using modern ultra-low-ESR ceramic capacitors ($<0.05\ \Omega$), place a small series damping resistor ($0.2\ \Omega \dots 0.5\ \Omega$) or pair with a bulk electrolytic capacitor to avoid high-frequency output oscillation.

## Common mistakes

- **Exceeding SOT-223 thermal power dissipation limits:** Linear power dissipation is calculated as $P_D = (V_{IN} - V_{OUT}) \times I_{OUT}$. Dropping 12V down to 3.3V at 500mA yields $P_D = (12 - 3.3) \times 0.5 = 4.35\text{ W}$, which will instantly trigger thermal shutdown on a standard PCB layout ($\theta_{JA} \approx 65^\circ\text{C/W}$). Keep $V_{IN} \le 5.5\text{V}$ for heavy continuous loads or provide ample PCB copper pour.
- **Shorting the metal tab to Ground:** On SOT-223 and TO-263 packages, the thermal tab is **internally tied to Pin 2 (`VOUT`)**, not Ground. Soldering the tab directly to a system ground plane creates a dead short on the 3.3V rail.
- **Insufficient input voltage below dropout:** If $V_{IN}$ falls below $V_{OUT} + V_{DO} \approx 3.3\text{V} + 1.2\text{V} = 4.5\text{V}$, the regulator drops out of regulation and $V_{OUT}$ sags.

## Notes

- **Pin-Compatible Drop-In Replacements:** AMS1117-3.3, LM1117-3.3, LD1117V33, NCP1117ST33T3G.
- **Voltage Options:** REG1117 (Adjustable), REG1117-2.85 (2.85V for SCSI termination), REG1117-3.3 (3.3V), REG1117-5 (5.0V).
