## Overview

The **MP2307** (commonly packaged as **MP2307DN** in SOIC-8 with exposed thermal pad) is a monolithic $3.0\text{ A}$ synchronous step-down (buck) switching regulator manufactured by Monolithic Power Systems (MPS). Famous for driving ultra-tiny buck converter modules such as the **Mini360** and **KIS-3R33S**, it integrates both high-side ($100\text{ m}\Omega$) and low-side ($20\text{ m}\Omega$) power MOSFET switches on-chip.

By replacing the external freewheeling Schottky diode with an integrated low-side synchronous MOSFET switch, the MP2307 achieves efficiency levels up to **$95\%$**, drastically reducing thermal dissipation and component count.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Synchronous Step-Down (Buck) Converter |
| **Package** | SOIC-8 EP / Mini360 Breakout Module ($17\times11\text{ mm}$) |
| **Input Voltage Range ($V_{IN}$)** | $4.75\text{ V}$ to $23.0\text{ V}$ DC |
| **Output Voltage Range ($V_{OUT}$)** | $0.925\text{ V}$ to $20.0\text{ V}$ DC (Adjustable) |
| **Continuous Output Current ($I_{OUT}$)** | Up to $3.0\text{ A}$ ($4.0\text{ A}$ peak) |
| **Switching Frequency** | $340\text{ kHz}$ fixed internal oscillator |
| **Conversion Efficiency** | $90\% \dots 95\%$ |
| **Control Features** | Programmable soft-start (`SS`), logic enable (`EN`) |

## Pinout (SOIC-8 EP Package)

```
        ┌─────────────┐
    BS ─│ 1         8 │─ SS
    IN ─│ 2         7 │─ EN
    SW ─│ 3    EP   6 │─ COMP
   GND ─│ 4         5 │─ FB
        └─────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `BS` / `BST` | High-side gate drive bootstrap pin (10nF cap between BS and SW) |
| 2 | `IN` / `VIN` | Power supply input (+4.75V to +23V DC) |
| 3 | `SW` | Switch node output connecting internal high-side and low-side MOSFETs to inductor |
| 4 | `GND` | Ground reference (connected to exposed pad underneath) |
| 5 | `FB` | Feedback input pin ($0.925\text{V}$ reference voltage) |
| 6 | `COMP` | Error amplifier compensation node for loop stability |
| 7 | `EN` | Enable input pin (High = ON, Low = OFF) |
| 8 | `SS` | Soft-start pin (capacitor to GND sets soft-start timing) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Supply Voltage | $V_{IN}$ | 4.75 | 12 | 23 | V | Operating range |
| Feedback Reference Volts | $V_{FB}$ | 0.900 | 0.925 | 0.950 | V | $T_A = 25^\circ\text{C}$ |
| Continuous Output Current | $I_{OUT}$ | — | 3.0 | — | A | $V_{IN} = 12\text{V}, V_{OUT} = 5\text{V}$ |
| Peak Current Limit | $I_{CL}$ | 4.0 | 5.8 | — | A | High-side switch current limit |
| High-Side Switch $R_{DS(ON)}$ | $R_{DS(ON)H}$ | — | 100 | — | $\text{m}\Omega$ | $V_{BS} - V_{SW} = 5\text{V}$ |
| Low-Side Switch $R_{DS(ON)}$ | $R_{DS(ON)L}$ | — | 20 | — | $\text{m}\Omega$ | $V_{IN} = 12\text{V}$ |
| Switching Frequency | $f_{SW}$ | 300 | 340 | 380 | kHz | Fixed internal clock |
| Shutdown Current | $I_{SD}$ | — | 1 | 10 | $\mu\text{A}$ | $V_{EN} = 0\text{V}$ |

## Typical Application Circuit (Synchronous Buck)

```
       +V_IN (4.75V - 23V Input)
          │
       [Pin 2: IN]
        MP2307DN ──── [Pin 3: SW] ──── [ 10µH Inductor ] ───┬─── +V_OUT Regulated Output
          │                                                  │
       [Pin 4: GND]                                       [ R1 ]
          │                                                  │
         GND ────────────────────────────────────────────────┼─── [Pin 5: FB]
                                                             │
                                                           [ R2 ]
                                                             │
                                                            GND
```

$$ V_{OUT} = 0.925\text{V} \times \left( 1 + \frac{R_1}{R_2} \right) $$

## Common mistakes

- **Exceeding the 23V input limit:** The MP2307 absolute maximum input voltage is $26\text{ V}$ ($23\text{ V}$ recommended operational). Using it on $24\text{ V}$ industrial or solar rails will cause destructive overvoltage breakdown.
- **Floating the EN pin:** Leaving the enable pin unconnected can result in erratic startup. Tie `EN` directly to `IN` for automatic power-on operation.

## Notes

- **Synchronous vs Non-Synchronous Buck:** The MP2307 contains an integrated low-side MOSFET switch so no external diode is required, yielding higher efficiency than non-synchronous regulators like LM2596.
