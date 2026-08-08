## Overview

The **AHT20** (and its predecessor AHT10) is a digital MEMS temperature and humidity sensor manufactured by ASAIR (Aosong Electronics). Equipped with a custom ASIC signal processing chip, a capacitive MEMS humidity sensing element, and an on-chip temperature sensor, the AHT20 delivers factory-calibrated digital measurements over an $I^2C$ bus.

Providing higher accuracy ($\pm 0.3^\circ\text{C}$ temperature, $\pm 2\%\text{ RH}$ relative humidity), lower power consumption, and standard SMD packaging at a low cost, the AHT20 has emerged as a popular replacement for older legacy sensors like the DHT11 and DHT22 in indoor air-quality monitors, smart thermostats, and ESPHome weather stations.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 2.0 V to 5.5 V DC |
| **Interface** | $I^2C$ (Standard Mode 100 kHz / Fast Mode 400 kHz) |
| **$I^2C$ Address** | `0x38` (Fixed) |
| **Temperature range** | $-40^\circ\text{C}$ to $+85^\circ\text{C}$ ($\pm 0.3^\circ\text{C}$ typ.) |
| **Humidity range** | $0\%$ to $100\%\text{ RH}$ ($\pm 2\%\text{ RH}$ typ.) |
| **Measurement current** | $0.98\text{ mA}$ active / $0.25\ \mu\text{A}$ standby |
| **Response time** | $t_63\% \le 8\text{ s}$ |

## Pinout

Breakout modules feature a standard 4-pin 0.1" (2.54 mm) header or Qwiic / STEMMA QT connector:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+2.0 V to +5.5 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SCL` | Digital Input | $I^2C$ Serial Clock (requires pull-up resistor) |
| 4 | `SDA` | Digital Input / Output | $I^2C$ Serial Data (requires pull-up resistor) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.0 | 3.3 / 5.0 | 5.5 | V | DC |
| Supply Current (Measuring) | $I_{CC}$ | — | 0.98 | 1.5 | mA | $V_{CC} = 3.3\text{ V}$ during conversion |
| Supply Current (Standby) | $I_{sb}$ | — | 0.25 | 1.0 | µA | Sleep state |
| Temperature Resolution | $T_{res}$ | — | 0.01 | — | °C | 20-bit output |
| Temperature Accuracy | $T_{acc}$ | -0.3 | $\pm 0.3$ | +0.3 | °C | $0^\circ\text{C}$ to $55^\circ\text{C}$ |
| Relative Humidity Resolution | $RH_{res}$ | — | 0.024 | — | % RH | 20-bit output |
| Relative Humidity Accuracy | $RH_{acc}$ | -2.0 | $\pm 2.0$ | +2.0 | % RH | At $25^\circ\text{C}$, 10%–90% RH |
| $I^2C$ Clock Frequency | $f_{SCL}$ | 0 | 100 | 400 | kHz | Standard / Fast mode |

## $I^2C$ Communication & Protocol

The AHT20 uses a fixed 7-bit $I^2C$ address of **`0x38`**.

1. **Initialization:** Upon power-up ($V_{CC} > 2.0\text{V}$), wait 40 ms. Read status byte. If bit 3 (`0x08`) is 0, send initialization command `0xBE 0x08 0x00` and wait 10 ms.
2. **Trigger Measurement:** Send 3-byte command sequence `0xAC 0x33 0x00`.
3. **Read Data:** Wait 80 ms for measurement completion. Read 7 bytes from `0x38`:
   - Byte 0: Status byte (bit 7 = Busy flag: 0 ready, 1 measuring).
   - Bytes 1–3: 20-bit Raw Humidity data ($S_{RH}$).
   - Bytes 3–5: 20-bit Raw Temperature data ($S_{T}$).
   - Byte 6: CRC-8 checksum.

### Conversion Formulas

$$ \text{Relative Humidity (\% RH)} = \left( \frac{S_{RH}}{2^{20}} \right) \times 100\% $$

$$ \text{Temperature } (^\circ\text{C}) = \left( \frac{S_{T}}{2^{20}} \right) \times 200 - 50 $$

## Wiring

| Sensor Pin | → | Arduino Uno | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Wide 2.0V–5.5V supply range |
| `GND` | | GND | GND | Shared ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock ($4.7\text{ k}\Omega$ pull-up recommended) |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data ($4.7\text{ k}\Omega$ pull-up recommended) |

## Example

```cpp
#include <Wire.h>
#include <Adafruit_AHTX0.h>

Adafruit_AHTX0 aht;

void setup() {
  Serial.begin(9600);
  while (!Serial) delay(10);

  Serial.println("Initializing AHT20 Sensor...");
  if (!aht.begin()) {
    Serial.println("Could not find AHT20 sensor! Check wiring.");
    while (1) delay(10);
  }
  Serial.println("AHT20 initialized successfully.");
}

void loop() {
  sensors_event_t humidity, temp;
  aht.getEvent(&humidity, &temp);

  Serial.print("Temperature: ");
  Serial.print(temp.temperature);
  Serial.print(" °C | Humidity: ");
  Serial.print(humidity.relative_humidity);
  Serial.println(" %RH");

  delay(2000);
}
```

## Common mistakes

- **Not waiting 80 ms after measurement trigger:** Reading bytes before the busy bit (Status Bit 7) drops to 0 returns stale or zeroed 20-bit sensor payloads.
- **Conflating AHT10 and AHT20 initialization commands:** AHT10 uses `0xE1 0x08 0x00` while AHT20 requires `0xBE 0x08 0x00`. Modern libraries auto-detect and send the correct byte sequence.
- **Condensation on MEMS element:** Exposure to liquid water drops shifts capacitive readings temporarily. Allow the sensor 24 hours in dry ambient air to recover.

## Notes

- **AHT20 vs SHT31:** AHT20 offers comparable accuracy to Sensirion's SHT30/SHT31 at a lower unit cost, making it ideal for high-volume IoT nodes.
