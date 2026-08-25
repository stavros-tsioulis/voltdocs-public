## Overview

The **STP16NF06** is a $60\text{V}$ $16\text{A}$ N-channel power MOSFET manufactured by STMicroelectronics using proprietary **STripFET II** planar technology. Available in a standard through-hole **TO-220-3** package (and surface-mount **DPAK** as STD16NF06), it is one of the most widespread European-sourced power MOSFETs found in educational electronics labs, robotics kits, and DIY hardware designs across Europe.

Featuring a drain-to-source breakdown voltage of **$60\text{V}$**, a continuous current rating of **$16\text{A}$ at $25^\circ\text{C}$**, a typical on-resistance of **$70\text{ m}\Omega$ ($0.07\ \Omega$) at $V_{GS} = 10\text{V}$**, and an exceptionally low total gate charge of **$14.5\text{ nC}$**, the STP16NF06 switches rapidly with minimal drive power. It is ideal for **$12\text{V} \dots 24\text{V}$ brushed DC motor control, solenoid and valve actuators, 3D printer hotend/fan switching, and audio amplifier power supply rails**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | N-Channel STripFET II Power MOSFET |
| **Package** | TO-220-3 (through-hole) / DPAK (STD16NF06 SMD) |
| **Drain-Source Voltage ($V_{DSS}$)** | $60\text{ V}$ max |
| **Continuous Drain Current ($I_D$)** | **$16\text{ A}$** at $T_C = 25^\circ\text{C}$ ($11.3\text{ A}$ at $100^\circ\text{C}$) |
| **Pulsed Drain Current ($I_{DM}$)** | **$64\text{ A}$** |
| **On-Resistance ($R_{DS(on)}$ at 10V)**| **$70\text{ m}\Omega$ typ / $80\text{ m}\Omega$ ($0.08\ \Omega$) max** |
| **Gate Threshold Voltage ($V_{GS(th)}$)**| **$2.0\text{ V}$ to $4.0\text{ V}$** (Requires $10\text{V} \dots 12\text{V}$ gate drive) |
| **Total Gate Charge ($Q_g$)** | **$14.5\text{ nC}$ typ** ($20\text{ nC}$ max) |
| **Total Power Dissipation ($P_D$)** | $45\text{ Watts}$ ($T_C = 25^\circ\text{C}$) |
| **Operating Junction Temp** | $-55^\circ\text{C}$ to $+175^\circ\text{C}$ |

## Pinout (TO-220-3 Package)

Looking at the **front labeled face** with leads pointing downward:

```
        ┌──────────────┐
        │  O  [Metal]  │ ── Tab is internally connected to Pin 2 (Drain)
        ├──────────────┤
        │  STP16NF06   │
        └─┬────┬────┬──┘
          1    2    3
          G    D    S
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GATE` | Gate Input | Gate control terminal (Drive with $10\text{V} \dots 15\text{V}$ for full saturation) |
| 2 (Tab) | `DRAIN` | Power Drain | Drain switching terminal (Internally connected to metal mounting tab) |
| 3 | `SOURCE`| Power Source | Source terminal (Connect to ground or negative return rail) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Drain-Source Breakdown | $V_{(BR)DSS}$ | 60 | — | — | V | $V_{GS} = 0\text{V}, I_D = 250\ \mu\text{A}$ |
| Static Drain-Source $R_{DS(on)}$ | $R_{DS(on)}$ | — | 70 | 80 | mΩ | $V_{GS} = 10\text{V}, I_D = 8.0\text{A}$ |
| Gate Threshold Voltage | $V_{GS(th)}$ | 2.0 | — | 4.0 | V | $V_{DS} = V_{GS}, I_D = 250\ \mu\text{A}$ |
| Drain-Source Leakage | $I_{DSS}$ | — | — | 1.0 | µA | $V_{DS} = 60\text{V}, V_{GS} = 0\text{V}$ |
| Gate-Body Leakage Current | $I_{GSS}$ | — | — | $\pm 100$ | nA | $V_{GS} = \pm 20\text{V}$ |
| Diode Forward Voltage | $V_{SD}$ | — | — | 1.5 | V | $I_S = 16\text{A}, V_{GS} = 0\text{V}$ |
| Thermal Resistance | $R_{\theta JC}$ | — | — | 3.33 | °C/W | Junction-to-Case |

## Typical Application Circuit: 12V/24V DC Motor PWM Speed Controller

```
                      +12V to +24V DC Motor Supply
                                   │
                               [ + DC Motor - ]
                                   │
                                   ├───[ Flyback Catch Diode (e.g. 1N5822 / MBR360) ]───┐
                                   │   (Anode to Drain, Cathode to +Supply)             │
                             [Pin 2: DRAIN]                                             │
                                STP16NF06                                               │
  MCU PWM Signal (via driver)[Pin 1: GATE]                                              │
  (e.g. TC4427 / BJT Driver)       │                                                    │
          │                        ├───[ 10kΩ Gate Pull-Down Resistor ]─────────────────┤
          ├───[ 22Ω Gate Resistor ]┤                                                    │
         GND                       │                                                    │
                             [Pin 3: SOURCE]                                            │
                                   │                                                    │
                                  GND ──────────────────────────────────────────────────┴─── Common GND
```

## Comparison: STP16NF06 vs IRFZ44N vs FQP30N06L

| Parameter | STP16NF06 | IRFZ44N | FQP30N06L |
|---|---|---|---|
| **$V_{DSS}$ Rating** | $60\text{ V}$ | $55\text{ V}$ | $60\text{ V}$ |
| **Max Current ($I_D$)** | $16\text{ A}$ | $49\text{ A}$ | $32\text{ A}$ |
| **$R_{DS(on)}$ at 10V** | $70\text{ m}\Omega$ | $17.5\text{ m}\Omega$ | $35\text{ m}\Omega$ |
| **Gate Charge ($Q_g$)** | **$14.5\text{ nC}$ (Fast)** | $63\text{ nC}$ | $15\text{ nC}$ |
| **5V Logic Drive** | Standard ($10\text{V}$) | Standard ($10\text{V}$) | **Logic-Level ($4.5\text{V}$)** |

## Common mistakes

- **Driving directly from 3.3V or 5V MCU pins:** The standard STP16NF06 requires $10\text{V}$ on its gate for full conduction. If driven directly from 3.3V/5V microcontroller outputs, the channel will partially conduct and overheat under moderate currents. (For 5V logic drive, use the logic-level **STP16NF06L** or **FQP30N06L**).
- **Omitting the flyback diode with inductive loads:** Solenoids, relays, and brushed motors create hundreds of volts of back-EMF upon shutoff. Always place a fast Schottky catch diode directly across the load.

## Notes

- **Suffix Guide:** `STP16NF06` denotes standard 10V gate drive in TO-220; `STP16NF06L` denotes logic-level 5V gate drive; `STD16NF06` denotes SMD DPAK packaging.
