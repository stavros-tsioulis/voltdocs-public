## Overview

The **CD4050B** is a high-voltage CMOS hex non-inverting buffer IC containing six independent non-inverting driver circuits. It is specifically engineered with modified input protection circuitry that allows the input signal voltage ($V_{IN}$) to **safely exceed the supply voltage ($V_{DD}$)** up to $+18\text{V}$ without forward-biasing any internal diode clamps.

This unique property makes the CD4050B one of the most popular and simple unidirectional **logic-level down-converters** in electronics: powered from a $+3.3\text{V}$ rail, it directly translates $+5\text{V}$ (or $+12\text{V}$) microcontroller logic signals down to clean $+3.3\text{V}$ levels for sensitive SPI displays, SD card modules, and low-voltage sensors.

## Quick reference

| | |
|---|---|
| **Supply Voltage Range (`VDD`)** | 3.0 V to 18.0 V DC (20.0 V maximum rating) |
| **Input Voltage Range ($V_{IN}$)** | $-0.5\text{ V}$ to $+18.0\text{ V}$ (Can safely exceed $V_{DD}$) |
| **Logic Function** | 6 Independent Non-Inverting Buffers ($Y = A$) |
| **Drive Capability** | Direct drive for 2 standard DTL/TTL loads ($I_{OL} \ge 3.2\text{ mA}$ at $5\text{V}$) |
| **Propagation Delay ($t_{pd}$)** | $32\text{ ns}$ typ at $V_{DD} = 10\text{V}$ ($55\text{ ns}$ at $5\text{V}$) |
| **Package Options** | 16-pin DIP / SOIC-16 / TSSOP-16 |

## Pinout (DIP-16 Package)

```
             ┌───┴───┐
         VDD 1│ 1   16│ NC
          1Y 2│       │15 6Y
          1A 3│       │14 6A
          2Y 4│CD4050B│13 NC
          2A 5│       │12 5Y
          3Y 6│       │11 5A
          3A 7│       │10 4Y
         VSS 8│       │9  4A
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VDD` | Power | Positive Supply Voltage (+3.0 V to +18.0 V DC; set to 3.3V for 5V-to-3.3V translation) |
| 2 | `1Y` | Digital Output | Buffer 1 Output |
| 3 | `1A` | Digital Input | Buffer 1 Input (Accepts up to 18V regardless of $V_{DD}$) |
| 4 | `2Y` | Digital Output | Buffer 2 Output |
| 5 | `2A` | Digital Input | Buffer 2 Input |
| 6 | `3Y` | Digital Output | Buffer 3 Output |
| 7 | `3A` | Digital Input | Buffer 3 Input |
| 8 | `VSS` | Power | Ground reference (0 V) |
| 9 | `4A` | Digital Input | Buffer 4 Input |
| 10 | `4Y` | Digital Output | Buffer 4 Output |
| 11 | `5A` | Digital Input | Buffer 5 Input |
| 12 | `5Y` | Digital Output | Buffer 5 Output |
| 13 | `NC` | No Connect | No internal connection |
| 14 | `6A` | Digital Input | Buffer 6 Input |
| 15 | `6Y` | Digital Output | Buffer 6 Output |
| 16 | `NC` | No Connect | No internal connection |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 3.0 | — | 18.0 | V | Operating DC range |
| Input Voltage | $V_I$ | 0 | — | 18.0 | V | Allowed independent of $V_{DD}$ |
| High-Level Input Voltage | $V_{IH}$ | 2.5 | — | — | V | $V_{DD} = 3.3\text{V}, V_O = 3.0\text{V}$ |
| Low-Level Input Voltage | $V_{IL}$ | — | — | 0.8 | V | $V_{DD} = 3.3\text{V}, V_O = 0.3\text{V}$ |
| Output Sink Current | $I_{OL}$ | 3.2 | 8.0 | — | mA | $V_{DD} = 5\text{V}, V_{OUT} = 0.4\text{V}, V_I = 5\text{V}$ |
| Output Source Current | $I_{OH}$ | -1.5 | -3.0 | — | mA | $V_{DD} = 5\text{V}, V_{OUT} = 4.6\text{V}, V_I = 5\text{V}$ |
| Propagation Delay | $t_{PLH}, t_{PHL}$ | — | 55 | 110 | ns | $V_{DD} = 5\text{V}, V_I = 5\text{V}, C_L = 50\text{ pF}$ |
| Quiescent Current | $I_{DD}$ | — | 0.02 | 1.0 | µA | $V_{DD} = 5\text{V}, T_A = 25^\circ\text{C}$ |

## Typical Applications

### 5V Arduino to 3.3V SPI Bus Level Shifting

```
    5V Microcontroller (Arduino Uno)                     3.3V Target (SD Card / Display)
   ──────────────────────────────────                   ─────────────────────────────────
   5V MOSI (Pin 11) ──────────────► [Pin 3: 1A]   [Pin 2: 1Y] ──────────► 3.3V MOSI
   5V SCK  (Pin 13) ──────────────► [Pin 5: 2A]   [Pin 4: 2Y] ──────────► 3.3V SCK
   5V CS   (Pin 10) ──────────────► [Pin 7: 3A]   [Pin 6: 3Y] ──────────► 3.3V CS
                                        CD4050B
                                   [Pin 1: VDD] ◄─── +3.3V Power Rail
                                   [Pin 8: VSS] ◄─── GND
```

## Common mistakes

- **Attempting bidirectional or 3.3V-to-5V up-conversion:** The CD4050B is strictly a **unidirectional down-converter** ($V_{OUT}$ amplitude is limited by $V_{DD}$). If powered with $V_{DD} = 5\text{V}$, a $3.3\text{V}$ input may not reliably reach $V_{IH}$ minimum ($3.5\text{V}$ at $5\text{V} V_{DD}$). For bidirectional signals like I2C, use MOSFET level shifters (e.g. BSS138).
- **Confusing pinout with standard 14-pin ICs:** The CD4050B is housed in a **16-pin package** (with $V_{DD}$ on Pin 1 and $V_{SS}$ on Pin 8, and unused NC pins on 13 and 16). Forcing it into a 14-pin socket will connect power to wrong pins.
- **Leaving unused inputs open:** Floating CMOS inputs cause elevated supply current. Tie unused input pins (`4A`, `5A`, `6A`) to $V_{SS}$ or $V_{DD}$.

## Notes

- **CD4050B vs CD4049B:** The CD4050B is non-inverting ($Y = A$). The CD4049B is inverting ($Y = \overline{A}$) with identical high-to-low level-shifting capability.
