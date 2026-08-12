## Overview

The **UC3843** (commonly **UC3843N**, **UC3843AN**, or **UC3843B** in an 8-pin DIP package) is a fixed-frequency current-mode PWM controller IC manufactured by Texas Instruments, ON Semiconductor, and STMicroelectronics. Optimized for low-voltage power supplies, automotive converters, and 12V DC-DC switch-mode power supplies (SMPS), it directly drives high-power N-channel MOSFET gates.

Unlike the high-voltage UC3842 (16V startup), the UC3843 features lower Undervoltage Lockout (UVLO) thresholds (**$8.4\text{ V}$ turn-on / $7.6\text{ V}$ turn-off**), allowing it to operate reliably from nominal $12\text{ V}$ power rails or battery supplies.

## Quick reference

| | |
|---|---|
| **Controller Type** | Low-Voltage Current-Mode PWM Controller |
| **Package** | 8-Pin DIP (Through-Hole) / SOIC-8 |
| **Supply Voltage Range ($V_{CC}$)** | $7.6\text{ V}$ to $30.0\text{ V}$ DC ($30\text{ V}$ max) |
| **UVLO Thresholds** | Turn-ON: $8.4\text{ V}$ / Turn-OFF: $7.6\text{ V}$ ($0.8\text{V}$ hysteresis) |
| **Peak Gate Output Current** | $\pm 1.0\text{ A}$ (Totem-Pole Driver for Power MOSFETs) |
| **Max Duty Cycle** | Up to $100\%$ |
| **Oscillator Frequency** | Programmable up to $500\text{ kHz}$ via external $R_T / C_T$ |
| **Internal Reference** | $+5.0\text{ V} \pm 1\%$ trimmed internal reference voltage (`VREF`) |

## Pinout (8-Pin DIP Package)

```
        ┌──────────┐
  COMP ─│ 1      8 │─ VREF
   VFB ─│ 2      7 │─ VCC
ISENSE ─│ 3      6 │─ OUTPUT
 RT/CT ─│ 4      5 │─ GND
        └──────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `COMP` | Error amplifier output pin (connect loop compensation network to VFB) |
| 2 | `VFB` | Voltage feedback sense input pin ($2.5\text{V}$ internal reference) |
| 3 | `ISENSE` | Current sense input pin (monitors primary MOSFET source resistor voltage drop) |
| 4 | `RT/CT` | Oscillator timing pin (resistor $R_T$ to VREF, capacitor $C_T$ to GND) |
| 5 | `GND` | Ground reference (0 V) |
| 6 | `OUTPUT` | High-current totem-pole gate output (drives external N-channel MOSFET gate) |
| 7 | `VCC` | Power supply voltage input (+7.6V to +30V DC) |
| 8 | `VREF` | $+5.0\text{V}$ precision reference voltage output |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Startup Voltage Threshold | $V_{TH(ON)}$ | 7.8 | 8.4 | 9.0 | V | $V_{CC}$ rising |
| Shutdown Voltage Threshold| $V_{TH(OFF)}$| 7.0 | 7.6 | 8.2 | V | $V_{CC}$ falling after startup |
| Feedback Reference Voltage | $V_{FB}$ | 2.45 | 2.50 | 2.55 | V | $T_J = 25^\circ\text{C}$ |
| Gate Peak Output Current | $I_{OUT\_PEAK}$ | $\pm 0.8$ | $\pm 1.0$ | — | A | Sourcing / Sinking peak |
| Current Sense Threshold | $V_{CS\_MAX}$ | 0.9 | 1.0 | 1.1 | V | Maximum current limit voltage |
| Operating Supply Current | $I_{CC}$ | — | 11 | 17 | mA | Normal switching state |

## Typical Application Circuit (12V DC-DC Converter Controller)

```
        +12V DC Input Rail
           │
        [10Ω Resistor]
           │
        [Pin 7: VCC]             UC3843 ───── [Pin 6: OUTPUT] ─── [10Ω] ──> Power MOSFET Gate
           │                        │
        [10µF Cap]         [Pin 3: ISENSE] ─── [MOSFET Source] ─── [0.22Ω Sense Resistor] ─── GND
           │                        │
          GND                      GND
```

$$ f_{OSC} = \frac{1.72}{R_T \times C_T} $$

## Common mistakes

- **Exceeding 30V on VCC:** While the UC3843 turns on at 8.4V, its absolute maximum supply voltage is $30.0\text{ V}$. Operating above 30V without a zener clamp will destroy the chip.
- **Omitting decoupling on VREF:** Pin 8 (`VREF`) supplies 5.0V to internal comparator blocks and external timing resistors. Always bypass Pin 8 to GND with a $100\text{ nF}$ ceramic capacitor.

## Notes

- **UC3843 vs UC3842:** UC3843 starts up at $8.4\text{ V}$ (ideal for 12V supplies and DC-DC converters), whereas UC3842 requires $16.0\text{ V}$ (designed for AC mains offline supplies).
