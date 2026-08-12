## Overview

The **TPS54331** (commonly supplied in 8-pin SOIC **TPS54331DR**) is a $3.0\text{ A}$ step-down (buck) switching regulator from Texas Instruments. Featuring an integrated $80\text{ m}\Omega$ high-side N-channel MOSFET, it operates across an input voltage range of **$3.5\text{ V}$ to $28.0\text{ V}$** and regulates output voltage down to $0.8\text{ V}$.

To maximize efficiency across all load conditions, the TPS54331 features **Eco-mode™ pulse skipping**, which automatically reduces switching frequency under light loads (such as standby MCU modes) to maintain high efficiency down to milliamp currents.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Eco-mode™ Step-Down (Buck) DC-DC Converter |
| **Package** | SOIC-8 (D) / SO PowerPAD-8 (DDA) |
| **Input Voltage Range ($V_{IN}$)** | $3.5\text{ V}$ to $28.0\text{ V}$ DC |
| **Output Voltage Range ($V_{OUT}$)** | $0.8\text{ V}$ to $25.0\text{ V}$ DC (Adjustable) |
| **Continuous Output Current ($I_{OUT}$)** | Up to $3.0\text{ A}$ |
| **Switching Frequency** | $570\text{ kHz}$ fixed internal oscillator |
| **Conversion Efficiency** | $88\% \dots 92\%$ (with light-load pulse skipping) |
| **Features** | Adjustable soft-start (`SS`), precision UVLO enable (`EN`), Eco-mode |

## Pinout (SOIC-8 / SO PowerPAD-8)

```
        ┌─────────────┐
   BOOT ─│ 1         8 │─ PH
    VIN ─│ 2         7 │─ GND
     EN ─│ 3    EP   6 │─ COMP
     SS ─│ 4         5 │─ VSENSE
        └─────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `BOOT` | Bootstrap capacitor connection to PH ($0.1\ \mu\text{F}$ cap) for high-side gate drive |
| 2 | `VIN` | Unregulated DC input voltage (+3.5V to +28V DC) |
| 3 | `EN` | Enable control input pin with internal precision threshold for UVLO tuning |
| 4 | `SS` | Soft-start programming pin (capacitor to GND sets soft-start ramp time) |
| 5 | `VSENSE` | Voltage sense feedback input ($0.8\text{V}$ internal reference) |
| 6 | `COMP` | Error amplifier output pin for external loop frequency compensation |
| 7 | `GND` | Ground reference pin |
| 8 | `PH` | Phase / Switch node output connected to internal high-side MOSFET drain |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Voltage Range | $V_{IN}$ | 3.5 | 12 | 28 | V | Operating range |
| Feedback Reference Volts | $V_{REF}$ | 0.784 | 0.800 | 0.816 | V | $T_J = 25^\circ\text{C}$ |
| Continuous Output Current | $I_{OUT}$ | — | 3.0 | — | A | $V_{IN} = 12\text{V}, V_{OUT} = 3.3\text{V}$ |
| Switch On-Resistance | $R_{DS(ON)}$ | — | 80 | 135 | $\text{m}\Omega$ | $V_{BOOT} - V_{PH} = 6\text{V}$ |
| Switching Frequency | $f_{SW}$ | 450 | 570 | 690 | kHz | Internal clock |
| Quiescent Current | $I_Q$ | — | 110 | 160 | $\mu\text{A}$ | Non-switching Eco-mode state |
| Shutdown Current | $I_{SD}$ | — | 1.0 | 2.5 | $\mu\text{A}$ | $V_{EN} = 0\text{V}$ |

## Typical Application Circuit

```
       +V_IN (3.5V - 28V DC Input)
          │
       [Pin 2: VIN]
        TPS54331DR ──── [Pin 8: PH] ──── [ 6.8µH - 10µH Inductor ] ──┬─── +V_OUT Regulated DC Output
          │                                   │                       │
       [Pin 7: GND]                [B340A Schottky Diode]          [ R1 ]
          │                                   │                       │
         GND ─────────────────────────────────┴───────────────────────┼─── [Pin 5: VSENSE]
                                                                      │
                                                                    [ R2 ]
                                                                      │
                                                                     GND
```

$$ V_{OUT} = 0.8\text{V} \times \left( 1 + \frac{R_1}{R_2} \right) $$

## Common mistakes

- **Floating the SS pin:** Leaving `SS` floating results in instantaneous startup current spikes. Always connect a small ceramic capacitor (e.g., 10nF) between `SS` and `GND` for smooth soft-start output ramp.
- **Incorrect COMP component values:** The TPS54331 relies on external RC compensation on the `COMP` pin (Pin 6). Leaving `COMP` unconnected or using arbitrary RC values can cause control loop instability or output ripple.

## Notes

- **Eco-mode Advantage:** Unlike standard buck switchers that consume 3–5mA idling, the TPS54331 drops quiescent current to ~110µA under light load, making it ideal for battery-backed systems.
