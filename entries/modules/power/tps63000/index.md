## Overview

The **TPS63000** (packaged in 10-pin VSON **TPS63000DRCR**) is a high-efficiency synchronous buck-boost DC-DC converter manufactured by Texas Instruments. Designed for products powered by a single Li-Ion/Li-Po cell, 2-to-3 cell alkaline/NiMH batteries, or USB ports, it regulates output voltage from input supplies ranging from **$1.8\text{ V}$ to $5.5\text{ V}$**.

Utilizing a single $2.2\ \mu\text{H} \dots 4.7\ \mu\text{H}$ inductor, the TPS63000 delivers up to **$1200\text{ mA}$ continuous output current** in buck mode and **$800\text{ mA}$** in boost mode at $3.3\text{ V}$ output with conversion efficiency up to **$96\%$**.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Synchronous Single-Inductor Buck-Boost Converter |
| **Package** | VSON-10 (DRC / $3\times3\text{ mm}$ Exposed Thermal Pad) |
| **Input Voltage Range ($V_{IN}$)** | $1.8\text{ V}$ to $5.5\text{ V}$ DC |
| **Output Voltage Range ($V_{OUT}$)** | $1.2\text{ V}$ to $5.5\text{ V}$ DC (Adjustable) / Fixed 3.3V, 5.0V |
| **Continuous Output Current ($I_{OUT}$)** | $1200\text{ mA}$ (Buck mode) / $800\text{ mA}$ (Boost mode at 3.3V) |
| **Switching Frequency** | $1.5\text{ MHz}$ fixed internal clock |
| **Conversion Efficiency** | Up to $96\%$ |
| **Features** | Power Save mode ($30\ \mu\text{A}$ $I_Q$), over-temperature & over-current protection |

## Pinout (VSON-10 Package)

```
        ┌─────────────┐
   VINA ─│ 1        10 │─ VOUT
    GND ─│ 2         9 │─ FB
     L1 ─│ 3    EP   8 │─ PS
    VIN ─│ 4         7 │─ EN
     L2 ─│ 5         6 │─ PGND
        └─────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `VINA` | Supply input for internal control logic circuitry |
| 2 | `GND` | Control logic ground reference |
| 3 | `L1` | Inductor connection 1 (Switch node for input MOSFETs) |
| 4 | `VIN` | Power stage input supply (+1.8V to +5.5V DC) |
| 5 | `L2` | Inductor connection 2 (Switch node for output MOSFETs) |
| 6 | `PGND` | Power stage ground reference (connected to thermal pad underneath) |
| 7 | `EN` | Enable control pin (>1.2V = Enabled, <0.4V = Disabled) |
| 8 | `PS` / `SYNC` | Power Save mode control pin (GND = Power Save enable, VINA = forced PWM) |
| 9 | `FB` | Voltage feedback sense input pin ($500\text{mV}$ reference) |
| 10 | `VOUT` | Regulated DC output voltage pin |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Voltage Range | $V_{IN}$ | 1.8 | 3.7 | 5.5 | V | Operational input range |
| Feedback Reference Voltage | $V_{FB}$ | 495 | 500 | 505 | mV | $T_A = 25^\circ\text{C}$ |
| Buck Output Current | $I_{OUT\_BUCK}$ | 1200 | — | — | mA | $V_{IN} = 3.6\text{V} \dots 5.5\text{V}, V_{OUT} = 3.3\text{V}$ |
| Boost Output Current | $I_{OUT\_BOOST}$ | 800 | — | — | mA | $V_{IN} = 2.4\text{V}, V_{OUT} = 3.3\text{V}$ |
| Switch Current Limit | $I_{CL}$ | 1700 | 2000 | 2400 | mA | Peak inductor current limit |
| Switching Frequency | $f_{SW}$ | 1.25 | 1.50 | 1.75 | MHz | Internal oscillator |
| Quiescent Current | $I_Q$ | — | 30 | 50 | $\mu\text{A}$ | Power Save mode active |

## Typical Application Circuit (Single Li-Ion Cell to 3.3V Output)

```
       +V_IN (1.8V - 5.5V Li-Ion / USB Input)
          │
       [Pin 4: VIN] ── [Pin 3: L1] ─── [ 2.2µH Inductor ] ─── [Pin 5: L2] ─── TPS63000 ─── [Pin 10: VOUT] ─── +3.3V Output
          │                                                                                     │
       [Pin 6: PGND]                                                                         [ R1 ]
          │                                                                                     │
         GND ───────────────────────────────────────────────────────────────────────────────────┴─── [Pin 9: FB]
                                                                                                │
                                                                                              [ R2 ]
                                                                                                │
                                                                                               GND
```

$$ V_{OUT} = 500\text{mV} \times \left( 1 + \frac{R_1}{R_2} \right) $$

## Common mistakes

- **Separating VINA from VIN without filtering:** Pin 1 (`VINA`) supplies control logic. Connecting `VINA` to noisy high-current `VIN` without an RC filter ($10\ \Omega$ and $1\ \mu\text{F}$) can introduce jitter into the feedback loop.
- **Inadequate Inductor Saturation Rating:** Use an inductor rated for at least $2.0\text{ A}$ continuous saturation current ($I_{SAT}$) to avoid core saturation during maximum load step transients.

## Notes

- **Li-Ion Discharge Advantage:** Provides steady 3.3V power even as a Li-Ion battery drops from 4.2V fully charged down to 2.8V discharged, eliminating the dead zone of standard LDOs or buck-only switchers.
