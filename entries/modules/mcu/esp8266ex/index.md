## Overview

The **ESP8266EX** is the groundbreaking 32-bit Wi-Fi System-on-Chip (SoC) manufactured by Espressif Systems. Responsible for triggering the low-cost Wi-Fi IoT revolution, it integrates a **32-bit Tensilica L106 microcontroller** core running at **$80\text{ MHz} \dots 160\text{ MHz}$**, a complete $802.11\text{b/g/n}$ Wi-Fi radio, power amplifier, low-noise receiver amplifier, transmit/receive switch, and TCP/IP protocol stack.

Found bare on QFN-32 packages and packaged inside **ESP-01**, **ESP-12F**, **NodeMCU**, and **Wemos D1 Mini** module boards, the ESP8266EX connects microcontrollers to the internet or acts as a standalone host MCU programmed via Arduino IDE, MicroPython, or ESPHome.

## Quick reference

| | |
|---|---|
| **CPU Architecture** | 32-bit Tensilica L106 32-bit RISC core ($80\text{ MHz} \dots 160\text{ MHz}$) |
| **Wi-Fi Standards** | $802.11\text{ b/g/n}$ ($2.4\text{ GHz} \dots 2.5\text{ GHz}$) |
| **Transmitter Output Power** | $+20\text{ dBm}$ (802.11b mode) / $+17\text{ dBm}$ (802.11g) |
| **Operating Voltage (`VDD`)** | 2.5 V to 3.6 V DC (3.3 V nominal) |
| **Memory Architecture** | $160\text{ KB}$ internal SRAM ($80\text{ KB}$ User RAM), External SPI Flash ($1\text{MB} \dots 16\text{MB}$) |
| **Sleep Power Consumption** | $< 10\ \mu\text{A}$ (Deep Sleep mode) |
| **ADC Channel** | 10-bit ADC channel ($0\text{V} \dots 1.0\text{V}$ raw IC input) |
| **Package** | 32-pin QFN ($5 \times 5\text{ mm}$) / ESP-12F Module |

## Pinout (ESP-12F Module Form Factor)

```
                       ┌─────────────┐
                [REST] │             │ [ADC  ] (A0 - 10-bit ADC)
                 [CH_PD]│   ESP-12F   │ [EN   ] (Chip Enable)
                 [GPIO16]│  ESP8266EX  │ [GPIO14] (HSPI_CLK)
                 [GPIO14]│             │ [GPIO12] (HSPI_MISO)
                 [GPIO12]│             │ [GPIO13] (HSPI_MOSI)
                 [GPIO13]│             │ [VCC  ] (3.3V)
                 [VCC   ]│             │ [CS0  ]
                 [CS0   ]│             │ [MISO ]
                 [MISO  ]│             │ [GPIO9 ]
                 [GPIO9 ]│             │ [GPIO10]
                 [GPIO10]│             │ [MOSI ]
                 [MOSI  ]│             │ [SCLK ]
                 [SCLK  ]│             │ [GND  ]
                 [GND   ]│             │ [GPIO15] (Boot Pin - Pull LOW)
                 [GPIO2 ]│             │ [GPIO0 ] (Boot Pin - Flashing)
                 [GPIO4 ]│             │ [GPIO5 ]
                 [RXD0  ]│             │ [TXD0  ]
                       └─────────────┘
```

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 2.5 | 3.3 | 3.6 | V | DC supply |
| TX Current (802.11b +20dBm)| $I_{TX}$ | — | 170 | 220 | mA | Continuous RF transmit |
| RX Current | $I_{RX}$ | — | 50 | 56 | mA | Continuous RF receive |
| Deep Sleep Current | $I_{sleep}$| — | 10 | 20 | µA | RTC timer active |
| Standby Current | $I_{stby}$| — | 0.9 | 1.2 | mA | Light sleep mode |

## Boot Mode Pin Selection Table

For the ESP8266EX to boot correctly from SPI Flash, specific GPIO boot pins must be pulled High or Low at power-on:

| Boot Mode | `GPIO15` | `GPIO0` | `GPIO2` |
|---|---|---|---|
| **UART Flashing (Download Code)** | LOW (GND) | **LOW (GND)** | HIGH (3.3V) |
| **Normal Flash Boot (Execute Code)**| LOW (GND) | **HIGH (3.3V)**| HIGH (3.3V) |
| **SDIO Boot** | HIGH (3.3V) | Any | Any |

> [!IMPORTANT]
> ESP8266 Chip Enable (`EN` / `CH_PD`):
> Pin `EN` (`CH_PD`) MUST be pulled **High to 3.3V** via a $10\ \text{k}\Omega$ resistor for the chip to power on. Leaving `EN` floating keeps the chip in shutdown mode.

## Example (Arduino ESP8266 Wi-Fi Station Scanner)

```cpp
#include <ESP8266WiFi.h>

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(100);

  Serial.println("ESP8266EX Wi-Fi Network Scanner");
}

void loop() {
  Serial.println("Scanning Wi-Fi networks...");
  int n = WiFi.scanNetworks();

  if (n == 0) {
    Serial.println("No networks found.");
  } else {
    Serial.print(n); Serial.println(" networks found:");
    for (int i = 0; i < n; ++i) {
      Serial.print(i + 1); Serial.print(": ");
      Serial.print(WiFi.SSID(i)); Serial.print(" (");
      Serial.print(WiFi.RSSI(i)); Serial.println(" dBm)");
    }
  }

  delay(5000);
}
```

## Common mistakes

- **Powering from Arduino 3.3V pin:** The ESP8266EX requires up to **$220\text{ mA} \dots 300\text{ mA}$ continuous current during Wi-Fi transmission spikes**. The onboard 3.3V regulator on older Arduino Uno boards can only supply $50\text{ mA}$, causing brownout reset loops. Power from a dedicated 3.3V 500mA LDO (like AMS1117-3.3).
- **Applying 5.0V to GPIO pins:** The ESP8266EX is NOT 5V tolerant. Connecting 5V signals directly to GPIO pins degrades and damages the chip over time. Use resistor voltage dividers or bidirectional level shifters.

## Notes

- **ESP8266EX vs ESP32:** ESP8266EX is single-core 80MHz with 2.4GHz Wi-Fi; ESP32 is dual-core 240MHz with Wi-Fi + Bluetooth LE.
