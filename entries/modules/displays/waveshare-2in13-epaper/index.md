## Overview

The **Waveshare 2.13-inch E-Paper Display HAT** is an ultra-low-power electronic ink (E-Ink) display module featuring a resolution of **$250 \times 122$ pixels**. Built around an onboard controller (SSD1680 in V4 revisions), it connects to microcontrollers and single-board computers via a 3-wire or 4-wire SPI bus.

Electronic paper displays reflect ambient light just like physical paper, eliminating backlight glare while retaining full readability under direct sunlight. Crucially, electrophoretic E-Ink displays consume **zero power to maintain static images**—power is drawn only during screen updates. Supporting fast **partial refresh (0.3 seconds)** without screen flickering, it is widely deployed in Raspberry Pi desktop dashboards, crypto tickers, weather stations, and battery-powered Home Assistant sensors.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.0 V DC (onboard level translator) |
| **Display area** | 2.13-inch diagonal ($48.55\text{ mm} \times 23.71\text{ mm}$) |
| **Resolution** | $250 \times 122$ pixels (130 DPI) |
| **Display color** | Black and White (monochrome) |
| **Interface** | 3-Wire / 4-Wire SPI |
| **Full refresh duration** | ~2.0 seconds |
| **Partial refresh duration** | ~0.3 seconds |
| **Standby power draw** | $<0.017\text{ mW}$ (near-zero current when idle) |
| **Form factor** | Raspberry Pi 40-pin GPIO HAT footprint + 8-pin JST connector |

## Pinout (8-Pin JST Connector & Raspberry Pi 40-Pin Header)

| Pin | Cable Color | Name | Type | Pi GPIO Header Pin | Description |
|---|---|---|---|---|---|
| 1 | Red | `VCC` | Power | Pin 2 (5V) / Pin 1 (3.3V) | Power supply (+3.3 V to +5.0 V DC) |
| 2 | Black | `GND` | Power | Pin 6 (GND) | Ground reference (0 V) |
| 3 | Blue | `DIN` / `MOSI`| Digital Input | Pin 19 (GPIO 10 - SPI0_MOSI)| SPI Master Output Data |
| 4 | Yellow | `CLK` / `SCK` | Digital Input | Pin 23 (GPIO 11 - SPI0_SCLK)| SPI Serial Clock |
| 5 | Orange | `CS` | Digital Input | Pin 24 (GPIO 8 - SPI0_CE0) | Active-Low SPI Chip Select |
| 6 | Green | `DC` | Digital Input | Pin 22 (GPIO 25) | Data / Command Select (Low = Cmd, High = Data) |
| 7 | White | `RST` | Digital Input | Pin 11 (GPIO 17) | Active-Low Reset pin |
| 8 | Purple | `BUSY` | Digital Output | Pin 18 (GPIO 24) | Active-High Busy signal (High = Screen Updating) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | DC |
| Active Refresh Power | $P_{refresh}$| — | 26.4 | 40.0 | mW | During screen update |
| Standby Sleep Power | $P_{sleep}$ | — | 0.017 | 0.03 | mW | Deep sleep mode |
| Full Refresh Time | $t_{full}$ | — | 2.0 | 3.0 | s | Room temperature ($25^\circ\text{C}$) |
| Partial Refresh Time | $t_{part}$ | — | 0.3 | 0.5 | s | Room temperature ($25^\circ\text{C}$) |
| Viewing Angle | $\theta$ | $>170^\circ$ | — | — | deg | Full reflection angle |
| Operating Temperature | $T_{opr}$ | 0 | 25 | 50 | °C | B/W monochrome version |

## Refresh Modes & Screen Care

1. **Full Refresh:** Inverts the entire display (black-to-white flash) to clear ghosting. Must be performed at least once every 24 hours to prevent permanent E-Ink burn-in.
2. **Partial Refresh:** Updates only changing pixel regions (e.g. clock digits) in ~0.3 seconds without full-screen flashing.
3. **Deep Sleep Command (`0x10`):** After updating the display, issue the deep sleep command to power down internal charge pumps and prevent DC voltage damage to the electrophoretic panel.

## Wiring (Arduino / ESP32 SPI Connection)

| E-Paper Pin | → | ESP32 GPIO | Arduino Uno | Notes |
|---|---|---|---|---|
| `VCC` | | 3.3V | 5V / 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `DIN` (MOSI) | | GPIO 23 | Digital D11 | SPI Data |
| `CLK` (SCK)  | | GPIO 18 | Digital D13 | SPI Clock |
| `CS`  | | GPIO 5 | Digital D10 | SPI Chip Select |
| `DC`  | | GPIO 17 | Digital D9 | Data/Command pin |
| `RST` | | GPIO 16 | Digital D8 | Hardware Reset |
| `BUSY`| | GPIO 4 | Digital D7 | Busy Status Output |

## Example (Python Raspberry Pi `waveshare_epd`)

```python
import sys
import os
import time
from waveshare_epd import epd2in13_V4
from PIL import Image, ImageDraw, ImageFont

epd = epd2in13_V4.EPD()

print("Initializing 2.13inch e-Paper...")
epd.init()
epd.Clear()

# Create blank image canvas for drawing (250x122)
image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear/white background
draw = ImageDraw.Draw(image)

font = ImageFont.load_default()
draw.text((10, 20), 'VoltDocs E-Ink Dashboard', font=font, fill=0)
draw.text((10, 50), 'Temp: 22.4 C | RH: 45%', font=font, fill=0)
draw.line([(10, 40), (200, 40)], fill=0, width=2)

# Display rendered image on screen
epd.display(epd.getbuffer(image))
time.sleep(2)

print("Entering Deep Sleep mode to save power...")
epd.sleep()
```

## Common mistakes

- **Leaving the display powered continuously without issuing `sleep()`:** Keeping voltage applied to the E-Ink panel without putting the controller to sleep causes permanent ghosting and panel degradation over time.
- **Ignoring the `BUSY` line:** Sending SPI commands while the `BUSY` pin is High corrupts display memory. Always wait for `BUSY` to go Low before issuing new refresh commands.

## Notes

- **2.13" E-Paper Variants:** Waveshare manufactures several 2.13" revisions: V2 (SSD1675), V3, V4 (SSD1680), and Tricolor (B/W/Red or B/W/Yellow). Ensure software drivers match your specific version.
