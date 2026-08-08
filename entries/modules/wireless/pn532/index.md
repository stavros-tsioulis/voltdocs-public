## Overview

The **PN532** is a highly integrated Near Field Communication (NFC) and 13.56 MHz RFID transceiver IC manufactured by NXP Semiconductors. Built around an 80C51 microcontroller core, it is the most versatile NFC controller for maker projects, supporting **Reader/Writer mode**, **Peer-to-Peer (P2P) mode**, and **NFC Card Emulation mode**.

Unlike basic RFID readers (such as the MFRC522 which only reads ISO 14443A MIFARE tags), the PN532 reads and writes **NTAG213 / NTAG215 / NTAG216** NFC stickers, MIFARE Classic/Ultralight cards, FeliCa cards, and communicates directly with NFC-enabled smartphones (Android / Apple).

## Quick reference

| | |
|---|---|
| **Module VCC** | 3.3 V to 5.0 V DC (onboard LDO) |
| **Chip VDD / VBAT** | 2.7 V to 5.5 V DC |
| **Carrier Frequency** | 13.56 MHz |
| **Operating Range** | Up to 50 mm (5 cm) |
| **Supported Protocols** | ISO/IEC 14443A/B, MIFARE 1K/4K, NTAG, FeliCa, ISO/IEC 18092 (NFCIP-1) |
| **Operating Modes** | Reader/Writer, P2P (NFCIP-1), Card Emulation (ISO 14443A) |
| **Bus Interfaces** | I2C (`0x24`), SPI, HSU (High-Speed UART 115200 baud) |
| **Interface Selection** | Onboard 2-bit DIP switch (`SEL0`, `SEL1`) |

## Pinout

### Standard Red PN532 Breakout Board Header & DIP Switches

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SDA` / `SS` / `TX` | Digital I/O | I2C `SDA` / SPI `SS` (CS) / HSU `TX` |
| 4 | `SCL` / `SCK` / `RX` | Digital Input | I2C `SCL` / SPI `SCK` / HSU `RX` |
| 5 | `MOSI` | Digital Input | SPI `MOSI` |
| 6 | `MISO` | Digital Output | SPI `MISO` |
| 7 | `IRQ` | Digital Output | Active-LOW Interrupt output (alerts MCU on card detection) |
| 8 | `RSTOUT` / `RST` | Digital Input | Hardware Reset pin |

## Bus Mode DIP Switch Configuration

The onboard 2-bit DIP switch (`SEL0`, `SEL1`) sets the active hardware communication interface:

| Bus Mode | `SEL0` Switch Position | `SEL1` Switch Position | Hardware Protocol Used |
|---|---|---|---|
| **I2C Mode** | **ON (0)** | **OFF (1)** | I2C (Address `0x24`, `SDA` & `SCL` pins) |
| **SPI Mode** | **OFF (1)** | **OFF (1)** | 4-Wire SPI (`SS`, `SCK`, `MOSI`, `MISO`) |
| **HSU Mode** | **OFF (1)** | **ON (0)** | High-Speed UART (`TX` & `RX` @ 115200 baud) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{BAT}$ | 2.7 | 3.3 / 5.0 | 5.5 | V | DC |
| Active Transmit Current | $I_{TX}$ | — | 100 | 150 | mA | RF field active |
| Power-Down Current | $I_{PD}$ | — | 1 | 5 | µA | Hard power-down |
| RF Output Power | $P_{RF}$ | — | 100 | — | mW | 13.56 MHz antenna driver |
| Operating Distance | $d_{range}$ | 0 | 30 | 50 | mm | Depends on antenna loop size |

## Wiring (I2C Mode Example)

| PN532 Module Pin | → | Microcontroller (Arduino Uno / ESP32) |
|---|---|---|
| `VCC` | | `5V` (or `3.3V`) |
| `GND` | | `GND` |
| `SDA` | | `SDA` (A4 on Uno, GPIO21 on ESP32) |
| `SCL` | | `SCL` (A5 on Uno, GPIO22 on ESP32) |
| `IRQ` | | GPIO Pin with Interrupt (e.g. D2 / GPIO4) |

> [!NOTE]
> DIP Switch Verification:
> For I2C mode, set DIP switch **`SEL0 = ON`** and **`SEL1 = OFF`**. Power cycle the PN532 module after changing DIP switches for new mode settings to take effect.

## Common mistakes

- **Changing DIP switches without power cycle:** The PN532 samples `SEL0` and `SEL1` pins ONLY during power-on reset. Changing DIP switch positions while powered on will not switch bus modes.
- **Forgetting I2C Pull-Up Resistors:** If using I2C mode on bare custom PCBs, place $4.7\text{ k}\Omega$ pull-up resistors on `SDA` and `SCL`.
- **Card Emulation Limits:** While the PN532 supports card emulation mode, iOS (Apple) and modern Android devices require Host Card Emulation (HCE) security keys. Emulating proprietary access cards may be restricted by smartphone OS security layers.

## Notes

- Compatible with Adafruit PN532 library, `NFCBridge`, and ESPHome `pn532` component.
