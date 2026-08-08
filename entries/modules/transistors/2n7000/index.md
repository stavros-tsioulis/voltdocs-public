## Overview

The **2N7000** is a universally used small-signal N-channel Enhancement Mode MOSFET IC manufactured by ON Semiconductor, Microchip, and STMicroelectronics. Packaged in a compact 3-pin **TO-92 enclosure**, it is often described as the "FET equivalent of the 2N3904 NPN transistor".

Designed for low-power signal switching, LED indicators, small relay coil drivers, and bidirectional $3.3\text{V} \leftrightarrow 5.0\text{V}$ $I^2C$ logic level shifters, the 2N7000 handles drain-source voltages up to **$60\text{ Volts}$** and continuous drain currents up to **$200\text{ mA}$**. With a low gate threshold voltage ($V_{GS(th)}$ of **$0.8\text{V} \dots 3.0\text{V}$**), it turns on directly from 3.3V and 5V microcontroller GPIO output pins.

## Quick reference

| | |
|---|---|
| **Transistor Type** | Small-Signal N-Channel Enhancement Mode MOSFET |
| **Package** | TO-92 (Flat face front, leads pointing down) / SOT-23 (2N7002) |
| **Drain-Source Voltage ($V_{DSS}$)**| $60\text{ V}$ max |
| **Continuous Drain Current ($I_D$)**| $200\text{ mA}$ continuous ($500\text{ mA}$ pulsed) |
| **Gate-Source Voltage ($V_{GS}$)**  | $\pm 20\text{ V}$ max ($\pm 40\text{ V}$ peak transient) |
| **Gate Threshold Voltage ($V_{GS(th)}$)**| $0.8\text{ V}$ min to $3.0\text{ V}$ max ($1.8\text{ V}$ typical) |
| **On-State Resistance ($R_{DS(on)}$)**| $5.0\ \Omega$ at $V_{GS} = 10\text{V}$ / $5.3\ \Omega$ at $V_{GS} = 4.5\text{V}$ |
| **Turn-on / Turn-off Time** | $10\text{ ns}$ turn-on / $10\text{ ns}$ turn-off (High speed switching) |

## Pinout (TO-92 Package)

Looking at the **flat face** of the TO-92 package with leads pointing down:

```
        ┌─────────────┐
        │   2N7000    │  (Flat Package Face)
        └─┬───┬───┬───┘
          1   2   3
          S   G   D
```

| Pin | Name | Description |
|---|---|---|
| 1 | `SOURCE` (`S`) | Source terminal (Ground reference 0 V) |
| 2 | `GATE` (`G`) | Gate control terminal (Connect to MCU GPIO pin) |
| 3 | `DRAIN` (`D`) | Drain terminal (Low-side load connection) |

> [!WARNING]
> Pinout Warning: 2N7000 vs BS170 Pinouts!
> - **2N7000 (TO-92):** Pin 1 = Source, Pin 2 = Gate, Pin 3 = Drain (**S-G-D**).
> - **BS170 (TO-92):** Pin 1 = Drain, Pin 2 = Gate, Pin 3 = Source (**D-G-S**).
> - Always double-check part numbers before plugging replacement FETs into breadboards.

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Drain-Source Breakdown Volts| $V_{(BR)DSS}$| 60 | — | — | V | $V_{GS} = 0\text{V}, I_D = 10\ \mu\text{A}$ |
| Gate Threshold Voltage | $V_{GS(th)}$| 0.8 | 1.8 | 3.0 | V | $V_{DS} = V_{GS}, I_D = 1\text{mA}$ |
| Zero Gate Voltage Current | $I_{DSS}$ | — | — | 1.0 | µA | $V_{DS} = 48\text{V}, V_{GS} = 0\text{V}$ |
| On-Resistance ($V_{GS}=5.0\text{V}$)| $R_{DS(on)}$| — | 4.0 | 5.3 | Ω | $V_{GS} = 4.5\text{V}, I_D = 75\text{mA}$ |
| Power Dissipation | $P_D$ | — | — | 400 | mW | $T_A = 25^\circ\text{C}$ |

## Bidirectional 3.3V to 5V $I^2C$ Level Shifter Circuit

A single 2N7000 MOSFET converts a $3.3\text{V}$ $I^2C$ bus signal (SDA/SCL) to a $5.0\text{V}$ $I^2C$ bus line:

```
        +3.3V Power Rail                    +5.0V Power Rail
              │                                   │
      [ R1 = 10kΩ Pullup ]               [ R2 = 10kΩ Pullup ]
              │                                   │
  3.3V MCU ───┴─── [Pin 1: SOURCE] ────┐          ├─── 5V I2C Sensor (SDA)
                        2N7000         │          │
                   [Pin 2: GATE] ──────┼── +3.3V  │
                                       │          │
                   [Pin 3: DRAIN] ─────┴──────────┘
```

## Common mistakes

- **Attempting to drive high-current loads (>200mA):** The 2N7000 has a relatively high $R_{DS(on)}$ resistance of **$5.0\ \Omega$**. Driving a $500\text{ mA}$ load creates $I^2 R = (0.5)^2 \times 5 = 1.25\text{ Watts}$ of dissipation, instantly overheating the $400\text{ mW}$ TO-92 package. For loads $>200\text{ mA}$, use a power MOSFET like the IRLZ44N.
- **Leaving gate pin floating:** MOSFET gates act as tiny capacitors. Leaving the gate disconnected allows static electricity to turn the transistor partially ON. Include a $10\ \text{k}\Omega$ pull-down resistor to GND.

## Notes

- **2N7000 vs 2N7002 vs BS170:** 2N7000 is TO-92 (S-G-D); 2N7002 is SOT-23 SMD version; BS170 is TO-92 with reversed (D-G-S) pinout.
