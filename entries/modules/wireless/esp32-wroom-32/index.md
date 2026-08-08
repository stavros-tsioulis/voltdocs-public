## Overview

The **ESP32-WROOM-32** (and variants ESP32-WROOM-32D / 32E) is a flagship Wi-Fi + Bluetooth + Bluetooth LE microcontroller module developed by Espressif Systems. At its core is the **ESP32-D0WDQ6** dual-core 32-bit Tensilica Xtensa LX6 microprocessor operating up to 240 MHz.

Targeted at IoT edge devices, robotics, smart home automation (ESPHome, Home Assistant), audio streaming, and wearable electronics, it integrates 4 MB SPI flash memory, 520 KB SRAM, cryptographic hardware accelerators, and a rich set of peripherals including capacitive touch, ADC, DAC, I2S, SPI, I2C, UART, and CAN bus.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.0 V to 3.6 V DC (3.3 V nominal) |
| **Processor** | Dual-Core 32-bit Xtensa LX6 (up to 240 MHz, 600 DMIPS) |
| **Internal SRAM** | 520 KB SRAM (including 8 KB RTC FAST/SLOW memory) |
| **External SPI Flash** | 4 MB (up to 16 MB option) |
| **Wi-Fi** | 802.11 b/g/n (up to 150 Mbps) |
| **Bluetooth** | Bluetooth v4.2 BR/EDR and BLE |
| **ADC / DAC** | 18-channel 12-bit SAR ADC, 2-channel 8-bit DAC |
| **Deep Sleep current** | $5\text{ }\mu\text{A}$ (RTC timer active) |

## Pinout

### Standard 30-Pin ESP32 DevKit Breakout Pinout

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `EN` / `RST` | Digital Input | Enable / Reset pin (Active-HIGH, pull HIGH to run) |
| 2 | `VP` / `GPIO36` | Analog Input | ADC1_CH0 / RTC_GPIO0 (Input only) |
| 3 | `VN` / `GPIO39` | Analog Input | ADC1_CH3 / RTC_GPIO3 (Input only) |
| 4 | `GPIO34` | Analog Input | ADC1_CH6 (Input only, no internal pull-up/down) |
| 5 | `GPIO35` | Analog Input | ADC1_CH7 (Input only, no internal pull-up/down) |
| 6 | `GPIO32` | Touch / I/O | Touch9 / ADC1_CH4 / XTAL32 |
| 7 | `GPIO33` | Touch / I/O | Touch8 / ADC1_CH5 / XTAL32 |
| 8 | `GPIO25` | DAC / I/O | DAC1 / ADC2_CH8 / RTC_GPIO6 |
| 9 | `GPIO26` | DAC / I/O | DAC2 / ADC2_CH9 / RTC_GPIO7 |
| 10 | `GPIO27` | Touch / I/O | Touch7 / ADC2_CH17 |
| 11 | `GPIO14` | Touch / I/O | Touch6 / ADC2_CH16 / HSPI_CLK |
| 12 | `GPIO12` | Touch / I/O | Touch5 / ADC2_CH15 / HSPI_MISO (Boot strapping pin!) |
| 13 | `GPIO13` | Touch / I/O | Touch4 / ADC2_CH14 / HSPI_MOSI |
| 14 | `GND` | Power | Ground (0 V) |
| 15 | `VIN` / `5V` | Power | 5 V DC supply input (feeds onboard 3.3V LDO regulator) |
| 16 | `GPIO23` | Digital I/O | VSPI_MOSI |
| 17 | `GPIO22` | Digital I/O | I2C `SCL` |
| 18 | `GPIO1` | Digital Output | UART0 `TX` |
| 19 | `GPIO3` | Digital Input | UART0 `RX` |
| 20 | `GPIO21` | Digital I/O | I2C `SDA` |
| 21 | `GPIO19` | Digital I/O | VSPI_MISO |
| 22 | `GPIO18` | Digital I/O | VSPI_CLK |
| 23 | `GPIO5` | Digital I/O | VSPI_CS (Boot strapping pin!) |
| 24 | `GPIO17` | Digital I/O | UART2 `TX` |
| 25 | `GPIO16` | Digital I/O | UART2 `RX` |
| 26 | `GPIO4` | Touch / I/O | Touch0 / ADC2_CH0 |
| 27 | `GPIO0` | Touch / I/O | Touch1 / ADC2_CH1 (Boot Mode: LOW = Flash, HIGH = Run) |
| 28 | `GPIO2` | Touch / I/O | Touch2 / ADC2_CH2 (Must be floating or LOW during flashing) |
| 29 | `GPIO15` | Touch / I/O | Touch3 / ADC2_CH3 / HSPI_CS |
| 30 | `3V3` | Power Output | Regulated +3.3 V DC output (or 3.3V power input) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 3.0 | 3.3 | 3.6 | V | DC |
| Peak Supply Current | $I_{peak}$ | — | 240 | 500 | mA | Wi-Fi TX burst at full power |
| Modem-Sleep Current | $I_{modem}$ | — | 20 | 30 | mA | CPU 240MHz active, radio idle |
| Light-Sleep Current | $I_{light}$ | — | 0.8 | 1.0 | mA | CPU paused, ULP / RTC active |
| Deep-Sleep Current | $I_{deep}$ | — | 5 | 10 | µA | RTC timer active |
| Hibernation Current | $I_{hib}$ | — | 2.5 | 5 | µA | RTC memory off |
| Max GPIO Sink/Source | $I_{GPIO}$ | — | 12 | 40 | mA | Per pin maximum |

