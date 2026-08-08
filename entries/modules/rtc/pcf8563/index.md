## Overview

The **PCF8563** is a low-power CMOS real-time clock (RTC) and calendar IC manufactured by NXP Semiconductors. Paired with a $32.768\text{ kHz}$ quartz tuning-fork crystal and a 3V coin cell backup battery (CR1220 / CR2032), it maintains timekeeping even when main system power is completely disconnected.

Operating down to **$1.0\text{V}$ DC** with a backup supply current of just **$0.25\ \mu\text{A}$**, the PCF8563 provides full BCD-formatted time registers (seconds, minutes, hours, date, day-of-week, month, century, and year) over an **$I^2C$ interface (`0x51`)**. It features a programmable countdown timer, alarm interrupt output (`INT`), and a programmable square-wave clock output (`CLKOUT`).

## Quick reference

| | |
|---|---|
| **Operating voltage (`VDD`)** | 1.8 V to 5.5 V DC (1.0 V to 5.5 V timekeeping backup) |
| **Interface** | $I^2C$ Fast-Mode (up to 400 kHz) |
| **Fixed $I^2C$ address** | `0x51` |
| **Crystal frequency** | $32.768\text{ kHz}$ ($C_L = 12.5\text{ pF}$) |
| **Backup power draw** | $0.25\ \mu\text{A}$ typical at $VDD = 3.0\text{V}$ |
| **Timekeeping fields** | Seconds, Minutes, Hours, Days, Weekdays, Months, Century, Years |
| **Clock Output (`CLKOUT`)** | Programmable $32.768\text{ kHz}, 1.024\text{ kHz}, 32\text{ Hz}$, or $1\text{ Hz}$ output |
| **Interrupt Output (`INT`)**| Active-Low open-drain output (Alarm trigger / Countdown timer) |

## Pinout (8-Pin SOIC & Module Header)

```
             ┌───┴───┐
         OSCI ─┤ 1   8├─ VDD
        OSCO ─┤ 2    7├─ CLKOUT
         INT ─┤ 3    6├─ SCL
         VSS ─┤ 4    5├─ SDA
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `OSCI` | Analog Input | $32.768\text{ kHz}$ crystal oscillator input |
| 2 | `OSCO` | Analog Output | $32.768\text{ kHz}$ crystal oscillator output |
| 3 | `INT` | Digital Output | Active-Low open-drain interrupt output pin |
| 4 | `VSS` | Power | Ground reference (0 V) |
| 5 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 6 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 7 | `CLKOUT` | Digital Output | Square-wave clock output pin (Open-drain) |
| 8 | `VDD` | Power | Supply power input (+1.8 V to +5.5 V DC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Operating)| $V_{DD}$ | 1.8 | 3.3 | 5.5 | V | $I^2C$ bus operation |
| Timekeeping Voltage | $V_{clock}$| 1.0 | — | 5.5 | V | Crystal oscillator running |
| Backup Current | $I_{DD\_bkp}$| — | 0.25 | 0.8 | µA | $V_{DD} = 3.0\text{V}, I^2C$ inactive |
| Low Voltage Detect Limit| $V_{LOW}$ | — | 1.0 | 1.3 | V | Integrity flag set if $V_{DD} < V_{LOW}$ |
| $I^2C$ Bus Frequency | $f_{SCL}$ | 0 | — | 400 | kHz | Fast-mode |

## $I^2C$ Register Map & BCD Format

Time registers are stored in **Binary-Coded Decimal (BCD)**:

| Address | Register Name | Bit Range | Format / Range |
|---|---|---|---|
| `0x02` | VL_Seconds | Bit 6–0 | 00–59 BCD (Bit 7 = `VL` Voltage Low integrity flag) |
| `0x03` | Minutes | Bit 6–0 | 00–59 BCD |
| `0x04` | Hours | Bit 5–0 | 00–23 BCD |
| `0x05` | Days | Bit 5–0 | 01–31 BCD |
| `0x06` | Weekdays | Bit 2–0 | 0–6 (Sunday = 0) |
| `0x07` | Century_Months| Bit 4–0 | 01–12 BCD (Bit 7 = Century Bit) |
| `0x08` | Years | Bit 7–0 | 00–99 BCD |

$$ \text{DecToBcd}(val) = \left( \frac{val}{10} \ll 4 \right) | (val \% 10) $$

$$ \text{BcdToDec}(val) = \left( (val \gg 4) \times 10 \right) + (val \& 0x0F) $$

## Wiring

| PCF8563 Module Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |

## Example (Arduino RTClib / PCF8563 Library)

```cpp
#include <Wire.h>
#include "RTClib.h"

RTC_PCF8563 rtc;

void setup() {
  Serial.begin(115200);
  Wire.begin();

  if (!rtc.begin()) {
    Serial.println("Couldn't find PCF8563 RTC!");
    while (1);
  }

  if (rtc.lostPower()) {
    Serial.println("PCF8563 lost power, setting time to compile time!");
    rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
  }
}

void loop() {
  DateTime now = rtc.now();

  Serial.print(now.year(), DEC); Serial.print('/');
  Serial.print(now.month(), DEC); Serial.print('/');
  Serial.print(now.day(), DEC); Serial.print(" ");
  Serial.print(now.hour(), DEC); Serial.print(':');
  Serial.print(now.minute(), DEC); Serial.print(':');
  Serial.print(now.second(), DEC); Serial.println();

  delay(1000);
}
```

## Common mistakes

- **Ignoring the `VL` (Voltage Low) flag:** Bit 7 of the seconds register (`0x02`) is the `VL` flag. If the backup battery voltage drops below $1.0\text{V}$, `VL` sets to 1, indicating that internal time data is corrupted and must be re-synchronized via NTP/GPS.
- **Forgetting pull-up resistors on `INT` / `CLKOUT`:** `INT` and `CLKOUT` are open-drain outputs and require external $10\text{ k}\Omega$ pull-up resistors to $V_{DD}$.

## Notes

- **PCF8563 vs DS1307 vs DS3231:** PCF8563 operates down to 1.0V with $0.25\ \mu\text{A}$ backup current; DS1307 requires 4.5V main supply; DS3231 includes an internal TCXO crystal for $\pm 2\text{ ppm}$ temperature compensation.
