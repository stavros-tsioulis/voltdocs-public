## Overview

The **BMP180** is a digital barometric pressure sensor manufactured by Bosch Sensortec. It serves as the predecessor to the BMP280, measuring barometric pressure ($300\text{ to }1100\text{ hPa}$) and temperature over an I2C bus.

It includes a piezo-resistive sensor, an ADC, a control unit, and an EPROM containing 11 factory calibration coefficients (`AC1`–`AC6`, `VB1`, `VB2`, `MB`, `MC`, `MD`). Host software reads these EEPROM coefficients on startup and applies them to calculate temperature-compensated pressure and altitude.

## Quick reference

| | |
|---|---|
| **Module VCC** | 3.3 V to 5.0 V DC (onboard 3.3V LDO) |
| **Chip VDD** | 1.8 V to 3.6 V DC |
| **Pressure range** | 300 hPa to 1100 hPa (+9000 m to -500 m relative to sea level) |
| **Pressure resolution** | 0.01 hPa (0.17 m altitude noise in ultra-high res mode) |
| **Temperature range** | $-40^\circ\text{C}$ to $+85^\circ\text{C}$ ($\pm 1.0\text{ }^\circ\text{C}$ accuracy) |
| **Communication interface** | I2C (fixed address `0x77`, up to 3.4 MHz) |
| **Peak current** | 650 µA during conversion, 0.1 µA standby |

## Pinout

### Standard GY-68 Breakout Board Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SCL` | Digital Input | I2C Serial Clock input line |
| 4 | `SDA` | Digital I/O | I2C Serial Data line |
| 5 | `3.3V` | Power Output | Regulated 3.3V power output |
| 6 | `CLR` / `EOC` | Digital Output | End of Conversion signal output (Active-HIGH) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Chip) | $V_{DD}$ | 1.8 | 2.5 | 3.6 | V | DC |
| Absolute Pressure Accuracy | $\Delta P_{abs}$ | -4.0 | -1.0 | +2.5 | hPa | $V_{DD} = 3.3\text{ V}$, $0^\circ\text{C} \text{ to } +65^\circ\text{C}$ |
| Relative Pressure Accuracy | $\Delta P_{rel}$ | — | $\pm 0.12$ | — | hPa | At $25^\circ\text{C}$, equivalent to $\pm 1\text{ m}$ |
| Temperature Accuracy | $\Delta T$ | -2.0 | $\pm 1.0$ | +2.0 | °C | $0^\circ\text{C} \text{ to } +65^\circ\text{C}$ |
| Conversion Time (Ultra Low Power) | $t_{conv,ULP}$ | — | 3.0 | 4.5 | ms | OSS = 0 |
| Conversion Time (Ultra High Res) | $t_{conv,UHR}$ | — | 17.0 | 25.5 | ms | OSS = 3 |

## Oversampling Modes (`OSS`)

| Mode (`OSS`) | Description | Samples | Conv Time | Current Draw |
|---|---|---|---|---|
| `0` | Ultra Low Power | 1 | 4.5 ms | $3\text{ }\mu\text{A}$ |
| `1` | Standard | 2 | 7.5 ms | $5\text{ }\mu\text{A}$ |
| `2` | High Resolution | 4 | 13.5 ms | $7\text{ }\mu\text{A}$ |
| `3` | Ultra High Resolution | 8 | 25.5 ms | $12\text{ }\mu\text{A}$ |

## Register Map & Measurement Flow

### Key Registers

| Address | Register | Access | Description |
|---|---|---|---|
| `0xAA`–`0xBF` | Calibration Coefficients | R | 11 16-bit calibration coefficients (`AC1`–`MD`) |
| `0xD0` | `CHIP_ID` | R | Chip ID register (returns `0x55`) |
| `0xF4` | `CONTROL` | W | Write `0x2E` to start Temp read; `0x34 + (OSS << 6)` for Pressure |
| `0xF6`–`0xF8` | `DATA_OUT` | R | Read raw conversion result MSB (`0xF6`), LSB (`0xF7`), XLSB (`0xF8`) |

### Measurement Sequence

1. Read 11 EEPROM calibration words (`0xAA` to `0xBF`).
2. Write `0x2E` to register `0xF4` (Start uncompensated Temperature measurement).
3. Wait at least **4.5 ms**, then read 2 bytes from `0xF6` (raw temperature `UT`).
4. Write `0x34 + (OSS << 6)` to register `0xF4` (Start uncompensated Pressure measurement).
5. Wait conversion time ($4.5\text{ ms to }25.5\text{ ms}$ depending on `OSS`), then read 3 bytes from `0xF6` (raw pressure `UP`).
6. Apply Bosch datasheet polynomial math using `UT`, `UP`, and calibration constants to calculate final $T$ and $P$.

## Wiring

| GY-68 (BMP180) Pin | → | Microcontroller (Arduino Uno / ESP32) |
|---|---|---|
| `VCC` | | `5V` (or `3.3V`) |
| `GND` | | `GND` |
| `SCL` | | `SCL` (A5 on Uno, GPIO22 on ESP32) |
| `SDA` | | `SDA` (A4 on Uno, GPIO21 on ESP32) |

## Common mistakes

- **Skipping EEPROM calibration step:** Applying raw pressure values without calculating temperature compensation using the 11 EEPROM coefficients yields completely invalid pressure readings.
- **Reading pressure before reading temperature:** The pressure compensation formula requires the temperature value ($B_5$ parameter). Temperature MUST be read and calculated prior to calculating pressure.
- **Fixed I2C address:** Unlike the BMP280 (`0x76`/`0x77`), the BMP180 has a hardcoded I2C address of **`0x77`** which cannot be changed via hardware pins.

## Notes

- Calculate altitude from pressure: $\text{Altitude (m)} = 44330 \times \left(1 - \left(\frac{P}{1013.25}\right)^{0.1903}\right)$.
