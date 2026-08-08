## Overview

The **LM35** is a precision integrated-circuit temperature sensor manufactured by Texas Instruments. Its output voltage is linearly proportional to the Celsius (Centigrade) temperature, scaling at **$10\text{ mV/}^\circ\text{C}$**.

Unlike thermistors, the LM35 requires no external calibration or signal conditioning circuit to deliver typical accuracies of $\pm 0.25\text{ }^\circ\text{C}$ at room temperature and $\pm 0.75\text{ }^\circ\text{C}$ over a full $-55^\circ\text{C}\text{ to }+150^\circ\text{C}$ range. It draws only 60 µA from its supply, resulting in minimal self-heating ($< 0.1\text{ }^\circ\text{C}$ in still air).

## Quick reference

| | |
|---|---|
| **Supply voltage (`VCC`)** | 4.0 V to 30.0 V DC |
| **Output scale factor** | $10.0\text{ mV / }^\circ\text{C}$ ($0\text{ mV}$ at $0^\circ\text{C}$, $250\text{ mV}$ at $+25^\circ\text{C}$) |
| **Temperature range (Basic circuit)** | $+2^\circ\text{C}$ to $+150^\circ\text{C}$ |
| **Temperature range (Full range with pull-down)** | $-55^\circ\text{C}$ to $+150^\circ\text{C}$ |
| **Accuracy** | $\pm 0.5\text{ }^\circ\text{C}$ at $+25^\circ\text{C}$ ($\pm 0.25\text{ }^\circ\text{C}$ for LM35A) |
| **Quiescent current** | 60 µA typical |
| **Package options** | TO-92 (3-pin plastic), SOIC-8, TO-46 (metal can) |

## Pinout

### Standard TO-92 Plastic Package (Flat side facing you, pins down)

```
        ┌─────────┐
        │  LM35   │
        └─────────┘
          │  │  │
          1  2  3
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+4.0 V to +30.0 V DC) |
| 2 | `VOUT` | Analog Output | Voltage output linearly proportional to temperature ($10\text{ mV/}^\circ\text{C}$) |
| 3 | `GND` | Power | Ground (0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{S}$ | 4.0 | 5.0 | 30.0 | V | DC |
| Output Scale Factor | $S$ | 9.9 | 10.0 | 10.1 | mV/°C | $+25^\circ\text{C}$ |
| Accuracy (LM35D) | $\Delta T$ | -1.5 | $\pm 0.6$ | +1.5 | °C | At $+25^\circ\text{C}$ |
| Non-Linearity | $NL$ | — | $\pm 0.2$ | $\pm 0.5$ | °C | Over full temperature range |
| Quiescent Current | $I_{S}$ | 43 | 56 | 133 | µA | $V_{S} = 5.0\text{ V}$ |
| Self-Heating in Air | $\Delta T_{self}$ | — | 0.08 | 0.1 | °C | Still air, TO-92 |

## Temperature Conversion Formula

Converting the raw analog-to-digital converter (ADC) voltage reading ($V_{OUT}$ in Volts) to temperature ($T$ in °C):

$$T\text{ }(^\circ\text{C}) = \frac{V_{OUT}\text{ (in Volts)}}{0.010\text{ V/}^\circ\text{C}} = V_{OUT}\text{ (in mV)} \times 0.1$$

With a 10-bit ADC ($1024$ steps) using a $5.0\text{ V}$ reference voltage ($V_{REF} = 5000\text{ mV}$):

$$T\text{ }(^\circ\text{C}) = \left(\frac{\text{ADC Output} \times 5000\text{ mV}}{1024}\right) \times \frac{1}{10\text{ mV/}^\circ\text{C}} = \frac{\text{ADC Output} \times 500}{1024}$$

## Wiring

| LM35 TO-92 Pin | → | Microcontroller (Arduino Uno / ESP32) |
|---|---|---|
| 1 (`VCC`) | | `5V` (or 4V–30V power supply) |
| 2 (`VOUT`) | | Analog Input Pin `A0` (or ADC input) |
| 3 (`GND`) | | `GND` |

> [!WARNING]
> Minimal Supply Voltage Requirement:
> The LM35 requires a minimum supply voltage of **4.0 V DC**. Powering an LM35 directly from a 3.3V rail will cause reading compression and non-linear errors above $+25^\circ\text{C}$. Use a **TMP36** for native 2.7V–3.3V low-voltage applications.

## Common mistakes

- **Powering from 3.3V rail:** Supplying 3.3V to `VCC` falls below the 4.0 V minimum operating threshold.
- **Reverse polarity connection:** Connecting `VCC` and `GND` backwards causes the LM35 to rapidly overheat and destroy the silicon die within seconds.
- **Measuring sub-zero temperatures without negative bias:** In a basic single-supply circuit ($V_{OUT}$ referenced to GND), the LM35 cannot output negative voltages. To measure temperatures below $0^\circ\text{C}$, connect a pull-down resistor from `VOUT` to a negative voltage rail (or use two diodes).

## Notes

- Using a $1.1\text{ V}$ internal ADC reference voltage on Arduino Uno ($V_{REF} = 1.1\text{ V}$) increases temperature resolution from $0.488\text{ }^\circ\text{C/count}$ to $0.107\text{ }^\circ\text{C/count}$.
