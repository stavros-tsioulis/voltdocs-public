## Overview

The **LM339** (LM339N) is a quad differential voltage comparator IC manufactured by Texas Instruments, STMicroelectronics, and ON Semiconductor. Containing four independent voltage comparators in a 14-pin package, it compares two analog input voltages and outputs a digital signal indicating which input is higher.

Designed to operate from a wide range of power supplies—from a single **2.0V to 36V DC** supply up to split **$\pm 1.0\text{V}$ to $\pm 18\text{V}$** rails—the LM339 features an input common-mode voltage range that includes Ground ($0\text{V}$). Each output is an **open-collector phototransistor-style stage**, allowing wired-OR connections and easy interfacing with 3.3V, 5V, or 12V logic levels using external pull-up resistors.

## Quick reference

| | |
|---|---|
| **Channels** | 4 (Quad Differential Voltage Comparator) |
| **Supply Voltage (Single Rail)** | $2.0\text{ V}$ to $36\text{ V}$ DC |
| **Supply Voltage (Split Rail)** | $\pm 1.0\text{ V}$ to $\pm 18\text{ V}$ DC |
| **Output Type** | Open-Collector (Requires external pull-up resistor to target logic voltage) |
| **Response Time** | $1.3\ \mu\text{s}$ (Large-signal response time) |
| **Input Offset Voltage** | $2.0\text{ mV}$ typical ($5.0\text{ mV}$ max) |
| **Input Bias Current** | $25\text{ nA}$ typical ($250\text{ nA}$ max) |
| **Quiescent Supply Current** | $0.8\text{ mA}$ total for all 4 comparators |
| **Package** | 14-pin DIP / SOIC-14 / TSSOP-14 |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
       OUT2 1│ 1   14│ OUT3
       OUT1 2│       │13 OUT4
        VCC 3│ LM339 │12 GND
      1IN-  4│       │11 4IN+
      1IN+  5│       │10 4IN-
      2IN-  6│       │9  3IN+
      2IN+  7│       │8  3IN-
             └───────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `OUT2` | Comparator 2 Output (Open-Collector) |
| 2 | `OUT1` | Comparator 1 Output (Open-Collector) |
| 3 | `VCC` | Positive Power Supply Input (+2V to +36V DC) |
| 4 | `1IN-` | Comparator 1 Inverting Input |
| 5 | `1IN+` | Comparator 1 Non-Inverting Input |
| 6 | `2IN-` | Comparator 2 Inverting Input |
| 7 | `2IN+` | Comparator 2 Non-Inverting Input |
| 8 | `3IN-` | Comparator 3 Inverting Input |
| 9 | `3IN+` | Comparator 3 Non-Inverting Input |
| 10 | `4IN-` | Comparator 4 Inverting Input |
| 11 | `4IN+` | Comparator 4 Non-Inverting Input |
| 12 | `GND` | Power Supply Ground (0 V) |
| 13 | `OUT4` | Comparator 4 Output (Open-Collector) |
| 14 | `OUT3` | Comparator 3 Output (Open-Collector) |

## Function & Output Truth Table (Per Comparator)

| Condition | Output Stage State | Output Voltage (With Pull-up to $V_{pull}$) |
|---|---|---|
| $V_{IN+} > V_{IN-}$ | Open (High-Z Off) | High ($V_{pull}$) |
| $V_{IN+} < V_{IN-}$ | Sinking to GND (ON) | Low ($0\text{V}$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Common-Mode Range | $V_{ICR}$ | 0 | — | $V_{CC}-1.5$| V | Includes GND ($0\text{V}$) |
| Input Offset Voltage | $V_{IO}$ | — | 2.0 | 5.0 | mV | $V_{CC} = 5\text{V}$ |
| Output Sink Current | $I_{SINK}$ | 6.0 | 16.0 | — | mA | $V_{OUT} \le 1.5\text{V}$ |
| Saturation Voltage | $V_{SAT}$ | — | 250 | 400 | mV | $I_{SINK} = 4\text{mA}$ |
| Low Power Quiescent Current| $I_{CC}$ | — | 0.8 | 2.0 | mA | All 4 channels |

## Typical Applications

### Window Detector / Voltage Limit Alarm

A dual-comparator window detector signals when an input voltage $V_{IN}$ falls outside a set range $[V_{REF\_LOW}, V_{REF\_HIGH}]$:

```
  V_REF_HIGH ────────► [4IN-] ──┐
                                ├─► [OUT4] ──┬── [Pullup 10k to 5V] ──► Alarm Out
  V_IN ──────────────► [4IN+] ──┘            │
                                             │
  V_IN ──────────────► [3IN-] ──┐            │
                                ├─► [OUT3] ──┘
  V_REF_LOW ─────────► [3IN+] ──┘
```

## Common mistakes

- **Forgetting external pull-up resistors:** Because LM339 outputs are **open-collector**, they cannot push current to a HIGH logic state on their own. Without an external pull-up resistor (e.g. $10\text{ k}\Omega$ to 3.3V, 5V, or 12V), the output will stay floating in High-Z state when $V_{IN+} > V_{IN-}$.
- **Oscillation near crossover without hysteresis:** Slow-moving analog input signals cause output chatter near the switching threshold due to noise. Add positive feedback ($100\text{ k}\Omega \dots 1\text{ M}\Omega$ hysteresis resistor) between output and non-inverting input.

## Notes

- **LM339 vs LM393 vs LM324:** LM339 is quad comparator with open-collector outputs; LM393 is dual comparator; LM324 is quad op-amp with push-pull outputs (op-amps are slower and lack open-collector flexibility).
