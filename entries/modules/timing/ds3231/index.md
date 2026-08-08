## Overview

The **DS3231** is a low-cost, highly accurate I2C real-time clock (RTC) manufactured by Maxim Integrated (now Analog Devices). It incorporates an integrated temperature-compensated crystal oscillator (TCXO) and a 32.768 kHz quartz crystal, providing exceptional timekeeping accuracy ($\pm 2\text{ ppm}$, ~1 minute per year error).

The device maintains seconds, minutes, hours, day, date, month, and year with leap-year compensation valid up to the year 2100. It includes a battery input (`VBAT`) for main power loss backup, two programmable time-of-day alarms, a square-wave/32.768 kHz output pin, and an internal digital temperature sensor.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 2.3 V to 5.5 V DC |
| **Battery backup (`VBAT`)** | 2.3 V to 5.5 V (typically CR2032 3V coin cell) |
| **Accuracy** | $\pm 2\text{ ppm}$ ($0^\circ\text{C}$ to $+40^\circ\text{C}$), $\pm 3.5\text{ ppm}$ ($-40^\circ\text{C}$ to $+85^\circ\text{C}$) |
| **Battery backup current** | $< 0.8\text{ }\mu\text{A}$ typical |
| **Communication interface** | I2C (address `0x68`, up to 400 kHz) |
| **Output signals** | `SQW` / `INT` (Programmable interrupt/square wave), `32kHz` |
| **Temperature sensor accuracy** | $\pm 3\text{ }^\circ\text{C}$ |

## Pinout

### Standard DS3231 Breakout Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `32K` | Digital Output | 32.768 kHz open-drain square wave output |
| 2 | `SQW` / `INT` | Digital Output | Interrupt or programmable square wave output (Active-LOW, Open-drain) |
| 3 | `SCL` | Digital Input | I2C Serial Clock input |
| 4 | `SDA` | Digital I/O | I2C Serial Data line |
| 5 | `VCC` | Power | Main supply voltage (+2.3 V to +5.5 V) |
| 6 | `GND` | Power | Ground (0 V) |

### Memory / AT24C32 EEPROM

Most DS3231 breakout modules (such as ZS-042) include an onboard 32 Kbit (4 KB) **AT24C32** I2C EEPROM chip at base address `0x57` (selectable `0x50`–`0x57` via solder pads A0, A1, A2).

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Main Supply Voltage | $V_{CC}$ | 2.3 | 3.3 | 5.5 | V | DC |
| Battery Supply Voltage | $V_{BAT}$ | 2.3 | 3.0 | 5.5 | V | Coin cell backup |
| Active I2C Supply Current | $I_{CCA}$ | — | 100 | 200 | µA | $f_{SCL} = 400\text{ kHz}$ |
| Standby Current | $I_{CCS}$ | — | 70 | 150 | µA | $V_{CC} = 5.0\text{ V}$, I2C bus idle |
| Timekeeping Battery Current | $I_{BATATT}$ | — | 0.85 | 3.0 | µA | $V_{CC} = 0\text{ V}$, $V_{BAT} = 3.0\text{ V}$ |
| Frequency Accuracy | $\Delta f/f$ | -2 | — | +2 | ppm | $0^\circ\text{C} \text{ to } +40^\circ\text{C}$ |
| Temp Sensor Resolution | $T_{res}$ | — | 0.25 | — | °C | 10-bit output |

## Register map

| Address | Register | Access | Description |
|---|---|---|---|
| `0x00` | `SECONDS` | R/W | BCD format (00–59) |
| `0x01` | `MINUTES` | R/W | BCD format (00–59) |
| `0x02` | `HOURS` | R/W | BCD format (12-hr with AM/PM or 24-hr 00–23) |
| `0x03` | `DAY` | R/W | Day of week (1–7) |
| `0x04` | `DATE` | R/W | Day of month BCD (01–31) |
| `0x05` | `MONTH` | R/W | Month BCD (01–12) + Century bit |
| `0x06` | `YEAR` | R/W | Year BCD (00–99) |
| `0x0E` | `CONTROL` | R/W | Enable oscillator (`EOSC`), Enable alarms (`INTCN`), Rate select (`RS1/RS2`) |
| `0x0F` | `STATUS` | R/W | Oscillator stop flag (`OSF`), Alarm flags (`A1F`, `A2F`) |
| `0x11` | `TEMP_MSB` | R | Temperature Integer part (°C, 2's complement) |
| `0x12` | `TEMP_LSB` | R | Temperature Fractional part (bits [7:6] represent .00, .25, .50, .75 °C) |

> [!NOTE]
> Registers `0x00` through `0x06` store values in **Binary Coded Decimal (BCD)** format. To convert BCD to decimal in software: `decimal = (bcd >> 4) * 10 + (bcd & 0x0F)`.

## Wiring

| DS3231 Breakout Pin | → | Microcontroller (Arduino Uno / ESP32) |
|---|---|---|
| `VCC` | | `5V` (or `3.3V`) |
| `GND` | | `GND` |
| `SDA` | | `SDA` (A4 on Uno, GPIO21 on ESP32) |
| `SCL` | | `SCL` (A5 on Uno, GPIO22 on ESP32) |
| `SQW` / `INT` | | GPIO Pin with internal pull-up (for alarm interrupts) |

> [!WARNING]
> Charging Circuit Danger on ZS-042 Modules:
> Many cheap "ZS-042" DS3231 modules include a simple diode-resistor trickle charge circuit designed for rechargeable LIR2032 cells. If using a non-rechargeable **CR2032** coin cell, this circuit can force current into the primary cell, risking leakage or rupture. Desolder the 200 Ω resistor or diode on ZS-042 boards when using standard CR2032 batteries.

## Common mistakes

- **Not converting BCD to Binary/Decimal:** Reading `0x15` from register `0x01` returns $0\times15$ (hex), which equals $21$ in decimal BCD. Treating it directly as an integer yields 21 instead of 15.
- **Forgetting to clear OSF (Oscillator Stop Flag):** On first power up or after battery replacement, the `OSF` bit in `0x0F` is set to `1` indicating the oscillator was stopped. Software must clear `OSF` to confirm time valid status.
- **Incompatible trickle charging with CR2032:** Using non-rechargeable CR2032 batteries on ZS-042 boards without disabling the onboard charging circuit.

## Notes

- The TCXO updates crystal compensation registers automatically every 64 seconds based on internal temperature readings.
