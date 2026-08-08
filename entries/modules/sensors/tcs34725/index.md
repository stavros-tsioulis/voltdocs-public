## Overview

The **TCS34725** is a high-precision color light-to-digital converter IC manufactured by ams OSRAM (formerly TAOS). It features a $3 \times 4$ array of filtered photodiodes (**Red**, **Green**, **Blue**, and **Clear / Unfiltered**) integrated with an **IR-blocking filter**.

Because the IR filter blocks infrared spectral interference from ambient light sources (incandescent light bulbs, sunlight), the TCS34725 delivers accurate RGB color readings, color temperature in Kelvin ($K$), and lux illuminance. Breakout boards include an onboard neutral white 4150K LED for illuminating target objects.

## Quick reference

| | |
|---|---|
| **Module VCC** | 3.3 V to 5.0 V DC (onboard 3.3V LDO) |
| **Chip VDD** | 2.7 V to 3.6 V DC |
| **Dynamic Range** | 3,800,000 : 1 |
| **IR Filter** | Integrated Infrared Blocking Filter |
| **Selectable Analog Gain** | $1\times, 4\times, 16\times, 60\times$ |
| **Programmable Integration Time** | 2.4 ms, 24 ms, 101 ms, 154 ms, 700 ms |
| **Communication Interface** | I2C (fixed slave address `0x29`, up to 400 kHz) |
| **Illumination Control (`LED` pin)** | High-brightness neutral white LED output control pin |

## Pinout

### Standard 7-Pin Breakout Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VIN` | Power Input | Supply voltage (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `3V3` | Power Output | Regulated +3.3 V DC output from internal LDO |
| 4 | `SCL` | Digital Input | I2C Serial Clock input |
| 5 | `SDA` | Digital I/O | I2C Serial Data line |
| 6 | `INT` | Digital Output | Active-LOW Interrupt output pin |
| 7 | `LED` | Digital Input | Onboard White LED control pin (`HIGH`/Unconnected = LED ON, `LOW` = LED OFF) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Chip) | $V_{DD}$ | 2.7 | 3.0 | 3.6 | V | DC |
| Active Current | $I_{DD}$ | — | 235 | 330 | µA | Active conversion mode |
| Sleep Current | $I_{SLEEP}$ | — | 2.5 | 10 | µA | Sleep state |
| Red Photodiode Responsivity | $R_R$ | — | 125 | — | % | Normalized to peak red |
| Green Photodiode Responsivity | $G_R$ | — | 140 | — | % | Normalized to peak green |
| Blue Photodiode Responsivity | $B_R$ | — | 100 | — | % | Normalized to peak blue |
| Max ADC Count | $FS_{count}$ | — | 65535 | — | Counts | 16-bit ADC per channel |

## Color Temperature & Lux Calculation

To calculate Color Temperature ($CT$ in Kelvin) and Illuminance ($Lux$) from raw 16-bit RGBC counts ($R, G, B, C$):

1. **Calculate Chromaticity Coordinates ($X, Y, Z$):**
   $$X = (-0.14282 \times R) + (0.15492 \times G) + (-0.05291 \times B)$$
   $$Y = (-0.32466 \times R) + (1.57837 \times G) + (-0.73191 \times B)$$
   $$Z = (-0.68202 \times R) + (0.77073 \times G) + (0.56332 \times B)$$

2. **Calculate Chromaticity Coordinates ($x, y$):**
   $$x = \frac{X}{X + Y + Z}, \quad y = \frac{Y}{X + Y + Z}$$

3. **McCamy's Formula for Color Temperature ($CT$):**
   $$n = \frac{x - 0.3320}{0.1858 - y}$$
   $$CT\text{ (in Kelvin)} = 449 \times n^3 + 3525 \times n^2 + 6823.3 \times n + 5520.33$$

## Wiring

| TCS34725 Breakout Pin | → | Microcontroller (Arduino Uno / ESP32) |
|---|---|---|
| `VIN` | | `5V` (or `3.3V`) |
| `GND` | | `GND` |
| `SCL` | | `SCL` (A5 on Uno, GPIO22 on ESP32) |
| `SDA` | | `SDA` (A4 on Uno, GPIO21 on ESP32) |
| `LED` | | Digital Pin (or leave floating to keep white LED ON) |

## Common mistakes

- **Forgetting Command Byte bit 7 (0x80):** All I2C register transactions require setting bit 7 of the register address byte (`0x80 | Register_Address`).
- **ADC Saturation under bright white LED reflection:** Placing glossy colored objects too close ($<2\text{ mm}$) to the white LED causes 16-bit ADC overflow (`65535` counts). Adjust Gain down to $1\times$ or reduce integration time to $24\text{ ms}$.
- **Measuring unilluminated objects:** Ambient shadows distort color reading accuracy. Always use the onboard white LED in a covered sensor shroud for consistent color sorting.

## Notes

- Standard choice for automated color-sorting robot arms, fruit ripeness sensors, and display color calibration tools.
