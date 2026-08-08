## Overview

The **XL6009** (XL6009E1) is a 4A 400kHz 60V step-up (boost) DC-DC converter manufactured by XLSEMI. Designed with a high-power internal N-channel MOSFET switch and current-mode control architecture, it serves as the modern replacement for the older LM2577 boost regulator IC.

Widely sold as a medium-to-high power adjustable DC-DC step-up module, it accepts input voltages between **$5.0\text{V}$ and $32.0\text{V}$** and delivers an adjustable boosted output voltage of **$5.0\text{V}$ to $38.0\text{V}$** with up to **94% conversion efficiency**.

## Quick reference

| | |
|---|---|
| **Input Voltage (`VIN`)** | 5.0 V to 32.0 V DC |
| **Output Voltage (`VOUT`)** | Adjustable from 5.0 V to 38.0 V DC |
| **Internal Switch Current Limit** | 4.0 A peak |
| **Switching Frequency** | 400 kHz fixed |
| **Max Efficiency** | Up to 94% |
| **Feedback Reference Voltage** | 1.25 V ($\pm 1.5\%$) |
| **Package** | TO-263-5L (D2PAK) / Breakout Module |

## Pinout & Module Terminals

### TO-263-5L Package IC

```
         ┌───┴───┐
     GND 1│       │
      EN 2│       │
      SW 3│XL6009 │ (Tab connected to SW)
      FB 4│       │
     VIN 5│       │
         └───────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `GND` | Ground reference pin |
| 2 | `EN` | Enable pin. High (or floating) = Active; Low = Shutdown |
| 3 | `SW` | Power switch output pin (internal N-MOSFET drain) |
| 4 | `FB` | Feedback pin (VFB = 1.25V) |
| 5 | `VIN` | Supply power input pin (5V to 32V) |

### Module Terminals

| Terminal | Function | Description |
|---|---|---|
| `IN+` | Positive Input | Positive DC supply rail (+5V to +32V) |
| `IN-` | Negative Input | System ground (GND) |
| `OUT+` | Positive Output | Boosted DC output rail (+5V to +38V) |
| `OUT-` | Negative Output | System ground (GND) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Voltage | $V_{IN}$ | 5.0 | — | 32.0 | V | DC |
| Output Voltage | $V_{OUT}$ | 5.0 | — | 38.0 | V | Adjustable |
| Switch Current Limit | $I_{SW}$ | — | 4.0 | — | A | Peak inductor switch current |
| Switching Frequency | $f_{OSC}$ | 320 | 400 | 480 | kHz | Operating frequency |
| Feedback Voltage | $V_{FB}$ | 1.231 | 1.250 | 1.269 | V | $V_{IN} = 12\text{V}$ |
| Quiescent Current | $I_q$ | — | 7.5 | 10.0 | mA | $V_{FB} = 2\text{V}$ |
| Max Efficiency | $\eta$ | — | 92 | 94 | % | $V_{IN}=12\text{V}, V_{OUT}=18\text{V}, I_{OUT}=1\text{A}$ |

## Basic Circuit Diagram (Standalone IC)

```
        Inductor L1 (33µH - 47µH)
  VIN ────┬───────███████───────┬───────►|─────┬─────────── VOUT
          │                     │     Schottky │
       [C_IN 47µF]         [Pin 3: SW]  Diode [C_OUT 220µF]
          │                     │   (SS34/SS54)│
         GND                XL6009             R1
                                │              │
                           [Pin 4: FB] ────────┴────[R2]─── GND
```

$$\text{Formula for Output Voltage:} \quad V_{OUT} = 1.25\text{V} \times \left(1 + \frac{R_1}{R_2}\right)$$

## Wiring (Breakout Module)

| XL6009 Module | → | Source / Load | Notes |
|---|---|---|---|
| `IN+` | | 12V Solar Panel / Battery | Input DC voltage |
| `IN-` | | GND | Input Ground |
| `OUT+` | | 24V Motor / LED Panel | Stepped-up output |
| `OUT-` | | GND | Output Ground |

## Common mistakes

- **Operating continuously above 2.5A without cooling:** Although rated for 4A peak switch current, continuous output operation above 2.5A creates significant heat in the TO-263 IC and inductor. Add an external heatsink or cooling fan for sustained high-current loads.
- **Forgetting input polarity protection:** Cheap XL6009 breakout modules lack input reverse polarity protection. Connecting $IN+$ and $IN-$ backwards will instantly destroy the XL6009 IC.
- **Output capacitor voltage rating:** When boosting to high output voltages ($24\text{V} \dots 35\text{V}$), ensure the output electrolytic filter capacitor is rated for at least **50V** to avoid dielectric failure.

## Notes

- **XL6009 vs LM2577 vs MT3608:** XL6009 switches at 400kHz (vs LM2577's 52kHz), allowing smaller inductors and higher efficiency. MT3608 is better suited for smaller <2A portable battery projects, while XL6009 handles higher power requirements up to 4A.
