## Overview

The **LM3914** is a monolithic integrated circuit manufactured by Texas Instruments that senses analog voltage levels and drives a **10-LED display**, providing a linear 10-step analog display. A single pin (`MODE`) changes the display from a solid moving **Bar Graph** to a single **Moving Dot** display.

The IC features an internal **1.25V precision voltage reference** and programmable LED current regulators ($2\text{ mA} \dots 30\text{ mA}$) that eliminate the need for external current-limiting resistors for all 10 LEDs. It operates across a wide supply voltage range of **3.0V to 25.0V DC** and can be cascaded to drive 20 to 100+ LED displays.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`V+`)** | 3.0 V to 25.0 V DC |
| **Decoded LED Outputs** | 10 Regulated Current Sink Outputs (`LED1` to `LED10`) |
| **Display Modes** | Bar Graph (Mode Pin tied to V+) / Moving Dot (Mode Pin floating) |
| **Internal Reference Voltage** | 1.25 V nominal (expandable up to 12V via divider) |
| **Programmable LED Current** | 2 mA to 30 mA (set by resistor between Pin 7 & 8/GND) |
| **Package** | 18-pin DIP / PLCC-20 |

## Pinout (DIP-18 Package)

```
             ┌───┴───┐
        LED1 1│ 1   18│ LED2
          V- 2│       │17 LED3
          V+ 3│       │16 LED4
         RLO 4│ LM3914│15 LED5
         SIG 5│       │14 LED6
         RHI 6│       │13 LED7
     REF OUT 7│       │12 LED8
     REF ADJ 8│       │11 LED9
        MODE 9│       │10 LED10
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `LED1` | Output | Open-collector LED 1 driver output (First threshold step) |
| 2 | `V-` | Power | Signal and power ground reference (0 V) |
| 3 | `V+` | Power | Positive supply power pin (+3.0V to +25.0V DC) |
| 4 | `RLO` | Input | Low-end of internal reference divider (Connect to GND or offset voltage) |
| 5 | `SIG` | Input | Analog voltage signal input pin (0V to V_RHI) |
| 6 | `RHI` | Input | High-end of internal reference divider (Connect to REF OUT for 1.25V full scale) |
| 7 | `REF OUT` | Output | Internal 1.25V reference output / LED current programming pin |
| 8 | `REF ADJ` | Output | Voltage reference adjust pin (Ground for 1.25V output) |
| 9 | `MODE` | Input | Display mode select pin (V+ = Bar Graph; Floating = Moving Dot) |
| 10–18 | `LED10`–`LED2`| Output | Open-collector LED driver outputs 10 down to 2 |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V^+$ | 3.0 | — | 25.0 | V | DC |
| Reference Voltage | $V_{REF}$ | 1.20 | 1.25 | 1.30 | V | Pin 7 to Pin 8 |
| LED Driver Current | $I_{LED}$ | 2.0 | 10.0 | 30.0 | mA | $R_{L(REF)} = 1.2\text{k}\Omega$ |
| Signal Input Range | $V_{IN}$ | $-0.5$ | — | $V^+-1.5$| V | Safe input range |
| Divider Step Linearity | — | — | 0.5 | 2.0 | % | Relative step error |
| Standby Supply Current | $I_S$ | — | 2.4 | 9.2 | mA | Dot mode, all LEDs off |

## Basic Application Circuit (0V to 1.25V 10-LED Voltmeter)

```
                       +5V to +12V Power
                               │
                       [Pin 3: V+] ────────── [Pin 9: MODE] (Tie to V+ for Bar Mode)
                        LM3914
                       [Pin 2: V-] ────────── GND
                               │
   Analog In (0..1.25V) ──► [Pin 5: SIG]
                               │
                       [Pin 6: RHI] ──┬────── [Pin 7: REF OUT]
                       [Pin 4: RLO] ──┴──┬─── [Pin 8: REF ADJ] ───[1.2kΩ Resistor]─── GND
                                         │
                                        GND
   LED Anodes (+VCC) ──► (10x LEDs) ───► [Pins 1, 18..10: LED1..LED10 Outputs]
```

$$\text{LED Current Formula:} \quad I_{LED} \approx \frac{12.5}{R_{L(REF)}} \quad \left(R_{L(REF)} = 1.2\text{ k}\Omega \Rightarrow I_{LED} \approx 10.4\text{ mA}\right)$$

## Common mistakes

- **Adding external current-limiting resistors to individual LEDs:** The LM3914 contains built-in internal constant-current regulators on all 10 LED outputs. Connecting external resistors is unnecessary and reduces LED brightness uniformity.
- **Power dissipation in Bar Graph mode at high supply voltages:** In Bar mode, when all 10 LEDs are lit at $20\text{mA}$ each ($200\text{mA}$ total), if $V_{LED}$ is $12\text{V}$ and LED forward drop is $2\text{V}$, the chip dissipates $(12\text{V} - 2\text{V}) \times 0.2\text{A} = 2.0\text{W}$, triggering thermal shutdown. Power LED anodes from a lower $+3.3\text{V} \dots +5\text{V}$ rail.
- **Floating `RLO` or `RHI` pins:** Leaving reference divider end-points floating causes erratic LED activation threshold levels.

## Notes

- **LM3914 vs LM3915 vs LM3916:** LM3914 is **linear** ($125\text{mV}$ per step); LM3915 is **logarithmic** ($3\text{dB}$ per step); LM3916 is a **VU meter** scale (logarithmic $-20\text{dB}$ to $+3\text{dB}$).
