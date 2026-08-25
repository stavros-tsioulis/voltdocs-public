## Overview

The **LM7905** (L7905CV / MC7905 / LM7905CT) is an industry-standard 3-terminal negative fixed linear voltage regulator manufactured by STMicroelectronics, onsemi, and Texas Instruments. Available in a through-hole **TO-220AB** package, it delivers a regulated **$-5.0\text{V}$ DC** rail at up to **$1.5\text{A}$** from negative input voltages down to **$-25\text{V}$ DC** ($-35\text{V}$ absolute maximum).

Paired with the positive **LM7805**, the LM7905 is the universal regulator for generating **split $\pm 5\text{V}$ dual-rail supplies**. It is standard equipment in **high-speed operational amplifier circuits (such as video buffers and high-bandwidth preamps), ECL-to-TTL level translators, high-resolution ADC/DAC analog stages, and legacy multi-rail microprocessor architectures (e.g. Intel 8080, TMS9900)**.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Standard Fixed Negative Linear Voltage Regulator |
| **Package** | TO-220AB (3-pin through-hole) / D2PAK |
| **Output Voltage ($V_{OUT}$)** | **$-5.0\text{ V}$ DC** ($\pm 4\%$) |
| **Input Voltage Range ($V_{IN}$)** | **$-7.0\text{ V}$ to $-25.0\text{ V}$ DC** ($-35\text{ V}$ absolute max) |
| **Dropout Voltage ($V_{DROP}$)** | **$1.4\text{ V}$ typ** ($2.0\text{ V}$ max at $1.0\text{A}$) |
| **Maximum Output Current ($I_{OUT}$)** | **$1.5\text{ A}$** continuous (with heatsink) |
| **Quiescent Current ($I_Q$)** | **$2.0\text{ mA} \dots 3.0\text{ mA}$** |
| **Ripple Rejection** | **$60\text{ dB}$** ($f = 120\text{ Hz}$) |
| **Positive Companion Regulator** | **LM7805** ($+5.0\text{V}$ Positive Regulator) |

## Pinout (TO-220AB Package - CRITICAL DIFFERENCE FROM 78xx)

Looking at the **front labeled face** with leads pointing downward:

```
        ┌──────────────┐
        │  O  [Metal]  │ ── Tab is internally connected to Pin 2 (-VIN)!
        ├──────────────┤
        │    LM7905    │
        └─┬────┬────┬──┘
          1    2    3
         GND  -VIN -VOUT
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` | Ground Reference | Common system ground reference ($0\text{ V}$) |
| 2 (Tab) | `INPUT (-VIN)` | Power Input | Negative unregulated DC input ($-7.0\text{V} \dots -25\text{V}$; **tied to metal tab!**) |
| 3 | `OUTPUT (-VOUT)`| Power Output | Regulated negative output voltage ($-5.0\text{V}$ DC) |

> [!WARNING]
> **Pinout and Tab Hazard:** 79xx series negative regulators do **NOT** share the pinout of 78xx positive regulators:
> - **78xx (Positive):** Pin 1 = `VIN`, Pin 2 = `GND` (Tab = GND), Pin 3 = `VOUT`
> - **79xx (Negative):** Pin 1 = `GND`, Pin 2 = `VIN` (**Tab = -VIN**), Pin 3 = `VOUT`
> Never mount an LM7805 and LM7905 to the same uninsulated heatsink, as the mounting tabs will create a direct short between system Ground and the negative input rail.

## Typical Dual-Rail Split Power Supply Circuit ($\pm 5\text{V}$)

```
  +9V to +12V DC Unregulated In ──► [Pin 1: VIN]
                                       LM7805     ───► [Pin 3: VOUT] ───► +5.0V DC (+1.5A)
                               ┌──► [Pin 2: GND]
  Center-Tap Ground (0V) ──────┤
                               └──► [Pin 1: GND]
                                       LM7905     ───► [Pin 3: -VOUT] ──► -5.0V DC (-1.5A)
  -9V to -12V DC Unregulated In ──► [Pin 2: -VIN]
```

## Recommended Bypass Capacitors

- **Input Capacitor ($C_{IN}$):** $2.2\ \mu\text{F}$ solid tantalum or electrolytic connected directly between Pin 2 ($-V_{IN}$) and Pin 1 (GND).
- **Output Capacitor ($C_{OUT}$):** $1.0\ \mu\text{F}$ solid tantalum or $10\ \mu\text{F}$ aluminum electrolytic between Pin 3 ($-V_{OUT}$) and Pin 1 (GND) is **required** for control loop stability.

## Common mistakes

- **Assuming Pin 2/Tab is Ground:** In 79xx regulators, the metal mounting tab is connected to Pin 2 ($-V_{IN}$). Bolting an LM7905 directly to a grounded metal chassis will short the negative power supply rail. Always use a **silicone insulating pad and nylon shoulder washer**.
- **Reversing capacitor polarities:** On negative regulators, the positive terminal of electrolytic capacitors must connect to **GND (0V)**, and the negative capacitor terminal connects to the negative rails ($-V_{IN}$ and $-V_{OUT}$).

## Notes

- **Suffix Guide:** `L7905CV` denotes standard TO-220 commercial temperature ($0^\circ\text{C} \dots 125^\circ\text{C}$); `LM7905CT` denotes Texas Instruments TO-220.
