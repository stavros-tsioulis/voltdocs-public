## Overview

The **DHT22** (also sold as **AM2302**) is a high-precision digital temperature and humidity sensor manufactured by Aosong Electronics. It serves as an accuracy upgrade to the basic DHT11, offering wider measurement ranges, 16-bit high-resolution output, sub-zero temperature capability, and decimal precision.

It incorporates a capacitive humidity sensor element, a high-precision NTC thermistor, and a 8-bit microcontroller that outputs a calibrated 40-bit digital signal over a single-bus interface.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 6.0 V DC (5 V recommended) |
| **Humidity range** | 0% to 100% RH ($\pm 2.0\%\text{ RH}$ accuracy) |
| **Temperature range** | $-40^\circ\text{C}$ to $+80^\circ\text{C}$ ($\pm 0.5\text{ }^\circ\text{C}$ accuracy) |
| **Resolution** | 16-bit (0.1% RH, 0.1 °C resolution) |
| **Sampling period** | 2.0 seconds (do not sample faster than 0.5 Hz) |
| **Interface** | Custom Single-Bus 1-Wire protocol |
| **Active measuring current** | 1.0 mA to 1.5 mA |

## Pinout

### 4-Pin Single In-line Package / 3-Pin Breakout

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+3.3 V to +6.0 V DC) |
| 2 | `DATA` | Digital I/O | Single-bus bidirectional data line (requires 1kΩ–10kΩ pull-up) |
| 3 | `NC` | Not Connected | Do not connect |
| 4 | `GND` | Power | Ground (0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 3.3 | 5.0 | 6.0 | V | DC |
| Measuring Current | $I_{DD}$ | 1.0 | 1.5 | 2.1 | mA | During data transmission |
| Standby Current | $I_{SB}$ | 40 | 50 | 60 | µA | Between measurements |
| Humidity Measuring Range | $RH$ | 0 | — | 100 | % RH | |
| Humidity Accuracy | $\Delta RH$ | -2.0 | — | +2.0 | % RH | At $25^\circ\text{C}$ |
| Humidity Resolution | $RH_{res}$ | — | 0.1 | — | % RH | 16-bit data |
| Temp Measuring Range | $T$ | -40 | — | 80 | °C | |
| Temp Accuracy | $\Delta T$ | -0.5 | — | +0.5 | °C | |
| Temp Resolution | $T_{res}$ | — | 0.1 | — | °C | 16-bit data |
| Data Response Time | $t_{read}$ | — | 2.0 | — | s | Minimum interval between reads |

## Communication protocol

The DHT22 uses a single-bus protocol sending a 40-bit (5-byte) frame. Unlike the DHT11, both humidity and temperature values are 16-bit signed values multiplied by 10:

$$\text{Data Packet} = \underbrace{\text{Humidity High} \ll 8 \mid \text{Humidity Low}}_{\text{16-bit RH } \times 10} + \underbrace{\text{Temp High} \ll 8 \mid \text{Temp Low}}_{\text{16-bit Temp } \times 10} + \underbrace{\text{Checksum}}_{\text{Byte 4}}$$

- **Negative Temperatures:** If bit 15 (MSB) of the Temperature word is `1`, the temperature is negative. Clear bit 15 and multiply by -0.1.
- **Checksum Formula:** $\text{Byte 4} = (\text{Byte 0} + \text{Byte 1} + \text{Byte 2} + \text{Byte 3}) \pmod{256}$.
- **Timing:** MCU pulls `DATA` LOW for **1 to 10 ms**, then releases. DHT22 responds with 80 µs LOW + 80 µs HIGH, followed by 40 data bits (50 µs LOW baseline; 26 µs HIGH = `0`, 70 µs HIGH = `1`).

## Wiring

| DHT22 / AM2302 | → | Microcontroller (Arduino Uno / ESP32) | Notes |
|---|---|---|---|
| `VCC` | | `5V` (or `3.3V`) | Power supply |
| `DATA` | | Digital GPIO Pin (e.g. GPIO4) | Requires $4.7\text{ k}\Omega$–$10\text{ k}\Omega$ pull-up resistor to VCC |
| `GND` | | `GND` | Ground |

## Common mistakes

- **Polling faster than 0.5 Hz (every 2 seconds):** The DHT22 requires 2 seconds between measurements to allow internal sensor element stabilization. Requesting data too quickly results in reading errors or internal self-heating.
- **Using DHT11 driver code for DHT22:** While the physical signaling waveform is identical, the data payload decoding differs. DHT11 sends 8-bit integer bytes, whereas DHT22 sends 16-bit values with decimal multipliers.
- **Inadequate pull-up resistor on long wires:** For cables longer than 5 meters, use a $1\text{ k}\Omega$ to $2.2\text{ k}\Omega$ pull-up resistor to ensure fast signal rise times.

## Notes

- AM2302 is the module version of the DHT22, often pre-wired with flexible lead wires and an internal pull-up resistor.
