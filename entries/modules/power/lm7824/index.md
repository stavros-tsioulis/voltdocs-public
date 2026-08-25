## Overview

The **LM7824** (and TO-220 packaged **L7824CV** / **LM7824CT**) is a 3-terminal fixed positive linear voltage regulator IC manufactured by STMicroelectronics, Texas Instruments, and ON Semiconductor. It supplies a regulated **$+24.0\text{V}$ DC power rail** from unregulated DC input voltages ranging from **$27.0\text{V}$ up to $40.0\text{V}$**.

As the highest fixed voltage member of the classic 78xx linear series, the LM7824 is frequently employed in industrial control panels, 24V relay driver boards, PLC interfaces, 24V DC solenoid drivers, and audio power amplifier stages. It features internal thermal overload shutdown, short-circuit current limiting, and safe-area protection.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Fixed Positive Linear Voltage Regulator |
| **Package** | TO-220 (L7824CV) / TO-263 / DPAK / TO-3 |
| **Pinout (TO-220 Front)** | Pin 1: Input (`IN`), Pin 2: Ground (`GND`), Pin 3: Output (`OUT`) |
| **Fixed Output Voltage** | $+24.0\text{ V}$ DC ($\pm 4\%$ tolerance across temperature) |
| **Input Voltage Range ($V_{IN}$)** | $27.0\text{ V}$ min to $40.0\text{ V}$ max |
| **Dropout Voltage** | $2.0\text{ V}$ typ (Requires $V_{IN} \ge 27.0\text{V}$ for full regulation) |
| **Continuous Output Current ($I_{OUT}$)** | $> 1.5\text{ A}$ (with adequate heatsink) |
| **Ripple Rejection Ratio** | $50\text{ dB} \dots 67\text{ dB}$ at $f = 120\text{ Hz}$ |

## Pinout (TO-220 Package)

Looking at the **front labeled face** of the TO-220 package with metal tab at top and leads pointing down:

```
        ┌──────────────┐
        │ [LM7824 Tab] │  (Metal Tab connected internally to Pin 2 GND)
        ├──────────────┤
        │    LM7824    │  (Front Face)
        └─┬────┬────┬──┘
          1    2    3
         IN   GND  OUT
```

| Pin | Name | Description |
|---|---|---|
| 1 | `IN` | Unregulated DC input voltage pin (+27.0V to +40.0V DC) |
| 2 | `GND` / `TAB` | Ground reference (0 V, connected internally to heatsink tab) |
| 3 | `OUT` | Fixed regulated +24.0V DC output pin |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Regulated Output Voltage | $V_{OUT}$ | 23.0 | 24.0 | 25.0 | V | $27.0\text{V} \le V_{IN} \le 38\text{V}, 5\text{mA} \le I_O \le 1.0\text{A}$ |
| Maximum Input Voltage | $V_{IN(max)}$ | — | — | 40.0 | V | Absolute Maximum Rating |
| Dropout Voltage | $V_d$ | — | 2.0 | 2.5 | V | $I_{OUT} = 1.0\text{A}, T_J = 25^\circ\text{C}$ |
| Peak Output Current | $I_{OS}$ | 1.5 | 2.2 | — | A | Short circuit peak current |
| Quiescent Current | $I_d$ | — | 4.6 | 8.0 | mA | $T_J = 25^\circ\text{C}$ |
| Quiescent Current Change | $\Delta I_d$ | — | — | 0.5 | mA | $5\text{mA} \le I_{OUT} \le 1.0\text{A}$ |
| Output Noise Voltage | $V_N$ | — | 170 | — | µV | $10\text{ Hz} \le f \le 100\text{ kHz}$ |

## Standard Circuit & Capacitors

```
       +V_IN Unregulated Input (27.0V - 40V DC)
          │
       [Pin 1: IN]
        LM7824
       [Pin 3: OUT] ──────────────┬─────────────── +24.0V Regulated DC Output
          │                       │
       [Pin 2: GND]          [ C2 = 0.1µF Ceramic ]
          │                       │
   [ C1 = 0.33µF Ceramic ]       GND
          │
         GND
```

- **Input Capacitor ($C_1 = 0.33\ \mu\text{F}$):** Required to stabilize the input and eliminate parasitic line inductances when positioned away from the filter capacitor.
- **Output Capacitor ($C_2 = 0.1\ \mu\text{F}$):** Ensures high-frequency stability and reduces transient dips during sudden load step changes.

## Common mistakes

- **Exceeding the 40V absolute maximum input voltage:** While standard LM78xx parts (5V–18V) are rated for 35V max, the LM7824 is rated for 40V. However, unregulated transformers can produce open-circuit DC voltages exceeding 40V during high AC line conditions, causing catastrophic dielectric breakdown.
- **Under-sizing heatsinks:** Because linear regulators dissipate $(V_{IN} - V_{OUT}) \times I_{LOAD}$, stepping down 36V to 24V at 1A produces $12\text{W}$ of heat. Without a generous heatsink ($\le 4^\circ\text{C/W}$), the IC will reach thermal shutdown ($\sim 150^\circ\text{C}$) rapidly.
- **Input voltage dip below 27V:** 24V output requires at least $27.0\text{V}$ input under all AC mains ripple conditions. If the input trough dips below $26.5\text{V}$, ripple will feed directly through to the output.

## Notes

- **Complementary Negative Rail:** The **LM7924** provides the $-24\text{V}$ companion rail for symmetrical $\pm 24\text{V}$ high-voltage audio or industrial driver circuits.
