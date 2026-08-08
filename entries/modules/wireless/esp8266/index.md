## Overview

The **ESP8266** (and ESP8266EX) is a highly integrated 32-bit Wi-Fi micro-module developed by Espressif Systems. It combines a 32-bit Tensilica Xtensa L106 RISC processor core running up to 160 MHz, full 802.11 b/g/n Wi-Fi radio capabilities, TCP/IP stack, and GPIO peripherals on a single chip.

It is widely available as standalone breakout modules (ESP-01, ESP-12E / ESP-12F) and complete development boards (NodeMCU, Wemos D1 Mini) with USB-to-UART programmers and 3.3V power regulation onboard.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.0 V to 3.6 V DC (3.3 V nominal) |
| **CPU** | 32-bit Tensilica Xtensa L106 RISC (80 MHz / 160 MHz) |
| **SRAM** | 80 KB Instruction RAM + 50 KB Data RAM |
| **External SPI Flash** | Typically 1 MB (ESP-01) or 4 MB (ESP-12E/F, NodeMCU) |
| **Wi-Fi protocol** | 802.11 b/g/n (2.4 GHz, WPA/WPA2 Personal & Enterprise) |
| **Peak Transmit Current** | Up to 170 mA (during Wi-Fi TX bursts) |
| **Deep Sleep Current** | ~20 µA |
| **Analog ADC Input** | 1 Channel (0.0 V to 1.0 V bare chip / 0.0 V to 3.3 V on NodeMCU) |

## Pinout

### ESP-01 Header Pinout (8-Pin 2x4 0.1" Header)

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` | Power | Ground (0 V) |
| 2 | `GPIO2` | Digital I/O | General purpose I/O / Boot config pin (must be HIGH on boot) |
| 3 | `GPIO0` | Digital I/O | General purpose I/O / Boot mode (LOW = Flash mode, HIGH = Normal) |
| 4 | `RXD` | Digital Input | UART Receive line (GPIO3) |
| 5 | `TXD` | Digital Output | UART Transmit line (GPIO1) |
| 6 | `CH_PD` / `EN` | Digital Input | Chip Enable (MUST be tied HIGH to 3.3V to run) |
| 7 | `RST` | Digital Input | Active-LOW Hardware Reset |
| 8 | `VCC` | Power | Supply voltage (+3.3 V DC only) |

### ESP-12E / ESP-12F Module Strapping Pins & Boot Modes

| Boot Mode | `GPIO15` | `GPIO0` | `GPIO2` |
|---|---|---|---|
| **Flash Boot (Normal Run)** | `LOW` (GND) | `HIGH` (3.3V) | `HIGH` (3.3V) |
| **UART Download (Flash Programming)** | `LOW` (GND) | `LOW` (GND) | `HIGH` (3.3V) |
| **SD-Card Boot** | `HIGH` (3.3V) | `LOW` (GND) | `HIGH` (3.3V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Operating Voltage | $V_{CC}$ | 3.0 | 3.3 | 3.6 | V | DC |
| TX Current (802.11b, +19.5dBm) | $I_{TX}$ | — | 170 | 220 | mA | Peak burst power |
| RX Current (802.11b/g/n) | $I_{RX}$ | — | 56 | 60 | mA | Active reception |
| Modem-Sleep Current | $I_{modem}$ | — | 15 | 20 | mA | CPU active, Wi-Fi disabled |
| Deep-Sleep Current | $I_{sleep}$ | — | 20 | 30 | µA | RTC active (`RST` tied to `GPIO16`) |
| GPIO Max Drive Current | $I_{GPIO}$ | — | 12 | 12 | mA | Per pin sink/source |
| Operating Temperature | $T_{OP}$ | -40 | — | 125 | °C | |

## Wiring & Bare-Module Hookup (ESP-01 / ESP-12)

| ESP8266 Pin | Connection Target | Notes |
|---|---|---|
| `VCC` | +3.3 V Power Supply | **Requires dedicated 3.3V regulator capable of 300 mA** |
| `GND` | Common Ground (0 V) | Ground connection |
| `CH_PD` / `EN` | +3.3 V | $10\text{ k}\Omega$ pull-up resistor to 3.3V |
| `RST` | +3.3 V | $10\text{ k}\Omega$ pull-up resistor to 3.3V (Momentary switch to GND to reset) |
| `GPIO15` (ESP-12) | Ground | $10\text{ k}\Omega$ pull-down resistor to GND |
| `GPIO0` | +3.3 V (Run) / GND (Program) | $10\text{ k}\Omega$ pull-up resistor to 3.3V (Switch to GND to Flash) |
| `GPIO2` | +3.3 V | $10\text{ k}\Omega$ pull-up resistor to 3.3V |

> [!WARNING]
> 3.3V Logic & Power Supply Requirements:
> - **ESP8266 GPIO pins are NOT 5V tolerant.** Connecting 5V signals to any GPIO pin risks permanent damage.
> - **The 3.3V rail of an Arduino Uno cannot power an ESP8266.** Peak Wi-Fi TX current pulses ($> 200\text{ mA}$) will cause the Arduino LDO to collapse, resulting in endless bootloops. Use an external 3.3V LDO (such as AMS1117-3.3) with a $100\text{ }\mu\text{F}$ decoupling capacitor.

## Common mistakes

- **Powering from Arduino 3.3V pin:** Causes continuous bootloops (`rst cause:4, bootmode:(3,6)`) due to supply rail voltage sag during Wi-Fi initialization.
- **Floating `CH_PD` / `EN` pin:** Leaving Chip Enable unconnected keeps the internal LDO turned off, rendering the board completely dead.
- **Incorrect strapping pin state at boot:** If `GPIO15` is pulled HIGH or `GPIO0` is held LOW on boot, the chip will refuse to execute application code from SPI flash.
- **Deep Sleep wake-up pin missing:** To wake from Deep Sleep, `GPIO16` MUST be connected to the `RST` pin so the internal RTC timer can pulse `RST` LOW to restart the CPU.

## Notes

- Programmable directly from the Arduino IDE, ESP-IDF, MicroPython, or ESPHome.
