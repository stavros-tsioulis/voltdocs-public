## Overview

The **74HC688** (commonly **SN74HC688N** in a 20-pin DIP package) is a high-speed CMOS 8-bit magnitude identity comparator IC. It compares two 8-bit binary words ($P_0 \dots P_7$ and $Q_0 \dots Q_7$) and asserts an active-LOW output ($\overline{P=Q}$) when all corresponding bit pairs are identical ($P = Q$).

Featuring an active-LOW enable input ($\overline{G}$), the 74HC688 is widely used in microcomputer memory address decoding, bus matching, dip-switch address verification, and digital hardware pattern matching.

## Quick reference

| | |
|---|---|
| **Logic Family** | High-Speed CMOS (HC) |
| **Package** | 20-Pin DIP (Through-Hole) / SOIC-20 / TSSOP-20 |
| **Supply Voltage Range ($V_{CC}$)** | $2.0\text{ V}$ to $6.0\text{ V}$ DC |
| **Word Width** | 8 Bits ($P_0 \dots P_7$ compared to $Q_0 \dots Q_7$) |
| **Propagation Delay ($t_{pd}$)** | $17\text{ ns}$ typical at $V_{CC} = 4.5\text{V}$ |
| **Enable Control** | Active-LOW Enable ($\overline{G}$) |
| **Output State** | Active-LOW Equality Output ($\overline{P=Q}$) |

## Pinout (20-Pin DIP Package)

```
        ┌──────────────┐
     ~G~ ─│ 1         20 │─ VCC
      P0 ─│ 2         19 │─ ~P=Q~
      Q0 ─│ 3         18 │─ Q7
      P1 ─│ 4         17 │─ P7
      Q1 ─│ 5         16 │─ Q6
      P2 ─│ 6         15 │─ P6
      Q2 ─│ 7         14 │─ Q5
      P3 ─│ 8         13 │─ P5
      Q3 ─│ 9         12 │─ Q4
     GND ─│ 10        11 │─ P4
        └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `~G~` | Active-LOW Enable input (LOW = Enable comparison, HIGH = Force output HIGH) |
| 2, 4, 6, 8, 11, 13, 15, 17 | `P0`–`P7` | Word P 8-bit input pins |
| 3, 5, 7, 9, 12, 14, 16, 18 | `Q0`–`Q7` | Word Q 8-bit input pins |
| 10 | `GND` | Ground reference (0 V) |
| 19 | `~P=Q~` | Active-LOW equality output pin (LOW when $P = Q$ and $\overline{G} = 0$) |
| 20 | `VCC` | Power supply input (+2.0V to +6.0V DC) |

## Function Table

| Inputs ($P_n, Q_n$) | Enable Input ($\overline{G}$) | Equality Output ($\overline{P=Q}$) |
|---|---|---|
| $P = Q$ | Low (`0`) | Low (`0`) |
| $P \neq Q$ | Low (`0`) | High (`1`) |
| X (Don't care) | High (`1`) | High (`1`) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage Range | $V_{CC}$ | 2.0 | 5.0 | 6.0 | V | Operational range |
| High-Level Input Voltage | $V_{IH}$ | 3.15 | — | — | V | $V_{CC} = 4.5\text{V}$ |
| Low-Level Input Voltage | $V_{IL}$ | — | — | 1.35 | V | $V_{CC} = 4.5\text{V}$ |
| High-Level Output Volts | $V_{OH}$ | 4.4 | 4.5 | — | V | $V_{CC} = 4.5\text{V}, I_{OH} = -20\mu\text{A}$ |
| Low-Level Output Volts | $V_{OL}$ | — | 0.1 | 0.4 | V | $V_{CC} = 4.5\text{V}, I_{OL} = 4\text{mA}$ |
| Propagation Delay ($P_n \to \overline{P=Q}$)| $t_{pd}$ | — | 17 | 30 | ns | $V_{CC} = 4.5\text{V}, C_L = 50\text{pF}$ |

## Common mistakes

- **Floating unused bit inputs:** Unused bit pairs (e.g. if comparing only 4 bits) must NOT be left floating. Tie matching unused $P_n$ and $Q_n$ input pairs to GND or $V_{CC}$ so they evaluate as equal ($P_n = Q_n$).
- **Expecting active-HIGH output:** The equality output pin is active-LOW ($\overline{P=Q}$). It pulls LOW when words match. Add an inverter if an active-HIGH match signal is needed.

## Notes

- **Address Decoding:** Easily cascades by tying the $\overline{P=Q}$ output of one chip into the $\overline{G}$ enable input of another to compare 16-bit or 32-bit bus addresses.
