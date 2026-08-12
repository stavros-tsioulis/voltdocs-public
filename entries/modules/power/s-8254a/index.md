## Overview

The **S-8254A** (specifically **S-8254AA** in a 16-pin TSSOP package) is a high-accuracy protection IC for **3-series or 4-series cell** lithium-ion / lithium-polymer rechargeable battery packs, manufactured by ABLIC (formerly Seiko Instruments). 

It continuously monitors individual cell voltages ($V_{C1} \dots V_{C4}$) and battery pack charge/discharge currents, controlling external N-channel MOSFET switches to protect against **overcharge**, **overdischarge**, **discharge overcurrent**, and **short circuit** conditions.

With extremely low operating power consumption ($30\ \mu\text{A}$ max operating, $0.1\ \mu\text{A}$ max power-down), the S-8254A prevents battery pack degradation and thermal runaway in power tools, E-bikes, robotics, and portable multi-cell battery packs.

## Quick reference

| | |
|---|---|
| **Protection Type** | 3-Series / 4-Series Cell Li-Ion Battery Protection Controller |
| **Package** | 16-Pin TSSOP |
| **Operating Voltage Range ($V_{DD}$)** | $2.0\text{ V}$ to $24.0\text{ V}$ DC |
| **Cell Configuration** | 3 Cells or 4 Cells in Series (Configurable via `SEL` pin) |
| **Overcharge Detection ($V_{CU}$)** | $4.0\text{ V}$ to $4.4\text{ V}$ ($\pm 25\text{ mV}$ accuracy) |
| **Overdischarge Detection ($V_{DL}$)** | $2.0\text{ V}$ to $3.0\text{ V}$ ($\pm 80\text{ mV}$ accuracy) |
| **Current Consumption** | Operating: $30\ \mu\text{A}$ max / Power-down: $0.1\ \mu\text{A}$ max |
| **Gate Drive Outputs** | `COP` (Charge Control N-MOS FET), `DOP` (Discharge Control N-MOS FET) |

## Pinout (16-Pin TSSOP Package)

```
        ┌──────────────┐
   COP ─│ 1         16 │─ NC
   DOP ─│ 2         15 │─ NC
   VMP ─│ 3         14 │─ NC
  DOPD ─│ 4         13 │─ SEL
  COPD ─│ 5         12 │─ VSS
   CTL ─│ 6         11 │─ VC4
   VDD ─│ 7         10 │─ VC3
   VC1 ─│ 8          9 │─ VC2
        └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `COP` | FET gate drive output pin for charge control MOSFET |
| 2 | `DOP` | FET gate drive output pin for discharge control MOSFET |
| 3 | `VMP` | Voltage monitor input pin (connects to charger / load positive voltage sense) |
| 4 | `DOPD` | Capacitor pin for setting overdischarge current detection delay time |
| 5 | `COPD` | Capacitor pin for setting overcharge detection delay time |
| 6 | `CTL` | Charge/discharge control input pin (Forced shutdown control) |
| 7 | `VDD` | Power supply input pin (connects to highest cell potential $V_{C4}$) |
| 8 | `VC1` | Voltage sense input for Cell 1 positive / Cell 2 negative |
| 9 | `VC2` | Voltage sense input for Cell 2 positive / Cell 3 negative |
| 10 | `VC3` | Voltage sense input for Cell 3 positive / Cell 4 negative |
| 11 | `VC4` | Voltage sense input for Cell 4 positive |
| 12 | `VSS` | Power supply ground reference pin (connects to Cell 1 negative) |
| 13 | `SEL` | Cell select pin: Connect to `VDD` for 4-cell mode; connect to `VSS` for 3-cell mode |
| 14–16 | `NC` | No internal connection |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Operating Voltage Range | $V_{DD}$ | 2.0 | — | 24.0 | V | Power supply voltage |
| Overcharge Voltage | $V_{CU}$ | 4.225 | 4.250 | 4.275 | V | $S-8254AA$ version |
| Overcharge Release Volts | $V_{CL}$ | 4.000 | 4.050 | 4.100 | V | Overcharge hysteresis |
| Overdischarge Voltage | $V_{DL}$ | 2.620 | 2.700 | 2.780 | V | $S-8254AA$ version |
| Overdischarge Release | $V_{DU}$ | 2.900 | 3.000 | 3.100 | V | Overdischarge hysteresis |
| Discharge Overcurrent 1 | $V_{IOV1}$ | 0.170 | 0.200 | 0.230 | V | Sense resistor voltage drop threshold |
| Short Circuit Protection | $V_{SHORT}$ | 1.000 | 1.200 | 1.400 | V | Short circuit voltage drop threshold |
| Operating Current | $I_{OPE}$ | — | 15.0 | 30.0 | $\mu\text{A}$ | Normal operation ($V_{CELL} = 3.5\text{V}$) |
| Power-Down Current | $I_{PDN}$ | — | — | 0.1 | $\mu\text{A}$ | Overdischarge state ($V_{CELL} = 2.0\text{V}$) |

## Typical Application Circuit (4-Series Cell BMS)

```
        +V_CELL4 (B4+) ───────┬──────────── [Pin 7: VDD]  S-8254A Protection IC
                              │
        +V_CELL3 (B3+) ───────┼──────────── [Pin 11: VC4]
                              │
        +V_CELL2 (B2+) ───────┼──────────── [Pin 10: VC3]
                              │
        +V_CELL1 (B1+) ───────┼──────────── [Pin 9: VC2]
                              │
        -V_CELL1 (B1-) ───────┼──────────── [Pin 8: VC1]
                              │
         PACK- GND ───────────┴──────────── [Pin 12: VSS]
                              │
                             [Pin 1: COP] ──> Charge FET Gate
                             [Pin 2: DOP] ──> Discharge FET Gate
```

## Common mistakes

- **Leaving the SEL pin floating:** `SEL` configures 3-cell vs 4-cell protection mode. Connect `SEL` to `VDD` for 4-series cell packs; connect `SEL` to `VSS` (and short $V_{C4}$ to $V_{C3}$) for 3-series cell packs.
- **Incorrect Sense Resistor sizing:** Overcurrent detection relies on sensing voltage drop across external MOSFETs or sense resistors between `VSS` and `VMP`. Sizing resistors incorrectly causes false overcurrent trips or delayed short-circuit response.

## Notes

- **3S/4S Protection Standard:** The S-8254A is one of the most widely deployed dedicated hardware 3S/4S BMS ICs, offering standalone protection without needing an external microcontroller.
