## Overview

The **MP1584** (specifically **MP1584EN** in an 8-pin SOIC package with exposed thermal pad) is a high-frequency $3.0\text{ A}$ step-down (buck) switching voltage regulator manufactured by Monolithic Power Systems (MPS). Featuring an integrated $100\text{ m}\Omega$ high-side N-channel MOSFET, it accepts input voltages from $4.5\text{ V}$ to $28\text{ V}$ and delivers output voltages adjustable down to $0.8\text{ V}$.

Capable of operating at switching frequencies up to **$1.5\text{ MHz}$**, the MP1584 allows the use of very small ceramic capacitors and low-profile $4.7\ \mu\text{H}$ or $10\ \mu\text{H}$ inductors. As a result, MP1584 modules are significantly smaller and lighter than legacy LM2596 modules while delivering superior efficiency.

## Quick reference

| | |
|---|---|
| **Regulator Type** | High-Frequency Monolithic Step-Down (Buck) Converter |
| **Package** | SOIC-8 EP (Exposed Pad) / Mini Buck Module ($22\times17\text{ mm}$) |
| **Input Voltage Range ($V_{IN}$)** | $4.5\text{ V}$ to $28.0\text{ V}$ DC |
| **Output Voltage Range ($V_{OUT}$)** | $0.8\text{ V}$ to $25.0\text{ V}$ DC (Adjustable) |
| **Continuous Output Current ($I_{OUT}$)** | Up to $3.0\text{ A}$ |
| **Switching Frequency** | Programmable up to $1.5\text{ MHz}$ (Typically $100\text{ kHz} \dots 1.5\text{ MHz}$) |
| **Conversion Efficiency** | $88\% \dots 95\%$ |
| **Features** | Internal soft-start, thermal shutdown, pulse-skipping light-load mode |

## Pinout (SOIC-8 EP Package)

```
        ┌─────────────┐
    SW ─│ 1         8 │─ BST
    EN ─│ 2         7 │─ VIN
  COMP ─│ 3    EP   6 │─ FREQ
    FB ─│ 4         5 │─ GND
        └─────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `SW` | Switch node output connecting internal MOSFET to catch diode and inductor |
| 2 | `EN` | Enable input (>1.35V enables, <1.15V disables; internal pull-up) |
| 3 | `COMP` | Error amplifier output / loop compensation network |
| 4 | `FB` | Feedback sense pin ($0.8\text{V}$ reference voltage) |
| 5 | `GND` | Ground reference (connected to exposed pad underneath) |
| 6 | `FREQ` / `FSET` | Switching frequency configuration pin (resistor connected to GND sets $f_{SW}$) |
| 7 | `VIN` | Power supply input (+4.5V to +28V DC) |
| 8 | `BST` | Bootstrap pin for internal N-channel high-side gate drive (10nF cap to SW) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Supply Voltage | $V_{IN}$ | 4.5 | 12 | 28 | V | DC input |
| Feedback Reference Voltage | $V_{FB}$ | 0.776 | 0.800 | 0.824 | V | $T_A = 25^\circ\text{C}$ |
| Continuous Output Current | $I_{OUT}$ | — | 3.0 | — | A | $V_{IN} = 12\text{V}, V_{OUT} = 5\text{V}$ |
| High-Side On-Resistance | $R_{DS(ON)}$ | — | 100 | — | $\text{m}\Omega$ | $V_{BST} - V_{SW} = 5\text{V}$ |
| Switching Frequency | $f_{SW}$ | 100 | 1000 | 1500 | kHz | Set by resistor on `FREQ` pin |
| Quiescent Current | $I_Q$ | — | 360 | 450 | $\mu\text{A}$ | Unswitched state ($V_{FB} = 1.0\text{V}$) |
| Shutdown Current | $I_{SD}$ | — | 1 | 10 | $\mu\text{A}$ | $V_{EN} = 0\text{V}$ |

## Typical Application Circuit

```
       +V_IN (4.5V - 28V DC Input)
          │
       [Pin 7: VIN]
        MP1584EN ──── [Pin 1: SW] ──── [ 4.7µH - 10µH Inductor ] ──┬─── +V_OUT Regulated Output
          │                                  │                     │
       [Pin 5: GND]               [B340A Schottky Diode]        [ R1 ]
          │                                  │                     │
         GND ────────────────────────────────┴─────────────────────┼─── [Pin 4: FB]
                                                                   │
                                                                 [ R2 ]
                                                                   │
                                                                  GND
```

$$ V_{OUT} = 0.8\text{V} \times \left( 1 + \frac{R_1}{R_2} \right) $$

## Common mistakes

- **Overheating under high continuous current without thermal dissipation:** While rated for 3A peak, running continuously at 3A on miniature breakout boards without heatsinking or thermal vias will trigger internal thermal protection.
- **Operating above 28V input:** Unlike the LM2596 (40V rating), the MP1584 max input rating is strictly $28\text{ V}$. Connecting a fully charged $24\text{ V}$ lead-acid battery or spikes over $28\text{ V}$ will destroy the chip.

## Notes

- **MP1584 vs LM2596:** The MP1584 runs 10x faster ($1.5\text{ MHz}$ vs $150\text{ kHz}$), allowing modules to be $1/3$ the size of LM2596 boards.
