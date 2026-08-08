## Overview

The **AMS1117-3.3** is a popular 800 mA Low Dropout (LDO) positive linear voltage regulator manufactured by Advanced Monolithic Systems (and generic semiconductor foundries). Populated on nearly every Arduino Mega/Uno, ESP8266 NodeMCU, ESP32, and Raspberry Pi accessory PCB, it regulates $5.0\text{V}$ USB or $12\text{V}$ DC input power down to a stable **$+3.3\text{V}$ DC power rail** for microcontrollers and sensors.

Housed in a compact 3-pin **SOT-223 package**, the AMS1117 features a low dropout voltage of **$1.1\text{V}$ at maximum $800\text{ mA}$ load current**, built-in short circuit protection, and thermal overload protection.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Low Dropout (LDO) Positive Linear Regulator |
| **Package** | SOT-223 (Tab connected to Pin 2 VOUT) / TO-252 |
| **Pinout (SOT-223 Front)** | Pin 1: Ground (`GND`), Pin 2: Output (`VOUT`), Pin 3: Input (`VIN`) |
| **Fixed Output Voltage** | $+3.3\text{ V}$ DC ($\pm 1.5\%$ initial accuracy) |
| **Input Voltage Range ($V_{IN}$)**| $4.5\text{ V}$ to $15.0\text{ V}$ DC |
| **Dropout Voltage** | $1.1\text{ V}$ max at $I_{OUT} = 800\text{ mA}$ ($1.0\text{V}$ at $100\text{mA}$) |
| **Continuous Output Current ($I_{OUT}$)**| $800\text{ mA}$ max (temperature dependent) |
| **Ripple Rejection Ratio** | $60\text{ dB} \dots 75\text{ dB}$ at $f = 120\text{ Hz}$ |

## Pinout (SOT-223 Package)

Looking at the **top face** of the SOT-223 package with large metal tab at top and 3 leads pointing down:

```
        ┌───────────────┐
        │ [AMS1117 Tab] │  (Metal Tab connected internally to Pin 2 VOUT)
        ├───────────────┤
        │  AMS1117-3.3  │  (Top Package Face)
        └─┬────┬────┬───┘
          1    2    3
         GND  VOUT IN
```

| Pin | Name | Description |
|---|---|---|
| 1 | `GND` / `ADJ` | Ground reference (0 V) for fixed versions |
| 2 | `VOUT` / `TAB`| Regulated +3.3V DC output pin (connected to large heatsink tab) |
| 3 | `VIN` | Unregulated DC input voltage pin (+4.5V to +15V DC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Regulated Output Voltage| $V_{OUT}$ | 3.250 | 3.300 | 3.350 | V | $4.75\text{V} \le V_{IN} \le 10\text{V}, 0 \le I_O \le 800\text{mA}$ |
| Dropout Voltage | $V_D$ | — | 1.1 | 1.3 | V | $I_{OUT} = 800\text{mA}, T_J = 25^\circ\text{C}$ |
| Current Limit | $I_{LIMIT}$| 900 | 1100 | 1500 | mA | Short circuit peak limit |
| Quiescent Current | $I_Q$ | — | 5.0 | 10.0 | mA | $V_{IN} = 5.0\text{V}$ |
| Line Regulation | $Reg_{line}$| — | 0.2 | 0.5 | % | $V_{IN} = 4.8\text{V} \dots 12\text{V}$ |
| Load Regulation | $Reg_{load}$| — | 0.2 | 1.0 | % | $I_{OUT} = 10\text{mA} \dots 800\text{mA}$ |

## Decoupling Capacitor & Stability Requirements

```
       +5V USB / Input Power
          │
       [Pin 3: VIN]
        AMS1117-3.3
       [Pin 2: VOUT] ─────────────┬─────────────── +3.3V Regulated Rail
          │                       │
       [Pin 1: GND]         [ C2 = 22µF Tantalum/Electrolytic ]
          │                       │
   [ C1 = 10µF Tantalum ]        GND
          │
         GND
```

> [!IMPORTANT]
> Minimum ESR & Capacitor Requirements:
> - The AMS1117 requires a **minimum $22\ \mu\text{F}$ output capacitor** ($10\ \mu\text{F}$ minimum tantalum or electrolytic) to maintain loop stability and prevent high-frequency oscillation.
> - Avoid using ceramic output capacitors with ultra-low ESR ($<0.1\ \Omega$) directly on older AMS1117 chips without adding a small series resistor ($0.5\ \Omega$), or add a parallel $10\ \mu\text{F}$ electrolytic capacitor.

## Common mistakes

- **Thermal overload from 12V inputs:** Dropping 12V to 3.3V at 500mA creates $P_D = (12\text{V} - 3.3\text{V}) \times 0.5\text{A} = 4.35\text{ Watts}$. The tiny SOT-223 package PCB copper trace area can only dissipate $\sim 1.0\text{ Watt}$, causing thermal shutdown. Limit $V_{IN}$ to 5V when drawing high current ($>300\text{mA}$).
- **Shorting VOUT tab to grounded metal enclosures:** On SOT-223 AMS1117 packages, the large metal tab is connected to **Pin 2 (`VOUT`)**, NOT Ground. Grounding the tab short-circuits the 3.3V output.

## Notes

- **AMS1117 Output Variants:** AMS1117-1.8 (1.8V), AMS1117-2.5 (2.5V), **AMS1117-3.3 (3.3V)**, AMS1117-5.0 (5.0V), AMS1117-ADJ (Adjustable).
