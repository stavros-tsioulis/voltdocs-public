## Overview

The **CD4015B** (and its second sources **HEF4015B**, **MC14015B**) is a CMOS dual 4-stage serial-in / parallel-out (SIPO) static shift register IC manufactured by Texas Instruments, Nexperia, and ON Semiconductor. It consists of two independent 4-stage shift registers integrated onto a single monolithic substrate.

Each 4-bit section features independent **`CLOCK`**, serial **`DATA`**, and asynchronous active-high **`RESET`** inputs, along with fully decoded parallel outputs for each stage ($Q_{A0} \dots Q_{A3}$ and $Q_{B0} \dots Q_{B3}$). Because the internal storage cells are fully static master-slave flip-flops, the device maintains data indefinitely down to $0\text{ Hz}$ (DC). Operating across an exceptionally wide power supply range ($3.0\text{ V}$ to $18.0\text{ V}$), the CD4015B is widely employed in $12\text{V}$ automotive electronics, industrial sequencers, high-voltage LED displays, and digital delay lines.

## Quick reference

| | |
|---|---|
| **Function** | Dual 4-Stage Static Shift Register (SIPO) |
| **Logic Family** | CMOS 4000B Series |
| **Supply Voltage Range ($V_{DD}$)** | $3.0\text{ V}$ to $18.0\text{ V}$ DC ($5\text{V}$, $10\text{V}$, $15\text{V}$ nominal) |
| **Register Capacity** | Dual 4-Bit (Configurable as single 8-Bit) |
| **Max Clock Frequency ($f_{CL}$)** | $3.0\text{ MHz}$ at $5\text{V}$, $6.0\text{ MHz}$ at $10\text{V}$, $8.5\text{ MHz}$ at $15\text{V}$ |
| **Propagation Delay ($t_{pd}$)** | $160\text{ ns}$ typ at $10\text{V}$ ($320\text{ ns}$ at $5\text{V}$) |
| **Reset Operation** | Asynchronous Master Reset (Active-HIGH) |
| **Minimum Clock Frequency** | $0\text{ Hz}$ (DC static retention) |
| **Operating Temperature** | $-55^\circ\text{C}$ to $+125^\circ\text{C}$ |
| **Package Options** | 16-pin DIP (E), SOIC-16 (M), TSSOP-16 (PW) |

## Pin configuration

### 16-Pin DIP / SOIC Package

