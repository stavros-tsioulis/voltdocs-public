## Overview

The **AS608** (and closely related ZFM-20 / FPM10A series) is an optical fingerprint reader module widely used in biometric security systems, smart door locks, and attendance loggers. It integrates an optical glass prism, internal blue illumination LEDs, a high-resolution CMOS image sensor, and a dedicated Synochip DSP image processing ASIC with onboard non-volatile flash memory.

Storing up to **300 fingerprint templates** in its internal flash memory, the AS608 performs onboard fingerprint feature extraction, 1:N pattern matching, and template management. It communicates with host microcontrollers (Arduino, ESP32, Raspberry Pi) over a simple 3.3V/5V TTL UART interface at **57,600 baud**.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.6 V to 6.0 V DC (5.0 V nominal) |
| **Interface** | TTL UART (57,600 bps default) & USB 1.1 |
| **Fingerprint capacity** | 300 templates |
| **Optical resolution** | 500 DPI |
| **Window size** | $14\text{ mm} \times 18\text{ mm}$ active optical glass prism |
| **Search/Match time** | $< 0.3\text{ seconds}$ (1:N search across 300 templates) |
| **Security ratings** | False Acceptance Rate (FAR) $< 0.001\%$, False Rejection Rate (FRR) $< 1.0\%$ |
| **Operating current** | $60\text{ mA}$ average / $120\text{ mA}$ peak during scan |

## Pinout

The module exposes a 6-pin 1.27 mm or 2.0 mm pitch cable connector:

| Pin | Cable Color | Name | Type | Description |
|---|---|---|---|---|
| 1 | Red | `VCC` | Power | Power supply input (+3.6 V to +6.0 V DC) |
| 2 | Black | `GND` | Power | Ground reference (0 V) |
| 3 | Yellow | `TX` | Digital Output | UART Transmit output pin (3.3V logic level) |
| 4 | White | `RX` | Digital Input | UART Receive input pin (3.3V/5V tolerant) |
| 5 | Blue | `TOUCH` / `WAKE`| Digital Output | Active-High finger detection output (pulls High when finger touches prism) |
| 6 | Green | `3.3V` | Power Output | 3.3V regulated output pin (max 20 mA) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 3.6 | 5.0 | 6.0 | V | DC |
| Active Scan Current | $I_{active}$| — | 60 | 120 | mA | Blue LEDs active |
| Standby Current | $I_{sb}$ | — | 10 | — | mA | Idle state |
| UART Baud Rate Range | $Baud$ | 9600 | 57600 | 115200| bps | Programmable (`$N \times 9600$`) |
| Image Processing Time | $t_{proc}$ | — | 0.2 | 0.5 | s | Feature vector extraction |
| Security Level | Level | 1 | 3 | 5 | — | Configurable 1 (lowest) to 5 (highest) |

## Command Packet Structure

All commands sent to the AS608 follow an 11-byte frame format:

- **Header (2 Bytes):** `0xEF 0x01`
- **Address (4 Bytes):** `0xFF 0xFF 0xFF 0xFF` (Default broadcast device address)
- **Package Identifier (1 Byte):** `0x01` (Command packet)
- **Package Length (2 Bytes):** Length of payload + checksum
- **Instruction Code (1 Byte):** e.g., `0x01` (Get Image), `0x02` (Generate Character File), `0x03` (Match Fingerprints), `0x06` (Store Template)
- **Checksum (2 Bytes):** Sum of Package ID + Length + Instruction + Payload

## Wiring

| AS608 Pin | → | Arduino (SoftwareSerial) | ESP32 | Notes |
|---|---|---|---|---|
| Red (`VCC`) | | 5V | 5V | Powers DSP and blue LEDs |
| Black (`GND`)| | GND | GND | System ground |
| Yellow (`TX`)| | Digital D2 (Software RX) | GPIO 16 (RX2) | 3.3V logic output |
| White (`RX`) | | Digital D3 (Software TX) | GPIO 17 (TX2) | 3.3V logic input |
| Blue (`TOUCH`)| | Digital D4 | GPIO 4 | Optional wake-up interrupt |

## Example (Arduino Adafruit_Fingerprint Library)

```cpp
#include <Adafruit_Fingerprint.h>

// Use SoftwareSerial on pins 2 (RX) and 3 (TX)
SoftwareSerial mySerial(2, 3);
Adafruit_Fingerprint finger = Adafruit_Fingerprint(&mySerial);

void setup() {
  Serial.begin(9600);
  while (!Serial);

  Serial.println("\nAS608 Fingerprint Sensor Test");
  finger.begin(57600);

  if (finger.verifyPassword()) {
    Serial.println("Found AS608 fingerprint sensor!");
  } else {
    Serial.println("Did not find fingerprint sensor :(");
    while (1);
  }

  finger.getTemplateCount();
  Serial.print("Sensor contains "); Serial.print(finger.templateCount); Serial.println(" enrolled templates");
}

void loop() {
  uint8_t p = finger.getImage();
  if (p == FINGERPRINT_OK) {
    Serial.println("Image taken");
    p = finger.image2Tz();
    if (p == FINGERPRINT_OK) {
      p = finger.fingerFastSearch();
      if (p == FINGERPRINT_OK) {
        Serial.print("MATCH FOUND! ID #"); Serial.print(finger.fingerID);
        Serial.print(" with confidence of "); Serial.println(finger.confidence);
      } else {
        Serial.println("No match found");
      }
    }
  }
  delay(50);
}
```

## Common mistakes

- **Using incorrect default baud rate:** Most AS608 modules ship configured for **57,600 baud**, not 9,600 baud. SoftwareSerial on 8-bit Arduinos must be initialized to 57,600 baud to establish connection.
- **Powering `VCC` with under-rated 3.3V supply:** The optical LED and CMOS sensor peak at **120 mA**. Powering `VCC` from 3.3V pins can cause brownouts during image acquisition.

## Notes

- **AS608 vs Capacitive Fingerprint Sensors (R503):** Optical sensors (AS608) use blue light prisms; capacitive sensors (R503) use flat ring metal contacts, offering thinner form factors and higher water resistance.
