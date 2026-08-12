## Overview

The **ADP1613** (ADP1613ARMZ-R7) is a step-up (boost) DC-DC converter IC manufactured by Analog Devices. Packaged in a subminiature **8-lead MSOP enclosure**, it integrates a **2.0A power switch** to deliver output voltages up to **$20\text{ Volts}$** from a single $2.5\text{V} \dots 5.5\text{V}$ DC supply or 5V USB power rail.

Operating at a selectable pin-programmable switching frequency of **650 kHz or 1.3 MHz**, the ADP1613 allows tiny surface-mount inductors and ceramic capacitors. It is widely used in LCD bias supplies, sensor rail generation ($12\text{V} / 15\text{V}$ from 3.3V/5V), and portable instrumentation.

## Quick reference

| | |
|---|---|
| **Input Voltage (`VIN`)** | 2.5 V to 5.5 V DC |
| **Output Voltage Range** | Adjustable up to $20.0\text{ V}$ DC |
| **Internal Power Switch** | $2.0\text{ A}$ continuous switch current limit |
| **Switching Frequency** | Pin selectable $650\text{ kHz}$ (`FREQ` = GND) or $1.3\text{ MHz}$ (`FREQ` = VIN) |
| **Feedback Reference Voltage** | $1.235\text{ V}$ reference |
| **Quiescent Current** | $2.2\text{ mA}$ operating ($< 1\ \mu\text{A}$ in shutdown) |
| **Package** | 8-lead MSOP |

## Pinout (MSOP-8 Package)

```
             ┌───┴───┐
        COMP 1│ 1   8 │ VIN (+2.5V to +5.5V)
          FB 2│       │ 7 FREQ (Frequency Select)
          EN 3│ADP1613│ 6 NC
         GND 4│       │ 5 SW (Switch Output 20V)
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `COMP` | Output | Error Amplifier Output (Connect RC compensation network to GND) |
| 2 | `FB` | Input | Feedback Voltage Sense Input ($1.235\text{V}$ reference to GND) |
| 3 | `EN` | Input | Active-HIGH Enable Input (High = Enable; Low = Shutdown $< 1\mu\text{A}$) |
| 4 | `GND` | Power | Ground Reference (0 V) |
| 5 | `SW` | Output | Internal 2.0A Power Switch Drain Output |
| 6 | `NC` | Unused | No Internal Connection |
| 7 | `FREQ` | Input | Frequency Select (GND = 650 kHz; VIN = 1.3 MHz) |
| 8 | `VIN` | Power | Power Supply Input (+2.5V to +5.5V DC) |

## Output Voltage Formula

$$ V_{OUT} = 1.235\text{V} \times \left(1 + \frac{R_1}{R_2}\right) $$

Where $R_1$ is connected between $V_{OUT}$ and `FB`, and $R_2$ is connected between `FB` and `GND`.

## Common mistakes

- **Leaving `FREQ` (Pin 7) floating:** Pin 7 selects the switching frequency. Leaving `FREQ` floating causes switching frequency instability. Tie to **GND** for 650 kHz or to **`VIN`** for 1.3 MHz.
- **Operating without low-ESR ceramic input/output capacitors:** Use $10\ \mu\text{F} \dots 22\ \mu\text{F}$ X5R or X7R ceramic capacitors directly at the `VIN` and `VOUT` pins.

## Notes

- **ADP1613 vs ADP1612:** ADP1613 has a 2.0A switch; ADP1612 is a lower-current 1.4A switch version in the same MSOP-8 footprint.
