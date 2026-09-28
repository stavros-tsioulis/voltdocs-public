## Overview

The **74HC273** is an 8-bit positive-edge-triggered D-type flip-flop IC manufactured by Texas Instruments, Nexperia, and ON Semiconductor. Equipped with a common clock input and an asynchronous active-low master reset ($\overline{\text{CLR}}$), the 74HC273 captures eight bits of parallel data on the rising edge of the clock signal.

Unlike bus-oriented registers like the 74HC374 or 74HC574, the 74HC273 features dedicated **push-pull outputs** without 3-state control. This makes it the preferred octal register for applications where output lines must remain actively driven at all times—such as driving indicator LEDs, controlling relay banks, latching microcontroller parallel output ports, or implementing pipeline registers in discrete digital state machines.

## Quick reference

| | |
|---|---|
| **Function** | Octal D-Type Flip-Flop with Master Reset |
| **Logic Family** | High-Speed CMOS (74HC Series) |
| **Supply Voltage Range ($V_{CC}$)** | $2.0\text{ V}$ to $6.0\text{ V}$ DC ($4.5\text{V} \dots 5.5\text{V}$ nominal) |
| **Register Width** | 8 bits ($1D \dots 8D \rightarrow 1Q \dots 8Q$) |
| **Max Clock Frequency ($f_{MAX}$)** | $50\text{ MHz}$ typ at $4.5\text{V}$ ($60\text{ MHz}$ at $6.0\text{V}$) |
| **Propagation Delay ($t_{pd}$)** | $15\text{ ns}$ typ at $4.5\text{V}$ |
| **Output Type** | Push-Pull (Always actively driven, non-3-state) |
| **Output Drive Current ($I_O$)** | $\pm 5.2\text{ mA}$ (10 LSTTL loads) |
| **Reset Control** | Asynchronous Master Reset (`~CLR~`, active-LOW) |
| **Packages** | 20-pin PDIP (N), SOIC-20 (DW), TSSOP-20 (PW) |

## Pin configuration

### 20-Pin DIP / SOIC Package

