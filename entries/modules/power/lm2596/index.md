## Overview

The **LM2596** (and surface-mount TO-263 packaged **LM2596S-ADJ**) is a 3.0 Amp step-down (buck) switching voltage regulator IC manufactured by Texas Instruments. Sold as a ubiquitous blue DC-DC buck converter breakout module with a multi-turn trimmer potentiometer on Amazon, eBay, and AliExpress, it efficiently steps down higher DC voltages (such as 12V, 24V, or 36V power supplies) to lower regulated voltages (such as 5V or 3.3V) for microcontrollers, motors, and LED strips.

Operating at a **$150\text{ kHz}$ switching frequency**, the LM2596 achieves power conversion efficiencies between **$80\%\text{ and }92\%$**, generating significantly less heat than traditional linear regulators (like the LM7805 or LM317).

## Quick reference

| | |
|---|---|
| **Regulator Type** | Monolithic Step-Down (Buck) Switching Regulator |
| **Package** | TO-263 (D2PAK 5-Lead) / TO-220-5 / Blue Breakout Module |
| **Input Voltage Range ($V_{IN}$)**| $4.5\text{ V}$ to $40.0\text{ V}$ DC (HV version up to 60V) |
| **Output Voltage Range ($V_{OUT}$)**| $1.23\text{ V}$ to $37.0\text{ V}$ DC (Adjustable) / Fixed 3.3V, 5V, 12V |
| **Continuous Output Current ($I_{OUT}$)**| Up to $3.0\text{ A}$ (with adequate copper PCB heatsinking) |
| **Switching Frequency** | $150\text{ kHz}$ internal oscillator |
| **Conversion Efficiency** | $80\% \dots 92\%$ |
| **Control Features** | `ON`/`OFF` shutdown control pin (Low = ON, High = OFF) |

## Pinout (TO-263 5-Lead Package & Module Terminals)

```
        ┌──────────────────┐
        │   LM2596S-ADJ    │  (Front Package Face)
        └─┬───┬───┬───┬────┘
          1   2   3   4   5
         VIN SW  GND FB  ON/OFF
```

| Pin | Name | Description |
|---|---|---|
| 1 | `VIN` | Unregulated DC power input pin (+4.5 V to +40 V DC) |
| 2 | `OUTPUT` / `SW` | Internal NPN switch output (Connects to Schottky diode & 33µH inductor) |
| 3 | `GND` / `TAB` | Ground reference (0 V) |
| 4 | `FEEDBACK` / `FB`| Voltage feedback sensing pin (1.23V reference) |
| 5 | `ON`/`OFF` | Logic control input (Connect to GND for normal operation, High to shut down) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Voltage Range | $V_{IN}$ | 4.5 | 12 / 24 | 40 | V | DC input |
| Output Feedback Volts | $V_{FB}$ | 1.193 | 1.230 | 1.267 | V | Adjustable version |
| Continuous Load Current| $I_{OUT}$ | — | 3.0 | — | A | $V_{IN} - V_{OUT} \ge 3.0\text{V}$ |
| Current Limit Threshold| $I_{CL}$ | 3.6 | 4.5 | 7.5 | A | Internal switch peak current limit |
| Oscillator Frequency | $f_{OSC}$ | 127 | 150 | 173 | kHz | Internal switching clock |
| Quiescent Current | $I_Q$ | — | 5.0 | 10.0 | mA | Operating state ($V_{FB} = 1.3\text{V}$) |

## Module Circuit & Voltage Calculation

```
       +V_IN (4.5V - 40V DC Input)
          │
       [Pin 1: VIN]
        LM2596S-ADJ ── [Pin 2: SW] ─── [ 33µH Inductor ] ───┬─── +V_OUT Regulated DC Output
          │                                  │              │
       [Pin 3: GND]               [SS34 Schottky Diode]  [ R1 = 1kΩ ]
          │                                  │              │
         GND ────────────────────────────────┴──────────────┼─── [Pin 4: FB]
                                                            │
                                                   [ R2 = Potentiometer ]
                                                            │
                                                           GND
```

$$ V_{OUT} = 1.23\text{V} \times \left( 1 + \frac{R_2}{R_1} \right) $$

*(Adjusting the brass screw on the 3296W multi-turn potentiometer changes $R_2$ to adjust output voltage).*

## Wiring (DC-DC Converter Module)

| LM2596 Module Terminal | → | Power Source / Load | Notes |
|---|---|---|---|
| `IN+` | | $+V_{CC}$ (12V / 24V Power Supply) | Positive input rail |
| `IN-` | | Power Supply GND | Ground reference |
| `OUT+` | | $+V_{OUT}$ (5V / 3.3V Load Rail) | Regulated output voltage |
| `OUT-` | | Load GND | Shared ground output |

> [!WARNING]
> Adjusting Blue LM2596 Buck Modules for the First Time:
> - Blue LM2596 modules shipped from factories often have their multi-turn potentiometer preset to maximum voltage ($V_{OUT} = V_{IN}$).
> - **Turn the brass screw 10 to 15 full turns COUNTER-CLOCKWISE** while measuring output with a multimeter to bring output voltage down to 5V before connecting sensitive microcontrollers.

## Common mistakes

- **Attempting to step UP voltage:** The LM2596 is a **Buck (Step-Down)** regulator. $V_{IN}$ must be at least **$1.5\text{V}$ higher than $V_{OUT}$**. It cannot boost $5\text{V}$ up to $12\text{V}$ (use XL6009 or MT3608 for step-up boost).
- **Omitting external Schottky diode on custom PCBs:** The LM2596 requires an external fast Schottky catch diode (e.g. 1N5822 or SS34) across the `SW` pin and GND to recirculate inductor current.

## Notes

- **LM2596 vs XL4015 vs MP1584:** LM2596 operates at 150kHz (3A max); XL4015 operates at 180kHz (5A max); MP1584 operates at 1.5MHz (tiny footprint).
