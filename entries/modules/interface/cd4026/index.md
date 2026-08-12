## Overview

The **CD4026** (commonly **CD4026BE** in a 16-pin DIP package) is a 5-stage Johnson decade counter IC with built-in 7-segment display output decoders, manufactured by Texas Instruments and ON Semiconductor. It converts clock pulses directly into active-HIGH signals to drive common-cathode 7-segment LED display digits without needing an intermediate BCD decoder IC (like the 74HC4511).

Operating across a supply voltage range of **$3.0\text{ V}$ to $18.0\text{ V}$**, the CD4026 features Carry-Out ($COUT$) for multi-digit cascading, Display Enable ($DE$) for power saving, and active-HIGH Reset for clearing the count.

## Quick reference

| | |
|---|---|
| **Counter Type** | 5-Stage Johnson Decade Counter with 7-Segment Decoder |
| **Package** | 16-Pin DIP (Through-Hole) / SOIC-16 / TSSOP-16 |
| **Supply Voltage Range ($V_{DD}$)** | $3.0\text{ V}$ to $18.0\text{ V}$ DC |
| **Display Support** | Common-Cathode LED 7-Segment Displays (Direct Drive) |
| **Max Clock Frequency** | $5.0\text{ MHz}$ typical at $V_{DD} = 10\text{V}$ |
| **Cascading Output** | Carry-Out ($COUT$) divides clock by 10 for multi-digit counters |
| **Control Functions** | Clock Enable (`CLK EN`), Display Enable (`DE`), Reset (`RESET`) |

## Pinout (16-Pin DIP Package)

```
        ┌──────────────┐
    CLK ─│ 1         16 │─ VDD
 CLK EN ─│ 2         15 │─ RESET
     DE ─│ 3         14 │─ UNGATED C
    DEO ─│ 4         13 │─ e
   COUT ─│ 5         12 │─ c
      f ─│ 6         11 │─ b
      g ─│ 7         10 │─ a
    VSS ─│ 8          9 │─ d
        └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `CLK` | Clock input pin (Increments counter on LOW-to-HIGH transition) |
| 2 | `CLK EN` | Clock Enable input pin (Active-LOW: GND = Enabled, VDD = Disabled) |
| 3 | `DE` | Display Enable input pin (Active-HIGH: VDD = Display ON, GND = Outputs OFF) |
| 4 | `DEO` | Display Enable Output (Used for blanking cascading display stages) |
| 5 | `COUT` | Carry-Out output pin (Pulses HIGH once every 10 clock cycles for next digit) |
| 6, 7, 9, 10, 11, 12, 13 | `a`–`g` | Decoded active-HIGH outputs driving segments a through g of LED display |
| 8 | `VSS` | Ground reference (0 V) |
| 14 | `UNGATED C` | Segment c output unaffected by `DE` display blanking |
| 15 | `RESET` | Asynchronous Reset input pin (Active-HIGH: VDD = Resets count to 0) |
| 16 | `VDD` | Positive power supply input (+3.0V to +18.0V DC) |

## Decoded Segment Display Output Mapping

```
     ── a ──
    │       │
    f       b
    │── g ──│
    e       c
    │       │
     ── d ──
```

| Count | Segments Active (Active-HIGH = 1) | Displayed Digit |
|---|---|---|
| 0 | a, b, c, d, e, f | `0` |
| 1 | b, c | `1` |
| 2 | a, b, d, e, g | `2` |
| 3 | a, b, c, d, g | `3` |
| 4 | b, c, f, g | `4` |
| 5 | a, c, d, f, g | `5` |
| 6 | a, c, d, e, f, g | `6` |
| 7 | a, b, c | `7` |
| 8 | a, b, c, d, e, f, g | `8` |
| 9 | a, b, c, d, f, g | `9` |

## Multi-Digit Cascade Wiring

```
   Clock Signal ───> [Digit 1: CD4026] ─── (COUT Pin 5) ───> [Digit 2: CD4026 (CLK Pin 1)]
                           │                                          │
                  [Segments a-g Out]                         [Segments a-g Out]
                           │                                          │
                 Common-Cathode Digit 1                    Common-Cathode Digit 2
```

## Common mistakes

- **Connecting to Common-Anode Displays:** CD4026 outputs are active-HIGH (source current). They work directly with **Common-Cathode** displays. They will NOT drive Common-Anode displays properly without inverters.
- **Floating CLK EN or RESET pins:** `CLK EN` is active-LOW (tie to GND for normal counting); `RESET` is active-HIGH (tie to GND for normal counting). Leaving either floating will prevent counting.

## Notes

- **CD4026 vs CD4033:** The CD4026 features Display Enable controls (`DE`/`DEO`), whereas the CD4033 features Ripple Blanking (`RBI`/`RBO`) for zero-suppression in multi-digit displays.
