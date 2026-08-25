## Overview

The **74HC86** (SN74HC86) is a high-speed silicon-gate CMOS integrated circuit containing four independent 2-input **Exclusive-OR (XOR)** logic gates. Each gate performs the Boolean function:

$$Y = A \oplus B = A\overline{B} + \overline{A}B$$

The output of an XOR gate is HIGH if and only if exactly one input is HIGH and the other is LOW. When both inputs are at the same logic level (both LOW or both HIGH), the output is LOW. This unique logic property makes the 74HC86 indispensable for **parity generation and checking, binary half-adders/full-adders, digital magnitude comparators, controlled inverters, and digital phase detectors** in PLL circuits.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | 2.0 V to 6.0 V DC (5.0 V nominal) |
| **Logic Family** | High-Speed CMOS (74HC) / TTL-Compatible (74HCT) |
| **Gate Count** | 4 Independent 2-Input XOR Gates |
| **Logic Function** | $Y = A \oplus B$ |
| **Propagation Delay ($t_{pd}$)** | $11\text{ ns}$ typ ($23\text{ ns}$ max) at $V_{CC} = 4.5\text{V}$ |
| **Output Drive Current** | $\pm 5.2\text{ mA}$ at $V_{CC} = 4.5\text{V}$ |
| **Package Options** | 14-pin DIP / SOIC-14 / TSSOP-14 |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
          1A 1│ 1   14│ VCC
          1B 2│       │13 4B
          1Y 3│       │12 4A
          2A 4│ 74HC86│11 4Y
          2B 5│       │10 3B
          2Y 6│       │9  3A
         GND 7│       │8  3Y
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1, 2 | `1A`, `1B` | Digital Input | Gate 1 Data Inputs |
| 3 | `1Y` | Digital Output | Gate 1 XOR Output ($1Y = 1A \oplus 1B$) |
| 4, 5 | `2A`, `2B` | Digital Input | Gate 2 Data Inputs |
| 6 | `2Y` | Digital Output | Gate 2 XOR Output ($2Y = 2A \oplus 2B$) |
| 7 | `GND` | Power | Ground reference (0 V) |
| 8 | `3Y` | Digital Output | Gate 3 XOR Output ($3Y = 3A \oplus 3B$) |
| 9, 10 | `3A`, `3B` | Digital Input | Gate 3 Data Inputs |
| 11 | `4Y` | Digital Output | Gate 4 XOR Output ($4Y = 4A \oplus 4B$) |
| 12, 13 | `4A`, `4B` | Digital Input | Gate 4 Data Inputs |
| 14 | `VCC` | Power | Supply voltage (+2.0 V to +6.0 V DC) |

## Function Table

| Input A | Input B | Output Y ($A \oplus B$) |
|---|---|---|
| Low ($L$) | Low ($L$) | Low ($L$) |
| Low ($L$) | High ($H$) | High ($H$) |
| High ($H$) | Low ($L$) | High ($H$) |
| High ($H$) | High ($H$) | Low ($L$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.0 | 5.0 | 6.0 | V | Operating DC range |
| High-Level Input Voltage | $V_{IH}$ | 3.15 | — | — | V | $V_{CC} = 4.5\text{V}$ |
| Low-Level Input Voltage | $V_{IL}$ | — | — | 1.35 | V | $V_{CC} = 4.5\text{V}$ |
| High-Level Output Voltage | $V_{OH}$ | 4.4 | 4.5 | — | V | $V_{CC} = 4.5\text{V}, I_{OH} = -20\ \mu\text{A}$ |
| Low-Level Output Voltage | $V_{OL}$ | — | 0.0 | 0.1 | V | $V_{CC} = 4.5\text{V}, I_{OL} = 20\ \mu\text{A}$ |
| Propagation Delay | $t_{PLH}, t_{PHL}$ | — | 11 | 23 | ns | $V_{CC} = 4.5\text{V}, C_L = 50\text{ pF}$ |
| Quiescent Current | $I_{CC}$ | — | — | 2.0 | µA | $V_{IN} = V_{CC}\text{ or GND}$ |

## Typical Applications

### 1. Controlled Inverter (True / Invert Control)

Holding input B LOW passes signal A non-inverted ($Y = A$). Pulling input B HIGH inverts signal A ($Y = \overline{A}$):

```
 Signal In (A) ───► [Pin 1: 1A]
                           74HC86
                    [Pin 3: 1Y] ──► Output Y (A if Invert=0, ~A if Invert=1)
 Invert Control ──► [Pin 2: 1B]
```

### 2. Frequency Doubler (Pulse Edge Detector)

Passing a clock signal directly into one XOR input and through a small RC delay to the other generates a short pulse on every rising and falling clock edge, effectively doubling the clock frequency.

## Common mistakes

- **Leaving unused gate inputs floating:** As with all high-impedance CMOS gates, floating inputs oscillate rapidly and generate excess noise. Tie all unused input pins to `GND` or `VCC`.
- **Misinterpreting as an OR gate:** In an OR gate (74HC32), $1 + 1 = 1$. In an XOR gate (74HC86), $1 \oplus 1 = 0$.

## Notes

- **Pin-Compatible Drop-In Alternatives:** 74HCT86 (TTL compatible), 74LS86 (Bipolar TTL), SN74HC86N, CD74HC86.
