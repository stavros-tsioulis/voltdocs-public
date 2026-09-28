## Overview

The **74HC374** is a high-speed CMOS octal D-type edge-triggered flip-flop integrated circuit with 3-state outputs, manufactured by Texas Instruments, Nexperia, and ON Semiconductor. It features eight edge-triggered flip-flops controlled by a common clock (`CLK`) and an active-low output enable (`~OE~`).

The 74HC374 is engineered specifically for driving bus lines in high-performance microprocessor, memory, and data communication systems. Its high-current 3-state outputs can source and sink up to $\pm 7.8\text{ mA}$ at $4.5\text{V}$, driving up to 15 LSTTL loads or highly capacitive transmission lines without external buffer ICs.

## Quick reference

| | |
|---|---|
| **Function** | Octal D-Type Edge-Triggered Flip-Flop with 3-State Outputs |
| **Logic Family** | High-Speed CMOS (74HC Series) |
| **Supply Voltage Range ($V_{CC}$)** | $2.0\text{ V}$ to $6.0\text{ V}$ DC ($4.5\text{V} \dots 5.5\text{V}$ nominal) |
| **Register Width** | 8 bits ($1D \dots 8D \rightarrow 1Q \dots 8Q$) |
| **Max Clock Frequency ($f_{MAX}$)** | $50\text{ MHz}$ typ at $4.5\text{V}$ ($60\text{ MHz}$ at $6.0\text{V}$) |
| **Propagation Delay ($t_{pd}$)** | $15\text{ ns}$ typ at $4.5\text{V}$ ($C_L = 50\text{ pF}$) |
| **Output Drive Capability** | 3-State outputs drive up to 15 LSTTL loads ($\pm 7.8\text{ mA}$) |
| **Clock Triggering** | Positive-edge triggered ($\uparrow$) |
| **Packages** | 20-pin PDIP (N), SOIC-20 (DW), TSSOP-20 (PW) |

## Pin configuration

### 20-Pin DIP / SOIC Package

