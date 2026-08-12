## Overview

The **AT24C32** (commonly **AT24C32D** or **AT24C32N** in SOIC-8 or DIP-8) is a $32\text{ Kbit}$ ($4,096\text{ Bytes}$) I2C serial EEPROM IC manufactured by Microchip Technology (originally Atmel). Organised as 4,096 8-bit bytes with a **32-byte page write buffer**, it operates across a wide voltage supply range of **$1.7\text{ V}$ to $5.5\text{ V}$**.

Extremely popular in maker projects, the AT24C32 is standard equipment on ubiquitous **DS3231 RTC breakout boards**, providing dedicated non-volatile memory for data logging, timestamp storage, and persistent system configuration without consuming microcontroller internal EEPROM.

## Quick reference

| | |
|---|---|
| **Memory Type** | 32-Kbit Serial I2C Non-Volatile EEPROM |
| **Package** | 8-Pin DIP (Through-Hole) / SOIC-8 / DS3231 RTC Board Component |
| **Supply Voltage Range ($V_{CC}$)** | $1.7\text{ V}$ to $5.5\text{ V}$ DC |
| **Memory Capacity** | $32\text{ Kbits}$ ($4\text{ Kbytes}$ / $4,096\text{ Bytes}$) |
| **Page Write Buffer** | $32\text{ Bytes}$ page write buffer |
| **I2C Clock Speed** | $400\text{ kHz}$ Fast Mode at $V_{CC} \ge 2.5\text{V}$ |
| **Default RTC Board I2C Address** | `0x57` (Address pins $A_0, A_1, A_2$ usually pulled HIGH via solder jumpers) |
| **Endurance & Retention** | 1,000,000 write cycles / $>100\text{ years}$ data retention |

## Pinout (8-Pin DIP / SOIC Package)

```
        ┌──────────┐
     A0 ─│ 1      8 │─ VCC
     A1 ─│ 2      7 │─ WP
     A2 ─│ 3      6 │─ SCL
    VSS ─│ 4      5 │─ SDA
        └──────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `A0` | Hardware I2C Chip Address bit 0 input |
| 2 | `A1` | Hardware I2C Chip Address bit 1 input |
| 3 | `A2` | Hardware I2C Chip Address bit 2 input |
| 4 | `GND` / `VSS` | Ground reference (0 V) |
| 5 | `SDA` | I2C Serial Data bidirectional line |
| 6 | `SCL` | I2C Serial Clock input line |
| 7 | `WP` | Hardware Write Protect pin (High = Write Protect ON, Low/GND = Write Enable) |
| 8 | `VCC` | Positive power supply (+1.7V to +5.5V DC) |

## DS3231 RTC Module Address Conflict Resolution

On standard ZS-042 / DS3231 RTC breakout modules:
- The **DS3231 RTC IC** uses fixed I2C address **`0x68`**.
- The onboard **AT24C32 EEPROM IC** has $A_0, A_1, A_2$ pulled HIGH by default, giving base I2C address **`0x57`** (`1010111`).
- Bridging solder pads $A_0, A_1, A_2$ to GND changes the EEPROM address down to **`0x50`** (`1010000`), allowing multi-EEPROM bus designs.

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage Range | $V_{CC}$ | 1.7 | 3.3 / 5.0 | 5.5 | V | Operational range |
| Read Current | $I_{CC\_READ}$ | — | 400 | 1000 | $\mu\text{A}$ | $V_{CC} = 5.0\text{V}, f_{SCL} = 400\text{kHz}$ |
| Write Current | $I_{CC\_WRITE}$ | — | 1.0 | 3.0 | mA | $V_{CC} = 5.0\text{V}$ |
| Standby Current | $I_{SB}$ | — | 1.0 | 6.0 | $\mu\text{A}$ | $V_{CC} = 5.0\text{V}, I2C\text{ idle}$ |
| Write Cycle Time | $T_{WR}$ | — | 2.0 | 5.0 | ms | Self-timed page write |

## Common mistakes

- **Confusing 32-byte page size with 64-byte page size:** The AT24C32 has a **32-byte** page buffer (unlike 24LC256 which has a 64-byte page buffer). Writing more than 32 consecutive bytes without updating the page address wraps around within the 32-byte page window!
- **Forgetting 16-bit internal address bytes:** EEPROMs with capacity $>2048$ bytes (like AT24C32) require a 2-byte (16-bit) memory address to be transmitted over I2C before data bytes.

## Notes

- **DS3231 Companion:** Paired with the DS3231 RTC, the AT24C32 allows microcontrollers to log hourly timestamped temperature/event logs without relying on external SD card modules.
