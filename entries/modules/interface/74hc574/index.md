## Overview

The **74HC574** (SN74HC574) is a high-speed CMOS 8-bit octal D-type edge-triggered flip-flop integrated circuit with 3-state outputs. It provides the exact logical operation of the classic 74HC374 register, but reorganizes all connections into a **flow-through pinout architecture**: all eight data inputs ($1D$ through $8D$) are located in order on the left side of the dual-in-line package (pins 2–9), while all eight corresponding 3-state outputs ($1Q$ through $8Q$) are arranged directly opposite on the right side (pins 19 down to 12).

This flow-through layout drastically simplifies printed circuit board (PCB) trace routing for microprocessor bus interfaces, port expanders, and pipelined data paths by eliminating trace crossovers and vias. Stored data is updated on the positive low-to-high transition ($\uparrow$) of the common clock (`CLK`). Driving the active-low Output Enable (`~OE~`) HIGH places all eight outputs into a high-impedance (High-Z) state, isolating the register from the bus without disturbing stored data.

## Quick reference

| | |
|---|---|
| **Function** | Octal D-Type Edge-Triggered Flip-Flop with 3-State Outputs |
| **Pinout Style** | Flow-Through Architecture (Inputs opposite Outputs) |
| **Logic Family** | High-Speed CMOS (74HC Series) / TTL Compatible (74HCT) |
| **Supply Voltage Range ($V_{CC}$)** | $2.0\text{ V}$ to $6.0\text{ V}$ DC ($4.5\text{ V} \dots 5.5\text{ V}$ nominal) |
| **Register Width** | 8 bits ($1D \dots 8D \rightarrow 1Q \dots 8Q$) |
| **Max Clock Frequency ($f_{MAX}$)** | $50\text{ MHz}$ typ at $4.5\text{V}$ ($60\text{ MHz}$ at $6.0\text{V}$) |
| **Propagation Delay ($t_{pd}$)** | $15\text{ ns}$ typ at $4.5\text{V}$ ($C_L = 50\text{ pF}$) |
| **Output Drive Capability** | $\pm 6.0\text{ mA}$ continuous ($\pm 7.8\text{ mA}$ at $4.5\text{V}$ bus-drive) |
| **Clock Triggering** | Positive edge-triggered ($\uparrow$, low-to-high transition) |
| **Package Options** | 20-pin DIP (N), SOIC-20 (DW), TSSOP-20 (PW) |

## Pin configuration

### 20-Pin DIP / SOIC Package

