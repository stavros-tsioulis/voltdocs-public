## Overview

The **LT3743** is a fixed-frequency, synchronous step-down DC/DC LED driver controller designed by Linear Technology (now Analog Devices). Tailored specifically for high-power illumination, DLP projectors, architectural stage lighting, and laser diodes, it uses average current mode control to drive high-brightness LEDs at continuous currents up to **$20.0\text{ A}$** with conversion efficiencies reaching **$94\%$**.

Operating across a wide **$6.0\text{ V}$ to $36.0\text{ V}$ input supply**, the LT3743 features revolutionary 3-state current control and ultrafast PWM dimming (achieving up to **$3000:1$ true color PWM dimming ratios** without LED color shift). By driving external high-side and low-side N-channel power MOSFETs and an external PWM disconnect switch, the LT3743 can transition between different current levels in less than $2\ \mu\text{s}$.

## Quick reference

| | |
|---|---|
| **Driver Type** | Synchronous Step-Down DC/DC LED Driver Controller |
| **Package** | 28-lead QFN (4mm × 5mm) / 28-lead TSSOP Exposed Pad (FE-28) |
| **Input Supply Voltage Range ($V_{IN}$)**| $6.0\text{ V}$ to $36.0\text{ V}$ DC |
| **Maximum LED Current** | Up to $20.0\text{ A}$ continuous (set by external sense resistor) |
| **PWM Dimming Ratio** | Up to $3000:1$ at $100\text{ Hz}$ |
| **Switching Frequency Range** | $200\text{ kHz}$ to $1.0\text{ MHz}$ (programmable with resistor) |
| **Peak Conversion Efficiency** | Up to $94\%$ |
| **LED Current Accuracy** | $\pm 6\%$ typical over temperature |
| **Protection Features** | Open LED overvoltage clamping, Short-circuit protection, Thermal shutdown |

## Pinout (28-Lead TSSOP FE-28 Package)

```
            ┌──────────────┐
      EN/UVLO ─│ 1          28 │─ CTRL_SEL
      CTRL_H  ─│ 2          27 │─ CTRL_L
      VREF    ─│ 3          26 │─ PWM
      SS      ─│ 4          25 │─ PWMOUT
      RT      ─│ 5          24 │─ HG (High Gate)
      SYNC    ─│ 6    EP    23 │─ BST (Bootstrap)
      VCC     ─│ 7   (GND)  22 │─ SW (Switch Node)
      INTVCC  ─│ 8          21 │─ LG (Low Gate)
      VIN     ─│ 9          20 │─ PGND
      SENSEP  ─│ 10         19 │─ VOUT
      SENSEN  ─│ 11         18 │─ FB
      SGND    ─│ 12         17 │─ VFB
      COMP    ─│ 13         16 │─ CLKOUT
      STATUS  ─│ 14         15 │─ TSET
            └──────────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `EN/UVLO` | Input | Precision enable and programmable undervoltage lockout pin |
| 2 | `CTRL_H` | Input | High-level LED current analog control reference input |
| 3 | `VREF` | Output | 2.0V reference output for resistor divider networks |
| 5 | `RT` | Input | Timing resistor connection to set switching frequency ($200\text{ kHz} \dots 1\text{ MHz}$) |
| 7 | `VCC` | Power | Input supply voltage for internal control circuitry |
| 8 | `INTVCC` | Output | 5.2V internal LDO output powering the external MOSFET gate drivers |
| 9 | `VIN` | Power | Main high-voltage power input (6V to 36V) |
| 10 | `SENSEP` | Input | Positive input to the average current sense amplifier |
| 11 | `SENSEN` | Input | Negative input to the average current sense amplifier |
| 18 | `FB` | Input | Output voltage feedback divider pin for open-LED overvoltage protection |
| 21 | `LG` | Output | Low-side synchronous N-MOSFET gate drive output |
| 22 | `SW` | Power | Switching node connecting inductor, high-side source, and low-side drain |
| 23 | `BST` | Power | High-side gate driver bootstrap supply pin |
| 24 | `HG` | Output | High-side N-MOSFET gate drive output |
| 25 | `PWMOUT` | Output | Fast gate drive for external series LED PWM disconnect switch |
| 26 | `PWM` | Input | Logic PWM dimming input signal |
| 27 | `CTRL_L` | Input | Low-level LED current analog control reference input |
| 28 | `CTRL_SEL` | Input | Logic input to select between `CTRL_H` and `CTRL_L` analog setpoints |

## LED Current Programming Formula

The maximum regulated LED current ($I_{LED}$) is determined by the external current sense resistor ($R_{SENSE}$) connected across `SENSEP` and `SENSEN`:

$$ I_{LED} = \frac{50\text{ mV}}{R_{SENSE}} $$

For a $20\text{ A}$ LED driver, using a $2.5\text{ m}\Omega$ sense resistor yields:

$$ I_{LED} = \frac{0.050\text{ V}}{0.0025\ \Omega} = 20.0\text{ A} $$

Analog dimming can scale this threshold continuously between $0\text{ mV}$ and $50\text{ mV}$ via the `CTRL_H` / `CTRL_L` control pins.

## Typical Application Circuit Architecture

```
        +V_IN (6V - 36V)
           │
           ├───────────────────────────────┐
           │                               │
        [VIN / VCC]                     [Q_TOP High-Side N-MOS]
         LT3743                            │
        [Pin 24: HG]  ──────── Gate ───────┤
        [Pin 22: SW]  ──────── Source ─────┴──────┬─────[ Inductor L ]─────┬──[ R_SENSE ]──┬───[ Q_PWM Disconnect ]─── +LED (Up to 20A)
        [Pin 21: LG]  ──────── Gate ───────┐      │                        │               │
           │                               │      │                    [SENSEP]         [SENSEN]                      -LED
        [PGND / SGND]                   [Q_BOT Low-Side N-MOS]             │               │                            │
           │                               │      │                        └───────┬───────┘                           GND
          GND                             GND    GND                            LT3743
