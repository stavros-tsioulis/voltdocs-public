## Overview

The **LTC3780EG** (Linear Technology, now Analog Devices) is a high-performance, synchronous 4-switch buck-boost switching regulator controller IC supplied in a 24-lead SSOP package (`EG` suffix, $-40^\circ\text{C}$ to $+85^\circ\text{C}$). 

Unlike standard buck regulators (which require $V_{IN} > V_{OUT}$) or boost regulators (which require $V_{IN} < V_{OUT}$), the LTC3780 seamlessly regulates an output voltage that can be **above, below, or equal to the input voltage** ($V_{IN} = 4.0\text{ V} \dots 36.0\text{ V}$, $V_{OUT} = 0.8\text{ V} \dots 30.0\text{ V}$) using a single power inductor. By driving four external N-channel power MOSFETs in a full H-bridge bridge configuration, the controller can deliver continuous currents of **$10\text{ A}$ or more** at peak efficiencies exceeding **$98\%$**.

In maker, solar, and robotic projects, the LTC3780 is best known as the core controller of heavy-duty aluminum-heatsinked DC-DC modules (commonly titled "LTC3780 Automatic Step-Up/Step-Down Converter 10A"). These modules feature three multi-turn calibration trimpots:
1. **Output Voltage ($V_{OUT}$):** Sets the regulated output voltage.
2. **Current Limit ($I_{LIMIT}$):** Sets the constant-current (CC) charging or overload threshold.
3. **Undervoltage Lockout ($UVLO$):** Protects source batteries (e.g. 12V automotive or solar lead-acid/LiFePO4) from destructive over-discharge.

## Quick reference

| Parameter | Value | Notes |
|---|---|---|
| **Controller Architecture** | 4-Switch Synchronous Buck-Boost | Single inductor, 4 external N-MOSFETs |
| **Input Voltage Range ($V_{IN}$)** | $4.0\text{ V}$ to $36.0\text{ V}$ DC | Absolute maximum $40.0\text{ V}$ |
| **Output Voltage Range ($V_{OUT}$)** | $0.8\text{ V}$ to $30.0\text{ V}$ DC | Set via feedback resistor divider |
| **Continuous Output Current** | Up to $10.0\text{ A}$ (typ. module rating) | Scalable with external MOSFETs and cooling |
| **Peak Electrical Efficiency** | Up to $98\%$ | Synchronous rectification on all 4 switches |
| **Operating Frequency ($f_{OSC}$)** | $200\text{ kHz}$ to $400\text{ kHz}$ | Phase-lockable to external clock |
| **Gate Drive Capability** | Strong $1.5\ \Omega$ drivers | Drives high-current logic/sub-logic MOSFETs |
| **Protection Modes** | Current Foldback, Output OVP, UVLO | Complete battery and load protection |
| **Package** | 24-lead SSOP (Narrow 5.30 mm) | Also available in 32-lead QFN |

## Terminals

### LTC3780EG IC Pinout (24-lead SSOP)

| Pin | Name | Description | Pin | Name | Description |
|---|---|---|---|---|---|
| 1 | `PGOOD` | Power Good indicator (open-drain) | 13 | `VOSENSE` | Output voltage feedback input ($0.800\text{ V}$) |
| 2 | `SS` | Soft-start programming pin | 14 | `SENSE-` | Current sense amplifier negative input |
| 3 | `SBOOST4` | Gate driver boost for switch D | 15 | `SENSE+` | Current sense amplifier positive input |
| 4 | `TG2` | Top gate drive output for switch D | 16 | `ITH` | Current control loop compensation node |
| 5 | `SW2` | Switch node 2 (inductor to output) | 17 | `SGND` | Low-noise signal ground |
| 6 | `BG2` | Bottom gate drive output for switch C | 18 | `PLLFLTR` | Phase-locked loop filter capacitor |
| 7 | `PGND` | Power ground return for gate drivers | 19 | `PLLIN` | External synchronization clock input |
| 8 | `BG1` | Bottom gate drive output for switch B | 20 | `FCB` | Forced continuous / Burst mode select |
| 9 | `SW1` | Switch node 1 (input to inductor) | 21 | `EXTVCC` | External gate drive bias supply input |
| 10 | `TG1` | Top gate drive output for switch A | 22 | `INTVCC` | Internal 6V LDO gate drive supply |
| 11 | `BOOST1` | Gate driver boost for switch A | 23 | `VIN` | Main input supply sense pin |
| 12 | `STBYMD` | Standby mode / micro-power control | 24 | `RUN` | Run / enable control input |

### Common 10A breakout module terminal block

| Terminal | Name | Type | Description |
|---|---|---|---|
| `IN+` | Input Positive | Power Input | $+5\text{ V}$ to $+32\text{ V}$ DC source (solar, vehicle battery, power brick) |
| `IN-` | Input Negative | Power Ground | Common ground power return ($0\text{ V}$) |
| `OUT+` | Output Positive | Power Output | Regulated DC output ($+1.0\text{ V}$ to $+30\text{ V}$ DC, up to $10\text{ A}$) |
| `OUT-` | Output Negative | Power Ground | Output load ground return |

