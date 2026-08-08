## Overview

The **74HC74** (SN74HC74) is a dual positive-edge-triggered D-type flip-flop IC manufactured using high-speed silicon-gate CMOS technology. Each of the two independent flip-flops contains individual Data ($D$), Clock ($CLK$), Active-Low Preset ($\overline{PRE}$), and Active-Low Clear ($\overline{CLR}$) inputs, along with complementary outputs ($Q$ and $\overline{Q}$).

Data on the $D$ input meeting setup time requirements is transferred to the $Q$ output on the **LOW-to-HIGH transition** of the clock pulse. Asynchronous $\overline{PRE}$ and $\overline{CLR}$ inputs override the clock and data inputs when driven LOW. It is a fundamental building block for digital logic latches, frequency dividers, pulse synchronizers, and state machines.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | 2.0 V to 6.0 V DC |
| **Logic Family** | High-Speed CMOS (74HC) / TTL Compatible (74HCT) |
| **Independent Flip-Flops** | 2 |
| **Max Clock Frequency** | $35\text{ MHz}$ at $VCC = 4.5\text{V}$ ($50\text{ MHz}$ typical) |
| **Propagation Delay** | $15\text{ ns}$ typical at $VCC = 4.5\text{V}$ |
| **Package** | 14-pin DIP / SOIC-14 / TSSOP-14 |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
      1/CLR 1│ 1   14│ VCC
         1D 2│       │13 2/CLR
       1CLK 3│       │12 2D
      1/PRE 4│ 74HC74│11 2CLK
         1Q 5│       │10 2/PRE
        1/Q 6│       │9  2Q
        GND 7│       │8  2/Q
             └───────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `1/CLR` | Flip-Flop 1 Active-Low Clear input (Async Reset) |
| 2 | `1D` | Flip-Flop 1 Data input |
| 3 | `1CLK` | Flip-Flop 1 Clock input (Triggered on Low-to-High edge) |
| 4 | `1/PRE` | Flip-Flop 1 Active-Low Preset input (Async Set) |
| 5 | `1Q` | Flip-Flop 1 True output |
| 6 | `1/Q` | Flip-Flop 1 Complementary output |
| 7 | `GND` | Ground reference (0 V) |
| 8 | `2/Q` | Flip-Flop 2 Complementary output |
| 9 | `2Q` | Flip-Flop 2 True output |
| 10 | `2/PRE` | Flip-Flop 2 Active-Low Preset input (Async Set) |
| 11 | `2CLK` | Flip-Flop 2 Clock input (Triggered on Low-to-High edge) |
| 12 | `2D` | Flip-Flop 2 Data input |
| 13 | `2/CLR` | Flip-Flop 2 Active-Low Clear input (Async Reset) |
| 14 | `VCC` | Power supply input (+2.0V to +6.0V DC) |

## Function Table

| Inputs | | | | Outputs | | Operating Mode |
|---|---|---|---|---|---|---|
| **/PRE** | **/CLR** | **CLK** | **D** | **Q** | **/Q** | |
| Low ($L$) | High ($H$) | X | X | High ($H$) | Low ($L$) | Asynchronous Set |
| High ($H$) | Low ($L$) | X | X | Low ($L$) | High ($H$) | Asynchronous Reset |
| Low ($L$) | Low ($L$) | X | X | High ($H$)* | High ($H$)* | Non-stable (Unstable) |
| High ($H$) | High ($H$) | $\uparrow$ | High ($H$) | High ($H$) | Low ($L$) | Clocked Load 1 |
| High ($H$) | High ($H$) | $\uparrow$ | Low ($L$) | Low ($L$) | High ($H$) | Clocked Load 0 |
| High ($H$) | High ($H$) | Low ($L$) | X | $Q_0$ | $\overline{Q}_0$ | Hold (No change) |

*\* Output condition is unstable; will not remain after /PRE and /CLR return High.*

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.0 | 5.0 | 6.0 | V | DC |
| Setup Time | $t_{su}$ | 20 | — | — | ns | $D$ to $CLK \uparrow, V_{CC} = 4.5\text{V}$ |
| Hold Time | $t_{h}$ | 0 | — | — | ns | $CLK \uparrow$ to $D, V_{CC} = 4.5\text{V}$ |
| Clock Frequency | $f_{MAX}$ | 30 | 50 | — | MHz | $V_{CC} = 4.5\text{V}$ |
| Output Drive Current | $I_{OUT}$ | — | — | $\pm 5.2$ | mA | $V_{CC} = 4.5\text{V}$ |
| Quiescent Current | $I_{CC}$ | — | — | 4.0 | µA | $V_{IN} = V_{CC}\text{ or GND}$ |

## Typical Applications

### Divide-by-2 Frequency Divider Circuit

Connecting the inverted output ($\overline{Q}$) directly back into the Data input ($D$) toggles the output state on every rising clock edge, halving the input clock frequency ($f_{OUT} = f_{IN} / 2$).

```
                      +5V
                       │
               [Pin 4: 1/PRE]
               [Pin 1: 1/CLR]
                       │
  Clock In ───► [Pin 3: 1CLK]   [Pin 5: 1Q] ───► F_OUT (F_IN / 2)
                       │           ▲
                74HC74 │           │
                       │           │
                [Pin 2: 1D] ◄──────┴─── [Pin 6: 1/Q]
```

## Common mistakes

- **Leaving $\overline{PRE}$ and $\overline{CLR}$ pins floating:** In CMOS ICs, un-terminated input pins float between voltage levels, triggering erratic resets or excessive power dissipation. Unused $\overline{PRE}$ and $\overline{CLR}$ pins must be tied directly to **$V_{CC}$** (High).
- **Ignoring Setup ($t_{su}$) and Hold ($t_h$) times:** Changing the $D$ input within $20\text{ ns}$ of the rising $CLK$ edge can cause **metastability**, where the output oscillation lingers between high and low logic states before settling.
- **Missing decoupling capacitor:** High-speed CMOS switching currents can corrupt state storage. Place a $100\text{ nF}$ ceramic capacitor directly across Pin 14 ($VCC$) and Pin 7 ($GND$).

## Notes

- **74HC74 vs 74HC73 / 74HC112:** 74HC74 features D-type flip-flops (data latching); 74HC73 and 74HC112 feature JK-type flip-flops (toggle / set / reset).