## Strapping pins & Boot configuration

| Pin | Default | Function | Strapping State |
|---|---|---|---|
| `GPIO0` | Pull-up | Boot Mode | `LOW` = ROM Serial Flasher, `HIGH` = SPI Flash Boot |
| `GPIO2` | Pull-down | Boot Mode / LED | Must be `LOW` or left floating during serial flashing |
| `GPIO5` | Pull-up | SDIO Slave Timing | Must be `HIGH` during boot |
| `GPIO12` | Pull-down | Flash Voltage ($V_{SPI}$) | `LOW` = 3.3V Flash (Default), `HIGH` = 1.8V Flash |
| `GPIO15` | Pull-up | Silence Boot Log | `HIGH` = Output debug log on TXD0 at 115200 baud |

> [!WARNING]
> GPIO Limitations & Gotchas:
> - **Input-Only Pins:** `GPIO34`, `GPIO35`, `GPIO36` (VP), and `GPIO39` (VN) are **Input-only**. They have no internal pull-up or pull-down resistors and cannot be used as outputs.
> - **ADC2 & Wi-Fi Conflict:** `ADC2` channels (`GPIO0`, `2`, `4`, `12`–`15`, `25`–`27`) cannot be used when Wi-Fi is active. Use `ADC1` (`GPIO32`–`39`) for analog readings when using Wi-Fi.
> - **GPIO12 1.8V LDO Trap:** If `GPIO12` is pulled HIGH during power-up, the ESP32 sets internal flash voltage to 1.8V, causing 3.3V SPI flash chips to fail and placing the ESP32 in a boot loop (`flash read err`).

## Common mistakes

- **Holding GPIO0 LOW after flashing:** If `GPIO0` is connected to GND via a jumper, the ESP32 will continuously enter bootloader mode upon reset instead of running application code.
- **Powering external high-current devices from 3V3 pin:** The onboard 3.3V LDO on DevKit boards has a max output limit of ~500 mA. Powering motors, servos, or heavy LED strips from the 3V3 pin will overheat the regulator.
- **Reading ADC2 while Wi-Fi is transmitting:** Code calling `analogRead()` on ADC2 pins returns `NaN` or incorrect values once `WiFi.begin()` is invoked. Always route analog sensors to `ADC1` pins.

## Notes

- Supports FreeRTOS natively with dual-core task pinning using `xTaskCreatePinnedToCore()`.
