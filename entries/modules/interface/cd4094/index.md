## Overview

The **CD4094B** (and its second-source variants **HEF4094B**, **MC14094B**) is a CMOS 8-stage serial shift-and-store bus register with 3-state outputs manufactured by Texas Instruments, Nexperia, and ON Semiconductor. It functions as the wide-voltage CMOS 4000 series equivalent to the popular 74HC595, operating across an extended supply range of $3.0\text{ V}$ to $18.0\text{ V}$.

Data is shifted into the 8-stage register on the positive-going edge of **`CLOCK`**. Stored data is transferred into parallel output latches whenever the **`STROBE`** input is driven HIGH. Parallel outputs ($Q_1$ through $Q_8$) are controlled by an active-high **`OUTPUT ENABLE`** (OE) terminal. Furthermore, the CD4094B provides two dedicated serial outputs for cascading: **$Q_S$** (which updates on the rising clock edge) and **$Q'_S$** (which updates on the falling clock edge), enabling reliable serial chaining across multiple devices without clock skew race conditions.

## Quick reference

| | |
|---|---|
| **Function** | 8-Stage Shift-and-Store Bus Register with 3-State Outputs |
| **Logic Family** | CMOS 4000B Series |
| **Supply Voltage Range ($V_{DD}$)** | $3.0\text{ V}$ to $18.0\text{ V}$ DC ($5\text{V}$, $10\text{V}$, $15\text{V}$ nominal) |
| **Register Width** | 8 Bits ($Q_1 \dots Q_8$) with intermediate storage latches |
| **Max Clock Frequency ($f_{CL}$)** | $2.5\text{ MHz}$ at $5\text{V}$, $5.5\text{ MHz}$ at $10\text{V}$, $7.0\text{ MHz}$ at $15\text{V}$ |
| **Propagation Delay ($t_{pd}$)** | $150\text{ ns}$ typ at $10\text{V}$ ($300\text{ ns}$ at $5\text{V}$) |
| **Output Enable Polarities** | `OUTPUT ENABLE` = Active-HIGH; `STROBE` = Active-HIGH |
| **Cascading Serial Outputs** | $Q_S$ (Positive-edge triggered), $Q'_S$ (Negative-edge triggered) |
| **Operating Temperature** | $-55^\circ\text{C}$ to $+125^\circ\text{C}$ |
| **Package Options** | 16-pin DIP (E), SOIC-16 (M), TSSOP-16 (PW) |

## Pin configuration

### 16-Pin DIP / SOIC Package

```
             ┌───┴───┐
      STROBE 1│ 1   16│ VDD (+3V to +18V)
        DATA 2│       │15 OUTPUT ENABLE (Active-HIGH)
       CLOCK 3│       │14 Q5
          Q1 4│ CD4094│13 Q6
          Q2 5│       │12 Q7
          Q3 6│       │11 Q8
          Q4 7│       │10 Q'S (Serial out, falling edge)
   (GND) VSS 8│       │ 9 QS  (Serial out, rising edge)
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `STROBE` | Digital Input | Storage latch transfer control (`HIGH` = transparent / latched to outputs, `LOW` = hold current latched data) |
| 2 | `DATA` | Digital Input | Serial data input |
| 3 | `CLOCK` | Digital Input | Clock input (Shifts data on rising edge $\uparrow$) |
| 4 | `Q1` | 3-State Output | Parallel output stage 1 (first bit) |
| 5 | `Q2` | 3-State Output | Parallel output stage 2 |
| 6 | `Q3` | 3-State Output | Parallel output stage 3 |
| 7 | `Q4` | 3-State Output | Parallel output stage 4 |
| 8 | `VSS` | Power / Ground | Ground reference terminal ($0\text{ V}$) |
| 9 | `QS` | Digital Output | Cascading serial output (Synchronized to rising clock edge $\uparrow$) |
| 10 | `Q'S` | Digital Output | Cascading serial output (Synchronized to falling clock edge $\downarrow$) |
| 11 | `Q8` | 3-State Output | Parallel output stage 8 (last bit) |
| 12 | `Q7` | 3-State Output | Parallel output stage 7 |
| 13 | `Q6` | 3-State Output | Parallel output stage 6 |
| 14 | `Q5` | 3-State Output | Parallel output stage 5 |
| 15 | `OE` | Digital Input | Output Enable (Active-HIGH; `HIGH` = outputs enabled, `LOW` = High-Z) |
| 16 | `VDD` | Power Supply | Positive supply voltage ($+3.0\text{ V}$ to $+18.0\text{ V}$) |

