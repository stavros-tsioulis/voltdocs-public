## Overview

The **LM13700** (commonly **LM13700N** in a 16-pin DIP package) is a dual Operational Transconductance Amplifier (OTA) manufactured by Texas Instruments (originally National Semiconductor). Unlike standard op-amps whose output voltage is proportional to input differential voltage, an OTA converts differential input voltage into an **output current** ($I_{OUT} = g_m \times V_{IN}$), where transconductance ($g_m$) is directly controlled by an external Amplifier Bias Current ($I_{ABC}$).

Integrated with **linearizing input diodes** (which extend linear signal dynamic range by $10\text{ dB}$) and independent **Darlington output buffers**, the LM13700 is the quintessential chip for DIY analog music synthesizers, powering Voltage-Controlled Amplifiers (VCAs), Voltage-Controlled Filters (VCFs), and Voltage-Controlled Oscillators (VCOs).

## Quick reference

| | |
|---|---|
| **Device Type** | Dual Operational Transconductance Amplifier (OTA) |
| **Package** | 16-Pin DIP (Through-Hole) / SOIC-16 |
| **Supply Voltage Range ($V_{CC}$)** | $\pm 4.75\text{ V}$ to $\pm 18.0\text{ V}$ ($9.5\text{ V}$ to $36.0\text{ V}$ single supply) |
| **Transconductance Range ($g_m$)** | $0$ to $10,000\ \mu\text{S}$ ($10\text{ mS}$) controlled by $I_{ABC}$ |
| **Max Bias Current ($I_{ABC}$)** | $2.0\text{ mA}$ maximum per channel |
| **Linearizing Diodes** | Reduces input distortion; allows larger signal levels ($\pm 50\text{mV}$) |
| **Integrated Buffers** | Independent Darlington voltage followers for low-impedance output driving |

## Pinout (16-Pin DIP Package)

```
        ┌──────────────┐
  1I_ABC ─│ 1         16 │─ 2I_ABC
  1 D_B ─│ 2         15 │─ 2 D_B
   1+IN ─│ 3         14 │─ 2+IN
   1-IN ─│ 4         15 │─ 2-IN
  1 OUT ─│ 5         12 │─ 2 OUT
     V- ─│ 6         11 │─ V+
 1BUF_I ─│ 7         10 │─ 2BUF_I
 1BUF_O ─│ 8          9 │─ 2BUF_O
        └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `1 I_ABC` | Amp 1 Amplifier Bias Current input ($I_{ABC1}$) |
| 2 | `1 Diode Bias`| Amp 1 Linearizing diode bias current input |
| 3 | `1 +IN` | Amp 1 Non-inverting input pin |
| 4 | `1 -IN` | Amp 1 Inverting input pin |
| 5 | `1 OUT` | Amp 1 High-impedance current output pin |
| 6 | `V-` | Negative power supply rail ($-15\text{V}$ for dual supply, $0\text{V}$ for single supply) |
| 7 | `1 Buffer IN` | Amp 1 Darlington buffer base input pin |
| 8 | `1 Buffer OUT`| Amp 1 Darlington buffer emitter output pin |
| 9 | `2 Buffer OUT`| Amp 2 Darlington buffer emitter output pin |
| 10 | `2 Buffer IN` | Amp 2 Darlington buffer base input pin |
| 11 | `V+` | Positive power supply rail ($+15\text{V}$ for dual supply) |
| 12 | `2 OUT` | Amp 2 High-impedance current output pin |
| 13 | `2 -IN` | Amp 2 Inverting input pin |
| 14 | `2 +IN` | Amp 2 Non-inverting input pin |
| 15 | `2 Diode Bias`| Amp 2 Linearizing diode bias current input |
| 16 | `2 I_ABC` | Amp 2 Amplifier Bias Current input ($I_{ABC2}$) |

## Transconductance Formula

The open-loop transconductance ($g_m$) of each OTA channel is directly proportional to its bias current ($I_{ABC}$):

$$ g_m \approx 19.2 \times I_{ABC} \quad (\text{at } T_A = 25^\circ\text{C}) $$

When linearizing diodes are biased, transconductance is calculated as:

$$ g_m \approx \frac{I_{ABC}}{2 V_T} $$

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Transconductance ($I_{ABC} = 500\mu\text{A}$)| $g_m$ | 6700 | 9600 | 13000 | $\mu\text{S}$ | $T_A = 25^\circ\text{C}$ |
| Transconductance Tracking | $\Delta g_m$ | — | 0.4 | 1.0 | dB | Channel-to-channel match |
| Input Offset Voltage | $V_{IO}$ | — | 0.4 | 4.0 | mV | $I_{ABC} = 500\mu\text{A}$ |
| Input Bias Current | $I_{IN}$ | — | 0.4 | 2.0 | $\mu\text{A}$ | $I_{ABC} = 500\mu\text{A}$ |
| Peak Output Current | $I_{OUT}$ | 350 | 500 | — | $\mu\text{A}$ | $I_{ABC} = 500\mu\text{A}$ |

## Common mistakes

- **Applying input signals larger than 20mV without linearizing diodes:** Unbiased OTA inputs overdrive easily. Input signals above $\approx 20\text{ mV}$ peak without diode bias produce heavy harmonic clipping. Attenuate input signals or bias Pin 2/15 (`Diode Bias`).
- **Connecting high capacitive loads directly to output pin (Pin 5/12):** The OTA output is a high-impedance current source. Connect Pin 5 to the internal Darlington buffer input (Pin 7) or an external op-amp current-to-voltage converter stage.

## Notes

- **Synthesizer VCA Core:** The LM13700 is the most popular OTA IC in DIY synth building (Erica Synths, MFOS, Doepfer modules), used in voltage-controlled gain cells, low-pass state-variable filters, and ring modulators.
