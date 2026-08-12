## Overview

The **TLV2372** (commonly **TLV2372IP** in DIP-8 or **TLV2372ID** in SOIC-8) is a fast, wide-supply-range, rail-to-rail input/output dual operational amplifier IC manufactured by Texas Instruments. It combines high bandwidth (**$3.0\text{ MHz}$**) and fast slew rate (**$2.4\text{ V}/\mu\text{s}$**) with a wide single-supply operating range of **$2.7\text{ V}$ to $16.0\text{ V}$** DC ($\pm 1.35\text{ V} \dots \pm 8.0\text{ V}$).

Unlike standard 5V rail-to-rail op-amps limited to 6V maximum, the TLV2372 supports supply voltages up to 16V with full rail-to-rail input common-mode voltage range and low CMOS input bias current ($1\text{ pA}$ typ), making it ideal for 12V automotive sensors, active filters, and precision industrial instrument signal conditioning.

## Quick reference

| | |
|---|---|
| **Op-Amp Type** | Fast Wide-Supply Rail-to-Rail Input/Output Dual Op-Amp |
| **Package** | 8-Pin DIP (Through-Hole) / SOIC-8 / VSSOP-8 |
| **Supply Voltage Range ($V_{DD}$)** | $2.7\text{ V}$ to $16.0\text{ V}$ DC ($\pm 1.35\text{ V}$ to $\pm 8.0\text{ V}$ dual supply) |
| **Gain Bandwidth Product (GBW)** | $3.0\text{ MHz}$ |
| **Slew Rate** | $2.4\text{ V}/\mu\text{s}$ |
| **Input Bias Current** | $1\text{ pA}$ typical (CMOS Input) |
| **Rail-to-Rail Range** | Input: $V_{DD-} - 0.2\text{V}$ to $V_{DD+} + 0.2\text{V}$ / Output: within $150\text{mV}$ of rails |
| **Quiescent Supply Current** | $550\ \mu\text{A}$ typical per channel |

## Pinout (Standard Dual Op-Amp 8-Pin Package)

```
        ┌──────────┐
  1OUT ─│ 1      8 │─ VDD
  1IN- ─│ 2      7 │─ 2OUT
  1IN+ ─│ 3      6 │─ 2IN-
   GND ─│ 4      5 │─ 2IN+
        └──────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `1OUT` | Operational Amplifier 1 output |
| 2 | `1IN-` | Operational Amplifier 1 inverting input |
| 3 | `1IN+` | Operational Amplifier 1 non-inverting input |
| 4 | `GND` / `V-` | Ground reference (0 V) or negative supply rail |
| 5 | `2IN+` | Operational Amplifier 2 non-inverting input |
| 6 | `2IN-` | Operational Amplifier 2 inverting input |
| 7 | `2OUT` | Operational Amplifier 2 output |
| 8 | `VDD` / `V+` | Positive power supply rail (+2.7V to +16.0V DC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage Range | $V_{DD}$ | 2.7 | 5.0 / 12.0 | 16.0 | V | Operational range |
| Input Offset Voltage | $V_{OS}$ | — | 2.0 | 4.5 | mV | $V_{DD} = 5\text{V}, T_A = 25^\circ\text{C}$ |
| Input Bias Current | $I_{B}$ | — | 1.0 | 60 | pA | $T_A = 25^\circ\text{C}$ |
| Gain Bandwidth Product | $GBW$ | — | 3.0 | — | MHz | $C_L = 100\text{pF}$ |
| Slew Rate | $SR$ | — | 2.4 | — | $\text{V}/\mu\text{s}$ | |
| Common-Mode Rejection | $CMRR$ | 60 | 75 | — | dB | |
| Supply Current | $I_{DD}$ | — | 550 | 750 | $\mu\text{A}$ | Per channel ($I_O = 0$) |

## Common mistakes

- **Assuming 32V input capability like LM358:** While the TLV2372 handles 16V (far higher than 6V 5V-only CMOS op-amps), it is NOT rated for 24V or 32V industrial supplies. Exceeding 16.5V destroys the chip.
- **Driving heavy capacitive loads without isolation:** Driving capacitive loads above $500\text{ pF}$ without a small series isolation resistor ($10\ \Omega \dots 100\ \Omega$) on the output pin can cause ringing and overshoot.

## Notes

- **High-Voltage Rail-to-Rail Performance:** Replaces legacy LM358 op-amps in 12V automotive and industrial designs, offering 3x higher bandwidth, 5x faster slew rate, and full rail-to-rail swing.
