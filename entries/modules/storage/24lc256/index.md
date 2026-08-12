## Overview

The **24LC256** (commonly **24LC256-I/P** in DIP-8 or **24LC256-I/SN** in SOIC-8) is a $256\text{ Kbit}$ ($32,768\text{ Bytes}$) I2C serial non-volatile EEPROM IC manufactured by Microchip Technology. Organised as 32,768 8-bit bytes with a **64-byte page write buffer**, it operates across a supply range of **$2.5\text{ V}$ to $5.5\text{ V}$** DC.

Featuring $400\text{ kHz}$ Fast-Mode I2C bus compatibility, three hardware chip-address pins ($A_0, A_1, A_2$), and a Hardware Write Protect pin (`WP`), the 24LC256 is widely used in microcontrollers (Arduino, ESP32, STM32) for persistent configuration storage, calibration parameters, and offline sensor data logging.

## Quick reference

| | |
|---|---|
| **Memory Type** | 256-Kbit Serial I2C Non-Volatile EEPROM |
| **Package** | 8-Pin DIP (Through-Hole) / SOIC-8 / TSSOP-8 |
| **Supply Voltage Range ($V_{CC}$)** | $2.5\text{ V}$ to $5.5\text{ V}$ DC ($1.7\text{V}$ for 24AA256 series) |
| **Memory Capacity** | $256\text{ Kbits}$ ($32\text{ Kbytes}$ / $32,768\text{ Bytes}$) |
| **Page Write Buffer** | $64\text{ Bytes}$ page write buffer |
| **I2C Clock Speed** | $400\text{ kHz}$ Fast Mode ($100\text{ kHz}$ Standard Mode) |
| **Write Cycle Time** | $5.0\text{ ms}$ max self-timed page write cycle |
| **Endurance & Retention** | 1,000,000 write cycles / $>200\text{ years}$ data retention |

## Pinout (8-Pin DIP Package)

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
| 4 | `VSS` | Ground reference (0 V) |
| 5 | `SDA` | I2C Serial Data bidirectional line (Open-drain) |
| 6 | `SCL` | I2C Serial Clock input line |
| 7 | `WP` | Hardware Write Protect pin (High = Write Protect ON, Low/GND = Write Enable) |
| 8 | `VCC` | Positive power supply (+2.5V to +5.5V DC) |

## Hardware I2C Address Mapping

The 7-bit I2C device address consists of a fixed 4-bit control code (`1010` / `0xA`) followed by the 3 hardware address pin states ($A_2, A_1, A_0$):

$$\text{I2C Address} = 1\ 0\ 1\ 0\ A_2\ A_1\ A_0$$

| Pin $A_2$ | Pin $A_1$ | Pin $A_0$ | 7-Bit Hex Address | 8-Bit Read Address | 8-Bit Write Address |
|---|---|---|---|---|---|
| GND (`0`) | GND (`0`) | GND (`0`) | `0x50` | `0xA1` | `0xA0` |
| GND (`0`) | GND (`0`) | VCC (`1`) | `0x51` | `0xA3` | `0xA2` |
| VCC (`1`) | VCC (`1`) | VCC (`1`) | `0x57` | `0xAF` | `0xAE` |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage Range | $V_{CC}$ | 2.5 | 3.3 / 5.0 | 5.5 | V | Operational range |
| Read Current | $I_{CC\_READ}$ | — | 400 | 1000 | $\mu\text{A}$ | $V_{CC} = 5.5\text{V}, f_{SCL} = 400\text{kHz}$ |
| Write Current | $I_{CC\_WRITE}$ | — | 1.5 | 3.0 | mA | $V_{CC} = 5.5\text{V}$ |
| Standby Current | $I_{CCS}$ | — | 100 | 1000 | nA | $V_{CC} = 5.5\text{V}, I2C\text{ idle}$ |
| Write Cycle Time | $T_{WC}$ | — | 2.0 | 5.0 | ms | Self-timed page write |

## Common mistakes

- **Writing across 64-byte page boundaries:** The internal page write buffer holds 64 bytes. If a multi-byte write crosses a 64-byte address boundary (e.g. starting at byte address 62 for 5 bytes), the memory address wraps around to the beginning of the SAME page (byte 0), overwriting previous data!
- **Not waiting for write cycle completion:** Self-timed page writes take up to $5\text{ ms}$. Sending a new I2C read/write command immediately without delay or I2C ACK polling will result in NAKs from the chip.

## Notes

- **Up to 8 EEPROMs on one bus:** Connecting combinations of $A_0, A_1, A_2$ to GND or $V_{CC}$ allows operating up to 8 $\times$ 256Kbit chips ($256\text{ KB}$ total) on a single I2C bus.
