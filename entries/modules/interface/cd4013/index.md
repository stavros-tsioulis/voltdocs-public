## Overview

The **CD4013** (commonly **CD4013BE** in a 14-pin DIP package) is a classic high-voltage CMOS dual D-type flip-flop IC from the standard 4000B logic family. It contains **two independent, identical D-type flip-flops**, each equipped with Data ($D$), Clock ($CLK$), asynchronous Set ($SET$), asynchronous Reset ($RESET$), true output ($Q$), and complementary output ($\overline{Q}$).

Operating over a wide supply range from **$3.0\text{ V}$ to $18.0\text{ V}$**, the CD4013 is extremely popular in DIY electronics for toggle switches (push-button ON/OFF latches), frequency division by 2 (connecting $\overline{Q}$ back to $D$), and digital control logic.

## Quick reference

| | |
|---|---|
| **Logic Family** | High-Voltage CMOS (4000B Series) |
| **Package** | 14-Pin DIP (Through-Hole) / SOIC-14 / TSSOP-14 |
| **Supply Voltage Range ($V_{DD}$)** | $3.0\text{ V}$ to $18.0\text{ V}$ DC |
| **Flip-Flops** | 2 Independent D-Type Flip-Flops |
| **Max Clock Frequency** | $12\text{ MHz}$ at $V_{DD} = 10\text{V}$ |
| **Propagation Delay ($t_{pd}$)** | $65\text{ ns}$ typical at $V_{DD} = 10\text{V}$ |
| **Outputs** | Complementary True ($Q$) and Inverted ($\overline{Q}$) per stage |

## Pinout (14-Pin DIP Package)

```
        ┌──────────┐
     1Q ─│ 1     14 │─ VDD
    1~Q ─│ 2     13 │─ 2Q
   1CLK ─│ 3     12 │─ 2~Q
 1RESET ─│ 4     11 │─ 2CLK
     1D ─│ 5     10 │─ 2RESET
   1SET ─│ 6      9 │─ 2D
    VSS ─│ 7      8 │─ 2SET
        └──────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `1Q` | Flip-Flop 1 True output |
| 2 | `1~Q~` | Flip-Flop 1 Inverted output |
| 3 | `1CLK` | Flip-Flop 1 Clock input (Positive-edge triggered) |
| 4 | `1RESET` | Flip-Flop 1 Reset input (Asynchronous, active-HIGH) |
| 5 | `1D` | Flip-Flop 1 Data input |
| 6 | `1SET` | Flip-Flop 1 Set input (Asynchronous, active-HIGH) |
| 7 | `VSS` | Ground reference (0 V) |
| 8 | `2SET` | Flip-Flop 2 Set input (Asynchronous, active-HIGH) |
| 9 | `2D` | Flip-Flop 2 Data input |
| 10 | `2RESET` | Flip-Flop 2 Reset input (Asynchronous, active-HIGH) |
| 11 | `2CLK` | Flip-Flop 2 Clock input (Positive-edge triggered) |
| 12 | `2~Q~` | Flip-Flop 2 Inverted output |
| 13 | `2Q` | Flip-Flop 2 True output |
| 14 | `VDD` | Positive power supply (+3.0V to +18.0V DC) |

## Truth Table (Each Flip-Flop)

| Clock (`CLK`) | Data (`D`) | Reset (`RESET`) | Set (`SET`) | Output (`Q`) | Output ($\overline{Q}$) |
|---|---|---|---|---|---|
| Low-to-High ($\uparrow$) | Low (`0`) | Low (`0`) | Low (`0`) | Low (`0`) | High (`1`) |
| Low-to-High ($\uparrow$) | High (`1`) | Low (`0`) | Low (`0`) | High (`1`) | Low (`0`) |
| Low or High ($\downarrow$) | X | Low (`0`) | Low (`0`) | Unchanged | Unchanged |
| X | X | High (`1`) | Low (`0`) | Low (`0`) | High (`1`) |
| X | X | Low (`0`) | High (`1`) | High (`1`) | Low (`0`) |
| X | X | High (`1`) | High (`1`) | High (`1`) | High (`1`) |

## Toggle Switch / Divide-by-2 Circuit

Connecting the inverted output ($\overline{Q}$) back to the Data input ($D$) configures the flip-flop as a **Toggle Flip-Flop (Divide-by-2)**:

```
                  ┌──────────────┐
                  │    CD4013    │
       Pulse ───> │ 3: 1CLK   1Q │ ───> Output Frequency (f_CLK / 2)
                  │              │
       ┌───────── │ 2: 1~Q   1D  │ <───┐
       │          └──────────────┘     │
       └───────────────────────────────┘
```

## Common mistakes

- **Floating SET and RESET pins:** Unlike 74HC series where reset inputs are often active-LOW, CD4013 Set and Reset inputs are **active-HIGH**. Leaving them floating will cause the flip-flop to latch into a constant reset or set state. Tie unused `SET` and `RESET` pins to `VSS` (GND).
- **No button debouncing on Clock input:** Connecting a physical mechanical push-button directly to `CLK` will cause multiple clock edges due to contact bounce, making toggle switches skip states randomly. Add an RC filter or Schmitt trigger debouncer.

## Notes

- **4000B High Voltage Versatility:** Supports up to 18V supplies directly, making it popular for 12V automotive and relay control circuits without needing 5V LDO regulators.
