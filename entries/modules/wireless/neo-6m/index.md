## Overview

The **NEO-6M** is a standalone GPS (Global Positioning System) receiver module developed by u-blox. Built around the 50-channel u-blox 6 positioning engine, it outputs standard **NMEA 0183** sentences over a serial UART interface at a default baud rate of 9600 bps.

Breakout modules typically integrate a 3.3V low-dropout (LDO) regulator, an onboard EEPROM (for saving configuration settings permanently), a rechargeable MS621FE coin battery (for hot-start epoch memory retention), an IPEX (U.FL) antenna connector, and a external ceramic patch antenna.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 2.7 V – 3.6 V (Breakouts include 3.3V LDO for 3.0 V – 5.0 V input) |
| **Logic level (`RX`/`TX`)** | 3.3 V LVTTL (TX pin is 5V logic readable; RX needs divider from 5V MCU) |
| **Interface** | UART Serial (NMEA 0183 & binary UBX protocol) |
| **Default baud rate** | 9600 bps (configurable up to 115,200 bps) |
| **Update rate** | 1 Hz default (up to 5 Hz configurable) |
| **Position accuracy** | 2.5 m CEP (Autonomous) / 2.0 m (SBAS / EGNOS / WAAS) |
| **Time-To-First-Fix (TTFF)** | Cold Start: 27 s / Warm Start: 27 s / Hot Start: 1 s |

## Pinout

### Standard 4-Pin / 5-Pin Breakout Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (3.0 V to 5.0 V DC) |
| 2 | `RX` | Digital Input | Serial Data Input (3.3 V logic level; receives UBX/NMEA commands) |
| 3 | `TX` | Digital Output | Serial Data Output (3.3 V logic level; transmits NMEA sentence stream) |
| 4 | `GND` | Power | Ground (0 V) |
| 5 | `PPS` / `TP` | Digital Output | Time Pulse (Outputs 1 Hz pulse synchronized to GPS time when fix achieved) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Core Supply Voltage | $V_{DD}$ | 2.7 | 3.0 | 3.6 | V | IC raw supply |
| Breakout Supply Voltage | $V_{CC}$ | 3.0 | 5.0 | 5.5 | V | Onboard LDO input |
| Tracking Current | $I_{CC}$ | — | 47 | 67 | mA | Continuous tracking @ 3.0V |
| Tracking Sensitivity | $S_{track}$ | — | -161 | — | dBm | Continuous tracking |
| Navigation Update Rate | $f_{NAV}$ | — | 1 | 5 | Hz | Configurable via UBX |
| Max Velocity | $v_{max}$ | — | — | 500 | m/s | 1800 km/h |
| Max Altitude | $h_{max}$ | — | — | 50,000 | m | High altitude mode |

## NMEA 0183 output protocol

The module continuously transmits standard ASCII NMEA sentences over UART:

| NMEA Sentence | Description | Key Information Extracted |
|---|---|---|
| `$GPRMC` | Recommended Minimum Specific GPS Data | UTC Time, Status (A=Valid/V=Invalid), Latitude, Longitude, Speed (knots), Date |
| `$GPGGA` | Global Positioning System Fix Data | Time, Latitude, Longitude, Fix Quality (0=Invalid, 1=GPS fix), Satellite Count, Altitude |
| `$GPGSA` | GPS DOP and Active Satellites | Operating mode, Satellite PRNs used in fix, PDOP, HDOP, VDOP |
| `$GPGSV` | Satellites in View | Total satellites in view, PRN, Elevation, Azimuth, Signal-to-Noise Ratio (SNR) |

### $GPRMC Example Sentence Parsing

```
$GPRMC,123519.00,A,4807.038,N,01131.000,E,022.4,084.4,230326,003.1,W*6A
```
- `123519.00`: UTC Time (12:35:19.00)
- `A`: Status (`A` = Active / Valid Fix, `V` = Void / Invalid)
- `4807.038,N`: Latitude $48^\circ 07.038'$ North
- `01131.000,E`: Longitude $11^\circ 31.000'$ East
- `022.4`: Speed over ground (22.4 knots)
- `230326`: Date (23rd March 2026)

## Wiring

| NEO-6M Pin | :i-lucide-move-right: | Microcontroller (Arduino Uno / ESP32) | Notes |
|---|---|---|---|
| `VCC` | | `5V` or `3.3V` | Supply power to onboard LDO |
| `GND` | | `GND` | Ground |
| `TX` | | SoftwareSerial `RX` (e.g. Pin `4` / ESP32 `GPIO16`) | Module TX $\to$ MCU RX |
| `RX` | | SoftwareSerial `TX` (e.g. Pin `3` / ESP32 `GPIO17`) | Module RX $\leftarrow$ MCU TX (Use 1k/2k resistor divider from 5V MCU) |

> [!INFO]
> The `PPS` (Pulse Per Second) pin outputs a 100 ms duration pulse once per second, but **only after the module establishes a valid 3D position fix**. The onboard LED is tied to `PPS` and blinks once per second when a fix is locked.

## Common mistakes

- **Testing indoors:** GPS signals (1575.42 MHz) cannot penetrate concrete walls or metal roofs. Testing indoors will result in `Status = V` (Void fix) and zero satellites in view. Always test outdoors under open sky.
- **Connecting RX directly to 5V MCU pins:** The NEO-6M IO pins operate at 3.3V LVTTL. Connecting a 5V MCU TX line directly to NEO-6M `RX` without a voltage divider can damage the u-blox chip over time.
- **Confusing RX and TX wiring:** Serial connections are crossed: NEO-6M `TX` connects to MCU `RX`, and NEO-6M `RX` connects to MCU `TX`.

## Notes

- **Cold Start vs. Hot Start:** After power-up without battery backup, a cold start takes ~27–60 seconds to download the satellite ephemeris data (Almanac). If the backup battery has charged, a hot start takes ~1 second.
