## Overview

The **CAT4238** (CAT4238TD-GT3) is a high-voltage step-up (boost) DC-DC LED driver IC manufactured by ON Semiconductor. Operating at a fixed switching frequency of **1.0 MHz**, it generates output voltages up to **$38\text{ Volts}$** to drive up to 10 series-connected white LEDs at constant currents up to **$30\text{ mA}$**.

Powered from single-cell Li-ion batteries or regulated 5V power rails (**$2.8\text{V}$ to $5.5\text{V}$**), the CAT4238 features a low **$300\text{ mV}$ internal feedback reference voltage**, minimizing power loss across the current-sense resistor and achieving efficiency up to $87\%$.

## Quick reference

| | |
|---|---|
| **Input Voltage (`VIN`)** | 2.8 V to 5.5 V DC |
| **Output Voltage Limit (`VOUT`)**| Up to $38.0\text{ V}$ DC (Internal open-LED clamp protection at 38V) |
| **LED Capacity** | Up to 10 Series-Connected White LEDs |
| **Max LED Current** | $30\text{ mA}$ continuous (Set via sense resistor $R_{SET}$) |
| **Feedback Voltage (`VFB`)** | $300\text{ mV}$ reference |
| **Switching Frequency** | $1.0\text{ MHz}$ fixed PWM frequency |
| **Dimming Modes** | Direct PWM Dimming or DC Voltage Analog Dimming via `SHDN` |
| **Package** | TSOT-23 6-lead (SOT-23-6) |

## Pinout (TSOT-23-6 Package)

```
             ┌───┴───┐
        SW  1│ 1   6 │ GND
       GND  2│       │ 5 SHDN
        FB  3│CAT4238│ 4 VIN
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `SW` | Output | Internal Power MOSFET Drain Connection (Connect to Inductor & Schottky Diode) |
| 2 | `GND` | Power | Ground Reference (0 V) |
| 3 | `FB` | Input | Feedback Current Sense Input ($300\text{ mV}$ reference to GND) |
| 4 | `VIN` | Power | Power Supply Input (+2.8V to +5.5V DC) |
| 5 | `SHDN` | Input | Shutdown / PWM Dimming Control (High = Enable; Low = Shutdown $< 1\mu\text{A}$) |
| 6 | `GND` | Power | Ground Reference (0 V) |

## LED Current Programming Formula

The LED string current ($I_{LED}$) is set by resistor $R_{SET}$ connected between `FB` (Pin 3) and `GND`:

$$ I_{LED} = \frac{V_{FB}}{R_{SET}} = \frac{300\text{ mV}}{R_{SET}} = \frac{0.30\text{V}}{R_{SET}} $$

$$\text{For } I_{LED} = 20\text{ mA} \implies R_{SET} = \frac{0.30\text{V}}{0.020\text{A}} = 15\ \Omega.$$

## Common mistakes

- **Operating with an open LED load:** Disconnecting the LED string while powered causes the boost converter output voltage to rise rapidly. The CAT4238 includes an internal $38\text{V}$ overvoltage protection clamp, but omitting output capacitors leads to voltage spikes.
- **Using a low-frequency inductor:** The 1.0 MHz switching frequency requires a $10\ \mu\text{H} \dots 22\ \mu\text{H}$ low-DCR surface-mount power inductor rated for $\ge 350\text{ mA}$ saturation current.

## Notes

- **CAT4238 vs AP3012:** CAT4238 features an integrated 38V open-LED protection clamp; AP3012 requires an external Zener diode for overvoltage protection.
