## Overview

The **INA260** is a 16-bit precision digital current, voltage, and power monitor manufactured by Texas Instruments. Unlike traditional power monitor ICs (such as the INA219 or INA226) that require external discrete sense resistors, the INA260 features a **factory-calibrated, integrated $2\ \text{m}\Omega$ precision shunt resistor** directly inside its 16-pin TSSOP package.

Capable of measuring continuous bidirectional currents up to **$\pm 15\text{ A}$** (and peak currents up to $\pm 36\text{ A}$) across bus voltages from **0 V to 36 V**, the INA260 eliminates trace resistance errors, component selection math, and thermal calibration drift. It is widely used in Adafruit STEMMA QT modules, robot motor power tracking, and USB-C power delivery monitoring.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 2.7 V to 5.5 V DC |
| **Bus voltage range (`VBUS`)** | 0 V to 36 V DC |
| **Continuous current rating** | $\pm 15\text{ A}$ continuous ($\pm 36\text{ A}$ peak) |
| **Integrated shunt resistance** | $2.0\ \text{m}\Omega \pm 0.1\%$ |
| **Resolution & LSB** | 16-bit ADC ($1.25\text{ mA/LSB}$ Current, $1.25\text{ mV/LSB}$ Voltage, $10\text{ mW/LSB}$ Power) |
| **Interface** | $I^2C$ (Fast Mode up to 400 kHz, High-Speed up to 3.4 MHz) |
| **Default $I^2C$ address** | `0x40` ($A_0, A_1 \to \text{GND}$) |
| **Operating current** | $310\ \mu\text{A}$ active / $2\ \mu\text{A}$ power-down |

## Pinout & High-Current Terminal Block

Breakout board screw terminal & 6-pin logic header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Logic power supply (+2.7 V to +5.5 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 4 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 5 | `ALERT` | Digital Output | Programmable alert / over-current interrupt output |
| 6 | `VBUS` | Analog Input | Bus voltage sense pin (0 to 36V DC) |
| Screw 1 | `IN+` / `V+` | Heavy Current Input | Positive current input terminal (connect to supply +) |
| Screw 2 | `IN-` / `V-` | Heavy Current Output| Negative current output terminal (connect to load +) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.7 | 3.3 / 5.0 | 5.5 | V | DC |
| Bus Voltage Range | $V_{BUS}$ | 0 | — | 36.0 | V | Independent of $V_{CC}$ |
| Continuous Current | $I_{CONT}$ | -15.0 | — | +15.0 | A | $T_A \le 85^\circ\text{C}$ continuous |
| Peak Current | $I_{PEAK}$ | -36.0 | — | +36.0 | A | $t_{pulse} < 1\text{ sec}$ |
| Shunt Resistance | $R_{shunt}$| 1.998 | 2.0 | 2.002 | mΩ | Internal silicon shunt |
| Shunt Thermal Drift | $TC_{shunt}$| — | 10 | — | ppm/°C | Low thermal drift |
| Bus Voltage Accuracy | $E_{bus}$ | -0.1% | $\pm 0.05\%$| +0.1%| — | Full scale |
| Current Accuracy | $E_{curr}$ | -0.5% | $\pm 0.15\%$| +0.5%| — | Full scale |

## Direct Reading Fixed Scales (No Math Required!)

Because the $2\ \text{m}\Omega$ internal shunt is factory-calibrated inside the IC, no custom calibration registers need to be calculated:

- **Current Register (`0x01`):** $1.25\text{ mA}$ per LSB.

$$ \text{Current (A)} = \text{Raw Current Code} \times 0.00125 $$

- **Bus Voltage Register (`0x02`):** $1.25\text{ mV}$ per LSB.

$$ \text{Bus Voltage (V)} = \text{Raw Bus Voltage Code} \times 0.00125 $$

- **Power Register (`0x03`):** $10\text{ mW}$ per LSB.

$$ \text{Power (W)} = \text{Raw Power Code} \times 0.010 $$

## Wiring

| INA260 Pin | → | Arduino / MCU | Load / Power Circuit | Notes |
|---|---|---|---|---|
| Screw Terminal `V+` | | — | Power Supply Positive (+) | High-current path |
| Screw Terminal `V-` | | — | Load Positive Input (+) | High-current path |
| `VCC` | | 3.3V / 5V | — | Logic supply |
| `GND` | | GND | Power Supply Ground (-) | Shared common ground |
| `SCL` | | A5 / GPIO 22 | — | $I^2C$ Clock |
| `SDA` | | A4 / GPIO 21 | — | $I^2C$ Data |

## Example (Adafruit_INA260 Library)

```cpp
#include <Wire.h>
#include <Adafruit_INA260.h>

Adafruit_INA260 ina260 = Adafruit_INA260();

void setup() {
  Serial.begin(115200);
  while (!Serial) delay(10);

  Serial.println("Adafruit INA260 Test");

  if (!ina260.begin()) {
    Serial.println("Couldn't find INA260 chip! Check wiring.");
    while (1);
  }
  Serial.println("Found INA260 chip");
}

void loop() {
  Serial.print("Current: "); Serial.print(ina260.readCurrent()); Serial.println(" mA");
  Serial.print("Bus Voltage: "); Serial.print(ina260.readBusVoltage()); Serial.println(" mV");
  Serial.print("Power: "); Serial.print(ina260.readPower()); Serial.println(" mW");
  Serial.println();

  delay(1000);
}
```

## Common mistakes

- **Attempting to measure $>15\text{ A}$ continuous without heatsinking:** Continuous currents above $15\text{ A}$ generate significant thermal dissipation ($P = I^2 R = 15^2 \times 0.002 = 0.45\text{ W}$) inside the 16-pin TSSOP package. Ensure heavy copper PCB trace pours or external heatsinking for high-current loads.
- **Floating `VBUS` pin:** If `VBUS` is left unconnected, voltage and power registers read 0. Connect `VBUS` to `V+` to monitor bus voltage.

## Notes

- **INA260 vs INA226:** INA260 includes an integrated $2\ \text{m}\Omega$ $15\text{ A}$ shunt; INA226 requires an external discrete shunt resistor.
