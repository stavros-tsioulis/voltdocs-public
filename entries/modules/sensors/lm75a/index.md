## Overview

The **LM75A** is an 11-bit digital temperature sensor and thermal watchdog manufactured by NXP Semiconductors, Texas Instruments, and Maxim Integrated. Operating over an $I^2C$ bus, it measures ambient temperatures from **$-55^\circ\text{C}$ to $+125^\circ\text{C}$** with a resolution of $0.125^\circ\text{C}$ ($1/8^\circ\text{C}$) and accuracy of $\pm 2.0^\circ\text{C}$.

Featuring a dedicated open-drain Over-temperature Shutdown (`OS`) output pin, the LM75A can operate as a standalone programmable hardware thermostat (thermal watchdog), pulling the `OS` pin Low when temperature exceeds the programmed `T_OS` limit threshold and releasing it when temperature drops below the `T_HYST` hysteresis threshold. It is widely used in server rack monitoring, 3D printer enclosure thermal protection, and ESPHome environmental nodes.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 2.8 V to 5.5 V DC |
| **Interface** | $I^2C$ (up to 400 kHz) |
| **Default $I^2C$ address** | `0x48` ($A_0, A_1, A_2 \to \text{GND}$) |
| **Configurable addresses** | 8 hardware addresses (`0x48` to `0x4F` via $A_0, A_1, A_2$ pins) |
| **Temperature range** | $-55^\circ\text{C}$ to $+125^\circ\text{C}$ |
| **ADC resolution** | 11-bit ($0.125^\circ\text{C}$ per LSB) |
| **Thermal Alarm (`OS`)** | Open-drain interrupt / thermostat control output |
| **Operating current** | $250\ \mu\text{A}$ active / $1.0\ \mu\text{A}$ shutdown |

## Pinout (SOIC-8 / TSSOP-8 Package & Breakout Header)

```
             ┌───┴───┐
         SDA ─┤ 1    8├─ VCC
         SCL ─┤ 2    7├─ A0
          OS ─┤ 3    6├─ A1
         GND ─┤ 4    5├─ A2
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 2 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 3 | `OS` | Open-Drain Output | Over-temperature Shutdown alarm pin |
| 4 | `GND` | Power | Ground reference (0 V) |
| 5 | `A2` | Digital Input | $I^2C$ Address bit 2 |
| 6 | `A1` | Digital Input | $I^2C$ Address bit 1 |
| 7 | `A0` | Digital Input | $I^2C$ Address bit 0 |
| 8 | `VCC` | Power | Supply input (+2.8 V to +5.5 V DC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.8 | 3.3 / 5.0 | 5.5 | V | DC |
| Temp Accuracy ($-25\dots 100^\circ\text{C}$) | $T_{acc1}$ | -2.0 | $\pm 1.0$ | +2.0 | °C | Main operating range |
| Temp Accuracy ($-55\dots 125^\circ\text{C}$) | $T_{acc2}$ | -3.0 | $\pm 1.5$ | +3.0 | °C | Extreme range |
| Resolution | $T_{res}$ | — | 0.125 | — | °C | 11-bit 2's complement |
| Conversion Time | $t_{conv}$ | — | 100 | 300 | ms | Single conversion |
| Shutdown Current | $I_{sd}$ | — | 1.0 | 3.5 | µA | Software shutdown mode |

## Register Map & Data Format

The temperature data register (`0x00`) returns 2 bytes in 11-bit 2's complement format (left-justified):

- **Byte 1:** Integer temperature bits 10–3.
- **Byte 2 (Bits 7–5):** Fractional temperature bits 2–0 ($0.125^\circ\text{C}$ per count).

$$ \text{Temperature } (^\circ\text{C}) = \frac{\text{Raw 11-Bit Signed Value}}{8} = \frac{\text{(Byte 1 } \ll 3) \mid (\text{Byte 2 } \gg 5)}{8} $$

## Wiring

| LM75A Pin | → | Arduino Uno | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |
| `OS`  | | Digital D2 | GPIO 4 | Open-drain alarm pin (requires $10\text{ k}\Omega$ pull-up) |

## Example

```cpp
#include <Wire.h>

#define LM75A_ADDR 0x48

void setup() {
  Serial.begin(9600);
  Wire.begin();
}

void loop() {
  Wire.beginTransmission(LM75A_ADDR);
  Wire.write(0x00); // Select Temperature Register
  Wire.endTransmission();

  Wire.requestFrom(LM75A_ADDR, 2);
  if (Wire.available() >= 2) {
    int16_t raw = (Wire.read() << 8) | Wire.read();
    // Shift right by 5 to get 11-bit signed value
    raw >>= 5;
    
    // Handle 11-bit sign extension
    if (raw & (1 << 10)) {
      raw |= 0xF800; // Sign extend negative values
    }

    float tempC = raw * 0.125;
    Serial.print("LM75A Temperature: "); Serial.print(tempC); Serial.println(" °C");
  }

  delay(1000);
}
```

## Common mistakes

- **Not bit-shifting the 2nd byte right by 5 bits:** The LM75A formats its 11-bit reading left-justified across 2 bytes. Reading raw 16-bit integers without right-shifting by 5 results in values multiplied by 32.
- **Floating address pins $A_0, A_1, A_2$:** On raw DIP/SOIC IC packages, tie $A_0, A_1, A_2$ to GND or $V_{CC}$ to lock the $I^2C$ address.

## Notes

- **LM75A vs TMP102:** LM75A is 11-bit ($0.125^\circ\text{C}$); TMP102 is 12-bit ($0.0625^\circ\text{C}$). Both share near-identical register structures.
