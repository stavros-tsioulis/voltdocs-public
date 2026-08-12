## Overview

The **LM2577** (LM2577T-ADJ / LM2577S-ADJ) is a 3A step-up (boost) voltage regulator IC belonging to Texas Instruments' iconic **SIMPLE SWITCHER** family. It is the step-up counterpart to the ubiquitous LM2596 buck regulator, widely featured on red and green adjustable DC-DC step-up power supply modules across AliExpress, Amazon, and eBay.

Operating over an input voltage range of **3.5V to 40.0V DC**, the LM2577 incorporates an internal **3.0A NPN power switch** rated for up to **60V DC output**, a 52 kHz internal oscillator, soft-start circuitry, and thermal shutdown protection.

## Quick reference

| | |
|---|---|
| **Input Supply Voltage (`VIN`)** | 3.5 V to 40.0 V DC |
| **Output Voltage Limit (`VOUT`)**| Up to $60.0\text{ V}$ DC (Internal switch rated for 65V breakdown) |
| **Internal Switch Current** | $3.0\text{ A}$ continuous switch limit |
| **Switching Frequency** | $52\text{ kHz}$ internal fixed oscillator |
| **Feedback Voltage (`VFB`)** | $1.23\text{ V}$ reference |
| **Available Versions** | Fixed 12V (`LM2577-12`), Fixed 15V (`LM2577-15`), Adjustable (`LM2577-ADJ`) |
| **Package** | TO-220-5 (Through-hole) / TO-263-5 DDPAK (SMD) |

## Pinout (TO-220-5 Package)

Looking at the **front labeled face** of the 5-lead package with leads pointing down:

```
        ┌─────────────┐
        │   O   [TAB] │  (Metal Mounting Tab = GROUND / GND)
        ├─────────────┤
        │   LM2577T   │  (Front Package Face)
        └─┬─┬─┬─┬─┬───┘
          1 2 3 4 5
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `COMP` | Input | Frequency Compensation Input (Connect $R_C + C_C$ network to GND) |
| 2 | `FB` | Input | Feedback Voltage Sense Input ($1.23\text{V}$ reference to GND) |
| 3 | `GND` | Power | Ground Reference (0 V; Connected internally to Metal Tab!) |
| 4 | `SW` | Output | Internal NPN Power Switch Collector Output (Connect to Inductor & Schottky Diode) |
| 5 | `VIN` | Power | Unregulated Supply Input (+3.5V to +40V DC) |

## Output Voltage Formula (Adjustable Version)

The output voltage ($V_{OUT}$) is set by resistor divider $R_1$ (between `VOUT` and `FB`) and $R_2$ (between `FB` and `GND`):

$$ V_{OUT} = 1.23\text{V} \times \left(1 + \frac{R_1}{R_2}\right) $$

$$\text{For } R_2 = 1.0\text{ k}\Omega \text{ and } R_1 = 8.76\text{ k}\Omega \implies V_{OUT} = 12.0\text{ Volts}.$$

## Common mistakes

- **Attempting to step-down ($V_{IN} > V_{OUT}$):** The LM2577 is a **boost (step-up)** converter. Current flows from $V_{IN}$ through the inductor and Schottky diode directly to $V_{OUT}$ even when the IC is idle. If $V_{IN}$ exceeds $V_{OUT}$, the output voltage will equal $V_{IN} - 0.5\text{V}$.
- **Omitting the compensation RC network on `COMP` (Pin 1):** Unlike buck regulators, boost converters require loop compensation ($R_C \approx 2.0\text{ k}\Omega$ and $C_C \approx 0.47\ \mu\text{F}$) on Pin 1 to maintain loop stability.

## Notes

- **LM2577 vs XL6009 vs LM2596:** LM2577 is a 52kHz 3A boost regulator; XL6009 is a 400kHz 4A modern boost replacement; LM2596 is a 150kHz 3A step-down (buck) regulator.
