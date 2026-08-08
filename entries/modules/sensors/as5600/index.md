## Overview

The **AS5600** is a 12-bit programmable contactless magnetic rotary position sensor manufactured by ams OSRAM. Placed directly above or below a small **diametrically magnetized disc magnet** attached to a rotating shaft, it measures the absolute angular position over a full **$360^\circ$ rotation** with a resolution of **$0.087^\circ$** (4,096 positions per revolution).

Unlike mechanical potentiometers or optical encoders that suffer from physical wiper wear or dust contamination, the AS5600 operates completely contactless without mechanical friction. It provides three simultaneous output modes: an **$I^2C$ interface (`0x36`)**, a **12-bit PWM output**, and a **ratiometric analog voltage output ($10\%\text{ to }90\%\ V_{DD}$)**. It is widely used in robotic joint encoders, FOC brushless motor closed-loop controllers (SimpleFOC), and custom steering wheels.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VDD`)** | 3.0 V to 3.6 V DC (3.3V mode) or 4.5 V to 5.5 V DC (5.0V mode) |
| **Interface** | $I^2C$ Fast-Mode (up to 1.0 MHz), 12-Bit PWM, or Ratiometric Analog |
| **Fixed $I^2C$ address** | `0x36` |
| **Angle resolution** | 12-bit (4,096 steps per revolution / $0.087^\circ$ per step) |
| **Angular range** | $0^\circ$ to $360^\circ$ (programmable start/end zero angles) |
| **Magnet requirement** | Diametrically magnetized neodymium cylinder (e.g. $6\text{ mm} \times 2.5\text{ mm}$) |
| **Airgap distance** | $0.5\text{ mm}$ to $3.0\text{ mm}$ above IC surface |
| **Operating current** | $6.5\text{ mA}$ active / $1.5\ \mu\text{A}$ low-power mode |

## Pinout (SOIC-8 Package & Breakout Header)

```
             ┌───┴───┐
          VDD ─┤ 1    8├─ VDD5V
          VDD3V3┤ 2   7├─ PGO
          OUT ─┤ 3    6├─ SDA
          GND ─┤ 4    5├─ SCL
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VDD` | Power | Supply input (+3.3V or +5V) |
| 2 | `VDD3V3`| Power | Internal 3.3V LDO output (connect to 3.3V rail or 100nF cap in 5V mode) |
| 3 | `OUT` | Analog / PWM | Ratiometric analog voltage output or 12-bit PWM output |
| 4 | `GND` | Power | Ground reference (0 V) |
| 5 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 6 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 7 | `PGO` | Digital Input | Programming option pin (pull Low for I2C operation) |
| 8 | `DIR` | Digital Input | Direction select pin (GND = Clockwise increase, VDD = Counter-clockwise) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (5V Mode) | $V_{DD5V}$ | 4.5 | 5.0 | 5.5 | V | $VDD3V3$ output connected to 100nF cap |
| Supply Voltage (3.3V Mode)| $V_{DD3V3}$| 3.0 | 3.3 | 3.6 | V | $VDD5V$ tied to $VDD3V3$ |
| Angle Resolution | $Res$ | — | 12 | — | bits | 4,096 counts / revolution |
| Angular Accuracy | $Err_{angle}$| -1.0 | $\pm 0.5$ | +1.0 | deg | Across $360^\circ$ at $25^\circ\text{C}$ |
| Sampling Rate | $f_{sample}$ | — | 55 | — | µs | Output refresh delay |
| Magnet Airgap | $Gap$ | 0.5 | 1.5 | 3.0 | mm | Center alignment tolerance $\pm 0.25\text{ mm}$ |
| PWM Frequency | $f_{PWM}$ | 110 | 115 | 120 | Hz | 12-bit resolution PWM |

## $I^2C$ Angle Registers & Math

- **RAW ANGLE Register (`0x0C`–`0x0D`):** Unfiltered 12-bit angle ($0\dots 4095$).
- **ANGLE Register (`0x0E`–`0x0F`):** Scaled 12-bit angle with zero-point offset ($0\dots 4095$).

$$ \text{Angle (Degrees)} = \left( \frac{\text{12-bit Register Value}}{4096} \right) \times 360.0^\circ $$

$$ \text{Angle (Radians)} = \left( \frac{\text{12-bit Register Value}}{4096} \right) \times 2\pi $$

## Wiring

| AS5600 Breakout Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |
| `DIR` | | GND | GND | Connect to GND for CW angle increase |

## Example (Arduino AS5600 $I^2C$ Reading)

```cpp
#include <Wire.h>

const int AS5600_ADDR = 0x36;
const int RAW_ANGLE_REG = 0x0C;

uint16_t readRawAngle() {
  Wire.beginTransmission(AS5600_ADDR);
  Wire.write(RAW_ANGLE_REG);
  Wire.endTransmission();

  Wire.requestFrom(AS5600_ADDR, 2);
  if (Wire.available() >= 2) {
    uint8_t highByte = Wire.read();
    uint8_t lowByte  = Wire.read();
    return ((uint16_t)highByte << 8) | lowByte;
  }
  return 0;
}

void setup() {
  Serial.begin(115200);
  Wire.begin();
  Serial.println("AS5600 Contactless Magnetic Encoder Online");
}

void loop() {
  uint16_t rawAngle = readRawAngle();
  float degrees = (rawAngle / 4096.0) * 360.0;

  Serial.print("Raw 12-bit Count: "); Serial.print(rawAngle);
  Serial.print(" | Angle: "); Serial.print(degrees, 2); Serial.println("°");

  delay(100);
}
```

## Common mistakes

- **Using axially magnetized magnets:** The AS5600 requires a **diametrically magnetized disc magnet** (north and south poles split across the circular face side-by-side). Using a standard axial magnet (poles top and bottom) will result in static readings.
- **Incorrect power pin wiring (3.3V vs 5V):** For 5V operation, supply 5V to `VDD5V` and place a $100\text{ nF}$ capacitor on `VDD3V3`. For 3.3V operation, short `VDD5V` directly to `VDD3V3`.

## Notes

- **AS5600 vs AS5048A:** AS5600 uses $I^2C$/Analog/PWM ($0.087^\circ$ accuracy); AS5048A uses high-speed SPI ($0.0219^\circ$ 14-bit accuracy).