```

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Voltage Range | $V_{IN}$ | 6.0 | — | 36.0 | V | Operating range |
| INTVCC Regulated Output | $V_{INTVCC}$ | 4.95 | 5.2 | 5.45 | V | $V_{IN} \ge 7.0\text{V}$ |
| Full-Scale Current Sense Threshold | $V_{SENSE(MAX)}$| 47.0 | 50.0 | 53.0 | mV | $CTRL\_H = 2.0\text{V}$ |
| Switching Frequency | $f_{SW}$ | 200 | 500 | 1000 | kHz | Set by $R_T$ resistor |
| High-Side Gate Rise Time | $t_{r(HG)}$ | — | 20 | — | ns | $C_L = 3.3\text{ nF}$ |
| Low-Side Gate Rise Time | $t_{r(LG)}$ | — | 20 | — | ns | $C_L = 3.3\text{ nF}$ |
| PWMOUT Rise / Fall Time | $t_{r(PWM)}$ | — | 15 | — | ns | $C_L = 1.0\text{ nF}$ |
| Minimum PWM Pulse Width | $t_{PWM(MIN)}$| — | 300 | — | ns | Fast current recovery |

## Common mistakes

- **Omitting the external series PWM MOSFET:** To achieve the full $3000:1$ dimming ratio with microsecond response times, an external N-channel MOSFET must be placed in series with the LED cathode/anode driven by `PWMOUT`. Turning off the main inductor converter alone results in slow decay times limited by output capacitance.
- **Inadequate Kelvin sense connections on R_SENSE:** At $20\text{A}$, copper trace resistance between the sense resistor solder pads and the IC pins will inject milliohms of error into the $50\text{mV}$ full-scale threshold. Use a true 4-terminal Kelvin connection from `SENSEP` and `SENSEN` directly to the resistor pads.
- **Insufficient INTVCC capacitor:** Pin 8 (`INTVCC`) powers both gate drivers. High-gate-charge ($Q_g$) MOSFETs require a $4.7\ \mu\text{F} \dots 10\ \mu\text{F}$ low-ESR ceramic capacitor directly adjacent to the `INTVCC` and `PGND` pins.

## Notes

- **Three-State Color Mixing:** The dual analog inputs (`CTRL_H` and `CTRL_L`) combined with digital `CTRL_SEL` allow projecting systems to instantaneously switch LED drive current levels between white, red, green, and blue frames without loop settling lag.
