## Overview

The **74HCT245** (commonly **SN74HCT245N** in a 20-pin DIP package) is an 8-bit non-inverting bidirectional 3-state bus transceiver IC. As a member of the **HCT logic family**, it operates on a $5\text{ V}$ supply while accepting TTL-compatible input thresholds ($V_{IH} \ge 2.0\text{ V}$).

Because its high-level input voltage threshold ($V_{IH} = 2.0\text{ V}$) is fully compatible with $3.3\text{ V}$ CMOS signals, the 74HCT245 is widely used as a **3.3V-to-5V level shifter and bus buffer** between 3.3V microcontrollers (ESP32, STM32, Raspberry Pi) and 5V peripherals (WS2812B LEDs, 5V LCD displays, legacy buses).

## Quick reference

| | |
|---|---|
| **Logic Family** | High-Speed CMOS with TTL Inputs (HCT) |
| **Package** | 20-Pin DIP (Through-Hole) / SOIC-20 / TSSOP-20 |
| **Supply Voltage Range ($V_{CC}$)** | $4.5\text{ V}$ to $5.5\text{ V}$ DC ($5\text{ V}$ nominal) |
| **Bus Width** | 8 Bits (Bidirectional $A_1 \dots A_8 \leftrightarrow B_1 \dots B_8$) |
| **TTL Input Threshold ($V_{IH}$)** | $\ge 2.0\text{ V}$ (Compatible with 3.3V MCU outputs) |
| **Propagation Delay ($t_{pd}$)** | $15\text{ ns}$ typical at $V_{CC} = 5\text{V}$ |
| **Output Sink/Source Current** | Up to $35\text{ mA}$ high-drive 3-state output |

## Pinout (20-Pin DIP Package)

```
        ┌──────────────┐
    DIR ─│ 1         20 │─ VCC
     A1 ─│ 2         19 │─ OE
     A2 ─│ 3         18 │─ B1
     A3 ─│ 4         17 │─ B2
     A4 ─│ 5         16 │─ B3
     A5 ─│ 6         15 │─ B4
     A6 ─│ 7         14 │─ B5
     A7 ─│ 8         13 │─ B6
     A8 ─│ 9         12 │─ B7
    GND ─│ 10        11 │─ B8
        └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `DIR` | Direction control pin (High = A to B, Low = B to A) |
| 2–9 | `A1`–`A8` | Side A bidirectional bus pins |
| 10 | `GND` | Ground reference (0 V) |
| 11–18| `B8`–`B1` | Side B bidirectional bus pins |
| 19 | `~OE~` | Active-LOW Output Enable (Low = Enabled, High = High-Z disconnect) |
| 20 | `VCC` | Power supply input (+4.5V to +5.5V DC) |

## Function Table

| Output Enable (`~OE~`) | Direction (`DIR`) | Operation |
|---|---|---|
| Low (`0`) | High (`1`) | $A$ data to $B$ bus ($A \to B$) |
| Low (`0`) | Low (`0`) | $B$ data to $A$ bus ($B \to A$) |
| High (`1`) | X (Don't care) | Isolation / High-Impedance (`Z`) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 4.5 | 5.0 | 5.5 | V | DC operational range |
| High-Level Input Voltage | $V_{IH}$ | 2.0 | — | — | V | TTL compatible ($V_{CC} = 4.5\text{V} \dots 5.5\text{V}$) |
| Low-Level Input Voltage | $V_{IL}$ | — | — | 0.8 | V | TTL compatible |
| High-Level Output Volts | $V_{OH}$ | 3.84 | 4.4 | — | V | $V_{CC} = 4.5\text{V}, I_{OH} = -6\text{mA}$ |
| Propagation Delay | $t_{PLH} / t_{PHL}$ | — | 15 | 25 | ns | $V_{CC} = 4.5\text{V}, C_L = 50\text{pF}$ |
| Quiescent Supply Current | $I_{CC}$ | — | 8.0 | 80 | $\mu\text{A}$ | $V_{IN} = V_{CC}$ or $\text{GND}$ |

## Common mistakes

- **Using 74HC245 instead of 74HCT245 for 3.3V-to-5V translation:** Standard 74HC245 powered at 5V requires $V_{IH} \ge 3.15\text{ V}$, so 3.3V signals from ESP32/Pi pins are unreliable. 74HCT245 only requires $V_{IH} \ge 2.0\text{ V}$, making it the correct part for 3.3V to 5V conversion.
- **Floating ~OE~ or DIR pins:** Always pull `~OE~` to GND for continuous buffer operation or pull to $V_{CC}$ with a resistor if 3-state control is needed.

## Notes

- **74HC vs 74HCT:** "HCT" specifies TTL-level input thresholds at 5V supply, allowing direct control from 3.3V logic outputs without active boost circuits.
