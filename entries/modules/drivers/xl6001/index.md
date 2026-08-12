## Overview

The **XL6001** (XL6001E1) is a 60V, 4A step-up (boost) and buck-boost constant-current LED driver IC manufactured by XLSEMI. Packaged in a **TO-263-5L (DDPAK)** or **SOP-8L** enclosure, it is widely featured on low-cost high-power LED driver breakout boards sold across global hobbyist markets.

Operating across an input voltage range of **5.0V to 32.0V DC**, the XL6001 integrates a **4.0A N-channel power MOSFET** rated for **60V output**, a 220 kHz fixed-frequency oscillator, and a low **220 mV feedback reference voltage ($V_{FB}$)** to minimize sense resistor power dissipation, achieving system efficiency up to $93\%$.

## Quick reference

| | |
|---|---|
| **Input Supply Voltage (`VIN`)** | 5.0 V to 32.0 V DC |
| **Output Switch Voltage (`SW`)**| Up to $60.0\text{ V}$ DC (Internal MOSFET breakdown 60V) |
| **Internal Switch Current** | $4.0\text{ A}$ continuous switch limit |
| **Feedback Voltage (`VFB`)** | $220\text{ mV}$ low-loss reference |
| **Switching Frequency** | $220\text{ kHz}$ fixed frequency |
| **Efficiency** | Up to $93\%$ typical |
| **Protection** | Thermal shutdown, Over-Current Protection (OCP), Output Over-Voltage Protection |
| **Package** | TO-263-5L (DDPAK) / SOP-8L |

## Pinout (TO-263-5L Package)

Looking at the **front face** of the 5-lead TO-263 package with leads pointing down:

```
        ┌─────────────┐
        │   O   [TAB] │  (Metal Mounting Tab = SW Output)
        ├─────────────┤
        │   XL6001    │  (Front Package Face)
        └─┬─┬─┬─┬─┬───┘
          1 2 3 4 5
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` | Power | Ground Reference (0 V) |
| 2 | `EN` | Input | Enable Input (High = Normal Operation; Low = Shutdown) |
| 3 | `SW` | Output | Internal N-Channel Power MOSFET Drain (Connected internally to Metal Tab!) |
| 4 | `FB` | Input | Constant Current Feedback Input ($220\text{ mV}$ reference to GND) |
| 5 | `VIN` | Power | Positive Supply Input (+5.0V to +32V DC) |

## Constant LED Current Formula

The constant LED current ($I_{LED}$) is set by resistor $R_{CS}$ connected in series with the LED string to GND:

$$ I_{LED} = \frac{V_{FB}}{R_{CS}} = \frac{220\text{ mV}}{R_{CS}} = \frac{0.22\text{V}}{R_{CS}} $$

$$\text{For } I_{LED} = 1.0\text{ A} \implies R_{CS} = \frac{0.22\text{V}}{1.0\text{A}} = 0.22\ \Omega\ \ (2\text{W}).$$

## Common mistakes

- **Leaving `SW` tab uninsulated:** The TO-263 metal tab is connected directly to **`SW` (Pin 3)**. Mounting the tab directly onto a grounded metal heatsink creates a dead short circuit across the internal 60V switch.
- **Operating without an overvoltage protection Zener:** In boost LED drivers, if the LED string is disconnected while powered, $V_{OUT}$ climbs rapidly. Connect a Zener diode ($V_Z \le 55\text{V}$) from $V_{OUT}$ to `FB` for open-load clamping.

## Notes

- **XL6001 vs PT4115:** XL6001 is a 60V 4A boost/buck-boost driver; PT4115 is a 30V 1.2A buck driver for stepping down higher voltages.
