## Overview

The **MH-Z19B** is an NDIR (Non-Dispersive Infrared) carbon dioxide ($\text{CO}_2$) gas sensor manufactured by Winsen Electronics. It utilizes infrared absorption spectroscopy to accurately measure atmospheric $\text{CO}_2$ concentration from **400 ppm to 5,000 ppm** (with optional 10,000 ppm variant).

The gold-plated optical chamber houses an internal IR light source, a narrow bandpass optical filter, an IR detector, and temperature compensation. It outputs concentration data via **UART serial** (9600 baud) and a **PWM duty cycle** output line.

## Quick reference

| | |
|---|---|
| **Operating Voltage (`Vin`)** | 4.5 V to 5.5 V DC (5.0 V nominal) |
| **Measurement Range** | 400 ppm to 5,000 ppm $\text{CO}_2$ |
| **Accuracy** | $\pm (50\text{ ppm} + 3\%\text{ of reading})$ |
| **Warm-up Time** | 3 minutes (180 seconds) |
| **UART Interface** | 9600 baud, 8 data bits, 1 stop bit, no parity (`9600,N,8,1`) |
| **PWM Cycle Period** | 1004 ms ($\text{PPM} = 5000 \times \frac{T_H - 2\text{ms}}{1000\text{ms}}$) |
| **Average Current** | $< 40\text{ mA}$ average / 150 mA peak during IR heating |

## Pinout

### Standard 7-Pin Gold Module Header

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `Vout` / `VO` | Analog Output | Analog voltage output (0.4 V to 2.0 V, optional) |
| 2 | `NC` | Not Connected | Unused |
| 3 | `GND` | Power | Ground (0 V) |
| 4 | `Vin` | Power Input | Supply voltage (+4.5 V to +5.5 V DC) |
| 5 | `Rx` | Digital Input | UART Receive line (3.3V TTL logic level input) |
| 6 | `Tx` | Digital Output | UART Transmit line (3.3V TTL logic level output) |
| 7 | `PWM` | Digital Output | PWM output pin (pulse width proportional to CO2 PPM) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{IN}$ | 4.5 | 5.0 | 5.5 | V | DC |
| Average Current | $I_{AVG}$ | — | 40 | 60 | mA | Active operating mode |
| Peak Current | $I_{PEAK}$ | — | 150 | 200 | mA | IR lamp pulse |
| Preheating Time | $t_{warmup}$ | — | 180 | — | s | Initial stabilization |
| Response Time ($t_{90}$) | $\tau$ | — | $< 120$ | — | s | Natural convection |
| Temperature Drift | $\Delta T$ | — | $\pm 0.2$ | — | % FS/°C | Internal temp compensation |

## UART Command Protocol (9600 Baud)

Send a 9-byte packet to read $\text{CO}_2$ concentration:
- **Request Command:** `0xFF 0x01 0x86 0x00 0x00 0x00 0x00 0x00 0x79`
- **Response Packet (9 Bytes):** `0xFF 0x86 HIGH LOW TT 0x00 0x00 0x00 CS`

$$\text{CO}_2\text{ Concentration (PPM)} = (\text{Byte}_2 \times 256) + \text{Byte}_3$$

Check Byte 8 Checksum ($CS$): $CS = 0xFF - (\text{Sum of Bytes 1 to 7}) + 1$.

## Wiring

| MH-Z19B Module Pin | → | Microcontroller (Arduino / ESP32) | Notes |
|---|---|---|---|
| `Vin` | | `5V` | **Requires 5V supply for internal IR lamp** |
| `GND` | | `GND` | Ground |
| `Tx` | | `RX` (e.g. GPIO16 / D2 for SoftwareSerial) | 3.3V TTL output |
| `Rx` | | `TX` (e.g. GPIO17 / D3 for SoftwareSerial) | 3.3V TTL input |
| `PWM` | | GPIO Pin (optional for PWM reading) | Pulse width proportional to PPM |

> [!WARNING]
> Automatic Zero Calibration (ABC) Warning:
> By default, the MH-Z19B has **ABC (Automatic Baseline Calibration)** enabled. Every 24 hours, the module assumes the lowest $\text{CO}_2$ concentration it recorded during that period was $400\text{ ppm}$ (fresh outdoor air). If used continuously in an unventilated bedroom or greenhouse, ABC will miscalibrate. Disable ABC via UART command `0x79` for indoor environments.

## Common mistakes

- **Powering from 3.3V:** Operating the sensor from a 3.3V rail causes incomplete IR lamp heating and erratic UART timeouts. Always supply **5.0 V DC**.
- **Inverted RX/TX lines:** Connecting module `Tx` to MCU `TX`.
- **Forgetting 3-minute warm-up:** Reading data immediately upon cold boot outputs invalid readings ($400\text{ ppm}$ or $5000\text{ ppm}$). Wait 180 seconds after applying power.

## Notes

- Fully supported in ESPHome via the dedicated `mhz19` component.
