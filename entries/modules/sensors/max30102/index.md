## Overview

The **MAX30102** is an integrated pulse oximetry and heart-rate monitor IC manufactured by Maxim Integrated (Analog Devices). It combines a **660 nm Red LED**, an **880 nm Infrared (IR) LED**, photodetectors, optical lenses, ambient light cancellation circuitry, and an 18-bit ADC inside a tiny $5.6 \times 3.3\text{ mm}$ package.

It measures blood oxygen saturation ($\text{SpO}_2$) and heart rate in Beats Per Minute (BPM) by detecting photoplethysmogram (PPG) optical absorption changes in arterial blood vessels when a finger is placed over the glass cover window.

## Quick reference

| | |
|---|---|
| **Breakout Module Supply (`VIN`)** | 3.3 V to 5.0 V DC (onboard 1.8V & 3.3V LDO regulators) |
| **Chip Power Supply (`VDD`)** | 1.7 V to 2.0 V DC |
| **LED Driver Voltage (`VLED`)** | 3.1 V to 5.25 V DC |
| **LED Wavelengths** | Red: 660 nm / Infrared: 880 nm |
| **ADC Resolution** | 18-bit delta-sigma ADC (up to 3200 samples per second) |
| **Communication Interface** | I2C (fixed slave address `0x57`, up to 400 kHz) |
| **FIFO Buffer** | 32-sample internal FIFO buffer |
| **Operating Current** | 600 µA active, 0.7 µA shutdown |

## Pinout

### Standard 5-Pin / 7-Pin Breakout Board Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VIN` | Power Input | Supply voltage (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SCL` | Digital Input | I2C Serial Clock input |
| 4 | `SDA` | Digital I/O | I2C Serial Data line |
| 5 | `INT` | Digital Output | Active-LOW Interrupt output (alerts MCU on new sample or FIFO full) |
| 6 | `IRD` | Power Output | Infrared LED cathode connection (internal connection on 5-pin boards) |
| 7 | `RD` | Power Output | Red LED cathode connection (internal connection on 5-pin boards) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Chip Voltage ($V_{DD}$) | $V_{DD}$ | 1.7 | 1.8 | 2.0 | V | DC |
| LED Voltage ($V_{LED}$) | $V_{LED}$ | 3.1 | 3.3 | 5.25 | V | DC |
| Peak Current (Red LED) | $I_{RED}$ | 0 | 25 | 50 | mA | Programmable in 0.2mA steps |
| Peak Current (IR LED) | $I_{IR}$ | 0 | 25 | 50 | mA | Programmable in 0.2mA steps |
| Sample Rate | $SR$ | 50 | 400 | 3200 | SPS | Samples per second |
| Dynamic Range | $DR$ | — | 89 | — | dB | Ambient light cancellation |

## Photoplethysmography ($\text{SpO}_2$) Principle

Oxygenated hemoglobin ($\text{HbO}_2$) absorbs more Infrared light ($880\text{ nm}$), whereas deoxygenated hemoglobin ($\text{Hb}$) absorbs more Red light ($660\text{ nm}$).

By calculating the ratio of ratios ($R$) from the AC and DC components of the Red and IR PPG signals:

$$R = \frac{(AC_{\text{Red}} / DC_{\text{Red}})}{(AC_{\text{IR}} / DC_{\text{IR}})}$$

$$\text{SpO}_2\text{ (\%)} = 110 - 25 \times R$$

## Wiring

| MAX30102 Breakout Pin | → | Microcontroller (Arduino Uno / ESP32) |
|---|---|---|
| `VIN` | | `3.3V` (or `5V`) |
| `GND` | | `GND` |
| `SCL` | | `SCL` (A5 on Uno, GPIO22 on ESP32) |
| `SDA` | | `SDA` (A4 on Uno, GPIO21 on ESP32) |
| `INT` | | GPIO Pin with Interrupt support (e.g. D2 / GPIO4) |

> [!WARNING]
> Medical Safety Warning & Cheap Breakout I2C Pull-up Flaw:
> - **Hobbyist Non-Medical Device:** The MAX30102 is an educational/hobbyist sensor. It must NOT be used for medical diagnosis, patient monitoring, or life safety.
> - **Cheap Breakout PCB Flaw:** Some low-cost purple/green MAX30102 breakout boards miswire the onboard I2C pull-up resistors to the 1.8V rail instead of 3.3V, causing I2C communication failures on 3.3V/5V MCUs. Cut the 1.8V pull-up trace or add external $4.7\text{ k}\Omega$ pull-up resistors to 3.3V.

## Common mistakes

- **Excessive finger pressure:** Pressing down hard on the sensor cuts off capillary blood flow in the fingertip, flattening the AC PPG pulse and causing zero readings. Rest the finger gently over the glass window.
- **Ambient Light Leakage:** Bright indoor light bleeding into the optical receiver photodiode distorts $\text{SpO}_2$ calculations. Cover the finger and sensor with a dark cloth or clip.
- **MAX30100 vs MAX30102 differences:** The MAX30100 is an older IC with different register addresses and 14-bit resolution. Software libraries written for MAX30100 will NOT work on MAX30102.

## Notes

- Supported by popular open-source libraries like `SparkFun_MAX3010x` for automatic heart rate and $\text{SpO}_2$ calculation.
