## Overview

The **INA219** is a high-side, bidirectional current and power monitoring IC with an I2C interface manufactured by Texas Instruments. It monitors both shunt voltage drop across an onboard precision current sense resistor ($0.1\text{ }\Omega$) and bus supply voltage up to **26 V DC**.

It includes a 12-bit ADC, a programmable multiplier for onboard current (in Amperes) and power (in Watts) calculations, and programmable averaging filtering. It is standard in solar monitoring, battery fuel-gauge systems, and power-metering projects.

## Quick reference

| | |
|---|---|
| **Logic supply (`VCC`)** | 3.0 V to 5.5 V DC |
| **Target bus voltage range (`VIN+`)** | 0.0 V to +26.0 V DC |
| **Max current range (Standard breakout)** | $\pm 3.2\text{ A}$ (with $0.1\text{ }\Omega$ shunt resistor) |
| **Max shunt voltage** | $\pm 320\text{ mV}$ (PGA gain /8) |
| **Resolution** | 12-bit ($0.8\text{ mA}$ current resolution, $4\text{ mV}$ bus voltage resolution) |
| **I2C slave address** | Base `0x40` (selectable `0x40` to `0x4F` via jumpers A0, A1) |
| **Operating current** | 1 mA active, 6 µA power-down |

## Pinout

### Standard INA219 Breakout Board Header & Screw Terminal

| Pin / Terminal | Name | Type | Description |
|---|---|---|---|
| Screw Terminal 1 | `VIN+` | High-Side Power Input | Connect to Positive Power Supply Output / Battery |
| Screw Terminal 2 | `VIN-` | High-Side Load Connection | Connect to Positive Load terminal |
| Header Pin 1 | `VCC` | Power | Logic supply (+3.0 V to +5.5 V DC) |
| Header Pin 2 | `GND` | Power | Logic Ground (0 V) |
| Header Pin 3 | `SCL` | Digital Input | I2C Serial Clock input |
| Header Pin 4 | `SDA` | Digital I/O | I2C Serial Data line |
| Header Pin 5 | `Vin+` | Power | High-Side Voltage Input (bridged to terminal `VIN+`) |
| Header Pin 6 | `Vin-` | Power | High-Side Voltage Output (bridged to terminal `VIN-`) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Logic Supply Voltage | $V_{CC}$ | 3.0 | 3.3 / 5.0 | 5.5 | V | DC |
| Bus Operating Voltage | $V_{BUS}$ | 0.0 | — | 26.0 | V | $V_{IN+}$ to GND |
| Max Shunt Voltage Range | $V_{SHUNT}$ | -320 | — | +320 | mV | $V_{IN+} - V_{IN-}$ |
| Bus Voltage Offset Error | $V_{OS,BUS}$ | — | 4.0 | 12.0 | mV | |
| Shunt Gain Error | $E_{GAIN}$ | — | 0.2 | 0.5 | % | |
| Quiescent Current | $I_{CC}$ | — | 1.0 | 1.5 | mA | Active conversion mode |
| Power-Down Current | $I_{PD}$ | — | 6 | 15 | µA | Shutdown mode |

## Register Map

| Address | Register | Access | Reset | Description |
|---|---|---|---|---|
| `0x00` | `CONFIGURATION` | R/W | `0x399F` | Bus voltage range, PGA gain, ADC resolution & mode |
| `0x01` | `SHUNT_VOLTAGE` | R | `0x0000` | Differential shunt voltage ($1\text{ LSB} = 10\text{ }\mu\text{V}$) |
| `0x02` | `BUS_VOLTAGE` | R | `0x0000` | Bus voltage ($1\text{ LSB} = 4\text{ mV}$) |
| `0x03` | `POWER` | R | `0x0000` | Calculated Power ($1\text{ LSB} = 20 \times \text{Current\_LSB}$) |
| `0x04` | `CURRENT` | R | `0x0000` | Calculated Current ($1\text{ LSB} = \text{Current\_LSB}$) |
| `0x05` | `CALIBRATION` | R/W | `0x0000` | Calibration value ($0.04096 / (\text{Current\_LSB} \times R_{SHUNT})$) |

## Wiring

```
        Power Supply (+12V) ─────► [ VIN+ ]  INA219  [ VIN- ] ─────► Load (+ Terminal)
                                      ▲                 ▲
                                      └───── Shunt ─────┘
                                           (0.1 Ω)
```

| INA219 Breakout Pin | → | Microcontroller / Circuit |
|---|---|---|
| `VCC` | | `5V` (or `3.3V`) |
| `GND` | | Common `GND` (MCU GND + Load GND) |
| `SDA` | | `SDA` (A4 on Uno, GPIO21 on ESP32) |
| `SCL` | | `SCL` (A5 on Uno, GPIO22 on ESP32) |

> [!WARNING]
> High-Side Voltage Limit:
> The target bus voltage ($V_{IN+}$) MUST NOT exceed **26.0 V DC**. Attempting to measure mains AC or DC voltages $> 26\text{ V}$ will permanently destroy the INA219 chip.

## Common mistakes

- **Low-side wiring instead of high-side:** The INA219 is designed for high-side current measurement (inserted on the positive supply wire). Wiring it on the ground side distorts ground reference levels for downstream sensors.
- **Forgetting common ground:** Not connecting the microcontroller ground to the power supply ground prevents I2C communication and causes erratic readings.
- **Uncalibrated current register reads:** The `CURRENT` (`0x04`) and `POWER` (`0x03`) registers remain zero until software writes a valid value to the `CALIBRATION` register (`0x05`).

## Notes

- Modifying the onboard sense resistor to a $0.01\text{ }\Omega$ shunt expands maximum current measurement up to $\pm 32\text{ A}$.