```
             ┌───┴───┐
       CLKB 1│ 1   16│ VDD (+3V to +18V)
        QB3 2│       │15 DB (Data Input B)
        QA2 3│       │14 RSTB (Reset B)
        QA1 4│ CD4015│13 QB2
        QA0 5│       │12 QB1
       RSTA 6│       │11 QB0
         DA 7│       │10 QA3
  (GND) VSS 8│       │ 9 CLKA
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `CLKB` | Digital Input | Clock input for Register B (shifts on rising edge $\uparrow$) |
| 2 | `QB3` | Digital Output | Parallel output stage 3 (last stage) of Register B |
| 3 | `QA2` | Digital Output | Parallel output stage 2 of Register A |
| 4 | `QA1` | Digital Output | Parallel output stage 1 of Register A |
| 5 | `QA0` | Digital Output | Parallel output stage 0 (first stage) of Register A |
| 6 | `RSTA` | Digital Input | Asynchronous Master Reset for Register A (Active-HIGH; `HIGH` = clear $Q_{A0} \dots Q_{A3}$ to `LOW`) |
| 7 | `DA` | Digital Input | Serial data input for Register A |
| 8 | `VSS` | Power / Ground | Ground reference terminal ($0\text{ V}$) |
| 9 | `CLKA` | Digital Input | Clock input for Register A (shifts on rising edge $\uparrow$) |
| 10 | `QA3` | Digital Output | Parallel output stage 3 (last stage) of Register A |
| 11 | `QB0` | Digital Output | Parallel output stage 0 (first stage) of Register B |
| 12 | `QB1` | Digital Output | Parallel output stage 1 of Register B |
| 13 | `QB2` | Digital Output | Parallel output stage 2 of Register B |
| 14 | `RSTB` | Digital Input | Asynchronous Master Reset for Register B (Active-HIGH; `HIGH` = clear $Q_{B0} \dots Q_{B3}$ to `LOW`) |
| 15 | `DB` | Digital Input | Serial data input for Register B |
| 16 | `VDD` | Power Supply | Positive supply voltage ($+3.0\text{ V}$ to $+18.0\text{ V}$) |

## Functional description

### Function Truth Table (per 4-Stage Register Section)

| Mode | `CLK` | $D$ | `RESET` | $Q_0$ | $Q_1$ | $Q_2$ | $Q_3$ | Description |
|---|---|---|---|---|---|---|---|---|
| **Clear** | X | X | **`HIGH`** | **`LOW`** | **`LOW`** | **`LOW`** | **`LOW`** | Asynchronous reset forces all outputs LOW |
| **Shift 0** | $\uparrow$ | **`LOW`** | `LOW` | **`LOW`** | $Q_{0n-1}$ | $Q_{1n-1}$ | $Q_{2n-1}$ | Shifter advances; zero entered into $Q_0$ |
| **Shift 1** | $\uparrow$ | **`HIGH`** | `LOW` | **`HIGH`** | $Q_{0n-1}$ | $Q_{1n-1}$ | $Q_{2n-1}$ | Shifter advances; one entered into $Q_0$ |
| **Hold** | $\downarrow$ or Level | X | `LOW` | $Q_0$ | $Q_1$ | $Q_2$ | $Q_3$ | No state change during steady clock or falling edge |

- **Active-HIGH Reset:** Notice that unlike 74HC series devices (which almost universally use active-low clear `~CLR~`), the CD4015B reset pins (`RSTA`, `RSTB`) are **active-HIGH**. For normal operation, `RSTA` and `RSTB` must be tied directly to ground ($V_{SS}$).
- **Cascading into an 8-Bit Register:** To form a single 8-bit shift register, connect the fourth stage output of Register A ($Q_{A3}$, pin 10) directly to the serial data input of Register B ($D_B$, pin 15), and tie `CLKA` to `CLKB` and `RSTA` to `RSTB`.

## Absolute maximum ratings

> [!WARNING]
> Exceeding these stress limits may cause permanent degradation or breakdown.

| Parameter | Symbol | Min | Max | Unit |
|---|---|---|---|---|
| DC Supply Voltage (referenced to $V_{SS}$) | $V_{DD}$ | $-0.5$ | $+20.0$ | V |
| Input Voltage (all inputs) | $V_I$ | $-0.5$ | $V_{DD} + 0.5$ | V |
| DC Input Current (any one pin) | $I_I$ | — | $\pm 10$ | mA |
| Power Dissipation ($T_A = -55^\circ\text{C} \dots 100^\circ\text{C}$, DIP-16) | $P_D$ | — | $500$ | mW |
| Operating Free-Air Temperature Range | $T_A$ | $-55$ | $+125$ | °C |
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
| Propagation Delay (`CLK` to $Q_n$) | $t_{PLH}, t_{PHL}$ | $5\text{ V}$ | — | 320 | 640 | ns |
| | | $10\text{ V}$ | — | 160 | 320 | ns |
| | | $15\text{ V}$ | — | 120 | 240 | ns |
| Maximum Clock Frequency | $f_{CL}$ | $5\text{ V}$ | 1.5 | 3.0 | — | MHz |
| | | $10\text{ V}$ | 3.0 | 6.0 | — | MHz |
| | | $15\text{ V}$ | 4.0 | 8.5 | — | MHz |
| Clock Pulse Width | $t_w$ | $5\text{ V}$ | 200 | 100 | — | ns |
| | | $10\text{ V}$ | 100 | 50 | — | ns |
| Data Setup Time | $t_{su}$ | $5\text{ V}$ | 150 | 75 | — | ns |
| | | $10\text{ V}$ | 80 | 40 | — | ns |
| Reset Pulse Width | $t_{w(R)}$ | $5\text{ V}$ | 260 | 130 | — | ns |
| | | $10\text{ V}$ | 140 | 70 | — | ns |

## Typical application circuit: 8-Bit Industrial Sequencer (+12V Rail)

Because the CD4015B tolerates up to $18\text{ V}$, it can operate directly on standard $+12\text{ V}$ industrial or automotive power rails without requiring level shifters or intermediate LDOs.

```
       +12V Industrial Supply
       ────────────────────────┬──────────────────────────────────────────┬─────── +12V
                               │                                          │
                             ┌─┴──┐                                    ┌──┴──┐
                             │C1  │ 0.1µF                              │ 16  │ (VDD)
                             │MLCC│                                  ┌─┴─────┴─┐
                             └─┬──┘                                  │ CD4015B │
                               │                                     │         │
       CLOCK Pulse ────────────┼──────────────────────────┬──────────┤ 9 (CLKA)│
       (+12V CMOS)             │                          │          │         │
                               │                          └──────────┤ 1 (CLKB)│
                               │                                     │         │
       DATA In ────────────────┼─────────────────────────────────────┤ 7 (DA)  │
                               │                                     │         │
                               │                        ┌────────────┤ 10(QA3) │
                               │                        │            │         │
                               │                        └────────────┤ 15(DB)  │ (Cascaded 8-bit)
                               │                                     │         │
       RESET (Active-HIGH) ────┼──────────────────────────┬──────────┤ 6 (RSTA)│
                               │                          │          │         │
                               │                          └──────────┤ 14(RSTB)│
                               │                                     │         │
                               │                     (QA0-QA2) 5,4,3 ┼───[1k]──┼───> Outputs 0..2
                               │                     (QB0-QB3) 11-13 ┼───[1k]──┼───> Outputs 4..6
                               │                                2,10 ┼───[1k]──┼───> Outputs 3, 7
                               │                                     │         │
                               │                                     │ 8 (VSS) │
       GND (0V) ───────────────┴─────────────────────────────────────┴───┬─────┴─────── 0V
                                                                         │
                                                                       [GND]
