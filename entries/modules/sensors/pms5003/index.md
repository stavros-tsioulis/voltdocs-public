## Overview

The **PMS5003** (and its smaller counterpart PMS7003) is a digital laser-scattering particulate matter (PM) air quality sensor manufactured by Plantower. It uses a semiconductor laser diode, a low-noise internal fan, and a photodetector to count microscopic airborne dust particles down to **0.3 µm** in diameter.

It streams real-time mass concentration values ($\mu\text{g/m}^3$) for **PM1.0**, **PM2.5**, and **PM10** over a 9600-baud UART serial interface, serving as standard hardware for indoor/outdoor air quality monitors (ESPHome `pmsx003` integration, PurpleAir monitors, Home Assistant).

## Quick reference

| | |
|---|---|
| **Operating Voltage (`VCC`)** | 4.5 V to 5.5 V DC (5.0 V nominal for fan motor) |
| **UART Logic Level** | 3.3 V TTL |
| **Particle Detection Range** | 0.3 µm to 10 µm |
| **PM2.5 Measurement Range** | 0 to 500 µg/m³ (up to 1000 µg/m³ max) |
| **Counting Efficiency** | 50% @ 0.3 µm, 98% @ $\ge 0.5\text{ }\mu\text{m}$ |
| **Response Time** | $\le 1\text{ second}$ real-time update rate |
| **Default Baud Rate** | 9600 bps (`9600,N,8,1`) |
| **Operating Current** | ~100 mA (fan running), $< 200\text{ }\mu\text{A}$ standby |

## Pinout

### Standard 10-Pin 1.27mm Connector (PMS5003)

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power Input | Supply voltage (+4.5 V to +5.5 V DC) |
| 2 | `VCC` | Power Input | Supply voltage (+4.5 V to +5.5 V DC) |
| 3 | `GND` | Power | Ground (0 V) |
| 4 | `GND` | Power | Ground (0 V) |
| 5 | `RESET` | Digital Input | Active-LOW Hardware Reset pin (pull HIGH for normal operation) |
| 6 | `NC` | Not Connected | Unused |
| 7 | `RX` | Digital Input | UART Receive data (3.3V logic level) |
| 8 | `NC` | Not Connected | Unused |
| 9 | `TX` | Digital Output | UART Transmit data (3.3V logic level output, 9600 baud) |
| 10 | `SET` | Digital Input | Sleep control pin (`HIGH` = Normal mode, `LOW` = Standby mode fan OFF) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 4.5 | 5.0 | 5.5 | V | DC |
| Active Supply Current | $I_{CC}$ | — | 100 | 120 | mA | Fan & laser active |
| Standby Current | $I_{STBY}$ | — | 100 | 200 | µA | $SET = LOW$ |
| PM2.5 Consistency | $\Delta PM2.5$ | -10 | — | +10 | % | $@ 100\text{ to } 500\text{ }\mu\text{g/m}^3$ |
| Laser Life Span | $MTBF$ | 3 | — | 5 | years | Continuous operation |

## UART Packet Frame (32 Bytes Data Frame)

The sensor streams a 32-byte binary packet every 1 second starting with header bytes `0x42 0x4D`:

| Byte Index | Field | Description |
|---|---|---|
| 0, 1 | Header | `0x42 0x4D` (`'BM'`) |
| 2, 3 | Frame Length | `0x00 0x1C` (28 bytes payload) |
| 4, 5 | **PM1.0 Standard** | PM1.0 concentration ($\mu\text{g/m}^3$, CF=1 factory standard) |
| 6, 7 | **PM2.5 Standard** | PM2.5 concentration ($\mu\text{g/m}^3$, CF=1 factory standard) |
| 8, 9 | **PM10 Standard** | PM10 concentration ($\mu\text{g/m}^3$, CF=1 factory standard) |
| 10, 11 | **PM1.0 Atmospheric** | PM1.0 concentration under atmospheric environment ($\mu\text{g/m}^3$) |
| 12, 13 | **PM2.5 Atmospheric** | **PM2.5 concentration under atmospheric environment ($\mu\text{g/m}^3$)** |
| 14, 15 | **PM10 Atmospheric** | **PM10 concentration under atmospheric environment ($\mu\text{g/m}^3$)** |
| 30, 31 | Checksum | Sum of Bytes 0 to 29 (16-bit integer check) |

## Wiring

| PMS5003 Pin | → | Microcontroller (Arduino / ESP32) | Notes |
|---|---|---|---|
| `VCC` (Pins 1 & 2) | | `5V` | **Must be 5V DC for internal fan** |
| `GND` (Pins 3 & 4) | | `GND` | Ground |
| `TX` (Pin 9) | | `RX` (e.g. GPIO16 / D2 for SoftwareSerial) | 3.3V logic output |
| `RX` (Pin 7) | | `TX` (e.g. GPIO17 / D3 for SoftwareSerial) | 3.3V logic input |
| `SET` (Pin 10) | | `3.3V` (or GPIO Pin) | Pull HIGH to enable fan/laser |
| `RESET` (Pin 5) | | `3.3V` (or GPIO Pin) | Pull HIGH for normal operation |

## Common mistakes

- **Powering with 3.3V:** Microcontroller 3.3V power rails cannot power the 5V fan motor. The fan will stall or fail to draw air across the laser chamber.
- **Vertical Orientation Mounting:** The PMS5003 air intake/exhaust vents MUST be mounted horizontally on the side of enclosures to prevent dust accumulation inside the optical cavity.
- **Running continuous fan non-stop in battery projects:** The laser diode and fan wear out over 3 years of continuous operation. Use the `SET` pin to toggle sleep mode (fan OFF) and wake the sensor for 30 seconds before taking periodic readings.

## Notes

- Fully integrated into ESPHome via `platform: pmsx003` component.
