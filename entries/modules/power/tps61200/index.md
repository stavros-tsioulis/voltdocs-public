## Overview

The **TPS61200** (packaged in 10-pin VSON **TPS61200DRCT**) is a low-input-voltage synchronous boost converter from Texas Instruments designed for single-cell alkaline, NiMH, or Li-Ion battery power supplies and energy harvesting systems.

It is capable of starting up into full load at an input voltage as low as **$0.5\text{ V}$**, and once running, continues operating down to **$0.3\text{ V}$**. Crucially, the TPS61200 features **Down-Mode operation**: if input voltage exceeds the output voltage setting, the converter automatically switches to a buck-like down-conversion mode to maintain regulation without pass-through voltage spikes.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Synchronous Boost Converter with Down-Mode |
| **Package** | VSON-10 (DRC / $3\times3\text{ mm}$ Exposed Thermal Pad) |
| **Input Voltage Range ($V_{IN}$)** | $0.3\text{ V}$ to $5.5\text{ V}$ DC ($0.5\text{ V}$ startup) |
| **Output Voltage Range ($V_{OUT}$)** | $1.8\text{ V}$ to $5.5\text{ V}$ DC (Adjustable) / Fixed 3.3V, 5.0V |
| **Continuous Output Current ($I_{OUT}$)** | Up to $600\text{ mA}$ at 3.3V (from 1.2V input) |
| **Switching Frequency** | $1.5\text{ MHz}$ fixed internal clock |
| **Conversion Efficiency** | Up to $90\%$ |
| **Special Features** | Programmable Undervoltage Lockout (`UVLO`), $55\ \mu\text{A}$ quiescent current |

## Pinout (VSON-10 Package)

```
        ┌─────────────┐
   VAUX ─│ 1        10 │─ VOUT
   VOUT ─│ 2         9 │─ FB
      L ─│ 3    EP   8 │─ UVLO
    GND ─│ 4         7 │─ PS
    VIN ─│ 5         6 │─ EN
        └─────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `VAUX` | Auxiliary supply input for internal circuitry bootstrap cap |
| 2 | `VOUT` | Regulated DC output voltage output pin |
| 3 | `L` / `SW` | Switch node connection for external inductor |
| 4 | `GND` | Ground reference (connected to exposed pad underneath) |
| 5 | `VIN` | Low-voltage DC input power supply pin (+0.3V to +5.5V) |
| 6 | `EN` | Enable control input (>1.2V enables converter, <0.4V disables) |
| 7 | `PS` | Power Save mode control pin (GND = Power Save enable, VOUT = forced PWM) |
| 8 | `UVLO` | Programmable Undervoltage Lockout resistor input |
| 9 | `FB` | Voltage feedback sense input pin ($500\text{mV}$ internal reference) |
| 10 | `VOUT` | Second regulated output connection pin |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Supply Voltage | $V_{IN}$ | 0.3 | 1.2 / 3.7 | 5.5 | V | Operational input range |
| Minimum Startup Voltage | $V_{START}$ | — | 0.5 | 0.8 | V | $I_{OUT} = 1\text{mA}$ |
| Feedback Reference Voltage | $V_{FB}$ | 490 | 500 | 510 | mV | $T_A = 25^\circ\text{C}$ |
| Switch Current Limit | $I_{CL}$ | 1200 | 1500 | 1800 | mA | Peak inductor current limit |
| High-Side Switch $R_{DS(ON)}$ | $R_{DS(ON)H}$ | — | 0.4 | — | $\Omega$ | $V_{OUT} = 3.3\text{V}$ |
| Low-Side Switch $R_{DS(ON)}$ | $R_{DS(ON)L}$ | — | 0.3 | — | $\Omega$ | $V_{OUT} = 3.3\text{V}$ |
| Switching Frequency | $f_{SW}$ | 1.2 | 1.5 | 1.8 | MHz | Internal oscillator |
| Quiescent Current | $I_Q$ | — | 55 | 80 | $\mu\text{A}$ | Power Save mode enabled |

## Typical Application Circuit (Single AA Cell to 3.3V Output)

```
       +V_IN (0.9V - 1.5V Single AA Cell)
          │
       [Pin 5: VIN] ── [ 4.7µH Inductor ] ── [Pin 3: L] ──── TPS61200 ──── [Pin 2/10: VOUT] ─── +3.3V Output
          │                                                                      │
       [Pin 4: GND]                                                           [ R1 ]
          │                                                                      │
         GND ────────────────────────────────────────────────────────────────────┴─── [Pin 9: FB]
                                                                                 │
                                                                               [ R2 ]
                                                                                 │
                                                                                GND
```

$$ V_{OUT} = 500\text{mV} \times \left( 1 + \frac{R_1}{R_2} \right) $$

## Common mistakes

- **Omitting the auxiliary capacitor on VAUX:** A $100\text{ nF}$ ceramic capacitor must be connected between `VAUX` (Pin 1) and `GND` to support low-voltage startup and internal gate drive bootstrap.
- **Improper UVLO resistor calculation:** Leaving the `UVLO` pin floating defaults to a high lockout threshold. Tie `UVLO` directly to `VIN` if external undervoltage lockout tuning is not required.

## Notes

- **Down-Mode Feature:** Standard boost converters short $V_{IN}$ to $V_{OUT}$ via their body diode if $V_{IN} > V_{OUT}$. The TPS61200's Down-Mode disconnects the body diode to maintain output voltage regulation.
