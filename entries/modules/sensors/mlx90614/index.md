## Overview

The **MLX90614** is a non-contact infrared thermometer IC manufactured by Melexis. It integrates an IR thermopile detector chip, a custom signal-conditioning ASSP with a 17-bit ADC, and a powerful DSP unit inside a TO-39 metal can package.

It measures two distinct temperatures simultaneously: **Ambient temperature ($T_A$)** of the package die, and **Object surface temperature ($T_O$)** of a target body placed in its field of view without making physical contact (from $-70^\circ\text{C}$ up to $+380^\circ\text{C}$).

## Quick reference

| | |
|---|---|
| **Operating Voltage (`VCC`)** | 3.0 V to 3.6 V DC (3 V variant `MLX90614ESF-Bxx`) / 4.5 V to 5.5 V DC (5 V variant `MLX90614ESF-Axx`) |
| **Object Temp Range** | $-70^\circ\text{C}$ to $+380^\circ\text{C}$ |
| **Ambient Temp Range** | $-40^\circ\text{C}$ to $+125^\circ\text{C}$ |
| **Accuracy** | $\pm 0.5\text{ }^\circ\text{C}$ around room/body temp ($0^\circ\text{C} \text{ to } +50^\circ\text{C}$) |
| **Resolution** | $0.02\text{ }^\circ\text{C}$ output step resolution |
| **Field of View (FOV)** | $90^\circ$ standard (AAA variant) / $35^\circ$ narrow angle (DCC medical variant) |
| **Communication protocol** | 2-wire SMBus (I2C compatible, fixed default slave address `0x5A`) |

## Pinout

### Standard 4-Pin TO-39 Package & GY-906 Breakout Board

```
           ┌──────────┐
           │ MLX90614 │
           └──────────┘
            │  │  │  │
            1  2  3  4
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `SCL` / `VNK` | Digital Input | SMBus Clock line (or PWM output line) |
| 2 | `SDA` / `PWM` | Digital I/O | SMBus Data line (open-drain, requires pull-up resistor) |
| 3 | `VDD` / `VCC` | Power | Supply voltage (+3.3 V or +5.0 V depending on chip suffix) |
| 4 | `VSS` / `GND` | Power | Ground (0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (5V variant) | $V_{DD}$ | 4.5 | 5.0 | 5.5 | V | `MLX90614ESF-AAA` |
| Supply Voltage (3V variant) | $V_{DD}$ | 3.0 | 3.3 | 3.6 | V | `MLX90614ESF-BAA` |
| Operating Supply Current | $I_{DD}$ | — | 1.5 | 2.5 | mA | Active SMBus mode |
| Medical Accuracy (Body temp) | $\Delta T_{med}$ | -0.2 | $\pm 0.1$ | +0.2 | °C | $T_{obj} = 36^\circ\text{C} \text{ to } 38^\circ\text{C}$ (DCC variant) |
| Output Resolution | $RES$ | — | 0.02 | — | °C | 17-bit ADC output |
| Refresh Rate | $f_{refresh}$ | 0.01 | 0.5 | 512 | Hz | EEPROM programmable |

## SMBus Temperature Read Register & Math

Temperature data is stored as a 16-bit raw integer ($RAW$) in RAM registers:
- **`0x06`:** Read Ambient Temperature ($T_A$).
- **`0x07`:** Read Object 1 Temperature ($T_{O1}$).

### Conversion Formula to Kelvin and Celsius

$$T\text{ (in Kelvin)} = RAW \times 0.02\text{ K}$$

$$T\text{ (in }^\circ\text{C}) = (RAW \times 0.02) - 273.15$$

For example, a raw reading of `0x3AF2` ($15090$ decimal):

$$T = (15090 \times 0.02) - 273.15 = 301.80\text{ K} - 273.15 = +28.65\text{ }^\circ\text{C}$$

## Wiring

| GY-906 (MLX90614) Pin | → | Microcontroller (Arduino Uno / ESP32) | Notes |
|---|---|---|---|
| `VIN` / `VCC` | | `3.3V` or `5V` (Check breakout LDO) | Check if breakout features LDO regulator |
| `GND` | | `GND` | Ground |
| `SCL` | | `SCL` (A5 on Uno, GPIO22 on ESP32) | $4.7\text{ k}\Omega$ pull-up resistor to VCC recommended |
| `SDA` | | `SDA` (A4 on Uno, GPIO21 on ESP32) | $4.7\text{ k}\Omega$ pull-up resistor to VCC recommended |

## Common mistakes

- **Mixing 3V and 5V part numbers:** The `MLX90614ESF-AAA` is a **5V-only** part, whereas the `MLX90614ESF-BAA` is a **3.3V-only** part. Feeding 5V to a 3.3V chip without a breakout board LDO will destroy it.
- **SMBus repeated start requirement:** The MLX90614 requires I2C **Repeated Start** (`Wire.endTransmission(false)`) between writing the register address and reading the 2-byte word + PEC byte response. Standard I2C stop conditions cause SMBus NACK errors.
- **Field of View (FOV) distance errors:** The standard $90^\circ$ FOV sees a wide cone. Measuring a small object (e.g. human forehead) from $>5\text{ cm}$ away averages the object's temperature with the surrounding wall/background temperature. Place the sensor $1\text{ to }3\text{ cm}$ from the target.

## Notes

- Includes an 8-bit Packet Error Code (PEC) CRC byte at the end of SMBus readings for high-reliability industrial sensing.
