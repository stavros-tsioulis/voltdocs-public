## Overview

The **LT3476** is a high-current, quad-output constant-current DC/DC converter IC manufactured by Analog Devices (originally Linear Technology). Designed specifically to drive high-brightness LEDs, the LT3476 integrates four fully independent driver channels, each equipped with an internal **$1.5\text{ A}$, $36\text{ V}$** bipolar NPN power switch.

Capable of operating in **Buck, Boost, or Buck-Boost** topologies thanks to high-side current sensing, the LT3476 provides up to **$1000:1$ True Color PWM™ dimming** independently across all four channels, preventing color shift across wide dynamic brightness ranges. With programmable switching frequencies from $200\text{ kHz}$ to $2\text{ MHz}$ and peak efficiencies up to $96\%$, it is the premier solution for RGBW architectural lighting, automotive LED headlights, avionics heads-up displays, and high-power TFT-LCD backlighting.

## Quick reference

| | |
|---|---|
| **Function** | High-Current Quad Output Constant-Current LED Driver |
| **Input Supply Voltage ($V_{IN}$)** | $2.8\text{ V}$ to $16.0\text{ V}$ DC |
| **Channels** | 4 independent constant-current DC/DC channels |
| **Internal Power Switches** | 4x $1.5\text{ A}$, $36\text{ V}$ NPN switches |
| **Switching Frequency ($f_{SW}$)** | $200\text{ kHz}$ to $2.0\text{ MHz}$ (set by single $R_T$ resistor) |
| **Dimming Capability** | True Color PWM™ dimming up to $1000:1$ (independent per channel) |
| **Current Sense Threshold** | $100\text{ mV}$ high-side current sense voltage ($200\text{ mV}$ max) |
| **Peak Efficiency** | Up to $96\%$ |
| **Operating Temperature Range** | $-40^\circ\text{C}$ to $+125^\circ\text{C}$ |
| **Package** | 38-lead $5\text{ mm} \times 7\text{ mm}$ QFN (`UFD` package with exposed ground pad) |

## Pin configuration

### 38-Lead QFN Pin Highlights

| Pin(s) | Name | Type | Description |
|---|---|---|---|
| 1, 10, 20, 29 | `SW1`–`SW4` | Power Switch | Switch node outputs for internal $1.5\text{ A}$ NPN switches (channels 1 to 4) |
| 4, 7, 23, 26 | `PWM1`–`PWM4` | Digital Input | Independent PWM dimming control inputs ($>1.4\text{V}$ = ON, $<0.4\text{V}$ = OFF) |
| 2, 9, 21, 28 | `CAP1`–`CAP4` | Current Sense | High-side sense input (connects to sense resistor on anode side of LED string) |
| 3, 8, 22, 27 | `LED1`–`LED4` | Current Sense | Negative side of current sense resistor / LED string connection |
| 5, 6, 24, 25 | `VREF1`–`VREF4`| Analog Input | Analog dimming reference inputs (connect to $V_{REF}$ or DAC/potentiometer) |
| 13, 14, 15, 16 | `VIN` | Power Input | Input power supply ($+2.8\text{ V}$ to $+16.0\text{ V}$ DC) |
| 33 | `RT` | Timing Input | Frequency setting resistor pin to GND ($200\text{ kHz} \dots 2\text{ MHz}$) |
| 34 | `SHDN` | Digital Input | Master shutdown control pin (pull below $0.3\text{ V}$ for $<10\text{ }\mu\text{A}$ standby) |
| 35 | `VREF` | Power Output | Internal $1.25\text{ V}$ precision bandgap reference voltage output |
| Exposed Pad | `GND` | Thermal Ground | Ground and thermal dissipation pad (must be soldered to PCB ground plane) |

## Functional description

- **High-Side Current Sensing:** Each channel measures LED current across an external sense resistor ($R_{SENSE}$) in the high-side positive LED supply rail ($100\text{ mV}$ nominal threshold). Because sensing is referenced to the high side, the negative cathode of the LED string can return to Ground, enabling true Buck, Boost, or SEPIC configurations.
- **True Color PWM™ Dimming:** A logic HIGH on any `PWM` pin connects the internal error amplifier and activates the power switch, while a logic LOW disables switching and locks the feedback capacitor voltage (`VC`). This allows instant resume without recharge delays, preserving the LED's spectral emission across dimming ratios up to $1000:1$.
- **Analog Dimming:** Applying a DC voltage ($0.1\text{ V}$ to $1.25\text{ V}$) to the `VREF` pins allows linear analog adjustment of the LED current setpoint in conjunction with, or independently of, digital PWM dimming.

## Absolute maximum ratings

> [!WARNING]
> Stresses beyond these ratings cause permanent damage. Exposure to absolute maximum conditions affects device reliability.

