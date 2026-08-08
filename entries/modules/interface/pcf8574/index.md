## Overview

The **PCF8574** (and its companion variant **PCF8574A**) is an 8-bit quasi-bidirectional I/O expander for the I2C bus manufactured by NXP Semiconductors and Texas Instruments. It provides general-purpose remote I/O expansion for microcontrollers via a two-line bidirectional I2C bus (`SDA` and `SCL`).

It features 8 quasi-bidirectional I/O pins (`P0`–`P7`), three hardware address input pins (`A0`, `A1`, `A2`), and an active-LOW open-drain interrupt output (`INT`). The PCF8574 is widely integrated into I2C backpack boards for HD44780 character LCD displays (LCD1602 / LCD2004) and used for button matrix scanning or driving LEDs.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 2.5 V to 6.0 V DC |
| **I2C bus clock speed** | Up to 100 kHz (Standard-mode I2C) |
| **I/O ports** | 8 Quasi-bidirectional pins (`P0`–`P7`) |
| **I2C address (PCF8574)** | `0x20` to `0x27` (determined by `A0`–`A2`) |
| **I2C address (PCF8574A)** | `0x38` to `0x3F` (determined by `A0`–`A2`) |
| **Interrupt output** | Active-LOW open-drain (`INT`) |
| **Standby current** | 10 µA max |

## Pinout

### 16-Pin DIP / SOIC Package

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `A0` | Digital Input | Address input 0 |
| 2 | `A1` | Digital Input | Address input 1 |
| 3 | `A2` | Digital Input | Address input 2 |
| 4 | `P0` | Quasi-I/O | Quasi-bidirectional I/O port 0 |
| 5 | `P1` | Quasi-I/O | Quasi-bidirectional I/O port 1 |
| 6 | `P2` | Quasi-I/O | Quasi-bidirectional I/O port 2 |
| 7 | `P3` | Quasi-I/O | Quasi-bidirectional I/O port 3 |
| 8 | `VSS` | Power | Ground (0 V) |
| 9 | `P4` | Quasi-I/O | Quasi-bidirectional I/O port 4 |
| 10 | `P5` | Quasi-I/O | Quasi-bidirectional I/O port 5 |
| 11 | `P6` | Quasi-I/O | Quasi-bidirectional I/O port 6 |
| 12 | `P7` | Quasi-I/O | Quasi-bidirectional I/O port 7 |
| 13 | `INT` | Digital Output | Interrupt output (Open-drain, Active-LOW) |
| 14 | `SCL` | Digital Input | I2C Serial Clock line |
| 15 | `SDA` | Digital I/O | I2C Serial Data line (Open-drain) |
| 16 | `VDD` | Power | Positive supply voltage (+2.5 V to +6.0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 2.5 | 5.0 | 6.0 | V | |
| Supply Current | $I_{DD}$ | — | 40 | 100 | µA | $V_{DD} = 5.0\text{ V}$, no load, $f_{SCL} = 100\text{ kHz}$ |
| Standby Current | $I_{stb}$ | — | 2.5 | 10 | µA | $V_{DD} = 5.0\text{ V}$, $I_{IO} = 0$ |
| LOW-level Input Voltage | $V_{IL}$ | -0.5 | — | $0.3 V_{DD}$ | V | |
| HIGH-level Input Voltage | $V_{IH}$ | $0.7 V_{DD}$ | — | $V_{DD} + 0.5$ | V | |
| LOW-level Output Current | $I_{OL}$ | 10 | 25 | — | mA | $V_{DD} = 5.0\text{ V}$, $V_{OL} = 1.0\text{ V}$ (Sinking) |
| HIGH-level Output Current | $I_{OH}$ | -30 | -100 | -300 | µA | $V_{DD} = 5.0\text{ V}$, $V_{OH} = V_{SS}$ (Source) |
| SCL/SDA Clock Frequency | $f_{SCL}$ | 0 | — | 100 | kHz | Standard Mode |

## Communication & Addressing

The PCF8574 uses a 7-bit slave address consisting of a 4-bit fixed control code (`0100` for PCF8574, `0111` for PCF8574A) followed by 3 programmable address bits (`A2`, `A1`, `A0`).

### Address Map

| Part Number | Slave Address Byte Format (R/W = 0) | I2C Address Range (Hex) |
|---|---|---|
| **PCF8574** | `0 1 0 0  A2 A1 A0 R/W` | `0x20` – `0x27` |
| **PCF8574A** | `0 1 1 1  A2 A1 A0 R/W` | `0x38` – `0x3F` |

### Quasi-Bidirectional I/O Architecture
Each pin can be used as an input or output without a direction control register. 
- **As an Output:** Sinks up to 25 mA (`LOW`). Sourcing current (`HIGH`) is limited to ~100 µA via an internal pull-up.
- **As an Input:** Software must first write a `HIGH` (1) to the port pin. When configured HIGH, an external driver can pull the pin `LOW`.

## Wiring

| PCF8574 Breakout | → | Microcontroller (Arduino / ESP32) | Notes |
|---|---|---|---|
| `VCC` / `VDD` | | `5V` (or `3.3V`) | Power supply |
| `GND` / `VSS` | | `GND` | Common ground |
| `SDA` | | `SDA` (A4 on Uno, GPIO21 on ESP32) | I2C Data (requires pull-up resistors) |
| `SCL` | | `SCL` (A5 on Uno, GPIO22 on ESP32) | I2C Clock (requires pull-up resistors) |
| `INT` | | GPIO Pin (e.g. GPIO2) | Optional interrupt line |

> [!NOTE]
> When using PCF8574 as an LCD backpack board, solder jumpers A0, A1, and A2 configure the address (`0x27` is common for PCF8574, `0x3F` for PCF8574A).

## Common mistakes

- **Attempting to read inputs without writing HIGH first:** Because ports are quasi-bidirectional, reading a pin that was previously written `LOW` will always return `0`. Always write `1` (`HIGH`) to pins intended as inputs before reading.
- **Relying on strong HIGH output drive:** The chip can sink up to 25 mA (`LOW`) but can only source ~100 µA (`HIGH`). Active-HIGH LED circuits will be very dim; connect LEDs in active-LOW (sinking) configuration instead.
- **Confusing PCF8574 and PCF8574A I2C addresses:** PCF8574 uses base `0x20`, whereas PCF8574A uses base `0x38`. Running an I2C scanner script is recommended if communication fails.

## Notes

- Up to 8 PCF8574 and 8 PCF8574A devices can co-exist on the same I2C bus for up to 128 total I/O pins.
