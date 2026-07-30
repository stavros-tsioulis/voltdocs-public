## Overview

The **PCF8574** (and its address-variant **PCF8574A**) is an 8-bit remote I/O expander for the I2C bus manufactured by NXP Semiconductors and Texas Instruments. It provides general-purpose quasi-bidirectional I/O expansion for microcontrollers via a 2-wire I2C interface (`SDA` / `SCL`).

It is most widely encountered in maker projects soldered onto character LCDs as an **I2C LCD Backpack**, reducing the required HD44780 control pins from 6–10 parallel lines down to just 2 I2C pins. The IC features an open-drain interrupt output (`INT`) that alerts the host MCU when input states change.

## Quick reference

| | |
|---|---|
| **Operating voltage** | 2.5 V – 6.0 V |
| **I/O pins** | 8 quasi-bidirectional bits (`P0`–`P7`) |
| **Interface** | I2C Standard-Mode (up to 100 kHz) |
| **PCF8574 I2C address range** | `0x20` to `0x27` (determined by `A0`, `A1`, `A2` pins) |
| **PCF8574A I2C address range** | `0x38` to `0x3F` (determined by `A0`, `A1`, `A2` pins) |
| **Sink current capability** | Up to 25 mA per pin (strong pull-down) |
| **Source current capability** | Up to 300 µA per pin (weak internal pull-up) |

## Pinout

### DIP-16 / SO16 Package

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `A0` | Digital Input | Address input 0 |
| 2 | `A1` | Digital Input | Address input 1 |
| 3 | `A2` | Digital Input | Address input 2 |
| 4 | `P0` | Digital I/O | Quasi-bidirectional I/O port 0 |
| 5 | `P1` | Digital I/O | Quasi-bidirectional I/O port 1 |
| 6 | `P2` | Digital I/O | Quasi-bidirectional I/O port 2 |
| 7 | `P3` | Digital I/O | Quasi-bidirectional I/O port 3 |
| 8 | `VSS` / `GND` | Power | Ground (0 V) |
| 9 | `P4` | Digital I/O | Quasi-bidirectional I/O port 4 |
| 10 | `P5` | Digital I/O | Quasi-bidirectional I/O port 5 |
| 11 | `P6` | Digital I/O | Quasi-bidirectional I/O port 6 |
| 12 | `P7` | Digital I/O | Quasi-bidirectional I/O port 7 |
| 13 | `INT` | Digital Output | Active-LOW open-drain interrupt output |
| 14 | `SCL` | Digital Input | I2C Serial Clock Line |
| 15 | `SDA` | Digital I/O | I2C Serial Data Line |
| 16 | `VDD` / `VCC` | Power | Supply voltage (2.5 V to 6.0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | `VDD` | 2.5 | 5.0 | 6.0 | V | Normal operation |
| Standby Current | `ISTB` | — | 2.5 | 10 | µA | $V_{DD} = 5\text{ V}$, $V_I = V_{DD}$ or $V_{SS}$ |
| LOW-Level Output Current | `IOL` | 10 | 25 | — | mA | $V_{DD} = 5\text{ V}$, $V_{OL} = 1\text{ V}$ (P-port sink) |
| HIGH-Level Output Current | `IOH` | -30 | -300 | — | µA | $V_{DD} = 5\text{ V}$, $V_{OH} = V_{SS}$ (P-port source) |
| SCL Clock Frequency | `fSCL` | 0 | — | 100 | kHz | Standard I2C Mode |
| Operating Temperature | `TA` | -40 | — | +85 | °C | Ambient rating |

## Communication

PCF8574 operates without internal register pointers. Writing a single data byte over I2C directly sets the 8 output pin states (`P7`–`P0`), while reading a single byte retrieves the current logical states of all 8 pins.

### I2C Address Map

The 7-bit I2C slave address is formed by combining fixed high bits with the logic levels applied to pins `A2`, `A1`, and `A0`:

- **PCF8574:** `0 0 1 0 A2 A1 A0` $\rightarrow$ Addresses `0x20` through `0x27`.
- **PCF8574A:** `0 1 0 0 A2 A1 A0` $\rightarrow$ Addresses `0x38` through `0x3F`.

> [!NOTE]
> PCF8574 and PCF8574A are identical in functionality and pinout; using both allows up to 16 expander ICs (128 I/O pins total) on the same I2C bus.

## Wiring

### Standard PCF8574 I2C LCD Backpack to Arduino Uno

| PCF8574 Backpack Pin | → | Arduino Uno Pin | Notes |
|---|---|---|---|
| `GND` | | `GND` | Power Ground |
| `VCC` | | `5V` | Power Supply |
| `SDA` | | `A4` (or SDA pin) | I2C Data Line |
| `SCL` | | `A5` (or SCL pin) | I2C Clock Line |

> [!INFO]
> On typical LCD backpacks, pins `P0`–`P2` map to HD44780 control signals (`RS`, `RW`, `E`), `P3` controls the backlight transistor, and `P4`–`P7` drive high-nibble data lines `DB4`–`DB7`.

## Common mistakes

- **Trying to source high current from P-ports:** PCF8574 pins have a very weak internal pull-up (~300 µA max source current). To drive LEDs directly, connect the LED anode to `VCC` and sink current into the PCF8574 pin (`LOW` state = ON).
- **Confusing PCF8574 and PCF8574A I2C addresses:** PCF8574 defaults to `0x27` on most LCD backpacks (with solder jumpers open), while PCF8574A defaults to `0x3F`. If an I2C scanner doesn't detect `0x27`, check for `0x3F`.
- **Forgetting I2C pull-up resistors:** Although many microcontrollers have weak internal pull-ups, reliable 100 kHz I2C bus operation requires external 4.7 kΩ pull-up resistors on `SDA` and `SCL`.

## Notes

- **Quasi-bidirectional I/O:** To use a pin as a digital input, write a `1` (`HIGH`) to that pin first. This turns off the strong pull-down transistor, leaving only the weak internal pull-up, allowing external circuits to pull the pin `LOW`.
