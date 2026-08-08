## Overview

The **NE555** is the single most iconic hobbyist IC: a precision timer that makes **one-shot delays** (monostable) or **free-running oscillators / PWM** (astable) with a handful of resistors and a capacitor. Internally it compares the capacitor voltage against thresholds at roughly **⅓ VCC** (trigger) and **⅔ VCC** (threshold), then drives a flip-flop that controls the output and the discharge transistor.

Output can **sink or source up to 200 mA**, so it can drive LEDs, small buzzers, or logic inputs directly. Commercial clones and second sources (`LM555`, `SA555`, CMOS `TLC555` / `LMC555`) share the same pinout with different supply/current/temp trade-offs.

## Quick reference

| | |
|---|---|
| **Function** | Precision timer (monostable / astable) |
| **Supply range** | 4.5 V – 16 V (NE555; SE555 abs max 18 V) |
| **Logic family** | Bipolar 555 (TTL-compatible at 5 V) |
| **Packages** | PDIP-8, SOIC-8, TSSOP-8 |
| **Output drive** | ±200 mA |
| **Key thresholds** | Trigger ≈ ⅓ VCC, Threshold ≈ ⅔ VCC |

## Pin configuration

```
             ┌───┴───┐
       GND ─┤ 1   8 ├─ VCC
      TRIG ─┤ 2   7 ├─ DISCH
       OUT ─┤ 3   6 ├─ THRES
     RESET ─┤ 4   5 ├─ CONT
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` | Power | Ground |
| 2 | `TRIG` | Input | Trigger — low (< ⅓ VCC) starts the timing cycle / sets output high |
| 3 | `OUT` | Output | Totem-pole output, sink/source up to 200 mA |
| 4 | `RESET` | Input | Active-low reset; tie to `VCC` if unused |
| 5 | `CONT` | Analog | Control voltage — access to ⅔ VCC divider; often bypassed with 10 nF |
| 6 | `THRES` | Input | Threshold — high (> ⅔ VCC) ends the cycle / resets output low |
| 7 | `DISCH` | Open-collector | Discharge path to GND when output is low |
| 8 | `VCC` | Power | Supply 4.5 V – 16 V |

## Functional description

### Monostable (one-shot)

A falling edge on `TRIG` drives `OUT` high and releases `DISCH`. Capacitor `C` charges through `RA` until `THRES` reaches ⅔ VCC; then `OUT` goes low and `DISCH` dumps `C`.

\[
t_{HIGH} \approx 1.1 \cdot R_A \cdot C
\]

### Astable (oscillator)

`THRES` and `TRIG` are tied together. `C` charges through `RA + RB` and discharges through `RB` via `DISCH`.

\[
f \approx \frac{1.44}{(R_A + 2 R_B)\,C}
\quad,\quad
Duty \approx \frac{R_A + R_B}{R_A + 2 R_B}
\]

## Absolute maximum ratings

> [!WARNING] Stresses beyond these values cause permanent damage. These are limits, not operating conditions.

| Parameter | Rating | Unit |
|---|---|---|
| Supply voltage `VCC` | 18 | V |
| Input voltage (`CONT`, `RESET`, `THRES`, `TRIG`) | `VCC` | V |
| Output current | ±225 | mA |
| Operating junction temperature | 150 | °C |

## Electrical characteristics

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply voltage | `VCC` | 4.5 | — | 16 | V | NE555 recommended |
| Supply current | `ICC` | — | 3 | 6 | mA | `VCC` = 5 V, no load |
| Supply current | `ICC` | — | 10 | 15 | mA | `VCC` = 15 V, no load |
| Threshold voltage | `VTH` | — | ⅔ VCC | — | V | |
| Trigger voltage | `VTR` | — | ⅓ VCC | — | V | |
| Output sink capability | `IOL` | — | — | 200 | mA | |
| Reset voltage | `VRESET` | 0.3 | 0.7 | 1.0 | V | |

## Typical application

### Astable LED blinker (~1 Hz)

```
VCC (5–15 V)
  │
  ├──── RA (e.g. 10 kΩ) ────┬──── RB (e.g. 100 kΩ) ────┐
  │                         │                          │
  │                      DISCH(7)                   THRES(6)──TRIG(2)
  │                         │                          │
  │                         └────────── C (10 µF) ─────┴── GND
  │
  ├── VCC(8)   OUT(3) ──► LED + series resistor ── GND
  ├── RESET(4) ── VCC
  └── CONT(5) ── 10 nF ── GND
      GND(1) ── GND
```

## Package & footprint

- **PDIP-8 (`NE555P`):** breadboard / through-hole default.
- **SOIC-8 (`NE555D`):** SMT boards; same pin function order.
- Temperature grades: **NE555** 0 °C–70 °C, **SA555** −40 °C–85 °C, **SE555** −55 °C–125 °C.

## Common mistakes

- **Leaving `RESET` floating:** Noise resets the timer randomly — always tie pin 4 to `VCC` if unused.
- **No bypass on `CONT`:** A 10 nF capacitor from pin 5 to GND reduces supply-noise jitter on the thresholds.
- **Expecting rail-to-rail CMOS behavior from bipolar NE555:** At 5 V the bipolar output high is well below VCC; use a CMOS 555 (`LMC555` / `TLC555`) for true rail-to-rail and lower quiescent current.
- **Duty cycle stuck above 50% in simple astable:** With one discharge resistor (`RB` only path), duty cannot go below 50%. Add a diode across `RB` (or use a PWM topology) for asymmetric duty.

## Notes

- Dual version is the **NE556** (two timers in one 14-pin package).
- CMOS drop-ins (`TLC555`, `LMC555`) keep the pinout but run from ~2 V with µA-class supply current — preferred for battery projects.
