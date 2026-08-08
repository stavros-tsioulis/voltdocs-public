## Overview

The **1N4007** is a standard 1.0 Amp general-purpose silicon rectifier diode housed in a 2-terminal DO-41 axial-lead plastic package. Universally included in Arduino, Raspberry Pi, and electronics starter kits (Elegoo, SunFounder), it is the most widely produced power diode in history.

Rated for a maximum **peak repetitive reverse voltage ($V_{RRM}$) of $1000\text{ Volts}$** and a continuous **forward current ($I_{F(AV)}$) of $1.0\text{ Ampere}$**, the 1N4007 is primarily deployed as a **flyback protection diode** across inductive loads (relays, DC motors, solenoids) to suppress back-EMF voltage spikes, as reverse-polarity protection in DC power circuits, and as a low-frequency AC mains rectifier.

## Quick reference

| | |
|---|---|
| **Diode Type** | Silicon PN Junction Power Rectifier Diode |
| **Package** | DO-41 (DO-204AL) Axial Lead Plastic Package |
| **Cathode Marking** | Silver / White band painted on package body indicates Cathode (-) |
| **Peak Repetitive Reverse Voltage ($V_{RRM}$)**| $1000\text{ V}$ max |
| **RMS Reverse Voltage ($V_{RMS}$)**| $700\text{ V}$ max |
| **Average Rectified Forward Current ($I_{F(AV)}$)**| $1.0\text{ A}$ (at $T_A = 75^\circ\text{C}$) |
| **Non-Repetitive Peak Surge Current ($I_{FSM}$)**| $30\text{ A}$ ($8.3\text{ ms}$ single half sine-wave pulse) |
| **Forward Voltage Drop ($V_F$)**| $1.1\text{ V}$ max at $I_F = 1.0\text{A}$ |
| **Reverse Leakage Current ($I_R$)**| $5.0\ \mu\text{A}$ at rated $V_{RRM}$ |

## Physical Structure & Polarity Identification

```
             Cathode (-)                  Anode (+)
           (Silver Band) 
              ┌──────┐
      ────────┤  ||  ├────────
              └──────┘
```

- **Silver / White Band:** Marks the **Cathode (-)** terminal.
- **Plain Black End:** Marks the **Anode (+)** terminal.
- **Forward Conduction:** Current flows freely from **Anode to Cathode** when $V_{Anode} - V_{Cathode} \ge 0.7\text{V}$.
- **Reverse Blocking:** Current is blocked when $V_{Cathode} > V_{Anode}$ (up to $1000\text{V}$).

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Peak Repetitive Reverse Volts| $V_{RRM}$ | 1000 | — | — | V | Maximum reverse blocking |
| Average Forward Current | $I_{F(AV)}$ | — | — | 1.0 | A | $T_A = 75^\circ\text{C}$, half sine wave |
| Peak Surge Forward Current | $I_{FSM}$ | — | — | 30 | A | $8.3\text{ ms}$ single half-cycle |
| Forward Voltage Drop | $V_F$ | — | 0.85 | 1.1 | V | $I_F = 1.0\text{A}, T_J = 25^\circ\text{C}$ |
| Reverse Leakage Current | $I_R$ | — | 0.05 | 5.0 | µA | $V_R = 1000\text{V}, T_J = 25^\circ\text{C}$ |
| Typical Junction Capacitance | $C_J$ | — | 15 | — | pF | $V_R = 4.0\text{V}, f = 1.0\text{ MHz}$ |

## Flyback Diode Application (Inductive Protection)

When switching off inductive loads (such as a 5V relay coil or DC motor) via a transistor, collapsing magnetic fields generate a massive negative voltage spike (Back-EMF) $V = -L \cdot \frac{di}{dt}$ that can exceed $-100\text{V}$, destroying driving transistors.

Placing a 1N4007 in **reverse parallel across the inductive load** safely recirculates and dissipates the inductive current loop:

```
       +V_LOAD (5V - 24V DC)
          │
          ├───┬──────────────────────┐
          │   │                      │
        [LOAD COIL]        [1N4007 Flyback Diode]
        (Relay / Motor)      (Cathode Silver Band Top)
          │   │                      │
          ├───┴──────────────────────┘
          │
       [Drain / Collector]
     Low-Side Transistor (PN2222 or MOSFET)
          │
         GND
```

## Common mistakes

- **Connecting the diode backwards across an inductive load:** Connecting the Cathode (silver band) to GND and Anode to $+V_{CC}$ short-circuits the power supply as soon as the circuit turns on, blowing fuses or burning traces. **Always connect Cathode (silver band) to $+V_{CC}$** in flyback applications.
- **Using 1N4007 in high-frequency switching circuits ($>10\text{ kHz}$):** The 1N4007 is a standard recovery diode ($t_{rr} \approx 2\ \mu\text{s}$). In high-frequency SMPS buck converters ($>100\text{ kHz}$), use a **Schottky diode** (such as the 1N5819 or SS14) or ultra-fast recovery diode.

## Notes

- **1N4001 through 1N4007 Voltage Ratings:** 1N4001 (50V), 1N4002 (100V), 1N4003 (200V), 1N4004 (400V), 1N4005 (600V), 1N4006 (800V), **1N4007 (1000V)**. All variants handle 1.0A forward current.
