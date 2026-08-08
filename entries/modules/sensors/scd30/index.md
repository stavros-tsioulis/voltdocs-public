## Overview

The **SCD30** is a dual-channel Non-Dispersive Infrared (NDIR) true $\text{CO}_2$ sensor module manufactured by Sensirion. Unlike eCO2 VOC sensors (such as SGP30 or MQ-135) that estimate carbon dioxide indirectly via proxy hydrogen/VOC gases, the SCD30 measures true atmospheric carbon dioxide molecules using infrared light absorption at $4.26\text{ }\mu\text{m}$.

The module incorporates a dual-channel NDIR optical absorption cell (one channel for $\text{CO}_2$ sensing, one reference channel to compensate for optical drift), an integrated Sensirion SHT31 humidity and temperature sensor, and automatic self-calibration (ASC) logic.

## Quick reference

| | |
|---|---|
| **Operating Voltage (`VDD`)** | 3.3 V to 5.5 V DC |
| **Measurement Range ($\text{CO}_2$)** | 400 ppm to 10,000 ppm |
| **Accuracy ($\text{CO}_2$)** | $\pm (30\text{ ppm} + 3\%\text{ of reading})$ |
| **Temperature Range / Accuracy** | $-40^\circ\text{C}$ to $+70^\circ\text{C}$ ($\pm 0.4\text{ }^\circ\text{C}$ accuracy) |
| **Relative Humidity Range / Accuracy** | 0% to 100% RH ($\pm 3\%\text{ RH}$ accuracy) |
| **Communication interfaces** | I2C (address `0x61`, clock stretching required), Modbus over UART |
| **Onboard Self-Calibration** | Automatic Self-Calibration (ASC) & Forced Recalibration (FRC) |
| **Average Supply Current** | 19 mA (2-second interval) / 75 mA peak during IR lamp pulse |

## Pinout

### Standard 7-Pin Header Interface

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VDD` | Power Input | Supply voltage (+3.3 V to +5.5 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `TX` / `SCL` | Digital I/O | UART TX (Modbus mode) / I2C Serial Clock `SCL` (I2C mode) |
| 4 | `RX` / `SDA` | Digital I/O | UART RX (Modbus mode) / I2C Serial Data `SDA` (I2C mode) |
| 5 | `RDDY` | Digital Output | Data Ready pin (`HIGH` when new sample measurement is ready) |
| 6 | `PWM` | Digital Output | PWM output pin (proportional to CO2 concentration) |
| 7 | `SEL` | Digital Input | Interface Select (`LOW` or Unconnected = I2C mode, `HIGH` = Modbus UART mode) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 3.3 | 5.0 | 5.5 | V | DC |
| Peak Current | $I_{PEAK}$ | — | 75 | 95 | mA | IR optical lamp pulse |
| Average Current (2s rate) | $I_{AVG}$ | — | 19 | 25 | mA | Default 2-second interval |
| Repeatability ($\text{CO}_2$) | $REP$ | — | $\pm 10$ | — | ppm | |
| Response Time ($t_{63\%}$) | $\tau$ | — | 20 | — | s | Natural convection |
| Temperature Compensation | $T_{COMP}$ | — | Onboard | — | — | Automatic SHT31 compensation |

## Communication Registers (I2C Address `0x61`)

Each I2C read/write command uses a 16-bit command word followed by 16-bit data words with an 8-bit CRC byte (`CRC-8` polynomial $x^8 + x^5 + x^4 + 1$):

| Command Hex | Description |
|---|---|
| `0x0010` | Start Continuous Measurement (Parameter: Ambient pressure in mbar or `0x0000`) |
| `0x0104` | Stop Continuous Measurement |
| `0x0202` | Set Measurement Interval (2 to 1800 seconds) |
| `0x0207` | Read Data Ready Status (Returns `1` if new reading available) |
| `0x0300` | Read Measurement (Returns 18 bytes: 4 bytes CO2, 4 bytes Temp, 4 bytes Humidity + CRCs) |
| `0x5306` | Enable / Disable Automatic Self-Calibration (ASC) |

## Wiring

| SCD30 Pin | → | Microcontroller (Arduino Uno / ESP32) | Notes |
|---|---|---|---|
| `VDD` | | `5V` (or `3.3V`) | 5V recommended for stable IR lamp pulse |
| `GND` | | `GND` | Ground |
| `SCL` | | `SCL` (A5 on Uno, GPIO22 on ESP32) | **Requires I2C Clock Stretching!** |
| `SDA` | | `SDA` (A4 on Uno, GPIO21 on ESP32) | $10\text{ k}\Omega$ pull-up resistor |
| `SEL` | | `GND` | Selects I2C protocol mode |

> [!WARNING]
> I2C Clock Stretching & Power Peak Guidance:
> - **Clock Stretching:** The internal microcontroller of the SCD30 holds the `SCL` line LOW for up to **150 ms** while reading the optical IR cell. Software MUST enable hardware I2C clock stretching or use a generous timeout setting.
> - **IR Lamp Peak Current:** The internal IR lamp pulses at 75 mA. Ensure the power rail can supply steady current without dropping below 3.3V.

## Common mistakes

- **Covering the white PTFE optical membrane:** The white filter membrane on top of the SCD30 protects the optical cell from dust. Touching, puncturing, or sealing this membrane prevents air exchange.
- **Orientation tilt:** The optical cavity in the SCD30 is factory calibrated in a vertical orientation. Mounting the module upside down or sideways can shift calibration by 20–50 ppm.
- **Disabling Automatic Self-Calibration (ASC) without outdoor fresh air exposure:** ASC assumes that the sensor is exposed to fresh outdoor air ($\approx 400\text{ ppm }\text{CO}_2$) at least once every 7 days. If deployed in a permanently sealed, occupied room without fresh air exchange, ASC will miscalibrate.

## Notes

- Includes ambient pressure compensation inputs (`0x0010`) to adjust $\text{CO}_2$ readings for barometric pressure changes at high altitudes.
