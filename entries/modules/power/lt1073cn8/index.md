## Overview

The **LT1073CN8** (LT1073) is a versatile micropower switching regulator DC-DC converter manufactured by Linear Technology (now Analog Devices) in a classic through-hole **8-pin DIP (DIP-8)** package. Immortalized in iconic application notes written by analog circuit master **Jim Williams** (Linear Tech AN-29 and AN-30), the LT1073 operates from an ultra-wide input voltage range of **$1.0\text{V}$ to $30.0\text{V}$ DC** with a standby quiescent current of only **$95\ \mu\text{A}$**.

Employing a gated-oscillator control architecture with an internal **$1.0\text{A}$ peak power switch**, the LT1073 can be wired in three distinct power conversion topologies:
1. **Step-Up (Boost):** Converting a single $1.5\text{V}$ AA battery into regulated $+5\text{V}$ or $+12\text{V}$.
2. **Step-Down (Buck):** Stepping down a $9\text{V}$ or $12\text{V}$ battery to $3.3\text{V}$ or $5\text{V}$ with high light-load efficiency.
3. **Positive-to-Negative (Inverting):** Generating negative supply rails (e.g. $-5\text{V}$ or $-12\text{V}$) for op-amps and audio preamplifiers from a single positive battery rail.

It also incorporates an auxiliary **uncommitted gain block / comparator** with an internal $200\text{ mV}$ reference for building low-battery indicator circuits.

## Quick reference

| | |
|---|---|
| **Converter Type** | Micropower Multi-Topology DC-DC Converter |
| **Topologies Supported** | Step-Up (Boost), Step-Down (Buck), Positive-to-Negative (Inverter) |
| **Package** | 8-pin DIP (DIP-8 / N8) / 8-pin SOIC |
| **Operating Input Range ($V_{IN}$)** | **$1.0\text{ V}$ to $30.0\text{ V}$ DC** |
| **Quiescent Current ($I_Q$)** | **$95\ \mu\text{A}$ typical** ($135\ \mu\text{A}$ max) |
| **Internal Power Switch** | $1.0\text{ A}$ peak current rating, $V_{CESAT} \approx 0.45\text{ V}$ |
| **Feedback Reference ($V_{FB}$)** | $212\text{ mV}$ (Adjustable version) |
| **Fixed Output Versions** | LT1073-5 ($+5.0\text{V}$), LT1073-12 ($+12.0\text{V}$) |
| **Auxiliary Gain Block** | Open-collector comparator with $200\text{ mV}$ reference for Low Battery Warning |

## Pinout (DIP-8 Package)

```
                            ┌───┴───┐
      (Current Limit) ILIM 1│ 1   8 │ FB / SENSE (Feedback)
      (Supply Input)   VIN 2│ LT1073│ 7 SET (Low-Battery Sense In)
      (Collector)      SW1 3│  CN8  │ 6 AO (Low-Battery Open-Collector Out)
      (Emitter)        SW2 4│ DIP-8 │ 5 GND (0V)
                            └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `ILIM` | Control Input | Switch Current Limit (Tie to `VIN` for full 1A limit, or insert resistor to reduce limit) |
| 2 | `VIN` | Power Input | Input Power Supply ($+1.0\text{ V}$ to $+30.0\text{ V}$) |
| 3 | `SW1` | Switch Output | Collector of internal NPN power switch transistor |
| 4 | `SW2` | Switch Output | Emitter of internal NPN power switch transistor |
| 5 | `GND` | Ground | Common system ground reference ($0\text{ V}$) |
| 6 | `AO` | Digital Output | Auxiliary comparator output (Open-collector, pulls LOW when `SET` < 200mV) |
| 7 | `SET` | Analog Input | Auxiliary comparator input ($200\text{ mV}$ threshold against GND) |
| 8 | `FB / SENSE` | Feedback | Voltage feedback input ($212\text{ mV}$ threshold on adjustable version, or direct $V_{OUT}$ sense on -5/-12) |

## Typical Application Circuit: Single-Cell 1.5V to +5.0V Boost Converter

```
  Single 1.5V Alkaline / NiMH Cell
           │
           ├───[ C_IN: 47µF Electrolytic / Tantalum ]──┐
           │                                          │
           ├───[ Pin 1: ILIM ]                        │
           ├───[ Pin 2: VIN ]                         │
           │                                          │
           ├───[ L1: 100µH Inductor (Ferrite) ]───┐   │
           │                                      │   │
       [Pin 3: SW1] ◄─────────────────────────────┤   │
         LT1073-5                                 │   │
       [Pin 4: SW2] ──────────────────────────────┼───┼─── Common System GND
       [Pin 5: GND] ──────────────────────────────┼───┤
       [Pin 8: SENSE] ──────────────┬─────────────┘   │
           │                        │                 │
           │              [ D1: 1N5818 Schottky ] ────┘
           │                        │ (Cathode to SENSE)
           ├───[ C_OUT: 100µF Low-ESR Tantalum ]── GND
           │
  Regulated +5.0V DC Output (Supplies up to 40mA from 1.5V, or 100mA from 3V)
```

## Multi-Topology Connection Summary

| Topology | `SW1` (Collector / Pin 3) | `SW2` (Emitter / Pin 4) | Diode Cathode | Inductor Location |
|---|---|---|---|---|
| **Step-Up (Boost)** | To Inductor & Diode Anode | To Ground (`GND`) | To $V_{OUT}$ | Between $V_{IN}$ and `SW1` |
| **Step-Down (Buck)** | To Supply ($V_{IN}$) | To Inductor & Diode Cathode | To Ground (`GND`) | Between `SW2` and $V_{OUT}$ |
| **Inverter ($-V_{OUT}$)**| To Inductor & Diode Anode | To Supply ($V_{IN}$) | To Ground (`GND`) | Between `SW1` and Ground |

## Common mistakes

- **Allowing SW2 to drop below ground without Schottky clamping:** In step-down mode, when the switch turns off, `SW2` swings negative. A fast Schottky catch diode (e.g. 1N5818) must clamp `SW2` to prevent the substrate diode from conducting.
- **Using general-purpose high-ESR aluminum capacitors:** Gated-oscillator converters draw high-frequency pulsating currents. Using regular high-ESR electrolytic capacitors causes severe output voltage ripple. Use **tantalum or low-ESR polymer capacitors**.

## Notes

- **Suffix Guide:** `CN8` designates commercial temperature ($0^\circ\text{C} \dots 70^\circ\text{C}$) in an 8-pin plastic DIP; `-5` is fixed 5V; `-12` is fixed 12V; un-suffixed is adjustable ($V_{REF} = 212\text{ mV}$).
