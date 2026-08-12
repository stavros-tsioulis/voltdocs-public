## Overview

The **CD4053** (CD4053B / HEF4053B) is a triple 2-channel analog multiplexer and demultiplexer IC manufactured by Texas Instruments, ON Semiconductor, and Renesas. It contains three independent single-pole double-throw (SPDT) digitally-controlled analog switches (`Channel A`, `Channel B`, and `Channel C`).

Operating over a wide supply range of **3.0V to 18.0V DC** (with dual-rail AC audio capability down to $V_{EE} = -9.0\text{V}$), the CD4053 is widely used for stereo audio channel switching, sensor signal routing, programmable gain amplifier selection, and A/B signal switching in DIY synths and audio mixers.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VDD - VSS`)** | 3.0 V to 18.0 V DC (CD4000B) / 2.0V to 6.0V DC (74HC4053) |
| **Bipolar Negative Rail (`VEE`)** | Down to $-9.0\text{ V}$ DC (for dual-rail AC audio signals) |
| **Channels** | Triple 2-Channel (3x SPDT Switches: `A`, `B`, `C`) |
| **On-Resistance ($R_{ON}$)** | $125\ \Omega$ typical at $VDD = 15\text{V}$ ($240\ \Omega$ at $10\text{V}$) |
| **Signal Bandwidth** | $60\text{ MHz}$ (-3 dB cutoff frequency) |
| **Control Inputs** | 3 Independent Select Lines ($A$, $B$, $C$), Inhibit ($INH$) |
| **Package** | 16-pin DIP / SOIC-16 / TSSOP-16 |

## Pinout (DIP-16 Package)

```
             ┌───┴───┐
          b1 1│ 1   16│ VDD (+3V to +18V)
          b0 2│       │15 b (COMMON B)
          c1 3│ CD4053│14 a (COMMON A)
   c (COMMON)4│       │13 a1
          c0 5│       │12 a0
         INH 6│       │11 A (Select A)
         VEE 7│       │10 B (Select B)
         VSS 8│       │9  C (Select C)
             └───────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `b1` | Channel B Switch State 1 |
| 2 | `b0` | Channel B Switch State 0 |
| 3 | `c1` | Channel C Switch State 1 |
| 4 | `c` | Common Channel C Terminal |
| 5 | `c0` | Channel C Switch State 0 |
| 6 | `INH` | Inhibit Input (High = Disconnect all channels; Low = Enable active switches) |
| 7 | `VEE` | Negative Voltage Rail (Connect to GND for single supply) |
| 8 | `VSS` | Digital Ground (0 V) |
| 9 | `C` | Select Line for Channel C (Low = `c0`; High = `c1`) |
| 10 | `B` | Select Line for Channel B (Low = `b0`; High = `b1`) |
| 11 | `A` | Select Line for Channel A (Low = `a0`; High = `a1`) |
| 12 | `a0` | Channel A Switch State 0 |
| 13 | `a1` | Channel A Switch State 1 |
| 14 | `a` | Common Channel A Terminal |
| 15 | `b` | Common Channel B Terminal |
| 16 | `VDD` | Positive Power Supply (+3.0V to +18.0V DC) |

## Function Table (Per Channel)

| INH | Select ($A/B/C$) | Connected Switch Path |
|---|---|---|
| Low ($0$) | Low ($0$) | Common terminal connected to State `0` ($a \leftrightarrow a_0$) |
| Low ($0$) | High ($1$) | Common terminal connected to State `1` ($a \leftrightarrow a_1$) |
| High ($1$)| X | High-Z Off (All switches disconnected) |

## Common mistakes

- **Leaving `VEE` (Pin 7) floating:** For single-supply DC circuits ($0\text{V} \dots 5\text{V}$), `VEE` **must be tied to `VSS` (GND)**.
- **Routing signals outside supply limits ($V_{EE} \le V_{SIGNAL} \le V_{DD}$):** Signals exceeding $V_{DD}$ or dropping below $V_{EE}$ trip ESD diodes and distort audio waveforms.

## Notes

- **CD4053 vs CD4051 vs CD4052:** CD4051 is a single 8-channel mux; CD4052 is a dual 4-channel mux; CD4053 is a triple 2-channel SPDT switch array.
