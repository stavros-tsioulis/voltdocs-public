## Overview

The **TPS5430** (packaged in 8-pin SO PowerPAD **TPS5430DDA**) is a $3.0\text{ A}$ continuous ($4.0\text{ A}$ peak) step-down (buck) DC-DC converter from Texas Instruments' **Swift™** family. Featuring an integrated $110\text{ m}\Omega$ high-side N-channel MOSFET switch, it operates over a wide input voltage range from **$5.5\text{ V}$ to $36.0\text{ V}$** and regulates output down to $1.221\text{ V}$.

With a fixed internal switching frequency of **$500\text{ kHz}$**, the TPS5430 provides high power density and fast transient response with minimal external component size, serving as a high-performance alternative to legacy 150kHz regulators like the LM2596.

## Quick reference

| | |
|---|---|
| **Regulator Type** | High-Efficiency Step-Down (Buck) DC-DC Converter |
| **Package** | SO PowerPAD-8 (DDA / 8-Pin SOIC with Thermal Pad) |
| **Input Voltage Range ($V_{IN}$)** | $5.5\text{ V}$ to $36.0\text{ V}$ DC |
| **Output Voltage Range ($V_{OUT}$)** | $1.221\text{ V}$ to $32.0\text{ V}$ DC (Adjustable) |
| **Continuous Output Current ($I_{OUT}$)** | Up to $3.0\text{ A}$ ($4.0\text{ A}$ peak current) |
| **Switching Frequency** | $500\text{ kHz}$ fixed internal clock |
| **Conversion Efficiency** | Up to $95\%$ |
| **Features** | Internal slope compensation, thermal shutdown, enable threshold |

## Pinout (SO PowerPAD-8 Package)

```
        ┌─────────────┐
   BOOT ─│ 1         8 │─ PH
     NC ─│ 2         7 │─ VIN
     NC ─│ 3    EP   6 │─ GND
 VSENSE ─│ 4         5 │─ ENA
        └─────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `BOOT` | Bootstrap cap connection to PH ($0.01\ \mu\text{F}$ / 10nF cap) for high-side gate drive |
| 2 | `NC` | No internal connection |
| 3 | `NC` | No internal connection |
| 4 | `VSENSE` | Feedback voltage sense input pin ($1.221\text{V}$ internal reference) |
| 5 | `ENA` | Enable input (>1.3V enables converter, <0.5V disables, floating = enabled) |
| 6 | `GND` | Ground reference (internally connected to thermal PowerPAD) |
| 7 | `VIN` | Unregulated DC power supply input (+5.5V to +36V DC) |
| 8 | `PH` | Phase / Switch node output connected to internal MOSFET drain |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Voltage Range | $V_{IN}$ | 5.5 | 12 / 24 | 36 | V | Operating range |
| Feedback Reference Voltage | $V_{REF}$ | 1.197 | 1.221 | 1.245 | V | $T_J = -40^\circ\text{C} \dots 125^\circ\text{C}$ |
| Continuous Output Current | $I_{OUT}$ | — | 3.0 | — | A | $V_{IN} = 12\text{V}, V_{OUT} = 5\text{V}$ |
| Switch On-Resistance | $R_{DS(ON)}$ | — | 110 | 180 | $\text{m}\Omega$ | $V_{BOOT} - V_{PH} = 6\text{V}$ |
| Switching Frequency | $f_{SW}$ | 400 | 500 | 600 | kHz | Internal oscillator |
| Quiescent Current | $I_Q$ | — | 3.0 | 4.4 | mA | Non-switching state |
| Shutdown Current | $I_{SD}$ | — | 18 | 40 | $\mu\text{A}$ | $V_{ENA} = 0\text{V}$ |

## Typical Application Circuit

```
       +V_IN (5.5V - 36V DC Input)
          │
       [Pin 7: VIN]
        TPS5430DDA ──── [Pin 8: PH] ──── [ 15µH Inductor ] ───┬─── +V_OUT Regulated DC Output
          │                                  │                │
       [Pin 6: GND]               [B340A Schottky Diode]   [ R1 = 10kΩ ]
          │                                  │                │
         GND ────────────────────────────────┴────────────────┼─── [Pin 4: VSENSE]
                                                              │
                                                            [ R2 ]
                                                              │
                                                             GND
```

$$ V_{OUT} = 1.221\text{V} \times \left( 1 + \frac{R_1}{R_2} \right) $$

## Common mistakes

- **Failing to solder the exposed PowerPAD:** The bottom thermal pad of the SO PowerPAD-8 package must be soldered directly to a PCB ground plane with thermal vias. Failure to do so reduces thermal dissipation drastically, triggering thermal shutdown under load.
- **Improper Bootstrap capacitor voltage rating:** A $10\text{ nF}$ ceramic capacitor is required between `BOOT` and `PH`. Using a capacitor with low voltage rating or wrong dielectric (use X7R/X5R) can fail high-side gate driving.

## Notes

- **TPS5430 vs LM2596:** The TPS5430 operates at $500\text{ kHz}$ (3x faster than LM2596's $150\text{ kHz}$), allowing much smaller $15\ \mu\text{H}$ inductors while handling up to 36V inputs.
