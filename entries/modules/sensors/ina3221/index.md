## Overview

The **INA3221** is a triple-channel, high-side current and bus voltage monitor IC manufactured by Texas Instruments. Mounted on a purple or black breakout board with 3 sets of screw terminal blocks, it measures current, voltage, and power across **three independent power rails simultaneously** (e.g., monitoring 3.3V, 5V, and 12V rails in a single system).

Equipped with three onboard **$0.1\ \Omega\ (100\ \text{m}\Omega)$ precision shunt resistors**, the INA3221 measures bus voltages from **$0\text{V}$ to $26\text{V}$ DC** and bi-directional current up to **$\pm 3.2\text{ Amperes}$** per channel with 13-bit ADC resolution. It communicates over an $I^2C$ bus (**`0x40`** default, configurable to 4 addresses) and includes hardware alert outputs (`CRITICAL`, `WARNING`).

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 2.7 V to 5.5 V DC (3.3 V or 5.0 V nominal) |
| **Monitored bus voltage (`VBUS`)**| 0 V to 26 V DC (across all 3 channels) |
| **Interface** | $I^2C$ / SMBus (up to 2.4 MHz) |
| **Default $I^2C$ address** | `0x40` (Configurable `0x40` to `0x43` via A0 pin) |
| **Number of channels** | 3 independent high-side measurement channels |
| **Onboard shunt resistors** | $0.1\ \Omega\ (100\ \text{m}\Omega)$ per channel |
| **Max current range** | $\pm 3.2\text{ A}$ per channel ($\pm 163.84\text{ mV}$ shunt voltage) |
| **Shunt ADC resolution** | 13-bit ($40\ \mu\text{V}$ LSB voltage step) |
| **Bus ADC resolution** | 13-bit ($8\text{ mV}$ LSB voltage step) |
| **Hardware Alerts** | `CRITICAL`, `WARNING`, `PV` (Power Valid) open-drain output pins |

## Pinout

Breakout board header & Terminal Blocks:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply power input (+2.7 V to +5.5 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 4 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 5 | `A0`  | Digital Input | $I^2C$ Address Selection pin |
| 6 | `CRI` | Digital Output | Active-Low Critical Over-Current Interrupt |
| 7 | `WAR` | Digital Output | Active-Low Warning Over-Current Interrupt |
| 8 | `PV`  | Digital Output | Power Valid Status Output |
| `CH1`, `CH2`, `CH3` | Screw Terminals | Power Input/Output | High-side current sensing terminals for Rails 1, 2, 3 |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.7 | 3.3 / 5.0 | 5.5 | V | DC |
| Active Supply Current | $I_{CC}$ | — | 350 | 550 | µA | Active 3-channel sampling |
| Power-Down Current | $I_{pd}$ | — | 5.0 | 10.0 | µA | Software shutdown mode |
| Bus Voltage Range | $V_{BUS}$ | 0 | — | 26 | V | Common-mode input range |
| Max Shunt Voltage | $V_{SHUNT}$| -163.84| — | +163.84| mV | Full-scale differential input |
| Shunt Voltage LSB | $LSB_{shunt}$| — | 40 | — | µV | 13-bit ADC step |
| Bus Voltage LSB | $LSB_{bus}$ | — | 8 | — | mV | 13-bit ADC step |

## Math & Current Calculations

With the factory-installed $R_{SHUNT} = 0.1\ \Omega$:

1. **Calculate Channel Current ($I_{CH}$):**

$$ I_{CH}\text{ (A)} = \frac{V_{SHUNT}}{R_{SHUNT}} = \frac{V_{SHUNT}\text{ (mV)}}{100\ \text{m}\Omega} $$

2. **Calculate Channel Power ($P_{CH}$):**

$$ P_{CH}\text{ (W)} = V_{BUS}\text{ (V)} \times I_{CH}\text{ (A)} $$

## Wiring

| INA3221 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |

## Example (Beelan INA3221 Arduino Library)

```cpp
#include <Wire.h>
#include <INA3221.h>

// Set I2C Address 0x40
INA3221 ina3221(INA3221_ADDR40_GND);

void setup() {
  Serial.begin(115200);
  Wire.begin();

  Serial.println("TI INA3221 Triple Power Monitor Test");

  ina3221.begin();
  ina3221.reset();
}

void loop() {
  for (int ch = 1; ch <= 3; ch++) {
    float busVolts = ina3221.getBusVoltage(ch);
    float current_mA = ina3221.getCurrent_mA(ch);

    Serial.print("CH"); Serial.print(ch);
    Serial.print(" Voltage: "); Serial.print(busVolts); Serial.print(" V | ");
    Serial.print("Current: "); Serial.print(current_mA); Serial.println(" mA");
  }

  Serial.println("----------------------------------------");
  delay(2000);
}
```

## Common mistakes

- **Leaving shared ground jumper traces un-isolated:** Some generic purple INA3221 breakout boards ship with the negative terminals of all 3 channels pre-bridged together to system GND on the PCB traces. If monitoring 3 isolated power supplies with different ground references, cut the GND trace jumpers between channels on the back of the PCB.
- **Forgetting address collision with `0x40`:** `0x40` is shared by HDC1080, HTU21D, and INA219. Pull `A0` to $V_{CC}$ to change INA3221 to `0x41`.

## Notes

- **INA3221 vs INA219 vs INA226:** INA3221 monitors 3 channels up to 26V; INA219 monitors 1 channel up to 26V; INA226 monitors 1 channel up to 36V with 16-bit resolution.
