## Overview

The **NCL30100** (NCL30100SNT1G) is a 70V step-down (buck) constant-current LED driver IC manufactured by ON Semiconductor. Enclosed in a compact **TSOT-23 5-lead (SOT-23-5) package**, it is designed to drive strings of high-brightness LEDs directly from unregulated **6.0V to 70.0V DC** power supplies.

Operating on a peak current-mode control scheme with constant off-time, the NCL30100 requires minimal external components (an inductor, Schottky diode, sense resistor, and input capacitor) while delivering **up to 95% efficiency**. Its dedicated `PWM` input enables wide-range PWM dimming from low frequencies up to 5 kHz.

## Quick reference

| | |
|---|---|
| **Input Supply Voltage (`VIN`)** | 6.0 V to 70.0 V DC |
| **Maximum Switch Voltage** | $70.0\text{ V}$ DC |
| **Control Architecture** | Peak Current-Mode / Constant Off-Time |
| **Efficiency** | Up to $95\%$ typical |
| **Dimming** | Dedicated PWM Dimming Pin (`PWM`, up to 5 kHz) |
| **Package** | TSOT-23 5-lead (SOT-23-5) |

## Pinout (TSOT-23-5 Package)

```
             ┌───┴───┐
        SW  1│ 1   5 │ VIN (+6V to +70V)
       GND  2│       │
       PWM  3│NCL30100│4 CS (Current Sense Input)
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `SW` | Output | Internal MOSFET Switch Drain (Connect to Schottky Diode & Inductor) |
| 2 | `GND` | Power | Ground Reference (0 V) |
| 3 | `PWM` | Input | Logic PWM Dimming Input (High = Enable output switch; Low = Shutdown output) |
| 4 | `CS` | Input | High-Side Peak Current Sense Input |
| 5 | `VIN` | Power | Power Supply Input (+6.0V to +70.0V DC) |

## High Voltage Caution

> [!CAUTION]
> High Input Voltage Hazard!
> The NCL30100 operates at input voltages up to **$70.0\text{V}$ DC**. Ensure that external Schottky diodes, inductors, and filter capacitors are rated for $\ge 100\text{V}$ breakdown.

## Common mistakes

- **Leaving `PWM` (Pin 3) ungrounded or floating:** `PWM` is a logic input. Connect `PWM` directly to `VIN` (via pull-up resistor) or a 3.3V/5V microcontroller pin for continuous non-dimmed lighting.

## Notes

- **NCL30100 vs AL8807:** NCL30100 supports high input voltages up to 70V DC (vs 30V on AL8807).
