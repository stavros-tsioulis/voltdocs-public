## Overview

The **TMP36** is a low-voltage, precision centigrade temperature sensor manufactured by Analog Devices. It provides a linear voltage output proportional to Celsius temperature at **$10\text{ mV/}^\circ\text{C}$**.

Designed specifically for single-supply 2.7 V to 5.5 V operation (ideal for 3.3V microcontrollers like ESP32 or Raspberry Pi), it incorporates a **500 mV DC offset** at $0^\circ\text{C}$. This offset allows the sensor to measure negative temperatures down to $-40^\circ\text{C}$ without requiring a negative supply voltage rail.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 2.7 V to 5.5 V DC |
| **Output scale factor** | $10.0\text{ mV / }^\circ\text{C}$ ($100\text{ mV}$ at $-40^\circ\text{C}$, $500\text{ mV}$ at $0^\circ\text{C}$, $750\text{ mV}$ at $+25^\circ\text{C}$) |
| **Temperature range** | $-40^\circ\text{C}$ to $+125^\circ\text{C}$ |
| **Accuracy** | $\pm 1.0\text{ }^\circ\text{C}$ typical at $+25^\circ\text{C}$ ($\pm 2.0\text{ }^\circ\text{C}$ max over range) |
| **Quiescent current** | 50 µA typical |
| **Shutdown current** | 0.5 µA max |
| **Package options** | TO-92 (3-pin plastic), SOIC-8, SOT-23 |

## Pinout

### Standard TO-92 Plastic Package (Flat side facing you, pins down)

```
        ┌─────────┐
        │  TMP36  │
        └─────────┘
          │  │  │
          1  2  3
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+2.7 V to +5.5 V DC) |
| 2 | `VOUT` | Analog Output | Voltage output ($500\text{ mV}$ offset + $10\text{ mV/}^\circ\text{C}$) |
| 3 | `GND` | Power | Ground (0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{S}$ | 2.7 | 3.3 / 5.0 | 5.5 | V | DC |
| Output Voltage at $0^\circ\text{C}$ | $V_{0\text{C}}$ | 490 | 500 | 510 | mV | $T_A = 0^\circ\text{C}$ |
| Output Scale Factor | $S$ | 9.8 | 10.0 | 10.2 | mV/°C | $+25^\circ\text{C}$ |
| Accuracy | $\Delta T$ | -2.0 | $\pm 1.0$ | +2.0 | °C | Full $-40^\circ\text{C} \text{ to } +125^\circ\text{C}$ range |
| Quiescent Current | $I_{SY}$ | — | 50 | 65 | µA | $V_{S} = 3.3\text{ V}$ |
| Load Capacitance Drive | $C_{L}$ | — | — | 1000 | pF | Without series resistor |

## Temperature Conversion Formula

To calculate temperature ($T$ in °C) from the measured output voltage ($V_{OUT}$ in Volts):

$$T\text{ }(^\circ\text{C}) = \frac{V_{OUT}\text{ (in Volts)} - 0.500\text{ V}}{0.010\text{ V/}^\circ\text{C}} = (V_{OUT}\text{ (in mV)} - 500) \times 0.1$$

With a 10-bit ADC ($1024$ steps) on a $3.3\text{ V}$ microcontroller ($V_{REF} = 3300\text{ mV}$):

$$V_{OUT}\text{ (in mV)} = \frac{\text{ADC Reading} \times 3300\text{ mV}}{1024}$$

$$T\text{ }(^\circ\text{C}) = \frac{V_{OUT}\text{ (in mV)} - 500}{10}$$

## Wiring

| TMP36 Pin | → | Microcontroller (Arduino Uno / ESP32) |
|---|---|---|
| 1 (`VCC`) | | `3.3V` (or `5V`) |
| 2 (`VOUT`) | | Analog Input Pin `A0` (or ESP32 ADC) |
| 3 (`GND`) | | `GND` |

## Common mistakes

- **Mixing up LM35 and TMP36 math:** The LM35 outputs $0\text{ mV}$ at $0^\circ\text{C}$, whereas the TMP36 outputs **$500\text{ mV}$** at $0^\circ\text{C}$. Forgetting to subtract 500 mV yields temperatures $50^\circ\text{C}$ too high!
- **Connecting pins backwards:** Swapping `VCC` and `GND` causes the package to heat up rapidly and break.
- **Noisy ADC readings from long wires:** High capacitive loads ($>1000\text{ pF}$) can cause $V_{OUT}$ oscillation. Add a $1\text{ k}\Omega$ series resistor near $V_{OUT}$ or a $0.1\text{ }\mu\text{F}$ bypass capacitor between $V_{CC}$ and $GND$.

## Notes

- The TMP36 is pin-compatible with the LM35 but operates at lower supply voltages ($2.7\text{ V}$ min vs $4.0\text{ V}$ min).
