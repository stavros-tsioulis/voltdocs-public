## Overview

The **HX8357** (specifically variants HX8357-C and HX8357-D) is a single-chip 320x480 resolution 65K/262K-color TFT LCD controller/driver manufactured by Himax Technologies. Commonly mounted on **3.5-inch color TFT breakout boards**, Adafruit FeatherWings, and Raspberry Pi display HATs, it drives full $320 \times 480$ HVGA graphics displays.

Integrating an internal **460.8 KB Graphic RAM (GRAM)** frame buffer, digital gamma control, and timing generators, the HX8357 supports both high-speed **4-wire SPI (up to 30 MHz)** and **8-bit / 16-bit 8080-parallel bus interfaces**. It is natively supported by Adafruit_GFX, TFT_eSPI, and ESPHome.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VIN`)** | 3.3 V to 5.0 V DC (breakout module with 3.3V LDO regulator) |
| **IC supply voltage (`VDD`)** | 2.4 V to 3.3 V DC (3.3 V nominal) |
| **Interface** | 4-Wire SPI (up to 30 MHz) or 8-Bit / 16-Bit Parallel 8080 |
| **Resolution** | $320 \times 480$ pixels (HVGA 3.5" display format) |
| **Color depth** | 16-bit RGB565 ($65,536$ colors) / 18-bit ($262,144$ colors) |
| **Onboard GRAM** | 460.8 KB internal frame buffer |
| **Backlight control** | PWM-dimmable LED backlight pin (`LITE` / `LED`) |

## Pinout (SPI Mode Breakout Header)

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VIN` | Power | Supply power input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `CS` | Digital Input | Active-Low SPI Chip Select |
| 4 | `C/D` / `DC` | Digital Input | Command / Data select pin (Low = Command, High = Data) |
| 5 | `RST` | Digital Input | Active-Low hardware reset pin |
| 6 | `MOSI` / `SDI`| Digital Input | SPI Master Output Slave Input |
| 7 | `SCK` / `CLK` | Digital Input | SPI Serial Clock |
| 8 | `MISO` / `SDO`| Digital Output | SPI Master Input Slave Output (Data Read) |
| 9 | `LITE` / `LED` | Digital Input | Backlight anode power control (PWM dimmable) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{VIN}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with LDO |
| Logic I/O Voltage | $V_{IO}$ | 1.65 | 3.3 | 3.3 | V | 3.3V logic (5V requires level shifters) |
| Logic Current (Logic Only)| $I_{logic}$| — | 10 | 15 | mA | Active display drawing |
| Backlight LED Current | $I_{led}$ | — | 100 | 150 | mA | 100% LED backlight brightness |
| Max SPI Clock Frequency | $f_{SPI}$ | 0 | 24 | 30 | MHz | SPI write operations |
| Display Frame Rate | $FPS$ | 30 | 60 | 90 | Hz | Programmable internal refresh |

## Display Orientation & Color Formats

- **RGB565 16-Bit Color Format:** 5 bits Red, 6 bits Green, 5 bits Blue.
- **Display Rotation Modes:**
  - `0`: Portrait ($320 \times 480$, connector at bottom).
  - `1`: Landscape ($480 \times 320$, connector at right).
  - `2`: Reverse Portrait ($320 \times 480$, connector at top).
  - `3`: Reverse Landscape ($480 \times 320$, connector at left).

## Wiring (SPI Interface Mode)

| HX8357 Pin | → | Arduino Uno (via Level Shifter) | ESP32 | Notes |
|---|---|---|---|---|
| `VIN` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `CS`  | | Digital D10 | GPIO 15 | SPI Chip Select |
| `DC`  | | Digital D9 | GPIO 2 | Command/Data Select |
| `RST` | | Digital D8 | GPIO 4 | Hardware Reset |
| `MOSI`| | Digital D11 | GPIO 23 | SPI MOSI |
| `SCK` | | Digital D13 | GPIO 18 | SPI Clock |
| `LITE`| | 3.3V / 5V | GPIO 5 | PWM Backlight Dimming |

## Example (Adafruit_HX8357 Library)

```cpp
#include <SPI.h>
#include <Adafruit_GFX.h>
#include <Adafruit_HX8357.h>

#define TFT_CS   15
#define TFT_DC   2
#define TFT_RST  4

Adafruit_HX8357 tft = Adafruit_HX8357(TFT_CS, TFT_DC, TFT_RST);

void setup() {
  Serial.begin(115200);
  Serial.println("HX8357 320x480 TFT Display Test");

  tft.begin(HX8357D); // Initialize HX8357D variant
  tft.setRotation(1); // Landscape 480x320

  tft.fillScreen(HX8357_BLACK);
  tft.setTextColor(HX8357_WHITE);
  tft.setTextSize(3);
  tft.setCursor(20, 20);
  tft.println("VoltDocs TFT");

  tft.drawRect(20, 80, 440, 200, HX8357_BLUE);
  tft.fillCircle(240, 180, 50, HX8357_RED);
}

void loop() {
  // Main display loop
}
```

## Common mistakes

- **Selecting wrong driver sub-variant (HX8357-B vs HX8357-D):** HX8357-C and HX8357-D have different initialization command sequence registers than earlier HX8357-B chips. Ensure `tft.begin(HX8357D)` is selected in software.
- **Connecting 5V logic directly without level shifters:** While module `VIN` accepts 5V, the HX8357 logic signals (`CS`, `DC`, `MOSI`, `SCK`) are 3.3V logic max.

## Notes

- **HX8357 vs ILI9341 vs ILI9488:** HX8357 and ILI9488 drive 3.5" $320 \times 480$ displays; ILI9341 drives 2.2" to 2.8" $240 \times 320$ displays.
