## Overview

The **MicroSD Card Module** is an SPI-based breakout board designed to interface standard MicroSD (SDSC) and MicroSDHC memory cards with 5 V or 3.3 V microcontrollers. Because native SD cards operate exclusively at 3.3 V logic and draw up to 200 mA during burst writes, this module includes an onboard 3.3 V low-dropout (LDO) linear regulator (e.g. AMS1117-3.3) and a quad buffer level shifter IC (such as the 74LVC125A or 74HC4050).

It is standard equipment in DIY datalogging projects, weather stations, flight recorders, and audio playback systems built on Arduino, ESP32, and Raspberry Pi platforms.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 4.5 V to 5.5 V (or 3.3 V direct) |
| **Logic level** | 3.3 V and 5 V tolerant (onboard level shifter) |
| **Interface** | SPI Mode 0 ($CPOL=0, CPHA=0$) |
| **Supported card types** | MicroSD ($\le 2\text{ GB}$), MicroSDHC ($\le 32\text{ GB}$) |
| **File system format** | FAT16 / FAT32 |
| **Peak current draw** | ~100 mA to 200 mA during write operations |

## Pinout

The module exposes a standard 6-pin 0.1" (2.54 mm) right-angle or straight header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` | Power | Ground (0 V) |
| 2 | `VCC` | Power | Supply input (+4.5 V to +5.5 V DC) |
| 3 | `MISO` | Output | Master In Slave Out — SPI data line from card to MCU |
| 4 | `MOSI` | Input | Master Out Slave In — SPI data line from MCU to card |
| 5 | `SCK` | Input | Serial Clock — SPI clock signal driven by MCU |
| 6 | `CS` | Input | Chip Select — Active-Low SPI slave select signal |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 4.5 | 5.0 | 5.5 | V | Powered via onboard regulator |
| Logic Input High | $V_{IH}$ | 2.0 | 3.3 / 5.0 | 5.5 | V | `MOSI`, `SCK`, `CS` pins |
| Logic Input Low | $V_{IL}$ | -0.5 | 0 | 0.8 | V | `MOSI`, `SCK`, `CS` pins |
| Operating Current (Idle) | $I_{idle}$ | — | 0.2 | 2.0 | mA | Standby mode |
| Operating Current (Write) | $I_{write}$ | — | 80 | 200 | mA | Peak burst write current |
| SPI Clock Speed | $f_{SCK}$ | — | 4 | 25 | MHz | Microcontroller dependent |
| Operating Temperature | $T_{opr}$ | -20 | — | 70 | °C | Ambient temperature |

## Communication & protocol

The module communicates via standard 4-wire **SPI** (Mode 0: active-high clock, data sampled on leading rising edge). 

1. **Card Initialization:** The host MCU sends 80+ clock pulses on `SCK` with `CS` held high to force the SD card into SPI mode, followed by software reset command `CMD0`.
2. **SPI Voltage Shifting:** Incoming 5 V logic signals from the MCU (`MOSI`, `SCK`, `CS`) pass through the onboard 74LVC125 level shifter down to 3.3 V. The `MISO` output line drives 3.3 V logic, which is correctly recognized as a High state by 5 V TTL microcontrollers (Arduino Uno `V_IH_min` = 3.0 V).

## Wiring

| Module Pin | → | Arduino Uno | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V | 5V / 3.3V | Connect to 5 V rail for onboard regulator |
| `GND` | | GND | GND | Shared system ground |
| `MISO` | | D12 | GPIO 19 | Hardware SPI MISO pin |
| `MOSI` | | D11 | GPIO 23 | Hardware SPI MOSI pin |
| `SCK` | | D13 | GPIO 18 | Hardware SPI Clock pin |
| `CS` | | D4 (or D10) | GPIO 5 | Configurable Chip Select pin |

> [!WARNING]
> Cheap resistor-divider clones hazard:
> - Some low-cost clone boards substitute the level-shifter IC with cheap passive resistor dividers ($1\text{ k}\Omega / 2.2\text{ k}\Omega$). Resistor dividers distort SPI clock edges at frequencies above 4 MHz, causing random file corruption and card initialization failures (`SD initialization failed`).
> - Ensure your module uses an active IC buffer (74LVC125 / 74HC4050).

## Example

```cpp
#include <SPI.h>
#include <SD.h>

const int chipSelect = 4;

void setup() {
  Serial.begin(9600);
  while (!Serial) { ; }

  Serial.print("Initializing SD card...");
  if (!SD.begin(chipSelect)) {
    Serial.println("Initialization failed!");
    return;
  }
  Serial.println("Initialization done.");

  File dataFile = SD.open("datalog.txt", FILE_WRITE);
  if (dataFile) {
    dataFile.println("Timestamp,Temperature_C");
    dataFile.println("1000,24.5");
    dataFile.close();
    Serial.println("Data written to datalog.txt");
  } else {
    Serial.println("Error opening datalog.txt");
  }
}

void loop() {
  // Main execution loop
}
```

## Common mistakes

- **Formatting cards $>32\text{ GB}$ with exFAT:** MicroSD card libraries on 8-bit MCUs (such as standard Arduino `SD.h`) only support FAT16 and FAT32 file systems. MicroSDXC cards ($>32\text{ GB}$) formatted in exFAT fail to initialize.
- **Powering from weak 3.3 V rails:** MicroSD cards draw up to 200 mA during write operations. Powering `VCC` from a low-current 3.3 V MCU pin (e.g. older FTDI adapters or Nano 3.3 V pins limited to 50 mA) causes brownout resets.
- **Leaving `CS` unhandled on shared SPI buses:** When sharing the SPI bus with displays or sensors (e.g. Ethernet shields, OLEDs), ensure all `CS` pins have pull-up resistors so inactive devices release the `MISO` line.

## Notes

- **MicroSD vs MicroSDHC:** MicroSDHC cards ($4\text{ GB}$ to $32\text{ GB}$) use block addressing (512-byte blocks) rather than byte addressing.
