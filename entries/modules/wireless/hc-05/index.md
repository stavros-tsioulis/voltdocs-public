## Overview

The **HC-05** is a ubiquitous, low-cost Bluetooth Serial Port Profile (SPP) module designed for transparent wireless serial communication. Based on the Cambridge Silicon Radio (CSR) **BC417** Bluetooth chipset paired with an 8 Mbit flash memory, it converts standard UART serial communication into a Bluetooth RF link.

Unlike the slave-only HC-06 module, the HC-05 can operate in both **Master** and **Slave** roles, allowing two HC-05 modules to connect directly to each other without an external host device (e.g. smartphone or PC).

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.6 V – 6.0 V (Breakout board includes 3.3V LDO) |
| **I/O logic level** | 3.3 V (RX pin requires level shifting from 5V MCUs) |
| **Bluetooth standard** | Bluetooth v2.0 + EDR (2.4 GHz ISM band) |
| **Default baud rate (Data mode)** | 9600 bps, 8 data bits, 1 stop bit, no parity |
| **AT mode baud rate** | 38,400 bps |
| **Default PIN / Passkey** | `1234` or `0000` |
| **Operating current** | 30 mA (pairing) / 10 mA (connected) |

## Pinout

### Standard 6-Pin Breakout Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `STATE` | Digital Output | Connection status indicator (HIGH when connected, LOW when disconnected) |
| 2 | `RXD` | Digital Input | UART Serial Receive (3.3 V logic level; use voltage divider from 5V MCU) |
| 3 | `TXD` | Digital Output | UART Serial Transmit (3.3 V logic level output) |
| 4 | `GND` | Power | Ground (0 V) |
| 5 | `VCC` | Power | Power supply input (3.6 V – 6.0 V DC) |
| 6 | `EN` / `KEY` | Digital Input | Enable / AT Command mode control (HIGH forces AT command mode) |

## Specifications

| Parameter | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|
| Supply Voltage (`VCC`) | 3.6 | 5.0 | 6.0 | V | Breakout VCC |
| Logic Level High (`VIH`) | 2.0 | 3.3 | 3.6 | V | `RXD` / `KEY` pins |
| Logic Level Low (`VIL`) | -0.3 | 0 | 0.8 | V | `RXD` / `KEY` pins |
| RF Transmit Power | — | +4 | — | dBm | Class 2 Bluetooth |
| Sensitivity | — | -80 | — | dBm | BER < 0.1% |
| Transmission Distance | — | 10 | — | m | Line of sight |

## AT Command mode

To configure module settings (name, role, baud rate, passkey), the HC-05 must enter **AT command mode**:

1. Power off the module.
2. Hold down the onboard push button (or pull the `KEY` / `EN` pin `HIGH`).
3. Apply power to `VCC`. The onboard LED will flash slowly (once every 2 seconds), indicating AT mode at **38400 baud**.

### Common AT commands

> All AT commands must be terminated with `\r\n` (CR + LF).

| Command | Response | Description |
|---|---|---|
| `AT` | `OK` | Test command |
| `AT+NAME=MyModule` | `OK` | Set Bluetooth device name |
| `AT+PSWD="1234"` | `OK` | Set pairing password |
| `AT+ROLE=0` | `OK` | Set role: `0` = Slave (default), `1` = Master, `2` = Loopback |
| `AT+UART=9600,0,0` | `OK` | Set baud rate (9600), stop bit (0=1bit), parity (0=None) |
| `AT+ADDR?` | `+ADDR:<address>` | Query module Bluetooth MAC address |
| `AT+RESET` | `OK` | Soft reset and exit AT mode |

## Wiring

| HC-05 Breakout | :i-lucide-move-right: | Microcontroller (e.g. Arduino Uno / ESP32) |
|---|---|---|
| `VCC` | | 5 V |
| `GND` | | GND |
| `TXD` | | MCU RX (e.g. Pin 10 SoftwareSerial RX / GPIO 16) |
| `RXD` | | MCU TX via **Voltage Divider** (1kΩ / 2kΩ to GND) |
| `KEY` | | Digital GPIO or button (Optional, for AT mode) |

> [!WARNING] Connecting a 5V MCU TX pin directly to the HC-05 `RXD` pin without a voltage divider can degrade or destroy the 3.3V CSR BC417 input line over time. Use a 1kΩ / 2kΩ resistor voltage divider.

## Common mistakes

- **Direct 5V connection to RXD:** The HC-05 logic level is strictly 3.3V. Connect a 1kΩ / 2kΩ voltage divider between MCU TX (5V) and HC-05 RXD (3.3V).
- **Wrong baud rate in AT mode:** When entering AT mode via the button-press method, the module fixedly communicates at **38400 baud**, regardless of the configured data baud rate (e.g., 9600).
- **Swap RX and TX lines:** Remember to connect HC-05 `TXD` to MCU `RX`, and HC-05 `RXD` to MCU `TX`.

## Notes

- **HC-05 vs HC-06:** The HC-06 has only 4 pins and operates exclusively as a Slave. The HC-05 has 6 pins, an onboard button, and supports both Master and Slave operation modes.