*Module Trimmer Potentiometers:*
- `CV` (Constant Voltage): Adjusts output voltage ($1.0\text{ V} - 30\text{ V}$).
- `CC` (Constant Current): Adjusts maximum current limit ($0.5\text{ A} - 10\text{ A}$) for LED driving or battery charging.
- `UV` (Under-Voltage): Sets input cutoff threshold to prevent over-discharging source batteries.

## The technical core

### 4-Switch buck-boost topology

The power stage comprises four N-channel MOSFET switches ($A, B, C, D$) and a single power inductor ($L_1$):

```
         [Switch A] (TG1)                 [Switch D] (TG2)
  VIN o-------/  ----------------+-----------  /  --------o VOUT
             |                   |            |
             |                 [L1]           |
             |                   |            |
          [Switch B] (BG1)       |         [Switch C] (BG2)
             |                   |            |
  GND o------+-------------------+------------+-----------o GND
```

The proprietary Linear Technology control scheme operates seamlessly in three distinct operating regions:
1. **Buck Region ($V_{IN} > 1.2 \times V_{OUT}$):** Switch $D$ is held continuously ON, switch $C$ is held OFF. Switches $A$ and $B$ modulate as a standard synchronous step-down buck converter.
2. **Boost Region ($V_{IN} < 0.8 \times V_{OUT}$):** Switch $A$ is held continuously ON, switch $B$ is held OFF. Switches $C$ and $D$ modulate as a standard synchronous step-up boost converter.
3. **Buck-Boost Region ($V_{IN} \approx V_{OUT}$):** The controller smoothly interleaves switching between buck and boost modes, maintaining rock-solid output regulation without instability or output voltage glitching during transitions (e.g. as an automotive battery dips from $14.4\text{ V}$ during charging to $9.0\text{ V}$ during engine cranking while maintaining a fixed $12.0\text{ V}$ output).

### Electrical specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Voltage Range | $V_{IN}$ | 4.0 | 12.0 / 24.0 | 36.0 | V | Operating supply |
| Feedback Reference Voltage | $V_{OSENSE}$ | 0.792 | 0.800 | 0.808 | V | Accuracy over temp |
| Output Voltage Range | $V_{OUT}$ | 0.8 | — | 30.0 | V | Resistor programmed |
| Oscillator Frequency | $f_{OSC}$ | 200 | 300 | 400 | kHz | Set by external resistor |
| Gate Driver Peak Current | $I_{PEAK\_DRV}$ | — | 1.5 | — | A | Sourcing/sinking |
| Gate Driver Rise/Fall Time | $t_r, t_f$ | — | 20 | — | ns | $C_L = 3300\text{ pF}$ |
| Quiescent Current | $I_Q$ | — | 2.5 | 4.0 | mA | Normal operating mode |
| Shutdown Current | $I_{SHDN}$ | — | 15 | 30 | µA | `RUN` = Low |
| Current Sense Threshold | $V_{SENSE(MAX)}$ | 125 | 150 | 175 | mV | Max current trip |

## Usage

### Adjusting breakout modules for battery charging (CC/CV)

To configure an LTC3780 module as a lead-acid or Li-ion battery charger:
1. **Set Undervoltage Protection (UV):** Supply the module from your input power source set to the lowest permissible cutoff voltage (e.g. $10.5\text{ V}$ for a $12\text{ V}$ lead-acid battery). Turn the `UV` trimpot until the fault LED illuminates.
2. **Set Output Voltage (CV):** With no load connected to `OUT`, measure output voltage with a multimeter. Adjust the `CV` trimpot until the target charge voltage is reached (e.g. $14.4\text{ V}$ absorption voltage).
3. **Set Current Limit (CC):** Rotate the `CC` trimpot counter-clockwise $\approx 20$ turns. Connect a digital multimeter set to 10A or 20A DC current mode directly across `OUT+` and `OUT-` (the module is short-circuit protected). Slowly rotate `CC` clockwise until the multimeter reads the desired maximum charge current (e.g. $4.0\text{ A}$). Disconnect multimeter immediately.

## Common mistakes

- **Inadequate cooling at high power:** At $12\text{V} \to 24\text{V}$ conversion at $8\text{ A}$ ($192\text{ W}$), even at $95\%$ efficiency the board must dissipate $\approx 10\text{ W}$ of heat. The small aluminum heatsink will exceed $90^\circ\text{C}$ in minutes without forced fan airflow.
- **Exceeding 36V input voltage:** Applying more than $36\text{ V}$ (such as an open-circuit $24\text{ V}$ solar panel that outputs $44\text{ V}$ on a cold sunny day) will destroy the input MOSFETs and the LTC3780 `VIN` pin.
- **Running long input cables without bulk electrolytic decoupling:** High-frequency $di/dt$ switching currents cause severe inductive ring spikes on long battery leads that exceed the $40\text{ V}$ absolute maximum breakdown rating. Add at least $470\ \mu\text{F}$ of low-ESR electrolytic capacitance at the module input terminals.

## Notes

- **LTC3780 vs Monolithic Converters:** Monolithic converters (like the TPS63020) integrate internal MOSFETs and are limited to $2\text{ A} - 4\text{ A}$ at under $5.5\text{ V}$. The LTC3780 is an external gate controller capable of handling hundreds of watts across industrial $12\text{ V}$, $24\text{ V}$, and $28\text{ V}$ voltage rails.
