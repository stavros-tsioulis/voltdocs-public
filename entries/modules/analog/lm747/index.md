## Overview

The **LM747** (commonly **LM747N** or **$\mu\text{A}747$** in a 14-pin DIP package) is a classic dual general-purpose operational amplifier IC manufactured by Texas Instruments, Fairchild, and National Semiconductor. It integrates **two independent 741-type operational amplifiers** on a single chip.

Each amplifier stage in the LM747 features short-circuit protection, internal frequency compensation, no latch-up under over-voltage, and **dedicated Offset Null pins** for precision DC voltage zeroing. It is popular in vintage analog audio, educational electronics, and legacy test gear repairs.

## Quick reference

| | |
|---|---|
| **Op-Amp Type** | Dual General-Purpose Operational Amplifier (Dual 741) |
| **Package** | 14-Pin DIP (Through-Hole) / CDIP-14 |
| **Supply Voltage Range ($V_{CC}$)** | $\pm 3.0\text{ V}$ to $\pm 18.0\text{ V}$ ($6.0\text{ V}$ to $36.0\text{ V}$ single supply) |
| **Gain Bandwidth Product (GBW)** | $1.0\text{ MHz}$ |
| **Slew Rate** | $0.5\text{ V}/\mu\text{s}$ |
| **Offset Nulling** | Dedicated Offset Null pins for both amplifier channels |
| **Short-Circuit Protection** | Continuous output short-circuit protection to ground |

## Pinout (14-Pin DIP Package)

```
        ┌──────────────┐
   1IN- ─│ 1         14 │─ 1OFFSET NULL (a)
   1IN+ ─│ 2         13 │─ 1V+
 1OS(b) ─│ 3         12 │─ 1OUT
     V- ─│ 4         11 │─ N.C.
 2OS(b) ─│ 5         10 │─ 2OUT
   2IN+ ─│ 6          9 │─ 2V+
   2IN- ─│ 7          8 │─ 2OFFSET NULL (a)
        └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `1IN-` | Operational Amplifier 1 inverting input |
| 2 | `1IN+` | Operational Amplifier 1 non-inverting input |
| 3 | `1OFFSET NULL (b)`| Operational Amplifier 1 Offset Null pin b |
| 4 | `V-` | Common negative power supply rail ($-15\text{V}$ for dual supply, $0\text{V}$ for single supply) |
| 5 | `2OFFSET NULL (b)`| Operational Amplifier 2 Offset Null pin b |
| 6 | `2IN+` | Operational Amplifier 2 non-inverting input |
| 7 | `2IN-` | Operational Amplifier 2 inverting input |
| 8 | `2OFFSET NULL (a)`| Operational Amplifier 2 Offset Null pin a |
| 9 | `2V+` | Operational Amplifier 2 positive supply rail |
| 10 | `2OUT` | Operational Amplifier 2 output pin |
| 11 | `N.C.` | No Connection |
| 12 | `1OUT` | Operational Amplifier 1 output pin |
| 13 | `1V+` | Operational Amplifier 1 positive supply rail |
| 14 | `1OFFSET NULL (a)`| Operational Amplifier 1 Offset Null pin a |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage Range | $V_{CC}$ | $\pm 3.0$ | $\pm 15$ | $\pm 18$ | V | Operational dual supply |
| Input Offset Voltage | $V_{IO}$ | — | 1.0 | 5.0 | mV | $R_S \le 10\text{k}\Omega, T_A = 25^\circ\text{C}$ |
| Input Bias Current | $I_{IB}$ | — | 80 | 500 | nA | |
| Large Signal Voltage Gain | $A_{VD}$ | 50 | 200 | — | V/mV | $V_{CC} = \pm 15\text{V}, R_L \ge 2\text{k}\Omega$ |
| Slew Rate | $SR$ | — | 0.5 | — | $\text{V}/\mu\text{s}$ | |
| Supply Current | $I_{CC}$ | — | 3.4 | 5.6 | mA | Both amplifiers ($I_O = 0$) |

## Common mistakes

- **Confusing 14-pin LM747 pinout with 8-pin dual op-amps:** Unlike modern dual op-amps (like LM358 or TL072 which use an 8-pin footprint), the LM747 uses a 14-pin DIP footprint with separate positive supply pins (`1V+` and `2V+`) and offset null pins.
- **Single-supply operation near GND:** The 741 topology does not feature a ground-sensing input stage. When operated on a single supply (e.g. $+15\text{V}$ to $0\text{V}$), inputs must be biased to at least $+3.0\text{ V}$ above GND.

## Notes

- **Dual 741 Legacy:** The LM747 is effectively two 741 op-amps in one 14-pin IC, sharing only the common negative supply pin (Pin 4: `V-`).