## Functional description

### Function Truth Table

| `CLOCK` | `OE` | `STROBE` | `DATA` | $Q_1$ | $Q_n$ | $Q_S$ | $Q'_S$ | Description |
|---|---|---|---|---|---|---|---|---|
| $\uparrow$ | `LOW` | X | X | **`Z`** | **`Z`** | $Q_7$ | No Chg | Shifter shifts; parallel outputs in High-Z |
| $\downarrow$ | `LOW` | X | X | **`Z`** | **`Z`** | No Chg | $Q_S$ | $Q'_S$ updates on falling clock edge |
| $\uparrow$ | `HIGH` | `LOW` | X | No Chg | No Chg | $Q_7$ | No Chg | Shifter shifts; storage latches hold prior byte |
| $\uparrow$ | `HIGH` | `HIGH` | `LOW` | **`LOW`** | $Q_{n-1}$ | $Q_7$ | No Chg | Shifter advances; 0 latched to $Q_1$ |
| $\uparrow$ | `HIGH` | `HIGH` | `HIGH` | **`HIGH`** | $Q_{n-1}$ | $Q_7$ | No Chg | Shifter advances; 1 latched to $Q_1$ |
| $\downarrow$ | `HIGH` | `HIGH` | X | No Chg | No Chg | No Chg | $Q_S$ | $Q'_S$ updates on falling edge |

- **Glitch-Free Output Latching:** Keeping `STROBE` LOW while clocking in a new 8-bit word prevents intermediate shifting states from appearing on $Q_1 \dots Q_8$. Once all 8 bits are shifted in, pulsing `STROBE` HIGH transfers the new byte instantaneously to the output pins.
- **Dual Cascading Outputs ($Q_S$ vs $Q'_S$):**
  - **$Q_S$:** Updates on the rising clock edge. Ideal for low-speed cascading or when both devices share short, matched clock lines.
  - **$Q'_S$:** Updates on the falling clock edge. By delaying the downstream data change by half a clock period ($180^\circ$ out of phase), $Q'_S$ provides massive setup time margin and prevents clock skew race conditions when cascading long chains across separate circuit boards.

### Comparison: CD4094B vs 74HC595

| Feature | CD4094B | 74HC595 |
|---|---|---|
| **Operating Voltage Range** | **$3.0\text{ V}$ to $18.0\text{ V}$** | $2.0\text{ V}$ to $6.0\text{ V}$ |
| **Output Enable (`OE`)** | **Active-HIGH** (`HIGH` = outputs on) | **Active-LOW** (`LOW` = outputs on) |
| **Latch Strobe (`STR`)** | Level-sensitive transparent latch | Edge-triggered storage register (`RCLK` $\uparrow$) |
| **Cascading Serial Outputs** | **Two pins** ($Q_S$ rising, $Q'_S$ falling edge) | One pin ($Q_{H'}$ rising edge) |
| **Maximum Clock Frequency** | $\approx 2.5\text{ MHz}$ at $5\text{V}$, $5.5\text{ MHz}$ at $10\text{V}$ | $\approx 25\text{ MHz} \dots 50\text{ MHz}$ at $5\text{V}$ |
| **Typical Output Drive** | $\pm 1.0\text{ mA}$ at $5\text{V}$, $\pm 3.0\text{ mA}$ at $10\text{V}$ | $\pm 6.0\text{ mA}$ at $4.5\text{V}$ continuous |

## Absolute maximum ratings

> [!WARNING]
> Stresses beyond these ratings will cause permanent damage.

