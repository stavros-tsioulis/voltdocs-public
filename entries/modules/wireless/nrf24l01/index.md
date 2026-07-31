## Overview

The **nRF24L01+** (revision 2.0) is Nordic Semiconductor's current, upgraded revision of the nRF24L01 transceiver IC. It integrates a 2.4 GHz RF synthesizer, power amplifier, crystal oscillator, demodulator, and the proprietary **Enhanced ShockBurst™** hardware protocol engine.

Compared to the legacy nRF24L01 (v1.0), the **nRF24L01+** adds a **250 kbps** air data rate mode for significantly extended RF range (-94 dBm sensitivity), dynamic payload length capability, Received Power Detector (RPD), and an increased SPI bus clock speed up to 10 MHz.

## Quick reference

| | |
|---|---|
| **Frequency band** | 2.400 GHz – 2.525 GHz (125 channels) |
| **Operating voltage** | 1.9 V – 3.6 V (5 V tolerant I/O pins) |
| **Data rates** | 250 kbps, 1 Mbps, 2 Mbps |
| **Max output power** | 0 dBm (1 mW) |
| **RX sensitivity** | -94 dBm @ 250 kbps / -85 dBm @ 1 Mbps / -82 dBm @ 2 Mbps |
| **Current draw (TX @ 0dBm)** | 11.3 mA |
| **Current draw (RX @ 2Mbps)** | 13.5 mA |
| **Interface** | SPI (up to 10 MHz) + CE & IRQ |

## Pinout

### Standard 8-pin module header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` | Power | Ground (0 V) |
| 2 | `VCC` | Power | Supply voltage (1.9 V – 3.6 V max) |
| 3 | `CE` | Digital Input | Chip Enable (activates RX or TX mode when active HIGH) |
| 4 | `CSN` | Digital Input | SPI Chip Select (Active LOW) |
| 5 | `SCK` | Digital Input | SPI Clock (up to 10 MHz) |
| 6 | `MOSI` | Digital Input | SPI Master Out Slave In |
| 7 | `MISO` | Digital Output | SPI Master In Slave Out |
| 8 | `IRQ` | Digital Output | Interrupt Request pin (Active LOW, optional) |

## Specifications

| Parameter | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|
| Supply voltage | 1.9 | 3.0 | 3.6 | V | Operating range |
| Input High voltage | 2.0 | — | 5.25 | V | 5V-tolerant control pins |
| Output power | -18 | 0 | 0 | dBm | Programmable (0, -6, -12, -18 dBm) |
| RX sensitivity | — | -94 | -82 | dBm | At 250 kbps (-94 dBm), 2 Mbps (-82 dBm) |
| Power-down current | — | 900 | — | nA | PWR_UP = 0 |
| Standby-I current | — | 26 | — | µA | PWR_UP = 1, CE = 0 |

## Register map

| Address | Register | Access | Reset | Description |
|---|---|---|---|---|
| `0x00` | `CONFIG` | R/W | `0x08` | Configuration (CRC, PWR_UP, PRIM_RX) |
| `0x01` | `EN_AA` | R/W | `0x3F` | Enable Auto Acknowledgment on pipes 0–5 |
| `0x02` | `EN_RXADDR` | R/W | `0x03` | Enable RX data pipes (P0, P1 by default) |
| `0x03` | `SETUP_AW` | R/W | `0x03` | Setup of Address Widths (3, 4, or 5 bytes) |
| `0x04` | `SETUP_RETR` | R/W | `0x03` | Setup of Automatic Retransmission |
| `0x05` | `RF_CH` | R/W | `0x02` | RF Channel (2400 + channel MHz) |
| `0x06` | `RF_SETUP` | R/W | `0x0E` | RF Setup (Data rate, RF output power) |
| `0x07` | `STATUS` | R/W | `0x0E` | Status register (RX_DR, TX_DS, MAX_RT) |
| `0x09` | `RPD` | R | `0x00` | Received Power Detector (> -64 dBm) |
| `0x1C` | `DYNPD` | R/W | `0x00` | Enable dynamic payload length per pipe |
| `0x1D` | `FEATURE` | R/W | `0x00` | Feature register (Dynamic payload, ACK payload) |

## Wiring

| nRF24L01+ Module | :i-lucide-move-right: | Microcontroller (e.g. Arduino / ESP32) |
|---|---|---|
| `VCC` | | **3.3 V** (Do NOT connect to 5V!) |
| `GND` | | GND |
| `CE` | | Digital GPIO (e.g., D9 / GPIO 4) |
| `CSN` | | Digital GPIO (e.g., D10 / GPIO 5) |
| `SCK` | | SPI SCK (e.g., D13 / GPIO 18) |
| `MOSI` | | SPI MOSI (e.g., D11 / GPIO 23) |
| `MISO` | | SPI MISO (e.g., D12 / GPIO 19) |

> [!WARNING] Connecting `VCC` to a 5 V supply will destroy the nRF24L01+ IC. While data pins (`CSN`, `SCK`, `MOSI`, `CE`) are 5 V tolerant, `VCC` must strictly be between 1.9 V and 3.6 V.

## Common mistakes

- **Power supply noise / insufficient decoupling:** The nRF24L01+ is sensitive to supply noise and power dips during RF transmission. Always solder a 10 µF electrolytic or tantalum capacitor directly across `VCC` and `GND` on the module header.
- **Connecting VCC to 5V:** The chip requires 3.3V power.
- **Mismatched RF channel or data rate:** Both transmitter and receiver must use identical RF channels (`RF_CH`) and data rates (`RF_SETUP`).

## Revision history

- **v2.0 / nRF24L01+ (Current):** Upgraded silicon revision adding 250 kbps long-range mode (-94 dBm sensitivity), 10 MHz SPI clock, RPD register (`0x09`), and dynamic payload support (`DYNPD` / `FEATURE` registers).
- **v1.0 (Deprecated):** Original nRF24L01 silicon release — supports 1 Mbps and 2 Mbps rates only. See [revision 1.0](revisions/1.0/index.md).
