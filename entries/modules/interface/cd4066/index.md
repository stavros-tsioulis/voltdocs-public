## Overview

The **CD4066** (CD4066B / HEF4066B) is a quad bilateral analog switch IC manufactured by Texas Instruments, ON Semiconductor, and Renesas. It contains four independent digitally-controlled single-pole single-throw (SPST) analog switches inside a 14-pin package.

Each bilateral switch handles signal peak-to-peak swings up to **18.0V DC** (when $VDD = 18\text{V}$) with a low on-state resistance ($R_{ON} = 80\ \Omega$ typical). Signals travel in either direction with minimal distortion, making the CD4066 widely used in audio muting circuits, programmable filter switching, sample-and-hold circuits, and digital signal gating.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VDD - VSS`)** | 3.0 V to 18.0 V DC (CD4000B) / 2.0V to 6.0V DC (74HC4066) |
| **Switches** | 4 Independent SPST Bilateral Switches ($A, B, C, D$) |
| **Control Signal Level** | Active-HIGH (High = Switch CLOSED/ON; Low = Switch OPEN/OFF) |
| **On-Resistance ($R_{ON}$)** | $80\ \Omega$ typical at $VDD = 15\text{V}$ ($125\ \Omega$ at $10\text{V}$) |
| **Bandwidth** | $40\text{ MHz}$ (-3 dB cutoff frequency) |
| **Off-State Leakage Current** | $\pm 10\text{ pA}$ typical |
| **Package** | 14-pin DIP / SOIC-14 / TSSOP-14 |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
    IN/OUT A 1│ 1   14│ VDD (+3V to +18V)
    OUT/IN A 2│       │13 CONTROL A
    OUT/IN B 3│ CD4066│12 CONTROL D
    IN/OUT B 4│       │11 IN/OUT D
   CONTROL B 5│       │10 OUT/IN D
   CONTROL C 6│       │9  OUT/IN C
    VSS (GND)7│       │8  IN/OUT C
             └───────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `IN/OUT A` | Switch A Input/Output Terminal |
| 2 | `OUT/IN A` | Switch A Output/Input Terminal |
| 3 | `OUT/IN B` | Switch B Output/Input Terminal |
| 4 | `IN/OUT B` | Switch B Input/Output Terminal |
| 5 | `CONTROL B` | Switch B Digital Control Input (Active-HIGH) |
| 6 | `CONTROL C` | Switch C Digital Control Input (Active-HIGH) |
| 7 | `VSS` | Digital Ground (0 V) |
| 8 | `IN/OUT C` | Switch C Input/Output Terminal |
| 9 | `OUT/IN C` | Switch C Output/Input Terminal |
| 10 | `OUT/IN D` | Switch D Output/Input Terminal |
| 11 | `IN/OUT D` | Switch D Input/Output Terminal |
| 12 | `CONTROL D` | Switch D Digital Control Input (Active-HIGH) |
| 13 | `CONTROL A` | Switch A Digital Control Input (Active-HIGH) |
| 14 | `VDD` | Positive Power Supply (+3.0V to +18.0V DC) |

## Function Table (Per Switch)

| Control Input | Switch State | Signal Path State |
|---|---|---|
| High ($1$) | Closed (ON) | Low Resistance ($R_{ON} \approx 80\ \Omega$) |
| Low ($0$) | Open (OFF) | High Impedance (High-Z Off, $> 100\text{ M}\Omega$) |

## Common mistakes

- **Leaving unused control inputs floating:** Unused control pins (`CONTROL A/B/C/D`) **must be pulled LOW to GND** or HIGH to VDD. Floating control inputs cause erratic switch behavior and excessive supply current.
- **Forgetting that $R_{ON}$ varies with signal voltage:** $R_{ON}$ fluctuates slightly as the signal voltage approaches $VDD / 2$. In precision analog circuits requiring flat $R_{ON}$, use modern precision analog switches like the **DG419** or **ADG701**.

## Notes

- **CD4066 vs CD4016:** CD4066 is the upgraded version of CD4016 with much lower $R_{ON}$ ($80\ \Omega$ vs $300\ \Omega$) and constant $R_{ON}$ across the entire input voltage range.
