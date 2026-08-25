## Overview

The **CD40106B** (CD40106) is a monolithic CMOS integrated circuit containing six independent inverting buffer gates with **Schmitt-trigger inputs**. Each gate functions as an inverter with built-in input hysteresis that discriminates between positive-going ($V_T+$) and negative-going ($V_T-$) threshold voltages.

With a wide operating supply voltage range from **$3.0\text{V}$ to $18.0\text{V}$ DC** and typical input hysteresis of **$0.9\text{V}$ at $5\text{V}$** ($2.3\text{V}$ at $10\text{V}$, $3.5\text{V}$ at $15\text{V}$), the CD40106B converts slowly changing, noisy, or corrupted analog signals into sharp, jitter-free square digital waveforms. It is a cornerstone component for 12V automotive sensors, switch debouncing, and low-frequency multi-channel RC oscillators in modular synthesizers.

## Quick reference

| | |
|---|---|
| **Supply Voltage Range (`VDD`)** | 3.0 V to 18.0 V DC (20.0 V maximum rating) |
| **Logic Family** | Standard CMOS 4000B Series |
| **Inverters Count** | 6 Independent Schmitt-Trigger Inverters ($Y = \overline{A}$) |
| **Hysteresis Voltage ($V_H$)** | $0.9\text{ V}$ typ at $5\text{V}$, $2.3\text{ V}$ typ at $10\text{V}$, $3.5\text{ V}$ typ at $15\text{V}$ |
| **Positive Threshold ($V_T+$)** | $2.9\text{ V}$ typ at $5\text{V}$ ($5.8\text{ V}$ typ at $10\text{V}$) |
| **Negative Threshold ($V_T-$)** | $1.9\text{ V}$ typ at $5\text{V}$ ($3.9\text{ V}$ typ at $10\text{V}$) |
| **Propagation Delay ($t_{pd}$)** | $140\text{ ns}$ typ at $V_{DD} = 10\text{V}$ ($280\text{ ns}$ at $5\text{V}$) |
| **Package Options** | 14-pin DIP / SOIC-14 / TSSOP-14 |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
          1A 1│ 1   14│ VDD
          1Y 2│       │13 6A
          2A 3│       │12 6Y
          2Y 4│CD40106B 11 5A
          3A 5│       │10 5Y
          3Y 6│       │9  4A
         VSS 7│       │8  4Y
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `1A` | Schmitt Input | Inverter 1 Input |
| 2 | `1Y` | Digital Output | Inverter 1 Output ($1Y = \overline{1A}$) |
| 3 | `2A` | Schmitt Input | Inverter 2 Input |
| 4 | `2Y` | Digital Output | Inverter 2 Output |
| 5 | `3A` | Schmitt Input | Inverter 3 Input |
| 6 | `3Y` | Digital Output | Inverter 3 Output |
| 7 | `VSS` | Power | Ground / Negative Supply reference (0 V) |
| 8 | `4Y` | Digital Output | Inverter 4 Output |
| 9 | `4A` | Schmitt Input | Inverter 4 Input |
| 10 | `5Y` | Digital Output | Inverter 5 Output |
| 11 | `5A` | Schmitt Input | Inverter 5 Input |
| 12 | `6Y` | Digital Output | Inverter 6 Output |
| 13 | `6A` | Schmitt Input | Inverter 6 Input |
| 14 | `VDD` | Power | Positive Supply Voltage (+3.0 V to +18.0 V DC) |

## Function Table

| Input A | Output Y ($\overline{A}$) |
|---|---|
| Low ($L < V_T-$) | High ($H$) |
| High ($H > V_T+$) | Low ($L$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 3.0 | — | 18.0 | V | Operating DC range |
| Positive Threshold Voltage | $V_T+$ | 2.2 | 2.9 | 3.6 | V | $V_{DD} = 5\text{V}$ |
| Negative Threshold Voltage | $V_T-$ | 1.3 | 1.9 | 2.4 | V | $V_{DD} = 5\text{V}$ |
| Hysteresis Voltage | $V_H$ | 0.3 | 0.9 | 1.6 | V | $V_T+ - V_T-, V_{DD} = 5\text{V}$ |
| Output Sink Current | $I_{OL}$ | 0.51 | 1.0 | — | mA | $V_{DD} = 5\text{V}, V_{OUT} = 0.4\text{V}$ |
| Output Source Current | $I_{OH}$ | -0.51 | -1.0 | — | mA | $V_{DD} = 5\text{V}, V_{OUT} = 4.6\text{V}$ |
| Propagation Delay | $t_{PLH}, t_{PHL}$ | — | 140 | 280 | ns | $V_{DD} = 10\text{V}, C_L = 50\text{ pF}$ |
| Quiescent Device Current | $I_{DD}$ | — | 0.02 | 1.0 | µA | $V_{DD} = 5\text{V}, 25^\circ\text{C}$ |

## Typical Applications

### 1. Simple Single-Gate RC Square Wave Oscillator

Because CMOS inputs have virtually infinite input impedance, an RC oscillator can be built using a single resistor and capacitor without loading effects:

```
            ┌─────[ R = 100kΩ ]─────┐
            │                       │
            ├───► [Pin 1: 1A]       │
            │       CD40106B        ├────► Square Wave Clock Output
            │     [Pin 2: 1Y] ──────┘
        [ C = 100nF ]
            │
           GND
```

*Frequency is approximately $f \approx \frac{1}{0.8 \times R \times C}$.*

## Common mistakes

- **Leaving unused inverter inputs floating:** Even with Schmitt triggers, floating CMOS inputs float near intermediate voltages and trigger internal switching noise and excess power draw. Connect all unused inputs to `VSS` (GND) or `VDD`.
- **Assuming 74HC speed:** The CD40106B has a propagation delay of $\sim 140\text{ ns}$ at $10\text{V}$ ($280\text{ ns}$ at $5\text{V}$), compared to $15\text{ ns}$ for the 74HC14. Use the 74HC14 for high-frequency applications ($> 5\text{ MHz}$).

## Notes

- **Pin-Compatible Equivalents:** 74HC14 (CMOS 2-6V high speed), 74HCT14 (TTL-compatible), 74LS14 (Bipolar TTL), HEF40106B.
