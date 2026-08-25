## Overview

The **CD4027** (CD4027B / CD4027BE) is a monolithic CMOS dual J-K master-slave flip-flop integrated circuit manufactured by Texas Instruments, ON Semiconductor, and Renesas. Operating across a wide supply voltage span of **$3.0\text{ V}$ to $18.0\text{ V}$**, each independent flip-flop contains individual `J`, `K`, `CLOCK`, asynchronous `SET`, and asynchronous `RESET` inputs, alongside complementary buffered outputs (`Q` and `~Q`).

The CD4027 triggers on the **positive-going (rising) edge of the clock signal**. It provides versatile sequential logic modes: when $J=1$ and $K=1$, the flip-flop toggles output on each rising clock pulse, acting as an ultra-reliable **divide-by-2 frequency divider** or toggle switch. It is heavily utilized in digital ripple counters, hardware debouncers, push-button power toggle circuits, shift registers, and state-machine sequencers.

## Quick reference

| | |
|---|---|
| **Logic Family** | High-Voltage CMOS (4000B Series) |
| **Package** | 16-pin PDIP (CD4027BE) / 16-pin SOIC (CD4027BM) |
| **Supply Voltage Range ($V_{DD}$)** | $3.0\text{ V}$ to $18.0\text{ V}$ DC |
| **Flip-Flops Per Package** | 2 independent J-K Flip-Flops |
| **Clock Triggering** | Positive (rising) edge-triggered |
| **Maximum Clock Frequency** | $4.0\text{ MHz}$ at $5\text{V}$ / $16.0\text{ MHz}$ at $15\text{V}$ |
| **Propagation Delay** | $65\text{ ns}$ typical at $15\text{V}$ ($150\text{ ns}$ at $5\text{V}$) |
| **Asynchronous Overrides** | Active-HIGH `SET` and `RESET` |
| **Quiescent Current** | $0.02\ \mu\text{A}$ typical at $5\text{V}$ (ultra-low power) |

## Pinout (DIP-16 / SOIC-16 Package)

```
             ┌──────────────┐
        Q2  ─│ 1         16 │─ VDD (+3V to +18V)
       ~Q2  ─│ 2         15 │─ Q1
    CLOCK2  ─│ 3   CD    14 │─ ~Q1
    RESET2  ─│ 4   4027  13 │─ CLOCK1
        K2  ─│ 5         12 │─ RESET1
        J2  ─│ 6         11 │─ K1
      SET2  ─│ 7         10 │─ J1
       VSS  ─│ 8          9 │─ SET1
     (GND)   └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `Q2` | Flip-Flop 2 True Output |
| 2 | `~Q2` | Flip-Flop 2 Inverted Output |
| 3 | `CLOCK2` | Flip-Flop 2 Positive-Edge Clock Input |
| 4 | `RESET2` | Flip-Flop 2 Asynchronous Reset Input (Active-HIGH) |
| 5 | `K2` | Flip-Flop 2 K Data Input |
| 6 | `J2` | Flip-Flop 2 J Data Input |
| 7 | `SET2` | Flip-Flop 2 Asynchronous Set Input (Active-HIGH) |
| 8 | `VSS` | Ground (0 V) reference |
| 9 | `SET1` | Flip-Flop 1 Asynchronous Set Input (Active-HIGH) |
| 10 | `J1` | Flip-Flop 1 J Data Input |
| 11 | `K1` | Flip-Flop 1 K Data Input |
| 12 | `RESET1` | Flip-Flop 1 Asynchronous Reset Input (Active-HIGH) |
| 13 | `CLOCK1` | Flip-Flop 1 Positive-Edge Clock Input |
| 14 | `~Q1` | Flip-Flop 1 Inverted Output |
| 15 | `Q1` | Flip-Flop 1 True Output |
| 16 | `VDD` | Positive Power Supply (+3.0V to +18.0V DC) |

## Truth Table (Each Flip-Flop)

### Synchronous Clocked Operation (`SET = 0`, `RESET = 0`)

| `CLOCK` Transition | `J` Input | `K` Input | $Q_{n+1}$ (Next Output) | $\overline{Q}_{n+1}$ (Inverted Output) | Operating Mode |
|---|---|---|---|---|---|
| Rising Edge ($\uparrow$) | Low (`0`) | Low (`0`) | $Q_n$ (No change) | $\overline{Q}_n$ (No change) | **Hold / Store** |
| Rising Edge ($\uparrow$) | High (`1`) | Low (`0`) | High (`1`) | Low (`0`) | **Set** |
| Rising Edge ($\uparrow$) | Low (`0`) | High (`1`) | Low (`0`) | High (`1`) | **Reset** |
| Rising Edge ($\uparrow$) | High (`1`) | High (`1`) | $\overline{Q}_n$ (Inverted) | $Q_n$ (Inverted) | **Toggle (Divide-by-2)** |
| Falling Edge ($\downarrow$) / Steady | X | X | $Q_n$ | $\overline{Q}_n$ | No state change |

### Asynchronous Override Inputs

| `SET` | `RESET` | `CLOCK` | `J` | `K` | `Q` Output | `~Q` Output | Action |
|---|---|---|---|---|---|---|---|
| High (`1`) | Low (`0`) | X | X | X | High (`1`) | Low (`0`) | **Asynchronous Force SET** |
| Low (`0`) | High (`1`) | X | X | X | Low (`0`) | High (`1`) | **Asynchronous Force RESET** |
| High (`1`) | High (`1`) | X | X | X | High (`1`) | High (`1`) | **Invalid / Undefined state** |

## Push-Button Toggle Switch Circuit (T-Flip-Flop)

```
        +VDD (+5V to +12V)
           │
           ├───────────────────┬───────────────────┐
           │                   │                   │
        [Pin 16: VDD]       [ 10k Pull-Up ]     [Pin 10: J1]
         CD4027                │                   │
        [Pin 13: CLOCK1] ──────┴─[ Push Button ]───┼───[Pin 11: K1]
           │                         │             │
        [Pin 9:  SET1]  ──── GND     GND          +VDD
        [Pin 12: RESET1] ─── GND
        [Pin 15: Q1] ───────────────────────────── Output Toggle Signal (High / Low)
