# WS2812B

> Individually addressable RGB LED with integrated control IC (popularized as "NeoPixel").

## Overview

The **WS2812B** is an intelligent control LED light source that integrates a control circuit and RGB chip into a single 5050 surface-mount package. Its internal structure includes an intelligent digital-port data latch and signal reshaping amplification drive circuit, as well as a precision internal oscillator and a 12V programmable constant-current output driver.

Data transfer uses a single-wire **Non-Return-to-Zero (NRZ)** communication mode. After power-on reset, the control IC receives data from the `DIN` port. The first pixel extracts the first 24-bit color data (8 bits each for Green, Red, and Blue) and passes the remaining data downstream through its `DOUT` pin after reshaping amplification.

## Quick reference

| | |
|---|---|
| **Supply voltage (`VDD`)** | 3.5 V – 5.3 V (Nominal 5.0 V) |
| **Logic input voltage** | -0.5 V to `VDD` + 0.5 V (0.7 · `VDD` for high) |
| **Color depth** | 24-bit (8 bits per channel: G, R, B) |
| **Current draw** | ~1 mA idle, ~50–60 mA at full white brightness |
| **Data rate** | 800 kbps (1.25 µs bit cycle) |
| **Package** | 5050 SMD (5.0 mm × 5.0 mm) |

## Terminals

### WS2812B 4-Pin 5050 Package

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VDD` | Power | Power supply voltage (5 V DC) |
| 2 | `DOUT` | Digital Output | Control data signal output (daisy-chain to next pixel `DIN`) |
| 3 | `VSS` | Power | Ground (0 V) |
| 4 | `DIN` | Digital Input | Control data signal input |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | `VDD` | 3.5 | 5.0 | 5.3 | V | |
| Input High Voltage | `VIH` | 0.7 · `VDD` | — | `VDD` + 0.5 | V | `DIN` pin |
| Input Low Voltage | `VIL` | -0.5 | — | 0.3 · `VDD` | V | `DIN` pin |
| Red Wavelength | `λd(R)` | 620 | 625 | 630 | nm | `IF` = 20 mA |
| Green Wavelength | `λd(G)` | 515 | 520 | 525 | nm | `IF` = 20 mA |
| Blue Wavelength | `λd(B)` | 465 | 470 | 475 | nm | `IF` = 20 mA |
| Luminous Intensity | `IV` | — | 1200 (R) / 2800 (G) / 900 (B) | — | mcd | `IF` = 20 mA |

## Communication protocol

- **Data order:** GRB (Green, Red, Blue), 8 bits MSB first per channel. Total 24 bits per LED.
- **Data transmission speed:** 800 kbps.

### Timing waveforms

| Signal | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| `T0H` | 0-code, high-level time | 220 | 400 | 380 (v5 max: 500) | ns |
| `T0L` | 0-code, low-level time | 580 | 850 | 1000 | ns |
| `T1H` | 1-code, high-level time | 580 | 800 | 1000 | ns |
| `T1L` | 1-code, low-level time | 220 | 450 | 1000 | ns |
| `RES` | Reset code (low level) | 50 (v5: >280) | — | — | µs |

## Wiring

| WS2812B Strip / Board | → | Power Supply / MCU |
|---|---|---|
| `VDD` (+5V) | | +5 V External Power Supply |
| `VSS` (GND) | | GND (Common Ground with MCU) |
| `DIN` | | GPIO Pin via **300 Ω – 500 Ω resistor** |

> [!WARNING] Always place a **1000 µF, 6.3V+ electrolytic capacitor** across the power supply (+5V and GND) near the LED strip to prevent inrush voltage spikes from damaging the first pixel's IC.

## Common mistakes

- **Missing Common Ground:** Operating the LED strip on an external 5V supply without connecting the power supply ground to the MCU ground causes corrupted signal timing and random flickering.
- **Driving 5V logic expectations from 3.3V MCUs:** WS2812B inputs specify `VIH` = 0.7 × `VDD` (3.5V when `VDD` = 5V). A 3.3V microcontroller output (ESP32, RP2040, STM32) may be marginally out of spec. Use a high-speed non-inverting level shifter (e.g. 74AHCT125) for long data lines.
- **Reversed DIN / DOUT direction:** Connecting the MCU signal to `DOUT` instead of `DIN` will not work. Data flows strictly in one direction from `DIN` to `DOUT`.

## Notes

- **WS2812B-V5:** Newer V5 revisions feature improved reverse power protection and require a longer reset pulse (> 280 µs vs 50 µs on earlier revs).