```
             ┌───┴───┐
       ~OE~ 1│ 1   20│ VCC (+2V to +6V)
         1D 2│       │19 1Q
         2D 3│       │18 2Q
         3D 4│       │17 3Q
         4D 5│ 74HC574 16 4Q
         5D 6│       │15 5Q
         6D 7│       │14 6Q
         7D 8│       │13 7Q
         8D 9│       │12 8Q
        GND 10│      │11 CLK (Clock)
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `~OE~` | Digital Input | Active-low 3-state output enable (`LOW` = drive outputs, `HIGH` = High-Z) |
| 2 | `1D` | Digital Input | Data input bit 1 |
| 3 | `2D` | Digital Input | Data input bit 2 |
| 4 | `3D` | Digital Input | Data input bit 3 |
| 5 | `4D` | Digital Input | Data input bit 4 |
| 6 | `5D` | Digital Input | Data input bit 5 |
| 7 | `6D` | Digital Input | Data input bit 6 |
| 8 | `7D` | Digital Input | Data input bit 7 |
| 9 | `8D` | Digital Input | Data input bit 8 |
| 10 | `GND` | Power Supply | Ground reference ($0\text{ V}$) |
| 11 | `CLK` | Digital Input | Positive edge-triggered clock (Data clocked in on $\uparrow$ transition) |
| 12 | `8Q` | 3-State Output | Register output bit 8 |
| 13 | `7Q` | 3-State Output | Register output bit 7 |
| 14 | `6Q` | 3-State Output | Register output bit 6 |
| 15 | `5Q` | 3-State Output | Register output bit 5 |
| 16 | `4Q` | 3-State Output | Register output bit 4 |
| 17 | `3Q` | 3-State Output | Register output bit 3 |
| 18 | `2Q` | 3-State Output | Register output bit 2 |
| 19 | `1Q` | 3-State Output | Register output bit 1 |
| 20 | `VCC` | Power Supply | Positive supply voltage ($+2.0\text{ V}$ to $+6.0\text{ V}$) |

## Functional description

### Function Truth Table

| Mode | `~OE~` | `CLK` | $D_n$ | $Q_n$ Output | Description |
|---|---|---|---|---|---|
| **Load 1** | **`LOW`** | $\uparrow$ | **`HIGH`** | **`HIGH`** (1) | Clocked high into flip-flop, driven to bus |
| **Load 0** | **`LOW`** | $\uparrow$ | **`LOW`** | **`LOW`** (0) | Clocked low into flip-flop, driven to bus |
| **Hold** | **`LOW`** | `LOW` / `HIGH` / $\downarrow$ | X | $Q_0$ | Retains stored value, outputs remain driven |
| **Store & High-Z** | **`HIGH`** | $\uparrow$ | $D_n$ | **`Z`** | Stores input $D_n$, outputs disabled to High-Z |
| **Hold & High-Z** | **`HIGH`** | `LOW` / `HIGH` / $\downarrow$ | X | **`Z`** | Retains internal state, outputs disabled to High-Z |

- **Edge Triggering vs. Transparent Latch:** Unlike the companion 74HC573 transparent latch—which lets input transitions pass through as long as `LE` is held HIGH—the 74HC574 only samples the data lines at the precise low-to-high transition ($\uparrow$) of the clock. This makes it ideal for synchronous pipelines, finite state machines, and microcomputer registers where race conditions must be eliminated.
- **Independent 3-State Output Enable:** The `~OE~` input affects only the output buffer stage. Changing `~OE~` between LOW and HIGH does not erase or modify the flip-flops' internal memory.

### Comparison: 74HC574 vs 74HC374 and 74HC573

| Feature | 74HC574 | 74HC374 | 74HC573 |
|---|---|---|---|
| **Storage Type** | Edge-Triggered Flip-Flop | Edge-Triggered Flip-Flop | Transparent Latch |
| **Control Signal** | Clock (`CLK`, rising-edge) | Clock (`CLK`, rising-edge) | Latch Enable (`LE`, level-active) |
| **Pinout Layout** | **Flow-Through** (Pins 2–9 In, 19–12 Out) | **Interspersed** (In and Out interleaved) | **Flow-Through** (Pins 2–9 In, 19–12 Out) |
| **PCB Trace Routing** | Straight-line parallel routing | Interleaved routing requiring vias | Straight-line parallel routing |
| **Primary Use** | High-speed bus registers & pipelines | Legacy system replacement | Multiplexed address/data demuxing |

## Absolute maximum ratings

> [!WARNING]
> Stresses beyond these ratings may cause permanent damage. These are absolute stress ratings only; functional operation under these conditions is not implied.

| Parameter | Symbol | Min | Max | Unit |
|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | $-0.5$ | $+7.0$ | V |
| Input Diode Clamp Current ($V_I < 0$ or $V_I > V_{CC}$) | $I_{IK}$ | — | $\pm 20$ | mA |
| Output Diode Clamp Current ($V_O < 0$ or $V_O > V_{CC}$) | $I_{OK}$ | — | $\pm 20$ | mA |
| Continuous Output Drive Current ($V_O = 0\text{ to }V_{CC}$) | $I_O$ | — | $\pm 35$ | mA |
| Continuous Supply / Ground Current | $I_{CC}$ / $I_{GND}$ | — | $\pm 70$ | mA |
| Operating Free-Air Temperature Range | $T_A$ | $-40$ | $+85$ | °C |
| Storage Temperature Range | $T_{stg}$ | $-65$ | $+150$ | °C |

## Electrical characteristics

### Recommended DC Operating Conditions ($T_A = 25^\circ\text{C}$)

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.0 | 5.0 | 6.0 | V | Operating range |
| High-Level Input Voltage | $V_{IH}$ | 1.5 | — | — | V | $V_{CC} = 2.0\text{ V}$ |
| | | 3.15 | — | — | V | $V_{CC} = 4.5\text{ V}$ |
| | | 4.2 | — | — | V | $V_{CC} = 6.0\text{ V}$ |
| Low-Level Input Voltage | $V_{IL}$ | — | — | 0.5 | V | $V_{CC} = 2.0\text{ V}$ |
| | | — | — | 1.35 | V | $V_{CC} = 4.5\text{ V}$ |
| | | — | — | 1.8 | V | $V_{CC} = 6.0\text{ V}$ |
| High-Level Output Voltage | $V_{OH}$ | 4.4 | 4.49 | — | V | $V_{CC} = 4.5\text{ V}, I_{OH} = -20\,\mu\text{A}$ |
| | | 3.84 | 4.3 | — | V | $V_{CC} = 4.5\text{ V}, I_{OH} = -6.0\text{ mA}$ |
| Low-Level Output Voltage | $V_{OL}$ | — | 0.001 | 0.1 | V | $V_{CC} = 4.5\text{ V}, I_{OL} = 20\,\mu\text{A}$ |
| | | — | 0.17 | 0.33 | V | $V_{CC} = 4.5\text{ V}, I_{OL} = 6.0\text{ mA}$ |
| High-Z Output Off-State Current | $I_{OZ}$ | — | — | $\pm 5.0$ | µA | $V_O = V_{CC}\text{ or GND}, V_{CC} = 6.0\text{ V}$ |
| Quiescent Supply Current | $I_{CC}$ | — | — | 8.0 | µA | $V_I = V_{CC}\text{ or GND}, I_O = 0\text{ A}$ |

### Switching & Timing Characteristics ($V_{CC} = 4.5\text{ V}, C_L = 50\text{ pF}, T_A = 25^\circ\text{C}$)

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Maximum Clock Frequency | $f_{MAX}$ | 30 | 50 | — | MHz | $V_{CC} = 4.5\text{ V}$ |
| Propagation Delay (`CLK` to $Q_n$) | $t_{pd}$ | — | 15 | 30 | ns | Output transition |
| 3-State Output Enable Time (`~OE~` to $Q_n$) | $t_{en}$ | — | 15 | 28 | ns | High-Z to active |
| 3-State Output Disable Time (`~OE~` to High-Z) | $t_{dis}$ | — | 15 | 28 | ns | Active to High-Z |
| Data Setup Time ($D_n$ before `CLK` $\uparrow$) | $t_{su}$ | 12 | 5 | — | ns | Setup requirement |
| Data Hold Time ($D_n$ after `CLK` $\uparrow$) | $t_h$ | 5 | 0 | — | ns | Hold requirement |
| Clock Pulse Duration (`CLK` High or Low) | $t_w$ | 16 | 8 | — | ns | Minimum pulse width |

## Typical application: 8-Bit Microcontroller Output Port

The 74HC574 is commonly used as a memory-mapped or GPIO-strobed 8-bit output port. The microcontroller presents data on its data bus ($D0 \dots D7$) and pulses the clock line (`CLK`) HIGH to lock the byte into the register.

```
       Microcontroller                              74HC574 Octal Register
     ┌─────────────────┐                       ┌───────────────────────────────┐
     │                 │                       │                               │
     │      GPIO_D0 ───┼───────────────────────┤ 2  (1D)               (1Q) 19 ├───> Output Bus bit 0
     │      GPIO_D1 ───┼───────────────────────┤ 3  (2D)               (2Q) 18 ├───> Output Bus bit 1
     │      GPIO_D2 ───┼───────────────────────┤ 4  (3D)               (3Q) 17 ├───> Output Bus bit 2
     │      GPIO_D3 ───┼───────────────────────┤ 5  (4D)               (4Q) 16 ├───> Output Bus bit 3
     │      GPIO_D4 ───┼───────────────────────┤ 6  (5D)               (5Q) 15 ├───> Output Bus bit 4
     │      GPIO_D5 ───┼───────────────────────┤ 7  (6D)               (6Q) 14 ├───> Output Bus bit 5
     │      GPIO_D6 ───┼───────────────────────┤ 8  (7D)               (7Q) 13 ├───> Output Bus bit 6
     │      GPIO_D7 ───┼───────────────────────┤ 9  (8D)               (8Q) 12 ├───> Output Bus bit 7
     │                 │                       │                               │
     │     STROBE_WR ──┼───────────────────────┤ 11 (CLK)                      │
     │                 │                       │                               │
     │       BUS_DIR ──┼───────────────────────┤ 1  (~OE~)            (GND) 10 ├─── GND
     │                 │                       │                               │
     │                 │                 +5V ──┤ 20 (VCC)                      │
     └─────────────────┘                       └───────┬───────────────┬───────┘
                                                       │  0.1µF MLCC   │
                                                       └───┤├───[GND]──┘
