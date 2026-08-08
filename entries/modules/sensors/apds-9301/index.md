## Overview

The **APDS-9301** is a low-voltage 16-bit digital ambient light sensor (ALS) manufactured by Broadcom (formerly Avago Technologies). Housed in an ultra-small $2.6 \times 2.0\text{ mm}$ 6-pin ChipLED package, it converts illuminance (Lux) into digital $I^2C$ output codes.

The APDS-9301 incorporates two integrating photodiodes on a single chip:
- **Channel 0 (`CH0`):** Detects both Visible and Infrared (IR) light.
- **Channel 1 (`CH1`):** Detects Infrared (IR) light only.

By subtracting Channel 1 from Channel 0 in software, the sensor compensates for ambient IR background radiation (from incandescent bulbs or sunlight), providing a human-eye spectral response curve across illuminance levels from **0.1 Lux to 40,000 Lux**.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 2.7 V to 3.6 V DC (3.0 V nominal) |
| **Interface** | $I^2C$ (up to 400 kHz) |
| **Default $I^2C$ address** | `0x39` (`ADDR` pin floating); configurable to `0x29` (GND) or `0x49` (VCC) |
| **Dynamic range** | 0.1 Lux to 40,000 Lux |
| **Internal ADCs** | Dual 16-bit integrating ADCs (CH0 & CH1) |
| **Operating current** | $240\ \mu\text{A}$ active / $3.2\ \mu\text{A}$ power-down |
| **Interrupt output** | Programmable threshold `INT` pin |

## Pinout

Standard 5-pin 0.1" (2.54 mm) breakout module header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+2.7 V to +3.6 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 4 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 5 | `INT` | Digital Output | Active-Low interrupt output (programmable lux thresholds) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 2.7 | 3.0 | 3.6 | V | DC |
| Active Supply Current | $I_{DD}$ | — | 240 | 350 | µA | Active integration state |
| Power-Down Current | $I_{pd}$ | — | 3.2 | 6.0 | µA | Software power-down |
| $I^2C$ Clock Frequency | $f_{SCL}$ | 0 | 100 | 400 | kHz | Standard / Fast mode |
| Integration Time (13.7ms)| $t_{int1}$ | 13.0 | 13.7 | 14.4 | ms | 13-bit max count (5,047) |
| Integration Time (101ms) | $t_{int2}$ | 96 | 101 | 106 | ms | 15-bit max count (37,177) |
| Integration Time (402ms) | $t_{int3}$ | 382 | 402 | 422 | ms | 16-bit max count (65,535) |

## $I^2C$ Protocol & Lux Calculation

To calculate true Lux from raw channel readings ($CH0$ and $CH1$):

1. **Calculate Ratio:** $R = \frac{CH1}{CH0}$.
2. **Apply Empirical Formula (for $0 < R \le 0.52$):**

$$ \text{Lux} = 0.0304 \times CH0 - 0.062 \times CH0 \times \left( \frac{CH1}{CH0} \right)^{1.4} $$

3. **High IR Conditions ($0.52 < R \le 0.65$):**

$$ \text{Lux} = 0.0224 \times CH0 - 0.031 \times CH1 $$

## Wiring

| APDS-9301 Pin | → | Arduino Uno (with 3.3V supply) | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 3.3V | 3.3V | **Do not connect to 5V** |
| `GND` | | GND | GND | System ground |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |

## Example

```cpp
#include <Wire.h>

#define APDS9301_ADDR 0x39

void setup() {
  Serial.begin(9600);
  Wire.begin();

  // Power ON sensor (Control Register 0x80 = 0x03)
  Wire.beginTransmission(APDS9301_ADDR);
  Wire.write(0x80); // Command byte + Control Register
  Wire.write(0x03); // Power ON
  Wire.endTransmission();
}

void loop() {
  // Read CH0 LSB & MSB (Register 0x8C)
  Wire.beginTransmission(APDS9301_ADDR);
  Wire.write(0xAC); // Command word + Word read starting at 0x0C
  Wire.endTransmission();

  Wire.requestFrom(APDS9301_ADDR, 2);
  uint16_t ch0 = Wire.read() | (Wire.read() << 8);

  Serial.print("Channel 0 (Visible+IR) Raw: ");
  Serial.println(ch0);

  delay(500);
}
```

## Common mistakes

- **Powering `VCC` directly from a 5V rail:** The APDS-9301 absolute maximum supply voltage is 3.8V. Supplying 5V destroys the ChipLED package.
- **Forgetting the command bit `0x80` in $I^2C$ writes:** Every register address write to APDS-9301 must set bit 7 (`0x80`) of the command byte to indicate a valid register select.

## Notes

- **APDS-9301 vs TSL2561:** Broadcom APDS-9301 and ams TSL2561 share functionally identical dual-channel architectures and $I^2C$ command registers.
