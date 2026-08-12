## Overview

The **MCP602** (commonly **MCP602-I/P** in DIP-8 or **MCP602-I/SN** in SOIC-8) is a low-power, rail-to-rail input and output dual operational amplifier manufactured by Microchip Technology. Fabricated using advanced CMOS processing, it operates from a single supply voltage of **$2.7\text{ V}$ to $6.0\text{ V}$** while consuming only **$325\ \mu\text{A}$** per amplifier.

With a typical input bias current of just **$1\text{ pA}$**, a gain-bandwidth product of **$2.8\text{ MHz}$**, and a $2.3\text{ V}/\mu\text{s}$ slew rate, the MCP602 is ideal for 3.3V and 5V microcontroller sensor signal conditioning (photodiodes, piezoelectric sensors, strain gauges, active filters) where true rail-to-rail dynamic range is required.

## Quick reference

| | |
|---|---|
| **Op-Amp Type** | Dual Rail-to-Rail Input/Output Low-Power CMOS Operational Amplifier |
| **Package** | 8-Pin DIP (Through-Hole) / SOIC-8 / TSSOP-8 |
| **Supply Voltage Range ($V_{DD}$)** | $2.7\text{ V}$ to $6.0\text{ V}$ DC |
| **Rail-to-Rail Architecture** | Full Rail-to-Rail Input ($V_{SS} - 0.3\text{V}$ to $V_{DD} + 0.3\text{V}$) and Output ($V_{SS} + 50\text{mV}$ to $V_{DD} - 50\text{mV}$) |
| **Input Bias Current** | $1\text{ pA}$ typical at $25^\circ\text{C}$ |
| **Gain Bandwidth Product (GBW)** | $2.8\text{ MHz}$ |
| **Slew Rate** | $2.3\text{ V}/\mu\text{s}$ |
| **Quiescent Current** | $325\ \mu\text{A}$ typical per channel |

## Pinout (Standard Dual Op-Amp 8-Pin Package)

```
        ┌──────────┐
  VOUTA ─│ 1      8 │─ VDD
  VINA- ─│ 2      7 │─ VOUTB
  VINA+ ─│ 3      6 │─ VINB-
    VSS ─│ 4      5 │─ VINB+
        └──────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `VOUTA` | Operational Amplifier A output |
| 2 | `VINA-` | Operational Amplifier A inverting input |
| 3 | `VINA+` | Operational Amplifier A non-inverting input |
| 4 | `VSS` | Ground reference (0 V) or negative supply rail |
| 5 | `VINB+` | Operational Amplifier B non-inverting input |
| 6 | `VINB-` | Operational Amplifier B inverting input |
| 7 | `VOUTB` | Operational Amplifier B output |
| 8 | `VDD` | Positive power supply rail (+2.7V to +6.0V DC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage Range | $V_{DD}$ | 2.7 | 5.0 | 6.0 | V | Operational range |
| Input Offset Voltage | $V_{OS}$ | — | 2.0 | 4.5 | mV | $V_{DD} = 5.0\text{V}, V_{CM} = V_{DD}/2$ |
| Input Bias Current | $I_{B}$ | — | 1.0 | 100 | pA | $T_A = 25^\circ\text{C}$ |
| Slew Rate | $SR$ | — | 2.3 | — | $\text{V}/\mu\text{s}$ | |
| Gain Bandwidth Product | $GBW$ | — | 2.8 | — | MHz | |
| Quiescent Current | $I_Q$ | — | 325 | 450 | $\mu\text{A}$ | Per channel ($I_O = 0$) |

## Common mistakes

- **Exceeding 6.0V supply rating:** Unlike standard LM358 op-amps that accept up to 32V, the MCP602 absolute maximum supply voltage is $7.0\text{ V}$. Connecting it to a 12V supply will instantly destroy the chip.
- **Unused op-amp left floating:** Unused channels in dual op-amp packages must not be left floating. Wire the unused amplifier as a voltage follower ($V_{OUT}$ connected to $V_{IN-}$) with $V_{IN+}$ connected to mid-supply ($V_{DD}/2$).

## Notes

- **Rail-to-Rail Advantage:** Unlike LM358 which clips $1.5\text{ V}$ below $V_{DD}$, the MCP602 output swings within $50\text{ mV}$ of both supply rails, maximizing ADC input range on 3.3V or 5V microcontrollers.
