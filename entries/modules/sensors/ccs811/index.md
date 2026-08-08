## Overview

The **CCS811** is an ultra-low power digital metal-oxide (MOX) gas sensor solution manufactured by ams OSRAM for monitoring indoor air quality (IAQ). It integrates a micro-hotplate sensor element along with a dedicated 8-bit microcontroller that processes raw sensor resistance values and calculates Total Volatile Organic Compounds (TVOC in parts per billion, ppb) and equivalent carbon dioxide ($\text{eCO}_2$ in parts per million, ppm).

Communicating over $I^2C$, the CCS811 supports environmental temperature and humidity compensation inputs (from external sensors like the BME280 or HDC1080) to improve baseline stability. It is widely incorporated into home automation systems, air purifiers, ESPHome nodes, and indoor environment monitors.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.0 V DC (breakout module with LDO) |
| **IC supply voltage (`VDD`)** | 1.8 V to 3.6 V DC (3.3 V nominal) |
| **Interface** | $I^2C$ (up to 400 kHz) |
| **Default $I^2C$ address** | `0x5A` (`ADDR` pin Low / un-connected) |
| **Alternate $I^2C$ address** | `0x5B` (`ADDR` pin High to `VCC`) |
| **$\text{eCO}_2$ measurement range** | 400 ppm to 8192 ppm |
| **TVOC measurement range** | 0 ppb to 1187 ppb |
| **Power modes** | Mode 0 (Idle), Mode 1 (1s), Mode 2 (10s), Mode 3 (60s), Mode 4 (250ms) |
| **Active current draw** | 26 mA (Mode 1 continuous) / 1.2 mA (Mode 3 low power) |

## Pinout

Breakout modules feature a 7-pin or 8-pin 0.1" (2.54 mm) header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 4 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 5 | `WAK` / `WAKE` | Digital Input | Active-Low wake pin (**MUST be tied to GND** for active $I^2C$) |
| 6 | `INT` | Digital Output | Active-Low interrupt output (goes Low when new data ready) |
| 7 | `RST` / `RESET` | Digital Input | Active-Low hardware reset pin (pull High to $V_{CC}$ if unused) |
| 8 | `ADD` / `ADDR` | Digital Input | $I^2C$ Address select (Low = `0x5A`, High = `0x5B`) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{CC}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Module with 3.3V regulator |
| Operating Current (Mode 1) | $I_{mode1}$ | — | 26 | 30 | mA | 1-second pulse measurement interval |
| Operating Current (Mode 3) | $I_{mode3}$ | — | 1.2 | 2.0 | mA | 60-second pulse measurement interval |
| $\text{eCO}_2$ Measurement Range | $eCO_2$ | 400 | — | 8192 | ppm | Equivalent $\text{CO}_2$ based on VOCs |
| TVOC Measurement Range | $TVOC$ | 0 | — | 1187 | ppb | Total Volatile Organic Compounds |
| Initial Sensor Burn-In | $t_{burnin}$ | 48 | — | — | hours | Recommended initial burn-in time |
| Warm-Up Time | $t_{warmup}$ | 20 | — | — | minutes | Warm-up time after cold start |
| Operating Temperature | $T_{opr}$ | -5 | — | 50 | °C | Ambient operating temperature |

## Register map

| Address | Register | Access | Reset | Description |
|---|---|---|---|---|
| `0x00` | `STATUS` | Read | `0x00` | Status register (bit 3: `DATA_READY`, bit 4: `APP_VALID`) |
| `0x01` | `MEAS_MODE` | R/W | `0x00` | Measurement mode and interrupt control |
| `0x02` | `ALG_RESULT_DATA` | Read | — | 4-byte payload: $\text{eCO}_2$ (bytes 0–1), TVOC (bytes 2–3) |
| `0x05` | `ENV_DATA` | Write | — | 4-byte payload for temperature and relative humidity compensation |
| `0xF4` | `APP_START` | Write | — | Write to transition from bootloader into Application mode |
| `0xFF` | `SW_RESET` | Write | — | Reset sequence (`0x11 0xE5 0x72 0x8A`) |

## Wiring

| CCS811 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Module onboard LDO |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |
| `WAKE` | | GND | GND | **Connect to GND** to enable $I^2C$ communications |
| `RESET` | | 5V | 3.3V | Tie to $V_{CC}$ or leave floating (internal pull-up) |

> [!WARNING]
> Floating `WAKE` pin hazard:
> - The `WAKE` pin is Active-Low. If left floating or connected to $V_{CC}$, the onboard MCU remains in ultra-low power sleep and **will not respond to $I^2C$ address `0x5A`**.
> - Always connect `WAKE` to `GND` (or control it via MCU GPIO).

## Example

```cpp
#include <Wire.h>
#include "Adafruit_CCS811.h"

Adafruit_CCS811 ccs;

void setup() {
  Serial.begin(115200);
  Serial.println("Initializing CCS811 Air Quality Sensor...");

  if (!ccs.begin(0x5A)) {
    Serial.println("Failed to start CCS811! Ensure WAKE pin is connected to GND.");
    while (1);
  }

  // Wait for sensor to become ready
  while (!ccs.available());
  Serial.println("CCS811 ready.");
}

void loop() {
  if (ccs.available()) {
    if (!ccs.readData()) {
      Serial.print("CO2: ");
      Serial.print(ccs.geteCO2());
      Serial.print(" ppm | TVOC: ");
      Serial.print(ccs.getTVOC());
      Serial.println(" ppb");
    } else {
      Serial.println("Error reading CCS811 data!");
    }
  }
  delay(1000);
}
```

## Common mistakes

- **Leaving `WAKE` floating:** The sensor ignores all $I^2C$ commands unless `WAKE` is grounded.
- **Conflating $\text{eCO}_2$ with true NDIR $\text{CO}_2$:** The CCS811 estimates equivalent $\text{CO}_2$ ($\text{eCO}_2$) by measuring hydrogen and volatile organic gas levels, assuming human breath correlates with VOCs. It does not contain an NDIR optical absorption cell and will not measure pure $\text{CO}_2$ accurately in non-human-occupied spaces.
- **Skipping initial 48-hour burn-in:** MOX sensor materials undergo initial resistance stabilization. Readings during the first 48 hours of power-on exhibit drift.
- **Forgetting temperature/humidity compensation:** Supplying live temperature and humidity values to `ENV_DATA` significantly improves accuracy in changing ambient environments.

## Notes

- **CCS811 vs SGP30:** Sensirion SGP30 and ams CCS811 are direct competitors in the metal-oxide indoor air quality market.
