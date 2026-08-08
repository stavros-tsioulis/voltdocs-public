## Overview

The **MCP23017** is a 16-bit general-purpose parallel I/O expander for the I2C bus manufactured by Microchip Technology. It provides 16 individual GPIO pins divided into two 8-bit ports (**GPIOA** and **GPIOB**).

Unlike quasi-bidirectional expanders (such as PCF8574), the MCP23017 contains explicit direction registers (`IODIRA`/`IODIRB`), internal $100\text{ k}\Omega$ pull-up resistors, input polarity inversion, and two configurable interrupt pins (`INTA`/`INTB`) with change-of-state detection.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VDD`)** | 1.8 V to 5.5 V DC |
| **I2C bus clock speed** | 100 kHz (Standard), 400 kHz (Fast), 1.7 MHz (High-Speed) |
| **I/O ports** | 16 General-Purpose I/O pins (`GPA0`–`GPA7`, `GPB0`–`GPB7`) |
| **Maximum current per pin** | 25 mA sink or source |
| **Maximum total current** | 125 mA ($V_{SS}$) / 150 mA ($V_{DD}$) |
| **I2C slave address** | `0x20` to `0x27` (selectable via hardware pins `A0`, `A1`, `A2`) |
| **Interrupt outputs** | 2 Open-drain / Push-pull interrupt pins (`INTA`, `INTB`) |

## Pinout

### 28-Pin DIP / SOIC Package

```
           ┌──────────┐
    GPB0 ──│ 1     28 │── GPA7
    GPB1 ──│ 2     27 │── GPA6
    GPB2 ──│ 3     26 │── GPA5
    GPB3 ──│ 4     25 │── GPA4
    GPB4 ──│ 5     24 │── GPA3
    GPB5 ──│ 6     23 │── GPA2
    GPB6 ──│ 7     22 │── GPA1
    GPB7 ──│ 8     21 │── GPA0
     VDD ──│ 9     20 │── INTA
     VSS ──│ 10    19 │── INTB
      NC ──│ 11    18 │── RESET*
     SCL ──│ 12    17 │── A2
     SDA ──│ 13    16 │── A1
      NC ──│ 14    15 │── A0
           └──────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1–8 | `GPB0`–`GPB7` | Digital I/O | Port B general purpose I/O pins |
| 9 | `VDD` | Power | Positive supply voltage (+1.8 V to +5.5 V DC) |
| 10 | `VSS` | Power | Ground (0 V) |
| 12 | `SCL` | Digital Input | I2C Serial Clock input |
| 13 | `SDA` | Digital I/O | I2C Serial Data line |
| 15–17 | `A0`–`A2` | Digital Input | Hardware address inputs |
| 18 | `RESET` | Digital Input | Active-LOW hardware reset pin (Must be tied to VDD for normal run) |
| 19–20 | `INTB`, `INTA` | Digital Output | Port B & Port A interrupt output pins |
| 21–28 | `GPA0`–`GPA7` | Digital I/O | Port A general purpose I/O pins |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 1.8 | 3.3 / 5.0 | 5.5 | V | DC |
| Standby Current | $I_{DDSTB}$ | — | 1.0 | 5.0 | µA | $V_{DD} = 5.5\text{ V}$, $I_{IO} = 0$ |
| Operating Current | $I_{DD}$ | — | 100 | 1000 | µA | $f_{SCL} = 400\text{ kHz}$ |
| Input Low Voltage | $V_{IL}$ | $V_{SS}$ | — | $0.2 V_{DD}$ | V | |
| Input High Voltage | $V_{IH}$ | $0.8 V_{DD}$ | — | $V_{DD}$ | V | |
| Output Low Voltage | $V_{OL}$ | — | — | 0.6 | V | $I_{OL} = 8.5\text{ mA}$, $V_{DD} = 5.0\text{ V}$ |
| Output High Voltage | $V_{OH}$ | $V_{DD} - 0.7$ | — | — | V | $I_{OH} = -3.0\text{ mA}$, $V_{DD} = 5.0\text{ V}$ |
| Internal Pull-up Resistance | $R_{PU}$ | 50 | 100 | 150 | kΩ | Configurable via `GPPUA`/`GPPUB` |

## Key Registers (IOCON.BANK = 0 default)

| Address (Port A / B) | Register | Access | Description |
|---|---|---|---|
| `0x00` / `0x01` | `IODIRA` / `IODIRB` | R/W | I/O Direction (`1` = Input, `0` = Output; Reset default: `0xFF`) |
| `0x02` / `0x03` | `IPOLA` / `IPOLB` | R/W | Input Polarity Inversion (`1` = Inverted logic) |
| `0x04` / `0x05` | `GPINTENA` / `GPINTENB` | R/W | Interrupt-on-Change Enable (`1` = Enabled) |
| `0x06` / `0x07` | `DEFVALA` / `DEFVALB` | R/W | Default Compare Register for Interrupts |
| `0x0C` / `0x0D` | `GPPUA` / `GPPUB` | R/W | Pull-up Resistor Enable (`1` = Enable $100\text{ k}\Omega$ pull-up) |
| `0x12` / `0x13` | `GPIOA` / `GPIOB` | R/W | Port Register (Read input values / Write output latches) |
| `0x14` / `0x15` | `OLATA` / `OLATB` | R/W | Output Latch Register |

## Wiring

| MCP23017 Pin | → | Microcontroller (Arduino / ESP32) | Notes |
|---|---|---|---|
| `VDD` (Pin 9) | | `5V` (or `3.3V`) | Power supply |
| `VSS` (Pin 10) | | `GND` | Ground |
| `RESET` (Pin 18) | | `VDD` (via 10kΩ pull-up) | **Must be pulled HIGH to prevent hardware resets** |
| `SDA` (Pin 13) | | `SDA` | I2C Data line |
| `SCL` (Pin 12) | | `SCL` | I2C Clock line |
| `A0`, `A1`, `A2` | | `GND` | Tie to GND for base address `0x20` |

> [!WARNING]
> Floating RESET Pin Failure:
> Pin 18 (`RESET`) is active-LOW. Leaving `RESET` unconnected/floating causes random device resets and lost configuration state. Always connect Pin 18 to `VDD` directly or through a $10\text{ k}\Omega$ resistor.

## Common mistakes

- **Leaving RESET pin floating:** Causes erratic dropouts on the I2C bus.
- **Forgetting IODIR default is INPUT:** All pins power up as inputs (`0xFF`). Pins intended as outputs must be explicitly cleared to `0` in `IODIRA`/`IODIRB` before writing values to `GPIOA`/`GPIOB`.
- **Mixing up MCP23017 (I2C) and MCP23S17 (SPI):** MCP23017 uses I2C; MCP23S17 uses SPI. Their pinouts and protocol commands are not interchangeable.

## Notes

- Up to 8 MCP23017 chips can share the same I2C bus by configuring address pins `A0`–`A2` (`0x20` to `0x27`).
