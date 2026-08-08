## Overview

The **BMA180** is a 14-bit 3-axis ultra-high performance digital MEMS accelerometer manufactured by Bosch Sensortec. Operating over $I^2C$ or SPI, it features ultra-low noise, high resolution ($0.13\text{ mg/LSB}$ at $\pm 1g$), and seven programmable full-scale acceleration ranges ($\pm 1g, \pm 1.5g, \pm 2g, \pm 3g, \pm 4g, \pm 8g, \pm 16g$).

Equipped with programmable low-pass filtering, self-test functions, an onboard temperature sensor, and interrupt generators for tap, slope, and orientation detection, the BMA180 was a staple component on early SparkFun and Adafruit high-precision motion sensing breakout boards.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.0 V DC (breakout module with LDO) |
| **IC supply voltage (`VDD`)** | 1.62 V to 3.6 V DC (2.4 V nominal) |
| **Interface** | $I^2C$ (up to 400 kHz) & 4-Wire SPI (up to 10 MHz) |
| **Default $I^2C$ address** | `0x40` (`SDO` pin Low / un-connected) |
| **Alternate $I^2C$ address** | `0x41` (`SDO` pin High to 3.3V) |
| **Full-scale ranges** | $\pm 1g, \pm 1.5g, \pm 2g, \pm 3g, \pm 4g, \pm 8g, \pm 16g$ |
| **Resolution** | 14-bit 2's complement |
| **Current draw** | $650\ \mu\text{A}$ active / $0.1\ \mu\text{A}$ sleep |

## Pinout

Standard 8-pin 0.1" (2.54 mm) breakout module header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SCK` / `SCL` | Digital Input | $I^2C$ Clock / SPI Clock |
| 4 | `SDO` / `ADDR`| Digital Output | SPI Data Out / $I^2C$ Address Bit 0 (Low = `0x40`, High = `0x41`) |
| 5 | `SDI` / `SDA` | Digital Input / Output | $I^2C$ Data / SPI Serial Data Input |
| 6 | `CS` | Digital Input | SPI Chip Select (High = $I^2C$ mode, Low = SPI mode) |
| 7 | `INT` / `INT1` | Digital Output | Programmable interrupt output line |
| 8 | `VIO` | Power | Logic Reference voltage (1.62V to 3.6V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{CC}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | DC |
| Active Supply Current | $I_{CC}$ | — | 650 | 950 | µA | Full operation |
| Standby Current | $I_{sb}$ | — | 0.1 | 1.0 | µA | Sleep mode |
| Sensitivity ($\pm 1g$) | $S_{1g}$ | — | 8192 | — | LSB/g | 14-bit ($0.13\text{ mg/LSB}$) |
| Sensitivity ($\pm 2g$) | $S_{2g}$ | — | 4096 | — | LSB/g | 14-bit ($0.24\text{ mg/LSB}$) |
| Sensitivity ($\pm 16g$) | $S_{16g}$ | — | 512 | — | LSB/g | 14-bit ($1.95\text{ mg/LSB}$) |
| Bandwidth Cutoff | $f_{BW}$ | 10 | 150 | 1200 | Hz | Configurable digital low-pass filter |

## Register Map & Calibration

| Address | Register | Access | Reset | Description |
|---|---|---|---|---|
| `0x00` | `CHIP_ID` | Read | `0x03` | Chip identification byte (returns `0x03`) |
| `0x02`–`0x07` | `ACC_X/Y/Z` | Read | — | 14-bit 2's complement acceleration data (`LSB` bit 0 = 1 for NEW data) |
| `0x08` | `TEMP` | Read | — | 8-bit signed temperature reading ($0.5^\circ\text{C}$ / LSB) |
| `0x0D` | `CTRL_REG0` | R/W | `0x00` | Control register 0 (EE_W enable bit 4 unlocks register writes) |
| `0x20` | `CTRL_REG3` | R/W | `0x00` | Full scale range (`range` bits 3–1: `000` = $\pm 1g$, `010` = $\pm 2g$) |

$$ \text{Acceleration } (g) = \frac{\text{Raw 14-bit Signed Value}}{\text{Sensitivity (LSB/g)}} $$

## Wiring

| BMA180 Pin | → | Arduino Uno | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Module includes 3.3V regulator |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |
| `CS`  | | 3.3V / 5V | 3.3V | **Pull High for $I^2C$ mode** |

## Example

```cpp
#include <Wire.h>

#define BMA180_ADDR 0x40

void setup() {
  Serial.begin(9600);
  Wire.begin();

  // Unlock EEPROM write access in CTRL_REG0
  Wire.beginTransmission(BMA180_ADDR);
  Wire.write(0x0D);
  Wire.write(0x10); // EE_W bit set
  Wire.endTransmission();

  // Set Range to +/- 2g in CTRL_REG3
  Wire.beginTransmission(BMA180_ADDR);
  Wire.write(0x20);
  Wire.write(0x04); // range = 2g (bits 3:1 = 010)
  Wire.endTransmission();
}

void loop() {
  Wire.beginTransmission(BMA180_ADDR);
  Wire.write(0x02); // Read ACC_X LSB
  Wire.endTransmission();

  Wire.requestFrom(BMA180_ADDR, 6);
  if (Wire.available() >= 6) {
    int16_t x = (Wire.read() | (Wire.read() << 8)) >> 2;
    int16_t y = (Wire.read() | (Wire.read() << 8)) >> 2;
    int16_t z = (Wire.read() | (Wire.read() << 8)) >> 2;

    float gx = x / 4096.0;
    float gy = y / 4096.0;
    float gz = z / 4096.0;

    Serial.print("X: "); Serial.print(gx); Serial.print(" g\t");
    Serial.print("Y: "); Serial.print(gy); Serial.print(" g\t");
    Serial.print("Z: "); Serial.print(gz); Serial.println(" g");
  }

  delay(200);
}
```

## Common mistakes

- **Forgetting to unlock `EE_W` bit before writing registers:** Writing configuration registers without setting bit 4 of `CTRL_REG0` (`0x0D`) results in register writes being ignored.
- **Not right-shifting 14-bit data by 2 bits:** The 14-bit acceleration data is stored left-justified across 2 bytes. Bits 0–1 of the LSB byte contain status flags, so raw 16-bit readings must be bit-shifted right by 2 (`>> 2`).

## Notes

- **BMA180 vs BMA280:** The BMA180 has been largely superseded in newer designs by the Bosch BMA280 and BMA400 series.
