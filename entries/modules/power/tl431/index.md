## Overview

The TL431 is a three-terminal adjustable precision shunt regulator IC originally designed by Texas Instruments and second-sourced by virtually every major semiconductor manufacturer. Acting as a programmable Zener diode with temperature stability across its operating temperature range, its output voltage can be set to any value between `VREF` (approximately 2.495 V) and 36 V using two external resistors.

With a low typical dynamic output impedance of 0.2 Ω and a sharp turn-on characteristic, the TL431 is an indispensable building block in power supply design. It is widely used as a voltage reference in precision analog circuits, an error amplifier in isolated switch-mode power supplies (SMPS) feedback loops (paired with an optocoupler), a voltage monitor, and a precision current source.

## Quick reference

| | |
|---|---|
| **Function** | Adjustable Precision Shunt Regulator / Voltage Reference |
| **Reference Voltage (`VREF`)** | 2.495 V (Typ) |
| **Output Voltage Range (`VKA`)**| `VREF` (2.495 V) to 36.0 V |
| **Cathode Operating Current (`IK`)**| 1.0 mA to 100 mA |
| **Dynamic Output Impedance** | 0.2 Ω (Typ) |
| **Tolerance Grades** | Standard (2.0%), A-Grade (1.0%), B-Grade (0.5%) |
| **Packages** | TO-92 (TO-226AA), SOT-23 (3-pin), SOIC-8 |

## Pin configuration

| Pin (TO-92) | Name | Type | Description |
|---|---|---|---|
| 1 | `REF` | Input | Voltage Reference Input pin (2.495V feedback threshold) |
| 2 | `ANODE` | Power | Anode terminal (ground reference / negative terminal) |
| 3 | `CATHODE` | Power | Cathode terminal (positive shunt regulator output) |

> [!INFO] Pinout Warning: SOT-23 packages have different pin orderings depending on vendor (e.g., TL431 vs TL431A vs TL431B or DBZ suffix). Always check the specific datasheet diagram before laying out PCBs.

## Functional description

The TL431 contains an internal 2.495 V temperature-compensated voltage reference, an operational amplifier, and a high-current NPN transistor connected between Cathode and Anode.

When the voltage applied to the `REF` pin exceeds `VREF` (2.495 V), the internal op-amp turns on the output NPN transistor, causing current to flow from Cathode to Anode and pulling down `VKA`. In a closed-loop feedback network using a voltage divider ($R1$ and $R2$), the output voltage $V_{KA}$ is held stable at:

$$V_{KA} = V_{\text{REF}} \times \left(1 + \frac{R1}{R2}\right) + I_{\text{REF}} \times R1$$

Since $I_{\text{REF}}$ is typically around 2 µA, the second term is negligible for reasonable resistor values ($R1 < 100\,\text{k}\Omega$), simplifying the formula to:

$$V_{KA} \approx 2.495\,\text{V} \times \left(1 + \frac{R1}{R2}\right)$$

## Absolute maximum ratings

> [!WARNING] Stresses beyond these values cause permanent damage. Limits, not operating conditions.

| Parameter | Rating | Unit |
|---|---|---|
| Cathode Voltage (`VKA`) | 37 | V |
| Continuous Cathode Current (`IK`) | -100 to +150 | mA |
| Reference Input Current (`IREF`) | -0.05 to +10 | mA |
| Operating Junction Temperature (`TJ`) | 150 | °C |
| Storage Temperature Range | -65 to +150 | °C |

## Electrical characteristics

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Reference Input Voltage | `VREF` | 2.470 | 2.495 | 2.520 | V | `VKA` = `VREF`, `IK` = 10 mA, TA = 25°C (Standard Grade) |
| Deviation of `VREF` over Temp | `VI(dev)` | — | 4.5 | 17 | mV | `VKA` = `VREF`, `IK` = 10 mA, 0°C to 70°C |
| Ratio of `VREF` Delta to `VKA` | `ΔVREF / ΔVKA` | — | -1.4 | -2.7 | mV/V | `IK` = 10 mA, `VKA` = `VREF` to 36V |
| Reference Input Current | `IREF` | — | 1.5 | 4.0 | µA | `IK` = 10 mA, `R1` = 10 kΩ, `R2` = ∞ |
| Minimum Cathode Current | `IMIN` | — | 0.4 | 1.0 | mA | `VKA` = `VREF` |
| Dynamic Output Impedance | `|ZKA|` | — | 0.2 | 0.5 | Ω | `VKA` = `VREF`, `f` < 1 kHz, `IK` = 1 mA to 100 mA |

## Typical application

### Adjustable 5.0 V Voltage Reference Circuit

```
       +12V Unregulated Input
                 |
               [ R_LIMIT (470 ohm) ]
                 |
                 +--------------------> +5.0V Regulated Output (V_KA)
                 |
                 +----+
                 |    |
               [R1] (10k)
                 |    |
  Ref Pin (1) <--+    |
                 |    | (Cathode, Pin 3)
               [R2]  [ TL431 ]
              (10k)   | (Anode, Pin 2)
                 |    |
                GND  GND
```

Using $R1 = 10\,\text{k}\Omega$ and $R2 = 10\,\text{k}\Omega$:

$$V_{KA} = 2.495\,\text{V} \times \left(1 + \frac{10\,\text{k}}{10\,\text{k}}\right) = 4.99\,\text{V} \approx 5.0\,\text{V}$$

## Common mistakes

- **Cathode Current Below 1.0 mA:** If `IK` drops below 1 mA, the internal reference and op-amp will not fully turn on, leading to poor regulation and out-of-spec output voltage. Ensure $R_{\text{LIMIT}}$ supplies at least 1 mA to 2 mA under maximum load.
- **Unstable Capacitive Load (Oscillation):** Connecting capacitive loads directly across Cathode and Anode can cause self-oscillation. Check the datasheet "Stability Boundary Conditions" chart; values below 1 nF or above 10 µF are generally stable, while 10 nF to 2.2 µF can cause instability depending on $V_{KA}$ and $I_K$.
- **Ignoring $R1$ / $R2$ Current:** Using extremely high resistor values ($R1 > 500\,\text{k}\Omega$) causes the 2 µA $I_{\text{REF}}$ input bias current to introduce significant setpoint error.

## Notes & further reading

- SMPS Isolation: In switch-mode power supplies (e.g. flyback converters), the TL431 is placed on the secondary side driving an optocoupler LED to provide galvanically isolated voltage feedback to the primary PWM controller.
- Equivalent Parts: LM431, NCV431, AS431, AP431.
