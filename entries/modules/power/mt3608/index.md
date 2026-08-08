## Overview

The **MT3608** is a 6-pin SOT23-6 constant frequency, 6-terminal step-up (boost) DC-DC converter manufactured by Aerosemi. Operating at a high switching frequency of **1.2 MHz**, it allows the use of tiny external inductors and capacitors while achieving up to **97% power efficiency**.

Most commonly sold as a tiny $36\text{ mm} \times 17\text{ mm}$ blue breakout module featuring a 25-turn precision trimmer potentiometer, it takes input voltages from **$2.0\text{V}$ to $24.0\text{V}$** (such as single LiPo cells, 5V USB power, or AA batteries) and steps them up to an adjustable output voltage of up to **$28.0\text{V}$**.

## Quick reference

| | |
|---|---|
| **Input Voltage (`VIN`)** | 2.0 V to 24.0 V DC |
| **Output Voltage (`VOUT`)** | Adjustable from $VIN$ up to 28.0 V DC |
| **Max Peak Switch Current** | 2.0 A |
| **Switching Frequency** | 1.2 MHz fixed |
| **Max Efficiency** | Up to 97% |
| **Feedback Reference Voltage** | 0.6 V ($\pm 2\%$) |
| **Package** | SOT23-6 IC / Breakout Module |

## Pinout & Module Terminals

### SOT23-6 Package IC

```
         ┌───┴───┐
     SW 1│       │6 NC
    GND 2│       │5 IN
     FB 3│       │4 EN
         └───────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `SW` | Power switch node. Connected to inductor and Schottky diode |
| 2 | `GND` | Power ground |
| 3 | `FB` | Feedback pin. Connected to output resistor divider (Reference = 0.6V) |
| 4 | `EN` | Enable pin. High = Active, Low = Shutdown (<1µA current draw) |
| 5 | `IN` | Power supply input pin (2.0V to 24V) |
| 6 | `NC` | Not connected |

### Module Terminals

| Terminal | Function | Description |
|---|---|---|
| `VIN+` | Positive Input | Connect positive voltage supply (e.g. 3.7V LiPo or 5V USB) |
| `VIN-` | Negative Input | Connect ground (GND) |
| `VOUT+` | Positive Output | Stepped-up DC output voltage |
| `VOUT-` | Negative Output | Common ground |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Voltage | $V_{IN}$ | 2.0 | — | 24.0 | V | DC input |
| Output Voltage Range | $V_{OUT}$ | $V_{IN}$ | — | 28.0 | V | Adjustable via FB resistor network |
| Feedback Voltage | $V_{FB}$ | 0.588 | 0.600 | 0.612 | V | $V_{IN} = 5\text{V}$ |
| Switch Current Limit | $I_{SW\_LIM}$ | — | 2.0 | — | A | Peak inductor current limit |
| Switching Frequency | $f_{SW}$ | 1.0 | 1.2 | 1.4 | MHz | Operating frequency |
| Shutdown Current | $I_{SD}$ | — | 0.1 | 1.0 | µA | $V_{EN} = 0\text{V}$ |
| Efficiency | $\eta$ | 90 | 93 | 97 | % | $V_{IN}=5\text{V}, V_{OUT}=12\text{V}, I_{OUT}=0.2\text{A}$ |

## Basic Circuit Diagram (Standalone IC)

```
        Inductor L1 (2.2µH - 10µH)
  VIN ────┬───────███████───────┬───────►|─────┬─────────── VOUT
          │                     │     Schottky │
       [C_IN 22µF]         [Pin 1: SW]  Diode [C_OUT 22µF]
          │                     │              │
         GND               MT3608 IC          R1
                                │              │
                           [Pin 3: FB] ────────┴────[R2]─── GND
```

$$\text{Formula for Output Voltage:} \quad V_{OUT} = 0.6\text{V} \times \left(1 + \frac{R_1}{R_2}\right)$$

## Wiring (Breakout Module)

| MT3608 Module | → | Source / Load | Notes |
|---|---|---|---|
| `VIN+` | | 3.7V LiPo / 5V USB Power | Input DC source |
| `VIN-` | | GND | Input Ground |
| `VOUT+` | | 12V / 24V DC Load | Stepped-up output |
| `VOUT-` | | GND | Output Ground |

## Common mistakes

- **Potentiometer requires multiple turns out of the box:** Fresh MT3608 modules often arrive with the multi-turn potentiometer set to its maximum resistance. When first powered, $V_{OUT}$ will appear identical to $V_{IN}$. Rotate the potentiometer brass screw **10 to 20 full counter-clockwise turns** until the output voltage begins to rise.
- **Attempting to step DOWN voltage:** MT3608 is strictly a **boost** converter. $V_{OUT}$ cannot be set lower than $V_{IN}$. If $V_{IN}$ rises above the set $V_{OUT}$, current flows straight through the inductor and Schottky diode to the output.
- **Exceeding 2A peak switch current:** The 2A limit applies to peak current through the internal MOSFET switch, **not** continuous output load current. Since $P_{IN} \approx P_{OUT}$, output current is limited by:
  $$I_{OUT(max)} \approx I_{IN(max)} \times \frac{V_{IN}}{V_{OUT}} \times \text{Efficiency}$$
  For example, boosting 3.7V to 12V yields a maximum output current of around $500\text{ mA}$.

## Notes

- **MT3608 vs LM2596 / XL6009:** MT3608 operates at 1.2MHz (far higher than LM2596's 150kHz or XL6009's 400kHz), making it much smaller and ideal for battery-powered projects.
