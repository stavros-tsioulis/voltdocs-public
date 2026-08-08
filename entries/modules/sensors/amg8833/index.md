## Overview

The **AMG8833** is a 64-pixel ($8 \times 8$) MEMS thermopile infrared array sensor manufactured by Panasonic under the *Grid-EYE* brand. Unlike single-point contactless non-contact infrared thermometers (such as the MLX90614), the AMG8833 acts as a low-resolution thermal camera, outputting a matrix of 64 independent temperature readings over $I^2C$ at frame rates up to 10 Hz.

Measuring surface temperatures from **$0^\circ\text{C}$ to $80^\circ\text{C}$** with a $60^\circ$ viewing angle, the AMG8833 can detect human presence, movement direction, hot spots, and thermal gradients. It is widely used in DIY thermal cameras, smart home occupancy detection, HVAC control, and robotic heat tracking.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.0 V DC (module with onboard regulator) |
| **IC supply voltage (`VDD`)** | 3.0 V to 3.6 V DC (3.3 V nominal) |
| **Interface** | $I^2C$ (Fast Mode up to 400 kHz) |
| **Default $I^2C$ address** | `0x69` (`ADDR` pin High / un-connected on Adafruit module) |
| **Alternate $I^2C$ address** | `0x68` (`ADDR` pin Low to `GND`) |
| **Pixel array matrix** | 64 pixels ($8 \times 8$ grid) |
| **Temperature range** | $0^\circ\text{C}$ to $+80^\circ\text{C}$ ($\pm 2.5^\circ\text{C}$ accuracy) |
| **Field of view (FOV)** | $60^\circ$ horizontal $\times 60^\circ$ vertical |
| **Frame rate** | 1 Hz or 10 Hz |
| **Active current draw** | 4.5 mA active / 0.2 mA standby |

## Pinout

Standard 6-pin 0.1" (2.54 mm) header or Qwiic / STEMMA QT connector:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 4 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 5 | `INT` | Digital Output | Active-Low interrupt output (triggers on temp threshold) |
| 6 | `ADDR` | Digital Input | $I^2C$ Address select (Low = `0x68`, High = `0x69`) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{CC}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | DC |
| Active Supply Current | $I_{CC}$ | — | 4.5 | 7.0 | mA | 10 FPS continuous capture |
| Standby Current | $I_{sb}$ | — | 0.2 | 0.8 | mA | Standby mode |
| Target Temp Range | $T_{target}$ | 0 | — | 80 | °C | Measured surface temperature |
| Temperature Accuracy | $T_{acc}$ | -2.5 | $\pm 2.5$ | +2.5 | °C | Within $0^\circ\text{C}$–$80^\circ\text{C}$ range |
| Temperature Resolution | $T_{res}$ | — | 0.25 | — | °C | 12-bit output ($0.25^\circ\text{C}$ per LSB) |
| Frame Rate | $FPS$ | 1 | 10 | 10 | Hz | Selectable via `FPSC` register |
| Thermistor Range | $T_{therm}$ | -20 | — | 80 | °C | Onboard IC reference thermistor |

## Pixel Layout & Data Registers

The 64 thermal pixels are arranged in an $8 \times 8$ matrix. Pixel data registers start at address **`0x80`** through **`0xFF`** (2 bytes per pixel, 12-bit 2's complement format):

- Pixel 1: `0x80` (Low Byte), `0x81` (High Byte)
- Pixel 2: `0x82` (Low Byte), `0x83` (High Byte)
- ...
- Pixel 64: `0xFE` (Low Byte), `0xFF` (High Byte)

$$\text{Temperature } (^\circ\text{C}) = \text{Raw 12-bit Signed Integer} \times 0.25^\circ\text{C}$$

## Wiring

| AMG8833 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Onboard regulator converts to 3.3V |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |
| `INT` | | Digital D2 | GPIO 4 | Interrupt pin (optional) |

## Example

```cpp
#include <Wire.h>
#include <Adafruit_AMG88xx.h>

Adafruit_AMG88xx amg;

float pixels[AMG88xx_PIXEL_ARRAY_SIZE];

void setup() {
  Serial.begin(115200);
  Serial.println(F("AMG8833 thermal camera test"));

  bool status = amg.begin(0x69); // Default address 0x69
  if (!status) {
    Serial.println("Could not find a valid AMG8833 sensor, check wiring!");
    while (1);
  }
  Serial.println("AMG8833 initialized.");
}

void loop() {
  // Read all 64 thermal pixels into array
  amg.readPixels(pixels);

  Serial.println("--- 8x8 Thermal Frame (°C) ---");
  for (int i = 1; i <= AMG88xx_PIXEL_ARRAY_SIZE; i++) {
    Serial.print(pixels[i - 1], 1);
    Serial.print("\t");
    if (i % 8 == 0) Serial.println();
  }
  Serial.println();

  delay(1000);
}
```

## Common mistakes

- **Expecting high-resolution optical images:** The AMG8833 is an $8 \times 8$ grid (64 pixels total). Producing smooth thermal images requires applying bicubic software interpolation (e.g. upscaling to $24 \times 24$ or $32 \times 32$ in code).
- **Measuring temperatures $>80^\circ\text{C}$:** Temperatures exceeding $80^\circ\text{C}$ cause sensor output registers to saturate.
- **Ignoring thermal stabilization warm-up:** Allow the sensor 30 seconds after powering on for internal silicon temperatures to stabilize.

## Notes

- **AMG8833 vs MLX90640:** AMG8833 is $8 \times 8$ (64 pixels, $0.25^\circ\text{C}$ resolution); MLX90640 is $32 \times 24$ (768 pixels). AMG8833 is simpler and cheaper for basic presence detection.
