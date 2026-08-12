## Overview

The **CN7511** is a 1.5A step-down (buck) constant-current LED driver IC manufactured by Consonance Electronics. Housed in an **8-pin SOP package**, it drives high-power single LEDs or multi-LED strings at continuous currents up to **1.5 Amperes** from an input supply voltage range of **6.0V to 30.0V DC**.

Utilizing high-side current sensing with a low **100 mV feedback threshold ($V_{CS}$)**, the CN7511 minimizes power loss across the sense resistor and reaches **up to 95% efficiency**. Its `EN` pin accepts both high-frequency **PWM dimming** signals ($100\text{ Hz} \dots 50\text{ kHz}$) and **DC voltage analog dimming**.

## Quick reference

| | |
|---|---|
| **Input Supply Voltage (`VIN`)** | 6.0 V to 30.0 V DC |
| **Output LED Current** | Up to $1.5\text{ A}$ continuous (Set by current sense resistor $R_{CS}$) |
| **Sense Reference Voltage (`VCS`)**| $100\text{ mV}$ low-loss high-side threshold |
| **Efficiency** | Up to $95\%$ typical |
| **Dimming Support** | PWM Dimming ($100\text{ Hz} \dots 50\text{ kHz}$) & DC Analog Voltage Dimming |
| **Protection** | Thermal shutdown, Open-LED, Short-LED protection |
| **Package** | SOP-8 / SOP-8-EP |

## Pinout (SOP-8 Package)

```
             ┌───┴───┐
        GND 1│ 1   8 │ VIN (+6V to +30V)
         CS 2│       │ 7 SW (Switch Output)
         EN 3│ CN7511│ 6 SW
         NC 4│       │ 5 NC
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` | Power | Ground Reference (0 V) |
| 2 | `CS` | Input | High-Side Current Sense Input ($100\text{ mV}$ reference relative to VIN) |
| 3 | `EN` | Input | Enable & Dimming Input (High = On; Low = Shutdown; PWM or DC Analog Input) |
| 4, 5 | `NC` | Unused | No Internal Connection |
| 6, 7 | `SW` | Output | Internal MOSFET Switch Drain Pins |
| 8 | `VIN` | Power | Supply Input (+6.0V to +30.0V DC) |

## LED Current Programming Formula

The constant LED current ($I_{LED}$) is set by resistor $R_{CS}$ connected between `VIN` (Pin 8) and `CS` (Pin 2):

$$ I_{LED} = \frac{100\text{ mV}}{R_{CS}} = \frac{0.10\text{V}}{R_{CS}} $$

$$\text{For } I_{LED} = 1.0\text{ A} \implies R_{CS} = \frac{0.10\text{V}}{1.0\text{A}} = 0.10\ \Omega\ \ (1\text{W}).$$

## Common mistakes

- **Leaving `EN` (Pin 3) floating:** `EN` has an internal pull-down resistor. Leaving `EN` disconnected holds the IC in shutdown ($0\text{ mA}$). Connect `EN` to `VIN` or 3.3V/5V microcontroller GPIO for active operation.

## Notes

- **CN7511 vs PT4115:** CN7511 delivers up to 1.5A in SOP-8; PT4115 delivers up to 1.2A in SOT-89-5.
