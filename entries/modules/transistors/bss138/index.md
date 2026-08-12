## Overview

The **BSS138** is a low-threshold N-channel Enhancement Mode MOSFET IC manufactured by ON Semiconductor, Fairchild, and Diodes Inc. Packaged in a 3-pin surface-mount **SOT-23 enclosure**, it is famous as the core switching element behind bidirectional $3.3\text{V} \leftrightarrow 5.0\text{V}$ $I^2C$ logic level converter modules (such as Adafruit, SparkFun, and generic AliExpress 4-channel level shifter boards).

Offering a maximum drain-source breakdown voltage of **$50\text{ Volts}$**, continuous drain current of **$220\text{ mA}$**, and a low gate threshold voltage ($V_{GS(th)}$ of **$0.8\text{V} \dots 1.5\text{V}$**), the BSS138 turns on fully at low gate voltages ($2.8\text{V} \dots 3.3\text{V}$), making it ideal for low-voltage sensor interfacing.

## Quick reference

| | |
|---|---|
| **Transistor Type** | N-Channel Logic-Level Enhancement Mode MOSFET |
| **Package** | SOT-23 (3-pin SMD) |
| **Drain-Source Voltage ($V_{DSS}$)**| $50\text{ V}$ max |
| **Continuous Drain Current ($I_D$)**| $220\text{ mA}$ continuous ($880\text{ mA}$ pulsed) |
| **Gate-Source Voltage ($V_{GS}$)**  | $\pm 20\text{ V}$ max |
| **Gate Threshold Voltage ($V_{GS(th)}$)**| $0.8\text{ V}$ min to $1.5\text{ V}$ max ($1.3\text{ V}$ typical) |
| **On-State Resistance ($R_{DS(on)}$)**| $3.5\ \Omega$ at $V_{GS} = 10\text{V}$ / $6.0\ \Omega$ at $V_{GS} = 4.5\text{V}$ |
| **Turn-on / Turn-off Speed** | $2.5\text{ ns}$ turn-on / $9\text{ ns}$ turn-off (Ultra fast) |

## Pinout (SOT-23 Package)

Looking at the top of the SOT-23 surface-mount component with single lead on top:

```
               ┌─────────┐
               │    3    │  (DRAIN)
               └─┐     ┌─┘
                 │BSS138│
               ┌─┘     └─┐
               │ 1     2 │
               └─────────┘
            (GATE)   (SOURCE)
```

| Pin | Name | Description |
|---|---|---|
| 1 | `GATE` (`G`) | Gate control input (Connect to 3.3V power rail in level shifters) |
| 2 | `SOURCE` (`S`) | Source terminal (Low-voltage 3.3V bus side) |
| 3 | `DRAIN` (`D`) | Drain terminal (High-voltage 5.0V bus side) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Drain-Source Voltage | $V_{DSS}$ | 50 | — | — | V | $V_{GS} = 0\text{V}, I_D = 100\ \mu\text{A}$ |
| Gate Threshold Voltage | $V_{GS(th)}$| 0.8 | 1.3 | 1.5 | V | $V_{DS} = V_{GS}, I_D = 1\text{mA}$ |
| On-Resistance ($V_{GS}=10\text{V}$)| $R_{DS(on)}$| — | 1.4 | 3.5 | Ω | $V_{GS} = 10\text{V}, I_D = 220\text{mA}$ |
| On-Resistance ($V_{GS}=4.5\text{V}$)| $R_{DS(on)}$| — | 1.8 | 6.0 | Ω | $V_{GS} = 4.5\text{V}, I_D = 220\text{mA}$ |
| Input Capacitance | $C_{iss}$ | — | 27 | 50 | pF | $V_{DS} = 25\text{V}, f = 1\text{MHz}$ |

## Bidirectional $I^2C$ Level Shifter Circuit (1 Channel)

```
        +3.3V Power Rail                    +5.0V Power Rail
              │                                   │
      [ R1 = 10kΩ Pullup ]               [ R2 = 10kΩ Pullup ]
              │                                   │
  3.3V MCU ───┴─── [Pin 2: SOURCE] ────┐          ├─── 5V Sensor (SDA/SCL)
                        BSS138         │          │
                   [Pin 1: GATE] ──────┼── +3.3V  │
                                       │          │
                   [Pin 3: DRAIN] ─────┴──────────┘
```

## Common mistakes

- **Using BSS138 for high-power DC load switching:** BSS138 has an $R_{DS(on)}$ up to **$6.0\ \Omega$**. Passing more than $200\text{ mA}$ results in substantial thermal dissipation in the SOT-23 package. Use a low-resistance MOSFET like the AO3400 for driving motors or LEDs.
- **Forgetting pull-up resistors in level shifter circuits:** The BSS138 level shifter circuit relies on external pull-up resistors (typically $10\text{ k}\Omega$) on both the 3.3V and 5V sides. Without pull-up resistors, lines cannot be pulled HIGH.

## Notes

- **BSS138 vs 2N7002:** BSS138 has a lower $V_{GS(th)}$ max ($1.5\text{V}$ vs $2.5\text{V}$) and faster switching speed ($2.5\text{ ns}$ vs $7\text{ ns}$), making it the preferred choice over 2N7002 for $3.3\text{V}$ $I^2C$ level shifter circuits.
