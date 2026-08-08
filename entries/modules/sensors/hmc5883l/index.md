## Overview

The **HMC5883L** is a 3-axis digital magnetometer IC manufactured by Honeywell. It uses Anisotropic Magnetoresistive (AMR) technology to measure both the direction and magnitude of Earth's magnetic fields (typically $0.3\text{ to }0.6\text{ Gauss}$) for electronic compass navigation in robotics, drones, and mobile devices.

Breakout boards (GY-271) include 3.3V power regulation and I2C level shifting. Note that most low-cost modules sold today contain the pin-compatible replacement chip **QMC5883L** by QST Corporation, which uses different I2C register addresses.

## Quick reference

| | |
|---|---|
| **Module VCC** | 3.3 V to 5.0 V DC (onboard LDO) |
| **Chip VDD / VDDIO** | 2.16 V to 3.6 V DC |
| **Field range** | $\pm 0.88\text{ Gauss}$ to $\pm 8.1\text{ Gauss}$ (default $\pm 1.3\text{ Gauss}$) |
| **ADC resolution** | 12-bit (5 milligauss field resolution) |
| **Output data rate** | 0.75 Hz to 75 Hz (up to 160 Hz in continuous mode) |
| **Communication interface** | I2C (fixed address `0x1E` for HMC5883L / `0x0D` for QMC5883L) |
| **Heading accuracy** | 1° to 2° (with proper hard/soft iron calibration) |

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
| Operating Current | $I_{DD}$ | — | 100 | 180 | µA | Continuous measurement mode |
| Idle Current | $I_{idle}$ | — | 2 | 5 | µA | Idle mode |
| Magnetic Field Range | $B$ | $\pm 0.88$ | $\pm 1.3$ | $\pm 8.1$ | Gauss | User selectable via Gain bits |
| Gain Sensitivity | $S_{gain}$ | 230 | 1090 | 1370 | LSB/Gauss | $1090\text{ LSB/Gauss at } \pm 1.3\text{ G}$ |
| Linearity Error | $NL$ | — | 0.1 | — | % FS | Full scale |
| Operating Temp Range | $T_{OP}$ | -30 | — | 85 | °C | |

## Register map (HMC5883L)

| Address | Register | Access | Reset | Description |
|---|---|---|---|---|
| `0x00` | `CRA` | R/W | `0x10` | Configuration Register A (Samples averaged, Output rate, Measurement mode) |
| `0x01` | `CRB` | R/W | `0x20` | Configuration Register B (Gain configuration) |
| `0x02` | `MODE` | R/W | `0x03` | Mode Register (`0x00` = Continuous-measurement, `0x01` = Single-measurement) |
| `0x03`–`0x08` | `DATAX_H`..`DATAZ_L` | R | — | Data Output Registers (Order: X-MSB, X-LSB, Z-MSB, Z-LSB, Y-MSB, Y-LSB) |
| `0x0A` | `IRA` | R | `0x48` | Identification Register A (returns `'H'`) |

> [!NOTE]
> HMC5883L Axis Read Order:
> Notice that the register read order for HMC5883L is **X, Z, Y** (not X, Y, Z!). Register `0x03`–`0x04` is X, `0x05`–`0x06` is Z, and `0x07`–`0x08` is Y.

## HMC5883L vs QMC5883L Differentiation

| Feature | HMC5883L (Honeywell) | QMC5883L (QST Corp) |
|---|---|---|
| **I2C Slave Address** | `0x1E` | `0x0D` |
| `ID` Register (`0x0A` / `0x0D`) | Returns `'H'` (`0x48`) | Returns `0xFF` / `0x00` |
| **Control Register** | `0x02` Mode Reg (`0x00` = Continuous) | `0x09` Control Reg 1 (`0x1D` = Continuous) |
| **Data Register Order** | X_MSB, X_LSB, **Z_MSB**, **Z_LSB**, Y_MSB, Y_LSB | X_LSB, X_MSB, Y_LSB, Y_MSB, Z_LSB, Z_MSB |

## Wiring

| GY-271 Module Pin | → | Microcontroller (Arduino Uno / ESP32) |
|---|---|---|
| `VCC` | | `3.3V` (or `5V`) |
| `GND` | | `GND` |
| `SCL` | | `SCL` (A5 on Uno, GPIO22 on ESP32) |
| `SDA` | | `SDA` (A4 on Uno, GPIO21 on ESP32) |

## Common mistakes

- **Using HMC5883L software library for QMC5883L clones:** Most modern GY-271 breakout boards ship with QMC5883L ICs. Running an HMC5883L library on a QMC5883L chip will fail with `I2C device not found at 0x1E`. Run an I2C scanner script to check for `0x1E` vs `0x0D`.
- **Misinterpreting X, Z, Y register order on HMC5883L:** Reading bytes in X, Y, Z order results in swapping the Y and Z values.
- **Ignoring Hard-Iron / Soft-Iron distortion:** Nearby metal components, battery wires, or motors cause severe distortion. Calibration is required to map raw X/Y readings to a centered circle before calculating heading ($\text{Heading} = \text{atan2}(Y, X)$).

## Notes

- Magnetic Declination angle must be added to the calculated magnetic heading to yield True North heading.
