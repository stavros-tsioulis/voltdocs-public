## Overview

The **MCP1700-3302E** (MCP1700-3302E/TO) is an ultra-low quiescent current CMOS positive low-dropout (LDO) linear voltage regulator manufactured by Microchip Technology. Available in a 3-pin through-hole **TO-92** and surface-mount **SOT-23 / SOT-89** package, it supplies a fixed **$+3.3\text{V}$ DC** rail at up to **$250\text{ mA}$** with a mere **$1.6\ \mu\text{A}$ typical standby quiescent current**.

With a typical dropout voltage of only **$178\text{ mV}$ at $250\text{mA}$** ($70\text{ mV}$ at $100\text{mA}$) and full stability with small $1.0\ \mu\text{F}$ ceramic MLCC capacitors, the MCP1700 is the gold standard for battery-powered IoT microcontrollers (ESP32 deep sleep, nRF52, ATmega328P, SAMD21, MSP430) running from single-cell Li-ion/LiFePO4 batteries or $3\times\text{AA/AAA}$ alkaline packs where standard linear regulators would otherwise deplete the battery in idle mode.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Ultra-Low Quiescent CMOS Low-Dropout (LDO) Regulator |
| **Package** | TO-92 (3-pin through-hole) / SOT-23 / SOT-89 |
| **Output Voltage ($V_{OUT}$)** | $+3.3\text{ V}$ DC ($\pm 0.4\%$ typ, $\pm 2.0\%$ max) |
| **Input Voltage Range ($V_{IN}$)** | $3.5\text{ V}$ to $6.0\text{ V}$ DC ($6.5\text{ V}$ absolute max) |
| **Quiescent Ground Current ($I_Q$)** | **$1.6\ \mu\text{A}$ typical** ($4.0\ \mu\text{A}$ max over $-40^\circ\text{C} \dots 125^\circ\text{C}$) |
| **Dropout Voltage ($V_{DROP}$)** | $178\text{ mV}$ typ at $250\text{mA}$ / $70\text{ mV}$ at $100\text{mA}$ |
| **Maximum Output Current ($I_{OUT}$)** | $250\text{ mA}$ continuous ($350\text{ mA}$ peak current limit) |
| **Output Capacitor Stability** | Stable with standard $1.0\ \mu\text{F}$ ceramic capacitors |

## Pinout (TO-92 Package)

Looking at the **flat front face** of the TO-92 package with leads pointing downward:

```
        ┌─────────┐
        │  TO-92  │
        │ MCP1700 │
        │ -3302E  │
        └─┬───┬───┬─┘
          1   2   3
         GND VIN VOUT
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` | Ground | Common system ground reference ($0\text{ V}$) |
| 2 | `VIN` | Power Input | Battery / DC Input ($+3.5\text{ V}$ to $+6.0\text{ V}$) |
| 3 | `VOUT` | Power Output | Regulated $+3.3\text{ V}$ DC output (Requires minimum $1.0\ \mu\text{F}$ ceramic capacitor) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Output Voltage ($25^\circ\text{C}$) | $V_{OUT}$ | 3.234 | 3.300 | 3.366 | V | $V_{IN} = 4.3\text{V}, I_L = 100\ \mu\text{A}$ |
| Output Voltage (Full Temp) | $V_{OUT}$ | 3.201 | 3.300 | 3.399 | V | $-40^\circ\text{C} \le T_J \le +125^\circ\text{C}$ |
| Operating Input Voltage | $V_{IN}$ | 3.5 | — | 6.0 | V | Normal operation |
| Quiescent Current | $I_Q$ | — | 1.6 | 4.0 | µA | $I_L = 0\text{mA}, V_{IN} = 4.3\text{V}$ |
| Dropout Voltage ($250\text{mA}$) | $V_{DROP}$ | — | 178 | 350 | mV | $I_L = 250\text{mA}$ |
| Dropout Voltage ($100\text{mA}$) | $V_{DROP}$ | — | 70 | 150 | mV | $I_L = 100\text{mA}$ |
| Line Regulation | $\Delta V_{OUT}$ | — | 0.05 | 0.20 | %/V | $3.5\text{V} \le V_{IN} \le 6.0\text{V}, I_L = 100\ \mu\text{A}$ |
| Load Regulation | $\Delta V_{OUT}$ | — | 0.5 | 1.5 | % | $I_L = 1.0\text{mA} \dots 250\text{mA}$ |
| Short-Circuit Current | $I_{SC}$ | — | 350 | — | mA | $V_{OUT} = 0\text{V}$ |

## Typical Application Circuit

```
  Li-Ion Battery (3.7V - 4.2V) or 3x AA Cells (4.5V)
           │
           ├───[ C_IN: 1.0µF Ceramic MLCC ]───┐
           │                                  │
       [Pin 2: VIN]                           │
      MCP1700-3302E                           │
       [Pin 1: GND] ──────────────────────────┼─── Common System GND
       [Pin 3: VOUT]                          │
           │                                  │
           ├───[ C_OUT: 1.0µF Ceramic MLCC ]──┘
           │
  Regulated +3.3V DC (Ultra-low quiescent standby for battery IoT MCUs)
```

## Battery Life Comparison

| Regulator | Quiescent Current ($I_Q$) | Battery Life (Idle 1000mAh Battery) |
|---|---|---|
| **AMS1117-3.3** | $5000\ \mu\text{A}$ ($5\text{ mA}$) | $\approx 200\text{ Hours}$ (8 days) |
| **LP2950-3.3** | $75\ \mu\text{A}$ | $\approx 13,300\text{ Hours}$ (1.5 years) |
| **MCP1700-3.3** | **$1.6\ \mu\text{A}$** | **$\approx 625,000\text{ Hours}$ (71 years)** |

## Common mistakes

- **Exceeding the 6.0V input limit:** The absolute maximum input rating of the MCP1700 is **$6.5\text{V}$**. Connecting a $9\text{V}$ battery or $12\text{V}$ adapter directly will destroy the chip immediately.
- **Pinout difference from LP2950 / 78L05:**
  - **MCP1700:** Pin 1 = `GND`, Pin 2 = `VIN`, Pin 3 = `VOUT`
  - **LP2950:** Pin 1 = `VOUT`, Pin 2 = `GND`, Pin 3 = `VIN`
  *Always double check the pin order before inserting into a breadboard or PCB.*

## Notes

- **Suffix Guide:** `3302E` denotes $+3.3\text{V}$ output, extended temp ($-40^\circ\text{C} \dots 125^\circ\text{C}$); `/TO` designates through-hole TO-92 packaging.
