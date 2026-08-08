## Overview

The **Pimoroni Unicorn HAT** is an $8 \times 8$ RGB LED matrix add-on board designed for the Raspberry Pi. Fitting onto the standard 40-pin GPIO header, it packs **64 surface-mount WS2812B (NeoPixel) RGB LEDs** into a compact $65 \times 56\text{ mm}$ HAT footprint.

Driven via a single hardware PWM/DMA channel (**GPIO 18**), the Unicorn HAT provides 24-bit full RGB color control ($16.7$ million colors) per pixel. It is widely used in Raspberry Pi desktop status displays, Moodlite indicators, audio spectrum visualizers, CPU load monitors, and 8-bit retro pixel art installations.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 5.0 V DC (powered directly from Pi 40-pin header 5V rail) |
| **Form factor** | Standard Raspberry Pi HAT footprint ($65 \times 56\text{ mm}$) |
| **Matrix dimensions** | 8 columns $\times$ 8 rows (64 RGB LEDs total) |
| **LED type** | WS2812B individually addressable smart RGB LEDs |
| **Color depth** | 24-bit RGB (8 bits per channel / 256 brightness levels per color) |
| **Control pin** | GPIO 18 (Pin 12 on 40-pin header; utilizes hardware PWM0 / PCM) |
| **Max current draw** | ~2.0 A at 100% full white brightness (typically 200–400 mA in software) |

## Pinout (Raspberry Pi 40-Pin GPIO Header)

The Unicorn HAT connects to the Raspberry Pi 40-pin header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 2, 4 | `5V` | Power | Supply power from Pi 5V rail (+5.0 V DC) |
| 6, 9, 14, 20, 25, 30, 34, 39 | `GND` | Power | Ground reference (0 V) |
| 12 | `GPIO 18` | Digital Output | WS2812B 800 kHz serial data line (PWM0 channel) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{5V}$ | 4.8 | 5.0 | 5.25 | V | Power from Pi 5V rail |
| Quiescent Current | $I_{idle}$| — | 60 | — | mA | All 64 LEDs off |
| Max Current Draw (Full White)| $I_{max}$ | — | 2000 | 2500 | mA | 100% brightness (64 x 60 mA) |
| Recommended Current Limit | $I_{rec}$ | — | 400 | 600 | mA | Soft-limited to 50% brightness |
| Refresh Rate | $FPS$ | 30 | 60 | 100 | fps | Driven via DMA controller |
| Serial Data Frequency | $f_{DATA}$ | 750 | 800 | 850 | kHz | Single-wire NRZ timing |

## Matrix Coordinates & Software Layout

The 64 LEDs are arranged in a serpentine matrix starting at pixel 0 (top-left) to pixel 63 (bottom-right):

```
       (0,0) [ 0  1  2  3  4  5  6  7 ]
             [ 8  9 10 11 12 13 14 15 ]
             [16 17 18 19 20 21 22 23 ]
             [ .  .  .  .  .  .  .  . ]
       (7,7) [56 57 58 59 60 61 62 63 ]
```

## Python Software Installation & Audio Conflict

Pimoroni provides an official Python library (`unicornhat`):

```bash
sudo apt-get update
sudo apt-get install python3-pip
sudo pip3 install unicornhat
```

> [!WARNING]
> Raspberry Pi Analog Audio (3.5mm Jack) Conflict:
> - The WS2812B LEDs on the Unicorn HAT use **GPIO 18 (PWM0)**. On the Raspberry Pi, GPIO 18 is shared with the onboard 3.5mm analog headphone jack PWM audio circuit.
> - Enabling analog audio playback while running the Unicorn HAT will corrupt the LED data stream, causing uncontrollable flickering. **Disable onboard analog audio** by editing `/boot/config.txt` and setting `dtparam=audio=off`.

## Python Code Example

```python
import unicornhat as unicorn
import time
import colorsys

print("Pimoroni Unicorn HAT 8x8 Test Script")

# Set display brightness (0.0 to 1.0)
unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)

# Rainbow effect loop
i = 0.0
try:
    while True:
        i += 0.01
        for x in range(8):
            for y in range(8):
                # Calculate rainbow HSL color
                hue = (x + y) / 16.0 + i
                r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue % 1.0, 1.0, 1.0)]
                unicorn.set_pixel(x, y, r, g, b)
        
        unicorn.show()
        time.sleep(0.02)

except KeyboardInterrupt:
    print("\nTurning off LEDs...")
    unicorn.off()
```

## Common mistakes

- **Running at 100% brightness on weak Pi power supplies:** Powering all 64 LEDs at full white draws up to **2.0 A**, which will cause a 5V supply voltage drop and trigger Raspberry Pi under-voltage warnings. Keep software brightness $\le 0.5$ (`unicorn.brightness(0.5)`).
- **Forgetting `sudo` permissions for DMA access:** Accessing hardware PWM/DMA memory registers requires root privileges. Always run Python scripts with `sudo python3 script.py`.

## Notes

- **Unicorn HAT vs Unicorn HAT HD:** Standard Unicorn HAT uses $8 \times 8$ WS2812B LEDs; Unicorn HAT HD uses a $16 \times 16$ (256 LED) high-density matrix driven via SPI.
