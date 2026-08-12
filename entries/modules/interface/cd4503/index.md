## Overview

The **CD4503** (commonly **CD4503BE** in a 16-pin DIP package) is a high-voltage CMOS hex non-inverting 3-state buffer IC belonging to the standard 4000B logic family. It contains **six independent buffer gates** designed to drive digital buses or high-capacitance loads.

The six buffers are divided into two groups: four buffers controlled by Disable Input A (`DIS A`), and two buffers controlled by Disable Input B (`DIS B`). Bringing a disable input HIGH forces its corresponding buffer outputs into a high-impedance (tri-state) OFF condition.

## Quick reference

| | |
|---|---|
| **Logic Family** | High-Voltage CMOS (4000B Series) |
| **Package** | 16-Pin DIP (Through-Hole) / SOIC-16 / TSSOP-16 |
| **Supply Voltage Range ($V_{DD}$)** | $3.0\text{ V}$ to $18.0\text{ V}$ DC |
| **Number of Channels** | 6 Non-Inverting 3-State Buffers (4-bit + 2-bit groups) |
| **Propagation Delay ($t_{pd}$)** | $75\text{ ns}$ typical at $V_{DD} = 10\text{V}$ |
| **Output Sink/Source Current** | Up to $10\text{ mA}$ at $V_{DD} = 15\text{V}$ |
| **Disable Controls** | `DIS A` (Controls Outputs 1–4), `DIS B` (Controls Outputs 5–6) |

## Pinout (16-Pin DIP Package)

```
        ┌──────────────┐
  DIS A ─│ 1         16 │─ VDD
     A1 ─│ 2         15 │─ DIS B
     Y1 ─│ 3         14 │─ Y6
     A2 ─│ 4         13 │─ A6
     Y2 ─│ 5         12 │─ Y5
     A3 ─│ 6         11 │─ A5
     Y3 ─│ 7         10 │─ Y4
    VSS ─│ 8          9 │─ A4
        └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `DIS A` | Disable input for Buffers 1–4 (High = High-Z Output, Low = Enabled) |
| 2, 4, 6, 9 | `A1`–`A4` | Data inputs for Buffers 1–4 |
| 3, 5, 7, 10 | `Y1`–`Y4` | 3-state data outputs for Buffers 1–4 |
| 8 | `VSS` | Ground reference (0 V) |
| 11, 13 | `A5`–`A6` | Data inputs for Buffers 5–6 |
| 12, 14 | `Y5`–`Y6` | 3-state data outputs for Buffers 5–6 |
| 15 | `DIS B` | Disable input for Buffers 5–6 (High = High-Z Output, Low = Enabled) |
| 16 | `VDD` | Positive power supply input (+3V to +18V DC) |

## Truth Table

| Data Input (`A_n`) | Disable Input (`DIS`) | Output (`Y_n`) |
|---|---|---|
| Low (`0`) | Low (`0`) | Low (`0`) |
| High (`1`) | Low (`0`) | High (`1`) |
| X (Don't care) | High (`1`) | High-Impedance (`Z`) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage Range | $V_{DD}$ | 3.0 | 5 / 12 | 18.0 | V | DC operating range |
| High-Level Output Volts | $V_{OH}$ | 4.95 | 5.0 | — | V | $V_{DD} = 5\text{V}, I_O = 0$ |
| Low-Level Output Volts | $V_{OL}$ | — | 0.0 | 0.05 | V | $V_{DD} = 5\text{V}, I_O = 0$ |
| Propagation Delay | $t_{PLH} / t_{PHL}$ | — | 75 | 150 | ns | $V_{DD} = 10\text{V}, C_L = 50\text{pF}$ |
| Output Enable/Disable Time| $t_{PZL} / t_{PLZ}$ | — | 60 | 120 | ns | $V_{DD} = 10\text{V}, C_L = 50\text{pF}$ |
| Quiescent Supply Current | $I_{DD}$ | — | 0.02 | 1.0 | $\mu\text{A}$ | $V_{DD} = 5\text{V}, V_{IN} = 0\text{V}$ or $V_{DD}$ |

## Common mistakes

- **Confusing active-HIGH disable with active-LOW enable:** The CD4503 uses **Disable** inputs (`DIS A`, `DIS B`). Drive `DIS` **LOW** to enable outputs; driving `DIS` HIGH disables the buffer.
- **Leaving unused inputs floating:** Like all CMOS ICs, unused data or disable inputs must be tied to $V_{DD}$ or $V_{SS}$ to prevent shoot-through current spikes and floating input oscillations.

## Notes

- **4000B High-Voltage Capability:** Unlike 74HC series buffers limited to 6V max, the CD4503 supports supply voltages up to 18V, making it ideal for 12V automotive and industrial logic.
