## Overview

The **MBI6651** (MBI6651GSD) is a step-down (buck) constant-current LED driver IC manufactured by Macroblock Inc. Packaged in a **SOT-23-6**, **TO-252-5**, or **SOP-8** enclosure, it drives high-power LEDs at continuous currents up to **1.2 Amperes** from supply voltages ranging from **9.0V to 36.0V DC**.

Operating at switching frequencies up to **1.0 MHz**, the MBI6651 uses high-side current sensing with a low **100 mV reference voltage ($V_{SEN}$)** to maximize efficiency (up to $96\%$). Its multi-function `DIM` pin accepts both high-frequency **PWM dimming** signals ($100\text{ Hz} \dots 1\text{ kHz}$) and **DC voltage analog dimming** ($0.5\text{V} \dots 2.5\text{V}$).

## Quick reference

| | |
|---|---|
| **Input Supply Voltage (`VIN`)** | 9.0 V to 36.0 V DC |
| **Output LED Current** | Up to $1.2\text{ A}$ continuous (Set by sense resistor $R_{SEN}$) |
| **Sense Voltage (`VSEN`)** | $100\text{ mV}$ low-loss high-side threshold |
| **Switching Frequency** | Up to $1.0\text{ MHz}$ |
| **Efficiency** | Up to $96\%$ typical |
| **Dimming Modes** | PWM Dimming ($100\text{ Hz} \dots 1\text{ kHz}$) & DC Analog Voltage Dimming |
| **Package** | SOT-23-6 / TO-252-5 / SOP-8 |

## Pinout (SOT-23-6 Package)

```
             ┌───┴───┐
        SW  1│ 1   6 │ VIN (+9V to +36V)
       GND  2│       │ 5 SEN (Sense Input)
       DIM  3│MBI6651│ 4 NC
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `SW` | Output | Internal MOSFET Switch Drain (Connect to Schottky Diode & Inductor) |
| 2 | `GND` | Power | Ground Reference (0 V) |
| 3 | `DIM` | Input | Dimming Control Input (Open = 100% LED Current; Low = Shutdown; PWM or Analog Input) |
| 4 | `NC` | Unused | No Internal Connection |
| 5 | `SEN` | Input | High-Side Current Sense Input ($100\text{ mV}$ reference relative to VIN) |
| 6 | `VIN` | Power | Power Supply Input (+9.0V to +36.0V DC) |

## LED Current Programming Formula

$$ I_{LED} = \frac{100\text{ mV}}{R_{SEN}} = \frac{0.10\text{V}}{R_{SEN}} $$

$$\text{For } I_{LED} = 1.0\text{ A} \implies R_{SEN} = \frac{0.10\text{V}}{1.0\text{A}} = 0.10\ \Omega\ \ (1\text{W}).$$

## Common mistakes

- **Leaving `DIM` (Pin 3) grounded:** `DIM` pulled below $0.4\text{V}$ places the chip in shutdown mode ($0\text{ mA}$). For 100% continuous output brightness, leave `DIM` floating or pull HIGH to $V_{IN}$ / 3.3V / 5V.

## Notes

- **MBI6651 vs PT4115:** MBI6651 supports up to 36V input voltage range; PT4115 supports up to 30V input voltage range. Both use 100mV high-side current sense.
