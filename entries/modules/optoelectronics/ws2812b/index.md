## Overview

The **WS2812B** is an intelligent control LED light source that integrates a control circuit and RGB chip into a single 5050 surface-mount package. Its internal structure includes an intelligent digital-port data latch and signal reshaping amplification drive circuit, as well as a precision internal oscillator and a 12V programmable constant-current output driver.

The current major hardware revision (**v5.0 / WS2812B-V5**) includes built-in reverse power protection, 12 mA channel drive current, and requires a **> 280 µs** reset pulse to latch frame data.

## Quick reference

| | |
|---|---|
| **Supply voltage (`VDD`)** | 3.7 V – 5.3 V (Nominal 5.0 V) |
| **Logic input voltage** | 0.7 · `VDD` (High) / 0.3 · `VDD` (Low) |
| **Color depth** | 24-bit (8 bits per channel: G, R, B) |
| **Reset pulse width (`RES`)** | **> 280 µs** (v5.0) / 50 µs (v1.0) |
| **Reverse power protection** | Integrated (v5.0) |
| **Package** | 5050 SMD (5.0 mm × 5.0 mm) |

## Terminals

### WS2812B 4-Pin 5050 Package

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VDD` | Power | Power supply voltage (3.7 V – 5.3 V DC) |
| 2 | `DOUT` | Digital Output | Control data signal output (daisy-chain to next pixel `DIN`) |
| 3 | `VSS` | Power | Ground (0 V) |
| 4 | `DIN` | Digital Input | Control data signal input |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | `VDD` | 3.7 | 5.0 | 5.3 | V | |
| Input High Voltage | `VIH` | 0.7 · `VDD` | — | `VDD` + 0.5 | V | `DIN` pin |
| Input Low Voltage | `VIL` | -0.5 | — | 0.3 · `VDD` | V | `DIN` pin |
| Channel Current | `IOUT` | 10.8 | 12.0 | 13.2 | mA | Per channel (v5.0) |
| Red Wavelength | `λd(R)` | 620 | 622.5 | 625 | nm | `IF` = 12 mA |
| Green Wavelength | `λd(G)` | 515 | 520 | 525 | nm | `IF` = 12 mA |
| Blue Wavelength | `λd(B)` | 465 | 467.5 | 470 | nm | `IF` = 12 mA |

## Communication protocol

- **Data order:** GRB (Green, Red, Blue), 8 bits MSB first per channel. Total 24 bits per LED.
- **Data transmission speed:** 800 kbps.

### Timing waveforms

| Signal | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| `T0H` | 0-code, high-level time | 220 | 250 | 380 | ns |
| `T0L` | 0-code, low-level time | 580 | 1000 | 1600 | ns |
| `T1H` | 1-code, high-level time | 580 | 900 | 1000 | ns |
| `T1L` | 1-code, low-level time | 220 | 550 | 1000 | ns |
| `RES` | Reset code (low level) | **280** | — | — | µs |

## Wiring

| WS2812B Strip / Board | → | Power Supply / MCU |
|---|---|---|
| `VDD` (+5V) | | +5 V External Power Supply |
| `VSS` (GND) | | GND (Common Ground with MCU) |
| `DIN` | | GPIO Pin via **300 Ω – 500 Ω resistor** |

## Common mistakes

- **50 µs vs 280 µs reset pulse:** Driving v5.0 LEDs with legacy 50 µs latch timings will cause data corruption or flickering. Ensure software output drivers emit a reset pulse of at least 280 µs.
- **Missing Common Ground:** Operating the LED strip on an external 5V supply without connecting the power supply ground to the MCU ground causes corrupted signal timing and random flickering.
- **Driving 5V logic expectations from 3.3V MCUs:** WS2812B inputs specify `VIH` = 0.7 × `VDD`. Use a high-speed non-inverting level shifter (e.g. 74AHCT125) for 3.3V MCUs.

## Revision history

- **v5.0 / WS2812B-V5 (Current):** Major hardware redesign — adds internal reverse power connection protection, lowers channel current to 12 mA for thermal efficiency, and increases recommended reset pulse to > 280 µs.
- **v2.0 – v4.0 (Datasheet PDF Revisions):** Incremental Worldsemi datasheet revisions (V2.0, V3.0, V4.0) updating test conditions, ESD ratings, and progressively updating reset pulse guidance from 50 µs to 280 µs ahead of the V5 hardware release.
- **v1.0 (Deprecated):** Original 4-pin WS2812B silicon release — 20 mA channel current, 50 µs reset pulse. See [revision 1.0](revisions/1.0/index.md).
