## Overview

The **ADS1115** is an ultra-small, low-power, 16-bit precision analog-to-digital converter (ADC) manufactured by Texas Instruments. It features 4 single-ended or 2 differential input channels, an onboard Programmable Gain Amplifier (PGA), a low-drift voltage reference, an internal oscillator, and a digital I2C interface.

It is widely used to add high-resolution analog measurement capabilities to microcontrollers that lack analog inputs (such as the Raspberry Pi) or require precision beyond standard 10-bit MCU ADCs.

## Quick reference

| | |
|---|---|
| **Supply voltage (`VDD`)** | 2.0 V to 5.5 V DC |
| **ADC resolution** | 16-bit (65,536 steps) / 15-bit single-ended |
| **Input channels** | 4 Single-Ended (`A0`–`A3`) or 2 Differential pairs |
| **Programmable gain (PGA)** | $\frac{2}{3}\times, 1\times, 2\times, 4\times, 8\times, 16\times$ (FSR $\pm 0.256\text{ V}$ to $\pm 6.144\text{ V}$) |
| **Programmable sample rate** | 8 SPS to 860 SPS |
| **Communication interface** | I2C (address selectable `0x48`–`0x4B`) |
| **Operating current** | 150 µA typical (continuous mode), 0.5 µA (power-down) |

## Pinout

### Standard ADS1115 Breakout Module Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VDD` | Power | Supply voltage (+2.0 V to +5.5 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SCL` | Digital Input | I2C Serial Clock line |
| 4 | `SDA` | Digital I/O | I2C Serial Data line |
| 5 | `ADDR` | Digital Input | I2C Slave Address select pin |
| 6 | `ALRT` / `RDY` | Digital Output | Active-LOW Comparator Alert or Conversion Ready output |
| 7 | `A0` | Analog Input | Analog input channel 0 |
| 8 | `A1` | Analog Input | Analog input channel 1 |
| 9 | `A2` | Analog Input | Analog input channel 2 |
| 10 | `A3` | Analog Input | Analog input channel 3 |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 2.0 | 3.3 | 5.5 | V | DC |
| Operating Current | $I_{DD}$ | — | 150 | 200 | µA | Continuous mode |
| Power-down Current | $I_{PD}$ | — | 0.5 | 2.0 | µA | Power-down mode |
| Full-Scale Range (PGA = 2/3) | $FSR$ | — | $\pm 6.144$ | — | V | $V_{IN}$ cannot exceed $V_{DD} + 0.3\text{ V}$ |
| Full-Scale Range (PGA = 1) | $FSR$ | — | $\pm 4.096$ | — | V | |
| Full-Scale Range (PGA = 2) | $FSR$ | — | $\pm 2.048$ | — | V | |
| Full-Scale Range (PGA = 16) | $FSR$ | — | $\pm 0.256$ | — | V | Max sensitivity: $7.8125\text{ }\mu\text{V/LSB}$ |
| Sample Rate | $f_{SPS}$ | 8 | — | 860 | SPS | Programmable via Config Register |

## I2C Addressing & PGA Settings

### Hardware Address Selection (`ADDR` Pin)

| Connection on `ADDR` Pin | I2C Slave Address (Hex) |
|---|---|
| Connect to `GND` | `0x48` (Default) |
| Connect to `VDD` | `0x49` |
| Connect to `SDA` | `0x4A` |
| Connect to `SCL` | `0x4B` |

### PGA Gain vs Resolution Voltage ($V_{LSB}$)

| PGA Gain | Full-Scale Range (FSR) | LSB Voltage ($V_{LSB} = \frac{FSR}{32768}$) |
|---|---|---|
| `2/3` | $\pm 6.144\text{ V}$ | $187.5\text{ }\mu\text{V}$ |
| `1` | $\pm 4.096\text{ V}$ | $125.0\text{ }\mu\text{V}$ |
| `2` | $\pm 2.048\text{ V}$ | $62.5\text{ }\mu\text{V}$ |
| `4` | $\pm 1.024\text{ V}$ | $31.25\text{ }\mu\text{V}$ |
| `8` | $\pm 0.512\text{ V}$ | $15.625\text{ }\mu\text{V}$ |
| `16` | $\pm 0.256\text{ V}$ | $7.8125\text{ }\mu\text{V}$ |

## Wiring

| ADS1115 Module Pin | → | Microcontroller (Arduino / ESP32 / Raspberry Pi) |
|---|---|---|
| `VDD` | | `5V` (or `3.3V`) |
| `GND` | | `GND` |
| `SDA` | | `SDA` (A4 on Uno, GPIO21 on ESP32, Pin 3 on Pi) |
| `SCL` | | `SCL` (A5 on Uno, GPIO22 on ESP32, Pin 5 on Pi) |
| `ADDR` | | `GND` (for default address `0x48`) |

> [!WARNING]
> Absolute Maximum Input Voltage Limit:
> Even when PGA gain is set to `2/3` ($\text{FSR} = \pm 6.144\text{ V}$), the analog input voltage on pins `A0`–`A3` MUST NOT exceed $V_{DD} + 0.3\text{ V}$. Supplying 6V to `A0` while $V_{DD} = 3.3\text{ V}$ will damage the internal protection diodes.

## Common mistakes

- **Exceeding $V_{DD}$ on analog inputs:** Assuming PGA `2/3` allows measuring up to 6.144 V when powering the chip with 3.3V. Input voltages must always stay within $GND - 0.3\text{ V} \le V_{IN} \le V_{DD} + 0.3\text{ V}$.
- **Not handling negative values in differential mode:** In differential mode (`A0` vs `A1`), readings range from -32768 to +32767. Store results in a signed 16-bit integer (`int16_t`).
- **Ignoring single-ended resolution limit:** In single-ended mode, negative voltages cannot be measured relative to GND. Effective single-ended resolution is 15-bit (0 to 32,767 counts).

## Notes

- Internal voltage reference accuracy is $\pm 0.15\%$ typical over temperature.
