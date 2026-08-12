## Overview

The **74HC14** (SN74HC14) is a hex Schmitt-trigger inverter IC manufactured using high-speed silicon-gate CMOS technology. Containing six independent inverters in a 14-pin package, it performs the Boolean inverting function $Y = \overline{A}$.

Each input features built-in **Schmitt-trigger action**, providing input hysteresis ($\sim 0.7\text{V}$ typical at $5\text{V}$). This allows slow or noisy input signals (such as noisy sensor lines, switch contacts, or sine waves) to be transformed into sharp, clean, jitter-free digital logic signals without false triggering.

Operating from a wide supply voltage range of **2.0V to 6.0V DC**, the 74HC14 is widely used for debouncing mechanical switches, RC oscillators, wave shaping, and signal conditioning.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | 2.0 V to 6.0 V DC |
| **Logic Family** | High-Speed CMOS (74HC) / TTL Compatible (74HCT) |
| **Independent Channels** | 6 (Hex Schmitt-Trigger Inverter) |
| **Input Hysteresis ($\Delta V_T$)** | $0.7\text{ V}$ typical at $VCC = 4.5\text{V}$ |
| **Propagation Delay** | $12\text{ ns}$ typical at $VCC = 4.5\text{V}$ |
| **Output Drive Current** | $\pm 5.2\text{ mA}$ at $VCC = 4.5\text{V}$ |
| **Package** | 14-pin DIP / SOIC-14 / TSSOP-14 |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
          1A 1│ 1   14│ VCC
          1Y 2│       │13 6A
          2A 3│       │12 6Y
          2Y 4│ 74HC14│11 5A
          3A 5│       │10 5Y
          3Y 6│       │9  4A
         GND 7│       │8  4Y
             └───────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `1A` | Inverter 1 Input (Schmitt Trigger) |
| 2 | `1Y` | Inverter 1 Output ($1Y = \overline{1A}$) |
| 3 | `2A` | Inverter 2 Input (Schmitt Trigger) |
| 4 | `2Y` | Inverter 2 Output ($2Y = \overline{2A}$) |
| 5 | `3A` | Inverter 3 Input (Schmitt Trigger) |
| 6 | `3Y` | Inverter 3 Output ($3Y = \overline{3A}$) |
| 7 | `GND` | Ground reference (0 V) |
| 8 | `4Y` | Inverter 4 Output ($4Y = \overline{4A}$) |
| 9 | `4A` | Inverter 4 Input (Schmitt Trigger) |
| 10 | `5Y` | Inverter 5 Output ($5Y = \overline{5A}$) |
| 11 | `5A` | Inverter 5 Input (Schmitt Trigger) |
| 12 | `6Y` | Inverter 6 Output ($6Y = \overline{6A}$) |
| 13 | `6A` | Inverter 6 Input (Schmitt Trigger) |
| 14 | `VCC` | Power supply voltage (+2.0V to +6.0V DC) |

## Function & Truth Table (Per Gate)

| Input A | Output Y |
|---|---|
| Low ($L$) | High ($H$) |
| High ($H$) | Low ($L$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.0 | 5.0 | 6.0 | V | DC |
| Positive-Going Threshold | $V_{T+}$ | 2.0 | 2.5 | 3.15 | V | $V_{CC} = 4.5\text{V}$ |
| Negative-Going Threshold | $V_{T-}$ | 0.9 | 1.8 | 2.4 | V | $V_{CC} = 4.5\text{V}$ |
| Hysteresis Voltage | $\Delta V_T$ | 0.4 | 0.7 | 1.4 | V | $V_{CC} = 4.5\text{V}$ |
| Propagation Delay ($A \rightarrow Y$) | $t_{PD}$ | — | 12 | 21 | ns | $V_{CC} = 4.5\text{V}, C_L = 50\text{pF}$ |
| Output Drive Current | $I_{OUT}$ | — | — | $\pm 5.2$ | mA | $V_{CC} = 4.5\text{V}$ |
| Quiescent Supply Current | $I_{CC}$ | — | — | 2.0 | µA | $V_{IN} = V_{CC}\text{ or GND}$ |

## Typical Applications

### Simple RC Oscillator / Clock Generator

A single inverter channel configured with a feedback resistor $R$ and input capacitor $C$ forms a simple relaxation oscillator.

```
       ┌─────────── R (10k) ──────────┐
       │                              │
       │     ┌───┐                    │
  ─────┴────┤o   ├─── Output Clock ───┴─────
       │     └───┘
     ═══ C (10nF)
       │
      GND
```

## Common mistakes

- **Leaving inputs of unused inverters floating:** Unused CMOS inputs (e.g. pins 5, 9, 11, 13) must be connected to **$V_{CC}$ or GND**. Floating inputs drift into the linear threshold region, causing thermal drift, high power consumption, and oscillation noise.
- **Driving 74HC14 with 3.3V signals when powered from 5V:** When powered from $5\text{V}$, $V_{T+}$ can be up to $3.15\text{V}$. A 3.3V logic high signal may barely exceed $V_{T+}$. Use the **74HCT14** variant for 3.3V TTL-compatible input switching.

## Notes

- **74HC14 vs 74HC04:** 74HC04 contains standard hex inverters without Schmitt-trigger hysteresis; 74HC14 adds hysteresis on every input channel.
