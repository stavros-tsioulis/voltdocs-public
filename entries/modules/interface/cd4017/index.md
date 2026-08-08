## Overview

The **CD4017B** is a 5-stage Johnson decade counter with 10 decoded active-high outputs (`Q0`–`Q9`) manufactured by Texas Instruments, ON Semiconductor, and Renesas. Operating across a wide supply range of **3.0V to 18.0V DC**, it advances its active output sequentially on each **LOW-to-HIGH transition** of the clock input.

It includes a `RESET` pin to zero the counter, a `CLOCK INHIBIT` pin to freeze counting, and a `CARRY OUT` signal ($Q0\dots Q4$ high / $Q5\dots Q9$ low) for cascading multiple counters into 100-step or higher multi-stage sequencers. It is one of the most iconic ICs in hobby electronics, widely used in LED chaser lights, electronic dice, frequency dividers, and sequential timing controls.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VDD`)** | 3.0 V to 18.0 V DC |
| **Logic Family** | CMOS 4000 Series (CD4000) / High-Speed CMOS (74HC4017) |
| **Decoded Outputs** | 10 Active-High Outputs (`Q0` through `Q9`) |
| **Max Clock Frequency** | $2.5\text{ MHz}$ at $VDD = 5\text{V}$, $5.5\text{ MHz}$ at $VDD = 10\text{V}$ |
| **Cascade Output** | `CARRY OUT` (divides clock by 10) |
| **Package** | 16-pin DIP / SOIC-16 / TSSOP-16 |

## Pinout (DIP-16 Package)

```
             ┌───┴───┐
          Q5 1│ 1   16│ VDD
          Q1 2│       │15 RESET
          Q0 3│       │14 CLOCK
          Q2 4│ CD4017│13 CLOCK INHIBIT
          Q6 5│       │12 CARRY OUT
          Q7 6│       │11 Q9
          Q3 7│       │10 Q4
         VSS 8│       │9  Q8
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `Q5` | Output | Output state 5 (Active High) |
| 2 | `Q1` | Output | Output state 1 (Active High) |
| 3 | `Q0` | Output | Output state 0 (Active High, default at reset) |
| 4 | `Q2` | Output | Output state 2 (Active High) |
| 5 | `Q6` | Output | Output state 6 (Active High) |
| 6 | `Q7` | Output | Output state 7 (Active High) |
| 7 | `Q3` | Output | Output state 3 (Active High) |
| 8 | `VSS` | Power | Ground reference (0 V) |
| 9 | `Q8` | Output | Output state 8 (Active High) |
| 10 | `Q4` | Output | Output state 4 (Active High) |
| 11 | `Q9` | Output | Output state 9 (Active High) |
| 12 | `CARRY OUT` | Output | Carry out signal for cascading (High for Q0-Q4, Low for Q5-Q9) |
| 13 | `CLOCK INHIBIT`| Input | Active-High Clock Inhibit (Disable clock when High) |
| 14 | `CLOCK` | Input | Clock input pin (Advances counter on Low-to-High edge) |
| 15 | `RESET` | Input | Active-High Reset pin (Sets Q0 High, Q1-Q9 Low) |
| 16 | `VDD` | Power | Positive supply power pin (+3.0V to +18.0V DC) |

## Truth & Control Table

| RESET | CLOCK | CLOCK INHIBIT | Decoded Output High |
|---|---|---|---|
| High ($H$) | X | X | `Q0` |
| Low ($L$) | X | High ($H$) | No Change (Inhibited) |
| Low ($L$) | $\uparrow$ | Low ($L$) | Advances to next output ($Q_n \rightarrow Q_{n+1}$) |
| Low ($L$) | Low ($L$) | $\downarrow$ | Advances to next output ($Q_n \rightarrow Q_{n+1}$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 3.0 | 5.0 | 18.0 | V | DC |
| High-Level Output Current | $I_{OH}$ | $-0.5$ | $-1.6$ | — | mA | $V_{DD} = 5\text{V}, V_{OH} = 4.6\text{V}$ |
| Low-Level Output Current | $I_{OL}$ | 0.5 | 1.6 | — | mA | $V_{DD} = 5\text{V}, V_{OL} = 0.4\text{V}$ |
| Maximum Clock Frequency | $f_{CL}$ | 2.5 | 5.0 | — | MHz | $V_{DD} = 5\text{V}$ |
| Propagation Delay ($CLK \rightarrow Qn$) | $t_{PHL}, t_{PLH}$ | — | 200 | 400 | ns | $V_{DD} = 5\text{V}$ |
| Reset Pulse Width | $t_{W(R)}$ | 100 | 50 | — | ns | $V_{DD} = 5\text{V}$ |

## Typical Applications

### 1. Classic 10-LED Chaser Circuit (with NE555 Timer)

```
                       +9V
                        │
    NE555 Timer ────────┼─────────────────── [Pin 16: VDD]
   [Pin 3: OUT] ────► [Pin 14: CLOCK]
                        │   CD4017
                        ├───[Pin 13: CLK INH] ─── GND
                        └───[Pin 15: RESET]   ─── GND
                        │
                  Q0..Q9 ───► [ 10x LEDs with 470Ω Resistors ] ─── GND
```

### 2. N-Step Sequence Limiter (e.g. 4-Step Sequencer)

To limit the counter to $N$ steps (e.g., 4 steps: `Q0`, `Q1`, `Q2`, `Q3`), connect the $(N)$th output (`Q4`, Pin 10) directly to the **`RESET` pin (Pin 15)**. When the count reaches `Q4`, it immediately resets to `Q0`.

## Common mistakes

- **Leaving `RESET` or `CLOCK INHIBIT` pins floating:** Floating inputs will catch stray noise, causing the counter to lock up at `Q0` or freeze. Tie `RESET` and `CLOCK INHIBIT` to **GND** if not used.
- **Switch bounce when triggering from mechanical buttons:** Connecting a push-button directly to the `CLOCK` pin causes multiple clock edges per press due to contact bounce, making the counter skip 2–5 steps per press. Use an RC debouncing circuit or 555 monostable.
- **Driving high-current LEDs directly without current-limiting resistors:** Standard CD4017B outputs can only supply $1\text{ mA} \dots 2\text{ mA}$ at 5V ($10\text{mA}$ at 15V). Overloading outputs drops output voltage significantly or overheats the IC.

## Notes

- **CD4017 vs CD4022:** CD4017 is a 10-output decade counter; CD4022 is an 8-output octal counter.
