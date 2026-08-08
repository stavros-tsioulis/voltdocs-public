## Overview

The **HC-06** is a popular slave-only Bluetooth 2.0 + EDR (Enhanced Data Rate) serial pass-through module built around the Cambridge Silicon Radio (CSR) BC417 chipset. It creates a transparent wireless UART serial bridge between microcontrollers and Bluetooth-enabled master devices (such as Android smartphones, laptops, or PCs).

Unlike the dual-mode HC-05 (which can operate as master or slave), the HC-06 is hardcoded as a **Slave device** only. It remains in AT command configuration mode whenever it is un-paired, and automatically transitions to transparent serial bridge mode as soon as a master device connects.

## Quick reference

| | |
|---|---|
| **Baseboard supply (`VCC`)** | 3.6 V to 6.0 V DC (5 V recommended) |
| **UART logic level** | 3.3 V TTL (requires resistor divider when receiving from 5V MCU) |
| **Bluetooth specification** | Bluetooth v2.0 + EDR (SPP - Serial Port Profile) |
| **Default UART configuration** | 9600 baud, 8 data bits, 1 stop bit, no parity (`9600,N,8,1`) |
| **Default PIN code** | `1234` or `0000` |
| **Default device name** | `HC-06` |
| **Operating mode** | Slave only (cannot initiate connections to other devices) |

## Pinout

### Standard 4-Pin Baseboard Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `STATE` / `NC` | Digital Output | Connection status indicator (`HIGH` = Connected, `LOW` = Unconnected) |
| 2 | `RXD` | Digital Input | UART Receive line (3.3V TTL logic level) |
| 3 | `TXD` | Digital Output | UART Transmit line (3.3V TTL logic level) |
| 4 | `GND` | Power | Ground (0 V) |
| 5 | `VCC` | Power | Supply voltage input (+3.6 V to +6.0 V DC) |
| 6 | `EN` / `KEY` | Digital Input | Unused on standard HC-06 modules |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 3.6 | 5.0 | 6.0 | V | DC |
| Logic Level High | $V_{IH}$ | 2.0 | 3.3 | 3.6 | V | `RXD` pin |
| Logic Level Low | $V_{IL}$ | -0.3 | 0 | 0.8 | V | `RXD` pin |
| Pairing Current | $I_{pair}$ | 30 | 35 | 40 | mA | LED blinking fast (Searching) |
| Connected Current | $I_{conn}$ | 8 | 10 | 12 | mA | Connected and transmitting |
| RF Transmit Power | $P_{TX}$ | — | +4 | — | dBm | Class 2 radio (~10m distance) |
| Baud Rate Range | $BR$ | 1200 | 9600 | 1382400 | bps | Programmable via AT commands |

## AT Command Set (Unconnected State Only)

When the HC-06 is powered ON and NOT connected to a Bluetooth master (onboard LED flashing red at 2 Hz):
- Send AT commands over UART **without carriage return (`\r`) or line feed (`\n`)**.
- Every valid AT command receives an immediate string response.

| Command | Expected Response | Description |
|---|---|---|
| `AT` | `OK` | Test UART communication |
| `AT+VERSION` | `OKlinvorV1.8` | Query firmware version |
| `AT+NAMEmydevice` | `OKsetname` | Change Bluetooth broadcast name to "mydevice" |
| `AT+PIN5678` | `OKsetPIN` | Change pairing PIN code to "5678" |
| `AT+BAUD4` | `OK9600` | Set baud rate (`4` = 9600, `5` = 19200, `6` = 38400, `7` = 57600, `8` = 115200) |

## Wiring

| HC-06 Baseboard Pin | → | Microcontroller (Arduino Uno / ESP32) | Notes |
|---|---|---|---|
| `VCC` | | `5V` | Onboard 3.3V LDO input |
| `GND` | | `GND` | Ground |
| `TXD` | | `RX` (e.g. D2 for SoftwareSerial / GPIO16) | 3.3V output (5V MCU inputs read 3.3V as HIGH) |
| `RXD` | | `TX` (e.g. D3 for SoftwareSerial / GPIO17) | **Requires 1kΩ / 2kΩ voltage divider from 5V MCUs** |

> [!WARNING]
> RXD 3.3V Logic Level Protection:
> The HC-06 `RXD` pin is NOT 5V tolerant. Connecting an Arduino 5V TX pin directly to `RXD` will degrade or destroy the CSR BC417 chip over time. Use a $1\text{ k}\Omega$ and $2\text{ k}\Omega$ resistor voltage divider on `RXD`.

## Common mistakes

- **Sending `\r\n` (CRLF) with AT commands:** Unlike the HC-05 (which requires `\r\n`), sending `\r\n` to an HC-06 causes AT command parsing to fail. Configure serial monitor to "No line ending".
- **Attempting to configure AT commands while paired:** Once connected to a smartphone or PC (LED stays solid ON), the HC-06 enters transparent pass-through mode and ignores AT commands.
- **Expecting Master mode operation:** The HC-06 cannot scan for or initiate connections to other Bluetooth modules (such as a Bluetooth sensor or barcode scanner). Use an **HC-05** if Master mode is required.

## Notes

- HC-06 uses classic Bluetooth 2.0 SPP (Serial Port Profile). iOS (Apple) devices do NOT support classic SPP; use **BLE (Bluetooth Low Energy) modules such as HM-10 or ESP32** for iOS compatibility.