```

### Operation

1. **Write Cycle:** The MCU outputs byte data onto pins 2–9 ($1D \dots 8D$). After a minimum setup time $t_{su} \ge 12\text{ ns}$, the MCU drives the `STROBE_WR` line HIGH.
2. **Latching:** On the rising clock edge ($\uparrow$), all eight data bits are latched simultaneously into internal D flip-flops.
3. **Bus Drive:** With `~OE~` connected to ground (or driven LOW by `BUS_DIR`), the outputs immediately reflect the newly stored byte and remain stable even if the microcontroller subsequently reuses the data bus for other tasks.

## Design considerations & common mistakes

- **Never Leave Inputs Floating:** Like all high-speed CMOS devices, unconnected input pins ($1D \dots 8D$, `CLK`, or `~OE~`) will float into the high-impedance linear region between $V_{IH}$ and $V_{IL}$, causing excessive power dissipation and erratic oscillations. Pull unused inputs to $V_{CC}$ or GND directly or via a $10\text{ k}\Omega$ resistor.
- **Power Supply Decoupling:** When all eight outputs switch simultaneously from HIGH to LOW (or vice versa) while driving heavy capacitive loads or long bus traces, substantial transient currents ($dI/dt$) occur. Place a $0.1\,\mu\text{F}$ low-ESR ceramic capacitor directly adjacent to pin 20 ($V_{CC}$) and pin 10 (GND).
- **Fast Clock Transitions:** The `CLK` input is edge-sensitive. Avoid feeding slow analog signals or RC-filtered transitions into `CLK` ($t_r, t_f \le 500\text{ ns}$ at $4.5\text{V}$); slow or noisy clock transitions can trigger multiple clockings. If slow signals must clock the register, use a Schmitt-trigger buffer such as the 74HC14 beforehand.
- **Bus Contention on Shared Lines:** When connecting multiple 74HC574 devices or other 3-state drivers to a shared parallel data bus, ensure that their respective `~OE~` enable lines are interlocked or driven by a decoder (e.g., 74HC138) to guarantee "break-before-make" bus handoffs and prevent dead short circuits between competing HIGH and LOW outputs.