| Parameter | Rating | Unit |
|---|---|---|
| Switch Voltage (`SW1`–`SW4`) | 36.0 | V |
| Input Supply Voltage (`VIN`) | 16.0 | V |
| Sense Inputs (`CAP1`–`CAP4`, `LED1`–`LED4`) | 40.0 | V |
| Differential Sense Voltage (`CAP` - `LED`) | $\pm 1.0$ | V |
| PWM and Control Inputs (`PWM`, `SHDN`) | 16.0 | V |
| Operating Junction Temperature Range | -40 to 125 | °C |
| Storage Temperature Range | -65 to 125 | °C |

## Electrical characteristics

$V_{IN} = 3.3\text{ V}$, $T_A = 25^\circ\text{C}$, unless otherwise noted.

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Supply Voltage | $V_{IN}$ | 2.8 | — | 16.0 | V | DC |
| Quiescent Current (Active) | $I_{IN}$ | — | 32 | 45 | mA | All 4 channels switching |
| Shutdown Quiescent Current | $I_{SHDN}$ | — | 0.1 | 10 | $\mu\text{A}$ | $V_{SHDN} = 0\text{ V}$ |
| Switch Current Limit | $I_{LIM}$ | 1.5 | 1.8 | 2.3 | A | Per switch |
| Switch Saturation Voltage | $V_{CE(sat)}$ | — | 350 | 450 | mV | $I_{SW} = 1.0\text{ A}$ |
| Current Sense Threshold | $V_{(CAP-LED)}$ | 90 | 100 | 110 | mV | Full temperature range |
| Internal Reference Voltage | $V_{REF}$ | 1.21 | 1.25 | 1.28 | V | $I_{LOAD} = 100\text{ }\mu\text{A}$ |
| Switching Frequency | $f_{SW}$ | 0.9 | 1.0 | 1.1 | MHz | $R_T = 24.9\text{ k}\Omega$ |
| PWM Input Threshold High | $V_{PWM(H)}$ | 1.4 | — | — | V | Channel active |
| PWM Input Threshold Low | $V_{PWM(L)}$ | — | — | 0.4 | V | Channel disabled |

## Typical application

### 4-Channel High-Power RGBW LED Driver (Step-Up Boost Configuration)

```
                       +12V DC Supply Input
                                │
               ┌────────────────┴────────────────┐
               │                                 │
           [Inductors L1-L4]                 [LT3476 VIN]
               │                                 │
        ┌──────┴──────┐                   ┌──────┴──────┐
        │ SW1-SW4     │                   │ CAP1-CAP4   ├───[Rsense = 0.14Ω]──┐
        │             │                   │             │                     │
        │   LT3476    ├──► [Schottky] ────┼─────────────┼─────────────────────┤
        │             │                   │ LED1-LED4   ├──► [Anode]          │
        │             │                   └─────────────┘       High-Power    │
        │ PWM1-PWM4   │                                         LED String    │
        └──────┬──────┘                                         (Up to 32V)   │
               │                                                [Cathode]     │
       MCU PWM Control                                              │         │
       (Red, Green, Blue, White)                                   GND ───────┘
```

Current is programmed via $R_{SENSE}$:
$$I_{LED} = \frac{100\text{ mV}}{R_{SENSE}} = \frac{0.100\text{ V}}{0.14\text{ }\Omega} \approx 700\text{ mA per channel}$$

## Common mistakes

- **Exceeding $16\text{ V}$ on $V_{IN}$:** The internal control circuitry and bias supply $V_{IN}$ has an absolute maximum rating of $16\text{ V}$. However, the switch pins (`SW1`–`SW4`) and sense pins (`CAP1`–`CAP4`) are rated up to $36\text{ V}$ and $40\text{ V}$ respectively. In $24\text{ V}$ or automotive systems, power $V_{IN}$ through a local step-down regulator (or $5\text{ V}$ rail) while driving the LED power switches from the high-voltage bus.
- **Inadequate Heatsinking on the Exposed Ground Pad:** With four switches operating simultaneously at up to $1.5\text{ A}$ each, internal power dissipation can reach $2\text{ W} \dots 3\text{ W}$. The 38-lead QFN's bottom metal pad **must** be soldered solidly to a top PCB ground plane with an array of at least 9 to 16 thermal vias connecting to internal and bottom ground copper pours.
- **Floating the Shutdown (`SHDN`) Pin:** The `SHDN` pin must be pulled above $1.4\text{ V}$ (or tied directly to $V_{IN}$) to enable the IC. Leaving it floating causes erratic turn-on behavior.

## Notes

- **Dimming Architecture:** Unlike analog dimming which alters the forward voltage and changes the LED's emission spectrum, True Color PWM preserves exact chromaticity by pulsing the LED at its rated peak current.
- **Evaluation Hardware:** Linear Technology / Analog Devices demonstration circuit **DC976A** provides a reference layout for a 4-channel 1A step-up LED driver using the LT3476.
