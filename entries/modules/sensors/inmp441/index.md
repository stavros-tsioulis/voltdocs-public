## Overview

The **INMP441** is a high-performance, low-power, digital-output omnidirectional MEMS microphone manufactured by InvenSense (a TDK Group Company). It combines a MEMS sensor element, signal conditioning, an analog-to-digital converter, and a 24-bit **I2S (Inter-IC Sound)** digital interface into a single compact package.

Because it outputs 24-bit digital audio directly over I2S (avoiding analog noise pick-up and ADC conversion losses), it is standard in ESP32 voice assistant projects (ESPHome, Alexa/Google Home DIY), smart speakers, noise monitors, and speech recognition applications.

## Quick reference

| | |
|---|---|
| **Operating Voltage (`VDD`)** | 1.8 V to 3.3 V DC (3.3 V nominal) |
| **Interface** | I2S Digital Bus (`SCK` / Bit Clock, `WS` / Word Select, `SD` / Data) |
| **Directional Pattern** | Omnidirectional |
| **Sensitivity** | -26 dBFS at 1 kHz, 94 dB SPL |
| **Signal-to-Noise Ratio (SNR)** | 61 dBA |
| **Frequency Response** | 60 Hz to 15,000 Hz |
| **Max Acoustic Input** | 120 dB SPL |
| **Channel Select (`L/R`)** | `LOW` = Left channel data, `HIGH` = Right channel data |
| **Operating Current** | 1.4 mA active, 17 µA sleep mode |

## Pinout

### Standard 6-Pin Breakout Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VDD` | Power | Supply voltage (+1.8 V to +3.6 V DC, 3.3V recommended) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SD` | Digital Output | I2S Serial Data output line |
| 4 | `L/R` | Digital Input | Left/Right Channel Select (`LOW` = Left channel, `HIGH` = Right channel) |
| 5 | `WS` | Digital Input | I2S Word Select / Frame Clock line (LRCK) |
| 6 | `SCK` | Digital Input | I2S Serial Bit Clock line (BCLK) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 1.8 | 3.3 | 3.6 | V | DC |
| Supply Current | $I_{DD}$ | — | 1.4 | 2.2 | mA | $V_{DD} = 3.3\text{ V}$, active mode |
| Standby Current | $I_{STBY}$ | — | 17 | 50 | µA | Clock stopped |
| Sensitivity | $S$ | -29 | -26 | -23 | dBFS | 1 kHz, 94 dB SPL |
| Signal-to-Noise Ratio | $SNR$ | — | 61 | — | dBA | 20 kHz bandwidth, A-weighted |
| Total Harmonic Distortion | $THD$ | — | 0.2 | 1.0 | % | 94 dB SPL, 1 kHz |
| Dynamic Range | $DR$ | — | 87 | — | dB | Max SPL to noise floor |

## I2S Timing & Channel Selection

The INMP441 streams 24-bit 2's-complement digital audio samples MSB-first:
- **`L/R` Pin tied to `GND`:** Microphone transmits 24-bit data during the **Left channel** period (`WS` = LOW). Data line `SD` goes high-impedance (tri-state) during the Right channel period (`WS` = HIGH).
- **`L/R` Pin tied to `VDD`:** Microphone transmits 24-bit data during the **Right channel** period (`WS` = HIGH).
- **Stereo Configuration:** Connect two INMP441 modules to the same I2S bus (`SCK`, `WS`, and `SD` shared). Set `L/R = GND` on Microphone 1 and `L/R = VDD` on Microphone 2.

## Wiring

| INMP441 Pin | → | ESP32 Board (Example I2S Pinout) | Notes |
|---|---|---|---|
| `VDD` | | `3.3V` | **Must be 3.3V supply** |
| `GND` | | `GND` | Ground |
| `L/R` | | `GND` | Selects Left Channel |
| `SD` | | GPIO35 (or I2S `DIN` pin) | Serial Data Out |
| `WS` | | GPIO25 (or I2S `LRCK` pin) | Word Select Clock |
| `SCK` | | GPIO32 (or I2S `BCLK` pin) | Bit Clock Input |

> [!WARNING]
> Power Supply Voltage Limit & Bottom Port Hole:
> - **3.3V Only:** Supplying 5V directly to `VDD` will destroy the INMP441 MEMS IC.
> - **Acoustic Port Obstruction:** The MEMS sound port hole is located on the **bottom of the PCB package**. Do NOT block or place tape over the small hole on the underside of the breakout board!

## Common mistakes

- **Powering with 5V:** Exceeding 3.6V damages the internal I2S ADC circuit.
- **Floating `L/R` pin:** Leaving `L/R` disconnected causes channel output ambiguity and silent audio buffers.
- **Using 8-bit or 10-bit ADC code:** The INMP441 outputs 24-bit I2S data. Microcontroller software must configure the I2S peripheral for **24-bit or 32-bit sample resolution** (with 24-bit data shifted into a 32-bit integer).

## Notes

- Ideal for ESP-ADF, ESPHome `i2s_audio` component, and speech-to-text engines (Kaldi, Whisper, Rhasspy).
