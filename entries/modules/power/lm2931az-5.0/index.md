## Overview

The **LM2931AZ-5.0** (LM2931) is a specialized automotive-grade positive low-dropout (LDO) linear voltage regulator manufactured by Texas Instruments and onsemi. Packaged in a compact 3-pin through-hole **TO-92** enclosure, it delivers a clean, regulated **$+5.0\text{V}$ DC** rail at up to **$100\text{ mA}$** from noisy, harsh vehicular power networks.

Specifically engineered to withstand extreme automotive electrical transients, the LM2931 provides built-in protection against **$+60\text{V}$ load-dump spikes, $-18\text{V}$ reverse battery connection, $-50\text{V}$ reverse inductive spikes, mirror-image pin insertion**, and thermal overload. With an exceptionally low dropout voltage ($160\text{ mV}$ typ at $10\text{mA}$ and $< 0.6\text{V}$ at $100\text{mA}$), it continues to maintain clean 5V regulation even during severe cold-cranking battery voltage sags.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Automotive Low-Dropout (LDO) Positive Linear Regulator |
| **Package** | TO-92 (3-pin through-hole) |
| **Output Voltage ($V_{OUT}$)** | $+5.0\text{ V}$ DC ($\pm 3.8\%$ over $-40^\circ\text{C} \dots 125^\circ\text{C}$) |
| **Operating Input Range ($V_{IN}$)** | $6.0\text{ V}$ to $26.0\text{ V}$ DC |
| **Transient Input Protection** | $+60\text{ V}$ Load Dump / $-18\text{ V}$ Reverse Battery / $-50\text{ V}$ Transient |
| **Dropout Voltage ($V_{DROP}$)** | $160\text{ mV}$ typ at $10\text{mA}$ / $600\text{ mV}$ max at $100\text{mA}$ |
| **Quiescent Ground Current ($I_Q$)** | $0.4\text{ mA}$ typical at $I_L = 10\text{mA}$ |
| **Operating Junction Temp** | $-40^\circ\text{C}$ to $+125^\circ\text{C}$ |

## Pinout (TO-92 Package)

Looking at the **flat front face** with leads pointing downwards:

```
        ┌─────────┐
        │  TO-92  │
        │ LM2931  │
        │ AZ-5.0  │
        └─┬───┬───┬─┘
          1   2   3
        VOUT GND VIN
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VOUT` | Power Output | Regulated $+5.0\text{ V}$ DC output (Requires minimum $100\ \mu\text{F}$ electrolytic or $22\ \mu\text{F}$ tantalum) |
| 2 | `GND` | Ground | Common system ground reference ($0\text{ V}$) |
| 3 | `VIN` | Power Input | Automotive DC input ($+6.0\text{ V}$ to $+26.0\text{ V}$, withstands $+60\text{V}$ load dump) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Output Voltage ($25^\circ\text{C}$) | $V_{OUT}$ | 4.90 | 5.00 | 5.10 | V | $I_L = 10\text{mA}$ (A-grade, $\pm 2\%$) |
| Output Voltage (Full Temp) | $V_{OUT}$ | 4.81 | 5.00 | 5.19 | V | $-40^\circ\text{C} \le T_J \le +125^\circ\text{C}$ |
| Operating Input Voltage | $V_{IN}$ | 6.0 | — | 26.0 | V | Normal operation |
| Max Input Transient Voltage | $V_{IN(trans)}$ | — | — | 60.0 | V | $t < 100\text{ ms}$ (Load dump) |
| Reverse Battery Voltage | $V_{IN(rev)}$ | — | — | -18.0 | V | Continuous DC reverse voltage |
| Dropout Voltage ($10\text{mA}$) | $V_{DROP}$ | — | 160 | 300 | mV | $I_L = 10\text{mA}$ |
| Dropout Voltage ($100\text{mA}$) | $V_{DROP}$ | — | 300 | 600 | mV | $I_L = 100\text{mA}$ |
| Quiescent Current | $I_Q$ | — | 0.4 | 1.0 | mA | $I_L = 10\text{mA}, V_{IN} = 14\text{V}$ |
| Peak Output Current | $I_{OUT(pk)}$ | 150 | 250 | — | mA | $V_{IN} = 14\text{V}$ |

## Typical Automotive Application Circuit

```
  Vehicle 12V Battery Rail (9V - 16V, transients to 60V)
           │
           ├───[ C_IN: 0.1µF Ceramic ]────────────┐
           │                                      │
       [Pin 3: VIN]                               │
      LM2931AZ-5.0                                │
       [Pin 2: GND] ──────────────────────────────┼─── Vehicle Chassis GND
       [Pin 1: VOUT]                              │
           │                                      │
           ├───[ C_OUT: 22µF Tantalum or 100µF ]──┘
           │
  Protected +5.0V DC Rail (Automotive MCU / CAN Bus / Sensors)
```

## Capacitor Selection & Stability

- **Input Capacitor:** A $0.1\ \mu\text{F}$ ceramic capacitor from `VIN` to `GND` is recommended if the regulator is located more than a few inches from the supply source.
- **Output Capacitor:** The LM2931 requires an output capacitor for stability. The minimum recommended value is **$22\ \mu\text{F}$ (tantalum)** or **$100\ \mu\text{F}$ (aluminum electrolytic)** with an ESR of **$0.1\ \Omega \dots 1.0\ \Omega$**.

## Common mistakes

- **Using insufficient output capacitance:** Unlike modern CMOS LDOs, the LM2931 requires substantial output capacitance ($\ge 22\ \mu\text{F}$) to prevent internal control loop oscillation.
- **Confusing with standard 78L05:** Standard 78L05 regulators will blow instantly if exposed to a $40\text{V}\dots 60\text{V}$ automotive alternator load dump spike or reverse battery connection. Always use the **LM2931** in vehicle-connected projects (CAN bus dongles, OBD-II gauges, motorcycle telemetry).

## Notes

- **Pin-Compatible Drop-In Alternatives:** LM2931Z-5.0 (standard grade), LP2950ACZ-5.0.
