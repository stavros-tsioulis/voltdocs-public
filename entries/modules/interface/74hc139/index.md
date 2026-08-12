## Overview

The **74HC139** (commonly **SN74HC139N** in a 16-pin DIP package) is a high-speed CMOS dual 2-to-4 line decoder / demultiplexer IC. It contains **two completely independent 2-to-4 decoders**, each featuring 2 address inputs ($A_0, A_1$), an active-LOW Enable input ($\overline{E}$ / $\overline{G}$), and 4 active-LOW outputs ($\overline{Y}_0, \overline{Y}_1, \overline{Y}_2, \overline{Y}_3$).

When enabled ($\overline{E} = 0$), the 2-bit binary address selects exactly one of the four outputs to pull LOW while keeping the remaining three outputs HIGH. The 74HC139 is widely used in microcontrollers, memory chip-select decoding, and signal demultiplexing.

## Quick reference

| | |
|---|---|
| **Logic Family** | High-Speed CMOS (HC) |
| **Package** | 16-Pin DIP (Through-Hole) / SOIC-16 / TSSOP-16 |
| **Supply Voltage Range ($V_{CC}$)** | $2.0\text{ V}$ to $6.0\text{ V}$ DC |
| **Decoders per IC** | 2 Independent 2-to-4 Line Decoders |
| **Propagation Delay ($t_{pd}$)** | $13\text{ ns}$ typical at $V_{CC} = 4.5\text{V}$ |
| **Enable Control** | Active-LOW Enable ($\overline{1E}$, $\overline{2E}$) |
| **Outputs** | Active-LOW Outputs ($\overline{1Y0} \dots \overline{1Y3}$, $\overline{2Y0} \dots \overline{2Y3}$) |

## Pinout (16-Pin DIP Package)

```
        ┌──────────────┐
    1~E~ ─│ 1         16 │─ VCC
    1A0 ─│ 2         15 │─ 2~E~
    1A1 ─│ 3         14 │─ 2A0
   1~Y0~ ─│ 4         13 │─ 2A1
   1~Y1~ ─│ 5         12 │─ 2~Y0~
   1~Y2~ ─│ 6         11 │─ 2~Y1~
   1~Y3~ ─│ 7         10 │─ 2~Y2~
    GND ─│ 8          9 │─ 2~Y3~
        └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `1~E~` / `1~G~` | Decoder 1 Enable input (Active-LOW: LOW = Enabled, HIGH = Disables outputs) |
| 2 | `1A0` | Decoder 1 Address bit 0 input |
| 3 | `1A1` | Decoder 1 Address bit 1 input |
| 4, 5, 6, 7 | `1~Y0~`–`1~Y3~` | Decoder 1 outputs (Active-LOW) |
| 8 | `GND` | Ground reference (0 V) |
| 9, 10, 11, 12 | `2~Y3~`–`2~Y0~` | Decoder 2 outputs (Active-LOW) |
| 13 | `2A1` | Decoder 2 Address bit 1 input |
| 14 | `2A0` | Decoder 2 Address bit 0 input |
| 15 | `2~E~` / `2~G~` | Decoder 2 Enable input (Active-LOW) |
| 16 | `VCC` | Power supply voltage input (+2.0V to +6.0V DC) |

## Function Table (Each Decoder)

| Enable ($\overline{E}$) | Address Bit 1 ($A_1$) | Address Bit 0 ($A_0$) | $\overline{Y}_0$ | $\overline{Y}_1$ | $\overline{Y}_2$ | $\overline{Y}_3$ |
|---|---|---|---|---|---|---|
| High (`1`) | X | X | High (`1`) | High (`1`) | High (`1`) | High (`1`) |
| Low (`0`) | Low (`0`) | Low (`0`) | **Low (`0`)** | High (`1`) | High (`1`) | High (`1`) |
| Low (`0`) | Low (`0`) | High (`1`) | High (`1`) | **Low (`0`)** | High (`1`) | High (`1`) |
| Low (`0`) | High (`1`) | Low (`0`) | High (`1`) | High (`1`) | **Low (`0`)** | High (`1`) |
| Low (`0`) | High (`1`) | High (`1`) | High (`1`) | High (`1`) | High (`1`) | **Low (`0`)** |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage Range | $V_{CC}$ | 2.0 | 5.0 | 6.0 | V | Operational range |
| Propagation Delay ($A \to Y$) | $t_{pd}$ | — | 13 | 25 | ns | $V_{CC} = 4.5\text{V}, C_L = 50\text{pF}$ |
| Enable Propagation ($E \to Y$) | $t_{en}$ | — | 11 | 23 | ns | $V_{CC} = 4.5\text{V}, C_L = 50\text{pF}$ |
| High-Level Output Volts | $V_{OH}$ | 4.4 | 4.5 | — | V | $V_{CC} = 4.5\text{V}, I_{OH} = -20\mu\text{A}$ |
| Low-Level Output Volts | $V_{OL}$ | — | 0.1 | 0.4 | V | $V_{CC} = 4.5\text{V}, I_{OL} = 4\text{mA}$ |

## Common mistakes

- **Expecting active-HIGH outputs:** Outputs ($\overline{Y}_0 \dots \overline{Y}_3$) are **active-LOW** (they transition to 0V when selected). This is ideal for active-LOW Chip Select ($\overline{CS}$) pins on SPI flash/RAM memories.
- **Floating enable pins:** Drive $\overline{E}$ LOW to enable decoding. Leaving $\overline{E}$ floating will cause inputs to be ignored and outputs to remain HIGH.

## Notes

- **Cascading for 3-to-8 Decoding:** Connecting the two halves of a 74HC139 together (using $A_2$ to invert enable inputs) creates a single 3-to-8 decoder, acting as a compact dual-package alternative to the 74HC138.
