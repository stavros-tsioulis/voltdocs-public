## Overview

The **CD4047** (CD4047B / CD4047BE) is a versatile CMOS low-power monostable (one-shot) and astable (free-running) multivibrator IC manufactured by Texas Instruments and onsemi. Available in a 14-pin through-hole **DIP-14** and surface-mount **SOIC-14** package, it requires only **one external resistor ($R$) and one external capacitor ($C$)** to set its timing period.

Operating across an ultra-wide voltage range of **$3.0\text{V}$ to $18.0\text{V}$ DC** with microamp quiescent power consumption, the CD4047 is distinguished by its built-in internal binary toggle flip-flop. In astable mode, this internal divider guarantees an **exact, mathematically perfect $50\%$ duty cycle** on its complementary outputs ($Q$ and $\bar{Q}$), while providing a doubled-frequency signal at $OSC_{OUT}$. Because of this feature, the CD4047 is one of the most famous and widely deployed ICs for driving **push-pull DC-to-AC power inverters (12V to 220V/110V 50Hz/60Hz inverters), ultrasonic transducers, and precision square-wave clock generators**.

## Quick reference

| | |
|---|---|
| **Device Type** | CMOS Monostable / Astable Multivibrator |
| **Operating Modes** | Astable (Free-Running), Monostable (Positive/Negative Edge, Retriggerable) |
| **Package** | 14-pin DIP (DIP-14 / PDIP-14) / 14-pin SOIC |
| **Supply Voltage Range ($V_{DD}$)** | $3.0\text{ V}$ to $18.0\text{ V}$ DC ($20\text{ V}$ absolute max) |
| **Duty Cycle Accuracy** | **Exact $50.0\%$ Duty Cycle** on $Q$ and $\bar{Q}$ outputs |
| **Outputs** | $Q$ (Pin 10), $\bar{Q}$ (Pin 11), $OSC_{OUT}$ (Pin 13, $2\times f_Q$) |
| **Astable Frequency Formula** | $f_Q = \frac{1}{4.4 \times R \times C}$, $f_{OSC} = \frac{1}{2.2 \times R \times C}$ |
| **Monostable Pulse Width** | $t_{pulse} = 2.48 \times R \times C$ |
| **Quiescent Current** | $0.02\ \mu\text{A}$ at $5\text{V}$ typ ($0.05\ \mu\text{A}$ at $10\text{V}$) |

## Pinout (DIP-14 Package)

```
                            ┌───┴───┐
                    C-EXT  1│ 1   14│ VDD (+3V to +18V)
                    R-EXT  2│       │13 OSC OUT (2x Frequency)
                RC-COMMON  3│ CD4047│12 RETRIGGER
                 /ASTABLE  4│   B   │11 /Q (Complementary Output)
                  ASTABLE  5│ DIP-14│10 Q  (True Output)
                 -TRIGGER  6│       │9  EXT RESET (Active-High)
                 VSS (0V)  7│       │8  +TRIGGER
                            └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `C-EXT` | Timing Input | Connect external timing capacitor $C$ between Pin 1 and Pin 3 |
| 2 | `R-EXT` | Timing Input | Connect external timing resistor $R$ between Pin 2 and Pin 3 |
| 3 | `RC-COMMON` | Timing Common | Common junction for external $R$ and $C$ components |
| 4 | `/ASTABLE` | Digital Input | Active-LOW Astable Enable (Connect to $V_{SS}$ / GND for astable mode) |
| 5 | `ASTABLE` | Digital Input | Active-HIGH Astable Enable (Connect to $V_{DD}$ for astable mode) |
| 6 | `-TRIGGER` | Digital Input | Negative-edge trigger input (Monostable mode; tie to $V_{DD}$ in astable) |
| 7 | `VSS` | Power | Common Ground reference ($0\text{ V}$) |
| 8 | `+TRIGGER` | Digital Input | Positive-edge trigger input (Monostable mode; tie to GND in astable) |
| 9 | `EXT RESET` | Digital Input | External Master Reset (Active HIGH; tie to GND for normal operation) |
| 10 | `Q` | Digital Output | Buffered true multivibrator output ($50\%$ duty cycle) |
| 11 | `/Q` | Digital Output | Buffered complementary inverted output ($50\%$ duty cycle) |
| 12 | `RETRIGGER` | Digital Input | Retrigger control input (Monostable mode; tie to GND in astable) |
| 13 | `OSC OUT` | Digital Output | Master oscillator output ($f = 2 \times f_Q$, non-50% duty cycle) |
| 14 | `VDD` | Power | Positive Supply Voltage ($+3.0\text{ V}$ to $+18.0\text{ V}$) |

## Typical Application Circuit: 50Hz / 60Hz Inverter Push-Pull Driver

```
                       +12V DC Supply
                             │
                      ┌──────┴──────────────────────────┐
                      │                                 │
                [Pin 14: VDD]                     [Pin 5: ASTABLE]
                      │                                 │
                [ 100nF Cap ]                     [Pin 6: -TRIGGER]
                      │                                 │
               [Pin 4: /ASTABLE] ──┐                    │
               [Pin 7: VSS] ───────┼────────────────────┤
               [Pin 8: +TRIGGER] ──┤                    │
               [Pin 9: RESET] ─────┼──────────┐         │
               [Pin 12: RETRIGGER] ┘          │         │
                                             GND       +12V
  Timing Network (50Hz on Q & /Q):
    Pin 1 (C-EXT) ────[ C = 100nF (0.1µF) Film ]────┐
                                                     ├──── Pin 3 (RC-COMMON)
    Pin 2 (R-EXT) ────[ R = 47kΩ Resistor ]──────────┘
    
  Complementary MOSFET Gate Drive:
    Pin 10 (Q)  ──────────────────► [Gate of Push-Pull MOSFET 1 (e.g. IRFZ44N)]
    Pin 11 (/Q) ──────────────────► [Gate of Push-Pull MOSFET 2 (e.g. IRFZ44N)]
```

## Calculating Astable Frequency

$$ f_Q = f_{\bar{Q}} = \frac{1}{4.4 \times R \times C} $$
$$ f_{OSC} = \frac{1}{2.2 \times R \times C} $$

- **For 50 Hz Output:** $C = 100\text{ nF} (0.1\ \mu\text{F})$, $R = \frac{1}{4.4 \times 50 \times 10^{-7}} \approx 45.4\text{ k}\Omega$ (use $39\text{k}\Omega$ in series with a $10\text{k}\Omega$ trim pot).
- **For 60 Hz Output:** $C = 100\text{ nF}$, $R \approx 37.8\text{ k}\Omega$ ($33\text{k}\Omega + 10\text{k}\Omega$ trimmer).

## Common mistakes

- **Leaving unused trigger / control inputs floating:** CMOS inputs must never float. In astable mode:
  - Connect Pins 4, 7, 8, 9, 12 to **GND ($V_{SS}$)**
  - Connect Pins 5, 6, 14 to **$+V_{DD}$**
- **Using low-quality electrolytic timing capacitors:** Electrolytic capacitors suffer from high leakage currents that disrupt the charge/discharge ramp across pins 1–3. Always use **polypropylene, Mylar film, or C0G ceramic capacitors** for timing component $C$.

## Notes

- **CD4047 vs NE555:** Unlike the 555 timer which requires external flip-flops or diode networks to produce a $50\%$ duty cycle, the CD4047 produces inherently perfect $50\%$ complementary outputs with a single RC network.
