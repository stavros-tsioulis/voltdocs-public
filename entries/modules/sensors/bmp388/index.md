## Overview

The **BMP388** is a 24-bit high-precision digital barometric pressure and temperature sensor manufactured by Bosch Sensortec. Built as the high-performance successor to the BMP280, it features an ultra-small $2.0 \times 2.0\text{ mm}$ 10-pin LGA package, a 512-byte FIFO buffer, and an advanced MEMS piezo-resistive pressure sensing element.

Offering exceptional relative altitude accuracy of **$\pm 0.5\text{ meters}$** ($\pm 8\text{ Pa}$) and pressure noise down to $0.08\text{ Pa}$ RMS, the BMP388 is the preferred altimeter sensor for drone flight controllers (altitude-hold mode), indoor floor-level navigation, vertical velocity estimation, and precision weather stations.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.0 V DC (breakout with 3.3V LDO) |
| **IC supply voltage (`VDD`)** | 1.65 V to 3.6 V DC (1.8 V or 3.3 V nominal) |
| **Interface** | $I^2C$ (up to 3.4 MHz) & 3-Wire / 4-Wire SPI (up to 10 MHz) |
| **Default $I^2C$ address** | `0x77` (`SDO` pin High to 3.3V) |
| **Alternate $I^2C$ address** | `0x76` (`SDO` pin Low to GND) |
| **Pressure range** | 300 hPa to 1250 hPa ($30\text{ kPa to }125\text{ kPa}$) |
| **Pressure RMS noise** | $0.08\text{ Pa}$ (with ultra-high resolution & IIR filtering) |
| **Relative altitude accuracy** | $\pm 0.5\text{ m}$ (equivalent to $\pm 8\text{ Pa}$) |
| **Active supply current** | $3.4\ \mu\text{A}$ at 1 Hz sampling / $2\ \mu\text{A}$ standby |

## Pinout

Breakout modules expose a 6-pin 0.1" (2.54 mm) header or Qwiic / STEMMA QT connector:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SCL` / `SCK` | Digital Input | $I^2C$ Serial Clock / SPI Clock |
| 4 | `SDA` / `SDI` | Digital Input / Output | $I^2C$ Serial Data / SPI Serial Data Input |
| 5 | `SDO` / `ADR` | Digital Output | SPI Data Out / $I^2C$ Address Select (Low = `0x76`, High = `0x77`) |
| 6 | `CS` | Digital Input | SPI Chip Select (High = $I^2C$ mode, Low = SPI mode) |
| 7 | `INT` | Digital Output | Programmable interrupt output line (FIFO watermark / data ready) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{CC}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with LDO |
| Active Supply Current | $I_{CC}$ | — | 3.4 | 700 | µA | 1 Hz forced mode vs max oversampling |
| Deep Sleep Current | $I_{sleep}$ | — | 2.0 | 5.0 | µA | Sleep mode |
| Pressure Measurement Range| $P_{range}$ | 300 | — | 1250 | hPa | $9000\text{m}$ below to $9000\text{m}$ above sea level |
| Absolute Pressure Accuracy| $P_{abs\_acc}$| -50 | $\pm 50$ | +50 | Pa | $300\dots 1100\text{ hPa}, 0\dots 65^\circ\text{C}$ |
| Relative Pressure Accuracy| $P_{rel\_acc}$| -8 | $\pm 8$ | +8 | Pa | $25^\circ\text{C}, 700\dots 1100\text{ hPa}$ ($\pm 0.5\text{m}$) |
| Temp Accuracy (BMP388) | $T_{acc}$ | -0.5 | $\pm 0.5$ | +0.5 | °C | $0^\circ\text{C} \le T \le 65^\circ\text{C}$ |
| Max Output Data Rate | $f_{ODR}$ | 0.001 | — | 200 | Hz | Configurable sampling rate |

## Hypsometric Barometric Altitude Formula

To compute altitude $h$ (in meters) from measured barometric pressure $P$ (in hPa):

$$ h = \frac{T_0}{L} \times \left[ 1 - \left( \frac{P}{P_0} \right)^{\frac{R \cdot L}{g \cdot M}} \right] \approx 44330 \times \left[ 1 - \left( \frac{P}{1013.25} \right)^{0.1903} \right] $$

- $P$: Measured pressure in hPa.
- $P_0$: Sea level reference pressure ($1013.25\text{ hPa}$ nominal, or current local airport QNH setting).

## Wiring

| BMP388 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Module includes 3.3V LDO |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |
| `CS`  | | 3.3V / 5V | 3.3V | **Pull High for $I^2C$ mode** |

## Example

```cpp
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_BMP388.h>

#define SEALEVELPRESSURE_HPA (1013.25)

Adafruit_BMP388 bmp;

void setup() {
  Serial.begin(115200);
  while (!Serial) delay(10);

  Serial.println("BMP388 test");

  if (!bmp.begin_I2C(0x77)) { // Default address 0x77
    Serial.println("Could not find BMP388 sensor! Check CS and SDO pins.");
    while (1);
  }

  // Set up oversampling and filter initialization
  bmp.setTemperatureOversampling(BMP3_OVERSAMPLING_8X);
  bmp.setPressureOversampling(BMP3_OVERSAMPLING_32X);
  bmp.setIIRFilterCoeff(BMP3_IIR_FILTER_COEFF_3);
  bmp.setOutputDataRate(BMP3_ODR_50_HZ);
}

void loop() {
  if (!bmp.performReading()) {
    Serial.println("Failed to perform reading");
    return;
  }

  Serial.print("Temperature = "); Serial.print(bmp.temperature); Serial.println(" *C");
  Serial.print("Pressure = "); Serial.print(bmp.pressure / 100.0); Serial.println(" hPa");
  Serial.print("Approx Altitude = "); Serial.print(bmp.readAltitude(SEALEVELPRESSURE_HPA)); Serial.println(" m");

  delay(200);
}
```

## Common mistakes

- **Leaving `CS` floating in $I^2C$ mode:** If `CS` is unconnected, electrical noise drops the IC into SPI mode. **Tie `CS` High to 3.3V for $I^2C$ mode.**
- **Exposing sensor aperture to direct sunlight or air drafts:** Air currents from drone propellers or ambient sunlight thermal radiation cause pressure fluctuation errors up to $\pm 20\text{ Pa}$ ($\pm 1.5\text{ m}$). Cover the sensor with open-cell dark foam in drone builds.

## Notes

- **BMP280 vs BMP388:** The BMP388 improves relative altitude precision from $\pm 1.0\text{ m}$ down to $\pm 0.5\text{ m}$ and lowers pressure noise significantly.
