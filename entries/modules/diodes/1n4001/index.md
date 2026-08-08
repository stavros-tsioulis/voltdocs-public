## Overview

The **1N4001** is a standard 1.0 Amp general-purpose silicon rectifier diode IC manufactured by ON Semiconductor, Vishay, and Diodes Incorporated. Bundled in almost every electronic components starter kit, it is used for AC-to-DC mains rectification, reverse polarity input protection, and flyback diode protection across inductive relay and motor coils.

Housed in a black plastic **DO-41 axial package** with a silver cathode band marking, the 1N4001 is rated for a peak repetitive reverse voltage ($V_{RRM}$) of **$50\text{ Volts}$** and an average forward rectified current ($I_{F(AV)}$) of **$1.0\text{ Ampere}$**.

## Quick reference

| | |
|---|---|
| **Diode Type** | Silicon Junction Power Rectifier Diode |
| **Package** | DO-41 (DO-204AL) Axial Package |
| **Polarity Marking** | Silver / White Band = Cathode (`K`), Opposite Lead = Anode (`A`) |
| **Peak Repetitive Reverse Voltage ($V_{RRM}$)**| $50\text{ V}$ max |
| **Average Forward Rectified Current ($I_{F(AV)}$)**| $1.0\text{ A}$ continuous at $T_A = 75^\circ\text{C}$ |
| **Peak Forward Surge Current ($I_{FSM}$)** | $30\text{ A}$ (8.3ms half sine-wave surge) |
| **Forward Voltage Drop ($V_F$)** | $1.0\text{ V}$ max at $I_F = 1.0\text{A}$ ($0.7\text{V} \dots 0.8\text{V}$ typical) |
| **Reverse Leakage Current ($I_R$)** | $5.0\ \mu\text{A}$ max at $V_R = 50\text{V}$ |

## Pinout (Axial DO-41 Package)

```
        (Anode) ───[ BLACK CYLINDER ]═══(Cathode Silver Band)───
                      1N4001
```

| Lead | Name | Description |
|---|---|---|
| Anode (`A`) | Plain Lead | Positive current entry lead |
| Cathode (`K` / `C`)| **Silver Band Lead** | Negative current exit lead (marked by silver/white stripe) |

## 1N400x Diode Series Comparison Table

The 1N4001 is the $50\text{V}$ rated entry in the 1N400x family. All 1N400x diodes share the same 1.0A current rating:

| Part Number | Peak Repetitive Reverse Voltage ($V_{RRM}$) | RMS Voltage ($V_{RMS}$) |
|---|---|---|
| **1N4001** | **$50\text{ V}$** | **$35\text{ V}$** |
| 1N4002 | $100\text{ V}$ | $70\text{ V}$ |
| 1N4003 | $200\text{ V}$ | $140\text{ V}$ |
| 1N4004 | $400\text{ V}$ | $280\text{ V}$ |
| 1N4005 | $600\text{ V}$ | $420\text{ V}$ |
| 1N4006 | $800\text{ V}$ | $560\text{ V}$ |
| **1N4007** | **$1000\text{ V}$** | **$700\text{ V}$** |

## Common Applications

### Inductive Flyback Protection Diode

When driving a relay coil or solenoid with a transistor, place a 1N4001 diode **in parallel across the coil with Cathode connected to $+V_{CC}$** and Anode to the transistor Collector:

```
        +12V Supply Rail ──────┬───────────────────────────┐
                               │                           │
                   [ 12V Relay Coil ]            [ 1N4001 Cathode ] (Silver Band)
                               │                           │
                               ├───────────────────────────┘
                               │
                       [ 2N2222 Collector ]
```

### Reverse Polarity Power Protection

Place a 1N4001 in series with the $+V_{CC}$ power input lead (Anode to Power Input, Cathode to Circuit $V_{CC}$) to prevent reverse battery connection from damaging sensitive electronics.

## Common mistakes

- **Installing diode in reverse polarity:** Connecting Cathode to Anode blocks forward current completely. Always identify the silver band marking the Cathode.
- **Using 1N4001 in high-frequency SMPS (>10kHz):** 1N4001 is a slow standard recovery rectifier ($t_{rr} > 30\ \mu\text{s}$). In high-frequency switching power supplies (like 150kHz buck converters), slow recovery diodes overheat. Use a fast Schottky diode (e.g. 1N5819, SS14, or SS34).

## Notes

- **1N4001 vs 1N4007 vs 1N4148:** 1N4001 is a 50V 1A power rectifier; 1N4007 is a 1000V 1A power rectifier; 1N4148 is a 100V 300mA high-speed small-signal switching diode.
