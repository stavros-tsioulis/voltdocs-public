## Overview

The **D882** (officially **2SD882**) is a 30V 3A medium-power silicon NPN bipolar junction transistor manufactured by NEC, Toshiba, UTC (Unisonic), and STMicroelectronics. Housed in a through-hole **TO-126 (SOT-32)** plastic package with a central mounting hole, it is renowned for its extraordinarily low saturation voltage.

Rated for a continuous collector current of **$3.0\text{A}$** ($7.0\text{A}$ pulsed peak) and a collector saturation voltage ($V_{CE(sat)}$) as low as **$0.3\text{V} \dots 0.5\text{V}$ at $2.0\text{A}$**, the D882 operates with minimal conduction losses compared to standard medium-power BJTs. Paired with its PNP complement **B772 (2SB772)**, the D882 is ubiquitous throughout Asian electronics in **low-voltage emergency lamp inverters, discrete audio power amplifier output stages, battery-powered camera strobe flash drivers, linear voltage regulator pass elements, and toy RC motor drivers**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | Medium-Power Low-Saturation Silicon NPN BJT |
| **Package** | TO-126 / SOT-32 (3-pin through-hole with mounting hole) / SOT-89 |
| **Collector-Emitter Voltage ($V_{CEO}$)**| **$30\text{ V}$ max** |
| **Collector-Base Voltage ($V_{CBO}$)** | **$40\text{ V}$ max** |
| **Continuous Collector Current ($I_C$)** | **$3.0\text{ A}$ max** ($7.0\text{ A}$ pulsed peak) |
| **Base Current ($I_B$)** | **$0.5\text{ A}$ max** |
| **Collector Saturation ($V_{CE(sat)}$)** | **$0.3\text{ V}$ typ / $0.5\text{ V}$ max** at $I_C = 2.0\text{A}, I_B = 200\text{mA}$ |
| **DC Current Gain ($h_{FE}$)** | **$60$ to $400$** (Classified by gain rank: R, Q, P, E) |
| **Transition Frequency ($f_T$)** | **$90\text{ MHz} \dots 150\text{ MHz}$** |
| **Power Dissipation ($P_D$)** | **$10.0\text{ Watts}$** ($T_C = 25^\circ\text{C}$ with heatsink) / $1.0\text{ W}$ free air |
| **Complementary PNP Pair** | **B772 (2SB772)** |

## Pinout (TO-126 Package - Japanese JIS Standard)

Looking at the **printed front face** of the TO-126 package with leads pointing downward:

```
        ┌───────────────┐
        │   O [Mount]   │
        ├───────────────┤
        │     D882      │
        └─┬─────┬─────┬─┘
          1     2     3
          E     C     B
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `EMITTER` | Emitter Terminal | Emitter (Connect to ground or negative rail) |
| 2 | `COLLECTOR`| Collector Terminal| Collector (Connected to switched load; internally bonded to rear metal tab) |
| 3 | `BASE` | Base Terminal | Base control input (Driven with base current via series resistor) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$ | 30 | — | — | V | $I_C = 10\text{mA}, I_B = 0$ |
| Collector-Base Breakdown | $V_{(BR)CBO}$ | 40 | — | — | V | $I_C = 100\ \mu\text{A}, I_E = 0$ |
| Emitter-Base Breakdown | $V_{(BR)EBO}$ | 6.0 | — | — | V | $I_E = 10\ \mu\text{A}, I_C = 0$ |
| Collector Cutoff Current | $I_{CBO}$ | — | — | 1.0 | µA | $V_{CB} = 30\text{V}, I_E = 0$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 60 | — | 400 | — | $I_C = 1.0\text{A}, V_{CE} = 2.0\text{V}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | 0.30 | 0.50 | V | $I_C = 2.0\text{A}, I_B = 200\text{mA}$ |
| Base Saturation Voltage | $V_{BE(sat)}$ | — | 1.00 | 2.00 | V | $I_C = 2.0\text{A}, I_B = 200\text{mA}$ |
| Transition Frequency | $f_T$ | 50 | 90 | — | MHz | $I_C = 500\text{mA}, V_{CE} = 5.0\text{V}$ |

## $h_{FE}$ Classification Ranks

| Rank | $h_{FE}$ Range | Common Application |
|---|---|---|
| **R** | $60 \dots 120$ | High-power switching |
| **Q** | $100 \dots 200$ | General purpose power switching |
| **P** | **$160 \dots 320$** | **Audio amplifier drivers & general DIY kits** |
| **E** | **$200 \dots 400$** | **High-gain audio output & low-current drive** |

## Comparison: D882 vs BD139 vs TIP31C

| Parameter | D882 | BD139 | TIP31C |
|---|---|---|---|
| **$V_{CEO}$ Voltage** | $30\text{ V}$ | **$80\text{ V}$** | **$100\text{ V}$** |
| **Max Current ($I_C$)** | **$3.0\text{ A}$** | $1.5\text{ A}$ | $3.0\text{ A}$ |
| **Saturation $V_{CE(sat)}$**| **$0.3\text{ V}$ at 2A (Ultra-Low)** | $0.5\text{ V}$ at 0.5A | $1.2\text{ V}$ at 3A |
| **Package** | TO-126 (Compact) | TO-126 (Compact) | TO-220 (Large) |

## Common mistakes

- **Exceeding the 30V breakdown voltage rating:** Unlike the 80V BD139, the D882 has a maximum $V_{CEO}$ limit of **$30\text{V}$**. Connecting it to 36V or 48V power supplies will cause immediate collector-emitter avalanche breakdown.
- **Overheating without a heatsink at 2A+ loads:** Although $V_{CE(sat)}$ is low, switching continuous currents above $1.0\text{A}$ requires mounting the TO-126 tab to a heatsink.

## Notes

- **Naming Convention:** `2SD882` is the full Japanese Industrial Standard (JIS) part number; `D882` is the standard top-mark abbreviation printed on the physical package.
