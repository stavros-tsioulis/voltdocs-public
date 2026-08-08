## Overview

The **MLX90640** is a 768-pixel ($32 \times 24$) Far-Infrared (FIR) thermopile thermal imaging camera sensor array manufactured by Melexis. Mounted in a 4-pin TO-39 metal can package, it converts infrared radiation from objects in its field of view into real-time 2D thermal heat maps.

Measuring non-contact surface temperatures from **$-40^\circ\text{C}$ to $+300^\circ\text{C}$** with a target accuracy of **$\pm 1.0^\circ\text{C}$**, the MLX90640 comes in two FOV lens options:
- **MLX90640-BAB:** $55^\circ \times 35^\circ$ narrow Field of View (telephoto lens).
- **MLX90640-BAA:** $110^\circ \times 75^\circ$ wide Field of View (wide angle lens).

Communicating over $I^2C$ (**`0x33`** default) at speeds up to **1.0 MHz (Fast-Mode Plus)**, it supports programmable frame refresh rates from $0.5\text{ Hz}$ up to $64\text{ Hz}$.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VIN`)** | 3.3 V to 5.0 V DC (breakout module with 3.3V LDO regulator) |
| **IC supply voltage (`VDD`)** | 3.0 V to 3.6 V DC (3.3 V nominal) |
| **Interface** | $I^2C$ Fast-Mode Plus (up to 1.0 MHz) |
| **Default $I^2C$ address** | `0x33` |
| **Thermal array resolution** | 768 pixels ($32 \text{ Columns} \times 24 \text{ Rows}$) |
| **Object temperature range** | $-40^\circ\text{C}\text{ to }+300^\circ\text{C}$ |
| **FOV Lens Variants** | BAB: $55^\circ \times 35^\circ$ / BAA: $110^\circ \times 75^\circ$ |
| **Programmable refresh rate**| 0.5 Hz, 1 Hz, 2 Hz, 4 Hz, 8 Hz, 16 Hz, 32 Hz, 64 Hz |
| **Active current** | $23.0\text{ mA}$ continuous sampling |

## Pinout (TO-39 Metal Can & Breakout Header)

```
        ┌───────────────────┐
        │  [TO-39 Metal Can]│
        │   (Infrared Lens) │
        └─┬───┬───┬───┬─────┘
         VIN GND SCL SDA
          1   2   3   4
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VIN` | Power | Supply power input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `SCL` | Digital Input | $I^2C$ Serial Clock (up to 1 MHz) |
| 4 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{VIN}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with LDO |
| Active Supply Current | $I_{CC}$ | — | 23.0 | 28.0 | mA | Continuous sampling state |
| Target Temp Accuracy | $T_{acc}$ | -1.0 | $\pm 1.0$ | +1.0 | °C | Within $0^\circ\text{C} \dots 100^\circ\text{C}$ range |
| Noise Equivalent Temp (NETD)| $NETD$ | — | 0.1 | 0.25 | K | At $1\text{ Hz}$ refresh rate |
| Storage EEPROM Size | $EEPROM$| — | 832 | — | Words | On-chip factory calibration matrix |

## Thermal Frame Refresh & $I^2C$ Bandwidth Requirements

Each frame requires reading **832 words (1,664 bytes)** of RAM telemetry over $I^2C$, plus applying complex factory EEPROM calibration calculations (Stefan-Boltzmann radiation equations).

- At $f_{SCL} = 100\text{ kHz}$, max achievable frame rate is $\sim 0.5\text{ Hz}$ to $1\text{ Hz}$.
- At $f_{SCL} = 400\text{ kHz}$ / $1.0\text{ MHz}$, frame rates of **8 Hz to 16 Hz** are achievable on 32-bit MCUs (ESP32, Teensy 4.0).

## Wiring

| MLX90640 Pin | → | ESP32 | Teensy 4.0 | Notes |
|---|---|---|---|---|
| `VIN` | | 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `SCL` | | GPIO 22 | Pin 19 (SCL0) | **Requires 400kHz/1MHz $I^2C$ clock** |
| `SDA` | | GPIO 21 | Pin 18 (SDA0) | $I^2C$ Data |

> [!IMPORTANT]
> RAM Memory Requirements for MCUs:
> Processing MLX90640 EEPROM calibration matrices and pixel calculations requires **$>20\text{ KB}$ of dynamic RAM**. Traditional 8-bit microcontrollers (such as the Arduino ATmega328P with 2KB SRAM) cannot run the MLX90640 driver library. Use 32-bit ARM or ESP32 microcontrollers.

## Example (Adafruit_MLX90640 Library)

```cpp
#include <Wire.h>
#include <Adafruit_MLX90640.h>

Adafruit_MLX90640 mlx;
float frame[768]; // Buffer for 32x24 thermal pixel grid

void setup() {
  Serial.begin(115200);
  Wire.begin();
  Wire.setClock(400000); // Set I2C clock to 400 kHz

  Serial.println("Adafruit MLX90640 Thermal Camera Test");

  if (!mlx.begin(MLX90640_I2CADDR_DEFAULT, &Wire)) {
    Serial.println("MLX90640 not found! Check I2C wiring.");
    while (1);
  }

  mlx.setMode(MLX90640_CHESS);
  mlx.setResolution(MLX90640_ADC_18BIT);
  mlx.setRefreshRate(MLX90640_2_HZ); // 2 Hz refresh rate
}

void loop() {
  if (mlx.getFrame(frame) == 0) {
    // Print center pixel temperature (row 12, col 16)
    float centerTemp = frame[12 * 32 + 16];

    Serial.print("Center Target Temp: ");
    Serial.print(centerTemp);
    Serial.println(" °C");
  }

  delay(500);
}
```

## Common mistakes

- **Attempting to run on 8-bit Arduino boards:** The MLX90640 API requires large float buffers and heavy matrix math. Use 32-bit microcontrollers.
- **Using 100 kHz standard $I^2C$ speed:** Operating at 100 kHz causes frame buffer reading to stall for over 200 ms per frame. Increase $I^2C$ bus clock to 400 kHz or 1 MHz in code (`Wire.setClock(400000)`).

## Notes

- **MLX90640 vs AMG8833 vs MLX90614:** MLX90640 provides 768 pixels ($32 \times 24$ thermal image); AMG8833 provides 64 pixels ($8 \times 8$ Grid-EYE); MLX90614 is a single-pixel thermometer.
