## Overview

The **DHT11** is a basic, ultra-low-cost digital temperature and humidity sensor manufactured by Aosong Electronics (Guangzhou Aosong). It combines a resistive-type humidity measurement component and an NTC temperature measurement component connected to an 8-bit microcontroller.

It outputs calibrated 40-bit digital signals over a proprietary custom single-wire serial interface (`DATA`). It is standard in beginner Arduino and Raspberry Pi starter kits for basic environmental monitoring.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.0 V to 5.5 V DC (5 V recommended) |
| **Humidity range** | 20% to 90% RH ($\pm 5\%\text{ RH}$ accuracy) |
| **Temperature range** | $0^\circ\text{C}$ to $+50^\circ\text{C}$ ($\pm 2.0\text{ }^\circ\text{C}$ accuracy) |
| **Resolution** | 8-bit (1% RH, 1 °C steps) |
| **Sampling period** | 1.0 second (do not sample faster than 1 Hz) |
| **Interface** | Custom Single-Bus 1-Wire protocol |
| **Active measuring current** | 0.5 mA to 2.5 mA |

## Pinout

### 4-Pin Package / 3-Pin Breakout Module

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+3.0 V to +5.5 V DC) |
| 2 | `DATA` | Digital I/O | Single-bus bidirectional data line (requires 4.7kΩ–10kΩ pull-up resistor) |
| 3 | `NC` | Not Connected | No connection (pin 3 omitted on 3-pin breakout modules) |
| 4 | `GND` | Power | Ground (0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 3.0 | 5.0 | 5.5 | V | DC |
| Measuring Current | $I_{DD}$ | 0.5 | 1.0 | 2.5 | mA | During data transmission |
| Standby Current | $I_{SB}$ | 100 | 120 | 150 | µA | Between measurements |
| Humidity Measuring Range | $RH$ | 20 | — | 90 | % RH | $0^\circ\text{C} \text{ to } 50^\circ\text{C}$ |
| Humidity Accuracy | $\Delta RH$ | -5 | — | +5 | % RH | At $25^\circ\text{C}$ |
| Temperature Measuring Range | $T$ | 0 | — | 50 | °C | |
| Temperature Accuracy | $\Delta T$ | -2.0 | — | +2.0 | °C | |
| Data Response Time | $t_{read}$ | — | 1.0 | — | s | Minimum interval between reads |

## Communication protocol

The DHT11 uses a single-line bidirectional protocol. Every read operation consists of a 40-bit data packet (5 bytes) transmitted MSB first:

$$\text{Data Packet} = \underbrace{\text{Humidity Integral}}_{\text{Byte 0}} + \underbrace{\text{Humidity Decimal}}_{\text{Byte 1 (0x00)}} + \underbrace{\text{Temp Integral}}_{\text{Byte 2}} + \underbrace{\text{Temp Decimal}}_{\text{Byte 3 (0x00)}} + \underbrace{\text{Checksum}}_{\text{Byte 4}}$$

- **Checksum verification:** $\text{Byte 4} = (\text{Byte 0} + \text{Byte 1} + \text{Byte 2} + \text{Byte 3}) \pmod{256}$.
- **Communication timing:**
  1. Microcontroller pulls `DATA` line LOW for at least **18 ms** to initiate a start signal, then pulls HIGH for 20–40 µs.
  2. DHT11 responds by pulling `DATA` LOW for 80 µs, then HIGH for 80 µs.
  3. DHT11 transmits 40 data bits. Each bit starts with a 50 µs LOW pulse. A 26–28 µs HIGH pulse represents bit `0`, whereas a 70 µs HIGH pulse represents bit `1`.

```
MCU Start:   ───┐            ┌───────────────
                └─ 18ms LOW ─┘ 20-40µs HIGH
DHT Response:                                └── 80µs LOW ─── 80µs HIGH ─── Data Bits...
```

## Wiring

| DHT11 Sensor | → | Microcontroller (Arduino Uno / ESP32) | Notes |
|---|---|---|---|
| `VCC` | | `5V` (or `3.3V`) | Power supply |
| `DATA` | | Digital GPIO Pin (e.g. GPIO2) | Requires a $4.7\text{ k}\Omega$ to $10\text{ k}\Omega$ pull-up resistor to VCC |
| `GND` | | `GND` | Ground |

> [!NOTE]
> 3-Pin Breakout Modules usually include an onboard $10\text{ k}\Omega$ pull-up resistor between `DATA` and `VCC`, making external resistors unnecessary.

## Common mistakes

- **Polling faster than 1 Hz:** The DHT11 requires at least 1.0 second between consecutive read requests. Polling faster will return stale data, checksum errors, or cause the sensor to freeze.
- **Missing pull-up resistor:** The single-bus protocol relies on an open-drain/pull-up architecture. Operating a bare 4-pin DHT11 without a $4.7\text{ k}\Omega$–$10\text{ k}\Omega$ pull-up resistor on the `DATA` line causes timeout errors.
- **Expecting sub-zero or fractional readings:** The DHT11 returns integer-only values for temperature and humidity, and cannot measure temperatures below $0^\circ\text{C}$. Use a **DHT22 / AM2302** for sub-zero or decimal precision requirements.

## Notes

- Long cable runs (> 20 meters) require reducing the pull-up resistor value to $1\text{ k}\Omega$ to compensate for bus capacitance.
