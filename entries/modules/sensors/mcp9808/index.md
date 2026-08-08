## Overview

The **MCP9808** is a high-accuracy digital temperature sensor manufactured by Microchip Technology. Operating across a wide supply range of **$2.7\text{V}$ to $5.5\text{V}$ DC**, it converts temperature to a 16-bit digital word over an $I^2C$ bus.

Featuring a typical accuracy of **$\pm 0.25^\circ\text{C}$** from $-40^\circ\text{C}$ to $+125^\circ\text{C}$ ($\pm 0.5^\circ\text{C}$ guaranteed maximum), the MCP9808 offers four user-selectable measurement resolutions ($0.5^\circ\text{C}, 0.25^\circ\text{C}, 0.125^\circ\text{C}$, and **$0.0625^\circ\text{C}$ default**). It includes programmable upper, lower, and critical temperature limit registers with an active hardware `ALERT` output pin.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VDD`)** | 2.7 V to 5.5 V DC (3.3 V or 5.0 V nominal) |
| **Interface** | $I^2C$ / SMBus (up to 400 kHz) |
| **Default $I^2C$ address** | `0x18` (`A0`, `A1`, `A2` tied to GND) |
| **Configurable addresses** | 8 distinct addresses (`0x18` through `0x1F` via 3 address pins) |
| **Typical accuracy ($-40^\circ\text{C}$ to $+125^\circ\text{C}$)**| $\pm 0.25^\circ\text{C}$ typical / $\pm 0.5^\circ\text{C}$ max |
| **Default resolution** | 16-bit ($0.0625^\circ\text{C}$ per LSB / $1/16^\circ\text{C}$) |
| **Conversion time** | 250 ms at $0.0625^\circ\text{C}$ resolution / 30 ms at $0.5^\circ\text{C}$ resolution |
| **Operating current** | $200\ \mu\text{A}$ active / $0.1\ \mu\text{A}$ shutdown mode |

## Pinout (8-Pin MSOP Package & Breakout Header)

```
             ┌───┴───┐
          VDD ─┤ 1    8├─ GND
          SCL ─┤ 2    7├─ A0
          SDA ─┤ 3    6├─ A1
        ALERT ─┤ 4    5├─ A2
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VDD` | Power | Supply power input (+2.7 V to +5.5 V DC) |
| 2 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 3 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 4 | `ALERT` | Digital Output | Programmable temperature alert output pin (Open-drain) |
| 5 | `A2` | Digital Input | $I^2C$ Address Bit 2 (Default GND) |
| 6 | `A1` | Digital Input | $I^2C$ Address Bit 1 (Default GND) |
| 7 | `A0` | Digital Input | $I^2C$ Address Bit 0 (Default GND) |
| 8 | `GND` | Power | Ground reference (0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 2.7 | 3.3 / 5.0 | 5.5 | V | DC |
| Active Supply Current | $I_{DD}$ | — | 200 | 400 | µA | Active sampling state |
| Shutdown Current | $I_{sd}$ | — | 0.1 | 2.0 | µA | Software shutdown mode |
| Accuracy ($-20^\circ\text{C} \dots +100^\circ\text{C}$)| $T_{acc1}$ | -0.5 | $\pm 0.25$ | +0.5 | °C | Max error bound |
| Accuracy ($-40^\circ\text{C} \dots +125^\circ\text{C}$)| $T_{acc2}$ | -1.0 | $\pm 0.5$ | +1.0 | °C | Full operational spectrum |
| LSB Resolution ($Mode = 3$)| $Res_3$ | — | 0.0625 | — | °C | 16-bit 2's complement |

## Data Format & Celsius Math

The ambient temperature register (**`0x05`**) returns a 16-bit word formatted as follows:

- **Bit 15–13:** Flag bits (`Sign`, `T_CRIT`, `T_UPPER`, `T_LOWER`).
- **Bit 12:** Sign bit ($0 = \text{Positive}, 1 = \text{Negative}$).
- **Bits 11–0:** 12-bit temperature value in $0.0625^\circ\text{C}$ steps.

### Positive Temperature Calculation

$$ \text{Temperature } (^\circ\text{C}) = \frac{\text{Raw Register Value } \& \text{ 0x1FFF}}{16.0} $$

### Negative Temperature Calculation (Sign Bit 12 = 1)

$$ \text{Temperature } (^\circ\text{C}) = 256.0 - \frac{\text{Raw Register Value } \& \text{ 0x1FFF}}{16.0} $$

## Wiring

| MCP9808 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VDD` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |

## Example (Adafruit_MCP9808 Library)

```cpp
#include <Wire.h>
#include "Adafruit_MCP9808.h"

Adafruit_MCP9808 tempsensor = Adafruit_MCP9808();

void setup() {
  Serial.begin(115200);
  while (!Serial) delay(10);

  Serial.println("MCP9808 High-Accuracy Temperature Sensor Test");

  // Default address 0x18
  if (!tempsensor.begin(0x18)) {
    Serial.println("MCP9808 not found! Check I2C wiring.");
    while (1);
  }

  // Set resolution to Mode 3 (0.0625°C resolution, 250ms conversion)
  tempsensor.setResolution(3);
  Serial.println("MCP9808 initialized.");
}

void loop() {
  tempsensor.wake(); // Wake up sensor

  float c = tempsensor.readTempC();
  float f = c * 9.0 / 5.0 + 32.0;

  Serial.print("Temperature: "); Serial.print(c, 4); Serial.print(" °C | ");
  Serial.print(f, 4); Serial.println(" °F");

  tempsensor.shutdown_modes(1); // Sleep to save power
  delay(2000);
}
```

## Common mistakes

- **Leaving `A0`, `A1`, `A2` floating:** On standalone IC breakout boards, address pins `A0`, `A1`, `A2` must be pulled to GND or VDD. Floating address pins cause $I^2C$ address changes between `0x18` and `0x1F`.
- **PCB thermal conduction:** Mount the sensor away from warm power supplies to avoid measuring PCB heat instead of ambient air.

## Notes

- **MCP9808 vs TMP117 vs DS18B20:** MCP9808 provides $\pm 0.25^\circ\text{C}$ accuracy over $I^2C$; TMP117 provides $\pm 0.1^\circ\text{C}$ medical-grade accuracy; DS18B20 provides $\pm 0.5^\circ\text{C}$ over 1-Wire.
