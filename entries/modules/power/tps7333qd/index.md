## Overview

The **TPS7333** (including the **TPS7333QD** SOIC-8 variant) is a low-dropout (LDO) linear voltage regulator manufactured by Texas Instruments. It combines a fixed **+3.3 V DC output** (up to 500 mA) with an integrated **microprocessor power-on reset supervisor** and an active-high Enable (`EN`) input in an 8-pin package.

Unlike conventional bipolar LDOs, the TPS7333 uses a **PMOS pass transistor**, which achieves extremely low dropout voltages ($300\text{ mV}$ typical at $500\text{ mA}$ load) and maintains a low quiescent current of $340\ \mu\text{A}$ virtually independent of load current. The integrated supervisory circuit monitors $V_{OUT}$ and holds the active-low `RESET` output LOW during power-up or undervoltage faults, releasing it with an internal **$200\text{ ms}$ delay** once $V_{OUT}$ reaches stable regulation.

## Quick reference

| | |
|---|---|
| **Regulator Type** | PMOS Micropower Low-Dropout (LDO) Regulator + Integrated Reset |
| **Package** | 8-pin SOIC (`D` suffix, e.g. TPS7333QD) / 8-pin PDIP (`P` suffix) |
| **Output Voltage** | Fixed $+3.3\text{ V}$ DC ($\pm 2.0\%$ accuracy across load/line/temp) |
| **Input Voltage Range ($V_{IN}$)** | $3.77\text{ V}$ to $10.0\text{ V}$ DC ($11.0\text{ V}$ absolute maximum) |
| **Max Output Current** | $500\text{ mA}$ continuous |
| **Dropout Voltage** | $300\text{ mV}$ typ ($440\text{ mV}$ max) at $I_{OUT} = 500\text{ mA}$ |
| **Quiescent Current ($I_Q$)** | $340\ \mu\text{A}$ typ ($385\ \mu\text{A}$ max at $500\text{ mA}$ load) |
| **Reset Delay Time ($t_{d}$)** | $200\text{ ms}$ typ ($130\text{ ms} \dots 270\text{ ms}$) |
| **Reset Threshold Voltage** | $3.12\text{ V}$ typ ($95\%$ of nominal $V_{OUT}$) |

## Pinout (SOIC-8 / PDIP-8)

```
             ┌───┴───┐
      OUTPUT 1│ 1    8│ OUTPUT
       SENSE 2│       │7 INPUT
         GND 3│TPS7333│6 INPUT
          EN 4│       │5 /RESET
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1, 8 | `OUTPUT` | Power Output | Regulated +3.3V DC power output (pins 1 and 8 internally connected) |
| 2 | `SENSE` | Analog Input | Output voltage feedback sense input; must be connected directly to `OUTPUT` at the load |
| 3 | `GND` | Power | Ground reference (0 V) |
| 4 | `EN` | Digital Input | Active-High regulator enable input ($>2.0\text{V}$ = ON, $<0.5\text{V}$ = Shutdown). Connect to $V_{IN}$ if unused |
| 5 | `/RESET` | Digital Output | Active-Low power-on reset output (open-drain with internal pull-up); 200 ms delay |
| 6, 7 | `INPUT` | Power Input | Unregulated DC supply input (+3.77V to +10.0V DC; pins 6 and 7 internally connected) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Output Voltage | $V_{OUT}$ | 3.23 | 3.30 | 3.37 | V | $3.77\text{V} \le V_{IN} \le 10.0\text{V}, 5\text{mA} \le I_{OUT} \le 500\text{mA}$ |
| Dropout Voltage | $V_{DO}$ | — | 300 | 440 | mV | $I_{OUT} = 500\text{ mA}, V_{IN} = 3.23\text{ V}$ |
| Ground Current | $I_{GND}$ | — | 340 | 385 | µA | $I_{OUT} = 500\text{ mA}, V_{IN} = 4.3\text{ V}$ |
| Standby Current | $I_{STBY}$ | — | 0.5 | 1.0 | µA | $\text{EN} \le 0.5\text{ V}$ (Shutdown mode) |
| Reset Threshold | $V_{IT-}$ | 3.04 | 3.12 | 3.20 | V | $V_{OUT}$ decreasing |
| Reset Hysteresis | $V_{hys}$ | 20 | 35 | 50 | mV | $V_{OUT}$ rising vs falling |
| Reset Delay Time | $t_d$ | 130 | 200 | 270 | ms | Output valid to `/RESET` high transition |
| Reset Output Low | $V_{OL}$ | — | 0.15 | 0.4 | V | $I_{SINK} = 1.6\text{ mA}, V_{IN} = 3.77\text{ V}$ |

## Typical Application Circuit

```
       +5V DC Supply In
           │
      ┌────┴────────────────────────┐
      │                             │
 [Pin 4: EN]                 [Pin 6, 7: INPUT]
                               TPS7333QD
                             [Pin 1, 8: OUTPUT] ────┬──────────────┬──── +3.3V Output Rail
                                    │               │              │
                              [Pin 2: SENSE] ───────┘    [ C2: 10µF Solid Tantalum ]
                                    │                              │
                               [Pin 3: GND]                       GND
                                    │
 [Pin 5: /RESET] ──────────┐       GND
                           │
                           ▼
             MCU Reset Pin (/RESET, NRST)
```

> [!IMPORTANT]
> **Output Capacitor ESR Requirement:**
> - To maintain stability of the PMOS regulator loop, the output capacitor ($C_{OUT}$) must have a capacitance $\ge 4.7\ \mu\text{F}$ (recommended $\ge 10\ \mu\text{F}$) and an Equivalent Series Resistance (**ESR**) between **$0.05\ \Omega$ and $1.5\ \Omega$**. Solid tantalum capacitors are recommended.
> - When using multi-layer ceramic capacitors (MLCCs) with extremely low ESR ($< 0.05\ \Omega$), insert a small resistor ($0.2\ \Omega \dots 0.5\ \Omega$) in series with the ceramic capacitor.

## Common mistakes

- **Leaving `SENSE` (Pin 2) unconnected:** Pin 2 provides remote voltage sensing for the feedback control loop. If Pin 2 is left floating, $V_{OUT}$ will drift uncontrolled or shut down. Always tie Pin 2 directly to Pins 1/8 (`OUTPUT`).
- **Leaving `EN` (Pin 4) floating:** The enable input has high input impedance. If left unconnected, capacitive noise can arbitrarily toggle the regulator on and off. Tie `EN` directly to `INPUT` (Pins 6/7) if enable switching is not required.
- **Overlooking the 200ms reset pulse:** Microcontroller code that boots up before `RESET` is released will be held in hardware reset for $\sim 200\text{ ms}$. This is by design to protect against power-brownout corrupted boot memory.

## Notes

- **TPS73xx Family Fixed & Adjustable Variants:** TPS7330 (3.0V), **TPS7333 (3.3V)**, TPS7348 (4.85V), TPS7350 (5.0V), TPS7301 (Adjustable 1.2V to 9.75V).
