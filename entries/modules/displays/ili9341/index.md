## Overview

The **ILI9341** is an a-Si TFT-LCD driver IC manufactured by ILITEK (ILI Technology). It drives **240x320 pixel (QVGA)** resolution full-color displays with up to 262,144 colors (18-bit) or 65,536 colors (16-bit RGB565).

It is universally used on 2.2-inch, 2.4-inch, 2.8-inch, and 3.2-inch color display breakout modules and Arduino Uno/Mega display shields (often bundled with an XPT2046 resistive touch controller and SD card socket).

## Quick reference

| | |
|---|---|
| **Module VCC** | 3.3 V to 5.0 V DC (onboard LDO) |
| **Chip VCI / VDDIO** | 2.3 V to 3.3 V DC |
| **Resolution** | $240 \times 320$ pixels (QVGA) |
| **Color Depth** | 16-bit RGB565 (65,536 colors) or 18-bit RGB666 (262,144 colors) |
| **GRAM Buffer** | $240 \times 320 \times 18\text{ bits}$ ($172,800\text{ bytes}$ frame buffer) |
| **Communication interfaces** | 4-wire SPI (up to 10 MHz write clock), 8-bit / 16-bit parallel |
| **Backlight Current** | ~80 mA at 3.3V (4-LED backlight array) |

## Pinout

### Standard 14-Pin Red SPI TFT Breakout Header (with Touch & SD Card)

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `CS` | Digital Input | LCD SPI Chip Select (Active-LOW) |
| 4 | `RESET` | Digital Input | LCD Active-LOW Reset line |
| 5 | `DC` / `RS` | Digital Input | LCD Data/Command control (`LOW` = Command, `HIGH` = Data) |
| 6 | `SDI` / `MOSI` | Digital Input | LCD SPI Master Output Slave Input |
| 7 | `SCK` | Digital Input | LCD SPI Serial Clock input |
| 8 | `LED` / `BL` | Power / PWM | Backlight Control (+3.3 V DC or PWM input) |
| 9 | `SDO` / `MISO` | Digital Output | LCD SPI Master Input Slave Output |
| 10 | `T_CLK` | Digital Input | Touch Controller SPI Clock |
| 11 | `T_CS` | Digital Input | Touch Controller SPI Chip Select |
| 12 | `T_DIN` | Digital Input | Touch Controller SPI Data Input (MOSI) |
| 13 | `T_DO` | Digital Output | Touch Controller SPI Data Output (MISO) |
| 14 | `T_IRQ` | Digital Output | Touch Controller Interrupt Output (Active-LOW) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{CC}$ | 3.3 | 5.0 | 5.5 | V | DC |
| Supply Voltage (Chip VCI) | $V_{CI}$ | 2.5 | 2.8 | 3.3 | V | DC |
| Logic High Input | $V_{IH}$ | $0.7 V_{IO}$ | — | $V_{IO}$ | V | SPI control lines |
| Logic Low Input | $V_{IL}$ | 0 | — | $0.3 V_{IO}$ | V | SPI control lines |
| Driver Operating Current | $I_{CC}$ | — | 15 | 20 | mA | Display active |
| Backlight Current | $I_{LED}$ | — | 80 | 100 | mA | $V_{LED} = 3.3\text{ V}$ |
| SPI Write Clock Cycle | $t_{SCWC}$ | 100 | — | — | ns | Up to 10 MHz write clock |

## Key Command Table

| Address Hex | Command Name | Description |
|---|---|---|
| `0x01` | `SWRESET` | Software Reset command |
| `0x11` | `SLPOUT` | Sleep Out (Exit sleep mode, enable DC-DC converter) |
| `0x28` / `0x29` | `DISPOFF` / `DISPON` | Display OFF / Display ON |
| `0x2A` | `CASET` | Column Address Set ($X_{start}$ to $X_{end}$, 0 to 239) |
| `0x2B` | `PASET` | Page Address Set ($Y_{start}$ to $Y_{end}$, 0 to 319) |
| `0x2C` | `RAMWR` | Memory Write (Stream RGB565 16-bit pixel data) |
| `0x36` | `MADCTL` | Memory Access Control (Orientation: Portrait, Landscape, Flip) |
| `0x3A` | `COLMOD` | Pixel Format Set (`0x55` = 16-bit RGB565) |

## Wiring

| ILI9341 Module Pin | → | Microcontroller (Arduino / ESP32) |
|---|---|---|
| `VCC` | | `5V` (or `3.3V`) |
| `GND` | | `GND` |
| `CS` | | SPI `SS` (e.g. D10 on Uno / GPIO5 on ESP32) |
| `RESET` | | GPIO Pin (e.g. D8 on Uno / GPIO4 on ESP32) |
| `DC` | | GPIO Pin (e.g. D9 on Uno / GPIO2 on ESP32) |
| `SDI` / `MOSI` | | SPI `MOSI` (D11 on Uno / GPIO23 on ESP32) |
| `SCK` | | SPI `SCK` (D13 on Uno / GPIO18 on ESP32) |
| `LED` | | `3.3V` (or PWM GPIO Pin) |

> [!WARNING]
> 3.3V Logic Level Warning:
> The ILI9341 chip inputs are strictly **3.3V TTL logic level**. Connecting 5V SPI signals directly from an Arduino Uno to `CS`, `RESET`, `DC`, `MOSI`, and `SCK` will damage the controller. Use a CD4050 buffer or $1\text{ k}\Omega / 2\text{ k}\Omega$ resistor dividers.

## Common mistakes

- **Leaving Backlight (`LED`) pin disconnected:** Disconnected LED backlight pin results in a completely black, unlit screen. Connect `LED` to 3.3V.
- **Slow software SPI / Bit-banging:** Sending $240 \times 320 \times 2\text{ bytes} = 153,600\text{ bytes}$ per full screen frame over slow software SPI results in noticeable screen tearing and low FPS. Use hardware SPI DMA peripherals (such as `TFT_eSPI` on ESP32).
- **Confusing LCD SPI and Touch SPI:** The LCD display (ILI9341) and the touch controller (XPT2046) share the MOSI, MISO, and SCK lines but require **separate Chip Select (`CS` and `T_CS`) pins**.

## Notes

- Highly optimized libraries include `TFT_eSPI` (ESP32 / RP2040), `Adafruit_ILI9341`, and ESPHome `ili9341` platform component.
