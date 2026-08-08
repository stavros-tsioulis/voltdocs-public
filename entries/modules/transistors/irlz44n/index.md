## Overview

The **IRLZ44N** is an N-channel logic-level power MOSFET manufactured by Infineon (formerly International Rectifier) in a TO-220AB package. Rated for **$55\text{V}$ drain-source voltage** ($V_{DSS}$) and **$47\text{A}$ continuous drain current** ($I_D$), it is engineered specifically for driving high-power DC loads directly from low-voltage digital microcontrollers.

Unlike standard power MOSFETs (such as the IRF540N or IRF520) that require $10\text{V}$ on the gate to fully turn on, the IRLZ44N features a low gate threshold voltage ($V_{GS(th)} = 1.0\text{V} \dots 2.0\text{V}$). It achieves an ultra-low $R_{DS(on)}$ resistance of just **$22\ \text{m}\Omega$ at $V_{GS} = 5.0\text{V}$** and **$25\ \text{m}\Omega$ at $V_{GS} = 4.0\text{V}$**, making it the premier choice for 3.3V and 5V MCU PWM motor control, high-current LED strip dimming, and solenoid switching.

## Quick reference

| | |
|---|---|
| **Transistor type** | N-Channel Power MOSFET (Logic-Level Gate) |
| **Package** | TO-220AB (Pin 1: Gate, Pin 2: Drain/Tab, Pin 3: Source) |
| **Drain-Source Voltage ($V_{DSS}$)** | $55\text{ V}$ max |
| **Continuous Drain Current ($I_D$)** | $47\text{ A}$ (at $T_C = 25^\circ\text{C}$, $V_{GS} = 10\text{V}$) |
| **Gate Threshold Voltage ($V_{GS(th)}$)**| $1.0\text{ V}$ min / $2.0\text{ V}$ max |
| **$R_{DS(on)}$ at $V_{GS} = 5.0\text{V}$** | $22\ \text{m}\Omega$ ($0.022\ \Omega$) |
| **$R_{DS(on)}$ at $V_{GS} = 4.0\text{V}$** | $25\ \text{m}\Omega$ ($0.025\ \Omega$) |
| **$R_{DS(on)}$ at $V_{GS} = 10\text{V}$** | $17.5\ \text{m}\Omega$ ($0.0175\ \Omega$) |
| **Max Power Dissipation ($P_D$)** | $110\text{ W}$ (with heatsink) |

## Pinout (TO-220AB Package)

```
        ┌─────────┐
        │  TO-220 │
        │  IRLZ44 │
        └─┬───┬───┬─┘
          1   2   3
          G   D   S
```

| Pin | Name | Description |
|---|---|---|
| 1 | `Gate` (`G`) | Control input (connected to MCU GPIO via $220\ \Omega$ series resistor) |
| 2 / Tab | `Drain` (`D`) | High-power load switching output (connected to load negative terminal) |
| 3 | `Source` (`S`) | Ground reference (connected to common system ground) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Drain-Source Breakdown Volts| $V_{(BR)DSS}$| 55 | — | — | V | $V_{GS} = 0\text{V}, I_D = 250\ \mu\text{A}$ |
| Gate-Source Threshold Volts | $V_{GS(th)}$ | 1.0 | — | 2.0 | V | $V_{DS} = V_{GS}, I_D = 250\ \mu\text{A}$ |
| Static Drain-Source On-Resist| $R_{DS(on)}$ | — | 18 | 22 | mΩ | $V_{GS} = 5.0\text{V}, I_D = 25\text{A}$ |
| Static Drain-Source On-Resist| $R_{DS(on)}$ | — | 21 | 25 | mΩ | $V_{GS} = 4.0\text{V}, I_D = 21\text{A}$ |
| Gate-Source Leakage Current | $I_{GSS}$ | — | — | $\pm 100$ | nA | $V_{GS} = \pm 16\text{V}$ |
| Total Gate Charge | $Q_g$ | — | 32 | 48 | nC | $V_{DS} = 44\text{V}, V_{GS} = 5.0\text{V}$ |
| Diode Forward Voltage | $V_{SD}$ | — | 0.8 | 1.3 | V | Internal body diode, $I_S = 25\text{A}$ |

## Driving Circuit Topology

To switch high-power loads cleanly from an Arduino (5V) or ESP32 / Raspberry Pi (3.3V):

```
       +V_LOAD (12V - 24V DC)
          │
        [LOAD] (Motor / LED Strip / Solenoid)
          │
          ├──────────────┐
          │              │
        [Drain]      [Flyback Diode 1N4007] (For Inductive Loads Only)
     IRLZ44N MOSFET      │
        [Source] ────────┼─────── GND (Common System Ground)
          │              │
        [Gate]           │
          │              │
       [220Ω]            │
          │              │
     MCU GPIO Pin ───────┴─────── [10kΩ Pull-Down to GND]
```

- **$220\ \Omega$ Gate Resistor:** Limits initial high-frequency capacitive gate charging current spikes into the MCU pin.
- **$10\ \text{k}\Omega$ Gate Pull-Down Resistor:** Keeps the gate firmly at 0V during MCU bootup/reset, preventing accidental un-commanded load activation.
- **1N4007 Flyback Diode:** Required across inductive loads (DC motors, relays, solenoids) to dissipate back-EMF voltage spikes.

## Power Dissipation Math

$$ P_{dissipated} = I_{D}^2 \times R_{DS(on)} $$

- **For a 5A LED Strip Load ($V_{GS} = 5.0\text{V}$):**

$$ P_{dissipated} = (5\text{A})^2 \times 0.022\ \Omega = 0.55\text{ Watts} \quad (\text{No heatsink required}) $$

- **For a 15A Motor Load ($V_{GS} = 5.0\text{V}$):**

$$ P_{dissipated} = (15\text{A})^2 \times 0.022\ \Omega = 4.95\text{ Watts} \quad (\text{TO-220 aluminum heatsink required}) $$

## Common mistakes

- **Using standard IRF540N / IRF520 instead of IRLZ44N:** Standard "IRF" series MOSFETs specify $R_{DS(on)}$ at $V_{GS} = 10\text{V}$. When driven with $3.3\text{V}$ or $5.0\text{V}$ from an MCU, standard MOSFETs remain in their linear region, overheating rapidly under high currents.
- **Forgetting common ground:** The MCU ground and the load power supply negative terminal must be connected together at the MOSFET Source pin.

## Notes

- **IRLZ44N vs IRFZ44N:** "L" indicates **Logic-Level** ($V_{GS(th)} = 1.0\text{--}2.0\text{V}$); "F" indicates **Standard-Gate** ($V_{GS(th)} = 2.0\text{--}4.0\text{V}$, requires 10V gate drive).
