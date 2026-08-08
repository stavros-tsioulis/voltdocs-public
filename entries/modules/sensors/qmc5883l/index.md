## Overview

The **QMC5883L** is a 3-axis magnetic sensor IC manufactured by QST Corporation. Designed as a modern, pin-compatible alternative to the legacy Honeywell HMC5883L, it integrates anisotropic magnetoresistive (AMR) sensors with a 16-bit high-resolution ADC and signal processing ASIC.

It is widely found on cheap GY-271 breakout boards sold online as "HMC5883L modules". While physically similar, the QMC5883L operates on a different I2C slave address (`0x0D` instead of `0x1E`) and uses different control register mappings.

## Quick reference

| | |
|---|---|
| **Module VCC** | 3.3 V to 5.0 V DC (onboard LDO) |
| **Chip VDD** | 2.16 V to 3.6 V DC |
| **Field range** | $\pm 2.0\text{ Gauss}$ or $\pm 8.0\text{ Gauss}$ (selectable via Control Register 1) |
| **ADC resolution** | 16-bit ($3000\text{ LSB/Gauss}$ sensitivity at $\pm 2\text{ G}$) |
| **Output data rate** | 10 Hz, 50 Hz, 100 Hz, or 200 Hz |
| **Communication interface** | I2C (fixed address `0x0D`, up to 400 kHz) |
| **Operating current** | 75 µA active, 3 µA standby |

## Pinout

### Standard GY-271 5-Pin Breakout Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SCL` | Digital Input | I2C Serial Clock input |
| 4 | `SDA` | Digital I/O | I2C Serial Data line |
| 5 | `DRDY` | Digital Output | Data Ready interrupt pin (Active-HIGH) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 2.16 | 3.0 | 3.6 | V | DC |
| Operating Current | $I_{DD}$ | — | 75 | 100 | µA | $ODR = 10\text{ Hz}$ |
| Standby Current | $I_{STB}$ | — | 3 | 10 | µA | Standby mode |
| Full-Scale Range (RNG = 00) | $FS$ | — | $\pm 2.0$ | — | Gauss | |
| Full-Scale Range (RNG = 01) | $FS$ | — | $\pm 8.0$ | — | Gauss | |
| Field Sensitivity (2G Range) | $S$ | — | 3000 | — | LSB/Gauss | |
| Output Data Rate | $ODR$ | 10 | — | 200 | Hz | Configurable in Control Register 1 |

## Register map (QMC5883L)

| Address | Register | Access | Reset | Description |
|---|---|---|---|---|
| `0x00`–`0x01` | `OUT_X_L`, `OUT_X_H` | R | `0x00` | Output X Data (16-bit signed, Little-Endian) |
| `0x02`–`0x03` | `OUT_Y_L`, `OUT_Y_H` | R | `0x00` | Output Y Data (16-bit signed, Little-Endian) |
| `0x04`–`0x05` | `OUT_Z_L`, `OUT_Z_H` | R | `0x00` | Output Z Data (16-bit signed, Little-Endian) |
| `0x06` | `STATUS` | R | `0x00` | Status Register (`DRDY` bit 0 = Data Ready, `OVL` bit 1 = Overflow) |
| `0x09` | `CONTROL_1` | R/W | `0x00` | Mode, ODR, Range, Oversampling ratio |
| `0x0A` | `CONTROL_2` | R/W | `0x00` | Soft Reset, Pointer roll-over, Interrupt enable |
| `0x0B` | `SET_RESET` | R/W | `0x01` | Set/Reset Period register (Write `0x01` during init) |
| `0x0D` | `CHIP_ID` | R | `0xFF` | Chip ID register (returns `0xFF`) |

## Control Register 1 (`0x09`) Configuration

| Bits [7:6] `OSR` | Bits [5:4] `RNG` | Bits [3:2] `ODR` | Bits [1:0] `MODE` |
|---|---|---|---|
| `00` = 512 Oversampling | `00` = $\pm 2\text{ Gauss}$ | `00` = 10 Hz | `00` = Standby Mode |
| `01` = 256 Oversampling | `01` = $\pm 8\text{ Gauss}$ | `01` = 50 Hz | `01` = Continuous Mode |
| `10` = 128 Oversampling | `10` = Reserved | `10` = 100 Hz | `10` = Reserved |
| `11` = 64 Oversampling | `11` = Reserved | `11` = 200 Hz | `11` = Reserved |

To initialize for continuous 200 Hz reading at $\pm 2\text{ Gauss}$ range with 512 oversampling: Write `0x1D` to register `0x09` and `0x01` to register `0x0B`.

## Wiring

| QMC5883L Module Pin | → | Microcontroller (Arduino Uno / ESP32) |
|---|---|---|
| `VCC` | | `3.3V` (or `5V`) |
| `GND` | | `GND` |
| `SCL` | | `SCL` (A5 on Uno, GPIO22 on ESP32) |
| `SDA` | | `SDA` (A4 on Uno, GPIO21 on ESP32) |

> [!WARNING]
> Incompatibility with HMC5883L Libraries:
> The QMC5883L defaults to I2C address `0x0D` and uses Little-Endian 16-bit register reads starting at `0x00` (X_LSB, X_MSB, Y_LSB, Y_MSB, Z_LSB, Z_MSB). Running standard HMC5883L code will fail to communicate. Ensure you install a `QMC5883L` specific library.

## Common mistakes

- **Attempting to read from I2C address 0x1E:** The QMC5883L responds on `0x0D`.
- **Forgetting to set `SET_RESET` register (`0x0B`):** Writing `0x01` to register `0x0B` is required during setup to clear the AMR sensor offset.
- **Reading data in Big-Endian format:** QMC5883L outputs Little-Endian bytes (`LSB` byte first, then `MSB` byte), opposite to the HMC5883L.

## Notes

- Compass Heading Formula: $\text{Heading (rad)} = \text{atan2}(Y, X)$. Convert to degrees: $\text{Heading (deg)} = \text{Heading (rad)} \times \frac{180}{\pi}$.
