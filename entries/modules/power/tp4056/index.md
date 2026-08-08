## Overview

The **TP4056** is a 1.0 Amp standalone linear Lithium-Ion and Lithium-Polymer (LiPo) battery charger IC manufactured by NanJing Top Power. Sold worldwide as a cheap $1\text{cm} \times 2\text{cm}$ red or blue breakout module with Micro-USB or USB-C connectors (and frequently paired with a **DW01A battery protection IC** and **FS8205A dual MOSFET** for over-charge, over-discharge, and short-circuit protection), it safely charges single-cell **$3.7\text{V}$ Li-Ion / 18650 / LiPo cells** to a target voltage of **$4.20\text{V}$**.

Operating on a standard $5.0\text{V}$ USB power supply, the TP4056 implements a complete **Constant-Current / Constant-Voltage (CC/CV)** charging profile with programmable charge current (up to $1.0\text{A}$), thermal regulation, automatic recharge, and dual open-drain LED status outputs (`/CHRG` and `/STDBY`).

## Quick reference

| | |
|---|---|
| **Charger Type** | Constant-Current / Constant-Voltage (CC/CV) Linear Charger |
| **Package** | 8-pin SOP-8 with exposed bottom thermal pad / Breakout Board |
| **Input Supply Voltage (`VCC`)**| 4.0 V to 8.0 V DC (5.0 V USB nominal) |
| **Final Float Charge Voltage** | $4.20\text{ V}$ DC ($\pm 1.5\%$ accuracy) |
| **Max Programmable Charge Current**| $1.0\text{ A}$ ($1000\text{ mA}$, set by $R_{PROG}$ resistor) |
| **Precharge Trickle Threshold**| $2.9\text{ V}$ (Trickle charge at $10\%$ current for deeply discharged cells) |
| **Charge Status Indicators** | Red LED (`/CHRG` pin 7) = Charging / Blue or Green LED (`/STDBY` pin 6) = Fully Charged |
| **Battery Protection Pair** | DW01A protection IC + FS8205A dual N-MOSFET (on protected modules) |

## Pinout (SOP-8 Package & Module Terminals)

```
             ┌───┴───┐
        TEMP ─┤ 1   8 ├─ VCC
        PROG ─┤ 2   7 ├─ /CHRG
         GND ─┤ 3   6 ├─ /STDBY
         BAT ─┤ 4   5 ├─ CE
             └───────┘
```

| Module Pin Label | Name | Type | Description |
|---|---|---|---|
| `IN+` / `USB` | `VCC` | Power | Positive $5.0\text{V}$ DC power input from USB |
| `IN-` | `GND` | Power | Ground reference (0 V) |
| `BAT+` / `B+` | `BAT` | Battery Connection| Connects to positive lead of 3.7V Li-Ion / LiPo battery |
| `BAT-` / `B-` | `GND` / `Protection`| Battery Connection| Connects to negative lead of battery (via DW01A MOSFET on protected boards) |
| `OUT+` | `OUT+` | Load Power Output | Regulated load output (+) on protected module boards |
| `OUT-` | `OUT-` | Load Power Output | Load output ground (-) (cuts off at 2.4V battery protection threshold) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Supply Voltage | $V_{CC}$ | 4.0 | 5.0 | 8.0 | V | USB 5.0V input |
| Regulated Output Voltage| $V_{BAT}$ | 4.137 | 4.200 | 4.263 | V | $0^\circ\text{C} \le T_A \le 85^\circ\text{C}$ |
| Charge Current ($R_{PROG}=1.2\text{k}\Omega$)| $I_{BAT}$ | 900 | 1000 | 1050 | mA | RPROG = 1200 Ω |
| Trickle Charge Threshold| $V_{TRIKL}$| 2.8 | 2.9 | 3.0 | V | $V_{BAT}$ rising |
| C/10 Termination Current| $I_{TERM}$ | — | 0.1 | — | $\times I_{BAT}$| Charge cycle termination threshold |
| Shutdown Supply Current | $I_{MSD}$ | — | 55 | 100 | µA | $V_{CC}$ disconnected |

