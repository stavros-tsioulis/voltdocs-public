## Overview

The **AL8807** (AL8807W5-7 / AL8807MP-13) is a step-down (buck) constant-current LED driver IC manufactured by Diodes Incorporated. Packaged in a compact **SOT-25 (SOT-23-5)** or **MSOP-8EP** housing, it drives high-brightness LEDs at continuous currents up to **1.0 Amp** from input supply voltages ranging from **6.0V to 30.0V DC**.

Operating at switching frequencies up to **1.0 MHz**, the AL8807 achieves **up to 96% efficiency** using a high-side current-sense circuit. Its multi-function `CTRL` pin supports both **PWM dimming** (up to 1 kHz) and **DC voltage analog dimming** ($0.5\text{V} \dots 2.5\text{V}$).

## Quick reference

| | |
|---|---|
| **Input Supply Voltage (`VIN`)** | 6.0 V to 30.0 V DC |
| **Output LED Current** | Up to $1.0\text{ A}$ continuous (Set by sense resistor $R_S$) |
| **Current Accuracy** | $\pm 5\%$ output current accuracy |
| **Switching Frequency** | Up to $1.0\text{ MHz}$ |
| **Efficiency** | Up to $96\%$ typical |
| **Dimming Modes** | PWM Dimming ($100\text{ Hz} \dots 1\text{ kHz}$) or DC Voltage Analog Dimming |
| **Package** | SOT-25 (SOT-23-5) / MSOP-8EP |

## Pinout (SOT-25 / SOT-23-5 Package)

```
             ┌───┴───┐
        SW  1│ 1   5 │ VIN (+6V to +30V)
       GND  2│       │
      CTRL  3│ AL8807│ 4 SET (Sense Input)
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `SW` | Output | Internal MOSFET Switch Drain (Connect to Freewheeling Diode & Inductor) |
| 2 | `GND` | Power | Ground Reference (0 V) |
| 3 | `CTRL` | Input | Control Pin (Open = 100% LED Current; Low = Shutdown; PWM or DC Analog Voltage Input) |
| 4 | `SET` | Input | High-Side Current Sense Input (Connect sense resistor $R_S$ between `VIN` and `SET`) |
| 5 | `VIN` | Power | Power Supply Input (+6.0V to +30.0V DC) |

## High-Side Buck LED Driver Circuit

```
  +6V to +30V DC Supply ───┬─── [Pin 5: VIN]
                           │
                   [Sense Resistor R_S]
                           │
                           ├─── [Pin 4: SET] ───► ( + ) LED String (1 to 8 LEDs in series)
                           │                               │
                      [AL8807]                             └─── [Inductor L1] ───┬─── [Pin 1: SW]
                           │                                                     │
                           └─── [Pin 2: GND] ─── Cathode Schottky Diode ─────────┘
```

## Output Current Formula

The constant LED current ($I_{LED}$) is set by high-side sense resistor $R_S$ connected between `VIN` and `SET`:

$$ I_{LED} = \frac{100\text{ mV}}{R_S} = \frac{0.10\text{V}}{R_S} $$

$$\text{For } I_{LED} = 700\text{ mA} \implies R_S = \frac{0.10\text{V}}{0.70\text{A}} \approx 0.143\ \Omega.$$

## Common mistakes

- **Leaving `CTRL` (Pin 3) grounded:** `CTRL` turns the IC OFF when pulled below $0.4\text{V}$. For 100% constant brightness, leave `CTRL` floating or pull HIGH to 3.3V/5V.
- **Using non-Schottky freewheeling diodes:** High 1MHz switching speed requires an ultra-fast low-forward-voltage Schottky diode (such as B140 or SS14).

## Notes

- **AL8807 vs PT4115:** AL8807 comes in a small 5-pin SOT-25 package; PT4115 is packaged in SOT-89-5. Both use high-side current sensing with $100\text{ mV}$ reference.
