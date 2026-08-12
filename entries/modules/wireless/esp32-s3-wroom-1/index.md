## Overview

The **ESP32-S3-WROOM-1** is a high-performance Wi-Fi and Bluetooth 5 (LE) MCU module manufactured by Espressif Systems. Built around the **ESP32-S3** dual-core 32-bit **Xtensa LX7** processor running at up to **$240\text{ MHz}$**, it includes dedicated vector instructions designed to accelerate neural network computing and signal processing workloads (TinyML, speech recognition, face detection).

Equipped with **$512\text{ KB}$ of internal SRAM**, **$4\text{ MB}$ to $16\text{ MB}$ of Quad/Octal SPI Flash**, and up to **$8\text{ MB}$ of Octal SPI PSRAM**, it features a native **USB 2.0 OTG Full-Speed interface**, a DVP parallel camera interface, and an RGB/I8080 LCD interface. It is the dominant platform for smart displays, AI camera modules (ESP32-S3-CAM), and voice assistants.

## Quick reference

| | |
|---|---|
| **CPU Core** | Dual-Core 32-bit Xtensa LX7 with Vector Extensions |
| **Max Clock Frequency** | $240\text{ MHz}$ |
| **Internal SRAM** | $520\text{ KB}$ ($512\text{ KB}$ usable) |
| **On-Module Flash** | $4\text{ MB}$, $8\text{ MB}$, or $16\text{ MB}$ SPI Flash |
| **On-Module PSRAM** | Up to $8\text{ MB}$ Octal SPI PSRAM (N8R8 / N16R8 variants) |
| **Operating Voltage (`VDD`)** | 3.0 V to 3.6 V DC (3.3 V nominal) |
| **Wireless Support** | Wi-Fi 802.11 b/g/n (2.4 GHz), Bluetooth 5.0 LE & Mesh |
| **Camera & Display** | 8-bit to 16-bit DVP Camera Interface, RGB565 / I8080 LCD Driver |
| **On-Chip USB** | Native USB 2.0 OTG Full-Speed Controller |
| **GPIO Count** | 36 I/O pins |
| **Package** | 41-pin SMD Castellated Module ($18 \times 25.5\text{ mm}$) / DevKitC-1 |

## Pinout (ESP32-S3-DevKitC-1 Header Layout)

```
                       ┌─────────────┐
                 [GND] │ 1        44 │ [GND]
                [3.3V] │ 2        43 │ [3.3V]
               [RESET] │ 3  ESP32 42 │ [GPIO44] (U0RXD)
       (ADC1_0) [GPIO1]│ 4  -S3   41 │ [GPIO43] (U0TXD)
       (ADC1_1) [GPIO2]│ 5        40 │ [GPIO42] (MTMS)
       (ADC1_2) [GPIO3]│ 6        39 │ [GPIO41] (MTDI)
       (ADC1_3) [GPIO4]│ 7        38 │ [GPIO40] (MTDO)
       (ADC1_4) [GPIO5]│ 8        37 │ [GPIO39] (MTCK)
       (ADC1_5) [GPIO6]│ 9        36 │ [GPIO38]
       (ADC1_6) [GPIO7]│ 10       35 │ [GPIO37]
       (ADC1_7) [GPIO8]│ 11       34 │ [GPIO36]
       (ADC1_8) [GPIO9]│ 12       33 │ [GPIO35]
      (ADC1_9) [GPIO10]│ 13       32 │ [GPIO0] (BOOT Button)
               [GPIO11]│ 14       31 │ [GPIO45]
               [GPIO12]│ 15       30 │ [GPIO48] (RGB LED)
               [GPIO13]│ 16       29 │ [GPIO47]
               [GPIO14]│ 17       28 │ [GPIO21] (USB D+)
               [GPIO15]│ 18       27 │ [GPIO20] (USB D-)
                       └─────────────┘
```

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 3.0 | 3.3 | 3.6 | V | DC |
| Peak TX Current | $I_{TX\_MAX}$ | — | 240 | 355 | mA | 802.11b, $+20.5\text{ dBm}$ |
| RX Current | $I_{RX}$ | — | 85 | 95 | mA | Wi-Fi active |
| Deep Sleep Current | $I_{DS}$ | — | 7 | 20 | µA | RTC memory retained |
| Light Sleep Current | $I_{LS}$ | — | 240 | — | µA | CPU paused |
| GPIO Output Drive | $I_{IO}$ | -40 | — | +40 | mA | Absolute max single pin |

## Example (Arduino ESP32 Core - Dual Core & Vector Math)

```cpp
#include "esp_dsp.h"

// Onboard RGB LED on ESP32-S3-DevKitC-1 is connected to GPIO48
const int rgbLedPin = 48;

void setup() {
  Serial.begin(115200);
  pinMode(rgbLedPin, OUTPUT);

  Serial.println("ESP32-S3 Dual-Core LX7 Vector Engine Initialized!");
  Serial.printf("Free Heap: %d bytes\n", ESP.getFreeHeap());
  Serial.printf("PSRAM Size: %d bytes\n", ESP.getPsramSize());
}

void loop() {
  neopixelWrite(rgbLedPin, 0, 64, 128); // Cyan
  delay(500);
  neopixelWrite(rgbLedPin, 0, 0, 0);     // OFF
  delay(500);
}
```

## Common mistakes

- **Using Octal PSRAM GPIOs (GPIO33 to GPIO37) on N8R8/N16R8 variants:** ESP32-S3 modules equipped with Octal SPI Flash or Octal PSRAM (e.g. `ESP32-S3-WROOM-1-N8R8`) internally use GPIO33, GPIO34, GPIO35, GPIO36, and GPIO37 for high-speed PSRAM bus communication. Attempting to use these GPIOs externally breaks PSRAM access.
- **Boot failures due to insufficient power supply decoupling:** The ESP32-S3 draws high transient current spikes ($>350\text{ mA}$) during Wi-Fi transmission. Ensure the 3.3V power supply is decoupled with a low-ESR $10\ \mu\text{F}$ and $100\text{ nF}$ capacitor.

## Notes

- **ESP32-S3 vs ESP32-WROOM-32:** ESP32-S3 upgrades the CPU from Xtensa LX6 (240MHz) to LX7 (240MHz with vector instructions), upgrades Bluetooth from v4.2 to v5.0 LE, adds native USB 2.0 OTG, supports High-Speed Octal PSRAM/Flash, and adds DVP camera support.
