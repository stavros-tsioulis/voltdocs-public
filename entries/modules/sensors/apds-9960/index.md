## Overview

The **APDS-9960** is an integrated 4-in-1 digital optical sensor manufactured by Broadcom (formerly Avago Technologies). It combines **3D gesture recognition** (up, down, left, right, near, far swipes), **infrared proximity detection**, **ambient light sensing (ALS)**, and **RGB color sensing** into a single compact package communicating over an I2C interface.

It features four directional photodiode sensors (North, South, East, West) and an integrated IR LED emitter to detect hand motion directions up to $100\text{ mm}$ away without physical touch.

## Quick reference

| | |
|---|---|
| **Operating Voltage (`VCC`)** | 2.4 V to 3.6 V DC (3.3 V nominal) |
| **IR LED Supply (`VL` / Breakout VCC)** | 3.0 V to 4.5 V DC |
| **Proximity Range** | $10\text{ mm to }100\text{ mm}$ |
| **Gesture Directions** | UP, DOWN, LEFT, RIGHT, NEAR, FAR |
| **Color Channels** | Red, Green, Blue, and Clear (unfiltered) |
| **Communication Interface** | I2C (fixed address `0x39`, up to 400 kHz) |
| **Interrupt Output** | Active-LOW hardware interrupt (`INT`) |
| **Operating Current** | 100 µA active, 1 µA sleep mode |

## Pinout

### Standard 5-Pin / 6-Pin Breakout Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+2.4 V to +3.6 V DC, 3.3V recommended) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SDA` | Digital I/O | I2C Serial Data line |
| 4 | `SCL` | Digital Input | I2C Serial Clock input |
| 5 | `INT` | Digital Output | Active-LOW Interrupt pin (alerts MCU on gesture or proximity event) |
| 6 | `VL` | Power | Power for internal IR LED (connected to VCC on 3.3V breakouts) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (IC) | $V_{DD}$ | 2.4 | 3.0 | 3.6 | V | DC |
| Supply Voltage (IR LED) | $V_{LEDA}$ | 3.0 | 3.8 | 4.5 | V | DC |
| Active Supply Current | $I_{DD}$ | — | 100 | 250 | µA | ALS / Proximity active |
| IR LED Peak Drive Current | $I_{LED}$ | — | 100 | 200 | mA | Configurable in `CONTROL` reg |
| Gesture Range | $d_{gest}$ | 10 | 50 | 100 | mm | Hand gesture distance |
| ADC Resolution | $RES$ | — | 16 | — | bits | RGBC / Proximity ADCs |

## Operating modes & Register map

### Operating Modes (`ENABLE` Register `0x80`)

- **`PON` (Bit 0):** Power ON.
- **`AEN` (Bit 1):** ALS / Color sensing enable.
- **`PEN` (Bit 2):** Proximity sensing enable.
- **`GEN` (Bit 6):** Gesture sensing engine enable.

### Key Registers

| Address | Register | Description |
|---|---|---|
| `0x80` | `ENABLE` | Enable register for Power, ALS, Proximity, and Gesture engines |
| `0x81` | `ATIME` | ALS ADC integration time ($2.78\text{ ms}$ to $712\text{ ms}$) |
| `0x8F` | `PROX` | 8-bit Proximity ADC data output |
| `0x92` | `ID` | Returns `0xAB` (APDS-9960 identification byte) |
| `0x94`..`0x9B` | `CDATAL`..`BDATAH` | 16-bit RGBC color data registers (Clear, Red, Green, Blue) |
| `0xFC`..`0xFF` | `GFIFO_U`..`GFIFO_W` | Gesture FIFO directional photodiode datasets (Up, Down, Left, Right) |

## Wiring

| APDS-9960 Breakout Pin | → | Microcontroller (Arduino / ESP32) |
|---|---|---|
| `VCC` | | `3.3V` |
| `GND` | | `GND` |
| `SDA` | | `SDA` (A4 on Uno, GPIO21 on ESP32) |
| `SCL` | | `SCL` (A5 on Uno, GPIO22 on ESP32) |
| `INT` | | GPIO Pin with Interrupt support (e.g. D2 / GPIO4) |

> [!NOTE]
> Hardware Interrupt Pin Recommended:
> For gesture recognition, connecting the `INT` pin to a hardware interrupt line on the MCU is strongly recommended. Polling the I2C bus continuously for gesture events can miss fast hand swipes.

## Common mistakes

- **Powering from 5.0V:** Connecting 5V directly to `VCC` exceeds the 3.6V maximum rating and damages the photodiode ASIC.
- **Obstructing optical field-of-view:** Placing dark tinted plastic or non-IR-transparent glass over the sensor blocks the 850 nm IR LED pulses and breaks gesture detection.
- **Swiping too far away:** Gesture detection requires hand swipes within **50 mm to 100 mm** ($2\text{ to }4\text{ inches}$) directly above the sensor package.

## Notes

- Color sensing outputs 16-bit raw counts for Clear, Red, Green, and Blue. Normalize RGBC counts to calculate RGB color coordinates or lux intensity.
