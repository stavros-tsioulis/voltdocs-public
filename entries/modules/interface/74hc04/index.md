## Overview

The **74HC04** (SN74HC04) is a hex inverter IC manufactured using high-speed silicon-gate CMOS technology. Containing six independent inverting gates (NOT gates) in a 14-pin DIP/SOIC package, it performs the Boolean function $Y = \overline{A}$ in positive logic.

Operating across a supply voltage range of **2.0V to 6.0V DC**, it combines low CMOS power consumption with high-speed switching speeds ($7\text{ ns}$ propagation delay). The 74HC04 is used everywhere in digital electronics for signal polarity inversion, square-wave clock generators, RC delay timing circuits, and crystal oscillators.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | 2.0 V to 6.0 V DC |
| **Logic Family** | High-Speed CMOS (74HC) / TTL Compatible (74HCT) / Unbuffered (74HCU) |
| **Independent Inverters** | 6 (Hex Inverter) |
| **Propagation Delay** | $7\text{ ns}$ typical at $VCC = 5.0\text{V}$ |
| **Output Drive Current** | $\pm 5.2\text{ mA}$ at $VCC = 4.5\text{V}$ |
| **Package** | 14-pin DIP / SOIC-14 / TSSOP-14 |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
          1A 1│ 1   14│ VCC
          1Y 2│       │13 6A
          2A 3│       │12 6Y
          2Y 4│ 74HC04│11 5A
          3A 5│       │10 5Y
          3Y 6│       │9  4A
         GND 7│       │8  4Y
             └───────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `1A` | Inverter 1 Input |
| 2 | `1Y` | Inverter 1 Output ($1Y = \overline{1A}$) |
| 3 | `2A` | Inverter 2 Input |
| 4 | `2Y` | Inverter 2 Output ($2Y = \overline{2A}$) |
| 5 | `3A` | Inverter 3 Input |
| 6 | `3Y` | Inverter 3 Output ($3Y = \overline{3A}$) |
| 7 | `GND` | Ground reference (0 V) |
| 8 | `4Y` | Inverter 4 Output ($4Y = \overline{4A}$) |
| 9 | `4A` | Inverter 4 Input |
| 10 | `5Y` | Inverter 5 Output ($5Y = \overline{5A}$) |
| 11 | `5A` | Inverter 5 Input |
| 12 | `6Y` | Inverter 6 Output ($6Y = \overline{6A}$) |
| 13 | `6A` | Inverter 6 Input |
| 14 | `VCC` | Power supply voltage (+2.0V to +6.0V DC) |

## Function & Truth Table (Per Gate)

| Input A | Output Y |
|---|---|
| Low ($L$) | High ($H$) |
| High ($H$) | Low ($L$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.0 | 5.0 | 6.0 | V | DC |
| High-Level Input Voltage | $V_{IH}$ | 3.15 | — | — | V | $V_{CC} = 4.5\text{V}$ |
| Low-Level Input Voltage | $V_{IL}$ | — | — | 1.35 | V | $V_{CC} = 4.5\text{V}$ |
| Propagation Delay ($A \rightarrow Y$) | $t_{PD}$ | — | 7 | 14 | ns | $V_{CC} = 4.5\text{V}, C_L = 50\text{pF}$ |
| Output Drive Current | $I_{OUT}$ | — | — | $\pm 5.2$ | mA | $V_{CC} = 4.5\text{V}$ |
| Quiescent Supply Current | $I_{CC}$ | — | — | 2.0 | µA | $V_{IN} = V_{CC}\text{ or GND}$ |

## Typical Applications

### Simple Ring Oscillator Clock Generator

Connecting an odd number of inverters (e.g. 3 inverters) in a feedback loop with a capacitor generates a continuous square-wave clock signal.

```
       ┌──────────────────[Feedback Capacitor C]─────────────────┐
       │                                                         │
  ───►[Pin 1: 1A] ──► [Pin 2: 1Y] ──► [Pin 3: 2A] ──► [Pin 4: 2Y] ──┴──► Clock Out
```

## Common mistakes

- **Leaving unused inverter inputs floating:** Floating inputs on pins 5, 9, 11, or 13 will drift into intermediate voltage levels, causing the CMOS output stage to enter a linear region where both internal PMOS and NMOS transistors conduct, causing high power consumption and noise. Connect unused input pins to **$V_{CC}$ or GND**.
- **Using standard 74HC04 instead of 74HCU04 for analog/crystal oscillators:** Standard 74HC04 inverters are buffered (high gain triple-stage). For crystal oscillators or analog linear amplifiers, unbuffered **74HCU04** inverters are required to prevent high-frequency self-oscillation.
- **Using 74HC04 as a Schmitt trigger debouncer:** Standard 74HC04 inputs lack hysteresis. Slow-changing input signals (such as charging RC circuits or noisy switches) will cause output chattering. Use **74HC14** (Schmitt-Trigger Hex Inverter) for noisy or slow signals.

## Notes

- **74HC04 vs 74HC14 vs 74HCU04:** 74HC04 is a standard buffered hex inverter; 74HC14 is a Schmitt-trigger hex inverter (with hysteresis); 74HCU04 is an unbuffered single-stage hex inverter.
