## Overview

The **LM2576** (and adjustable TO-220 5-pin variant **LM2576T-ADJ**) is a 3.0 Amp step-down (buck) switching regulator IC manufactured by Texas Instruments (originally National Semiconductor). Operating at a **$52\text{ kHz}$ switching frequency**, it is the direct predecessor to the ubiquitous LM2596 ($150\text{ kHz}$).

Because of its lower switching frequency, the LM2576 uses larger inductors (typically $100\ \mu\text{H}$ to $330\ \mu\text{H}$) than modern high-frequency converters, but offers exceptional ruggedness, internal current limiting, and thermal shutdown features. It is widely used in power supplies, industrial control circuits, and hobbyist DC-DC step-down converters.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Monolithic Step-Down (Buck) Switching Regulator |
| **Package** | TO-220-5 (Through-Hole) / TO-263-5 (D2PAK) |
| **Input Voltage Range ($V_{IN}$)** | $4.0\text{ V}$ to $40.0\text{ V}$ DC (HV version up to $60\text{ V}$) |
| **Output Voltage Range ($V_{OUT}$)** | $1.23\text{ V}$ to $37.0\text{ V}$ DC (Adjustable) / Fixed 3.3V, 5V, 12V, 15V |
| **Continuous Output Current ($I_{OUT}$)** | Up to $3.0\text{ A}$ |
| **Switching Frequency** | $52\text{ kHz}$ internal oscillator |
| **Conversion Efficiency** | $75\% \dots 88\%$ |
| **Control Features** | `ON`/`OFF` logic shutdown pin (Low = ON, High = OFF) |

## Pinout (TO-220 5-Pin Package)

```
        ┌──────────────────┐
        │   LM2576T-ADJ    │  (Front Package Face)
        └─┬───┬───┬───┬────┘
          1   2   3   4   5
         VIN SW  GND FB  ON/OFF
```

| Pin | Name | Description |
|---|---|---|
| 1 | `VIN` | Unregulated DC input supply pin (+4.0 V to +40 V DC) |
| 2 | `OUTPUT` / `SW` | Internal NPN power switch emitter output (Connects to Schottky catch diode & 100µH inductor) |
| 3 | `GND` | Ground reference (0 V) |
| 4 | `FEEDBACK` / `FB` | Feedback sensing pin (1.23V internal reference for ADJ version) |
| 5 | `ON`/`OFF` | Logic control shutdown input (Connect to GND for normal operation, High to shut down) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Voltage Range | $V_{IN}$ | 4.0 | 12 / 24 | 40 | V | Standard version ($V_{IN} - V_{OUT} \ge 2.0\text{V}$) |
| Feedback Reference Voltage | $V_{FB}$ | 1.193 | 1.230 | 1.267 | V | Adjustable version ($V_{IN} = 12\text{V}, I_{OUT} = 0.5\text{A}$) |
| Continuous Load Current | $I_{OUT}$ | — | 3.0 | — | A | $V_{IN} - V_{OUT} \ge 2.0\text{V}$ |
| Peak Current Limit | $I_{CL}$ | 4.2 | 5.8 | 6.9 | A | Internal switch current limit |
| Oscillator Frequency | $f_{OSC}$ | 47 | 52 | 58 | kHz | Internal clock frequency |
| Quiescent Current | $I_Q$ | — | 5.0 | 10.0 | mA | Operating state ($V_{FB} = 1.3\text{V}$) |
| Standby Current | $I_{STBY}$ | — | 50 | 200 | $\mu\text{A}$ | Shutdown state ($V_{ON/OFF} = 5.0\text{V}$) |

## Typical Application Circuit

```
       +V_IN (4.0V - 40V DC Input)
          │
       [Pin 1: VIN]
        LM2576T-ADJ ── [Pin 2: SW] ─── [ 100µH Inductor ] ──┬─── +V_OUT Regulated DC Output
          │                                  │              │
       [Pin 3: GND]               [1N5822 Schottky Diode] [ R1 = 1kΩ ]
          │                                  │              │
         GND ────────────────────────────────┴──────────────┼─── [Pin 4: FB]
                                                            │
                                                          [ R2 ]
                                                            │
                                                           GND
```

$$ V_{OUT} = 1.23\text{V} \times \left( 1 + \frac{R_2}{R_1} \right) $$

## Common mistakes

- **Using a standard silicon rectifier diode instead of a Schottky diode:** The LM2576 requires a fast Schottky catch diode (such as 1N5822 or SR360) between `SW` and `GND`. Standard 1N4007 diodes are too slow and cause overheating and failure.
- **Undersized inductor value:** Due to the $52\text{ kHz}$ switching frequency, using smaller inductors (such as 10µH or 22µH meant for 1MHz+ switchers) leads to excessive peak currents and regulator saturation. Use $100\ \mu\text{H}$ or higher rated for 3A continuous.

## Notes

- **LM2576 vs LM2596:** LM2576 operates at $52\text{ kHz}$, requiring larger inductors ($100\ \mu\text{H}$), whereas LM2596 operates at $150\text{ kHz}$ with smaller inductors ($33\ \mu\text{H}$).
