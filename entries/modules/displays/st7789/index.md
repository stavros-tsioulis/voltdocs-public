## Overview

The **ST7789** (and variants ST7789V / ST7789VI) is a single-chip controller/driver for 262,144-color graphic TFT-LCD displays manufactured by Sitronix. Designed for mobile, wearable, and smart home IoT interfaces, it incorporates an internal frame buffer ($240 \times 320 \times 18\text{-bit}$ RAM) and drives high-density IPS color display panels over a fast 4-wire SPI bus supporting clock rates up to 62.5 MHz.

Popular breakout modules feature square $240 \times 240$ (1.3" / 1.54") or rectangular $240 \times 320$ (2.0" / 2.4") IPS screens offering vivid color saturation and wide viewing angles for ESP32, Raspberry Pi, and Arduino UI applications.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.0 V DC (module with onboard regulator) |
| **IC logic voltage (`VDD`)** | 2.4 V to 3.3 V DC (3.3 V nominal) |
| **Native resolution** | $240 \times 320$ pixels (modules commonly crop to $240 \times 240$) |
| **Color depth** | 16-bit RGB565 (65,536 colors) or 18-bit RGB666 |
| **Interface** | 4-Wire SPI (SPI Mode 3 or Mode 0) |
| **Max SPI clock** | Up to 62.5 MHz (write) |
| **Backlight control** | Dedicated `BLK` / `LED` pin (PWM dimmable) |

## Pinout

Common 7-pin or 8-pin 0.1" (2.54 mm) breakout module header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` | Power | Ground (0 V) |
| 2 | `VCC` | Power | Power supply (+3.3 V to +5.0 V DC) |
| 3 | `SCL` / `SCK` | Digital Input | SPI Serial Clock |
| 4 | `SDA` / `MOSI` | Digital Input | SPI Master Out Slave In (Data Input) |
| 5 | `RES` / `RST` | Digital Input | Active-Low Hardware Reset |
| 6 | `DC` / `RS` | Digital Input | Data / Command Select (Low = Command, High = Data) |
| 7 | `CS` | Digital Input | Active-Low Chip Select (tied low on some 7-pin modules) |
| 8 | `BLK` / `LEDA` | Digital Input | Backlight enable / PWM brightness control |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{CC}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with 3.3V LDO |
| Logic Input High | $V_{IH}$ | 0.7 $V_{DD}$ | 3.3 | 3.6 | V | `SCL`, `SDA`, `DC`, `CS`, `RES` |
| Logic Input Low | $V_{IL}$ | -0.3 | 0 | 0.3 $V_{DD}$ | V | `SCL`, `SDA`, `DC`, `CS`, `RES` |
| Logic Driver Current | $I_{logic}$ | — | 8 | 15 | mA | Active frame rendering |
| Backlight Current | $I_{led}$ | — | 40 | 60 | mA | 100% LED brightness |
| Max SPI Write Clock | $f_{SCK}$ | — | 30 | 62.5 | MHz | $V_{DD} = 3.3\text{ V}$ |
| Operating Temperature | $T_{opr}$ | -30 | — | 85 | °C | Ambient |

## Register map

The ST7789 uses command bytes followed by data payloads over SPI (`DC` low for commands, `DC` high for data):

| Command | Name | Access | Reset | Description |
|---|---|---|---|---|
| `0x01` | `SWRESET` | Write | — | Software Reset |
| `0x11` | `SLPOUT` | Write | — | Sleep Out (exits low-power sleep) |
| `0x29` | `DISPON` | Write | — | Display On |
| `0x2A` | `CASET` | Write | — | Column Address Set ($X_{start}$ to $X_{end}$) |
| `0x2B` | `RASET` | Write | — | Row Address Set ($Y_{start}$ to $Y_{end}$) |
| `0x2C` | `RAMWR` | Write | — | Memory Write (stream RGB pixel data) |
| `0x36` | `MADCTL` | Write | `0x00` | Memory Data Access Control (rotation, BGR/RGB) |
| `0x3A` | `COLMOD` | Write | `0x66` | Interface Pixel Format (`0x55` = 16-bit RGB565) |

## Wiring

| ST7789 Pin | → | ESP32 | Arduino Uno (with level shifter) | Notes |
|---|---|---|---|---|
| `VCC` | | 3.3V / 5V | 5V | Onboard LDO converts to 3.3V |
| `GND` | | GND | GND | Common ground |
| `SCL` | | GPIO 18 (SCK) | D13 | Hardware SPI Clock |
| `SDA` | | GPIO 23 (MOSI) | D11 | Hardware SPI Data |
| `RES` | | GPIO 4 | D8 | Hardware Reset |
| `DC` | | GPIO 2 | D9 | Data / Command Control |
| `CS` | | GPIO 5 | D10 | Chip Select (if present) |
| `BLK` | | 3.3V | 5V | Pull High for 100% backlight |

> [!WARNING]
> Logic level compatibility:
> - The ST7789 IC operates strictly at **3.3 V logic**. While some breakout boards include a 3.3V voltage regulator for `VCC`, many cheaper modules **do not include logic level shifters** on `SCL`, `SDA`, `DC`, and `CS`.
> - Connecting 5 V logic directly from an Arduino Uno to an unbuffered ST7789 module will cause screen corruption or permanent IC damage. Use inline $1\text{ k}\Omega$ series resistors or a 74LVC245 buffer IC.

## Example

```cpp
#include <Adafruit_GFX.h>
#include <Adafruit_ST7789.h>
#include <SPI.h>

#define TFT_CS    5
#define TFT_RST   4
#define TFT_DC    2

Adafruit_ST7789 tft = Adafruit_ST7789(TFT_CS, TFT_DC, TFT_RST);

void setup() {
  Serial.begin(115200);
  
  // Initialize 240x240 ST7789 display
  tft.init(240, 240, SPI_MODE3);
  tft.setRotation(2);
  tft.fillScreen(ST77XX_BLACK);
  
  tft.setCursor(20, 100);
  tft.setTextColor(ST77XX_GREEN);
  tft.setTextSize(3);
  tft.println("VoltDocs");
}

void loop() {
  // Main execution loop
}
```

## Common mistakes

- **Missing $240 \times 240$ offset alignment:** On $240 \times 240$ displays, the physical screen is cropped from the ST7789's native $240 \times 320$ RAM array. Setting the wrong rotation offset causes a black band or glitchy pixels along the display edge. Use `SPI_MODE3` and correct library offsets (`offset_x = 0, offset_y = 0` or `32`).
- **Color inversion (RGB vs BGR):** ST7789 IPS displays default to inverted colors. If blacks appear white and blue appears yellow, call `tft.invertDisplay(true)` in setup.
- **Floating `BLK` pin:** Leaving the backlight pin disconnected leaves the screen dark on modules that pull `BLK` Low by default.

## Notes

- **ST7789 vs ST7735:** ST7789 offers much higher pixel density ($240 \times 240$ vs $128 \times 160$), faster SPI fill rates, and superior IPS viewing angles compared to older ST7735 TN displays.
