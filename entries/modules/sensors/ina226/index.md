## Overview

The **INA226** is a 16-bit high-precision bidirectional current and power monitor IC manufactured by Texas Instruments. Interfacing over $I^2C$ / SMBus, it measures both the differential voltage drop across a shunt resistor and the common-mode bus voltage, internally multiplying them to calculate power in Watts.

Surpassing the popular 12-bit INA219, the INA226 features 16-bit ADC resolution ($2.5\ \mu\text{V}$ shunt LSB, $1.25\text{ mV}$ bus LSB), extremely low offset voltage ($<10\ \mu\text{V}$ max), high-side or low-side sensing up to **36 V**, and a 16-configurable $I^2C$ address matrix. It is widely used in high-accuracy battery fuel gauges, solar charge controllers, and ESPHome power meters.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 2.7 V to 5.5 V DC |
| **Bus voltage range (`VBUS`)** | 0 V to 36 V DC (independent of supply voltage `VCC`) |
| **Shunt full-scale range** | $\pm 81.92\text{ mV}$ differential ($2.5\ \mu\text{V}$ LSB) |
| **Resolution** | 16-bit ADC |
| **Offset voltage** | $10\ \mu\text{V}$ max ($10\times$ lower than INA219) |
| **Gain error** | $0.1\%$ max |
| **Interface** | $I^2C$ (Fast Mode up to 400 kHz, High-Speed up to 3.4 MHz) |
| **Default $I^2C$ address** | `0x40` ($A_0, A_1 \to \text{GND}$) |
| **Operating current** | $330\ \mu\text{A}$ active / $2\ \mu\text{A}$ power-down |

## Pinout

Breakout module header & heavy-current terminal block:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Logic power supply (+2.7 V to +5.5 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 4 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 5 | `ALERT` | Digital Output | Open-drain programmable alert / interrupt pin |
| 6 | `IN+` / `VIN+` | Analog Input | High-side positive shunt voltage measurement pin |
| 7 | `IN-` / `VIN-` | Analog Input | High-side negative shunt voltage measurement pin |
| 8 | `VBUS` | Analog Input | Bus voltage sense input (0 to 36V DC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.7 | 3.3 / 5.0 | 5.5 | V | DC |
| Common-Mode Bus Voltage| $V_{CM}$ | 0 | — | 36.0 | V | High-side or low-side |
| Full-Scale Shunt Voltage| $V_{SENSE}$| -81.92 | — | +81.92 | mV | Bidirectional |
| Shunt LSB Size | $LSB_{shunt}$| — | 2.5 | — | µV | 16-bit signed |
| Bus LSB Size | $LSB_{bus}$ | — | 1.25 | — | mV | 16-bit unsigned |
| Bus Voltage Max Error | $E_{bus}$ | -0.1% | $\pm 0.02\%$| +0.1%| — | Over temperature |
| Conversion Time | $t_{conv}$ | 140 | 1100 | 8244 | µs | Configurable per sample |

## Internal Math & Register Calculations

1. **Current Calibration Register (`0x05`):**

$$ \text{Current\_LSB} = \frac{\text{Maximum Expected Current}}{2^{15}} = \frac{I_{max}}{32768} $$

$$ \text{CAL} = \text{trunc}\left( \frac{0.00512}{\text{Current\_LSB} \times R_{shunt}} \right) $$

2. **Current Register (`0x04`):**

$$ \text{Current (A)} = \text{Raw Current Register Code} \times \text{Current\_LSB} $$

3. **Power Register (`0x03`):**

$$ \text{Power (W)} = 25 \times \text{Raw Power Register Code} \times \text{Current\_LSB} $$

## Wiring (High-Side Sensing Configuration)

| INA226 Pin | → | Power Circuit / MCU | Notes |
|---|---|---|---|
| `VIN+` | | Connected to Positive Power Supply (+) | Up to +36V DC |
| `VIN-` | | Connected to Load positive side | After $0.1\ \Omega$ or $0.01\ \Omega$ shunt |
| `VBUS` | | Connected to `VIN+` or `VIN-` | Bus voltage monitoring rail |
| `VCC`  | | MCU 3.3V / 5V Rail | Logic power |
| `GND`  | | MCU GND & Load Ground | Common ground |
| `SCL`  | | MCU SCL Pin | $I^2C$ Clock |
| `SDA`  | | MCU SDA Pin | $I^2C$ Data |

## Example (Arduino / ESP32 INA226 Library)

```cpp
#include <Wire.h>
#include <INA226_WE.h>

#define I2C_ADDRESS 0x40

INA226_WE ina226 = INA226_WE(I2C_ADDRESS);

void setup() {
  Serial.begin(115200);
  Wire.begin();

  if(!ina226.init()){
    Serial.println("Failed to find INA226 chip!");
    while(1);
  }

  // Set shunt resistor value (0.1 ohm) and max expected current (0.8A)
  ina226.setResistorRange(0.1, 0.8);
  ina226.setAverage(INA226_AVERAGES_16); // 16-sample averaging
  
  Serial.println("INA226 initialized successfully.");
}

void loop() {
  float shuntVoltage_mV = ina226.getShuntVoltage_mV();
  float busVoltage_V = ina226.getBusVoltage_V();
  float current_mA = ina226.getCurrent_mA();
  float power_mW = ina226.getBusPower();

  Serial.print("Bus Voltage: "); Serial.print(busVoltage_V); Serial.print(" V\t");
  Serial.print("Current: "); Serial.print(current_mA); Serial.print(" mA\t");
  Serial.print("Power: "); Serial.print(power_mW); Serial.println(" mW");

  delay(500);
}
```

## Common mistakes

- **Exceeding the $\pm 81.92\text{ mV}$ shunt voltage limit:** With a standard $0.1\ \Omega$ onboard shunt resistor, maximum measurable current is $0.8192\text{ A}$. For currents up to $10\text{ A}$ or $20\text{ A}$, replace the shunt resistor with $0.005\ \Omega$ or $0.002\ \Omega$.
- **Forgetting to write the Calibration Register (`0x05`):** Unlike voltage readings, reading the Current and Power registers returns zero until a valid `CAL` value is written to register `0x05`.

## Notes

- **INA226 vs INA219:** INA226 has 16-bit resolution ($10\ \mu\text{V}$ offset) vs INA219's 12-bit resolution ($100\ \mu\text{V}$ offset); INA226 supports 36V bus voltage vs INA219's 26V.