| Parameter | Symbol | Min | Max | Unit |
|---|---|---|---|---|
| Supply Voltage (referenced to $V_{SS}$) | $V_{DD}$ | $-0.5$ | $+20.0$ | V |
| Input Voltage (all inputs) | $V_I$ | $-0.5$ | $V_{DD} + 0.5$ | V |
| DC Input Current (any one pin) | $I_I$ | — | $\pm 10$ | mA |
| Power Dissipation ($T_A = -55^\circ\text{C} \dots 100^\circ\text{C}$, DIP-16) | $P_D$ | — | $500$ | mW |
| Operating Temperature Range | $T_A$ | $-55$ | $+125$ | °C |
| Storage Temperature Range | $T_{stg}$ | $-65$ | $+150$ | °C |

## Electrical characteristics

### Static DC Characteristics ($T_A = 25^\circ\text{C}$)

| Parameter | Symbol | $V_{DD}$ | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|---|
| High-Level Output Voltage | $V_{OH}$ | $5\text{ V}$ | 4.95 | 5.0 | — | V | $|I_O| < 1\,\mu\text{A}$ |
| | | $10\text{ V}$ | 9.95 | 10.0 | — | V | $|I_O| < 1\,\mu\text{A}$ |
| | | $15\text{ V}$ | 14.95 | 15.0 | — | V | $|I_O| < 1\,\mu\text{A}$ |
| Low-Level Output Voltage | $V_{OL}$ | $5\text{ V}$ | — | 0 | 0.05 | V | $|I_O| < 1\,\mu\text{A}$ |
| | | $10\text{ V}$ | — | 0 | 0.05 | V | $|I_O| < 1\,\mu\text{A}$ |
| | | $15\text{ V}$ | — | 0 | 0.05 | V | $|I_O| < 1\,\mu\text{A}$ |
| High-Level Input Voltage | $V_{IH}$ | $5\text{ V}$ | 3.5 | 2.75 | — | V | $V_O = 0.5\text{V or } 4.5\text{V}$ |
| | | $10\text{ V}$ | 7.0 | 5.5 | — | V | $V_O = 1.0\text{V or } 9.0\text{V}$ |
| | | $15\text{ V}$ | 11.0 | 8.25 | — | V | $V_O = 1.5\text{V or } 13.5\text{V}$ |
| Low-Level Input Voltage | $V_{IL}$ | $5\text{ V}$ | — | 2.25 | 1.5 | V | $V_O = 0.5\text{V or } 4.5\text{V}$ |
| | | $10\text{ V}$ | — | 4.5 | 3.0 | V | $V_O = 1.0\text{V or } 9.0\text{V}$ |
| | | $15\text{ V}$ | — | 6.75 | 4.0 | V | $V_O = 1.5\text{V or } 13.5\text{V}$ |
| Output Drive Current (Source) | $I_{OH}$ | $5\text{ V}$ | $-0.51$ | $-1.0$ | — | mA | $V_O = 4.6\text{ V}$ |
| | | $10\text{ V}$ | $-1.3$ | $-2.6$ | — | mA | $V_O = 9.5\text{ V}$ |
| Quiescent Device Current | $I_{DD}$ | $5\text{ V}$ | — | 0.04 | 5.0 | µA | $V_{IN} = V_{DD}\text{ or } V_{SS}$ |
| | | $10\text{ V}$ | — | 0.04 | 10.0 | µA | $V_{IN} = V_{DD}\text{ or } V_{SS}$ |
| | | $15\text{ V}$ | — | 0.04 | 20.0 | µA | $V_{IN} = V_{DD}\text{ or } V_{SS}$ |

### Dynamic Switching Characteristics ($C_L = 50\text{ pF}, T_A = 25^\circ\text{C}$)

| Parameter | Symbol | $V_{DD}$ | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
| Maximum Clock Frequency | $f_{CL}$ | $5\text{ V}$ | 1.25 | 2.5 | — | MHz |
| | | $10\text{ V}$ | 2.5 | 5.5 | — | MHz |
| | | $15\text{ V}$ | 3.5 | 7.0 | — | MHz |
| Propagation Delay (`CLK` to $Q_n$) | $t_{PLH}, t_{PHL}$ | $5\text{ V}$ | — | 300 | 600 | ns |
| | | $10\text{ V}$ | — | 150 | 300 | ns |
| 3-State Output Disable Time (`OE` to High-Z) | $t_{PHZ}, t_{PLZ}$ | $5\text{ V}$ | — | 140 | 280 | ns |
| | | $10\text{ V}$ | — | 70 | 140 | ns |
| Data Setup Time ($D$ to `CLK` $\uparrow$) | $t_{su}$ | $5\text{ V}$ | 160 | 80 | — | ns |
| | | $10\text{ V}$ | 80 | 40 | — | ns |
| Data Hold Time ($D$ to `CLK` $\uparrow$) | $t_h$ | $5\text{ V}$ | 60 | 30 | — | ns |
| | | $10\text{ V}$ | 40 | 20 | — | ns |

