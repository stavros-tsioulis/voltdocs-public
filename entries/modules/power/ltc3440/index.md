## Overview

The **LTC3440** (commonly packaged in 8-pin MSOP **LTC3440EMS8**) is a high-efficiency $600\text{ mA}$ synchronous buck-boost DC-DC converter manufactured by Analog Devices (originally Linear Technology). Operating over an input voltage range of **$2.5\text{ V}$ to $5.5\text{ V}$**, it seamlessly maintains a fixed output voltage (such as $3.3\text{ V}$) regardless of whether the input voltage is higher, lower, or equal to the output voltage.

Integrating four internal low-$R_{DS(ON)}$ N-channel and P-channel MOSFET switches, the LTC3440 eliminates external Schottky diodes and achieves conversion efficiency up to **$96\%$**. Its programmable switching frequency ($300\text{ kHz}$ to $2.0\text{ MHz}$) makes it ideal for single-cell Li-Ion or multi-cell alkaline battery powered electronics.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Synchronous Buck-Boost DC-DC Converter |
| **Package** | MSOP-8 / 10-Lead DFN ($3\times3\text{ mm}$) |
| **Input Voltage Range ($V_{IN}$)** | $2.5\text{ V}$ to $5.5\text{ V}$ DC |
| **Output Voltage Range ($V_{OUT}$)** | $2.5\text{ V}$ to $5.5\text{ V}$ DC (Adjustable) |
| **Continuous Output Current ($I_{OUT}$)** | Up to $600\text{ mA}$ ($V_{IN} \ge 2.7\text{V}$) |
| **Switching Frequency** | Programmable $300\text{ kHz} \dots 2.0\text{ MHz}$ |
| **Conversion Efficiency** | Up to $96\%$ |
| **Operating Modes** | Burst Mode® operation ($25\ \mu\text{A}$ $I_Q$), Fixed Frequency PWM |

## Pinout (MSOP-8 Package)

```
        ┌─────────────┐
   SW1 ─│ 1         8 │─ Rt/SYNC
   VIN ─│ 2         7 │─ SHDN/MODE
   GND ─│ 3         6 │─ FB
   SW2 ─│ 4         5 │─ VOUT
        └─────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `SW1` | Switch node 1 connecting internal switches A & B to inductor terminal 1 |
| 2 | `VIN` | Power supply input voltage (+2.5V to +5.5V DC) |
| 3 | `GND` | Ground reference (0 V) |
| 4 | `SW2` | Switch node 2 connecting internal switches C & D to inductor terminal 2 |
| 5 | `VOUT` | Regulated DC output voltage pin |
| 6 | `FB` | Voltage feedback sense input ($1.22\text{V}$ reference) |
| 7 | `SHDN`/`MODE` | Shutdown & mode selection pin (Low = Shutdown, High = PWM, Mid-voltage = Burst Mode) |
| 8 | `Rt` / `SYNC` | Frequency setting resistor pin (resistor to GND sets $f_{SW}$ or external clock sync) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Supply Voltage | $V_{IN}$ | 2.5 | 3.7 | 5.5 | V | Single Li-Ion / battery input |
| Feedback Reference Voltage | $V_{FB}$ | 1.196 | 1.220 | 1.244 | V | $T_A = 25^\circ\text{C}$ |
| Output Current Capability | $I_{OUT}$ | 600 | — | — | mA | $V_{IN} \ge 2.7\text{V}, V_{OUT} = 3.3\text{V}$ |
| Switch $R_{DS(ON)}$ (P-Channel) | $R_{DS(ON)P}$ | — | 0.19 | — | $\Omega$ | $V_{IN} = 3.3\text{V}$ |
| Switch $R_{DS(ON)}$ (N-Channel) | $R_{DS(ON)N}$ | — | 0.22 | — | $\Omega$ | $V_{IN} = 3.3\text{V}$ |
| Burst Mode Quiescent Current| $I_Q$ | — | 25 | 50 | $\mu\text{A}$ | Burst Mode enabled ($V_{IN} = 3.3\text{V}$) |
| Shutdown Current | $I_{SD}$ | — | 0.1 | 1.0 | $\mu\text{A}$ | $V_{SHDN} = 0\text{V}$ |

## Typical Application Circuit (3.3V Output from Single Li-Ion Cell)

```
       +V_IN (2.5V - 5.5V Single Li-Ion Battery)
          │
       [Pin 2: VIN]
        LTC3440 ──── Pin 1: SW1 ─── [ 4.7µH Inductor ] ─── Pin 4: SW2 ──── LTC3440 ──── [Pin 5: VOUT] ─── +3.3V Output
          │                                                                                 │
       [Pin 3: GND]                                                                      [ R1 ]
          │                                                                                 │
         GND ───────────────────────────────────────────────────────────────────────────────┴──── [Pin 6: FB]
                                                                                            │
                                                                                          [ R2 ]
                                                                                            │
                                                                                           GND
```

$$ V_{OUT} = 1.22\text{V} \times \left( 1 + \frac{R_1}{R_2} \right) $$

## Common mistakes

- **Incorrect Inductor Placement across SW1 and SW2:** A single inductor must be connected directly between Pin 1 (`SW1`) and Pin 4 (`SW2`). It is NOT connected to ground or output directly.
- **Noise on the feedback pin (`FB`):** Place feedback resistors $R_1$ and $R_2$ as close to Pin 6 (`FB`) as possible, routing the trace away from noisy switch nodes `SW1` and `SW2`.

## Notes

- **Buck-Boost Seamless Operation:** Unlike separate buck or boost switchers, LTC3440 automatically transitions between Buck, Buck-Boost, and Boost operating modes as a Li-Ion battery discharges from 4.2V down to 3.0V.
