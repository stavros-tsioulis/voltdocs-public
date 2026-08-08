## Overview

The **L3GD20H** is a 3-axis digital angular rate sensor (gyroscope) manufactured by STMicroelectronics. It measures rotational angular velocity around the X, Y, and Z axes with user-selectable full-scale ranges of $\pm 245\text{ dps}$, $\pm 500\text{ dps}$, and $\pm 2000\text{ dps}$ (degrees per second).

Housed in a compact 16-pin $3 \times 3\text{ mm}$ LGA package, the L3GD20H incorporates an internal 16-bit ADC, configurable low-pass and high-pass digital filters, a 32-level FIFO buffer, an embedded temperature sensor, and dual programmable interrupt generators. It is used in dead-reckoning navigation, optical image stabilization, RC quadcopter flight stabilization, and gaming motion controllers.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.0 V DC (breakout with onboard regulator) |
| **IC supply voltage (`VDD`)** | 2.2 V to 3.6 V DC (3.0 V nominal) |
| **Interface** | $I^2C$ (up to 400 kHz) & 3-Wire / 4-Wire SPI (up to 10 MHz) |
| **Default $I^2C$ address** | `0x6B` (`SDO`/`SA0` pin High to 3.3V) |
| **Alternate $I^2C$ address** | `0x6A` (`SDO`/`SA0` pin Low to GND) |
| **Full-scale angular rate** | $\pm 245\text{ dps}, \pm 500\text{ dps}, \pm 2000\text{ dps}$ |
| **Output resolution** | 16-bit 2's complement ($I^2C$/SPI) |
| **Active current draw** | 6.0 mA active / $5.0\ \mu\text{A}$ power-down |

## Pinout

Breakout modules expose an 8-pin or 9-pin 0.1" (2.54 mm) header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SCL` / `SPC` | Digital Input | $I^2C$ Clock / SPI Clock |
| 4 | `SDA` / `SDI` | Digital Input / Output | $I^2C$ Data / SPI Serial Data Input |
| 5 | `SDO` / `SA0` | Digital Output | SPI Data Out / $I^2C$ Address Bit 0 (High = `0x6B`, Low = `0x6A`) |
| 6 | `CS` | Digital Input | SPI Chip Select (High = $I^2C$ mode, Low = SPI mode) |
| 7 | `INT1` | Digital Output | Programmable Interrupt Line 1 (data ready / threshold trigger) |
| 8 | `INT2` / `DRDY` | Digital Output | Interrupt Line 2 / Data Ready signal |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{CC}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with LDO |
| Active Supply Current | $I_{CC}$ | — | 6.0 | 8.0 | mA | Normal operating state |
| Power-Down Current | $I_{pd}$ | — | 5.0 | 10.0 | µA | Software power-down |
| Sensitivity ($\pm 245\text{ dps}$)| $So_{245}$ | 7.6 | 8.75 | 9.8 | mdps/digit | 16-bit output |
| Sensitivity ($\pm 500\text{ dps}$)| $So_{500}$ | 15.3 | 17.50 | 19.7 | mdps/digit | 16-bit output |
| Sensitivity ($\pm 2000\text{ dps}$)| $So_{2000}$ | 61.25 | 70.00 | 78.75 | mdps/digit | 16-bit output |
| Output Data Rate | $f_{ODR}$ | 12.5 | 100 | 800 | Hz | Configurable via `CTRL1` |

## Register map

| Address | Register | Access | Reset | Description |
|---|---|---|---|---|
| `0x0F` | `WHO_AM_I` | Read | `0xD7` | Device identification register (always returns `0xD7` for L3GD20H) |
| `0x20` | `CTRL1` | R/W | `0x07` | Data rate ($ODR$), bandwidth cutoff, power mode, X/Y/Z enable |
| `0x23` | `CTRL4` | R/W | `0x00` | Full-scale selection ($\pm 245 / \pm 500 / \pm 2000\text{ dps}$), SPI mode |
| `0x26` | `OUT_TEMP` | Read | — | Internal temperature sensor output byte |
| `0x28`–`0x29` | `OUT_X_L` / `H` | Read | — | X-axis angular rate output bytes |
| `0x2A`–`0x2B` | `OUT_Y_L` / `H` | Read | — | Y-axis angular rate output bytes |
| `0x2C`–`0x2D` | `OUT_Z_L` / `H` | Read | — | Z-axis angular rate output bytes |

## Wiring

| L3GD20H Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Module includes 3.3V regulator |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |
| `CS`  | | 3.3V / 5V | 3.3V | **Pull High for $I^2C$ mode** |
| `SDO` | | 3.3V / 5V | 3.3V | Connect to VCC for `0x6B`, GND for `0x6A` |

## Example

```cpp
#include <Wire.h>
#include <Adafruit_L3GD20_U.h>

Adafruit_L3GD20_Unified gyro = Adafruit_L3GD20_Unified(20);

void setup() {
  Serial.begin(115200);
  Serial.println("L3GD20H Gyroscope Test");

  /* Enable auto-ranging */
  gyro.enableAutoRange(true);

  /* Initialize the sensor */
  if (!gyro.begin()) {
    Serial.println("Could not find L3GD20H! Check wiring.");
    while (1);
  }
  Serial.println("L3GD20H initialized.");
}

void loop() {
  sensors_event_t event;
  gyro.getEvent(&event);

  Serial.print("X: "); Serial.print(event.gyro.x); Serial.print(" rad/s  ");
  Serial.print("Y: "); Serial.print(event.gyro.y); Serial.print(" rad/s  ");
  Serial.print("Z: "); Serial.print(event.gyro.z); Serial.println(" rad/s");

  delay(200);
}
```

## Common mistakes

- **Leaving `CS` floating on $I^2C$ setups:** As with ST accelerometers, leaving `CS` disconnected allows noise to switch the IC into SPI mode. **Tie `CS` High to $V_{CC}$ for $I^2C$ mode.**
- **Assuming zero-rate output is 0 dps:** All mechanical MEMS gyroscopes exhibit static zero-rate offset drift. Application code must perform a 500-sample calibration at startup while stationary to subtract DC bias offsets from X, Y, and Z axes.
- **`WHO_AM_I` register mismatch:** Older L3GD20 chips return `0xD4`, whereas newer L3GD20H chips return `0xD7`. Ensure your library supports `0xD7`.

## Notes

- **L3GD20 vs L3GD20H:** The L3GD20H reduces power consumption, adds a 32-level FIFO buffer, improves zero-rate offset stability, and changes full-scale range from $\pm 250\text{ dps}$ to $\pm 245\text{ dps}$.