## Typical application circuit: Cascaded 16-Bit Display Driver (+12V Rail)

Two CD4094B ICs cascaded using the negative-edge $Q'_S$ output (pin 10) to prevent clock race conditions across a noisy ribbon cable.

```
       +12V Power Bus
       ────────────────────────┬────────────────────────────────┬──────────────────────────┬─── +12V
                               │                                │                          │
                             ┌─┴──┐                           ┌─┴──┐                     ┌─┴──┐
                             │C1  │ 0.1µF                     │ 16 │ (VDD)               │ 16 │ (VDD)
                             │MLCC│                           │ 15 │ (OE)                │ 15 │ (OE)
                             └─┬──┘                         ┌─┴────┴────┐              ┌─┴────┴────┐
                               │                            │ CD4094 #1 │              │ CD4094 #2 │
       DATA From MCU ──────────┼────────────────────────────┤ 2 (DATA)  │              │           │
       (+12V Level)            │                            │           │              │           │
       CLOCK From MCU ─────────┼───────────────────┬────────┤ 3 (CLK)   ├──────┬───────┤ 3 (CLK)   │
                               │                   │        │           │      │       │           │
       STROBE From MCU ────────┼─────────────┬─────┼────────┤ 1 (STR)   ├───┐  │       │ 1 (STR)   │
                               │             │     │        │           │   │  │       │           │
                               │             │     │        │ 10 (Q'S)  ├───┼──┼───────┤ 2 (DATA)  │ (Chained)
                               │             │     │        └─────┬─────┘   │  │       └─────┬─────┘
                               │             │     │              │         │  │             │
                               │             │     │         Q1-Q8│(Pins)   └──┼─────────────┘
                               │             │     │          4-7, 11-14       │          Q1-Q8 (Pins 4-7, 11-14)
                               │             │     │              │            │             │
                               │             │     │              ▼            │             ▼
                               │             │     │         To Outputs        │        To Outputs
                               │             │     │         (Bits 0..7)       │        (Bits 8..15)
                               │             │     │                           │
                               │             │     │          8 (VSS)          │          8 (VSS)
       GND (0V) ───────────────┴─────────────┴─────┴──────────┴───┬────────────┴──────────┴───┬─────── 0V
                                                                  │                           │
                                                                [GND]                       [GND]
```

## Design considerations & common mistakes

- **Active-HIGH Output Enable:** Remember that `OE` (pin 15) is **active-HIGH**. If replacing a 74HC595 (where `~OE~` is active-low and typically grounded), connecting pin 15 to ground will completely disable all outputs into High-Z. Connect pin 15 to $V_{DD}$ for permanently enabled outputs.
- **Level-Sensitive Strobe:** Unlike the edge-triggered `RCLK` of a 74HC595, `STROBE` on the CD4094B is a **transparent latch level enable**. As long as `STROBE` is HIGH, any data shifting through the register appears immediately at outputs $Q_1 \dots Q_8$. To prevent output flicker during data loading, keep `STROBE` LOW while clocking, and apply a single HIGH pulse only after all 8 bits are shifted in.
- **Cascading Selection ($Q_S$ vs $Q'_S$):** Always use $Q'_S$ (pin 10) for cascading when clock lines are long, high-capacitance, or driven by slow edges. Because $Q'_S$ transitions on the falling clock edge while the receiving register samples on the rising edge, this guarantees half a clock cycle of setup and hold time margin, virtually eliminating clock race conditions.
- **CMOS Input Termination:** Unconnected CMOS inputs on the CD4094B will float into the intermediate linear region, causing high supply current and false clocking. Tie all unused control pins firmly to $V_{DD}$ or $V_{SS}$.
