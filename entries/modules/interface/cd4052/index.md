## Overview

The **CD4052** (CD4052B / HEF4052B) is a dual 4-channel analog multiplexer and demultiplexer IC manufactured by Texas Instruments, ON Semiconductor, and Renesas. It functions as a digitally-controlled dual 4-position rotary switch, independently connecting common input/output terminals `X` and `Y` to one of four channel lines (`0X`–`3X` and `0Y`–`3Y`).

Supporting supply voltages from **3.0V to 18.0V DC** (and bipolar signal swings up to $\pm 9\text{V}$ when $V_{EE} = -9\text{V}$), the CD4052 is bidirectionally transparent, allowing analog audio, sensor signals, or digital bus lines to flow in either direction.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VDD - VSS`)** | 3.0 V to 18.0 V DC (CD4000B) / 2.0V to 6.0V DC (74HC4052) |
| **Bipolar Negative Rail (`VEE`)** | Down to $-9.0\text{ V}$ DC (for dual-rail AC audio signals) |
| **Channels** | Dual 4-Channel (2x 1-of-4 Multiplexer/Demultiplexer) |
| **On-Resistance ($R_{ON}$)** | $125\ \Omega$ typical at $VDD = 15\text{V}$ ($240\ \Omega$ at $10\text{V}$) |
| **Signal Bandwidth** | $60\text{ MHz}$ (-3 dB cutoff frequency) |
| **Control Inputs** | Binary Select lines $A$ and $B$, Inhibit input ($INH$) |
| **Package** | 16-pin DIP / SOIC-16 / TSSOP-16 |

## Pinout (DIP-16 Package)

```
             ┌───┴───┐
          0Y 1│ 1   16│ VDD (+3V to +18V)
          2Y 2│       │15 2X
    Y (COMMON)3│ CD4052│14 1X
          3Y 4│       │13 X (COMMON)
          1Y 5│       │12 0X
         INH 6│       │11 3X
         VEE 7│       │10 A (Select LSB)
         VSS 8│       │9  B (Select MSB)
             └───────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `0Y` | Channel Y Input/Output 0 |
| 2 | `2Y` | Channel Y Input/Output 2 |
| 3 | `Y` | Common Channel Y Input/Output |
| 4 | `3Y` | Channel Y Input/Output 3 |
| 5 | `1Y` | Channel Y Input/Output 1 |
| 6 | `INH` | Inhibit Input (High = Disconnect all channels; Low = Enable active channel) |
| 7 | `VEE` | Negative Voltage Rail (Connect to GND for single supply, or negative voltage for AC signals) |
| 8 | `VSS` | Digital Ground (0 V) |
| 9 | `B` | Binary Select Input Bit 1 (MSB) |
| 10 | `A` | Binary Select Input Bit 0 (LSB) |
| 11 | `3X` | Channel X Input/Output 3 |
| 12 | `0X` | Channel X Input/Output 0 |
| 13 | `X` | Common Channel X Input/Output |
| 14 | `1X` | Channel X Input/Output 1 |
| 15 | `2X` | Channel X Input/Output 2 |
| 16 | `VDD` | Positive Power Supply (+3.0V to +18.0V DC) |

## Truth Table

| INH | B | A | Selected Channel X | Selected Channel Y |
|---|---|---|---|---|
| Low ($0$) | $0$ | $0$ | $0X$ | $0Y$ |
| Low ($0$) | $0$ | $1$ | $1X$ | $1Y$ |
| Low ($0$) | $1$ | $0$ | $2X$ | $2Y$ |
| Low ($0$) | $1$ | $1$ | $3X$ | $3Y$ |
| High ($1$)| X | X | None (High-Z Off) | None (High-Z Off) |

## Common mistakes

- **Leaving `VEE` (Pin 7) floating:** For single-supply DC applications ($0\text{V} \dots 5\text{V}$), `VEE` **must be tied directly to `VSS` (GND)**. Leaving `VEE` floating prevents analog switches from turning ON reliably.
- **Exceeding $VDD$ or $VEE$ signal range:** Analog signals routed through the switches must stay strictly between $V_{EE} \le V_{IN} \le V_{DD}$. Exceeding the supply rails causes internal ESD diode conduction and audio clipping.

## Notes

- **CD4052 vs CD4051 vs CD4053:** CD4051 is a single 8-channel mux; CD4052 is a dual 4-channel mux (stereo audio routing); CD4053 is a triple 2-channel mux (SPDT switches).
