## Overview

The **RFM95W** is a low-power, long-range wireless transceiver module manufactured by HopeRF. Powered by Semtech's **SX1276** LoRa (Long Range) modem engine, it operates in the sub-GHz license-free ISM bands (**868 MHz** in Europe, **915 MHz** in the Americas and Australia).

Using chirp spread spectrum (CSS) modulation, the RFM95W achieves receiver sensitivities down to **-148 dBm** and transmit power up to **+20 dBm** ($100\text{ mW}$). This enables point-to-point wireless ranges of several kilometers line-of-sight and integration into **LoRaWAN** IoT gateway networks.

## Quick reference

| | |
|---|---|
| **Operating Voltage (`VDD`)** | 1.8 V to 3.7 V DC (3.3 V nominal) |
| **Logic Levels** | 3.3 V TTL (requires level shifting for 5V MCUs) |
| **Frequency Bands** | 868 MHz (EU) / 915 MHz (US/AU) |
| **RF Transmit Power** | +5 to +20 dBm (up to 100 mW software configurable) |
| **Receiver Sensitivity** | Down to -148 dBm |
| **Communication Interface** | 4-wire SPI (up to 10 MHz) + hardware DIO interrupt pins |
| **Peak Transmit Current** | 120 mA (+20 dBm output) |
| **Receive Current** | 10.3 mA |
| **Sleep Current** | 0.2 µA |

## Pinout

### Standard 16-Pin Castellation Module Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` | Power | Ground (0 V) |
| 2 | `MISO` | Digital Output | SPI Master Input Slave Output |
| 3 | `MOSI` | Digital Input | SPI Master Output Slave Input |
| 4 | `SCK` | Digital Input | SPI Clock input |
| 5 | `NSS` / `CS` | Digital Input | SPI Chip Select (Active-LOW) |
| 6 | `RESET` | Digital Input | Active-LOW Reset input pin |
| 7, 8, 9, 10, 11 | `DIO0`–`DIO4` | Digital Output | Configurable Digital I/O Interrupt pins (`DIO0` = TxDone/RxDone) |
| 12 | `DIO5` | Digital Output | Configurable ModeReady interrupt pin |
| 13 | `3.3V` / `VDD` | Power | Supply voltage (+1.8 V to +3.7 V DC) |
| 14 | `GND` | Power | Ground |
| 15 | `ANA` / `ANT` | RF I/O | RF Antenna connection point (50 Ω impedance) |
| 16 | `GND` | Power | RF Ground shield |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 1.8 | 3.3 | 3.7 | V | DC |
| Transmit Current (+20dBm) | $I_{TX}$ | — | 120 | 130 | mA | PA_BOOST pin enabled |
| Transmit Current (+13dBm) | $I_{TX13}$ | — | 29 | 35 | mA | RFO pin enabled |
| Receive Current | $I_{RX}$ | — | 10.3 | 12.0 | mA | LoRa Mode, $BW = 125\text{ kHz}$ |
| Spreading Factor | $SF$ | 6 | — | 12 | — | Configurable (SF6 to SF12) |
| Bandwidth | $BW$ | 7.8 | 125 | 500 | kHz | Configurable |
| Frequency Error | $\Delta f$ | -10 | — | +10 | ppm | Crystal accuracy |

## Spreading Factor (SF) vs Range Trade-off

| Spreading Factor | Bit Rate (BW = 125 kHz) | Sensitivity | Airtime (20-byte payload) | Link Budget / Distance |
|---|---|---|---|---|
| **SF7** | 5.47 kbps | -123 dBm | 56 ms | Shortest Range / Fast speed |
| **SF9** | 1.76 kbps | -129 dBm | 185 ms | Medium Range |
| **SF12** | 0.29 kbps | -137 dBm | 1482 ms | Maximum Range / Slow speed |

## Wiring

| RFM95W Module / Breakout Pin | → | Microcontroller (Arduino / ESP32) | Notes |
|---|---|---|---|
| `VIN` / `3.3V` | | `3.3V` | **Do NOT connect to 5V!** |
| `GND` | | `GND` | Ground |
| `EN` / `RESET` | | GPIO Pin (e.g. D9 / GPIO14) | Reset control |
| `G0` / `DIO0` | | GPIO Pin with Interrupt (e.g. D2 / GPIO26) | **Required for RxDone / TxDone events** |
| `SCK` | | SPI `SCK` (D13 on Uno / GPIO18 on ESP32) | SPI Clock |
| `MISO` | | SPI `MISO` (D12 on Uno / GPIO19 on ESP32) | SPI Data Out |
| `MOSI` | | SPI `MOSI` (D11 on Uno / GPIO23 on ESP32) | SPI Data In |
| `CS` / `NSS` | | SPI `SS` / GPIO (D10 on Uno / GPIO5 on ESP32) | Chip Select |

> [!WARNING]
> Antenna Requirement Warning:
> NEVER power ON or transmit with an RFM95W module without a $50\text{ }\Omega$ antenna (or a $8.2\text{ cm}$ wire for 868 MHz / $8.6\text{ cm}$ wire for 915 MHz) attached to the `ANT` pin. Transmitting without an antenna creates RF energy reflection that will permanently burn out the internal Power Amplifier (PA).

## Common mistakes

- **Powering from 5.0V or connecting 5V SPI signals:** The SX1276 silicon die is NOT 5V tolerant. Always use 3.3V supply and level shifters on 5V microcontrollers.
- **Forgetting `DIO0` interrupt connection:** Libraries like RadioHead or LMIC rely on hardware interrupts on `DIO0` to signal packet reception. Leaving `DIO0` disconnected will cause software wait timeouts.
- **Frequency mismatch:** Operating an 868 MHz module on 915 MHz software settings degrades output power and range severely.

## Notes

- Compatible with popular open-source libraries like `RadioHead` (RH_RF95) and `MCCI LoRaWAN LMIC` framework.
