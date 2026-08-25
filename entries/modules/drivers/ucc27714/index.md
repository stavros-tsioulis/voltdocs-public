## Overview

The **UCC27714** (UCC27714D) is a 600V high-speed, high-density high-side and low-side gate driver IC engineered by Texas Instruments. Designed as a modern, high-performance successor to legacy gate drivers, it delivers an enormous **$4.0\text{A}$ source and $4.0\text{A}$ sink peak gate drive current** with an industry-leading propagation delay of just **$90\text{ ns}$** ($5\text{ ns}$ typical delay matching).

Operating with gate drive supply voltages from **$10.0\text{ V}$ to $20.0\text{ V}$**, the UCC27714 provides exceptional transient robustness, handling negative voltages on the switch node (`HS`) down to **$-8.0\text{V}$** without latch-up. It includes an active-HIGH enable input (`EN`), separate high- and low-side undervoltage lockouts (UVLO), and separated logic ground (`VSS`) and power ground (`COM`) terminals for high-efficiency phase-shifted full-bridge converters, LLC resonant topologies, solar microinverters, and EV charging stations.

## Quick reference

| | |
|---|---|
| **Driver Type** | High and Low Side Half-Bridge Gate Driver IC |
| **Package** | 14-pin SOIC (D-Package) |
| **High-Side Floating Offset ($V_{HS}$)** | Up to $+600\text{ V}$ DC max (Tolerates $-8.0\text{V}$ transients) |
| **Gate Driver Bias Range ($V_{DD}$)** | $10.0\text{ V}$ to $20.0\text{ V}$ DC |
| **Output Peak Current** | $+4.0\text{ A}$ Source / $-4.0\text{ A}$ Sink peak (at $V_{DD} = 15\text{V}$) |
| **Propagation Delay** | $90\text{ ns}$ typical ($5\text{ ns}$ maximum delay matching) |
| **Rise / Fall Times** | $16\text{ ns}$ Rise / $12\text{ ns}$ Fall ($C_L = 1000\text{ pF}$) |
| **Logic Compatibility** | $3.3\text{ V}$, $5.0\text{ V}$, and $15.0\text{ V}$ CMOS / TTL inputs |
| **Protection Features** | High- & Low-Side UVLO, Negative Transient Immunity, Enable (`EN`) |

## Pinout (SOIC-14 Package)

```
        ┌──────────────┐
     HI ─│ 1         14 │─ VDD
     LI ─│ 2         13 │─ HB
    VSS ─│ 3  UCC    12 │─ HO
     EN ─│ 4  27714  11 │─ HS
    COM ─│ 5         10 │─ NC
     LO ─│ 6          9 │─ NC
    VDD ─│ 7          8 │─ NC
         └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `HI` | High-side gate driver logic input (In-phase with `HO`) |
| 2 | `LI` | Low-side gate driver logic input (In-phase with `LO`) |
| 3 | `VSS` | Logic ground reference (Connects to microcontroller ground) |
| 4 | `EN` | Enable logic input (Active-HIGH: HIGH = Enabled, LOW = Both outputs disabled) |
| 5 | `COM` | Power ground return for low-side gate driver |
| 6 | `LO` | Low-side gate drive output (4.0A peak) |
| 7, 14 | `VDD` | Positive gate driver supply (+10V to +20V DC) |
| 8, 9, 10 | `NC` | No connection (Provides high-voltage safety isolation gap) |
| 11 | `HS` | High-side floating supply return / Half-bridge switching node |
| 12 | `HO` | High-side gate drive output (4.0A peak) |
| 13 | `HB` | High-side floating bootstrap supply pin |

## Control Logic Truth Table

To enable gate drive outputs, `EN` must be held **HIGH**:

| `EN` (Enable) | `HI` (High Input) | `LI` (Low Input) | `HO` (High-Side Gate) | `LO` (Low-Side Gate) | Bridge State |
|---|---|---|---|---|---|
| Low (`0`) | X | X | Low (OFF) | Low (OFF) | **Disabled (Both OFF)** |
| High (`1`) | Low (`0`) | Low (`0`) | Low (OFF) | Low (OFF) | **Both MOSFETs OFF** |
| High (`1`) | High (`1`) | Low (`0`) | High (ON) | Low (OFF) | **High-Side ON** |
| High (`1`) | Low (`0`) | High (`1`) | Low (OFF) | High (ON) | **Low-Side ON** |
| High (`1`) | High (`1`) | High (`1`) | High (ON) | High (ON) | **Shoot-Through Warning** (MCU deadtime required!) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| High-Side Floating Supply Voltage | $V_{HB}$ | -0.3 | — | 620 | V | Relative to COM |
| High-Side Floating Offset Voltage | $V_{HS}$ | -8.0 | — | 600 | V | Relative to COM ($t_{pulse} < 100\text{ ns}$) |
| Gate Driver Supply Voltage | $V_{DD}$ | 10.0 | 15.0 | 20.0 | V | Operating range |
| Peak Sourcing Current | $I_{SRC}$ | — | 4.0 | — | A | $V_{DD} = 15\text{V}, C_L = 100\text{ nF}$ |
| Peak Sinking Current | $I_{SNK}$ | — | 4.0 | — | A | $V_{DD} = 15\text{V}, C_L = 100\text{ nF}$ |
| Turn-On / Turn-Off Propagation Delay| $t_{on}, t_{off}$| — | 90 | 125 | ns | $C_L = 1000\text{ pF}$ |
| Delay Matching (Channel-to-Channel) | $t_{DM}$ | — | 5 | 15 | ns | High/Low channels |
| Output Rise Time | $t_r$ | — | 16 | 30 | ns | $C_L = 1000\text{ pF}$ |
| Output Fall Time | $t_f$ | — | 12 | 25 | ns | $C_L = 1000\text{ pF}$ |
| UVLO Rising Threshold | $V_{DDR}$ | 8.2 | 8.8 | 9.4 | V | $V_{DD}$ rising |

## Common mistakes

- **Leaving the EN pin unconnected:** The `EN` pin has an internal pull-down. If left floating, the driver will remain permanently disabled. Pull `EN` to $3.3\text{V}$, $5\text{V}$, or $V_{DD}$ to enable operation.
- **Forgetting microcontroller deadband:** Like the IR2110, the UCC27714 provides completely independent control of high and low sides for advanced resonant converter topologies. Ensure deadtime (typically $100\text{ ns} \dots 300\text{ ns}$) is configured in the MCU PWM peripheral.
- **Inadequate decoupling on VDD pins:** Connect Pins 7 and 14 to $V_{DD}$ and place a $2.2\ \mu\text{F} \dots 4.7\ \mu\text{F}$ low-ESR ceramic capacitor directly adjacent to Pin 7 and Pin 5 (`COM`).

## Notes

- **High-Current Advantage over IR2110:** With double the drive current ($4.0\text{A}$ vs $2.0\text{A}$) and a significantly faster propagation delay ($90\text{ ns}$ vs $120\text{ ns}$), the UCC27714 drives modern large SuperJunction and SiC MOSFETs with minimal gate switching losses.
