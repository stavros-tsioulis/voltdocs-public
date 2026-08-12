## Overview

The **LM741** (µA741) is a historic single general-purpose operational amplifier IC originally designed by Fairchild Semiconductor and produced by Texas Instruments, STMicroelectronics, and ON Semiconductor. It is one of the most famous integrated circuits in electrical engineering history and a staple of university electronics labs.

Featuring internal frequency compensation, output short-circuit protection, and input offset voltage nulling pins, the LM741 operates over a wide split supply range of **$\pm 5\text{V}$ to $\pm 18\text{V}$** (or single supply up to $36\text{V}$). Although largely superseded by modern op-amps in commercial applications, it remains widely referenced in textbooks and introductory circuits.

## Quick reference

| | |
|---|---|
| **Channels** | 1 (Single Operational Amplifier) |
| **Supply Voltage (Split Rail)** | $\pm 5\text{ V}$ to $\pm 18\text{ V}$ DC |
| **Supply Voltage (Single Rail)** | $10\text{ V}$ to $36\text{ V}$ DC |
| **Gain Bandwidth Product** | $1.0\text{ MHz}$ |
| **Slew Rate** | $0.5\text{ V}/\mu\text{s}$ |
| **Input Offset Voltage** | $1.0\text{ mV}$ typical ($6.0\text{ mV}$ max, nullable via pins 1 & 5) |
| **Input Bias Current** | $80\text{ nA}$ typical ($500\text{ nA}$ max) |
| **Package** | 8-pin DIP / SOIC-8 |

## Pinout (DIP-8 Package)

```
             ┌───┴───┐
     OFFSET1 1│ 1   8 │ NC (No Connection)
      IN-    2│       │ 7 V+ (VCC)
      IN+    3│ LM741 │ 6 OUT
   V- (GND)  4│       │ 5 OFFSET2
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `OFFSET1` | Analog Input | Offset Null Pin 1 (Connect to $10\text{k}\Omega$ potentiometer wiper to $V-$) |
| 2 | `IN-` | Analog Input | Inverting Input |
| 3 | `IN+` | Analog Input | Non-Inverting Input |
| 4 | `V-` | Power | Negative Supply ($V-$ or GND) |
| 5 | `OFFSET2` | Analog Input | Offset Null Pin 2 |
| 6 | `OUT` | Analog Output | Op-Amp Output |
| 7 | `V+` | Power | Positive Supply ($V+$ or $V_{CC}$) |
| 8 | `NC` | Unused | No Internal Connection |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Split) | $V_{CC\pm}$ | $\pm 5$ | $\pm 15$ | $\pm 18$ | V | Dual power rails |
| Unity Gain Bandwidth | $GBW$ | 0.4 | 1.0 | — | MHz | $V_{CC} = \pm 15\text{V}$ |
| Slew Rate | $SR$ | 0.3 | 0.5 | — | V/µs | $V_{CC} = \pm 15\text{V}, R_L = 2\text{k}\Omega$ |
| Input Bias Current | $I_{IB}$ | — | 80 | 500 | nA | $T_A = 25^\circ\text{C}$ |
| Input Offset Voltage | $V_{IO}$ | — | 1.0 | 6.0 | mV | $T_A = 25^\circ\text{C}$ |
| Quiescent Supply Current | $I_{CC}$ | — | 1.7 | 2.8 | mA | $V_{CC} = \pm 15\text{V}$, no load |

## Typical Applications

### Inverting Amplifier (Gain = -10)

```
                       ┌─── R_feedback (100kΩ) ───┐
                       │                          │
  Audio Input ───[10k]─┴─── [Pin 2: IN-]          │
                                LM741 ────────────┼─── Output Voltage
  GND ───────────────────── [Pin 3: IN+]          │
```

## Common mistakes

- **Attempting single-supply operation near Ground ($0\text{V}$):** The LM741 does NOT have rail-to-rail inputs or outputs. Its common-mode input voltage range extends only to within $\sim 3\text{V}$ of the power rails. Input signals near $0\text{V}$ when powered from a single $0\text{V} \dots 12\text{V}$ supply will distort. Use an LM358 for single-supply low-voltage applications.
- **Assuming high slew rate for high-frequency AC signals:** With a slow $0.5\text{ V}/\mu\text{s}$ slew rate, full-power bandwidth is limited to $\sim 10\text{ kHz}$. Audio or high-frequency signals will suffer slew-induced distortion.

## Notes

- **LM741 vs LM358 vs TL071:** LM741 is a legacy single op-amp; LM358 is a dual op-amp capable of single-supply operation down to ground; TL071 is a low-noise JFET single op-amp with fast $13\text{ V}/\mu\text{s}$ slew rate.
