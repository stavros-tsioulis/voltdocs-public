## Overview

The **74HC151** (SN74HC151 / 74HCT151) is a high-speed silicon-gate CMOS 8-to-1 line data selector / multiplexer IC manufactured by Texas Instruments, Nexperia, and onsemi. Available in a 16-pin through-hole **DIP-16** and surface-mount **SOIC-16 / TSSOP-16** package, it routes one of eight digital data inputs ($I_0 \dots I_7$) to a pair of complementary outputs ($Y$ non-inverted, and $W$ inverted) based on a 3-bit binary address ($S_0, S_1, S_2$).

Operating across a wide supply range of **$2.0\text{V}$ to $6.0\text{V}$ DC** with a typical propagation delay of only **$15\text{ ns}$ at $5\text{V}$**, the 74HC151 features an active-LOW Strobe / Enable ($\bar{E}$) input. It is widely used in digital logic design for **parallel-to-serial data conversion, data bus multiplexing, digital signal routing, and universal 3-variable Boolean logic function generation** (synthesizing arbitrary truth tables without discrete gate arrays).

## Quick reference

| | |
|---|---|
| **Logic Family** | High-Speed CMOS (74HC) / TTL-Compatible (74HCT) |
| **Function** | 8-Channel to 1-Line Data Multiplexer |
| **Package** | 16-pin DIP (DIP-16 / PDIP-16) / 16-pin SOIC / TSSOP-16 |
| **Supply Voltage ($V_{CC}$)** | $2.0\text{ V}$ to $6.0\text{ V}$ (74HC) / $4.5\text{ V} \dots 5.5\text{ V}$ (74HCT) |
| **Propagation Delay ($t_{pd}$)** | $15\text{ ns}$ typ ($30\text{ ns}$ max) at $V_{CC} = 5.0\text{ V}$ |
| **Output Drive Current ($I_{OH}/I_{OL}$)**| $\pm 4.0\text{ mA}$ at $5.0\text{ V}$ ($10\text{ LSTTL}$ load fan-out) |
| **Outputs** | Complementary True ($Y$) and Inverted ($W / \bar{Y}$) |
| **Enable Control** | Active-LOW Enable ($\bar{E}$ / Pin 7) |

## Pinout (DIP-16 Package)

```
                            ┌───┴───┐
                       I3  1│ 1   16│ VCC (+2V to +6V)
                       I2  2│       │15 I4
                       I1  3│ 74HC  │14 I5
                       I0  4│  151  │13 I6
        (True Output)  Y   5│ DIP-16│12 I7
    (Inverted Output)  W   6│       │11 S0 (Select LSB)
    (Active-Low Enable)E   7│       │10 S1 (Select)
                      GND  8│       │9  S2 (Select MSB)
                            └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `I3` | Digital Input | Data Input 3 |
| 2 | `I2` | Digital Input | Data Input 2 |
| 3 | `I1` | Digital Input | Data Input 1 |
| 4 | `I0` | Digital Input | Data Input 0 |
| 5 | `Y` | Digital Output | Selected data output (Non-inverted / True) |
| 6 | `W` | Digital Output | Complementary selected data output (Inverted / $\bar{Y}$) |
| 7 | `E` | Digital Input | Active-LOW Strobe / Enable ($\bar{E}$; tie to GND to enable) |
| 8 | `GND` | Power | Common Ground reference ($0\text{ V}$) |
| 9 | `S2` | Digital Input | Binary Select Address Bit 2 (Most Significant Bit) |
| 10 | `S1` | Digital Input | Binary Select Address Bit 1 |
| 11 | `S0` | Digital Input | Binary Select Address Bit 0 (Least Significant Bit) |
| 12 | `I7` | Digital Input | Data Input 7 |
| 13 | `I6` | Digital Input | Data Input 6 |
| 14 | `I5` | Digital Input | Data Input 5 |
| 15 | `I4` | Digital Input | Data Input 4 |
| 16 | `VCC` | Power | Positive Supply Voltage ($+2.0\text{ V}$ to $+6.0\text{ V}$) |

## Function / Truth Table

| Enable ($\bar{E}$) | Select $S_2$ (Pin 9) | Select $S_1$ (Pin 10) | Select $S_0$ (Pin 11) | Output $Y$ (Pin 5) | Output $W$ (Pin 6) |
|---|---|---|---|---|---|
| **H** | X | X | X | **L** | **H** |
| **L** | L | L | L | **$I_0$** | $\bar{I_0}$ |
| **L** | L | L | H | **$I_1$** | $\bar{I_1}$ |
| **L** | L | H | L | **$I_2$** | $\bar{I_2}$ |
| **L** | L | H | H | **$I_3$** | $\bar{I_3}$ |
| **L** | H | L | L | **$I_4$** | $\bar{I_4}$ |
| **L** | H | L | H | **$I_5$** | $\bar{I_5}$ |
| **L** | H | H | L | **$I_6$** | $\bar{I_6}$ |
| **L** | H | H | H | **$I_7$** | $\bar{I_7}$ |

## Universal Logic Function Generation Example

The 74HC151 can implement **any 3-input Boolean logic function** $F(A,B,C)$ without any extra gates:
1. Connect inputs $A, B, C$ to select pins $S_2, S_1, S_0$.
2. For each minterm of the truth table, tie the corresponding input $I_n$ to $V_{CC}$ (for logic 1) or GND (for logic 0).
3. The desired Boolean function output appears directly at $Y$.

## Common mistakes

- **Leaving Enable Pin 7 ($\bar{E}$) floating:** If $\bar{E}$ floats or is pulled HIGH, the multiplexer is disabled: output $Y$ is forced LOW and $W$ is forced HIGH regardless of select address inputs. Always pull Pin 7 to **GND (0V)** for normal operation.
- **Confusing with analog multiplexers (CD4051):** The 74HC151 is a purely unidirectional **digital logic data selector** with internal CMOS logic buffers. It cannot pass bidirectional analog voltages or audio signals. (For analog signals, use the **CD4051**).

## Notes

- **74HC vs 74HCT:** 74HC operates from $2.0\text{V} \dots 6.0\text{V}$ with CMOS switching levels; 74HCT operates from $4.5\text{V} \dots 5.5\text{V}$ with TTL-compatible input switching thresholds ($V_{IH} = 2.0\text{V}$).
