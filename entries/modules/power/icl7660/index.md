## Overview

The **ICL7660** (commonly **ICL7660CPA** in DIP-8 or **TC7660** by Microchip) is a classic CMOS switched-capacitor charge pump voltage converter manufactured by Renesas (originally Intersil). It performs negative voltage inversion, converting a positive input voltage ($+1.5\text{ V} \dots +10\text{ V}$) to a corresponding negative output voltage ($-1.5\text{ V} \dots -10\text{ V}$) using only two low-cost external capacitors.

Because it requires **no inductors or magnetic components**, the ICL7660 is widely used in analog audio gear, op-amp circuits, RS-232 level translators, and sensor interfaces to generate negative supply rails (such as $-5\text{ V}$ from a single $+5\text{ V}$ supply).

## Quick reference

| | |
|---|---|
| **Converter Type** | Switched-Capacitor Charge Pump Voltage Inverter |
| **Package** | 8-Pin DIP (Through-Hole) / SOIC-8 |
| **Input Voltage Range ($V^+$)** | $+1.5\text{ V}$ to $+10.0\text{ V}$ DC (ICL7660A version up to $+12\text{ V}$) |
| **Output Voltage Range ($V_{OUT}$)** | $-V_{IN}$ (Negative Voltage Inverter mode) |
| **Output Current Capability** | Up to $20\text{ mA}$ continuous |
| **Voltage Conversion Efficiency** | $99.9\%$ typical (Open circuit) |
| **Power Efficiency** | $98\%$ at $I_{OUT} = 2\text{mA}$ |
| **Oscillator Frequency** | $10\text{ kHz}$ internal switching clock ($100\text{ kHz}$ with `BOOST` pin) |

## Pinout (8-Pin DIP Package)

```
        ┌──────────┐
  NC/BO ─│ 1      8 │─ V+
   CAP+ ─│ 2      7 │─ OSC
    GND ─│ 3      6 │─ LV
   CAP- ─│ 4      5 │─ VOUT
        └──────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `BOOST` / `NC` | Oscillator frequency boost pin (Connect to $V^+$ to increase switching speed) |
| 2 | `CAP+` | Positive terminal for external charge pump capacitor $C_1$ |
| 3 | `GND` | Ground reference (0 V) |
| 4 | `CAP-` | Negative terminal for external charge pump capacitor $C_1$ |
| 5 | `VOUT` | Inverted negative output voltage pin ($-V_{IN}$) |
| 6 | `LV` | Low voltage operation pin (Connect to GND if $V^+ < 3.5\text{V}$; open for $V^+ \ge 3.5\text{V}$) |
| 7 | `OSC` | Internal oscillator control input (Connect external cap to GND to slow clock) |
| 8 | `V+` | Positive supply input (+1.5V to +10.0V DC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage Range | $V^+$ | 1.5 | 5.0 | 10.0 | V | DC operating input |
| Output Resistance | $R_{OUT}$ | — | 70 | 100 | $\Omega$ | $V^+ = 5\text{V}, I_{OUT} = 20\text{mA}$ |
| Oscillator Frequency | $f_{OSC}$ | 4.0 | 10.0 | 15.0 | kHz | $V^+ = 5\text{V}$, Pin 1 open |
| Voltage Conversion Efficiency| $E_V$ | 99.0 | 99.9 | — | % | Open circuit |
| Supply Current | $I_S$ | — | 80 | 170 | $\mu\text{A}$ | $V^+ = 5\text{V}$, $I_{OUT} = 0$ |

## Typical Application Circuit (Positive-to-Negative Voltage Inverter)

```
       +5V Power Input
          │
       [Pin 8: V+]
        ICL7660 ─── [Pin 2: CAP+] ─── [ 10µF Capacitor C1 ] ─── [Pin 4: CAP-]
          │
       [Pin 3: GND] ─── GND
          │
       [Pin 5: VOUT] ──┬─── -5V Inverted Output
                       │
                    [ 10µF Capacitor C2 ]
                       │
                      GND
```

## Common mistakes

- **Leaving the LV pin floating at low operating voltages:** When operating below $+3.5\text{ V}$ input, Pin 6 (`LV`) MUST be connected directly to `GND`. Leaving `LV` open at low supply voltages halts switching.
- **Exceeding the 10V input limit on standard ICL7660:** Standard ICL7660 absolute maximum rating is $+10.5\text{ V}$. Connecting $+12\text{ V}$ or higher destroys the internal MOS switches (use the `ICL7660A` or `MAX1044` for inputs up to $+12\text{ V}$).

## Notes

- **Op-Amp Dual Supply Generation:** The ICL7660 is the classic choice for deriving a $-5\text{ V}$ rail from a single $+5\text{ V}$ USB or 5V logic rail to power dual-rail analog op-amps like the TL072 or LM358.
