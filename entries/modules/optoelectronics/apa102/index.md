## Overview

The **APA102** (sold by Adafruit under the brand name **DotStar**) is an individually addressable RGB LED light source with an integrated CMOS control IC in a 5050 SMD package. 

Unlike the ubiquitous WS2812B (NeoPixel), which relies on a strict single-wire $800\text{ kHz}$ timing protocol that requires microsecond-accurate bit-banging and disables interrupts on 8-bit MCUs, the APA102 uses a standard 2-wire **SPI protocol (Clock and Data)**. This allows transmission rates up to **20 MHz**, enables high-speed PWM dimming (19.2 kHz PWM rate vs WS2812B's 400 Hz), and eliminates timing sensitivity when driven from non-realtime operating systems like Raspberry Pi Linux.

## Quick reference

| | |
|---|---|
| **Supply voltage (`VCC`)** | 4.5 V to 5.5 V DC (5.0 V nominal) |
| **Protocol** | 2-Wire SPI (Serial Clock `CKI`, Serial Data `SDI`) |
| **Max SPI clock rate** | Up to 20 MHz |
| **Internal PWM frequency** | 19.2 kHz (flicker-free high-speed persistence of vision) |
| **Color depth** | 24-bit RGB (8 bits per channel) + 5-bit global brightness (32 levels) |
| **Max current draw** | ~60 mA per LED at 100% full white ($V_{CC} = 5.0\text{V}$) |

## Pinout & Connector

APA102 LEDs are integrated on strips or matrices exposing a 4-wire interface:

| Lead | Cable Color | Name | Type | Description |
|---|---|---|---|---|
| 1 | Red | `VCC` | Power | Supply voltage (+5.0 V DC) |
| 2 | Green / Yellow | `CKI` / `CI` | Digital Input | Serial Clock Input |
| 3 | Blue / White | `SDI` / `DI` | Digital Input | Serial Data Input |
| 4 | Black | `GND` | Power | Ground (0 V) |

*(Signal outputs on the far end of an LED strip are labeled `CKO` and `SDO` for cascading to the next strip segment).*

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 4.5 | 5.0 | 5.5 | V | DC |
| Logic Input Voltage | $V_{IN}$ | -0.5 | 5.0 | $V_{CC}+0.5$| V | `CKI`, `SDI` pins |
| Max Clock Frequency | $f_{CLK}$ | — | 15.0 | 20.0 | MHz | SPI bus clock |
| Internal PWM Rate | $f_{PWM}$ | — | 19.2 | — | kHz | LED current modulation rate |
| Red LED Peak Wavelength | $\lambda_R$ | 620 | 625 | 630 | nm | Brightness ~400 mcd |
| Green LED Peak Wavelength | $\lambda_G$ | 520 | 522.5 | 525 | nm | Brightness ~1200 mcd |
| Blue LED Peak Wavelength | $\lambda_B$ | 465 | 467.5 | 470 | nm | Brightness ~300 mcd |

## Data Framing & SPI Protocol

A complete data frame for an APA102 LED strip consists of 3 distinct sections:

1. **Start Frame:** 32 zero bits (`0x00 0x00 0x00 0x00`).
2. **LED Data Frames (4 bytes per LED):**
   - **Byte 0:** `111` + 5-bit Global Brightness (`0xE0` | `0x00`–`0x1F`).
   - **Byte 1:** Blue brightness (`0x00`–`0xFF`).
   - **Byte 2:** Green brightness (`0x00`–`0xFF`).
   - **Byte 3:** Red brightness (`0x00`–`0xFF`).
3. **End Frame:** $\lceil \frac{N}{2} \rceil$ bits of High (`0xFF`) pulses (or $N$ clock pulses) to push remaining bits through internal shift registers to the last LED on long strips ($N = \text{number of LEDs}$).

```
[Start Frame 4B] -> [LED 1: 4B] -> [LED 2: 4B] ... -> [LED N: 4B] -> [End Frame]
```

## Wiring

| APA102 Lead | → | Arduino / MCU | Raspberry Pi | Notes |
|---|---|---|---|---|
| `VCC` | | 5V Power Supply | 5V Power Supply | **Do not power long strips from MCU 5V pin** |
| `GND` | | GND | GND | Common ground mandatory |
| `CKI` (Clock) | | Digital D13 (SCK) | GPIO 11 (SPI0_SCLK)| Hardware or Software SPI Clock |
| `SDI` (Data)  | | Digital D11 (MOSI)| GPIO 10 (SPI0_MOSI)| Hardware or Software SPI Data |

> [!WARNING]
> High current supply hazard:
> - A strip of 60 APA102 LEDs draws up to **3.6 A** at full white brightness ($60\text{ mA} \times 60 = 3600\text{ mA}$).
> - Always use an external 5V DC high-current power supply and inject power at both ends of strips longer than 2 meters to prevent copper voltage drop (which causes color shifting towards red at the tail end).

## Example

```cpp
#include <Adafruit_DotStar.h>
#include <SPI.h>

#define NUMPIXELS 30 // Number of LEDs in strip

// Hardware SPI setup (using SPI MOSI and SCK pins)
Adafruit_DotStar strip(NUMPIXELS, DOTSTAR_BRG);

void setup() {
  strip.begin(); // Initialize pins for output
  strip.setBrightness(80); // Set global brightness (0 to 255)
  strip.show(); // Turn all LEDs off
}

void loop() {
  // Chase a blue light down the strip
  for(int i=0; i<NUMPIXELS; i++) {
    strip.setPixelColor(i, 0x0000FF); // Blue color (0xRRGGBB)
    strip.show();
    delay(30);
    strip.setPixelColor(i, 0); // Turn off
  }
}
```

## Common mistakes

- **Leaving ground un-connected to MCU:** Connecting external 5V power without connecting external `GND` to MCU `GND` causes severe data corruption and flickering.
- **Conflating RGB and BGR byte order:** APA102 LEDs from different manufacturers use different internal byte sequences (`DOTSTAR_BGR`, `DOTSTAR_RGB`, or `DOTSTAR_BRG`). If colors are swapped, adjust the color-order parameter in software.

## Notes

- **APA102 vs WS2812B:** APA102 uses $19.2\text{ kHz}$ internal PWM (flicker-free for high-speed photography/video recording and persistence-of-vision wands) compared to WS2812B's $400\text{ Hz}$ PWM.
