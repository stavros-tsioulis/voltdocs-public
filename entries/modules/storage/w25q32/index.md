## Overview

The **W25Q32** (W25Q32JV / W25Q32FV) is a 32-Mbit (4 Megabyte) non-volatile SPI NOR serial flash memory IC manufactured by Winbond Electronics. Available in an 8-pin SOIC package or a 5-pin DIP breakout module, it provides external data storage for embedded microcontrollers without SD card slot overhead.

Supporting Standard SPI, Dual-SPI, and Quad-SPI at clock frequencies up to **104 MHz** (transfer rates up to $416\text{ Mbits/sec}$ in Quad-SPI mode), the W25Q32 is widely used for storing web server HTML files, UI graphic assets, firmware binaries (OTA updates), audio samples, and file systems (LittleFS, SPIFFS, FATFS) on ESP32, STM32, RP2040, and Arduino boards.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 2.7 V to 3.6 V DC (3.3 V nominal) |
| **Capacity** | 32 Mbits ($4,194,304\text{ Bytes} / 4\text{ MB}$) |
| **Interface** | Standard SPI, Dual-SPI, Quad-SPI (Mode 0,0 & Mode 3,3) |
| **Max SPI Clock** | 104 MHz (Dual SPI equivalent 208 MHz, Quad SPI equivalent 416 MHz) |
| **Sector erase size** | 4 KB uniform sectors ($1,024\text{ sectors}$ total) |
| **Block erase size** | 32 KB & 64 KB blocks ($64\text{ blocks}$ of 64KB) |
| **Page program size** | 256 bytes per page ($16,384\text{ pages}$ total) |
| **Endurance & Retention** | 100,000 erase/program cycles / 20-year data retention |
| **Operating current** | $4.0\text{ mA}$ active read / $1.0\ \mu\text{A}$ power-down |

## Pinout (8-Pin SOIC Package & Module Header)

```
             ┌───┴───┐
         /CS ─┤ 1   8├─ VCC
      DO(IO1)─┤ 2   7├─ /HOLD(IO3)
     /WP(IO2)─┤ 3   6├─ CLK
         GND ─┤ 4   5├─ DI(IO0)
             └───────┘
```

| Pin Label | Name | Type | Description |
|---|---|---|---|
| 1 | `/CS` | Digital Input | Active-Low SPI Chip Select |
| 2 | `DO (IO1)` | Digital Output | SPI Serial Data Output / Dual & Quad I/O Pin 1 |
| 3 | `/WP (IO2)`| Digital Input | Active-Low Write Protect / Quad I/O Pin 2 |
| 4 | `GND` | Power | Ground reference (0 V) |
| 5 | `DI (IO0)` | Digital Input | SPI Serial Data Input / Dual & Quad I/O Pin 0 |
| 6 | `CLK` | Digital Input | SPI Serial Clock |
| 7 | `/HOLD (IO3)`| Digital Input| Active-Low Pause/Hold / Quad I/O Pin 3 |
| 8 | `VCC` | Power | Supply power input (+2.7 V to +3.6 V DC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.7 | 3.3 | 3.6 | V | DC |
| Active Read Current | $I_{CC1}$ | — | 4.0 | 10.0 | mA | $f_{CLK} = 50\text{ MHz}$ |
| Program/Erase Current | $I_{CC3}$ | — | 15.0 | 25.0 | mA | Page program or sector erase |
| Power-Down Current | $I_{pd}$ | — | 1.0 | 5.0 | µA | Deep power-down command (`0xB9`) |
| Page Program Time | $t_{PP}$ | — | 0.7 | 3.0 | ms | 256 bytes page program |
| Sector Erase Time (4KB) | $t_{SE}$ | — | 45 | 400 | ms | 4 KB sector erase |
| Block Erase Time (64KB) | $t_{BE}$ | — | 150 | 1000 | ms | 64 KB block erase |

## Common SPI Command Instructions

| Instruction Name | Opcode (Hex) | Description |
|---|---|---|
| Write Enable | `0x06` | Sets the Write Enable Latch (WEL) bit prior to write/erase |
| Read Status Register-1 | `0x05` | Reads `BUSY` flag (Bit 0) and `WEL` flag (Bit 1) |
| Read Data | `0x03` | Reads continuous data bytes starting at 24-bit address |
| Page Program | `0x02` | Writes up to 256 bytes into a single page |
| Sector Erase (4KB) | `0x20` | Erases a 4 KB sector (resets all bits to `0xFF`) |
| Read JEDEC ID | `0x9F` | Returns Manufacturer ID (`0xEF`) and Memory Type (`0x4016`) |

> [!IMPORTANT]
> Flash Memory Erase Rule:
> - In NOR flash memory, programming can only change bits from `1` to `0`. Changing bits from `0` back to `1` requires performing a **Sector Erase (`0x20`)** or **Block Erase**, which resets all bytes in that 4 KB sector to `0xFF`.

## Wiring

| W25Q32 Pin | → | Arduino (via Level Shifter) | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 3.3V Rail | 3.3V | **Do not connect to 5V** |
| `GND` | | GND | GND | System ground |
| `/CS` | | Digital D10 | GPIO 5 | SPI Chip Select |
| `CLK` | | Digital D13 | GPIO 18 | SPI Clock |
| `DI` (MOSI) | | Digital D11 | GPIO 23 | SPI MOSI |
| `DO` (MISO) | | Digital D12 | GPIO 19 | SPI MISO |
| `/WP` & `/HOLD`| | 3.3V | 3.3V | Pull High to disable write protect & hold |

## Example (Arduino `Adafruit_SPIFlash` Library)

```cpp
#include <SPI.h>
#include "Adafruit_SPIFlash.h"

// Hardware SPI with CS on pin 5
Adafruit_FlashTransport_SPI flashTransport(5, SPI);
Adafruit_SPIFlash flash(&flashTransport);

void setup() {
  Serial.begin(115200);
  while (!Serial) delay(10);

  Serial.println("W25Q32 SPI Flash Memory Test");

  if (!flash.begin()) {
    Serial.println("Could not find W25Q32 flash chip! Check SPI wiring.");
    while (1);
  }

  Serial.print("Flash chip JEDEC ID: 0x");
  Serial.println(flash.getJEDECID(), HEX);
  Serial.print("Flash size: ");
  Serial.print(flash.size() / 1024 / 1024);
  Serial.println(" MB");
}

void loop() {
  // Read first 16 bytes of sector 0
  uint8_t buffer[16];
  flash.readBuffer(0, buffer, sizeof(buffer));

  Serial.print("First 16 Bytes: ");
  for (int i = 0; i < 16; i++) {
    Serial.print(buffer[i], HEX); Serial.print(" ");
  }
  Serial.println();

  delay(5000);
}
```

## Common mistakes

- **Connecting 5V logic directly to SPI pins:** The W25Q32 operates strictly at 3.3V logic. Connecting 5V SPI lines directly damages the IC. Use level shifters for 5V microcontrollers.
- **Writing without erasing first:** Attempting to write new data over non-erased flash memory results in corrupted data, as `0` bits cannot be flipped back to `1` without a 4KB Sector Erase.

## Notes

- **Winbond W25Q Series Capacity:** W25Q16 (16 Mbit / 2 MB), **W25Q32 (32 Mbit / 4 MB)**, W25Q64 (64 Mbit / 8 MB), W25Q128 (128 Mbit / 16 MB).
