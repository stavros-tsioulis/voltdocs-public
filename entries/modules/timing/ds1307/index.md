## Overview

The **DS1307** is a low-power, full binary-coded decimal (BCD) real-time clock (RTC) IC manufactured by Maxim Integrated (Analog Devices). It counts seconds, minutes, hours, day of the week, date of the month, month, and year with leap-year compensation valid up to the year 2100.

The chip incorporates a $32.768\text{ kHz}$ quartz crystal oscillator circuit, a power-sense circuit that automatically switches to a 3V CR2032 lithium battery backup during power outages, and **56 bytes of nonvolatile battery-backed SRAM** for storing custom user settings.

## Quick reference

| | |
|---|---|
| **Operating Voltage (`VCC`)** | 4.5 V to 5.5 V DC (**5.0 V required**) |
| **Backup Battery Voltage (`VBAT`)** | 2.0 V to 3.5 V DC (3 V CR2032 coin cell) |
| **Oscillator Frequency** | 32.768 kHz (requires external crystal with $12.5\text{ pF}$ load capacitance) |
| **Nonvolatile SRAM** | 56 bytes (address `0x08` to `0x3F`) |
| **Communication Interface** | I2C (fixed slave address `0x68`, up to 100 kHz) |
| **Square Wave Output (`SQW/OUT`)** | Programmable output frequency: 1 Hz, 4.096 kHz, 8.192 kHz, 32.768 kHz |
| **Backup Battery Current** | $< 500\text{ nA}$ (battery lasts 10+ years) |

## Pinout

### 8-Pin DIP / SOIC Package & Tiny RTC Module Header

```
           ┌──────────┐
        X1 ──│ 1      8 │── VCC (5V)
        X2 ──│ 2      7 │── SQW/OUT
      VBAT ──│ 3      6 │── SCL
       GND ──│ 4      5 │── SDA
           └──────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `X1` | Oscillator Input | Connect to 32.768 kHz crystal terminal 1 |
| 2 | `X2` | Oscillator Output | Connect to 32.768 kHz crystal terminal 2 |
| 3 | `VBAT` | Battery Input | Backup +3V CR2032 lithium battery input |
| 4 | `GND` | Power | Ground (0 V) |
| 5 | `SDA` | Digital I/O | I2C Serial Data line |
| 6 | `SCL` | Digital Input | I2C Serial Clock line |
| 7 | `SQW` / `OUT` | Digital Output | Square-Wave / Interrupt output line (Open-drain) |
| 8 | `VCC` | Power Input | Primary supply voltage (+4.5 V to +5.5 V DC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Primary Supply Voltage | $V_{CC}$ | 4.5 | 5.0 | 5.5 | V | DC |
| Battery Voltage | $V_{BAT}$ | 2.0 | 3.0 | 3.5 | V | CR2032 Lithium coin cell |
| Active Supply Current | $I_{CCA}$ | — | 0.8 | 1.5 | mA | $V_{CC} = 5.0\text{ V}$, I2C active |
| Battery Backup Current | $I_{BAT}$ | — | 300 | 500 | nA | $V_{CC} = 0\text{ V}$, $V_{BAT} = 3.0\text{ V}$ |
| Power-Fail Threshold | $V_{PF}$ | 1.21 $V_{BAT}$ | 1.25 $V_{BAT}$ | 1.29 $V_{BAT}$ | V | Switch to battery mode threshold |
| Crystal Load Capacitance | $C_L$ | — | 12.5 | — | pF | $32.768\text{ kHz}$ quartz crystal |

## Register Map (BCD Format)

Time and calendar data are stored in Binary-Coded Decimal (BCD) format across registers `0x00` to `0x06`:

| Address | Register | Bit 7 (MSB) | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 (LSB) | Range |
|---|---|---|---|---|---|---|---|---|---|---|
| `0x00` | `SECONDS` | **`CH`** | 10 Seconds | Seconds | 00–59 |
| `0x01` | `MINUTES` | 0 | 10 Minutes | Minutes | 00–59 |
| `0x02` | `HOURS` | 0 | 12/24 | 10Hr / AM/PM | Hours | 01–12 / 00–23 |
| `0x03` | `DAY` | 0 | 0 | 0 | 0 | 0 | Day of Week | 01–07 |
| `0x04` | `DATE` | 0 | 0 | 10 Date | Date | 01–31 |
| `0x05` | `MONTH` | 0 | 0 | 0 | 10 Month | Month | 01–12 |
| `0x06` | `YEAR` | 10 Year | Year | 00–99 |
| `0x07` | `CONTROL` | `OUT` | 0 | 0 | `SQWE` | 0 | 0 | `RS1` | `RS0` | Control byte |
| `0x08`–`0x3F` | `RAM` | 56 Bytes General Purpose Non-Volatile User SRAM | `0x00`–`0xFF` |

> [!NOTE]
> Clock Halt (`CH`) Bit:
> Bit 7 of register `0x00` is the **Clock Halt (`CH`) bit**. When `CH = 1`, the internal crystal oscillator is STOPPED and the clock does not run. Software MUST write `CH = 0` during initialization to start counting time!

## Wiring

| DS1307 Module Pin | → | Microcontroller (Arduino Uno / ESP32) | Notes |
|---|---|---|---|
| `VCC` | | `5V` | **Must be 5.0 V DC (Does NOT work on 3.3V)** |
| `GND` | | `GND` | Ground |
| `SDA` | | `SDA` (A4 on Uno, GPIO21 on ESP32) | $4.7\text{ k}\Omega$ pull-up resistor |
| `SCL` | | `SCL` (A5 on Uno, GPIO22 on ESP32) | $4.7\text{ k}\Omega$ pull-up resistor |
| `SQW` | | Digital Pin (optional 1 Hz pulse interrupt) | Open-drain output |

## Common mistakes

- **Powering with 3.3V:** The DS1307 requires $V_{CC} \ge 4.5\text{ V}$. Operating on 3.3V causes the power-fail comparator to assume main power was lost, locking out I2C access. For native 3.3V systems, use the **DS3231**.
- **Forgetting to clear Clock Halt (`CH`) bit:** New DS1307 ICs default to `CH = 1`. Time values stay frozen until software writes `0x00` to register `0x00`.
- **Crystal temperature drift:** Unlike the DS3231 (which has an integrated TCXO temperature-compensated crystal), the DS1307 uses an external uncompensated crystal. Ambient temperature changes can cause time drift up to **1–2 minutes per month**.

## Notes

- Tiny RTC modules often contain an 8-pin 24C32 EEPROM chip on the same I2C bus at address `0x50`.
