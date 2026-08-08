## Overview

The **LM7812** (L7812CV / MC7812) is a 3-terminal fixed positive linear voltage regulator in the classic 78xx series manufactured by STMicroelectronics, Texas Instruments, and ON Semiconductor. Capable of supplying in excess of **1.5A output current** at a fixed **+12.0V DC**, it incorporates internal current limiting, thermal overload shutdown, and safe-area compensation.

Operating with input voltages between **14.5V and 35.0V DC**, it is widely used to provide clean, regulated +12V rails for operational amplifiers, audio preamps, 12V relays, cooling fans, and analog sensors from unregulated DC bench power supplies or AC transformer rectifiers.

## Quick reference

| | |
|---|---|
| **Output Voltage (`VOUT`)** | +12.0 V DC ($\pm 4\%$ tolerance) |
| **Minimum Input Voltage (`VIN_MIN`)**| 14.5 V DC ($VOUT + 2.5\text{V}$ dropout margin) |
| **Maximum Input Voltage (`VIN_MAX`)**| 35.0 V DC |
| **Maximum Output Current** | 1.5 A (with adequate heatsinking) |
| **Dropout Voltage** | 2.0 V typical at $I_{OUT} = 1.0\text{A}$ |
| **Quiescent Current** | 4.3 mA typical |
| **Package** | TO-220 / TO-263 (D2PAK) / DPAK / TO-3 |

## Pinout & Terminal Identification (TO-220 Package)

```
        ┌─────────┐
        │  O O O  │  Heatsink Tab (Connected to Pin 2 Ground)
        ├─────────┤
        │ LM7812  │
        └─┬──┬──┬─┘
          │  │  │
          1  2  3
         IN GND OUT
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `INPUT` | Power | Unregulated DC input voltage (+14.5V to +35.0V DC) |
| 2 | `GND` | Power | Ground reference (0 V, connected to metal heatsink tab) |
| 3 | `OUTPUT` | Power | Regulated +12.0V DC output rail |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Output Voltage | $V_{OUT}$ | 11.5 | 12.0 | 12.5 | V | $I_{OUT} = 500\text{mA}, V_{IN} = 19\text{V}$ |
| Line Regulation | $Reg_{line}$ | — | 10 | 120 | mV | $14.5\text{V} \le V_{IN} \le 30\text{V}, I_{OUT} = 500\text{mA}$ |
| Load Regulation | $Reg_{load}$ | — | 12 | 120 | mV | $5\text{mA} \le I_{OUT} \le 1.5\text{A}, V_{IN} = 19\text{V}$ |
| Quiescent Current | $I_d$ | — | 4.3 | 8.0 | mA | $I_{OUT} = 0, T_A = 25^\circ\text{C}$ |
| Output Noise Voltage | $V_N$ | — | 75 | — | µV | $10\text{Hz} \le f \le 100\text{kHz}$ |
| Peak Output Current | $I_{MAX}$ | 1.5 | 2.2 | — | A | $T_J = 25^\circ\text{C}$ |

## Basic Application Circuit

```
  Unregulated DC In ───┬───[Pin 1: IN]   [Pin 3: OUT]───┬─── Regulated +12V DC Out
  (+15V to +24V)       │        LM7812                  │
                    [C_IN 0.33µF] [Pin 2: GND]      [C_OUT 0.1µF]
                       │               │                │
  GND ─────────────────┴───────────────┴────────────────┴─── GND
```

- **Input Capacitor ($C_{IN} = 0.33\ \mu\text{F}$ ceramic):** Required if the regulator is located more than 2 inches ($5\text{ cm}$) from the power supply filter capacitor to prevent high-frequency oscillation.
- **Output Capacitor ($C_{OUT} = 0.1\ \mu\text{F}$ ceramic):** Improves transient response and stability against load current surges.

## Common mistakes

- **Input voltage below 14.5V:** The LM7812 requires a minimum dropout voltage of $2.0\text{V} \dots 2.5\text{V}$. Powering it from a $12\text{V}$ wall adapter or a $12\text{V}$ lead-acid battery results in dropout, causing output voltage to sag and pass input AC ripple straight through to the load.
- **Neglecting thermal dissipation at high input voltages:** Heat generated ($P_D$) equals $(V_{IN} - 12\text{V}) \times I_{OUT}$. For example, reducing $24\text{V}$ to $12\text{V}$ at $1.0\text{A}$ dissipates $12\text{W}$ of heat in the TO-220 package. Without an adequate heatsink, the IC will rapidly enter thermal shutdown.
- **Connecting the metal tab to Ground without electrical insulation when mounting to grounded metal chassis:** The TO-220 metal tab is internally connected to **Pin 2 (Ground)**. If mounting several different 78xx/79xx regulators to a shared metal heatsink, use mica or silicone insulating washers.

## Notes

- **LM7812 vs LM7805 vs LM7912:** LM7812 is a +12V positive regulator; LM7805 is a +5V positive regulator; LM7912 is a **-12V negative** linear voltage regulator.
