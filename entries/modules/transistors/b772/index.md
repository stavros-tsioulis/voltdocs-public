## Overview

The **B772** (officially **2SB772**) is a -30V -3A medium-power silicon PNP bipolar junction transistor manufactured by NEC, Toshiba, UTC (Unisonic), and STMicroelectronics. Housed in a through-hole **TO-126 (SOT-32)** plastic package with a central mounting hole, it is renowned for its extraordinarily low saturation voltage.

Providing a continuous collector current rating of **$-3.0\text{A}$** ($-7.0\text{A}$ pulsed peak) and a collector saturation voltage ($V_{CE(sat)}$) as low as **$-0.3\text{V} \dots -0.5\text{V}$ at $-2.0\text{A}$**, the B772 operates with minimal conduction losses. Serving as the official PNP complement to the **D882 (2SD882)**, the B772 is ubiquitous in Asian consumer electronics, found in **low-voltage emergency lamp inverters, discrete audio power amplifiers, camera flash triggers, linear voltage regulator pass elements, and toy RC car bidirectional motor drivers**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | Medium-Power Low-Saturation Silicon PNP BJT |
| **Package** | TO-126 / SOT-32 (3-pin through-hole with mounting hole) / SOT-89 |
| **Collector-Emitter Breakdown ($V_{CEO}$)**| **$-30\text{ V}$ max** |
| **Collector-Base Breakdown ($V_{CBO}$)** | **$-40\text{ V}$ max** |
| **Continuous Collector Current ($I_C$)** | **$-3.0\text{ A}$ max** ($-7.0\text{ A}$ pulsed peak) |
| **Base Current ($I_B$)** | **$-0.5\text{ A}$ max** |
| **Collector Saturation ($V_{CE(sat)}$)** | **$-0.3\text{ V}$ typ / $-0.5\text{ V}$ max** at $I_C = -2.0\text{A}, I_B = -200\text{mA}$ |
| **DC Current Gain ($h_{FE}$)** | **$60$ to $400$** (Classified by gain rank: R, Q, P, E) |
| **Transition Frequency ($f_T$)** | **$80\text{ MHz} \dots 100\text{ MHz}$** |
| **Power Dissipation ($P_D$)** | **$10.0\text{ Watts}$** ($T_C = 25^\circ\text{C}$ with heatsink) / $1.0\text{ W}$ in free air |
| **Complementary NPN Pair** | **D882 (2SD882)** |

## Pinout (TO-126 Package - Japanese JIS Standard)

Looking at the **printed front face** of the TO-126 package with leads pointing downward:

```
        ┌───────────────┐
        │   O [Mount]   │
        ├───────────────┤
        │     B772      │
        └─┬─────┬─────┬─┘
          1     2     3
          E     C     B
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `EMITTER (E)` | Emitter Terminal | Emitter (Connect to positive power supply rail) |
| 2 | `COLLECTOR (C)`| Collector Terminal| Collector (Connected to switched load; internally bonded to rear metal tab) |
| 3 | `BASE (B)` | Base Terminal | Base control input (Driven with base current via series resistor) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$ | -30 | — | — | V | $I_C = -10\text{mA}, I_B = 0$ |
| Collector-Base Breakdown | $V_{(BR)CBO}$ | -40 | — | — | V | $I_C = -100\ \mu\text{A}, I_E = 0$ |
| Emitter-Base Breakdown | $V_{(BR)EBO}$ | -6.0 | — | — | V | $I_E = -10\ \mu\text{A}, I_C = 0$ |
| Collector Cutoff Current | $I_{CBO}$ | — | — | -1.0 | µA | $V_{CB} = -30\text{V}, I_E = 0$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 60 | — | 400 | — | $I_C = -1.0\text{A}, V_{CE} = -2.0\text{V}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | -0.30 | -0.50 | V | $I_C = -2.0\text{A}, I_B = -200\text{mA}$ |
| Base Saturation Voltage | $V_{BE(sat)}$ | — | -1.00 | -2.00 | V | $I_C = -2.0\text{A}, I_B = -200\text{mA}$ |
| Transition Frequency | $f_T$ | 50 | 80 | — | MHz | $I_C = -500\text{mA}, V_{CE} = -5.0\text{V}$ |

## $h_{FE}$ Classification Ranks

| Rank | $h_{FE}$ Range | Application Suitability |
|---|---|---|
| **R** | $60 \dots 120$ | High-power switching |
| **Q** | $100 \dots 200$ | General-purpose power switching |
| **P** | **$160 \dots 320$** | **Audio amplifier drivers & general DIY kits** |
| **E** | **$200 \dots 400$** | **High-gain audio preamplifiers & low-current drive** |

## Comparison: B772 vs BD140 vs TIP42C

| Parameter | B772 | BD140 | TIP42C |
|---|---|---|---|
| **$V_{CEO}$ Voltage** | $-30\text{ V}$ | **$-80\text{ V}$** | **$-100\text{ V}$** |
| **Max Current ($I_C$)** | **$-3.0\text{ A}$** | $-1.5\text{ A}$ | $-6.0\text{ A}$ |
| **Saturation $V_{CE(sat)}$**| **$-0.3\text{ V}$ at 2A (Ultra-Low)** | $-0.5\text{ V}$ at 0.5A | $-1.5\text{ V}$ at 6A |
| **Package** | TO-126 (Compact) | TO-126 (Compact) | TO-220 (Large) |

## Common mistakes

- **Exceeding the -30V breakdown limit:** The B772 is designed for low-voltage ($3.7\text{V} \dots 24\text{V}$) high-current circuits. Do not use in $36\text{V} \dots 48\text{V}$ systems; use the **BD140** instead.
- **Operating without a heatsink at 2A+ loads:** Although $V_{CE(sat)}$ is low, continuous operation above $1.0\text{A}$ requires mounting the TO-126 tab to a heatsink.

## Notes

- **Naming Convention:** `2SB772` is the full Japanese Industrial Standard (JIS) part number; `B772` is the standard top-mark abbreviation printed on the physical package.
