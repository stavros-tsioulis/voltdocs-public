## Overview

The **CD4049UB** is a high-voltage CMOS hex inverting buffer IC containing six independent inverting buffer circuits. Like its non-inverting companion, the CD4050B, the CD4049UB is designed with specialized input protection that allows the input signal voltage ($V_{IN}$) to **exceed the supply voltage ($V_{DD}$)** up to $+18\text{V}$ without forward-biasing internal diode clamps to $V_{DD}$.

The CD4049UB provides high current-sinking capability, capable of driving up to **two standard TTL/DTL loads** ($I_{OL} \ge 3.2\text{ mA}$ at $5\text{V}$). It is commonly employed for logic inversion, high-voltage to low-voltage **signal down-conversion** (e.g. 15V CMOS to 5V TTL or 5V to 3.3V), and direct driving of LEDs and low-power relays.

## Quick reference

| | |
|---|---|
| **Supply Voltage Range (`VDD`)** | 3.0 V to 18.0 V DC (20.0 V maximum rating) |
| **Input Voltage Range ($V_{IN}$)** | $-0.5\text{ V}$ to $+18.0\text{ V}$ (Can safely exceed $V_{DD}$) |
| **Logic Function** | 6 Independent Inverting Buffers ($Y = \overline{A}$) |
| **Drive Capability** | Direct drive for 2 standard TTL/DTL loads ($I_{OL} \ge 3.2\text{ mA}$ at $5\text{V}$) |
| **Propagation Delay ($t_{pd}$)** | $30\text{ ns}$ typ at $V_{DD} = 10\text{V}$ ($50\text{ ns}$ at $5\text{V}$) |
| **Package Options** | 16-pin DIP / SOIC-16 / TSSOP-16 |

## Pinout (DIP-16 Package)

```
             ┌───┴───┐
         VDD 1│ 1   16│ NC
          1Y 2│       │15 6Y
          1A 3│       │14 6A
          2Y 4│CD4049UB 13 NC
          2A 5│       │12 5Y
          3Y 6│       │11 5A
          3A 7│       │10 4Y
         VSS 8│       │9  4A
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VDD` | Power | Positive Supply Voltage (+3.0 V to +18.0 V DC) |
| 2 | `1Y` | Digital Output | Inverting Buffer 1 Output ($1Y = \overline{1A}$) |
| 3 | `1A` | Digital Input | Inverting Buffer 1 Input (Accepts up to 18V regardless of $V_{DD}$) |
| 4 | `2Y` | Digital Output | Inverting Buffer 2 Output ($2Y = \overline{2A}$) |
| 5 | `2A` | Digital Input | Inverting Buffer 2 Input |
| 6 | `3Y` | Digital Output | Inverting Buffer 3 Output ($3Y = \overline{3A}$) |
| 7 | `3A` | Digital Input | Inverting Buffer 3 Input |
| 8 | `VSS` | Power | Ground / Negative Supply reference (0 V) |
| 9 | `4A` | Digital Input | Inverting Buffer 4 Input |
| 10 | `4Y` | Digital Output | Inverting Buffer 4 Output ($4Y = \overline{4A}$) |
| 11 | `5A` | Digital Input | Inverting Buffer 5 Input |
| 12 | `5Y` | Digital Output | Inverting Buffer 5 Output ($5Y = \overline{5A}$) |
| 13 | `NC` | No Connect | No internal connection |
| 14 | `6A` | Digital Input | Inverting Buffer 6 Input |
| 15 | `6Y` | Digital Output | Inverting Buffer 6 Output ($6Y = \overline{6A}$) |
| 16 | `NC` | No Connect | No internal connection |

## Function Table

| Input A | Output Y ($\overline{A}$) |
|---|---|
| Low ($L$) | High ($H$) |
| High ($H$) | Low ($L$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 3.0 | — | 18.0 | V | Operating DC range |
| Input Voltage | $V_I$ | 0 | — | 18.0 | V | Safe without $V_{DD}$ clamp diode |
| High-Level Input Voltage | $V_{IH}$ | 2.5 | — | — | V | $V_{DD} = 3.3\text{V}, V_O = 0.5\text{V}$ |
| Low-Level Input Voltage | $V_{IL}$ | — | — | 0.8 | V | $V_{DD} = 3.3\text{V}, V_O = 2.8\text{V}$ |
| Output Sink Current | $I_{OL}$ | 3.2 | 8.0 | — | mA | $V_{DD} = 5\text{V}, V_{OUT} = 0.4\text{V}, V_I = 5\text{V}$ |
| Output Source Current | $I_{OH}$ | -1.0 | -2.5 | — | mA | $V_{DD} = 5\text{V}, V_{OUT} = 4.6\text{V}, V_I = 0\text{V}$ |
| Propagation Delay | $t_{PLH}, t_{PHL}$ | — | 50 | 90 | ns | $V_{DD} = 5\text{V}, V_I = 5\text{V}, C_L = 50\text{ pF}$ |
| Quiescent Current | $I_{DD}$ | — | 0.02 | 1.0 | µA | $V_{DD} = 5\text{V}, T_A = 25^\circ\text{C}$ |

## Typical Applications

### 12V Industrial Sensor to 5V TTL / MCU Inverted Interface

```
  +12V Industrial Signal
           │
           ▼
      [Pin 3: 1A]
        CD4049UB (VDD = 5V)
      [Pin 2: 1Y] ──► +5V Active-Low Logic Signal to MCU GPIO
```

## Common mistakes

- **Confusing 16-pin package with standard 14-pin inverters:** The CD4049UB is a **16-pin DIP/SOIC** package with power on Pin 1 ($V_{DD}$) and Pin 8 ($V_{SS}$). Plugging it into a standard 14-pin socket (like 74HC04 or CD4069UB) will cause incorrect power routing and chip malfunction.
- **Overlooking inverted output polarity:** Unlike the CD4050B which is non-inverting, the CD4049UB inverts the logic state ($Y = \overline{A}$). Ensure downstream software or hardware expects inverted logic levels.
- **Leaving unused inputs open:** CMOS inputs float to uncertain voltages if un-terminated. Connect all unused inputs (`4A`, `5A`, `6A`) to $V_{SS}$ or $V_{DD}$.

## Notes

- **CD4049UB vs CD4050B:** CD4049UB is inverting ($Y = \overline{A}$); CD4050B is non-inverting ($Y = A$). Both share identical 16-pin footprint and high-to-low level conversion capability.
