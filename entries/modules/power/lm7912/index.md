## Overview

The **LM7912** (L7912CV / MC7912 / LM7912CT) is an industry-standard 3-terminal negative fixed linear voltage regulator manufactured by STMicroelectronics, onsemi, and Texas Instruments. Housed in a through-hole **TO-220AB** package, it delivers a regulated **$-12.0\text{V}$ DC** rail at up to **$1.5\text{A}$** from negative input voltages down to **$-35\text{V}$ DC**.

Paired with its positive counterpart the **LM7812**, the LM7912 is the universal companion regulator for creating clean, low-noise **split $\pm 12\text{V}$ dual-rail power supplies**. It is standard equipment in **Eurorack modular synthesizer power supplies, analog mixing consoles, audio operational amplifier stages (TL072/NE5532), instrumentation preamps, and bipolar DAC/ADC reference circuits**.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Standard Fixed Negative Linear Voltage Regulator |
| **Package** | TO-220AB (3-pin through-hole) / D2PAK |
| **Output Voltage ($V_{OUT}$)** | **$-12.0\text{ V}$ DC** ($\pm 4\%$) |
| **Input Voltage Range ($V_{IN}$)** | **$-14.5\text{ V}$ to $-35.0\text{ V}$ DC** |
| **Dropout Voltage ($V_{DROP}$)** | **$1.4\text{ V}$ typ** ($2.0\text{ V}$ max at $1.0\text{A}$) |
| **Maximum Output Current ($I_{OUT}$)** | **$1.5\text{ A}$** continuous (with adequate heatsink) |
| **Quiescent Current ($I_Q$)** | **$2.0\text{ mA} \dots 3.0\text{ mA}$** |
| **Ripple Rejection** | **$60\text{ dB}$** ($f = 120\text{ Hz}$) |
| **Positive Companion Regulator** | **LM7812** ($+12.0\text{V}$ Positive Regulator) |

## Pinout (TO-220AB Package - CRITICAL DIFFERENCE FROM 78xx)

Looking at the **front labeled face** with leads pointing downward:

```
        ┌──────────────┐
        │  O  [Metal]  │ ── Tab is internally connected to Pin 2 (-VIN)!
        ├──────────────┤
        │    LM7912    │
        └─┬────┬────┬──┘
          1    2    3
         GND  -VIN -VOUT
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` | Ground Reference | Common system ground ($0\text{ V}$) |
| 2 (Tab) | `INPUT (-VIN)` | Power Input | Negative unregulated DC input ($-14.5\text{V} \dots -35\text{V}$; **tied to metal tab!**) |
| 3 | `OUTPUT (-VOUT)`| Power Output | Regulated negative output voltage ($-12.0\text{V}$ DC) |

> [!WARNING]
> **Pinout and Tab Hazard:** 79xx series negative regulators do **NOT** share the pinout of 78xx positive regulators:
> - **78xx (Positive):** Pin 1 = `VIN`, Pin 2 = `GND` (Tab = GND), Pin 3 = `VOUT`
> - **79xx (Negative):** Pin 1 = `GND`, Pin 2 = `VIN` (**Tab = -VIN**), Pin 3 = `VOUT`
> Never mount a 7812 and 7912 to the same uninsulated heatsink, as this creates a dead short between system Ground and the negative input rail.

## Typical Dual-Rail Split Power Supply Circuit ($\pm 12\text{V}$)

```
  +18V DC Unregulated In ───► [Pin 1: VIN]
                                 LM7812     ───► [Pin 3: VOUT] ───► +12.0V DC (+1.5A)
                         ┌──► [Pin 2: GND]
  Center-Tap Ground (0V) ┤
                         └──► [Pin 1: GND]
                                 LM7912     ───► [Pin 3: -VOUT] ──► -12.0V DC (-1.5A)
  -18V DC Unregulated In ───► [Pin 2: -VIN]
```

## Recommended Bypass Capacitors

- **Input Capacitor ($C_{IN}$):** $2.2\ \mu\text{F}$ solid tantalum or electrolytic placed directly between Pin 2 ($-V_{IN}$) and Pin 1 (GND).
- **Output Capacitor ($C_{OUT}$):** $1.0\ \mu\text{F}$ solid tantalum or $10\ \mu\text{F}$ aluminum electrolytic between Pin 3 ($-V_{OUT}$) and Pin 1 (GND) is **mandatory** for loop stability.

## Common mistakes

- **Assuming Pin 2/Tab is Ground:** In 79xx regulators, the metal mounting tab is connected to Pin 2 ($-V_{IN}$). Bolting a 7912 directly to a grounded metal chassis will short the negative power supply rail. Always use a **silicone insulating pad and nylon shoulder washer**.
- **Reversing capacitor polarities:** On negative regulators, the positive terminal of electrolytic capacitors must connect to **GND (0V)**, and the negative capacitor terminal connects to the negative rails ($-V_{IN}$ and $-V_{OUT}$).

## Notes

- **Suffix Guide:** `L7912CV` denotes standard TO-220 commercial temperature ($0^\circ\text{C} \dots 125^\circ\text{C}$); `LM7912CT` denotes Texas Instruments TO-220.
