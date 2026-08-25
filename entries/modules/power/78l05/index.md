## Overview

The **78L05** (LM78L05 / MC78L05 / L78L05) is the classic 3-terminal positive fixed linear voltage regulator delivering **$+5.0\text{V}$ DC** at up to **$100\text{ mA}$**. Housed in a through-hole **TO-92** package, it is the low-current, compact companion to the ubiquitous 1.5A LM7805 (TO-220).

Operating with an input voltage range from **$7.0\text{V}$ to $30.0\text{V}$ DC**, the 78L05 incorporates internal thermal overload protection, internal short-circuit current limiting, and safe-area compensation. It is widely used across breadboards, consumer electronics, audio preamplifiers, and retrocomputing modules for local point-of-load 5V regulation where load currents remain below $100\text{mA}$.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Positive Fixed Linear Voltage Regulator |
| **Package** | TO-92 (3-pin through-hole) / SOIC-8 / SOT-89 |
| **Output Voltage ($V_{OUT}$)** | $+5.0\text{ V}$ DC ($\pm 4\%$ or $\pm 5\%$) |
| **Input Voltage Range ($V_{IN}$)** | $7.0\text{ V}$ to $30.0\text{ V}$ DC ($35\text{ V}$ max surge) |
| **Dropout Voltage ($V_{DROP}$)** | $1.7\text{ V}$ typical ($2.0\text{ V}$ max at $100\text{mA}$) |
| **Maximum Output Current ($I_{OUT}$)** | $100\text{ mA}$ continuous ($140\text{ mA}$ peak) |
| **Quiescent Ground Current ($I_Q$)** | $3.5\text{ mA}$ typical ($5.5\text{ mA}$ max) |
| **Operating Junction Temp** | $0^\circ\text{C}$ to $+125^\circ\text{C}$ (Commercial) / $-40^\circ\text{C} \dots 125^\circ\text{C}$ (Industrial) |

## Pinout (TO-92 Package)

Looking at the **flat front face** of the TO-92 package with leads pointing downward:

```
        ┌─────────┐
        │  TO-92  │
        │  78L05  │
        └─┬───┬───┬─┘
          1   2   3
        VOUT GND VIN
```

*(Note: When viewing from the bottom lead entrance, Pin 1 is Output on the right or left depending on convention; looking at the flat face, left-to-right is Pin 1: Output, Pin 2: Ground, Pin 3: Input).*

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VOUT` | Power Output | Regulated $+5.0\text{ V}$ DC output (Connect $0.1\ \mu\text{F}$ bypass capacitor) |
| 2 | `GND` | Ground | Common system ground reference ($0\text{ V}$) |
| 3 | `VIN` | Power Input | Unregulated DC input ($+7.0\text{ V}$ to $+30.0\text{ V}$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Output Voltage ($25^\circ\text{C}$) | $V_{OUT}$ | 4.80 | 5.00 | 5.20 | V | $V_{IN} = 10\text{V}, I_O = 40\text{mA}$ (4% A-grade) |
| Output Voltage (Full Temp) | $V_{OUT}$ | 4.75 | 5.00 | 5.25 | V | $7.0\text{V} \le V_{IN} \le 20\text{V}, I_O = 1\text{mA} \dots 40\text{mA}$ |
| Line Regulation | $\Delta V_{OUT}$ | — | 32 | 150 | mV | $7.0\text{V} \le V_{IN} \le 20\text{V}$ |
| Load Regulation | $\Delta V_{OUT}$ | — | 15 | 60 | mV | $I_O = 1.0\text{mA} \dots 100\text{mA}$ |
| Dropout Voltage | $V_{DROP}$ | — | 1.7 | 2.0 | V | $T_J = 25^\circ\text{C}, I_O = 100\text{mA}$ |
| Quiescent Current | $I_Q$ | — | 3.5 | 5.5 | mA | $V_{IN} = 10\text{V}, I_O = 0\text{mA}$ |
| Peak Output Current | $I_{OUT(pk)}$ | 110 | 140 | — | mA | $T_J = 25^\circ\text{C}$ |
| Ripple Rejection | $RR$ | 41 | 49 | — | dB | $f = 120\text{ Hz}, V_{IN} = 8\text{V} \dots 18\text{V}$ |

## Typical Application Circuit

```
  Unregulated DC In (7.0V - 24V)
           │
           ├───[ C_IN: 0.33µF Ceramic / Tantalum ]──┐
           │                                        │
       [Pin 3: VIN]                                 │
         78L05                                      │
       [Pin 2: GND] ────────────────────────────────┼─── Common System GND
       [Pin 1: VOUT]                                │
           │                                        │
           ├───[ C_OUT: 0.1µF Ceramic ]─────────────┘
           │
  Regulated +5.0V DC Output (Up to 100mA)
```

## Thermal & Power Dissipation

Because the 78L05 is a linear regulator, all excess voltage is converted directly into heat:

$$ P_{diss} = (V_{IN} - V_{OUT}) \times I_{OUT} $$

- **With $V_{IN} = 9\text{V}$ and $I_{OUT} = 50\text{mA}$:**
  $$ P_{diss} = (9\text{V} - 5\text{V}) \times 0.05\text{A} = 0.20\text{ Watts} \quad (\Delta T \approx 0.20\text{W} \times 160^\circ\text{C/W} = +32^\circ\text{C}) $$
- **With $V_{IN} = 24\text{V}$ and $I_{OUT} = 100\text{mA}$:**
  $$ P_{diss} = (24\text{V} - 5\text{V}) \times 0.1\text{A} = 1.9\text{ Watts} \quad (\text{Thermal shutdown will trigger in TO-92}) $$

## Common mistakes

- **Assuming 78L05 is a Low-Dropout (LDO) regulator:** The 78L05 requires at least **$7.0\text{V}$ input** ($V_{IN} \ge V_{OUT} + 2.0\text{V}$) to regulate 5.0V. It will not work from a 5V USB port or 6V battery pack (use an **LM2931-5.0** or **LP2950-5.0** instead).
- **Pinout mirror confusion:** The TO-92 78L05 pinout (`VOUT-GND-VIN`) is completely different from the TO-220 LM7805 pinout (`VIN-GND-VOUT`). Reversing input and output pins will cause the chip to draw excessive current and overheat.

## Notes

- **78L05 vs LM7805:** 78L05 is rated for $100\text{ mA}$ max in TO-92; LM7805 is rated for $1.5\text{ A}$ max in TO-220.