## Charge Current Programming ($R_{PROG}$ Resistor Table)

The continuous charge current ($I_{BAT}$) is programmed by resistor $R_{PROG}$ connected between Pin 2 (`PROG`) and GND:

$$ I_{BAT}\text{ (mA)} = \frac{1200\text{V}}{R_{PROG}\text{ (k}\Omega\text{)}} \times 1000 $$

| $R_{PROG}$ Resistor Value | Programmed Charge Current ($I_{BAT}$) | Recommended Battery Capacity |
|---|---|---|
| $1.2\ \text{k}\Omega$ (**Default on modules**) | $1000\text{ mA}$ ($1.0\text{A}$) | $\ge 1000\text{ mAh}$ (e.g. 18650 cell) |
| $1.66\ \text{k}\Omega$ | $700\text{ mA}$ | $\ge 700\text{ mAh}$ |
| $2.4\ \text{k}\Omega$ | $500\text{ mA}$ | $\ge 500\text{ mAh}$ |
| $5.0\ \text{k}\Omega$ | $250\text{ mA}$ | $\ge 250\text{ mAh}$ |
| $10.0\ \text{k}\Omega$ | $130\text{ mA}$ | $\ge 130\text{ mAh}$ (small LiPo cells) |

## CC/CV Charging Profile Stages

```
 Voltage (V) / Current (A)
   4.2V  ─────────────────────────────┐ (Constant Voltage Stage)
         │                           │ ╲
         │   (Constant Current)      │  ╲  Current Drops
   2.9V ─┼───────────────────────────┤   ╲  to C/10
   (0.1A)│---(Trickle Precharge)---- │    └── Charge Complete (STDBY LED ON)
   0V    └───────────────────────────┴─────────────────────── Time
```

1. **Trickle Precharge:** If battery voltage $< 2.9\text{V}$, the charger outputs $10\%$ of programmed current ($100\text{ mA}$) to safely recover deeply discharged cells.
2. **Constant Current (CC):** Once $V_{BAT} \ge 2.9\text{V}$, full programmed current ($1.0\text{A}$) is delivered to the battery while voltage rises toward $4.20\text{V}$.
3. **Constant Voltage (CV):** When $V_{BAT}$ reaches $4.20\text{V}$, voltage is held constant while charge current decays.
4. **Charge Termination:** When current drops to $C/10$ ($100\text{ mA}$), charging terminates, the red LED turns OFF, and the blue/green LED turns ON.

## Wiring (Protected TP4056 Breakout Module)

| TP4056 Module Pin | → | Power Source / Battery / Load | Notes |
|---|---|---|---|
| `IN+` / `USB` | | +5V USB Power Supply | Charge power input |
| `IN-` | | USB GND | Charge ground |
| `B+` | | Li-Ion / 18650 Battery (+) | Battery positive lead |
| `B-` | | Li-Ion / 18650 Battery (-) | Battery negative lead |
| `OUT+` | | MCU / System Load 5V/3.3V LDO | Load power positive output |
| `OUT-` | | MCU System Ground | Load power ground output |

## Common mistakes

- **Charging small LiPo batteries (<500mAh) at the default 1A rate:** Default TP4056 modules come pre-soldered with a $1.2\ \text{k}\Omega$ $R_{PROG}$ resistor ($1.0\text{A}$ charge rate). Charging small $100\text{ mAh}$ or $250\text{ mAh}$ LiPo cells at $1.0\text{A}$ ($4C \dots 10C$ rate) causes severe overheating and fire hazards. Desolder the $1.2\text{k}$ resistor and replace it with a $5\text{k}\Omega$ or $10\text{k}\Omega$ resistor for small LiPo cells.
- **Connecting battery in reverse polarity:** Connecting battery `+` to `B-` and `-` to `B+` instantly destroys the TP4056 IC.

## Notes

- **TP4056 vs MCP73831 vs BQ24160:** TP4056 is a low-cost 1A linear charger; MCP73831 is Microchip's 500mA linear charger; BQ24160 is a TI switch-mode charger.
