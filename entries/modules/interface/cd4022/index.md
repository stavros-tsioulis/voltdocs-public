## Overview

The **CD4022B** (HEF4022B / HCF4022B) is a 4-stage Johnson octal counter with eight decoded active-HIGH outputs manufactured by Texas Instruments, onsemi, and Renesas. Housed in a through-hole **DIP-16** and surface-mount **SOIC-16** package, it serves as the 8-state counterpart to the 10-state CD4017 decade counter.

On each positive clock transition (with CLOCK INHIBIT held LOW), the CD4022B advances its count sequentially, asserting exactly one decoded output ($Q_0 \dots Q_7$) HIGH while all others remain LOW. An asynchronous RESET input forces the counter back to $Q_0$, and a CARRY OUT signal ($Q_{0-3}$) allows effortless cascading for multi-stage frequency division. Operating across a wide supply range of **$3.0\text{V}$ to $18.0\text{V}$ DC**, the CD4022B is standard hardware in **8-step analog synthesizer sequencers (Baby 8 sequencers), 8-LED running light chasers, binary-to-octal decoding, rotary multi-position switch emulation, and 3-bit Johnson frequency dividers**.

## Quick reference

| | |
|---|---|
| **Logic Family** | CMOS 4000 Series (CD4000B High-Voltage) |
| **Counter Architecture**| 4-Stage Johnson Counter with 8 Decoded Outputs |
| **Package** | 16-pin DIP (DIP-16 / PDIP-16) / SOIC-16 / TSSOP-16 |
| **Supply Voltage ($V_{DD}$)**| **$3.0\text{ V}$ to $18.0\text{ V}$ DC** |
| **Decoded Outputs** | 8 Mutually Exclusive Active-HIGH Outputs ($Q_0 \dots Q_7$) |
| **Max Clock Frequency** | **$5.0\text{ MHz}$ at $10\text{V}$** ($2.5\text{ MHz}$ at $5\text{V}$) |
| **Control Inputs** | CLOCK (Positive Edge), CLOCK INHIBIT (Active-HIGH), RESET (Active-HIGH) |
| **Cascading Output** | CARRY OUT (Complete 8-count square wave output) |
| **10-Output Counter Twin**| **CD4017B** (Decade Counter with 10 Outputs) |

## Pinout (DIP-16 Package)

```
                            ┌───┴───┐
                   (Out) Q1 1│ 1   16│ VDD (+3V to +18V)
                   (Out) Q0 2│       │15 RESET (Active-High)
                   (Out) Q2 3│ CD4022│14 CLOCK (Active Rising Edge)
                   (Out) Q5 4│       │13 CLOCK INHIBIT (Low=Run, High=Stop)
                   (Out) Q6 5│ DIP-16│12 CARRY OUT (Cout)
            (No Connection) 6│       │11 Q4 (Out)
                   (Out) Q3 7│       │10 Q7 (Out)
                  (GND) VSS 8│       │ 9 NC (No Connection)
                            └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `Q1` | Output | Decoded Count Output 1 (Goes HIGH during Count 1) |
| 2 | `Q0` | Output | Decoded Count Output 0 (HIGH upon Reset / Initial state) |
| 3 | `Q2` | Output | Decoded Count Output 2 |
| 4 | `Q5` | Output | Decoded Count Output 5 |
| 5 | `Q6` | Output | Decoded Count Output 6 |
| 6, 9 | `NC` | No Connect | Unused internal pins (Leave unconnected) |
| 7 | `Q3` | Output | Decoded Count Output 3 |
| 8 | `VSS` | Power | Common Circuit Ground ($0\text{ V}$) |
| 10 | `Q7` | Output | Decoded Count Output 7 (Final state of 8-count cycle) |
| 11 | `Q4` | Output | Decoded Count Output 4 |
| 12 | `CARRY OUT` | Output | Carry Output (HIGH for counts 0–3, LOW for counts 4–7) |
| 13 | `CLK INHIBIT` | Input | Clock Enable (Tie to GND for normal counting; HIGH pauses clock) |
| 14 | `CLOCK` | Input | Clock input (Advances counter on LOW-to-HIGH rising edge) |
| 15 | `RESET` | Input | Asynchronous Reset (Pulse HIGH to force counter to $Q_0 = 1$) |
| 16 | `VDD` | Power | Positive Supply Rail ($+3.0\text{ V}$ to $+18.0\text{ V}$) |

## Typical Application: 8-Step "Baby 8" Analog Synthesizer Sequencer

```
     555 Timer / LFO Clock Pulse
                 │
                 ├───► [Pin 14: CLOCK]
                 │        CD4022B
                 │     [Pin 13: CLK INH] ───► GND (Enabled)
                 │     [Pin 15: RESET]   ───► GND (or to Step Switch for < 8 Steps)
                 │
                 ├───► [Pin 2: Q0] ───► [100kΩ Potentiometer 1] ──┐
                 ├───► [Pin 1: Q1] ───► [100kΩ Potentiometer 2] ──┤
                 ├───► [Pin 3: Q2] ───► [100kΩ Potentiometer 3] ──┤
                 ├───► [Pin 7: Q3] ───► [100kΩ Potentiometer 4] ──┤
                 ├───► [Pin 11: Q4] ──► [100kΩ Potentiometer 5] ──┼──► Control Voltage (CV Out to Synth VCO)
                 ├───► [Pin 4: Q5] ───► [100kΩ Potentiometer 6] ──┤
                 ├───► [Pin 5: Q6] ───► [100kΩ Potentiometer 7] ──┤
                 └───► [Pin 10: Q7] ──► [100kΩ Potentiometer 8] ──┘
```

## Comparison: CD4022B vs CD4017B

| Parameter | CD4022B | CD4017B |
|---|---|---|
| **Architecture** | 4-Stage Johnson (8 Counts) | 5-Stage Johnson (10 Counts) |
| **Number of Decoded Outputs**| **8 Outputs ($Q_0 \dots Q_7$)** | 10 Outputs ($Q_0 \dots Q_9$) |
| **Musical Sequencer Fit** | **Perfect 8-Step (1 Measure)** | Requires resetting at 8 steps |
| **Binary Modulo** | **Natural Power of 2 (Modulo 8)** | Decimal (Modulo 10) |
| **Supply Range** | $3.0\text{V} \dots 18.0\text{V}$ | $3.0\text{V} \dots 18.0\text{V}$ |

## Common mistakes

- **Leaving CLOCK INHIBIT floating:** Pin 13 is active-HIGH. If left floating, capacitive pickup will hold it HIGH, freezing the counter. Always tie Pin 13 to **GND** for continuous operation.
- **Assuming consecutive pin sequence for outputs:** Like the CD4017, the physical outputs are scrambled around the perimeter for internal silicon optimization ($Q_1$ is on Pin 1, $Q_0$ on Pin 2, $Q_2$ on Pin 3, $Q_5$ on Pin 4, etc.). Double-check your PCB routing against the pinout table.

## Notes

- **Truncating the Sequence (e.g. 4-step or 6-step loop):** To make a sequence shorter than 8 steps, connect the desired termination output (e.g., $Q_6$ for a 6-step loop) directly to the **RESET (Pin 15)** input.
