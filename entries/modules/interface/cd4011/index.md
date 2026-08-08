## Overview

The **CD4011B** (HEF4011B) is a quad 2-input NAND gate IC in the classic CMOS 4000 series manufactured by Texas Instruments, ON Semiconductor, and Renesas. Containing four independent 2-input NAND gates in a 14-pin DIP/SOIC package, it operates across a wide supply voltage range from **3.0V to 18.0V DC**.

Because of its high voltage rating (up to 18V), low power consumption, and noise immunity, the CD4011B is widely used in 12V automotive electronics, industrial sensor interfaces, high-voltage RC oscillators, touch sensors, and latching relay drivers.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VDD`)** | 3.0 V to 18.0 V DC |
| **Logic Family** | CMOS 4000 Series (CD4000 / HEF4000) |
| **Independent Gates** | 4 (Quad 2-Input NAND) |
| **Propagation Delay** | $60\text{ ns}$ typical at $VDD = 10\text{V}$ |
| **Output Drive Current** | $\pm 1.5\text{ mA}$ at $VDD = 10\text{V}$ |
| **Package** | 14-pin DIP / SOIC-14 / TSSOP-14 |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
          1A 1│ 1   14│ VDD
          1B 2│       │13 4B
         1/Y 3│ CD4011│12 4A
         2/Y 4│       │11 4/Y
          2A 5│       │10 3/Y
          2B 6│       │9  3B
         VSS 7│       │8  3A
             └───────┘
```

*Crucial Note: Output pins on CD4011 are on Pins 3, 4, 10, 11 (unlike 74HC00 outputs on Pins 3, 6, 8, 11).*

| Pin | Name | Description |
|---|---|---|
| 1 | `1A` | Gate 1 Input A |
| 2 | `1B` | Gate 1 Input B |
| 3 | `1/Y` | Gate 1 Output ($1Y = \overline{1A \cdot 1B}$) |
| 4 | `2/Y` | Gate 2 Output ($2Y = \overline{2A \cdot 2B}$) |
| 5 | `2A` | Gate 2 Input A |
| 6 | `2B` | Gate 2 Input B |
| 7 | `VSS` | Ground reference (0 V) |
| 8 | `3A` | Gate 3 Input A |
| 9 | `3B` | Gate 3 Input B |
| 10 | `3/Y` | Gate 3 Output ($3Y = \overline{3A \cdot 3B}$) |
| 11 | `4/Y` | Gate 4 Output ($4Y = \overline{4A \cdot 4B}$) |
| 12 | `4A` | Gate 4 Input A |
| 13 | `4B` | Gate 4 Input B |
| 14 | `VDD` | Positive power supply voltage (+3.0V to +18.0V DC) |

## Function & Truth Table (Per Gate)

| Input A | Input B | Output Y |
|---|---|---|
| Low ($L$) | Low ($L$) | High ($H$) |
| Low ($L$) | High ($H$) | High ($H$) |
| High ($H$) | Low ($L$) | High ($H$) |
| High ($H$) | High ($H$) | Low ($L$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 3.0 | 10.0 | 18.0 | V | DC |
| High-Level Input Voltage | $V_{IH}$ | 3.5 | — | — | V | $V_{DD} = 5\text{V}$ |
| Low-Level Input Voltage | $V_{IL}$ | — | — | 1.5 | V | $V_{DD} = 5\text{V}$ |
| Propagation Delay ($A,B \rightarrow Y$) | $t_{PHL}, t_{PLH}$ | — | 60 | 120 | ns | $V_{DD} = 10\text{V}$ |
| High Output Drive Current | $I_{OH}$ | $-0.5$ | $-1.6$ | — | mA | $V_{DD} = 5\text{V}, V_{OH} = 4.6\text{V}$ |
| Quiescent Supply Current | $I_{DD}$ | — | 0.02 | 1.0 | µA | $V_{DD} = 5\text{V}$ |

## Typical Applications

### 12V Latching Touch Sensor Relay Circuit

Using two gates of a CD4011 powered directly from $12\text{V}$ DC to form an active-LOW Set-Reset latch driving a relay transistor.

```
  Touch Set (/S) ────► [Pin 1: 1A]   [Pin 3: 1/Y] ──┬──► [Pin 5: 2A]
                             │                      │
                             └───[Cross Feedback]───┼──┐
                                                    │  │
  Touch Reset (/R) ──► [Pin 6: 2B]   [Pin 4: 2/Y] ──┴──┼──► Transistor Relay Driver
                             │                         │
                             └─────────────────────────┘
```

## Common mistakes

- **Mixing up CD4011 and 74HC00 pinouts:** Although both are 14-pin DIP Quad 2-Input NAND ICs, Gate 2's output is on **Pin 4** in CD4011, but on **Pin 6** in 74HC00. Plugging a CD4011 into a 74HC00 socket shorts outputs to inputs.
- **Assuming high output current drive:** CD4000-series output stages supply only $1\text{ mA} \dots 2\text{ mA}$ at 5V. Do not attempt to drive LEDs or relays directly; use a NPN transistor (e.g. 2N2222) or MOSFET to buffer the output.
- **Floating unused gate inputs:** Leave no CMOS inputs floating. Tie unused input pins directly to **$V_{DD}$ or $V_{SS}$ (GND)**.

## Notes

- **CD4011 vs 74HC00:** CD4011 supports up to 18V supply voltage; 74HC00 is limited to 6V but operates 10x faster.
