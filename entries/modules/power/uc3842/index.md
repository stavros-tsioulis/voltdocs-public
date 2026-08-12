## Overview

The **UC3842** (commonly **UC3842N** or **UC3842B** in an 8-pin DIP package) is the industry-standard fixed-frequency current-mode PWM controller IC, manufactured by Texas Instruments, STMicroelectronics, and ON Semiconductor. Designed for off-line AC-to-DC converters and high-voltage DC-DC flyback/forward power supplies, it directly drives high-voltage power MOSFETs.

Featuring high Undervoltage Lockout (UVLO) thresholds (**$16.0\text{ V}$ turn-on / $10.0\text{ V}$ turn-off**), the UC3842 can self-start directly from rectified AC mains via a high-value trickle-charge resistor, then run off an auxiliary transformer winding.

## Quick reference

| | |
|---|---|
| **Controller Type** | Fixed-Frequency Current-Mode PWM Controller |
| **Package** | 8-Pin DIP (Through-Hole) / SOIC-8 |
| **Supply Voltage Range ($V_{CC}$)** | $12.0\text{ V}$ to $30.0\text{ V}$ DC ($30\text{ V}$ max) |
| **UVLO Thresholds** | Turn-ON: $16.0\text{ V}$ / Turn-OFF: $10.0\text{ V}$ ($6\text{V}$ hysteresis) |
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
| 7 | `VCC` | Power supply voltage input (+12V to +30V DC) |
| 8 | `VREF` | $+5.0\text{V}$ precision reference voltage output |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Startup Voltage Threshold | $V_{TH(ON)}$ | 14.5 | 16.0 | 17.5 | V | $V_{CC}$ rising |
| Shutdown Voltage Threshold| $V_{TH(OFF)}$| 8.5 | 10.0 | 11.5 | V | $V_{CC}$ falling after startup |
| Feedback Reference Voltage | $V_{FB}$ | 2.45 | 2.50 | 2.55 | V | $T_J = 25^\circ\text{C}$ |
| Gate Peak Output Current | $I_{OUT\_PEAK}$ | $\pm 0.8$ | $\pm 1.0$ | — | A | Sourcing / Sinking peak |
| Current Sense Threshold | $V_{CS\_MAX}$ | 0.9 | 1.0 | 1.1 | V | Maximum current limit voltage |
| Startup Trickle Current | $I_{START}$ | — | 0.5 | 1.0 | mA | $V_{CC} = 14\text{V}$ (before startup) |
| Operating Supply Current | $I_{CC}$ | — | 11 | 17 | mA | Normal switching state |

## Typical Application Circuit (Flyback SMPS Controller)

```
        +300V DC Rectified Mains
           │
        [Primary Winding] ─── [MOSFET Drain]
           │                        │
       [100kΩ Startup]      [Pin 6: OUTPUT] ─── [10Ω] ──> MOSFET Gate
           │                        │
        [Pin 7: VCC]             UC3842
           │                        │
        [10µF Cap]         [Pin 3: ISENSE] ─── [MOSFET Source] ─── [0.47Ω Sense Resistor] ─── GND
           │                        │
          GND                      GND
```

$$ f_{OSC} = \frac{1.72}{R_T \times C_T} $$

## Common mistakes

- **Attempting to run off a 12V rail without reaching 16V startup:** The UC3842 requires $16.0\text{ V}$ minimum on $V_{CC}$ to turn ON initially. Connecting it to a fixed 12V supply means it will NEVER start up. Use the **UC3843** ($8.4\text{ V}$ turn-on threshold) for 12V systems instead!
- **Omitting RC filter on ISENSE pin:** Switching spikes on the MOSFET source resistor can prematurely trigger current limiting. Add a small RC filter ($1\text{ k}\Omega$ and $470\text{ pF}$) between the current sense resistor and Pin 3 (`ISENSE`).

## Notes

- **UC3842 vs UC3843 vs UC3844 vs UC3845:** UC3842 has 16V/10V UVLO (100% duty cycle); UC3843 has 8.4V/7.6V UVLO (100% duty cycle); UC3844/45 limit max duty cycle to 50%.
