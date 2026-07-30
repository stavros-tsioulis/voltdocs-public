## Overview

The **DS18B20** is a 1-Wire digital temperature sensor manufactured by Maxim Integrated (now Analog Devices). It communicates over a single data line plus ground (1-Wire bus protocol), requiring only one microcontroller pin to interface with multiple sensors distributed over a large area.

Each DS18B20 has a unique 64-bit factory-lasered ROM ID code, allowing multiple DS18B20 sensors to coexist on the same 1-Wire bus. The sensor offers user-configurable measurement resolution from 9 to 12 bits (corresponding to $0.5\text{ }^\circ\text{C}$ down to $0.0625\text{ }^\circ\text{C}$ increments).

## Quick reference

| | |
|---|---|
| **Operating voltage (`VDD`)** | 3.0 V – 5.5 V (Supports Parasite Power mode on `DQ`) |
| **Measurement range** | -55 °C to +125 °C (-67 °F to +257 °F) |
| **Accuracy** | $\pm 0.5\text{ }^\circ\text{C}$ (from -10 °C to +85 °C) |
| **Resolution** | Configurable 9, 10, 11, or 12 bits ($0.5\text{ }^\circ\text{C}$ to $0.0625\text{ }^\circ\text{C}$) |
| **Interface** | 1-Wire (Dallas/Maxim single-wire serial interface) |
| **Conversion time** | 93.75 ms (9-bit) to 750 ms (12-bit max) |

## Pinout

### TO-92 Package & Waterproof Probe Cable

| Pin / Wire Color | Name | Type | Description |
|---|---|---|---|
| 1 (Left / Black) | `GND` | Power | Ground (0 V) |
| 2 (Center / Yellow or White) | `DQ` | Digital I/O | 1-Wire Data Input/Output (requires 4.7 kΩ pull-up to VDD) |
| 3 (Right / Red) | `VDD` | Power | Optional external power supply (GND for parasite power mode) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | `VDD` | 3.0 | 5.0 | 5.5 | V | Local power mode |
| Standby Current | `DDS` | — | 750 | 1000 | nA | $V_{DD} = 5.0\text{ V}$ |
| Active Current | `DD` | — | 1.0 | 1.5 | mA | During temperature conversion |
| Temperature Accuracy | $T_{acc}$ | — | $\pm 0.5$ | $\pm 2.0$ | °C | $-10\text{ }^\circ\text{C}$ to $+85\text{ }^\circ\text{C}$ |
| 12-Bit Conversion Time | $t_{CONV}$ | — | 400 | 750 | ms | 12-bit resolution mode |
| DQ Pull-Up Resistor | $R_{PUP}$ | 1.5 | 4.7 | 10.0 | kΩ | Bus pull-up resistor |

## 1-Wire protocol & scratchpad commands

Communication with the DS18B20 follows a strict sequence:
1. **Reset pulse & Presence detect** (Master pulls DQ LOW for $\ge 480\text{ }\mu\text{s}$, slave responds with presence pulse).
2. **ROM Command** (`0xCC` Skip ROM for single sensor, `0x55` Match ROM for multiple sensors).
3. **Function Command** (e.g. `0x44` Convert T, `0xBE` Read Scratchpad).

### Scratchpad memory map

The DS18B20 scratchpad consists of 9 bytes of SRAM:

| Byte | Register | Description |
|---|---|---|
| 0 | `Temperature LSB` | Low byte of temperature value ($2^{-4} = 0.0625\text{ }^\circ\text{C}/\text{LSB}$) |
| 1 | `Temperature MSB` | High byte of temperature value (sign bits) |
| 2 | `TH Register` | High temperature alarm trigger byte (EEPROM backed) |
| 3 | `TL Register` | Low temperature alarm trigger byte (EEPROM backed) |
| 4 | `Configuration` | Resolution setting (Bits 6:5 — `00`: 9-bit, `01`: 10-bit, `10`: 11-bit, `11`: 12-bit) |
| 5–7 | `Reserved` | Factory reserved bytes |
| 8 | `CRC` | CRC byte calculated over bytes 0 through 7 ($X^8 + X^5 + X^4 + 1$) |

### Temperature formula

The 16-bit temperature register stores two's-complement temperature in increments of $0.0625\text{ }^\circ\text{C}$:

$$\text{Temperature }(^\circ\text{C}) = \frac{\text{Raw 16-bit Value}}{16}$$

## Wiring

### Standard Local Power Setup

| DS18B20 | → | Microcontroller (Arduino / ESP32) | Notes |
|---|---|---|---|
| `GND` (Black) | | `GND` | Ground |
| `DQ` (Yellow) | | Digital GPIO Pin | Connected to GPIO; **4.7 kΩ pull-up resistor** to $V_{DD}$ |
| `VDD` (Red) | | `3.3V` or `5V` | External Power Supply |

> [!WARNING]
> A pull-up resistor (typically **4.7 kΩ**) between the `DQ` data line and `VDD` is mandatory. Without this pull-up resistor, the 1-Wire bus remains floating and communication will fail completely.

## Common mistakes

- **Missing 4.7 kΩ pull-up resistor:** The 1-Wire bus is open-drain and cannot function without an external pull-up resistor connected between `DQ` and `VDD`.
- **Not waiting for conversion to complete:** At 12-bit resolution, a temperature conversion takes up to 750 ms. Attempting to read the scratchpad before this delay completes returns stale or invalid data ($85\text{ }^\circ\text{C}$ default power-on value).
- **Parasite power mode current starvation:** When using parasite power mode (where `VDD` is tied to `GND`), the data line must be held strongly HIGH during conversion to supply sufficient current.

## Notes

- **Power-On Reset Value:** The DS18B20 scratchpad initializes to $+85\text{ }^\circ\text{C}$ (`0x0550`) upon power-up. If your software reads exactly $85.0\text{ }^\circ\text{C}$, it usually indicates a power cycle occurred without issuing a new `0x44` Convert T command.
