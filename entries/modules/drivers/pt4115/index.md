## Overview

The **PT4115** (PT4115E / PT4115B) is an ubiquitous 30V 1.2A step-down (buck) constant-current LED driver IC manufactured by Power Trend Microelectronics (PowTech). Enclosed in a **SOT-89-5** or **ESOP-8** package, it is one of the most widely deployed LED driver ICs in modern maker electronics, driving MR16 lamps, automotive auxiliary lights, and DIY high-power LED spotlight modules ($1\text{W}, 3\text{W}, 5\text{W}, 10\text{W}$).

Operating over an input voltage range of **6.0V to 30.0V DC**, the PT4115 incorporates an internal **30V 1.2A power N-MOSFET**, high-side current sensing ($100\text{ mV}$ reference), thermal shutdown, and hysteretic PFM control to deliver **up to 97% efficiency**.

## Quick reference

| | |
|---|---|
| **Input Supply Voltage (`VIN`)** | 6.0 V to 30.0 V DC |
| **Output LED Current** | Up to $1.2\text{ A}$ continuous (Set by high-side sense resistor $R_S$) |
| **Sense Voltage (`VCSN`)** | $100\text{ mV}$ low-loss high-side threshold |
| **Internal Switch Rating** | $30\text{ V}, 1.2\text{ A}$ integrated N-MOSFET |
| **Efficiency** | Up to $97\%$ typical |
| **Dimming Modes** | PWM Dimming ($100\text{ Hz} \dots 50\text{ kHz}$) & DC Analog Voltage Dimming ($0.5\text{V} \dots 2.5\text{V}$) |
| **Package** | SOT-89-5 / ESOP-8 |

## Pinout (SOT-89-5 Package)

```
             ┌───┴───┐
        SW  1│ 1   5 │ CSN (Sense Input)
       GND  2│       │
       DIM  3│ PT4115│ 4 VIN (+6V to +30V)
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `SW` | Output | Internal MOSFET Switch Drain (Connect to Freewheeling Schottky Diode & Inductor) |
| 2 | `GND` | Power | Ground Reference (0 V) |
| 3 | `DIM` | Input | Multi-function Control Pin (Open = 100% LED Current; Low = Shutdown; PWM or DC Analog Input) |
| 4 | `VIN` | Power | Power Supply Input (+6.0V to +30.0V DC) |
| 5 | `CSN` | Input | High-Side Current Sense Input (Connect sense resistor $R_S$ between `VIN` and `CSN`) |

## High-Side Buck LED Application Circuit

```
  +6V to +30V DC Supply ───┬─── [Pin 4: VIN]
                           │
                   [Sense Resistor R_S]
                           │
                           ├─── [Pin 5: CSN] ───► ( + ) High-Power LED String
                           │                             │
                      [PT4115]                           └─── [Inductor L1 (68µH)] ───┬─── [Pin 1: SW]
                           │                                                           │
                           └─── [Pin 2: GND] ─── Cathode Schottky Diode (SS14) ────────┘
```

## Output LED Current Formula

$$ I_{LED} = \frac{100\text{ mV}}{R_S} = \frac{0.10\text{V}}{R_S} $$

$$\text{For } I_{LED} = 350\text{ mA } (1\text{W LED}) \implies R_S = \frac{0.10\text{V}}{0.35\text{A}} \approx 0.28\ \Omega.$$
$$\text{For } I_{LED} = 700\text{ mA } (3\text{W LED}) \implies R_S = \frac{0.10\text{V}}{0.70\text{A}} \approx 0.14\ \Omega.$$

## Common mistakes

- **Leaving `DIM` (Pin 3) pulled LOW:** Pulling `DIM` below $0.3\text{V}$ places the PT4115 into ultra-low-power standby mode. For full constant brightness, leave `DIM` floating or pull HIGH to 3.3V/5V.
- **Forgetting PCB copper heatsinking under SOT-89 package:** Running $1.2\text{A}$ continuously generates thermal heat. Solder the SOT-89 tab to a wide PCB ground copper plane.

## Notes

- **PT4115 vs AL8807 vs CN7511:** All three are 30V step-down LED drivers; PT4115 is packaged in SOT-89-5 and remains the budget standard on open-source hardware modules.
