## Overview

The **BH1750FVI** is a digital ambient light sensor IC with an I2C bus interface. It converts light intensity directly into a 16-bit digital number corresponding to illuminance in **lux (lx)** without requiring complex mathematical calibration.

The sensor features a spectral response closely matching the human eye response (peak sensitivity at ~560 nm). It includes built-in signal conditioning, an ADC, and automatic rejection of 50 Hz / 60 Hz light flicker.

## Quick reference

| | |
|---|---|
| **Operating voltage** | 2.4 V – 3.6 V (5 V module breakouts include a regulator) |
| **Measurement range** | 1 lx – 65,535 lx |
| **Interface** | I2C (Standard & Fast mode, up to 400 kHz) |
| **I2C address** | `0x23` (ADDR pin LOW or floating) / `0x5C` (ADDR pin HIGH) |
| **Current draw** | 120 µA operating / 0.01 µA power-down |
| **Peak spectral response** | 560 nm (human eye visual curve) |

## Pinout

### Standard 5-Pin Breakout Module

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (3.3 V or 5 V for regulated breakouts) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SCL` | Digital Input | I2C Clock Line |
| 4 | `SDA` | Digital I/O | I2C Data Line |
| 5 | `ADDR` | Digital Input | I2C Address Select (`LOW`: 0x23, `HIGH`: 0x5C) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | `VCC` | 2.4 | 3.0 | 3.6 | V | IC rating |
| Power-down Current | `IPD` | — | 0.01 | 1.0 | µA | No illumination |
| Operating Current | `IIN` | — | 120 | 190 | µA | High-resolution mode |
| Measurement Time (H-Mode) | `tH` | — | 120 | 180 | ms | 1 lx resolution |
| Measurement Time (L-Mode) | `tL` | — | 16 | 24 | ms | 4 lx resolution |

## Communication & instructions

BH1750 is controlled by sending single opcode bytes over I2C.

| Opcode | Instruction Name | Description |
|---|---|---|
| `0x00` | Power Down | Power down IC, reducing current to < 1 µA. |
| `0x01` | Power On | Power up IC, waiting for measurement command. |
| `0x07` | Reset | Reset Data register value (only valid in Power On mode). |
| `0x10` | Continuously H-Resolution Mode | Start continuous measurement at 1 lx resolution (120 ms). |
| `0x11` | Continuously H-Resolution Mode 2 | Start continuous measurement at 0.5 lx resolution (120 ms). |
| `0x13` | Continuously L-Resolution Mode | Start continuous measurement at 4 lx resolution (16 ms). |
| `0x20` | One Time H-Resolution Mode | Perform one measurement at 1 lx, then automatically Power Down. |
| `0x21` | One Time H-Resolution Mode 2 | Perform one measurement at 0.5 lx, then automatically Power Down. |
| `0x23` | One Time L-Resolution Mode | Perform one measurement at 4 lx, then automatically Power Down. |

### Lux calculation formula

To calculate illuminance in lux from the 2-byte I2C read result:

$$\text{Illuminance (lx)} = \frac{\text{Raw Data (16-bit)}}{1.2}$$

## Wiring

| BH1750 Module | :i-lucide-move-right: | Microcontroller (Arduino / ESP32) |
|---|---|---|
| `VCC` | | 3.3 V (or 5 V if module has 662K regulator) |
| `GND` | | GND |
| `SCL` | | I2C SCL |
| `SDA` | | I2C SDA |
| `ADDR` | | GND (`0x23`) or VCC (`0x5C`) |

## Common mistakes

- **Reading data before measurement conversion finishes:** In High-Resolution mode, a measurement takes up to 180 ms. Requesting I2C data before this delay completes yields stale or zero values.
- **Floating ADDR pin:** Leaving `ADDR` disconnected may cause erratic switching between I2C address `0x23` and `0x5C`. Tie `ADDR` explicitly to GND or VCC.

## Notes

- **Measurement Time Register:** The default measurement time factor can be adjusted (via opcodes `0x40`–`0x7F`) to calibrate for optical window attenuation (e.g. dark glass covers).
