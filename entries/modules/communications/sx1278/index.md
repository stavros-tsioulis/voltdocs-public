## Overview

The **SX1278** is a long-range, low-power wireless transceiver IC manufactured by Semtech. Sold commercially on popular breakout modules such as the **AI-Thinker Ra-02**, it operates in the **433 MHz** unlicensed ISM frequency band.

Utilizing Semtech's patented **LoRa (Long Range)** chirp spread spectrum (CSS) modulation, the SX1278 achieves extreme receiver sensitivities down to **$-148\text{ dBm}$** while delivering up to **$+20\text{ dBm}$ ($100\text{ mW}$)** transmit power. This enables robust line-of-sight wireless communication links exceeding **$5\text{ to }10\text{ kilometers}$** in rural environments over an SPI bus, outperforming traditional FSK/GFSK radio modules.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VDD`)** | 1.8 V to 3.7 V DC (3.3 V nominal) |
| **Nominal frequency** | 433 MHz ISM band (configurable 137 MHz to 525 MHz) |
| **Modulation schemes** | LoRa, FSK, GFSK, MSK, GMSK, OOK |
| **Interface** | SPI (Mode 0,0, up to 10 MHz) |
| **Transmit power** | Up to $+20\text{ dBm}$ ($100\text{ mW}$) programmable |
| **Receiver sensitivity** | Down to $-148\text{ dBm}$ (at Spreading Factor 12) |
| **Packet buffer** | 256-byte dual-port SRAM TX/RX FIFO |
| **I/O tolerance** | 3.3V logic (requires level shifters for 5V Arduinos) |

## Pinout (AI-Thinker Ra-02 Module Header)

```
             ┌───────────┐
         GND ─┤ 1      16├─ GND
        3.3V ─┤ 2      15├─ DIO1 / DIO2
       RESET ─┤ 3      14├─ DIO0
        DIO0 ─┤ 4      13├─ MISO
        DIO1 ─┤ 5      12├─ MOSI
        DIO2 ─┤ 6      11├─ SCK
        DIO3 ─┤ 7      10├─ NSS / CS
        GND  ─┤ 8       9├─ GND
             └───────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1, 8, 9, 16 | `GND` | Power | Ground reference (0 V) |
| 2 | `3.3V` | Power | Supply power input (+1.8 V to +3.7 V DC) |
| 3 | `RESET` | Digital Input | Active-Low hardware reset pin |
| 4 | `DIO0` | Digital Output | Interrupt 0 (RX Done / TX Done trigger) |
| 10 | `NSS` / `CS` | Digital Input | Active-Low SPI Chip Select |
| 11 | `SCK` | Digital Input | SPI Clock Input |
| 12 | `MOSI` | Digital Input | SPI Master Output Slave Input |
| 13 | `MISO` | Digital Output | SPI Master Input Slave Output |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 1.8 | 3.3 | 3.7 | V | DC power rail |
| Transmit Current (+20dBm)| $I_{tx\_20}$ | — | 120 | 140 | mA | Max power transmit (+20 dBm) |
| Transmit Current (+13dBm)| $I_{tx\_13}$ | — | 29 | 35 | mA | Standard power transmit |
| Receive Current | $I_{rx}$ | — | 12.1 | 14.0 | mA | Active reception mode |
| Sleep Current | $I_{sleep}$ | — | 0.2 | 1.0 | µA | Sleep mode |
| Spreading Factor (SF) | $SF$ | 6 | — | 12 | — | Programmable chirp factor |
| Bandwidth (BW) | $BW$ | 7.8 | 125 | 500 | kHz | Signal bandwidth |

## LoRa Modulation Parameters & Range Math

1. **Spreading Factor (SF 6 to 12):** Higher SF values increase receiver sensitivity and link range at the cost of lower data rate and longer airtime.
2. **Bandwidth (BW 125/250/500 kHz):** Wider bandwidths increase data throughput; narrower bandwidths increase signal range.
3. **Coding Rate (CR 4/5 to 4/8):** Forward Error Correction (FEC) rate.

$$ \text{Data Rate (bps)} = SF \times \frac{BW}{2^{SF}} \times CR $$

## Wiring

| SX1278 (Ra-02) Pin | → | Arduino Uno (via Level Shifter) | ESP32 | Notes |
|---|---|---|---|---|
| `3.3V` | | 3.3V Rail | 3.3V | **Do not connect to 5V** |
| `GND`  | | GND | GND | Shared system ground |
| `NSS` (CS) | | Digital D10 | GPIO 5 | SPI Chip Select |
| `SCK`  | | Digital D13 | GPIO 18 | SPI Clock |
| `MOSI` | | Digital D11 | GPIO 23 | SPI MOSI |
| `MISO` | | Digital D12 | GPIO 19 | SPI MISO |
| `DIO0` | | Digital D2 (INT0) | GPIO 2 | RX / TX Interrupt trigger |
| `RESET`| | Digital D9 | GPIO 14 | Hardware Reset |

> [!WARNING]
> No-Antenna Power Warning:
> - Never transmit on the SX1278 without an antenna connected to the IPEX connector or SMA pin. Transmitting $+20\text{ dBm}$ power into an open load causes RF energy reflection that will destroy the onboard Power Amplifier (PA).

## Example (Arduino `LoRa.h` Library by Sandeep Mistry)

```cpp
#include <SPI.h>
#include <LoRa.h>

#define SCK 18
#define MISO 19
#define MOSI 23
#define SS 5
#define RST 14
#define DIO0 2

void setup() {
  Serial.begin(115200);
  while (!Serial);

  Serial.println("SX1278 LoRa Transmitter Test");

  // Configure SPI pins for ESP32
  SPI.begin(SCK, MISO, MOSI, SS);
  LoRa.setPins(SS, RST, DIO0);

  // Initialize at 433 MHz
  if (!LoRa.begin(433E6)) {
    Serial.println("Starting LoRa failed! Check wiring & antenna.");
    while (1);
  }

  // Set transmit power to +17 dBm
  LoRa.setTxPower(17);
  Serial.println("SX1278 LoRa initialized at 433 MHz.");
}

int counter = 0;

void loop() {
  Serial.print("Sending packet: "); Serial.println(counter);

  LoRa.beginPacket();
  LoRa.print("VoltDocs Telemetry #");
  LoRa.print(counter);
  LoRa.endPacket();

  counter++;
  delay(5000);
}
```

## Common mistakes

- **Connecting 5V logic directly to SPI pins:** The SX1278 operates on 3.3V logic. Connecting 5V Arduino SPI signals directly to `NSS`, `SCK`, or `MOSI` damages the chip. Use a resistor divider or bi-directional logic level converter.
- **Conflating 433 MHz (SX1278) and 868/915 MHz (SX1276) versions:** SX1278 is tuned specifically for 433 MHz. Attempting to transmit at 868 MHz or 915 MHz results in extreme power loss due to internal RF matching network mismatch.

## Notes

- **SX1278 vs SX1276 vs RFM95W:** SX1278 is optimized for 433 MHz; SX1276 / RFM95W are optimized for 868 MHz (Europe) and 915 MHz (Americas).
