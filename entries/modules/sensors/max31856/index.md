## Overview

The **MAX31856** is an advanced 19-bit cold-junction compensated thermocouple-to-digital converter IC manufactured by Maxim Integrated (Analog Devices). Designed for high-accuracy temperature sensing in industrial furnaces, kilns, 3D printers, and environmental test chambers, it natively supports eight standard thermocouple types (**K, J, N, R, S, T, E, and B**).

Unlike older fixed K-type converters (such as MAX6675 or MAX31855), the MAX31856 features **on-chip linearizing lookup tables** for non-linear thermocouples, high-precision $19\text{-bit}$ resolution ($0.0078125^\circ\text{C}$ per LSB), programmable $50\text{ Hz} / 60\text{ Hz}$ AC mains filter rejection, and a bi-directional **SPI interface (up to 5 MHz)**.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VIN`)** | 3.3 V to 5.0 V DC (breakout includes 3.3V LDO regulator) |
| **IC supply voltage (`VDD`)** | 3.0 V to 3.6 V DC (3.3 V nominal) |
| **Interface** | SPI Mode 1 or Mode 3 (up to 5 MHz) |
| **Supported Thermocouples** | K, J, N, R, S, T, E, B (configured via Register `0x01`) |
| **Probe Temperature Range**| $-210^\circ\text{C}\text{ to }+1800^\circ\text{C}$ (dependent on thermocouple type) |
| **ADC Resolution** | 19-bit ($0.0078125^\circ\text{C}$ per LSB) |
| **Cold-Junction Accuracy** | $\pm 0.7^\circ\text{C}$ over $-40^\circ\text{C} \dots +125^\circ\text{C}$ |
| **Line Noise Rejection** | 50 Hz & 60 Hz programmable notch filter rejection |
| **Fault Detection** | Open circuit, over/under temperature limits, short to GND/$V_{CC}$ |

## Pinout (TSSOP-14 Package & Breakout Header)

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VIN` | Power | Supply power input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `SDO` / `MISO`| Digital Output | SPI Master Input Slave Output |
| 4 | `SDI` / `MOSI`| Digital Input | SPI Master Output Slave Input |
| 5 | `CS` | Digital Input | Active-Low SPI Chip Select |
| 6 | `SCK` | Digital Input | SPI Serial Clock |
| 7 | `FLT` / `DRDY`| Digital Output | Active-Low Fault or Data Ready interrupt pin |
| `+` / `-` | Screw Terminals | Analog Input | Thermocouple lead wire input terminals |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{VIN}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with LDO |
| Active Supply Current | $I_{CC}$ | — | 1.2 | 2.0 | mA | Continuous conversion mode |
| Cold-Junction Accuracy | $T_{CJ\_acc}$| -0.7 | $\pm 0.7$ | +0.7 | °C | $-40^\circ\text{C} \dots +125^\circ\text{C}$ |
| Thermocouple ADC Bits | $Res_{ADC}$| — | 19 | — | bits | Signed 19-bit output |
| LSB Temperature Step | $LSB_{temp}$| — | 0.0078125| — | °C | $1/128^\circ\text{C}$ |
| Conversion Time (60Hz)| $t_{conv}$ | 143 | 170 | 185 | ms | 60Hz filter mode |

## Register Configuration & Thermocouple Selection

- **CR0 Register (`0x00`):** Automatic Conversion mode (`0x80`), 50/60 Hz noise filter (`0x01`).
- **CR1 Register (`0x01`):** Thermocouple Type Selection:
  - `0x00` = B Type
  - `0x01` = E Type
  - `0x02` = J Type
  - `0x03` = K Type (Default)
  - `0x04` = N Type
  - `0x05` = R Type
  - `0x06` = S Type
  - `0x07` = T Type

## Wiring

| MAX31856 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VIN` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `CS`  | | Digital D10 | GPIO 5 | SPI Chip Select |
| `SDI` (MOSI) | | Digital D11 | GPIO 23 | SPI MOSI |
| `SDO` (MISO) | | Digital D12 | GPIO 19 | SPI MISO |
| `SCK` (CLK)  | | Digital D13 | GPIO 18 | SPI Clock |

## Example (Adafruit_MAX31856 Library)

```cpp
#include <Adafruit_MAX31856.h>

// Use hardware SPI with CS on pin 10
Adafruit_MAX31856 maxthermo = Adafruit_MAX31856(10);

void setup() {
  Serial.begin(115200);
  Serial.println("Adafruit MAX31856 Thermocouple Test");

  if (!maxthermo.begin()) {
    Serial.println("Could not initialize MAX31856 sensor! Check SPI wiring.");
    while (1);
  }

  // Set thermocouple type to K-Type (options: MAX31856_TCTYPE_K, J, N, R, S, T, E, B)
  maxthermo.setThermocoupleType(MAX31856_TCTYPE_K);
  Serial.println("MAX31856 Initialized for K-Type Thermocouple.");
}

void loop() {
  float temp = maxthermo.readThermocoupleTemperature();

  uint8_t fault = maxthermo.readFault();
  if (fault) {
    if (fault & MAX31856_FAULT_OPEN) Serial.println("Fault: Thermocouple Open!");
    if (fault & MAX31856_FAULT_OVUV) Serial.println("Fault: Over/Under Voltage!");
  } else {
    Serial.print("Probe Temp: "); Serial.print(temp); Serial.println(" °C");
  }

  delay(1000);
}
```

## Common mistakes

- **Leaving `SDI` (MOSI) disconnected:** Unlike the read-only MAX31855, the MAX31856 requires a bi-directional SPI interface to receive configuration register settings (such as thermocouple type selection and 50Hz/60Hz noise filtering).
- **Mismatched thermocouple type selection in software:** Setting `MAX31856_TCTYPE_K` when using a J-type probe introduces non-linear temperature errors exceeding $\pm 20^\circ\text{C}$.

## Notes

- **MAX31856 vs MAX31855:** MAX31856 supports 8 thermocouple types with bi-directional SPI control and $0.0078^\circ\text{C}$ resolution; MAX31855 supports 1 thermocouple type (K-Type) read-only.
