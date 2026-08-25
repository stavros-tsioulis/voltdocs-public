## Overview

The **74HC132** (SN74HC132) is a high-speed silicon-gate CMOS integrated circuit containing four independent 2-input **NAND** gates with **Schmitt-trigger hysteresis** on every input. It shares the identical pinout and logic function ($Y = \overline{A \cdot B}$) of the standard 74HC00, but each input has separate positive-going ($V_{T+} \approx 2.7\text{ V}$ at $4.5\text{V}$) and negative-going ($V_{T-} \approx 1.8\text{ V}$) threshold trip points.

This internal hysteresis of typically **$0.7\text{ V} \dots 0.9\text{ V}$** eliminates jitter and spurious double-triggering caused by slow rise/fall times or noisy signal lines. Furthermore, because it is a 2-input gate, one input can serve as an active-high **enable/gating line**, allowing developers to create gated clock generators, tone burst generators, and pulse-width modulators with minimal component count.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | 2.0 V to 6.0 V DC (5.0 V nominal) |
| **Logic Family** | High-Speed CMOS (74HC) / TTL-Compatible (74HCT) |
| **Gate Count** | 4 Independent 2-Input Schmitt-Trigger NAND Gates |
| **Hysteresis Voltage ($V_H$)** | $0.4\text{ V}$ min ($0.7\text{ V} \dots 0.9\text{ V}$ typ) at $V_{CC} = 4.5\text{V}$ |
| **Propagation Delay ($t_{pd}$)** | $11\text{ ns}$ typ ($21\text{ ns}$ max) at $V_{CC} = 4.5\text{V}$ |
| **Output Drive Current** | $\pm 5.2\text{ mA}$ at $V_{CC} = 4.5\text{V}$ |
| **Package Options** | 14-pin DIP / SOIC-14 / TSSOP-14 |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
          1A 1│ 1   14│ VCC
          1B 2│       │13 4B
          1Y 3│       │12 4A
          2A 4│74HC132│11 4Y
          2B 5│       │10 3B
          2Y 6│       │9  3A
         GND 7│       │8  3Y
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1, 2 | `1A`, `1B` | Schmitt Input | Gate 1 Inputs with Hysteresis |
| 3 | `1Y` | Digital Output | Gate 1 NAND Output ($1Y = \overline{1A \cdot 1B}$) |
| 4, 5 | `2A`, `2B` | Schmitt Input | Gate 2 Inputs with Hysteresis |
| 6 | `2Y` | Digital Output | Gate 2 NAND Output ($2Y = \overline{2A \cdot 2B}$) |
| 7 | `GND` | Power | Ground reference (0 V) |
| 8 | `3Y` | Digital Output | Gate 3 NAND Output ($3Y = \overline{3A \cdot 3B}$) |
| 9, 10 | `3A`, `3B` | Schmitt Input | Gate 3 Inputs with Hysteresis |
| 11 | `4Y` | Digital Output | Gate 4 NAND Output ($4Y = \overline{4A \cdot 4B}$) |
| 12, 13 | `4A`, `4B` | Schmitt Input | Gate 4 Inputs with Hysteresis |
| 14 | `VCC` | Power | Supply voltage (+2.0 V to +6.0 V DC) |

## Function Table

| Input A | Input B | Output Y ($\overline{A \cdot B}$) |
|---|---|---|
| Low ($L < V_{T-}$) | Low ($L < V_{T-}$) | High ($H$) |
| Low ($L < V_{T-}$) | High ($H > V_{T+}$) | High ($H$) |
| High ($H > V_{T+}$) | Low ($L < V_{T-}$) | High ($H$) |
| High ($H > V_{T+}$) | High ($H > V_{T+}$) | Low ($L$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.0 | 5.0 | 6.0 | V | Operating DC range |
| Positive Threshold Voltage | $V_{T+}$ | 2.0 | 2.7 | 3.15 | V | $V_{CC} = 4.5\text{V}$ |
| Negative Threshold Voltage | $V_{T-}$ | 0.9 | 1.8 | 2.0 | V | $V_{CC} = 4.5\text{V}$ |
| Hysteresis Voltage | $V_H$ | 0.4 | 0.9 | 1.4 | V | $V_{T+} - V_{T-}, V_{CC} = 4.5\text{V}$ |
| Output Drive Current | $I_{OUT}$ | — | — | $\pm 5.2$ | mA | $V_{CC} = 4.5\text{V}$ |
| Propagation Delay | $t_{PLH}, t_{PHL}$ | — | 11 | 21 | ns | $V_{CC} = 4.5\text{V}, C_L = 50\text{ pF}$ |
| Quiescent Current | $I_{CC}$ | — | — | 2.0 | µA | $V_{IN} = V_{CC}\text{ or GND}$ |

## Typical Applications

### Gated RC Clock Generator (Buzzer / Tone Burst Generator)

When the Enable control is HIGH, the circuit oscillates continuously; when Enable is LOW, the oscillator is stopped and output is held HIGH:

```
 Enable (HIGH = Run) ───► [Pin 1: 1A]
                                 74HC132
                          [Pin 3: 1Y] ────┬──────────────► Gated Clock Output
                                 │        │
               ┌──────[ R = 10kΩ ]───────┘
               │
          [Pin 2: 1B]
               │
          [ C = 100nF ]
               │
              GND
```

## Common mistakes

- **Leaving unused gate inputs floating:** As with all CMOS ICs, floating inputs drift into high-frequency oscillation. Tie unused inputs to `VCC` or `GND`.
- **Assuming pinout difference from 74HC00:** The 74HC132 uses the exact same 14-pin pinout as the standard 74HC00. It is a direct drop-in upgrade for noisy NAND logic environments.

## Notes

- **74HC132 vs CD4093B:** 74HC132 operates up to 6V with fast $11\text{ ns}$ delay; CD4093B operates up to 18V with slower $\sim 100\text{ ns}$ delay.
