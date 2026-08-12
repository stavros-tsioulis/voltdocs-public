## Overview

The **XL4005** (specifically **XL4005E1** in a 5-lead TO-263 package) is a high-current $5.0\text{ A}$ step-down (buck) DC-DC switching regulator manufactured by XLSEMI. Integrating a high-side N-channel power MOSFET switch, it operates over an input voltage range of **$5.0\text{ V}$ to $32.0\text{ V}$** and regulates output voltage down to $0.8\text{ V}$.

Operating at a fixed switching frequency of **$300\text{ kHz}$**, the XL4005 achieves high power conversion efficiency (up to **$95\%$**) while minimizing external inductor size compared to legacy 150kHz buck switchers.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Monolithic High-Current Step-Down (Buck) Regulator |
| **Package** | TO-263-5L (D2PAK 5-Lead) / 5A Buck Module |
| **Input Voltage Range ($V_{IN}$)** | $5.0\text{ V}$ to $32.0\text{ V}$ DC |
| **Output Voltage Range ($V_{OUT}$)** | $0.8\text{ V}$ to $30.0\text{ V}$ DC (Adjustable) |
| **Continuous Output Current ($I_{OUT}$)** | Up to $5.0\text{ A}$ (with adequate heatsinking) |
| **Switching Frequency** | $300\text{ kHz}$ fixed internal clock |
| **Conversion Efficiency** | $90\% \dots 95\%$ |
| **Protection Features** | Thermal shutdown, short-circuit current limit, internal soft-start |

## Pinout (TO-263-5L Package)

```
        ┌──────────────────┐
        │     XL4005E1     │  (Front Package Face)
        └─┬───┬───┬───┬────┘
          1   2   3   4   5
         GND FB  VC  VIN SW
```

| Pin | Name | Description |
|---|---|---|
| 1 | `GND` | Ground reference (0 V) |
| 2 | `FB` | Voltage feedback sense pin ($0.8\text{V}$ internal reference voltage) |
| 3 | `VC` / `COMP` | Error amplifier compensation pin for control loop frequency stabilization |
| 4 | `VIN` | Unregulated DC power supply input pin (+5.0V to +32V DC) |
| 5 | `OUTPUT` / `SW` | Switch node output connecting internal MOSFET to Schottky diode & inductor |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Voltage Range | $V_{IN}$ | 5.0 | 12 / 24 | 32 | V | DC input operational range |
| Feedback Reference Voltage | $V_{FB}$ | 0.784 | 0.800 | 0.816 | V | $V_{IN} = 12\text{V}, I_{OUT} = 0.5\text{A}$ |
| Continuous Output Current | $I_{OUT}$ | — | 5.0 | — | A | $V_{IN} - V_{OUT} \ge 2.0\text{V}$ |
| Current Limit Threshold | $I_{CL}$ | 6.0 | 7.0 | — | A | Internal switch peak current limit |
| Switching Frequency | $f_{SW}$ | 240 | 300 | 360 | kHz | Internal oscillator frequency |
| Quiescent Current | $I_Q$ | — | 3.0 | 5.0 | mA | Operating state ($V_{FB} = 1.0\text{V}$) |

## Typical Application Circuit

```
       +V_IN (5.0V - 32V DC Input)
          │
       [Pin 4: VIN]
        XL4005E1 ──── [Pin 5: SW] ──── [ 33µH - 47µH Inductor ] ───┬─── +V_OUT Regulated DC Output
          │                                  │                     │
       [Pin 1: GND]               [B540 / SS54 Schottky Diode]  [ R1 ]
          │                                  │                     │
         GND ────────────────────────────────┴─────────────────────┼─── [Pin 2: FB]
                                                                   │
                                                                 [ R2 ]
                                                                   │
                                                                  GND
```

$$ V_{OUT} = 0.8\text{V} \times \left( 1 + \frac{R_1}{R_2} \right) $$

## Common mistakes

- **Exceeding the 32V input limit:** The XL4005 maximum input rating is $32\text{ V}$. Operating near or above 32V (such as raw 24V AC transformer rectifications without clamping) can destroy the internal switch.
- **Using thin PCB traces for 5A current paths:** Drawing 5A continuous requires wide copper traces or copper pours on `VIN`, `SW`, `GND`, and `VOUT` lines to prevent resistive voltage drops and thermal buildup.

## Notes

- **XL4005 vs XL4015:** XL4005 operates at $300\text{ kHz}$ with a $0.8\text{V}$ feedback reference; XL4015 operates at $180\text{ kHz}$ with a $1.25\text{V}$ feedback reference.
