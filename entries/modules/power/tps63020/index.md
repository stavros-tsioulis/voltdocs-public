## Overview

The **TPS63020** (packaged in a 14-pin VSON **TPS63020DSJR**) is a high-current synchronous buck-boost DC-DC converter manufactured by Texas Instruments. Designed for high-power handheld devices, single-cell Li-Ion battery systems, and USB Type-C power rails, it integrates **4.0 A internal N-channel and P-channel MOSFET switches**.

Operating at a fast **$2.4\text{ MHz}$ switching frequency**, the TPS63020 delivers up to **$3.0\text{ A}$ output current** in buck mode and **$2.0\text{ A}$** in boost mode at $3.3\text{ V}$ output with conversion efficiency up to **$96\%$**, using tiny $1.0\ \mu\text{H} \dots 1.5\ \mu\text{H}$ inductors.

## Quick reference

| | |
|---|---|
| **Regulator Type** | High-Current Synchronous Buck-Boost Converter |
| **Package** | VSON-14 (DSJ / $3\times4\text{ mm}$ Thermal Pad) |
| **Input Voltage Range ($V_{IN}$)** | $1.8\text{ V}$ to $5.5\text{ V}$ DC |
| **Output Voltage Range ($V_{OUT}$)** | $1.2\text{ V}$ to $5.5\text{ V}$ DC (Adjustable) / Fixed 3.3V |
| **Continuous Output Current ($I_{OUT}$)** | $3.0\text{ A}$ (Buck mode) / $2.0\text{ A}$ (Boost mode at 3.3V) |
| **Switching Frequency** | $2.4\text{ MHz}$ fixed internal clock |
| **Conversion Efficiency** | Up to $96\%$ |
| **Protection Features** | Power-Good output (`PG`), Power Save mode, over-temp & short-circuit protection |

## Pinout (VSON-14 Package)

```
        ┌─────────────┐
   VINA ─│ 1        14 │─ VOUT
   GND  ─│ 2        13 │─ FB
    FB  ─│ 3   EP   12 │─ PG
     L1 ─│ 4        11 │─ PS/SYNC
    VIN ─│ 5        10 │─ EN
     L2 ─│ 6         9 │─ PGND
   PGND ─│ 7         8 │─ VOUT
        └─────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `VINA` | Supply input for internal control logic |
| 2 | `GND` | Control logic ground reference |
| 3 | `FB` | Voltage feedback sense input ($500\text{mV}$ internal reference) |
| 4 | `L1` | Inductor switch node 1 (input side) |
| 5 | `VIN` | High-current power stage input (+1.8V to +5.5V) |
| 6 | `L2` | Inductor switch node 2 (output side) |
| 7, 9 | `PGND` | Power stage ground pins (connected to thermal pad) |
| 8, 14| `VOUT` | High-current power stage output pins |
| 10 | `EN` | Enable pin (>1.2V = Enabled, <0.4V = Disabled) |
| 11 | `PS`/`SYNC` | Power Save mode / clock sync pin (GND = Power Save enable, VINA = PWM) |
| 12 | `PG` | Open-drain Power-Good output indicator |
| 13 | `FB` | Feedback connection |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Supply Voltage | $V_{IN}$ | 1.8 | 3.7 | 5.5 | V | Operational input range |
| Feedback Reference Voltage | $V_{FB}$ | 492 | 500 | 508 | mV | $T_A = 25^\circ\text{C}$ |
| Buck Continuous Output Current| $I_{OUT\_BUCK}$ | 3000 | — | — | mA | $V_{IN} = 3.6\text{V} \dots 5.5\text{V}, V_{OUT} = 3.3\text{V}$ |
| Boost Continuous Output Current| $I_{OUT\_BOOST}$ | 2000 | — | — | mA | $V_{IN} = 2.4\text{V}, V_{OUT} = 3.3\text{V}$ |
| Switch Current Limit | $I_{CL}$ | 4000 | 4500 | 5500 | mA | Peak switch current limit |
| Switching Frequency | $f_{SW}$ | 2.0 | 2.4 | 2.8 | MHz | Internal oscillator |
| Quiescent Current | $I_Q$ | — | 35 | 50 | $\mu\text{A}$ | Power Save mode active |

## Typical Application Circuit (High-Current 3.3V Rail)

```
       +V_IN (1.8V - 5.5V High-Current Input)
          │
       [Pin 5: VIN] ── [Pin 4: L1] ─── [ 1.0µH - 1.5µH Inductor ] ─── [Pin 6: L2] ─── TPS63020 ─── [Pin 8/14: VOUT] ─── +3.3V (3A) Output
          │                                                                                             │
       [Pin 7/9: PGND]                                                                               [ R1 ]
          │                                                                                             │
         GND ───────────────────────────────────────────────────────────────────────────────────────────┴─── [Pin 3/13: FB]
                                                                                                        │
                                                                                                      [ R2 ]
                                                                                                        │
                                                                                                       GND
```

$$ V_{OUT} = 500\text{mV} \times \left( 1 + \frac{R_1}{R_2} \right) $$

## Common mistakes

- **Undersized PCB thermal layout for 3A output:** Delivering 3A continuous output creates localized heat. Solder the central thermal pad (`EP`) to multiple PCB ground copper planes with thermal vias.
- **Using high-DCR inductors:** High DC resistance (DCR) in the inductor reduces efficiency significantly at 3A output. Select shielded inductors with $\text{DCR} < 15\ \text{m}\Omega$ and $I_{SAT} > 4.5\text{ A}$.

## Notes

- **TPS63020 vs TPS63000:** The TPS63020 features 4.0A internal switches (vs 2.0A for TPS63000) and operates at $2.4\text{ MHz}$ (vs $1.5\text{ MHz}$), tripling continuous output current capacity.
