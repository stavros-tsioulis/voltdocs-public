## Overview

The **ESP32-C3** is a low-power, high-integration 32-bit System-on-Chip (SoC) manufactured by Espressif Systems. Powered by an open-standard **32-bit single-core RISC-V (RV32IMC)** microcontroller operating at up to **$160\text{ MHz}$**, it is designed as a pin-compatible, low-cost successor to the classic ESP8266.

Equipped with **$400\text{ KB}$ of SRAM**, **$384\text{ KB}$ of ROM**, integrated **2.4 GHz Wi-Fi (802.11 b/g/n)**, **Bluetooth 5.0 (LE)**, and a native **USB Serial/JTAG controller**, it delivers secure connectivity (AES-128/256, RSA, ECC, and digital signatures) for budget smart home devices (ESPHome/Home Assistant, Matter).

## Quick reference

| | |
|---|---|
| **CPU Core** | 32-bit Single-Core RISC-V RV32IMC processor |
| **Max Clock Frequency** | $160\text{ MHz}$ |
| **SRAM** | $400\text{ KB}$ |
| **ROM** | $384\text{ KB}$ |
| **Flash Memory** | Embedded $4\text{ MB}$ (FN4/FH4) or external SPI Flash up to $16\text{ MB}$ |
| **Operating Voltage (`VDD`)** | 3.0 V to 3.6 V DC (3.3 V nominal) |
| **Wireless Support** | Wi-Fi 802.11 b/g/n (up to 150 Mbps), Bluetooth 5.0 LE |
| **On-Chip USB** | Integrated USB Serial/JTAG Controller |
| **GPIO Count** | 22 I/O pins |
| **ADC Channels** | 6 channels (12-bit ADC) |
| **Package** | 32-pin QFN ($5 \times 5\text{ mm}$) / ESP32-C3 SuperMini PCB |

## Pinout (ESP32-C3 SuperMini Development Board Layout)

```
                       ┌─────────────┐
        (GPIO0 / ADC1_0) 1│ 1   16│ 5V (Power Input)
        (GPIO1 / ADC1_1) 2│       │15 GND
        (GPIO2 / ADC1_2) 3│ ESP32 │14 3V3 (3.3V Output)
        (GPIO3 / ADC1_3) 4│ -C3   │13 GPIO10
        (GPIO4 / ADC1_4) 5│ Super │12 GPIO9 (BOOT Button)
        (GPIO5 / ADC2_0) 6│ Mini  │11 GPIO8 (Onboard LED)
        (GPIO6 / SDA)    7│       │10 GPIO21 (TX)
        (GPIO7 / SCL)    8│       │9  GPIO20 (RX)
                       └─────────────┘
```

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 3.0 | 3.3 | 3.6 | V | DC supply |
| Wi-Fi Peak TX Current | $I_{TX}$ | — | 290 | 350 | mA | 802.11b, $+21\text{ dBm}$ |
| Wi-Fi RX Current | $I_{RX}$ | — | 82 | 90 | mA | 802.11g/n active |
| Deep Sleep Current | $I_{DS}$ | — | 5 | 15 | µA | RTC timer active |
| Light Sleep Current | $I_{LS}$ | — | 130 | — | µA | CPU paused |
| Max Output Drive | $I_{IO}$ | -28 | — | +28 | mA | Single GPIO pin |

## Example (Arduino ESP32 Core - Wi-Fi Scanner & Blinking LED)

```cpp
#include <WiFi.h>

// Onboard LED on ESP32-C3 SuperMini is connected to GPIO8 (Active LOW)
const int ledPin = 8;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
  
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(100);

  Serial.println("ESP32-C3 RISC-V Wi-Fi Scanner Ready!");
}

void loop() {
  digitalWrite(ledPin, LOW); // LED ON
  
  int n = WiFi.scanNetworks();
  Serial.printf("Found %d networks\n", n);
  for (int i = 0; i < n; ++i) {
    Serial.printf("%d: %s (%d dBm)\n", i + 1, WiFi.SSID(i).c_str(), WiFi.RSSI(i));
  }
  
  digitalWrite(ledPin, HIGH); // LED OFF
  delay(5000);
}
```

## Common mistakes

- **Holding GPIO9 LOW during boot:** GPIO9 is a strapping pin on the ESP32-C3. If held LOW during power-up or reset, the chip enters SPI flash download mode instead of booting normal user firmware.
- **Driving 5V signals directly into GPIOs:** Unlike older AVR microcontrollers, ESP32-C3 GPIO pins are **NOT 5V tolerant**. Exceeding 3.6V on any I/O pin damages the chip.

## Notes

- **ESP32-C3 vs ESP8266 vs ESP32-S3:** ESP32-C3 is a single-core 160MHz RISC-V MCU with Wi-Fi + BLE 5; ESP8266 is an older 80MHz Tensilica MCU with Wi-Fi only; ESP32-S3 is a dual-core 240MHz Xtensa LX7 MCU with vector instructions for AI.
