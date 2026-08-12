## Overview

The **XL4015** (specifically **XL4015E1** in a 5-lead TO-263 package) is one of the most widely used high-power $5.0\text{ A}$ step-down (buck) DC-DC converter ICs, manufactured by XLSEMI. Famous as the core chip on red/blue 5A buck breakout modules with dual potentiometers for Constant Voltage (CV) and Constant Current (CC) limiting, it converts input voltages from **$8.0\text{ V}$ to $36.0\text{ V}$** down to adjustable output voltages from $1.25\text{ V}$ to $32.0\text{ V}$.

Operating at a **$180\text{ kHz}$ switching frequency**, the XL4015 achieves power conversion efficiencies up to **$96\%$**, generating significantly less heat than legacy LM2596 modules when powering heavy loads like lithium battery charging or high-power LED arrays.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Monolithic High-Current Step-Down (Buck) DC-DC Regulator |
| **Package** | TO-263-5L (D2PAK 5-Pin) / 5A CC/CV Buck Module |
| **Input Voltage Range ($V_{IN}$)** | $8.0\text{ V}$ to $36.0\text{ V}$ DC |
| **Output Voltage Range ($V_{OUT}$)** | $1.25\text{ V}$ to $32.0\text{ V}$ DC (Adjustable) |
| **Continuous Output Current ($I_{OUT}$)** | Up to $5.0\text{ A}$ (Heatsink recommended above 3.5A) |
| **Switching Frequency** | $180\text{ kHz}$ fixed internal oscillator |
| **Conversion Efficiency** | $90\% \dots 96\%$ |
| **Protection Features** | Thermal shutdown, short-circuit protection, internal soft-start |

## Pinout (TO-263-5L Package)

```
        ┌──────────────────┐
        │     XL4015E1     │  (Front Package Face)
        └─┬───┬───┬───┬────┘
          1   2   3   4   5
         GND FB  ON  VIN SW
```

| Pin | Name | Description |
|---|---|---|
| 1 | `GND` | Ground reference (0 V) |
| 2 | `FB` | Voltage feedback sense pin ($1.25\text{V}$ internal reference) |
| 3 | `ON`/`OFF` | Logic shutdown pin (Connect to GND for normal operation, High to shut down) |
| 4 | `VIN` | Unregulated DC power supply input (+8.0V to +36V DC) |
| 5 | `OUTPUT` / `SW` | Switch node output connecting internal MOSFET switch to catch diode & inductor |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Voltage Range | $V_{IN}$ | 8.0 | 12 / 24 | 36 | V | DC input operational range |
| Feedback Reference Voltage | $V_{FB}$ | 1.225 | 1.250 | 1.275 | V | $V_{IN} = 12\text{V}, I_{OUT} = 0.5\text{A}$ |
| Continuous Output Current | $I_{OUT}$ | — | 5.0 | — | A | $V_{IN} - V_{OUT} \ge 1.5\text{V}$ |
| Current Limit Threshold | $I_{CL}$ | 6.0 | 7.0 | — | A | Internal switch peak current limit |
| Switching Frequency | $f_{SW}$ | 144 | 180 | 216 | kHz | Internal clock frequency |
| Quiescent Current | $I_Q$ | — | 2.5 | 5.0 | mA | Operating state ($V_{FB} = 1.5\text{V}$) |

## Typical Application Circuit (CC/CV Module)

```
       +V_IN (8.0V - 36V DC Input)
          │
       [Pin 4: VIN]
        XL4015E1 ──── [Pin 5: SW] ──── [ 47µH Inductor ] ────┬─── +V_OUT Regulated DC Output
          │                                 │                 │
       [Pin 1: GND]               [B540 / SS54 Schottky]   [ R1 ]
          │                                 │                 │
         GND ───────────────────────────────┴─────────────────┼─── [Pin 2: FB]
                                                              │
                                                            [ R2 ]
                                                              │
                                                             GND
```

$$ V_{OUT} = 1.25\text{V} \times \left( 1 + \frac{R_1}{R_2} \right) $$

## Common mistakes

- **Attempting to step UP voltage:** The XL4015 is strictly a **Buck (Step-Down)** converter. $V_{IN}$ must be at least $1.5\text{V}$ higher than $V_{OUT}$.
- **Running at 5A continuous without an external heatsink:** Although rated for 5A peak, drawing more than 3.5A continuous on standard breakout modules without an adhesive aluminum heatsink on the TO-263 package will trigger thermal throttling.

## Notes

- **XL4015 vs LM2596:** The XL4015 delivers up to 5A (vs 3A for LM2596) at higher switching frequency ($180\text{ kHz}$ vs $150\text{ kHz}$) and efficiency up to 96%.
