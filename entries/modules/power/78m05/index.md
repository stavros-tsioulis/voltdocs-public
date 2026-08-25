## Overview

The **78M05** (L78M05 / MC78M05 / LM78M05) is the medium-power 3-terminal positive fixed linear voltage regulator delivering **$+5.0\text{V}$ DC** at up to **$500\text{ mA}$ ($0.5\text{A}$)**. Housed in standard **TO-220, DPAK (TO-252), and IPAK** packages, it fills the design space between the low-power $100\text{mA}$ 78L05 (TO-92) and the heavy-duty $1.5\text{A}$ LM7805 (TO-220).

Operating with an input voltage range from **$7.0\text{V}$ to $35.0\text{V}$ DC**, the 78M05 incorporates full internal thermal overload protection, internal short-circuit current limiting, and output transistor safe-operating-area (SOA) protection. It is an ideal regulator for microcontroller boards, relay driver circuits, and sensor subsystems that require more than $100\text{mA}$ without requiring the physical board footprint or heatsink mass of a full 1.5A regulator.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Positive Fixed Linear Voltage Regulator |
| **Package Options** | TO-220-3 / DPAK (TO-252) / SOT-82 / IPAK |
| **Output Voltage ($V_{OUT}$)** | $+5.0\text{ V}$ DC ($\pm 2\%$ to $\pm 4\%$) |
| **Input Voltage Range ($V_{IN}$)** | $7.0\text{ V}$ to $35.0\text{ V}$ DC |
| **Dropout Voltage ($V_{DROP}$)** | $2.0\text{ V}$ typical at $500\text{mA}$ |
| **Maximum Output Current ($I_{OUT}$)** | $500\text{ mA}$ ($0.5\text{ A}$) continuous |
| **Quiescent Ground Current ($I_Q$)** | $4.2\text{ mA}$ typical ($6.0\text{ mA}$ max) |
| **Operating Junction Temp** | $0^\circ\text{C}$ to $+125^\circ\text{C}$ (Commercial) / $-40^\circ\text{C} \dots 125^\circ\text{C}$ (Industrial) |

## Pinout (TO-220 / DPAK Package)

Looking at the **front labeled face** of the TO-220 / DPAK package with leads pointing downward:

```
        ┌──────────────┐
        │  O  [Metal]  │ ── Tab is internally tied to Pin 2 (GND)
        ├──────────────┤
        │    78M05     │
        └─┬────┬────┬──┘
          1    2    3
         VIN  GND  VOUT
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VIN` | Power Input | Unregulated DC Input voltage ($+7.0\text{ V}$ to $+35.0\text{ V}$) |
| 2 (Tab) | `GND` | Ground | Common system ground reference ($0\text{ V}$, internally tied to tab) |
| 3 | `VOUT` | Power Output | Regulated $+5.0\text{ V}$ DC output (Requires $0.1\ \mu\text{F}$ bypass capacitor) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Output Voltage ($25^\circ\text{C}$) | $V_{OUT}$ | 4.90 | 5.00 | 5.10 | V | $V_{IN} = 10\text{V}, I_O = 350\text{mA}$ (2% A-grade) |
| Output Voltage (Full Temp) | $V_{OUT}$ | 4.75 | 5.00 | 5.25 | V | $7.0\text{V} \le V_{IN} \le 20\text{V}, I_O = 5\text{mA} \dots 350\text{mA}$ |
| Line Regulation | $\Delta V_{OUT}$ | — | 3.0 | 50.0 | mV | $7.0\text{V} \le V_{IN} \le 25\text{V}, I_O = 200\text{mA}$ |
| Load Regulation | $\Delta V_{OUT}$ | — | 10.0 | 50.0 | mV | $I_O = 5.0\text{mA} \dots 500\text{mA}$ |
| Dropout Voltage | $V_{DROP}$ | — | 2.0 | 2.5 | V | $T_J = 25^\circ\text{C}, I_O = 500\text{mA}$ |
| Quiescent Current | $I_Q$ | — | 4.2 | 6.0 | mA | $V_{IN} = 10\text{V}, I_O = 200\text{mA}$ |
| Peak Output Current | $I_{OUT(pk)}$ | 500 | 700 | — | mA | $T_J = 25^\circ\text{C}$ |
| Ripple Rejection | $RR$ | 62 | 80 | — | dB | $f = 120\text{ Hz}, V_{IN} = 8\text{V} \dots 18\text{V}$ |

## Typical Application Circuit

```
  Unregulated DC In (7.0V - 24V)
           │
           ├───[ C_IN: 0.33µF Ceramic / Tantalum ]──┐
           │                                        │
       [Pin 1: VIN]                                 │
         78M05                                      │
       [Pin 2: GND] ────────────────────────────────┼─── Common System GND
       [Pin 3: VOUT]                                │
           │                                        │
           ├───[ C_OUT: 0.1µF Ceramic ]─────────────┘
           │
  Regulated +5.0V DC Output (Up to 500mA)
```

## Comparison: 78L05 vs 78M05 vs LM7805

| Parameter | 78L05 | 78M05 | LM7805 |
|---|---|---|---|
| **Max Current** | **$100\text{ mA}$** | **$500\text{ mA}$** | **$1500\text{ mA}$ ($1.5\text{A}$)** |
| **Typical Package** | TO-92 | TO-220 / DPAK | TO-220 / TO-3 |
| **Pinout (Facing Front)**| `VOUT - GND - VIN` | `VIN - GND - VOUT` | `VIN - GND - VOUT` |
| **Thermal Resistance ($\theta_{JA}$)**| $\approx 160^\circ\text{C/W}$ | $\approx 65^\circ\text{C/W}$ | $\approx 50^\circ\text{C/W}$ |

## Common mistakes

- **Assuming 78M05 shares the 78L05 pinout:**
  - **78M05 / LM7805 (TO-220 / DPAK):** Pin 1 = `VIN`, Pin 2 = `GND`, Pin 3 = `VOUT`
  - **78L05 (TO-92):** Pin 1 = `VOUT`, Pin 2 = `GND`, Pin 3 = `VIN`
  *Always verify the package type when migrating a design between 78L05 and 78M05.*
- **Neglecting thermal heatsinking at high input voltages:** At $V_{IN} = 15\text{V}$ and $I_{OUT} = 400\text{mA}$, dissipated power is $P = (15 - 5) \times 0.4 = 4.0\text{ Watts}$. Without a heatsink, the internal thermal protection will trip within seconds.

## Notes

- **"M" Designation:** In standard semiconductor nomenclature, the "M" denotes **Medium power** ($500\text{mA}$), "L" denotes **Low power** ($100\text{mA}$), and no letter denotes standard power ($1.0\text{A} \dots 1.5\text{A}$).
