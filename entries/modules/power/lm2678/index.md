## Overview

The **LM2678** is a $5.0\text{ A}$ step-down (buck) switching regulator from Texas Instruments' **SIMPLE SWITCHER®** family. Capable of driving loads up to $5.0\text{ A}$ with efficiency up to **$92\%$**, it features an integrated $0.2\ \Omega$ DMOS power switch operating at a fixed switching frequency of **$260\text{ kHz}$**.

The LM2678 accepts input voltages from $8.0\text{ V}$ to $40.0\text{ V}$ and delivers adjustable output voltages down to $1.21\text{ V}$ (or fixed 3.3V, 5.0V, 12V outputs). Its higher switching frequency ($260\text{ kHz}$) compared to classic 52kHz regulators enables smaller filter inductors and capacitors while handling high power.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Monolithic High-Current Step-Down (Buck) Regulator |
| **Package** | TO-263-7 (D2PAK-7 Surface-Mount) / TO-220-7 / VSON-14 |
| **Input Voltage Range ($V_{IN}$)** | $8.0\text{ V}$ to $40.0\text{ V}$ DC |
| **Output Voltage Range ($V_{OUT}$)** | $1.21\text{ V}$ to $37.0\text{ V}$ DC (Adjustable) / Fixed 3.3V, 5V, 12V |
| **Continuous Output Current ($I_{OUT}$)** | Up to $5.0\text{ A}$ |
| **Switching Frequency** | $260\text{ kHz}$ internal fixed oscillator |
| **Conversion Efficiency** | $85\% \dots 92\%$ |
| **Control Features** | Logic `ON`/`OFF` shutdown control, thermal shutdown, current limiting |

## Pinout (TO-263-7 / TO-220-7 Package)

```
        ┌─────────────────────┐
        │     LM2678S-ADJ     │  (Front Package Face)
        └─┬──┬──┬──┬──┬──┬────┘
          1  2  3  4  5  6  7
         SW VIN CB GND NC FB ON/OFF
```

| Pin | Name | Description |
|---|---|---|
| 1 | `SWITCH OUT` / `SW` | Internal DMOS power switch output connecting to Schottky diode & inductor |
| 2 | `VIN` | Unregulated DC power supply input (+8.0V to +40V DC) |
| 3 | `CB` / `BOOST` | Bootstrap capacitor connection to `SW` ($0.01\ \mu\text{F}$ / 10nF ceramic cap) |
| 4 | `GND` | Ground reference (connected to tab/exposed pad) |
| 5 | `NC` | No internal connection |
| 6 | `FEEDBACK` / `FB` | Feedback sensing input ($1.21\text{V}$ reference voltage for ADJ version) |
| 7 | `ON`/`OFF` | Shutdown control input pin (Low = ON, High = OFF) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Voltage Range | $V_{IN}$ | 8.0 | 12 / 24 | 40 | V | Operating DC input range |
| Feedback Reference Voltage | $V_{FB}$ | 1.174 | 1.210 | 1.246 | V | $V_{IN} = 12\text{V}, I_{OUT} = 2.5\text{A}$ |
| Continuous Output Current | $I_{OUT}$ | — | 5.0 | — | A | $V_{IN} - V_{OUT} \ge 3.0\text{V}$ |
| Peak Current Limit | $I_{CL}$ | 6.5 | 8.0 | 10.0 | A | Internal switch peak current limit |
| DMOS Switch On-Resistance | $R_{DS(ON)}$ | — | 0.20 | 0.35 | $\Omega$ | $I_{OUT} = 5.0\text{A}$ |
| Switching Frequency | $f_{SW}$ | 225 | 260 | 290 | kHz | Internal clock frequency |
| Standby Current | $I_{STBY}$ | — | 50 | 150 | $\mu\text{A}$ | Shutdown state ($V_{ON/OFF} = 3.0\text{V}$) |

## Typical Application Circuit

```
       +V_IN (8.0V - 40V DC Input)
          │
       [Pin 2: VIN]
        LM2678S-ADJ ── [Pin 1: SW] ─── [ 22µH - 47µH Inductor ] ──┬─── +V_OUT Regulated Output
          │     │                            │                     │
          │  [CB: 10nF]                      │                  [ R1 = 1kΩ ]
          │     │                            │                     │
       [Pin 4: GND]               [1N5825 / B540 Schottky]        │
          │                                  │                     │
         GND ────────────────────────────────┴─────────────────────┼─── [Pin 6: FB]
                                                                   │
                                                                 [ R2 ]
                                                                   │
                                                                  GND
```

$$ V_{OUT} = 1.21\text{V} \times \left( 1 + \frac{R_2}{R_1} \right) $$

## Common mistakes

- **Omitting the Bootstrap capacitor (`CB`):** A $10\text{ nF}$ ceramic capacitor must be connected between Pin 3 (`CB`) and Pin 1 (`SW`) to supply gate voltage for the internal DMOS switch. Without it, the switch will not turn on properly.
- **Inadequate PCB copper area for heatsinking:** Delivering 5A output creates thermal dissipation even at 90% efficiency. Solder the TO-263 tab to a large copper ground plane with thermal vias to prevent over-temperature shutdown.

## Notes

- **LM2678 vs LM2596:** The LM2678 handles 5A continuous (vs 3A for LM2596) and operates at $260\text{ kHz}$ with higher efficiency due to its low-resistance DMOS switch.
