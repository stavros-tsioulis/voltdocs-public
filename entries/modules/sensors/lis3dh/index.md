## Overview

The **LIS3DH** is an ultra-low-power 3-axis high-performance linear accelerometer belonging to the "nano" family of STMicroelectronics MEMS sensors. Housed in a compact $3 \times 3 \times 1\text{ mm}$ 16-pin LGA package, it integrates a 3-axis capacitive sensing element along with an IC interface outputting 16-bit digital acceleration data over $I^2C$ or SPI.

Consuming as little as $2\ \mu\text{A}$ in low-power operating mode (and $11\ \mu\text{A}$ in normal mode), the LIS3DH features programmable full scales ($\pm 2g$, $\pm 4g$, $\pm 8g$, $\pm 16g$), a 32-level FIFO buffer, two independent programmable interrupt pins, an integrated temperature sensor, and dedicated hardware logic for single/double-click (tap) detection and free-fall sensing. It is widely used in battery-powered wearables, asset trackers, tilt sensors, and tap-to-wake UI devices.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.0 V DC (breakout with onboard LDO) |
| **IC supply voltage (`VDD`)** | 1.71 V to 3.6 V DC |
| **Interface** | $I^2C$ (up to 400 kHz) & 3-Wire / 4-Wire SPI (up to 10 MHz) |
| **Default $I^2C$ address** | `0x18` (`SDO`/`ALT` pin Low / un-connected) |
| **Alternate $I^2C$ address** | `0x19` (`SDO`/`ALT` pin High to 3.3V) |
| **Full-scale acceleration range** | $\pm 2g, \pm 4g, \pm 8g, \pm 16g$ |
| **Output resolution** | 10-bit (Normal), 12-bit (High Res), 8-bit (Low Power) |
| **Active current draw** | $11\ \mu\text{A}$ (Normal Mode at 50 Hz) / $0.5\ \mu\text{A}$ power-down |

## Pinout

Breakout modules feature an 8-pin 0.1" (2.54 mm) header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SCL` / `SPC` | Digital Input | $I^2C$ Clock / SPI Clock |
| 4 | `SDA` / `SDI` | Digital Input / Output | $I^2C$ Data / SPI Serial Data Input |
| 5 | `SDO` / `ALT` | Digital Output | SPI Serial Data Out / $I^2C$ Address Bit 0 (Low = `0x18`, High = `0x19`) |
| 6 | `CS` | Digital Input | SPI Chip Select (High = $I^2C$ mode, Low = SPI mode) |
| 7 | `INT1` | Digital Output | Programmable Interrupt Line 1 (free-fall / motion trigger) |
| 8 | `INT2` | Digital Output | Programmable Interrupt Line 2 (click / double-click trigger) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{CC}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with LDO |
| Normal Mode Current | $I_{norm}$ | — | 11 | 20 | µA | $f_{ODR} = 50\text{ Hz}$, $V_{DD} = 2.5\text{V}$ |
| Low Power Current | $I_{low}$ | — | 2 | 4 | µA | $f_{ODR} = 1\text{ Hz}$, low-power mode |
| Power-Down Current | $I_{pd}$ | — | 0.5 | 1.0 | µA | Shut down state |
| Sensitivity ($\pm 2g$) | $S_{2g}$ | — | 1 | — | mg/digit | 16-bit left-justified |
| Sensitivity ($\pm 16g$) | $S_{16g}$ | — | 12 | — | mg/digit | 16-bit left-justified |
| Output Data Rate | $f_{ODR}$ | 1 | 100 | 5376 | Hz | Configurable via `CTRL_REG1` |

## Register map

| Address | Register | Access | Reset | Description |
|---|---|---|---|---|
| `0x0F` | `WHO_AM_I` | Read | `0x33` | Device identification register (always returns `0x33`) |
| `0x20` | `CTRL_REG1` | R/W | `0x07` | Data rate ($ODR$), Low-power mode enable, X/Y/Z enable |
| `0x23` | `CTRL_REG4` | R/W | `0x00` | Full-scale selection ($\pm 2g / \pm 4g / \pm 8g / \pm 16g$), High resolution |
| `0x28`–`0x29` | `OUT_X_L` / `H` | Read | — | X-axis acceleration output bytes |
| `0x2A`–`0x2B` | `OUT_Y_L` / `H` | Read | — | Y-axis acceleration output bytes |
| `0x2C`–`0x2D` | `OUT_Z_L` / `H` | Read | — | Z-axis acceleration output bytes |
| `0x38` | `CLICK_CFG` | R/W | `0x00` | Single-tap / double-tap interrupt configuration |

## Wiring

| LIS3DH Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Module includes 3.3V LDO |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |
| `CS`  | | 3.3V / 5V | 3.3V | **Pull High for $I^2C$ mode** |
| `SDO` | | GND | GND | Connect to GND for `0x18`, VCC for `0x19` |

## Example

```cpp
#include <Wire.h>
#include <Adafruit_LIS3DH.h>
#include <Adafruit_Sensor.h>

Adafruit_LIS3DH lis = Adafruit_LIS3DH();

void setup() {
  Serial.begin(115200);
  Serial.println("LIS3DH Test!");

  // Initialize I2C with default address 0x18
  if (!lis.begin(0x18)) {
    Serial.println("Could not find LIS3DH! Check CS and SDO pins.");
    while (1);
  }
  Serial.println("LIS3DH found!");

  lis.setRange(LIS3DH_RANGE_4_G);   // 2, 4, 8 or 16 G
  Serial.print("Range set to: 4G");
}

void loop() {
  sensors_event_t event;
  lis.getEvent(&event);

  Serial.print("X: "); Serial.print(event.acceleration.x); Serial.print(" m/s^2 ");
  Serial.print("Y: "); Serial.print(event.acceleration.y); Serial.print(" m/s^2 ");
  Serial.print("Z: "); Serial.print(event.acceleration.z); Serial.println(" m/s^2");

  delay(200);
}
```

## Common mistakes

- **Leaving `CS` floating on $I^2C$ setups:** If `CS` is left unconnected, the LIS3DH defaults to SPI mode or toggles protocol modes randomly. **Always pull `CS` High to $V_{CC}$ for $I^2C$ mode.**
- **Assuming 16-bit raw values are right-justified:** Raw acceleration output registers (`OUT_X_L` / `OUT_X_H`) are **left-justified**. Shift raw 16-bit values right by 4 bits in Normal (12-bit) mode or 6 bits in Low-Power (10-bit) mode.
- **Wrong address jumper:** Pulling `SDO` High changes the $I^2C$ address from `0x18` to `0x19`.

## Notes

- **LIS3DH vs ADXL345:** The LIS3DH operates down to 1.71V supply and consumes significantly lower active current ($11\ \mu\text{A}$ vs $145\ \mu\text{A}$) than the ADXL345, making it ideal for coin-cell battery operation.
