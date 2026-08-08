## Overview

The **HM3301** (Seeed Studio Grove Laser PM2.5 Sensor) is an optical particulate matter (PM) sensor engineered for real-time air quality monitoring. Housed in a compact metallic shielding case with a 4-pin Grove $I^2C$ connector, it integrates a semiconductor laser diode, an internal miniature air fan, light scattering collection optics, and a photo-detector.

Operating on the principle of **light scattering**, the sensor continuously draws ambient air across the laser beam. As airborne particles ($0.3\ \mu\text{m}$ to $10.0\ \mu\text{m}$) pass through the beam, scattered light signals are processed by internal algorithms to compute real-time mass concentrations of **PM1.0, PM2.5, and PM10** (in $\mu\text{g/m}^3$) over an $I^2C$ bus (`0x40`).

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.5 V DC (5.0 V nominal) |
| **Interface** | $I^2C$ (up to 100 kHz) over Grove connector |
| **Fixed $I^2C$ address** | `0x40` |
| **Detectable particle sizes** | $0.3\ \mu\text{m}, 0.5\ \mu\text{m}, 1.0\ \mu\text{m}, 2.5\ \mu\text{m}, 5.0\ \mu\text{m}, 10.0\ \mu\text{m}$ |
| **Concentration range** | $1\ \mu\text{g/m}^3$ to $1000\ \mu\text{g/m}^3$ (PM2.5 / PM10) |
| **Warm-up time** | 30 seconds after power-on |
| **Sample data output** | 29-byte binary telemetry frame (PM1.0, PM2.5, PM10 standard & atmospheric) |
| **Operating current** | $120\text{ mA}$ active (fan running) / $2\text{ mA}$ standby |

## Pinout (Grove 4-Pin Connector Header)

| Pin | Wire Color | Name | Type | Description |
|---|---|---|---|---|
| 1 | Yellow | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 2 | White | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 3 | Red | `VCC` | Power | Supply power (+3.3 V to +5.5 V DC) |
| 4 | Black | `GND` | Power | Ground reference (0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 3.3 | 5.0 | 5.5 | V | DC power input |
| Active Current (Fan On)| $I_{active}$| — | 120 | 150 | mA | Laser diode & fan running |
| Standby Current | $I_{sb}$ | — | 2.0 | — | mA | Low-power sleep mode |
| PM2.5 Mass Accuracy | $Acc_{PM2.5}$| -10% | $\pm 5\%$ | +10% | — | In 0 to 100 µg/m³ range |
| Counting Efficiency | $Eff_{count}$| 50% at $0.3\mu\text{m}$ | 98% at $\ge 0.5\mu\text{m}$ | — | — | Particle count efficiency |
| Data Update Frequency | $f_{update}$| — | 1.0 | — | Hz | 1 frame per second |
| Operating Temperature | $T_{opr}$ | -10 | — | 60 | °C | Non-condensing humidity |

## $I^2C$ Telemetry Frame Structure

When reading 29 bytes from $I^2C$ address `0x40`, the HM3301 returns binary data formatted as 16-bit big-endian integers:

- **Bytes 0–1:** Sensor Sensor Head / Checksum ID.
- **Bytes 6–7:** **PM1.0 Standard concentration ($\mu\text{g/m}^3$).**
- **Bytes 8–9:** **PM2.5 Standard concentration ($\mu\text{g/m}^3$).**
- **Bytes 10–11:** **PM10 Standard concentration ($\mu\text{g/m}^3$).**
- **Bytes 12–13:** **PM1.0 Atmospheric concentration ($\mu\text{g/m}^3$).**
- **Bytes 14–15:** **PM2.5 Atmospheric concentration ($\mu\text{g/m}^3$).**
- **Bytes 16–17:** **PM10 Atmospheric concentration ($\mu\text{g/m}^3$).**
- **Byte 28:** Checksum byte (8-bit sum of bytes 0 through 27).

## Wiring

| HM3301 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| Red (`VCC`) | | 5V / 3.3V | 5V | Powers internal fan & laser |
| Black (`GND`) | | GND | GND | System ground |
| Yellow (`SCL`)| | A5 | GPIO 22 | $I^2C$ Clock |
| White (`SDA`) | | A4 | GPIO 21 | $I^2C$ Data |

## Example (Seeed_PM2_5_sensor_HM3301 Library)

```cpp
#include <Wire.h>
#include <Seeed_HM3301.h>

HM3301 sensor;
uint8_t buf[30];

void setup() {
  Serial.begin(115200);
  Wire.begin();

  Serial.println("HM3301 Laser PM2.5 Sensor Test");

  if (sensor.init()) {
    Serial.println("HM3301 initialization failed! Check I2C wiring.");
    while (1);
  }
}

void loop() {
  if (sensor.read_sensor_value(buf, 29)) {
    Serial.println("Error reading HM3301 data");
  } else {
    // Parse 16-bit big-endian PM values from buffer
    uint16_t pm1_0 = (uint16_t)buf[12] << 8 | buf[13];
    uint16_t pm2_5 = (uint16_t)buf[14] << 8 | buf[15];
    uint16_t pm10  = (uint16_t)buf[16] << 8 | buf[17];

    Serial.print("PM1.0: "); Serial.print(pm1_0); Serial.print(" µg/m³");
    Serial.print(" | PM2.5: "); Serial.print(pm2_5); Serial.print(" µg/m³");
    Serial.print(" | PM10: "); Serial.print(pm10); Serial.println(" µg/m³");
  }

  delay(2000);
}
```

## Common mistakes

- **Blocking airflow intakes:** The metal casing has specific air inlet and outlet vents. Blocking or enclosing the air vents in a sealed box prevents ambient air flow, leading to zero particle readings.
- **Reading before 30-second warm-up:** The internal air fan requires 30 seconds to establish stable laminar airflow over the laser beam.

## Notes

- **HM3301 vs PMS5003 vs SDS011:** HM3301 uses $I^2C$ (0x40) with a Grove connector; PMS5003 and SDS011 use UART serial communication.
