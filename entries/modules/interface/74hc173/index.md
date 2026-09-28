## Overview

The **74HC173** (also designated CD74HC173 / SN74HC173) is a high-speed CMOS 4-bit D-type register integrated circuit manufactured by Texas Instruments and Nexperia. It consists of four positive-edge-triggered D-type flip-flops equipped with gated data enables, an asynchronous master reset, and 3-state output buffers.

Designed specifically for bus-organized digital systems, the 74HC173 allows multiple registers to tie directly to a common shared microprocessor data bus. The dual active-low data enable inputs ($\overline{E}_1, \overline{E}_2$) permit selective data loading without gating the master system clock, while the dual active-low output enables ($M, N$) place outputs into a high-impedance ($Z$) state when the register is not driving the bus.

## Quick reference

| | |
|---|---|
| **Function** | 4-Bit D-Type Register with 3-State Outputs |
| **Logic Family** | High-Speed CMOS (74HC Series) |
| **Supply Voltage Range ($V_{CC}$)** | $2.0\text{ V}$ to $6.0\text{ V}$ DC ($4.5\text{V} \dots 5.5\text{V}$ nominal) |
| **Register Width** | 4 bits ($1D \dots 4D \rightarrow 1Q \dots 4Q$) |
| **Max Clock Frequency ($f_{MAX}$)** | $33\text{ MHz}$ typ at $4.5\text{V}$ ($60\text{ MHz}$ at $6.0\text{V}$) |
| **Propagation Delay ($t_{pd}$)** | $17\text{ ns}$ typ at $4.5\text{V}$ |
| **Output Drive Capability** | 3-State outputs drive up to 15 LSTTL loads ($\pm 6\text{ mA}$) |
| **Reset Mode** | Asynchronous Master Reset (`MR`, active-HIGH) |
| **Packages** | 16-pin PDIP (E), SOIC-16 (M), TSSOP-16 (PW) |

## Pin configuration

### 16-Pin DIP / SOIC Package