```

## Design considerations & common mistakes

- **Do Not Leave Reset Pins Floating (Active-HIGH Gotcha):** Engineers accustomed to 74HC series logic often forget that CMOS 4000 series resets are **active-HIGH**. If `RSTA` (pin 6) or `RSTB` (pin 14) is left unconnected, electrostatic charges will pull the inputs HIGH, perpetually freezing the shift register in a cleared ($0\text{ V}$) state. Always tie unused reset pins to $V_{SS}$ (ground).
- **Limited Output Drive at 5V:** At $V_{DD} = 5\text{ V}$, the CD4015B outputs can only source or sink $\approx 0.5\text{ mA} \dots 1.0\text{ mA}$ before output voltages drop severely out of logic spec. If driving standard $20\text{ mA}$ indicator LEDs, relays, or optocouplers, use an intermediate driver array such as the ULN2003A or discrete NPN transistors.
- **Clock Edge Slew Rate:** As a static CMOS device, the clock inputs (`CLKA`, `CLKB`) are sensitive to slow-rising clock waveforms. Slew rates slower than $15\,\mu\text{s}$ at $5\text{V}$ (or $5\,\mu\text{s}$ at $15\text{V}$) can cause parasitic oscillations and false multi-clocking. Use a Schmitt-trigger buffer (e.g. CD40106B) if generating clocks with passive RC circuits.
- **Unused Stage Input Termination:** If only using Register A, never leave the unused inputs of Register B ($D_B$, `CLKB`, `RSTB`) floating. Tie them to $V_{SS}$ or $V_{DD}$ to prevent excessive CMOS shoot-through current.
