## Overview

The **LM3915** is a monolithic integrated circuit manufactured by Texas Instruments that senses analog audio signal levels and drives a 10-LED dot or bar graph display logarithmically. The internal divider is scaled to **3dB per step** across a total **30dB dynamic range**, matching human auditory perception of volume.

Widely used in audio equipment, mixing consoles, stereo amplifiers, and DIY VU meters, it accommodates signals from $10\text{ mV}$ up to $12\text{V}$ without external attenuators. Like the LM3914, it includes a 1.25V internal reference, programmable LED currents ($2\text{ mA} \dots 30\text{ mA}$), and a `MODE` pin to switch between Moving Dot and Bar Graph display modes.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`V+`)** | 3.0 V to 25.0 V DC |
| **Decoded LED Outputs** | 10 Regulated Current Sink Outputs (`LED1` to `LED10`) |
| **Logarithmic Step Scale** | $3\text{ dB}$ per step ($30\text{ dB}$ total dynamic range) |
| **Display Modes** | Bar Graph (Mode Pin tied to V+) / Moving Dot (Mode Pin floating) |
| **Internal Reference Voltage** | 1.25 V nominal |
| **Programmable LED Current** | 2 mA to 30 mA (set by resistor between Pin 7 & 8/GND) |
| **Package** | 18-pin DIP / PLCC-20 |

## Pinout (DIP-18 Package)

```
             ┌───┴───┐
        LED1 1│ 1   18│ LED2
          V- 2│       │17 LED3
          V+ 3│       │16 LED4
         RLO 4│ LM3915│15 LED5
         SIG 5│       │14 LED6
         RHI 6│       │13 LED7
     REF OUT 7│       │12 LED8
     REF ADJ 8│       │11 LED9
        MODE 9│       │10 LED10
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `LED1` | Output | Open-collector LED 1 driver output ($-27\text{dB}$ threshold) |
| 2 | `V-` | Power | Signal and power ground reference (0 V) |
| 3 | `V+` | Power | Positive supply power pin (+3.0V to +25.0V DC) |
| 4 | `RLO` | Input | Low-end of internal reference divider (Connect to GND) |
| 5 | `SIG` | Input | Analog audio signal input pin |
| 6 | `RHI` | Input | High-end of internal reference divider (Connect to REF OUT) |
| 7 | `REF OUT` | Output | Internal 1.25V reference output / LED current programming pin |
| 8 | `REF ADJ` | Output | Voltage reference adjust pin (Ground for 1.25V output) |
| 9 | `MODE` | Input | Display mode select pin (V+ = Bar Graph; Floating = Moving Dot) |
| 10–18 | `LED10`–`LED2`| Output | Open-collector LED driver outputs 10 down to 2 |

## Logarithmic Step Threshold Table (3dB / Step)

| LED Step | Relative Level (dB) | Threshold Voltage ($V_{REF}=1.25\text{V}$) |
|---|---|---|
| `LED1` | $-27\text{ dB}$ | $0.056\text{ V}$ |
| `LED2` | $-24\text{ dB}$ | $0.079\text{ V}$ |
| `LED3` | $-21\text{ dB}$ | $0.112\text{ V}$ |
| `LED4` | $-18\text{ dB}$ | $0.158\text{ V}$ |
| `LED5` | $-15\text{ dB}$ | $0.223\text{ V}$ |
| `LED6` | $-12\text{ dB}$ | $0.315\text{ V}$ |
| `LED7` | $-9\text{ dB}$ | $0.446\text{ V}$ |
| `LED8` | $-6\text{ dB}$ | $0.630\text{ V}$ |
| `LED9` | $-3\text{ dB}$ | $0.891\text{ V}$ |
| `LED10` | $0\text{ dB}$ (Full Scale) | $1.250\text{ V}$ |

## Basic Audio VU Meter Application Circuit

```
                      +9V to +12V Power
                             │
                     [Pin 3: V+] ────────── [Pin 9: MODE] (Tie to V+ for Bar Mode)
                      LM3915
                     [Pin 2: V-] ────────── GND
                             │
  AC Audio In ─[10µF]─►|─┬─► [Pin 5: SIG]
                    1N4148│
                         [100k]
                          │
                         GND
                             │
                     [Pin 6: RHI] ──┬────── [Pin 7: REF OUT]
                     [Pin 4: RLO] ──┴──┬─── [Pin 8: REF ADJ] ───[1.2kΩ Resistor]─── GND
                                       │
                                      GND
   LED Anodes (+VCC) ──► (10x LEDs) ──► [Pins 1, 18..10: LED1..LED10 Outputs]
```

## Common mistakes

- **Connecting AC audio directly to Pin 5 without rectification:** Negative swings of an un-rectified AC audio signal going below $-0.5\text{V}$ on Pin 5 will cause false triggering or damage internal comparators. Use a simple half-wave diode rectifier (1N4148 + 100k parallel resistor/capacitor smoothing filter) before Pin 5.
- **Excessive supply voltage in Bar Graph mode:** Operating at $12\text{V} \dots 15\text{V}$ in Bar Mode driving 10 LEDs at high current causes heavy IC heating. Power the LED anodes from a separate lower voltage source ($3.3\text{V} \dots 5\text{V}$).
- **Ground loops between audio signal ground and heavy power ground:** Connect the signal ground (`Pin 2`, `RLO`) directly to the audio input ground point to prevent ground hum from riding on the display.

## Notes

- **LM3915 vs LM3914 vs LM3916:** LM3915 has $3\text{dB}$ steps over $30\text{dB}$; LM3914 has linear steps; LM3916 has a standard VU scale ($-20\text{dB}$ to $+3\text{dB}$). Two LM3915s can be cascaded for a $60\text{dB}$ display range.