```

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage Range | $V_{DD}$ | 3.0 | 5.0 / 12.0 | 18.0 | V | Operating range |
| Maximum Clock Frequency | $f_{CL}$ | 3.0 | 8.0 | — | MHz | $V_{DD} = 5\text{V}, T_A = 25^\circ\text{C}$ |
| Maximum Clock Frequency ($15\text{V}$)| $f_{CL}$ | 12.0 | 24.0 | — | MHz | $V_{DD} = 15\text{V}, T_A = 25^\circ\text{C}$ |
| Propagation Delay ($CLK \to Q$)| $t_{PHL}, t_{PLH}$| — | 150 | 300 | ns | $V_{DD} = 5\text{V}, C_L = 50\text{ pF}$ |
| Propagation Delay ($15\text{V}$)| $t_{PHL}, t_{PLH}$| — | 45 | 90 | ns | $V_{DD} = 15\text{V}, C_L = 50\text{ pF}$ |
| Clock Pulse Width Minimum | $t_W$ | — | 70 | 140 | ns | $V_{DD} = 5\text{V}$ |
| Quiescent Device Current | $I_{DD}$ | — | 0.02 | 1.0 | $\mu\text{A}$ | $V_{DD} = 5\text{V}$ |

## Common mistakes

- **Leaving unused inputs floating:** CMOS inputs have infinite input impedance ($10^{12}\ \Omega$). Leaving unused inputs (like `SET`, `RESET`, `J`, `K`, or the unused second flip-flop) floating will pick up electrostatic noise, causing massive power dissipation and erratic behavior. Tie unused logic inputs to `VSS` (GND) or `VDD`.
- **Active-HIGH Set and Reset confusion:** Unlike 74HC series flip-flops (which use active-LOW $\overline{SET}$ and $\overline{RESET}$), the CD4027 uses **active-HIGH** Set and Reset pins. For normal clocked operation, `SET` and `RESET` must both be tied to **Ground (`VSS`)**.
- **Contact bounce on clock input:** Connecting a mechanical switch directly to `CLOCK` causes multiple rapid clock edges per press. Always debounce mechanical switches with an RC filter and Schmitt trigger (like 74HC14 or CD40106) before the clock input.

## Notes

- **Comparison with CD4013:** The **CD4013** is a Dual D-type flip-flop (data follows D input), whereas the **CD4027** is a Dual J-K flip-flop, offering native hardware toggle capabilities without external feedback routing.
