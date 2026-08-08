## Overview

The **SIM800L** is a miniature quad-band GSM/GPRS cellular transceiver module manufactured by SIMCom Wireless Solutions. It operates across 850/900/1800/1900 MHz frequencies to deliver SMS text messaging, voice calling, and GPRS mobile data packet connectivity for embedded IoT applications.

The module features a 3.7V–4.2V operating voltage range (tailored for direct 1S LiPo battery power), a Micro-SIM card slot, IPEX antenna connector, and standard AT command UART control interface.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | 3.4 V to 4.4 V DC (**4.0 V recommended**, e.g. 1S LiPo or high-current LDO) |
| **Peak Burst Current** | **Up to 2.0 A** during GSM RF transmission bursts |
| **Quad-Band Frequencies** | GSM 850 / EGSM 900 / DCS 1800 / PCS 1900 MHz |
| **UART Logic Level** | 2.8 V TTL (requires level shifter for 5V MCUs) |
| **Default Baud Rate** | Auto-baud / 115200 bps |
| **SIM Card Socket** | Micro-SIM (1.8V / 3.0V supported) |
| **GPRS Data Rate** | Download: 85.6 kbps / Upload: 85.6 kbps (Class 12) |

## Pinout

### Standard Red SIM800L Breakout Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `NET` | Antenna / Net status | Connects to wire helical antenna / Network LED status output |
| 2 | `VCC` | Power Input | Supply voltage (+3.4 V to +4.4 V DC, **MUST support 2A bursts**) |
| 3 | `RST` | Digital Input | Active-LOW Reset input pin |
| 4 | `RXD` | Digital Input | UART Receive line (2.8V logic level input) |
| 5 | `TXD` | Digital Output | UART Transmit line (2.8V logic level output) |
| 6 | `GND` | Power | Ground (0 V) |
| 7 | `RING` | Digital Output | Ring Indicator line (pulls LOW on incoming call or SMS) |
| 8 | `DTR` | Digital Input | Sleep Mode control pin (`HIGH` = Enable Sleep mode) |
| 9 | `MIC+`, `MIC-` | Audio Input | Electret Microphone differential inputs |
| 10 | `SPK+`, `SPK-` | Audio Output | 8 Ω Speaker differential outputs |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Operating Voltage | $V_{BAT}$ | 3.4 | 4.0 | 4.4 | V | DC |
| Peak Transmit Current | $I_{PEAK}$ | — | 2.0 | 2.5 | A | GSM RF burst transmission |
| Idle Current | $I_{IDLE}$ | — | 7.0 | — | mA | Registered to network |
| Sleep Current | $I_{SLEEP}$ | — | 0.7 | 1.0 | mA | Sleep mode ($DTR = HIGH$) |
| Transmit Power (Class 4) | $P_{TX900}$ | — | 2.0 | — | W | 33 dBm @ 850/900 MHz |
| Transmit Power (Class 1) | $P_{TX1800}$ | — | 1.0 | — | W | 30 dBm @ 1800/1900 MHz |

## AT Command Set Examples

Set terminal to 115200 baud with `\r\n` (CRLF) line endings:

| Command | Expected Response | Description |
|---|---|---|
| `AT` | `OK` | Test module UART connection |
| `AT+CPIN?` | `+CPIN: READY` | Check if SIM card is inserted and unlocked |
| `AT+CSQ` | `+CSQ: 22,0` | Check signal strength (First number $> 10$ is good signal) |
| `AT+CREG?` | `+CREG: 0,1` | Check cellular registration (`0,1` = Registered home network) |
| `AT+CMGF=1` | `OK` | Set SMS text mode |
| `AT+CMGS="+1234567890"` | `>` | Send SMS (type body, end with `Ctrl+Z` / `0x1A`) |
| `ATD+1234567890;` | `OK` | Place voice call |

## Wiring

| SIM800L Breakout Pin | → | Power Supply / Microcontroller | Notes |
|---|---|---|---|
| `VCC` | | **External 4.0V / 2A Power Source** (LM2596 buck or 1S LiPo) | **Do NOT power from Arduino 5V / 3.3V pins!** |
| `GND` | | Common `GND` (Power GND + MCU GND) | Must share ground |
| `TXD` | | `RX` (e.g. GPIO16 on ESP32 / D2 on Arduino) | 2.8V TTL output |
| `RXD` | | `TX` (e.g. GPIO17 on ESP32 / D3 on Arduino) | **Use 1kΩ/2kΩ voltage divider from 5V MCU** |

> [!WARNING]
> Critical Power Supply Requirement & Voltage Warning:
> - **Voltage Window:** The SIM800L operating voltage range is strictly **3.4 V to 4.4 V**. Feeding 5.0 V directly to `VCC` will destroy the SIM800L chip! Supplying $<3.4\text{ V}$ causes brownout resets.
> - **Peak Current:** The module demands **up to 2.0 A bursts** during network transmission. If powered from an inadequate supply, the module will repeatedly reboot (LED blinks rapidly once per second continuously). Place a $1000\text{ }\mu\text{F}$ low-ESR electrolytic capacitor across `VCC` and `GND`.

## Common mistakes

- **Powering from Arduino 5V or 3.3V pins:** Microcontroller onboard regulators cannot supply 2.0 A current bursts, causing infinite reboot loops.
- **2G Network Availability:** SIM800L is a 2G-only module. In countries where 2G networks have been decommissioned (e.g. USA, Australia), 2G modules cannot register on cellular towers. Use LTE Cat-M1 / NB-IoT modules (e.g. SIM7000G / SIM7600) instead.
- **Forgetting common ground:** MCU and external power supply grounds MUST be connected together.

## Notes

- Network LED status: Blinking every 1s = Searching for network; Blinking every 3s = Registered on network.
