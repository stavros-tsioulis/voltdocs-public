## Overview

The **DS3231** is an extremely accurate, low-cost I2C real-time clock (RTC) manufactured by Maxim Integrated (now Analog Devices). It incorporates an integrated Temperature-Compensated Crystal Oscillator (TCXO) and a 32.768 kHz resonator crystal inside its package.

Unlike older RTCs (such as the DS1307) that drift by several seconds per day due to ambient temperature shifts, the DS3231 continuously measures temperature and adjusts its internal crystal tuning capacitors every 64 seconds, maintaining timekeeping accuracy within **$\pm 2\text{ ppm}$** ($\sim 1\text{ minute per year}$) across $-40^\circ\text{C}$ to $+85^\circ\text{C}$.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 2.3 V – 5.5 V |
| **Backup battery (`VBAT`)** | 2.3 V – 5.5 V (typically CR2032 3V Lithium cell) |
| **Accuracy** | $\pm 2\text{ ppm}$ ($0^\circ\text{C}$ to $+40^\circ\text{C}$) / $\pm 3.5\text{ ppm}$ ($-40^\circ\text{C}$ to $+85^\circ\text{C}$) |
| **Interface** | Fast-Mode I2C (400 kHz) |
| **Default I2C address** | `0x68` (Fixed 7-bit slave address) |
| **Timekeeping current** | ~500 nA on `VBAT` when primary `VCC` is removed |
| **Features** | Seconds, Minutes, Hours, Day, Date, Month, Year (to 2100 with Leap Year), 2 Alarms, 32kHz Square Wave |

## Pinout

### Standard 6-Pin Breakout Module (ZS-042)

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `32K` | Digital Output | 32.768 kHz square-wave output (open-drain, push-pull capable) |
| 2 | `SQW` / `INT` | Digital Output | Active-LOW Interrupt or Programmable Square-Wave output (Open-drain) |
| 3 | `SCL` | Digital Input | I2C Clock Line |
| 4 | `SDA` | Digital I/O | I2C Data Line |
| 5 | `VCC` | Power | Primary Power Supply (+2.3 V to +5.5 V) |
| 6 | `GND` | Power | Ground (0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Active Supply Voltage | `VCC` | 2.3 | 3.3 | 5.5 | V | Normal I2C operation |
| Battery Supply Voltage | `VBAT` | 2.3 | 3.0 | 5.5 | V | Battery backup power |
| Active Supply Current | `ICC` | — | 200 | 300 | µA | $f_{SCL} = 400\text{ kHz}$ |
| Timekeeping Current | `IBATT` | — | 0.85 | 2.5 | µA | $V_{CC} = 0\text{ V}$, $V_{BAT} = 3.0\text{ V}$, $T_A = +25^\circ\text{C}$ |
| Temperature Sensor Accuracy | `TACC` | -3.0 | — | +3.0 | °C | Integrated temperature ADC |
| Temperature Conversion Time | `tCONV` | — | 125 | 200 | ms | Performed every 64 seconds |

## Register map

Time and date values are stored in binary-coded decimal (BCD) format across registers `0x00` to `0x06`.

| Address | Register Name | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 | Range / Format |
|---|---|---|---|---|---|---|---|---|---|---|
| `0x00` | Seconds | 0 | 10 Seconds | 1 Second | `00`–`59` BCD |
| `0x01` | Minutes | 0 | 10 Minutes | 1 Minute | `00`–`59` BCD |
| `0x02` | Hours | 0 | 12/24 | 20/AM/PM | 10 Hour | 1 Hour | `01`–`12` / `00`–`23` BCD |
| `0x03` | Day of Week | 0 | 0 | 0 | 0 | 0 | Day | `1`–`7` (User defined) |
| `0x04` | Date | 0 | 0 | 10 Date | 1 Date | `01`–`31` BCD |
| `0x05` | Month / Century | Century | 0 | 0 | 10 Month | 1 Month | `01`–`12` BCD + Century bit |
| `0x06` | Year | 10 Year | 1 Year | `00`–`99` BCD |
| `0x11` | Temp (MSB) | Sign | 2^6 | 2^5 | 2^4 | 2^3 | 2^2 | 2^1 | 2^0 | Integer temperature in °C |
| `0x12` | Temp (LSB) | 2^-1 | 2^-2 | 0 | 0 | 0 | 0 | 0 | 0 | Fractional temperature ($0.25^\circ\text{C}$ resolution) |

## Wiring

| DS3231 Module Pin | :i-lucide-move-right: | Microcontroller (Arduino Uno / ESP32) |
|---|---|---|
| `VCC` | | 5V (or 3.3V) |
| `GND` | | GND |
| `SDA` | | I2C SDA (Pin `A4` on Uno / GPIO`21` on ESP32) |
| `SCL` | | I2C SCL (Pin `A5` on Uno / GPIO`22` on ESP32) |
| `SQW` | | Digital Pin `2` (Optional for alarm wake-up interrupts) |

## Common mistakes

- **Charging circuit damage to non-rechargeable CR2032 batteries:** Many cheap ZS-042 modules include a simple trickle-charge circuit (resistor + diode from VCC to VBAT). Inserting a standard primary (non-rechargeable) **CR2032** battery can cause it to swell or leak. Remove the diode/resistor on the board or use a rechargeable **LIR2032** coin cell.
- **Forgetting BCD to Binary conversion:** All timekeeping registers store numbers in Binary-Coded Decimal (BCD). To convert BCD to standard integers:
  $$\text{Integer} = (\text{BCD} \gg 4) \times 10 + (\text{BCD} \& 0\text{x0F})$$
- **Not clearing the Alarm Interrupt Flag (`A1F` / `A2F`):** When an alarm fires, the `SQW/INT` pin goes `LOW` and stays `LOW` until software explicitly clears the alarm flag bit in register `0x0F` (Control/Status).

## Notes

- **AT24C32 EEPROM:** Most DS3231 breakout boards also include an onboard **AT24C32** 32 Kbit (4 KB) I2C EEPROM chip at address `0x57` for non-volatile data logging.
