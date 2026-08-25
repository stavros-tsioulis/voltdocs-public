## Overview

The **NCP1400ASN33T1** (NCP1400A 3.3V) is a miniature micropower step-up (boost) DC-DC converter manufactured by onsemi. Housed in a compact 5-pin surface-mount **TSOP-5 (SOT-23-5)** package, it provides a regulated **$+3.3\text{V}$ DC** rail at up to **$100\text{ mA}$** from low-voltage single-cell power sources.

Featuring an ultra-low startup voltage of just **$0.8\text{V}$** (operating down to $0.2\text{V}$ once started), an idle quiescent current of only **$19\ \mu\text{A}$**, and a pulse-frequency modulation (**PFM**) architecture switching up to **$180\text{ kHz}$**, the NCP1400A requires only three external components: a miniature inductor, a Schottky diode, and input/output ceramic capacitors. It is widely used in wearable electronics, wireless sensors, electronic badges, and battery-powered gadgets running microcontrollers (such as ATtiny, PIC, or MSP430) from a **single $1.5\text{V}$ AA/AAA alkaline battery, $1.2\text{V}$ NiMH cell, or $3.0\text{V}$ CR2032 coin cell**.

## Quick reference

| | |
|---|---|
| **Converter Topology** | Micropower PFM Step-Up (Boost) DC-DC Converter |
| **Package** | TSOP-5 (5-pin SMD / SOT-23-5) |
| **Output Voltage ($V_{OUT}$)** | $+3.3\text{ V}$ DC fixed ($\pm 2.5\%$) |
| **Startup Input Voltage ($V_{START}$)** | **$0.8\text{ V}$ typical** ($0.9\text{ V}$ max) |
| **Operating Input Range ($V_{IN}$)** | $0.8\text{ V}$ to $3.3\text{ V}$ DC ($6.0\text{ V}$ absolute max) |
| **Output Current ($I_{OUT}$)** | Up to $100\text{ mA}$ ($V_{IN} = 1.5\text{V}, V_{OUT} = 3.3\text{V}$) |
| **Quiescent Current ($I_Q$)** | **$19\ \mu\text{A}$ typical** (No load) / $< 0.1\ \mu\text{A}$ in shutdown |
| **Switching Frequency** | Up to $180\text{ kHz}$ (PFM architecture) |
| **Peak Efficiency** | Up to $82\%$ |
| **Shutdown Control** | Active-HIGH Chip Enable (`CE`) pin |

## Pinout (TSOP-5 / SOT-23-5 Package)

```
        ┌───┬───┐
      1 │   │ 5 │ LX (Inductor Switching Node)
     CE │   └───┤
    OUT │ 2   4 │ GND (0V)
     NC │ 3     │
        └───┴───┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `CE` | Control Input | Chip Enable (Active HIGH; tie to $V_{IN}$ to enable, pull LOW for $< 0.1\ \mu\text{A}$ shutdown) |
| 2 | `OUT` | Power Output / Feedback | Output voltage sense and internal bias supply ($+3.3\text{ V}$) |
| 3 | `NC` | No Connect | Leave unconnected or solder to ground plane |
| 4 | `GND` | Ground | Common system ground reference ($0\text{ V}$) |
| 5 | `LX` | Switching Node | Drain of internal N-channel power MOSFET (Connect to inductor and Schottky diode anode) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Output Voltage | $V_{OUT}$ | 3.218 | 3.300 | 3.382 | V | $I_O = 10\text{mA}, V_{IN} = 1.5\text{V}$ |
| Minimum Startup Voltage | $V_{START}$ | — | 0.8 | 0.9 | V | $I_O = 1.0\text{mA}$ |
| Operating Voltage (Post Start)| $V_{HOLD}$ | 0.2 | 0.6 | — | V | $I_O = 1.0\text{mA}$ |
| Quiescent Current | $I_Q$ | — | 19.0 | 35.0 | µA | $I_O = 0\text{mA}, V_{IN} = 1.5\text{V}$ |
| Shutdown Current | $I_{SD}$ | — | 0.1 | 0.6 | µA | $V_{CE} = 0\text{V}, V_{IN} = 1.5\text{V}$ |
| Max Switching Frequency | $f_{OSC}$ | 140 | 180 | 220 | kHz | $V_{OUT} = 3.3\text{V}$ |
| Internal Switch Limit | $I_{LIM}$ | — | 350 | — | mA | Peak inductor current |

## Typical Application Circuit

```
  Single Alkaline / NiMH Cell (0.9V - 1.5V)
           │
           ├───[ C_IN: 10µF Ceramic / Tantalum ]──┐
           │                                      │
           ├───[ L1: 47µH Inductor (CD54/0630) ]──┼───────────┐
           │                                      │           │
           │                                  [Pin 4: GND]    │
           │                                      │           │
       [Pin 1: CE]                                │       [Pin 5: LX]
         NCP1400A                                 │           │
       [Pin 2: OUT] ──────────────┬───────────────┴─── GND    │
           │                      │                           │
           │            [ D1: MBR0520LT1 Schottky ] ──────────┘
           │                      │ (Cathode to OUT)
           ├───[ C_OUT: 22µF Low-ESR Ceramic / Tantalum ]── GND
           │
  Regulated +3.3V DC (Up to 100mA for Microcontroller & Radio)
```

## Recommended External Components

1. **Inductor ($L_1$):** $22\ \mu\text{H}$ to $47\ \mu\text{H}$ shielded power inductor with saturation current $I_{SAT} \ge 500\text{ mA}$ and low DC resistance (e.g. Sumida CD43 / CD54).
2. **Schottky Diode ($D_1$):** Low forward drop Schottky diode (e.g. **MBR0520L**, **1N5819HW**, **BAT54**).
3. **Output Capacitor ($C_{OUT}$):** $10\ \mu\text{F} \dots 22\ \mu\text{F}$ low-ESR X5R/X7R ceramic or tantalum capacitor placed directly adjacent to Pins 2 and 4.

## Common mistakes

- **Using a standard PN junction diode instead of Schottky:** Standard silicon diodes (e.g. 1N4148, 1N4007) have a $0.7\text{V} \dots 1.0\text{V}$ forward drop, severely cutting efficiency and preventing the circuit from boosting under load. Always use a **Schottky diode** with $V_F < 0.35\text{V}$.
- **Input voltage exceeding output voltage:** In boost topology, current flows directly from input through inductor and diode to output. If $V_{IN} > V_{OUT}$ (e.g. connecting a 4.2V LiPo battery to a 3.3V NCP1400A), the output voltage will rise uncontrollably to $V_{IN} - V_{DIODE}$.

## Notes

- **Suffix Guide:** `ASN33` designates $+3.3\text{V}$ fixed output; `ASN50` designates $+5.0\text{V}$ fixed output; `T1G` denotes RoHS lead-free tape & reel packaging.