```
               ┌──────────┐
        ~CLR~ ─┤ 1     20 ├─ VCC (+2V to +6V)
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
| 1 | `~CLR~` | Digital Input | Master Reset (Asynchronous, Active-LOW; forces all outputs to 0) |
| 2 | `1Q` | Digital Output | Flip-flop output bit 1 |
| 3 | `1D` | Digital Input | Data input bit 1 |
| 4 | `2D` | Digital Input | Data input bit 2 |
| 5 | `2Q` | Digital Output | Flip-flop output bit 2 |
| 6 | `3Q` | Digital Output | Flip-flop output bit 3 |
| 7 | `3D` | Digital Input | Data input bit 3 |
| 8 | `4D` | Digital Input | Data input bit 4 |
| 9 | `4Q` | Digital Output | Flip-flop output bit 4 |
| 10 | `GND` | Power Supply | System Ground ($0\text{ V}$) |
| 11 | `CLK` | Digital Input | Clock input (Data transferred on low-to-high edge $\uparrow$) |
| 12 | `5Q` | Digital Output | Flip-flop output bit 5 |
| 13 | `5D` | Digital Input | Data input bit 5 |
| 14 | `6D` | Digital Input | Data input bit 6 |
| 15 | `6Q` | Digital Output | Flip-flop output bit 6 |
| 16 | `7Q` | Digital Output | Flip-flop output bit 7 |
| 17 | `7D` | Digital Input | Data input bit 7 |
| 18 | `8D` | Digital Input | Data input bit 8 |
| 19 | `8Q` | Digital Output | Flip-flop output bit 8 |
| 20 | `VCC` | Power Supply | Positive DC supply voltage ($+2.0\text{V} \dots +6.0\text{V}$) |

## Functional description

### Function Truth Table

| Mode | `~CLR~` | `CLK` | $D_n$ | $Q_n$ Output | Description |
|---|---|---|---|---|---|
| **Reset** | **`LOW`** | X | X | **`LOW`** (0) | Asynchronous clear (all 8 outputs forced low immediately) |
| **Load 1** | `HIGH` | $\uparrow$ | **`HIGH`** | **`HIGH`** (1) | Clocked load of logic 1 |
| **Load 0** | `HIGH` | $\uparrow$ | **`LOW`** | **`LOW`** (0) | Clocked load of logic 0 |
| **Hold** | `HIGH` | `LOW` / `HIGH` | X | $Q_0$ | No change while clock is steady |

- **Edge-Triggered Operation:** Data on inputs $1D \dots 8D$ meeting the setup time ($t_s$) requirement is transferred to outputs $1Q \dots 8Q$ exclusively on the rising edge of the clock signal ($\uparrow$). The inputs can change freely at all other times without affecting outputs.
- **Asynchronous Clear:** Pulling `~CLR~` LOW immediately forces all eight outputs to logic 0, overriding both clock and data inputs.

## Absolute maximum ratings

> [!WARNING]
> Stresses beyond these ratings cause permanent damage. Functional operation at these limits is not guaranteed.

| Parameter | Rating | Unit |
|---|---|---|
| Supply Voltage ($V_{CC}$) | $-0.5$ to $+7.0$ | V |
| Input Clamp Current ($I_{IK}$, $V_I < 0$ or $V_I > V_{CC}$) | $\pm 20$ | mA |
| Output Clamp Current ($I_{OK}$, $V_O < 0$ or $V_O > V_{CC}$) | $\pm 20$ | mA |
| Continuous Output Current ($I_O$) | $\pm 25$ | mA |
| Continuous Supply Current ($I_{CC}$ or $I_{GND}$) | $\pm 50$ | mA |
| Operating Ambient Temperature Range | -40 to 85 | °C |
| Storage Temperature Range | -65 to 150 | °C |

## Electrical characteristics

$T_A = 25^\circ\text{C}$, unless otherwise noted.

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| High-Level Input Voltage | $V_{IH}$ | 3.15 | — | — | V | $V_{CC} = 4.5\text{ V}$ |
| Low-Level Input Voltage | $V_{IL}$ | — | — | 1.35 | V | $V_{CC} = 4.5\text{ V}$ |
| High-Level Output Voltage | $V_{OH}$ | 4.4 | 4.49 | — | V | $V_{CC} = 4.5\text{ V}, I_O = -20\text{ }\mu\text{A}$ |
| High-Level Output Voltage | $V_{OH}$ | 3.98 | 4.3 | — | V | $V_{CC} = 4.5\text{ V}, I_O = -5.2\text{ mA}$ |
| Low-Level Output Voltage | $V_{OL}$ | — | 0.01 | 0.1 | V | $V_{CC} = 4.5\text{ V}, I_O = 20\text{ }\mu\text{A}$ |
| Low-Level Output Voltage | $V_{OL}$ | — | 0.17 | 0.26 | V | $V_{CC} = 4.5\text{ V}, I_O = 5.2\text{ mA}$ |
| Propagation Delay (CLK to Q) | $t_{pd}$ | — | 15 | 27 | ns | $V_{CC} = 4.5\text{ V}, C_L = 50\text{ pF}$ |
| Propagation Delay (~CLR~ to Q) | $t_{PHL}$ | — | 16 | 30 | ns | $V_{CC} = 4.5\text{ V}, C_L = 50\text{ pF}$ |
| Max Clock Frequency | $f_{MAX}$ | 31 | 50 | — | MHz | $V_{CC} = 4.5\text{ V}, C_L = 50\text{ pF}$ |
| Setup Time ($D$ to CLK) | $t_s$ | 15 | 7 | — | ns | $V_{CC} = 4.5\text{ V}$ |
| Hold Time ($D$ to CLK) | $t_h$ | 3 | 0 | — | ns | $V_{CC} = 4.5\text{ V}$ |

## Typical application

### Microcontroller 8-Bit Latched Output Port / Relay Driver Buffer

```
     Microcontroller 8-Bit Data Bus (D0 - D7)
     ══════════════╦══════════════
                   ║
           ┌───────┴───────┐
           │ 1D ... 8D     │
           │               │
  GPIO Write ──► CLK       │
  MCU Reset ───► ~CLR~     │
           │    74HC273    │
           │               │
           │ 1Q ... 8Q     │
           └───────┬───────┘
                   ║
     ══════════════╩══════════════
     Actively Driven Outputs to Transistors / ULN2803
```

Because outputs are non-3-state push-pull stages, connected relays or transistors will never float during bus tri-stating, and the asynchronous `~CLR~` ensures that all relays de-energize instantly on power-up reset.

## Common mistakes

- **Leaving `~CLR~` Floating:** The `~CLR~` input is active-LOW. Leaving it floating will allow capacitive noise to trigger spurious resets. Always tie Pin 1 (`~CLR~`) to $V_{CC}$ via a pull-up resistor or connect directly to the system active-low reset bus.
- **Connecting Directly to a Multiplexed Shared Bus:** The 74HC273 does **not** have 3-state outputs; its outputs are always driving high or low. Tying its outputs to a shared data bus will cause bus contention and short circuits. If you need tri-state outputs for bus driving, use the **74HC374** or **74HC574**.
- **Confusing with 74HC373 / 74HC573 Latches:** The 74HC273 is an **edge-triggered flip-flop**, not a transparent latch. Data passes only on the rising clock edge ($\uparrow$).

## Notes

- **74HCT273 Variant:** Provides TTL-compatible input switching thresholds ($V_{IH} \ge 2.0\text{V}$, $V_{IL} \le 0.8\text{V}$) for direct interfacing to 3.3V logic or classic TTL busses.
- **Pinout Note:** The 74HC273 interweaves inputs and outputs around the package perimeter. For designs prioritizing straight flow-through PCB trace routing, consider using the 74HC574.
