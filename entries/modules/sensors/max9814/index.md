## Overview

The **MAX9814** is a low-cost, high-performance electret microphone amplifier IC manufactured by Maxim Integrated (Analog Devices). It features an integrated **Automatic Gain Control (AGC)** system that automatically adjusts signal amplification based on ambient sound levels.

When quiet whisper sounds occur, the AGC automatically boosts gain up to **60 dB**; when sudden loud noises or applause occur, the AGC dynamically reduces gain to prevent output clipping and distortion. It is widely used in sound-reactive LED strips (FastLED, WLED), voice recording, and noise detection systems.

## Quick reference

| | |
|---|---|
| **Operating Voltage (`VCC`)** | 2.7 V to 5.5 V DC |
| **Selectable Max Gain** | 40 dB, 50 dB, or 60 dB (configured via `GAIN` pin) |
| **Automatic Gain Control (AGC)** | Active compression & limiting to prevent audio clipping |
| **Microphone Bias Voltage** | Integrated low-noise $2.0\text{ V}$ bias output |
| **Output Voltage Bias** | DC-biased at $1.25\text{ V}$ ($2\text{ V}_{\text{p-p}}$ output swing) |
| **Attack / Release Ratio** | 1:500 (default), 1:2000, 1:4000 (configured via `A/R` pin) |
| **Operating Current** | 3.0 mA active, 20 µA shutdown |

## Pinout

```pinout
module
```


### Five-Pin Adafruit-Style Breakout

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `A/R` | Digital Input | Attack/release: GND `1:500`, VDD `1:2000`, floating `1:4000` |
| 2 | `GAIN` | Digital Input | VDD 40 dB, GND 50 dB, floating 60 dB |
| 3 | `OUT` | Analog Output | Audio output with approximately 1.25 V DC bias |
| 4 | `GND` | Power | Ground |
| 5 | `VDD` | Power Input | +2.7 V to +5.5 V |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 2.7 | 3.3 / 5.0 | 5.5 | V | DC |
| Supply Current | $I_{DD}$ | — | 3.0 | 4.0 | mA | Active mode |
| Shutdown Current | $I_{SHDN}$ | — | 20 | 35 | µA | `SHDN = LOW` |
| Maximum Gain (Unconnected) | $G_{max}$ | 59 | 60 | 61 | dB | $GAIN = Unconnected$ |
| Maximum Gain (`GND`) | $G_{50}$ | 49 | 50 | 51 | dB | $GAIN = GND$ |
| Maximum Gain (`VCC`) | $G_{40}$ | 39 | 40 | 41 | dB | $GAIN = VCC$ |
| Output Offset Voltage | $V_{OUT,DC}$ | 1.15 | 1.23 | 1.30 | V | DC bias voltage |
| Total Harmonic Distortion | $THD+N$ | — | 0.04 | — | % | $f = 1\text{ kHz}$ |

## Gain Configuration Options

| `GAIN` Pin Connection | Max Gain | Typical Application |
|---|---|---|
| **Unconnected (Floating)** | **60 dB** | Quiet rooms / Long-distance whisper pick-up |
| **Tied to `GND`** | **50 dB** | Normal speaking voice / General audio input |
| **Tied to `VCC`** | **40 dB** | Loud environments / Concerts / Loudspeakers |

## Wiring

| MAX9814 Breakout Pin | → | Microcontroller (Arduino / ESP32) | Notes |
|---|---|---|---|
| `VCC` | | `5V` (or `3.3V`) | Clean power source recommended |
| `GND` | | `GND` | Ground |
| `OUT` | | Analog Pin `A0` (or ESP32 ADC) | Analog signal centered at ~1.25V |
| `GAIN` | | `GND` / `VCC` / Unconnected | Selects 50dB / 40dB / 60dB gain |

## Common mistakes

- **Power supply noise bleeding into audio output:** Amplifying small microvolt signals by 60 dB makes the MAX9814 sensitive to power rail ripple. Add a $10\text{ }\mu\text{F}$ capacitor across `VCC` and `GND`.
- **Assuming 0V baseline output:** The `OUT` pin has an internal **1.25 V DC offset**. Subtract the 1.25 V DC offset (or ~400 ADC counts on a 10-bit 3.3V ADC) in software before calculating peak-to-peak sound amplitude.
- **Using 60 dB gain in loud environments:** Leaving the `GAIN` pin floating in loud rooms causes constant AGC compression, flattening audio dynamics.

## Notes

- Ideal for WLED / FastLED sound-reactive ambient lighting projects using peak-to-peak amplitude measurement ($V_{max} - V_{min}$).