```
               ┌──────────┐
         ~OE~ ─┤ 1     20 ├─ VCC (+2V to +6V)
           1Q ─┤ 2     19 ├─ 8Q
           1D ─┤ 3     18 ├─ 8D
           2D ─┤ 4     17 ├─ 7D
           2Q ─┤ 5     16 ├─ 7Q
           3Q ─┤ 6     15 ├─ 6Q
           3D ─┤ 7     14 ├─ 6D
           4D ─┤ 8     13 ├─ 5D
           4Q ─┤ 9     12 ├─ 5Q
          GND ─┤ 10    11 ├─ CLK (Clock)
               └──────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `~OE~` | Digital Input | Output Enable (Active-LOW; `LOW` = drive bus, `HIGH` = high-Z) |
| 2 | `1Q` | 3-State Output | Register output bit 1 |
| 3 | `1D` | Digital Input | Data input bit 1 |
| 4 | `2D` | Digital Input | Data input bit 2 |
| 5 | `2Q` | 3-State Output | Register output bit 2 |
| 6 | `3Q` | 3-State Output | Register output bit 3 |
| 7 | `3D` | Digital Input | Data input bit 3 |
| 8 | `4D` | Digital Input | Data input bit 4 |
| 9 | `4Q` | 3-State Output | Register output bit 4 |
| 10 | `GND` | Power Supply | System Ground ($0\text{ V}$) |
| 11 | `CLK` | Digital Input | Clock input (Data loaded on low-to-high transition $\uparrow$) |
| 12 | `5Q` | 3-State Output | Register output bit 5 |
| 13 | `5D` | Digital Input | Data input bit 5 |
| 14 | `6D` | Digital Input | Data input bit 6 |
| 15 | `6Q` | 3-State Output | Register output bit 6 |
| 16 | `7Q` | 3-State Output | Register output bit 7 |
| 17 | `7D` | Digital Input | Data input bit 7 |
| 18 | `8D` | Digital Input | Data input bit 8 |
| 19 | `8Q` | 3-State Output | Register output bit 8 |
| 20 | `VCC` | Power Supply | Positive DC supply voltage ($+2.0\text{V} \dots +6.0\text{V}$) |

## Functional description

### Function Truth Table

| Mode | `~OE~` | `CLK` | $D_n$ | $Q_n$ Output | Description |
|---|---|---|---|---|---|
| **Load 1** | **`LOW`** | $\uparrow$ | **`HIGH`** | **`HIGH`** (1) | Data bit loaded on rising clock edge |
| **Load 0** | **`LOW`** | $\uparrow$ | **`LOW`** | **`LOW`** (0) | Data bit loaded on rising clock edge |
| **Hold** | **`LOW`** | `LOW` / `HIGH` | X | $Q_0$ | No change while clock is steady |
| **Bus High-Z** | **`HIGH`** | $\uparrow$ | $D_n$ | **`Z`** | Data stored internally, outputs in high-impedance |
| **Bus High-Z** | **`HIGH`** | `LOW` / `HIGH` | X | **`Z`** | Outputs high-impedance, previous data held |

- **True Edge Triggering:** Unlike transparent latches which pass data continuously whenever their enable pin is high, the 74HC374 samples the input lines only during the low-to-high transition ($\uparrow$) of the clock. This prevents race conditions and feedback loops in synchronous pipelines.
- **Independent Output Enable:** Toggling `~OE~` HIGH disconnects the outputs from the bus without clearing or altering the internal flip-flop state. When `~OE~` returns LOW, the previously stored byte appears on the outputs immediately.

## Absolute maximum ratings

> [!WARNING]
> Stresses beyond these ratings cause permanent damage. Functional operation at these limits is not guaranteed.

| Parameter | Rating | Unit |
|---|---|---|
| Supply Voltage ($V_{CC}$) | $-0.5$ to $+7.0$ | V |
| Input Diode Current ($I_{IK}$, $V_I < 0$ or $V_I > V_{CC}$) | $\pm 20$ | mA |
| Output Diode Current ($I_{OK}$, $V_O < 0$ or $V_O > V_{CC}$) | $\pm 20$ | mA |
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
| Propagation Delay (CLK to Q) | $t_{pd}$ | — | 15 | 28 | ns | $V_{CC} = 4.5\text{ V}, C_L = 50\text{ pF}$ |
| Output Enable Time (~OE~ to Q) | $t_{en}$ | — | 14 | 28 | ns | $V_{CC} = 4.5\text{ V}, C_L = 50\text{ pF}$ |
| Max Clock Frequency | $f_{MAX}$ | 31 | 50 | — | MHz | $V_{CC} = 4.5\text{ V}, C_L = 50\text{ pF}$ |
| Setup Time ($D$ to CLK) | $t_s$ | 15 | 6 | — | ns | $V_{CC} = 4.5\text{ V}$ |
| Hold Time ($D$ to CLK) | $t_h$ | 3 | 0 | — | ns | $V_{CC} = 4.5\text{ V}$ |

## Typical application

### Microprocessor Parallel Data Bus Buffer / Instruction Register

```
         8-Bit Shared System Data Bus (D0 - D7)
         ══════════════╦══════════════
                       ║
               ┌───────┴───────┐
               │ 1D ... 8D     │
               │               │
  Bus Strobe ──► CLK   74HC374 │
  Read Enable ─► ~OE~          │
               │               │
               │ 1Q ... 8Q     │
               └───────┬───────┘
                       ║
         ══════════════╩══════════════
         Internal CPU Execution Bus
```

## Common mistakes

- **Confusing with 74HC373 (Transparent Latch):** The 74HC373 is level-sensitive: whenever its latch enable (`LE`) pin is HIGH, outputs follow the inputs in real time. The 74HC374 is **edge-triggered**: data transfers only on the rising clock edge ($\uparrow$). Using a latch in place of a flip-flop in state machines causes feedback oscillation.
- **Clock Line Noise and Slow Rise Times:** Because the clock input is edge-triggered, slow or noisy clock transitions ($t_r > 500\text{ ns}$) can trigger multiple false clocks. Always drive the clock from a clean digital output or Schmitt-trigger buffer (such as the 74HC14).
- **Leaving `~OE~` Floating:** Always tie `~OE~` to a defined logic level (or pull down to GND through a resistor if outputs should always be active).

## Notes

- **74HC374 vs 74HC574:** The 74HC374 has an interleaved pinout (inputs and outputs alternate on both sides of the chip). The **74HC574** is electrically identical but features a modern "flow-through" pinout (all 8 inputs on pins 2–9, all 8 outputs directly opposite on pins 12–19), making PCB routing significantly simpler.
