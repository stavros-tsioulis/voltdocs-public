## Overview

The **SCD40** and **SCD41** are next-generation, ultra-miniature photoacoustic $\text{CO}_2$ sensors manufactured by Sensirion. Occupying a footprint of just **$10.1 \times 10.1 \times 6.5\text{ mm}$** ($101\text{ mm}^3$ volume—5 times smaller than traditional NDIR sensors like SCD30), they measure true carbon dioxide concentration alongside ambient temperature and relative humidity over an I2C interface.

Using Sensirion's **PASens® Photoacoustic Sensing technology**, infrared emitter pulses excite $\text{CO}_2$ molecules inside a tiny acoustic measurement cell, creating pressure oscillations detected by a MEMS microphone. The **SCD40** is optimized for indoor air quality ($400\text{ to }2000\text{ ppm}$), while the **SCD41** expands the measurement range up to **40,000 ppm** and adds single-shot low-power modes.

## Quick reference

| | |
|---|---|
| **Operating Voltage (`VDD`)** | 2.4 V to 5.5 V DC (3.3 V or 5.0 V nominal) |
| **SCD40 Range ($\text{CO}_2$)** | 400 ppm to 2000 ppm |
| **SCD41 Range ($\text{CO}_2$)** | 400 ppm to 40,000 ppm |
| **Accuracy ($\text{CO}_2$)** | $\pm (40\text{ ppm} + 5\%\text{ of reading})$ |
| **Temperature Range / Accuracy** | $-10^\circ\text{C}$ to $+60^\circ\text{C}$ ($\pm 0.8\text{ }^\circ\text{C}$ accuracy) |
| **Relative Humidity Range / Accuracy** | 0% to 100% RH ($\pm 6\%\text{ RH}$ accuracy) |
| **Communication Interface** | I2C (fixed slave address `0x62`, up to 100 kHz) |
| **Single-Shot Low Power Mode (SCD41 only)** | $3.2\text{ mA}$ average current ($110\text{ }\mu\text{A}$ at 5-minute intervals) |

## Comparison: SCD40 vs SCD41

| Feature | SCD40 | SCD41 |
|---|---|---|
| **Target Application** | Indoor Air Quality / HVAC | Industrial / Medical / Low-power IoT |
| **$\text{CO}_2$ Range** | 400 to 2000 ppm | **400 to 40,000 ppm** |
| **Specified Accuracy Range** | 400 to 2000 ppm | 400 to 5000 ppm ($\pm 40\text{ ppm} + 5\%$) |
| **Continuous Measurement Mode** | Yes (5s interval) | Yes (5s interval) |
| **Low Power Periodic Mode** | Yes (30s interval, ~3.2 mA) | Yes (30s interval, ~3.2 mA) |
| **Single-Shot Measurement Command** | No | **Yes (`0x219D` for low power battery operation)** |

## Pinout

### Standard 5-Pin Breakout Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VDD` | Power Input | Supply voltage (+2.4 V to +5.5 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SCL` | Digital Input | I2C Serial Clock input line |
| 4 | `SDA` | Digital I/O | I2C Serial Data line |
| 5 | `CAD` | Digital Input | I2C Address select (tie to GND) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 2.4 | 3.3 / 5.0 | 5.5 | V | DC |
| Peak Current | $I_{PEAK}$ | — | 205 | 230 | mA | During 5 ms emitter pulse |
| Average Current (Continuous 5s) | $I_{AVG}$ | — | 18 | 22 | mA | $V_{DD} = 3.3\text{ V}$ |
| Average Current (Low Power 30s) | $I_{LP}$ | — | 3.2 | 4.0 | mA | 30s periodic mode |
| Single Shot Power Consumption | $E_{shot}$ | — | 35 | — | mJ | SCD41 per measurement |
| I2C Clock Rate | $f_{SCL}$ | — | — | 100 | kHz | Standard Mode |

## Command Set (I2C Address `0x62`)

Each command consists of a 16-bit command code. Data responses include a CRC-8 byte per 2 bytes of data:

| Command Hex | Command Name | Description |
|---|---|---|
| `0x21B1` | `start_periodic_measurement` | Starts 5-second periodic measurement execution |
| `0xEC05` | `read_measurement` | Read $\text{CO}_2$ (ppm), Temp (°C), and Humidity (%RH) |
| `0x3920` | `stop_periodic_measurement` | Stops periodic measurement mode |
| `0x219D` | `measure_single_shot` | **(SCD41 Only)** Executes a single 5-second measurement |
| `0x241D` | `perform_forced_recalibration` | Perform manual calibration ($400\text{ to }5000\text{ ppm}$) |
| `0x2416` | `set_automatic_self_calibration` | Enable / Disable Automatic Self-Calibration (ASC) |

## Wiring

| SCD4x Breakout Pin | → | Microcontroller (Arduino Uno / ESP32) |
|---|---|---|
| `VDD` | | `3.3V` or `5V` (Must support 205 mA peak pulses) |
| `GND` | | `GND` |
| `SCL` | | `SCL` (A5 on Uno, GPIO22 on ESP32) |
| `SDA` | | `SDA` (A4 on Uno, GPIO21 on ESP32) |

> [!WARNING]
> Photoacoustic Pulse Peak Current:
> During photoacoustic IR emitter pulses, the SCD4x draws **up to 205 mA** peak current for several milliseconds. Ensure the $V_{DD}$ supply line is decoupled with a $10\text{ }\mu\text{F}$ to $47\text{ }\mu\text{F}$ capacitor on breakout boards powered by weak 3.3V LDOs.

## Common mistakes

- **Sending I2C commands while measurement is running:** Modifying settings (e.g., setting temperature offsets or recalibrating) requires sending `stop_periodic_measurement` (`0x3920`) first and waiting 500 ms.
- **Reading data before Data Ready:** Software should poll `get_data_ready_status` (`0xE4B8`) before reading data bytes to avoid receiving stale or corrupted readings.
- **Enclosing the acoustic port in airtight foam:** Photoacoustic sensing relies on acoustic pressure pulses. Encapsulating the SCD4x in airtight potting or dense acoustic foam dampens pressure waves and ruins readings.

## Notes

- Modern gold standard for ESPHome `scd4x` air quality sensors and smart home indoor environmental monitors.
