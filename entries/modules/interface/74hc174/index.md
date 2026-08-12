## Overview

The **74HC174** (commonly **SN74HC174N** in a 16-pin DIP package) is a high-speed CMOS hex D-type flip-flop IC. It contains **six independent D-type flip-flops** sharing a common positive-edge-triggered Clock input (`CLK`) and a common active-LOW Master Reset input ($\overline{MR}$ / $\overline{CLR}$).

When `CLK` transitions from LOW to HIGH, information at the data inputs ($1D \dots 6D$) meeting setup and hold times is stored and transferred to the true outputs ($1Q \dots 6Q$). Driving $\overline{MR}$ LOW asynchronously clears all six outputs to LOW regardless of clock or data states.

## Quick reference

| | |
|---|---|
| **Logic Family** | High-Speed CMOS (HC) |
| **Package** | 16-Pin DIP (Through-Hole) / SOIC-16 / TSSOP-16 |
| **Supply Voltage Range ($V_{CC}$)** | $2.0\text{ V}$ to $6.0\text{ V}$ DC |
| **Number of Channels** | 6 Independent D-Type Flip-Flops |
| **Max Clock Frequency** | $35\text{ MHz}$ min ($50\text{ MHz}$ typ at $V_{CC} = 4.5\text{V}$) |
| **Propagation Delay ($t_{pd}$)** | $14\text{ ns}$ typical at $V_{CC} = 4.5\text{V}$ |
| **Control Inputs** | Common Clock (`CLK`), Master Reset ($\overline{MR}$) |

## Pinout (16-Pin DIP Package)

```
        ┌──────────────┐
   ~MR~ ─│ 1         16 │─ VCC
     1Q ─│ 2         15 │─ 6Q
     1D ─│ 3         14 │─ 6D
     2D ─│ 4         13 │─ 5D
     2Q ─│ 5         12 │─ 5Q
     3D ─│ 6         11 │─ 4D
     3Q ─│ 7         10 │─ 4Q
    GND ─│ 8          9 │─ CLK
        └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `~MR~` | Common Master Reset input (Asynchronous, active-LOW) |
| 2, 5, 7, 10, 12, 15 | `1Q`–`6Q` | Flip-Flop 1–6 true outputs |
| 3, 4, 6, 11, 13, 14 | `1D`–`6D` | Flip-Flop 1–6 data inputs |
| 8 | `GND` | Ground reference (0 V) |
| 9 | `CLK` | Common Clock input (Positive-edge triggered) |
| 16 | `VCC` | Power supply voltage input (+2.0V to +6.0V DC) |

## Function Table (Each Flip-Flop)

| Master Reset ($\overline{MR}$) | Clock (`CLK`) | Data Input (`D_n`) | Output (`Q_n`) |
|---|---|---|---|
| Low (`0`) | X (Don't care) | X (Don't care) | Low (`0`) |
| High (`1`) | Low-to-High ($\uparrow$) | High (`1`) | High (`1`) |
| High (`1`) | Low-to-High ($\uparrow$) | Low (`0`) | Low (`0`) |
| High (`1`) | Low or High ($\downarrow$) | X (Don't care) | $Q_0$ (Unchanged) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage Range | $V_{CC}$ | 2.0 | 5.0 | 6.0 | V | Operational range |
| Clock Frequency | $f_{CLK}$ | 0 | 50 | 35 | MHz | $V_{CC} = 4.5\text{V}$ |
| Propagation Delay ($CLK \to Q$)| $t_{pd}$ | — | 14 | 26 | ns | $V_{CC} = 4.5\text{V}, C_L = 50\text{pF}$ |
| Setup Time ($D \to CLK$) | $t_{su}$ | 12 | 5 | — | ns | $V_{CC} = 4.5\text{V}$ |
| Hold Time ($CLK \to D$) | $t_{h}$ | 0 | -3 | — | ns | $V_{CC} = 4.5\text{V}$ |
| Reset Pulse Width | $t_{w}$ | 12 | 5 | — | ns | $V_{CC} = 4.5\text{V}, \overline{MR}$ LOW |

## Common mistakes

- **Leaving unused D inputs floating:** Tie unused data inputs ($1D \dots 6D$) to $V_{CC}$ or GND to prevent internal CMOS gate oscillation and supply current spikes.
- **Floating Master Reset ($\overline{MR}$):** Leaving Pin 1 ($\overline{MR}$) unconnected can cause random resetting due to noise pickup. Pull $\overline{MR}$ to $V_{CC}$ for normal operation.

## Notes

- **74HC174 vs 74HC175:** The 74HC174 contains 6 flip-flops with only true outputs ($Q$), whereas the 74HC175 contains 4 flip-flops with both true ($Q$) and complementary ($\overline{Q}$) outputs.