```
               ┌──────────┐
      ~OE1~ (M)─┤ 1     16 ├─ VCC (+2V to +6V)
      ~OE2~ (N)─┤ 2     15 ├─ MR (Master Reset)
            1Q ─┤ 3     14 ├─ 1D
            2Q ─┤ 4     13 ├─ 2D
            3Q ─┤ 5     12 ├─ 3D
            4Q ─┤ 6     11 ├─ 4D
           CLK ─┤ 7     10 ├─ ~E2~ (Data Enable 2)
           GND ─┤ 8      9 ├─ ~E1~ (Data Enable 1)
               └──────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `~OE1~` (`M`) | Digital Input | Output enable input 1 (Active-LOW; must be LOW with pin 2 to enable outputs) |
| 2 | `~OE2~` (`N`) | Digital Input | Output enable input 2 (Active-LOW; must be LOW with pin 1 to enable outputs) |
| 3 | `1Q` | 3-State Output | Register output bit 1 |
| 4 | `2Q` | 3-State Output | Register output bit 2 |
| 5 | `3Q` | 3-State Output | Register output bit 3 |
| 6 | `4Q` | 3-State Output | Register output bit 4 |
| 7 | `CLK` | Digital Input | Clock input (Data loaded on low-to-high positive edge $\uparrow$) |
| 8 | `GND` | Power Supply | System Ground ($0\text{ V}$) |
| 9 | `~E1~` | Digital Input | Data enable input 1 (Active-LOW; must be LOW with pin 10 to load data) |
| 10 | `~E2~` | Digital Input | Data enable input 2 (Active-LOW; must be LOW with pin 9 to load data) |
| 11 | `4D` | Digital Input | Data input bit 4 |
| 12 | `3D` | Digital Input | Data input bit 3 |
| 13 | `2D` | Digital Input | Data input bit 2 |
| 14 | `1D` | Digital Input | Data input bit 1 |
| 15 | `MR` | Digital Input | Master Reset (Asynchronous, Active-HIGH; forces all $Q$ bits to 0) |
| 16 | `VCC` | Power Supply | Positive DC supply voltage ($+2.0\text{V} \dots +6.0\text{V}$) |

## Functional description

### Function Truth Table

| Mode | `MR` | `CLK` | $\overline{E}_1$ | $\overline{E}_2$ | $D$ | $\overline{OE}_1$ ($M$) | $\overline{OE}_2$ ($N$) | Output $Q$ |
|---|---|---|---|---|---|---|---|---|
| **Reset** | **`HIGH`** | X | X | X | X | **`LOW`** | **`LOW`** | **`LOW`** (0) |
| **Reset (High-Z)** | **`HIGH`** | X | X | X | X | `HIGH` | X | **`Z`** |
| **Load Data** | `LOW` | $\uparrow$ | **`LOW`** | **`LOW`** | `HIGH` | **`LOW`** | **`LOW`** | **`HIGH`** (1) |
| **Load Data** | `LOW` | $\uparrow$ | **`LOW`** | **`LOW`** | `LOW` | **`LOW`** | **`LOW`** | **`LOW`** (0) |
| **Hold Data** | `LOW` | $\uparrow$ | `HIGH` | X | X | **`LOW`** | **`LOW`** | $Q_0$ (No change) |
| **Hold Data** | `LOW` | $\uparrow$ | X | `HIGH` | X | **`LOW`** | **`LOW`** | $Q_0$ (No change) |
| **Hold Data** | `LOW` | `LOW` | X | X | X | **`LOW`** | **`LOW`** | $Q_0$ (No change) |
| **Disable Bus** | X | X | X | X | X | `HIGH` | X | **`Z`** (High-impedance) |
| **Disable Bus** | X | X | X | X | X | X | `HIGH` | **`Z`** (High-impedance) |

- **Clock Gating via Data Enables:** When either $\overline{E}_1$ or $\overline{E}_2$ is HIGH, the clock is internally inhibited from clocking new data, maintaining the existing register contents across clock cycles.
- **Asynchronous Master Reset:** Asserting `MR` HIGH immediately clears all internal flip-flops to logic 0 without waiting for a clock edge.

## Absolute maximum ratings

> [!WARNING]
> Stresses beyond these ratings cause permanent damage. Functional operation at these limits is not guaranteed.

| Parameter | Rating | Unit |
|---|---|---|
| Supply Voltage ($V_{CC}$) | $-0.5$ to $+7.0$ | V |
| Input Clamp Current ($I_{IK}$, $V_I < 0$ or $V_I > V_{CC}$) | $\pm 20$ | mA |
| Output Clamp Current ($I_{OK}$, $V_O < 0$ or $V_O > V_{CC}$) | $\pm 20$ | mA |
| Continuous Output Drive Current ($I_O$) | $\pm 35$ | mA |
| Continuous Supply Current ($I_{CC}$ or $I_{GND}$) | $\pm 70$ | mA |
| Operating Ambient Temperature Range | -40 to 85 | °C |
| Storage Temperature Range | -65 to 150 | °C |

## Electrical characteristics

$T_A = 25^\circ\text{C}$, unless otherwise noted.

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| High-Level Input Voltage | $V_{IH}$ | 3.15 | — | — | V | $V_{CC} = 4.5\text{ V}$ |
| Low-Level Input Voltage | $V_{IL}$ | — | — | 1.35 | V | $V_{CC} = 4.5\text{ V}$ |
| High-Level Output Voltage | $V_{OH}$ | 4.4 | 4.49 | — | V | $V_{CC} = 4.5\text{ V}, I_O = -20\text{ }\mu\text{A}$ |
| High-Level Output Voltage | $V_{OH}$ | 3.98 | 4.3 | — | V | $V_{CC} = 4.5\text{ V}, I_O = -6.0\text{ mA}$ |
| Low-Level Output Voltage | $V_{OL}$ | — | 0.01 | 0.1 | V | $V_{CC} = 4.5\text{ V}, I_O = 20\text{ }\mu\text{A}$ |
| Low-Level Output Voltage | $V_{OL}$ | — | 0.17 | 0.26 | V | $V_{CC} = 4.5\text{ V}, I_O = 6.0\text{ mA}$ |
| High-Impedance Off-State Current | $I_{OZ}$ | — | — | $\pm 0.5$ | $\mu\text{A}$ | $V_O = V_{CC}$ or GND |
| Propagation Delay (CLK to Q) | $t_{pd}$ | — | 17 | 30 | ns | $V_{CC} = 4.5\text{ V}, C_L = 50\text{ pF}$ |
| Max Clock Frequency | $f_{MAX}$ | 30 | 45 | — | MHz | $V_{CC} = 4.5\text{ V}, C_L = 50\text{ pF}$ |
| Setup Time ($D$ to CLK) | $t_s$ | 15 | 8 | — | ns | $V_{CC} = 4.5\text{ V}$ |
| Hold Time ($D$ to CLK) | $t_h$ | 3 | 0 | — | ns | $V_{CC} = 4.5\text{ V}$ |

## Typical application

### 4-Bit Microprocessor Data Bus Register / Accumulator

In homebrew discrete 4-bit/8-bit CPU builds (e.g. SAP-1 or Ben Eater computer architectures), the 74HC173 is the classic component used for the A-Register, B-Register, and Output Register:

```
            4-Bit Shared CPU Data Bus (D0 - D3)
            ══════════════╦══════════════
                          ║
                  ┌───────┴───────┐
                  │ 1D 2D 3D 4D   │
                  │               │
  Load Signal ───►│ ~E1~, ~E2~    │
  System Clock ──►│ CLK   74HC173 │
  Clear Signal ──►│ MR            │
  Read Signal ───►│ ~OE1~, ~OE2~  │
                  │               │
                  │ 1Q 2Q 3Q 4Q   │
                  └───────┬───────┘
                          ║
            ══════════════╩══════════════
            Output to ALU / Display LEDs
```

## Common mistakes

- **Leaving Master Reset (`MR`) Floating:** The `MR` input is active-HIGH. If left floating, capacitive stray noise will pull it high, holding the register continuously in reset. If reset is not required, tie Pin 15 (`MR`) directly to `GND`.
- **Forgetting Dual Active-LOW Enables:** Both data enable pins ($\overline{E}_1$ and $\overline{E}_2$) must be tied LOW for the register to load data. Similarly, both output enable pins ($M$ and $N$) must be tied LOW for outputs to drive the bus.
- **Confusing with Level-Sensitive Latches:** The 74HC173 is an **edge-triggered flip-flop**, not a transparent latch. Data on inputs $1D-4D$ is sampled only on the rising clock edge ($\uparrow$), not continuously while the clock is high.

## Notes

- **74HCT173 Variant:** The 74HCT173 features TTL-compatible input logic levels ($V_{IH} \ge 2.0\text{V}$, $V_{IL} \le 0.8\text{V}$ at $4.5\text{V} \dots 5.5\text{V}$), allowing direct interfacing with classic TTL or 3.3V microcontrollers driving 5V logic.
- **Comparison with 74HC174:** The 74HC174 has 6 flip-flops in a 16-pin package, but lacks 3-state outputs and gated data enables.
