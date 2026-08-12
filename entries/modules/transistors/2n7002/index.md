## Overview

The **2N7002** is a widely used small-signal N-channel Enhancement Mode MOSFET IC packaged in a 3-pin surface-mount **SOT-23 enclosure**. It is the SMD counterpart to the classic through-hole 2N7000 transistor.

Designed for low-power signal switching, LED drive, small relay coil activation, and bidirectional $3.3\text{V} \leftrightarrow 5.0\text{V}$ $I^2C$ logic level shifters, the 2N7002 handles drain-source voltages up to **$60\text{ Volts}$** and continuous drain currents up to **$115\text{ mA}$**. With a low gate threshold voltage ($V_{GS(th)}$ of **$1.0\text{V} \dots 2.5\text{V}$**), it drives directly from 3.3V and 5V microcontroller GPIO pins.

## Quick reference

| | |
|---|---|
| **Transistor Type** | Small-Signal N-Channel Enhancement Mode MOSFET |
| **Package** | SOT-23 (3-pin SMD) |
| **Drain-Source Voltage ($V_{DSS}$)**| $60\text{ V}$ max |
| **Continuous Drain Current ($I_D$)**| $115\text{ mA}$ continuous ($300\text{ mA}$ pulsed) |
| **Gate-Source Voltage ($V_{GS}$)**  | $\pm 20\text{ V}$ max ($\pm 40\text{ V}$ peak transient) |
| **Gate Threshold Voltage ($V_{GS(th)}$)**| $1.0\text{ V}$ min to $2.5\text{ V}$ max ($1.8\text{ V}$ typical) |
| **On-State Resistance ($R_{DS(on)}$)**| $5.0\ \Omega$ at $V_{GS} = 10\text{V}$ / $7.5\ \Omega$ at $V_{GS} = 4.5\text{V}$ |
| **Turn-on / Turn-off Time** | $7\text{ ns}$ turn-on / $11\text{ ns}$ turn-off |

## Pinout (SOT-23 Package)

Looking at the top of the SOT-23 surface-mount component with single lead on top:

```
               ┌─────────┐
               │    3    │  (DRAIN)
               └─┐     ┌─┘
                 │2N702│
               ┌─┘     └─┐
               │ 1     2 │
               └─────────┘
            (GATE)   (SOURCE)
```

| Pin | Name | Description |
|---|---|---|
| 1 | `GATE` (`G`) | Gate control input (MCU GPIO pin) |
| 2 | `SOURCE` (`S`) | Source terminal (Ground reference 0 V) |
| 3 | `DRAIN` (`D`) | Drain terminal (Low-side load connection) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Drain-Source Breakdown Volts| $V_{(BR)DSS}$| 60 | — | — | V | $V_{GS} = 0\text{V}, I_D = 10\ \mu\text{A}$ |
| Gate Threshold Voltage | $V_{GS(th)}$| 1.0 | 1.8 | 2.5 | V | $V_{DS} = V_{GS}, I_D = 250\ \mu\text{A}$ |
| Zero Gate Voltage Current | $I_{DSS}$ | — | — | 1.0 | µA | $V_{DS} = 60\text{V}, V_{GS} = 0\text{V}$ |
| On-Resistance ($V_{GS}=10\text{V}$)| $R_{DS(on)}$| — | 3.5 | 5.0 | Ω | $V_{GS} = 10\text{V}, I_D = 500\text{mA}$ |
| On-Resistance ($V_{GS}=4.5\text{V}$)| $R_{DS(on)}$| — | 4.5 | 7.5 | Ω | $V_{GS} = 4.5\text{V}, I_D = 75\text{mA}$ |
| Total Power Dissipation | $P_D$ | — | — | 350 | mW | $T_A = 25^\circ\text{C}$ |

## Common mistakes

- **Attempting to drive high-current loads (>150mA):** The 2N7002 has an $R_{DS(on)}$ of up to **$7.5\ \Omega$** at $4.5\text{V}$ gate drive. Driving heavy loads generates excessive heat for an SMD SOT-23 footprint. For loads $>200\text{ mA}$, use a high-current SMD MOSFET like the AO3400 ($33\text{ m}\Omega$).
- **Leaving gate floating:** Always place a $10\text{ k}\Omega$ pull-down resistor from Gate to Source (GND) to prevent floating electrostatic charges from inadvertently triggering the FET.

## Notes

- **2N7002 vs 2N7000 vs BSS138:** 2N7002 is SOT-23 SMD ($115\text{ mA}$); 2N7000 is TO-92 through-hole ($200\text{ mA}$); BSS138 is SOT-23 SMD with lower threshold ($1.3\text{V}$ typ) optimized for 3.3V level shifters.
