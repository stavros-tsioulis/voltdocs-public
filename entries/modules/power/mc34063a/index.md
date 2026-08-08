## Overview

The **MC34063A** (and industrial-grade **MC33063A**) is a monolithic control circuit containing the primary functions required for DC-to-DC converters. Originally designed by Motorola and now produced by ON Semiconductor, Texas Instruments, and STMicroelectronics, it contains an internal temperature-compensated reference, comparator, controlled duty cycle oscillator with active peak current limit circuit, driver, and a **1.5A high-current output switch**.

Unlike specialized single-topology regulators, the MC34063A is a **universal switcher** that can be configured into three fundamental topologies:
1. **Step-Down (Buck)** converter (e.g., 12V to 5V)
2. **Step-Up (Boost)** converter (e.g., 5V to 12V or 170V for Nixie tubes)
3. **Voltage Inverting** converter (e.g., +5V to -5V dual supply rail)

## Quick reference

| | |
|---|---|
| **Input Voltage (`VCC`)** | 3.0 V to 40.0 V DC |
| **Output Voltage Range** | Adjustable from 1.25 V to 40.0 V DC (or negative voltages) |
| **Max Peak Switch Current (`Ipk`)** | 1.5 A (expandable using external NPN/PNP transistor) |
| **Oscillator Frequency** | Up to 100 kHz ($C_T$ capacitor programmed) |
| **Internal Reference Voltage** | 1.25 V ($\pm 2\%$) |
| **Low Standby Current** | 2.5 mA typical |
| **Package** | 8-pin DIP / SOIC-8 |

## Pinout (DIP-8 Package)

```
             ┌───┴───┐
     Switch  │ 1   8 │ Driver Collector
  Collector  │       │
             │ 2   7 │ IPK Sense
      Switch │       │
    Emitter  │ 3   6 │ VCC
    Timing   │       │
  Capacitor  │ 4   5 │ Comparator Inverting Input
             └───────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `Switch Collector` | Collector of internal output Darlington NPN switch |
| 2 | `Switch Emitter` | Emitter of internal output Darlington NPN switch |
| 3 | `Timing Capacitor` | Connect timing capacitor $C_T$ to GND to set switching frequency |
| 4 | `GND` | Power and signal ground reference |
| 5 | `Comparator Inverting Input` | Feedback pin ($V_{TH} = 1.25\text{V}$) connected to output resistor divider |
| 6 | `VCC` | Positive power supply voltage pin (+3.0V to +40V DC) |
| 7 | `IPK Sense` | Peak current sense pin. Connected to $VCC$ through current sense resistor $R_{SC}$ |
| 8 | `Driver Collector` | Collector of internal driver transistor |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Power Supply Voltage | $V_{CC}$ | 3.0 | — | 40.0 | V | DC input |
| Output Switch Current | $I_{SW}$ | — | 1.0 | 1.5 | A | Continuous switch current |
| Saturation Voltage | $V_{CE(sat)}$ | — | 1.0 | 1.3 | V | Darlington switch at $I_{SW}=1.0\text{A}$ |
| Internal Reference Voltage | $V_{th}$ | 1.225 | 1.250 | 1.275 | V | $T_A = 25^\circ\text{C}$ |
| Current Limit Sense Voltage| $V_{ISENSE}$ | 250 | 300 | 350 | mV | Pin 7 to Pin 6 |
| Operating Frequency | $f_{OSC}$ | 24 | 33 | 42 | kHz | $C_T = 1.0\text{ nF}$ |

## Basic Configurations

### 1. Step-Down (Buck) Converter Circuit

```
            R_sc (Current Sense)
  VCC ─────███████───┬───────────────┬─────── [Pin 6: VCC]
                     │               │
                 [Pin 7: IPK]  [Pin 1: Sw Coll]
                               [Pin 8: Drv Coll]
                                     │
   GND ───┤<───┬───────────────[Pin 2: Sw Emit]
         Diode │                     │
            [Inductor L]       [Timing Cap C_T]
               │                     │
  VOUT ────────┴───[C_OUT]─── GND   GND
```

### Key Design Formulas

$$\text{Current Sense Resistor:} \quad R_{SC} = \frac{0.3\text{V}}{I_{PK}}$$

$$\text{Feedback Output Voltage:} \quad V_{OUT} = 1.25\text{V} \times \left(1 + \frac{R_2}{R_1}\right)$$

## Common mistakes

- **Omission of the current sense resistor $R_{SC}$:** Shorts Pin 7 to Pin 6 without a low-ohm sense resistor (e.g., $0.22\ \Omega \dots 0.5\ \Omega$). Without $R_{SC}$, overcurrent protection is disabled, causing immediate Destruction of the internal NPN switch when overloaded.
- **High voltage drop on internal Darlington switch:** The internal bipolar Darlington switch has a relatively high $V_{CE(sat)}$ of about $1.0\text{V} \dots 1.3\text{V}$. At high currents ($>0.75\text{A}$), the IC will get warm. Use an external MOSFET or external PNP transistor for efficiency above 80%.
- **Incorrect $C_T$ capacitor calculation:** If $C_T$ is chosen too large, the switching frequency drops into the audible range ($<20\text{ kHz}$), causing audible inductor whine.

## Notes

- **MC34063A vs MC33063A:** MC34063A is specified for $0^\circ\text{C}$ to $+70^\circ\text{C}$; MC33063A is industrial grade specified for $-40^\circ\text{C}$ to $+85^\circ\text{C}$.
