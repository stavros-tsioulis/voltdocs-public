# MFRC522

Highly-integrated 13.56 MHz reader/writer IC for ISO/IEC 14443 A / MIFARE
contactless communication. Drives a reader antenna directly with no extra
active circuitry and exposes SPI, I2C, and UART host interfaces. Sold as the
bare IC (HVQFN32) or, far more commonly, on the ubiquitous low-cost **RC522**
breakout module used with Arduino/ESP32/Raspberry Pi projects.

> **NRND:** NXP lists the MFRC522 as *Not Recommended for New Designs*;
> the suggested replacement is the CLRC663 Plus family.

## Key specs

| Parameter | Value |
|---|---|
| Protocol | ISO/IEC 14443 A / MIFARE (Mini, 1K, 4K, Ultralight, DESFire EV1, Plus) |
| Carrier frequency | 13.56 MHz |
| Host interfaces | SPI (≤10 Mbit/s), I2C (≤3.4 Mbit/s), UART (≤1228.8 kBd) |
| Supply voltage | 2.5–3.6 V |
| Operating temperature | −25 °C to +85 °C |
| FIFO buffer | 64 bytes |
| Typical read range | ~50 mm (antenna/tuning dependent) |
| Package | HVQFN32 (SOT617-1) |

## IC pinout (HVQFN32)

| Pin | Signal | Description |
|---|---|---|
| 1 | I2C | I2C-bus enable input |
| 2 | PVDD | Pin power supply |
| 3 | DVDD | Digital power supply |
| 4 | DVSS | Digital ground |
| 5 | PVSS | Pin power supply ground |
| 6 | NRSTPD | Reset / power-down input |
| 7 | MFIN | MIFARE signal input |
| 8 | MFOUT | MIFARE signal output |
| 9 | SVDD | MFIN/MFOUT pin power supply |
| 10 | TVSS | Transmitter 1 ground |
| 11 | TX1 | Transmitter 1 output |
| 12 | TVDD | Transmitter power supply |
| 13 | TX2 | Transmitter 2 output |
| 14 | TVSS | Transmitter 2 ground |
| 15 | AVDD | Analog power supply |
| 16 | VMID | Internal reference voltage |
| 17 | RX | RF signal input |
| 18 | AVSS | Analog ground |
| 19 | AUX1 | Auxiliary test output |
| 20 | AUX2 | Auxiliary test output |
| 21 | OSCIN | Crystal osc. input (27.12 MHz) |
| 22 | OSCOUT | Crystal osc. output |
| 23 | IRQ | Interrupt request output |
| 24 | SDA / NSS / RX | I2C data / SPI select / UART address |
| 25–31 | D1–D7 | Test port, shared with I2C address bits, SPI SCK/MOSI/MISO, UART DTRQ/MX/TX |
| 32 | EA | External address input (I2C address coding) |

*Pins 25–31 are multiplexed by interface mode — see the datasheet's §7.1 for
the full per-mode mapping.*

## Common breakout module pinout (RC522, 8-pin SPI header)

| Pin | Name | Function |
|---|---|---|
| 1 | SDA/SS | SPI chip select |
| 2 | SCK | SPI clock |
| 3 | MOSI | SPI data in |
| 4 | MISO | SPI data out |
| 5 | IRQ | Interrupt (unused on most modules) |
| 6 | GND | Ground |
| 7 | RST | Reset |
| 8 | 3.3V | Power (3.3 V only — **not** 5 V tolerant on most boards) |

## Versions

- **2.0** (`MFRC52202HN1`, current) — improved reader-IC stability, added timer
  prescaler, corrected CRC handling when `RxMultiple` is set.
- **1.0** (`MFRC52201HN1`) — original release. See [version 1.0](versions/1.0/index.md).
