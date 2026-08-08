## Overview

The **NEO-M8N** is a concurrent GNSS (Global Navigation Satellite System) receiver module manufactured by u-blox. Unlike older single-constellation receivers (such as the NEO-6M), the NEO-M8N can simultaneously receive and track multiple satellite constellations—including **GPS**, **GLONASS**, **BeiDou**, and **QZSS**—delivering higher positioning accuracy ($2.5\text{ m}$ CEP), faster Time-To-First-Fix (TTFF), and superior signal immunity in urban canyons.

It features onboard SQI flash memory for user configuration storage, an active antenna supervisor, low-noise amplifier (LNA), and supports update rates up to **10 Hz**. It is widely used in flight controllers (ArduPilot, INAV, Betaflight), vehicle trackers, and outdoor IoT loggers.

## Quick reference

| | |
|---|---|
| **Module VCC** | 3.3 V to 5.0 V DC (onboard LDO) |
| **Chip VCC** | 2.7 V to 3.6 V DC |
| **Constellations** | Concurrent GPS + GLONASS + BeiDou + QZSS + SBAS (WAAS/EGNOS) |
| **Position accuracy** | 2.5 m CEP (Autonomous) / 2.0 m CEP (SBAS augmented) |
| **Tracking sensitivity** | -167 dBm |
| **Update rate** | Up to 10 Hz (Concurrent GNSS) |
| **Default UART config** | 9600 baud (configurable up to 921600 baud), NMEA 0183 protocol |
| **Time-To-First-Fix (TTFF)** | Cold start: 26 s / Hot start: 1 s |

## Pinout

### Standard 5-Pin Breakout Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `TXD` / `TX` | Digital Output | UART Transmit data line (3.3V TTL logic level) |
| 4 | `RXD` / `RX` | Digital Input | UART Receive data line (3.3V TTL logic level) |
| 5 | `PPS` / `TP` | Digital Output | Time Pulse 1-PPS output (1 pulse-per-second strobe when locked) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Chip Supply Voltage | $V_{CC}$ | 2.7 | 3.0 | 3.6 | V | DC |
| Tracking Current | $I_{track}$ | — | 67 | 85 | mA | Concurrent GPS + GLONASS |
| Max Velocity Limit | $v_{max}$ | — | 500 | — | m/s | $1800\text{ km/h}$ |
| Max Altitude Limit | $h_{max}$ | — | 50000 | — | m | 50 km (COCOM limit) |
| Velocity Accuracy | $v_{acc}$ | — | 0.05 | — | m/s | |
| Heading Accuracy | $\psi_{acc}$ | — | 0.3 | — | ° | Motion dependent |

## Communication NMEA Sentences & UBX Binary Protocol

The NEO-M8N transmits standard NMEA-0183 ASCII text sentences at 9600 baud by default:
- **`$GNRMC` / `$GPRMC`:** Recommended Minimum Specific GNSS Data (Latitude, Longitude, Speed, Heading, Date).
- **`$GNGGA` / `$GPGGA`:** Global Positioning System Fix Data (Fix quality, Number of satellites, Altitude).

It also supports u-blox's proprietary **UBX binary protocol** via the *u-center* software tool for high-throughput 10 Hz binary data streaming and custom constellation selection.

## Wiring

| NEO-M8N Module Pin | → | Microcontroller (Arduino / ESP32 / Flight Controller) |
|---|---|---|
| `VCC` | | `5V` (or `3.3V`) |
| `GND` | | `GND` |
| `TXD` | | `RX` (e.g. GPIO16 / Serial2 RX) |
| `RXD` | | `TX` (e.g. GPIO17 / Serial2 TX) |
| `PPS` | | GPIO Pin (optional 1-PPS time synchronization input) |

> [!NOTE]
> Active Ceramic Patch Antenna Requirement:
> GNSS satellite signals are extremely weak indoors. Always connect the external active ceramic patch antenna via the U.FL / IPEX connector and position the antenna outdoors under a clear view of the sky for initial satellite acquisition.

## Common mistakes

- **Testing indoors:** Testing the module indoors behind concrete or metallic roofs prevents satellite lock. The onboard LED will flash `1 PPS` only when a valid 3D position fix is acquired outdoors.
- **Inverted RX/TX lines:** Connecting module `TXD` to microcontroller `TX` instead of `RX`.
- **Forgetting baud rate increase for 10 Hz updates:** Transmitting NMEA sentences at 10 Hz requires increasing the UART baud rate to **115200 baud** using UBX commands (9600 baud is limited to ~1 Hz update rate due to serial bandwidth limits).

## Notes

- The NEO-M8N contains onboard non-volatile SQI flash memory, allowing custom settings (baud rate, rate limit, UBX output) to persist across power cycles.
