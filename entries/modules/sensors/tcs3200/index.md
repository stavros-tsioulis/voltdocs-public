## Overview

The **TCS3200** (an upgraded version of the TCS230) is a programmable color light-to-frequency converter manufactured by AMS OSRAM (formerly TAOS). It integrates a matrix of 64 silicon photodiodes and a current-to-frequency converter into a single CMOS IC.

The $8 \times 8$ photodiode array is split into four color filter sets: 16 photodiodes with **Red** filters, 16 with **Green** filters, 16 with **Blue** filters, and 16 **Clear** (unfiltered). By selecting filter combinations via digital input pins (`S2` and `S3`), the module outputs a 50% duty-cycle square wave on the `OUT` pin whose frequency is directly proportional to the irradiance of the selected primary color. Four bright white LEDs surround the sensor on breakout boards to provide uniform object illumination for color-sorting robots.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 2.7 V to 5.5 V DC (5.0 V nominal) |
| **Output signal** | Square-wave frequency (50% duty cycle, $0\text{ to }500\text{ kHz}$) |
| **Control inputs** | `S0`, `S1` (Frequency Scaling), `S2`, `S3` (Color Filter Select) |
| **Photodiode matrix** | 64 photodiodes ($16 \times \text{Red}$, $16 \times \text{Green}$, $16 \times \text{Blue}$, $16 \times \text{Clear}$) |
| **Onboard illumination** | 4 white spotlight LEDs with `LED` control pin |
| **Operating current** | $2\text{ mA}$ typical (IC only; LEDs draw ~$40\text{ mA}$) |

## Pinout

Standard 8-pin or 10-pin breakout board header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+2.7 V to +5.5 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `S0` | Digital Input | Output frequency scaling selector bit 0 |
| 4 | `S1` | Digital Input | Output frequency scaling selector bit 1 |
| 5 | `S2` | Digital Input | Photodiode color filter selector bit 0 |
| 6 | `S3` | Digital Input | Photodiode color filter selector bit 1 |
| 7 | `OUT` | Digital Output | Square-wave output frequency pin |
| 8 | `LED` | Digital Input | Active-Low / High control pin for 4 white LEDs |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.7 | 5.0 | 5.5 | V | DC |
| Output Frequency (Clear)| $f_{out}$ | 500 | 600 | 750 | kHz | $100\%$ scaling, $\lambda = 640\text{ nm}$ |
| Non-Linearity | $E_L$ | — | 0.5%| 2.0%| — | $0\text{ to }100\text{ kHz}$ |
| Temperature Coefficient | $TC_f$ | — | 200 | — | ppm/°C | Frequency output stability |
| Peak Red Sensitivity | $\lambda_R$ | — | 640 | — | nm | Red filter peak |
| Peak Green Sensitivity | $\lambda_G$ | — | 524 | — | nm | Green filter peak |
| Peak Blue Sensitivity | $\lambda_B$ | — | 470 | — | nm | Blue filter peak |

## Control Logic Tables

### Filter Selection (`S2`, `S3`)

| `S2` | `S3` | Active Photodiode Filter Set |
|---|---|---|
| LOW | LOW | **Red** filter |
| LOW | HIGH | **Blue** filter |
| HIGH | LOW | **Clear** (no filter) |
| HIGH | HIGH | **Green** filter |

### Output Frequency Scaling (`S0`, `S1`)

| `S0` | `S1` | Output Frequency Scaling | Typical Max Frequency |
|---|---|---|---|
| LOW | LOW | Power Down | 0 Hz |
| LOW | HIGH | 2% scaling | ~10–12 kHz |
| HIGH | LOW | 20% scaling | ~100–120 kHz |
| HIGH | HIGH | 100% scaling | ~500–600 kHz |

> [!TIP]
> 20% scaling (`S0`=HIGH, `S1`=LOW) is the most common setting for Arduino and 8-bit microcontrollers, keeping pulse frequencies under $120\text{ kHz}$ for reliable hardware interrupt timing (`pulseIn()`).

## Wiring

| TCS3200 Pin | → | Arduino Uno | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V | 3.3V / 5V | Powers IC and white LEDs |
| `GND` | | GND | GND | System ground |
| `S0`  | | Digital D4 | GPIO 16 | Set HIGH |
| `S1`  | | Digital D5 | GPIO 17 | Set LOW (for 20% scaling) |
| `S2`  | | Digital D6 | GPIO 18 | Color select bit 0 |
| `S3`  | | Digital D7 | GPIO 19 | Color select bit 1 |
| `OUT` | | Digital D2 (INT0) | GPIO 4 | Frequency reading pin |

## Example

```cpp
#define S0 4
#define S1 5
#define S2 6
#define S3 7
#define sensorOut 2

void setup() {
  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);
  pinMode(sensorOut, INPUT);
  
  // Set Frequency scaling to 20%
  digitalWrite(S0, HIGH);
  digitalWrite(S1, LOW);
  
  Serial.begin(9600);
}

void loop() {
  // Read Red Filtered Frequency
  digitalWrite(S2, LOW);
  digitalWrite(S3, LOW);
  int redFreq = pulseIn(sensorOut, LOW);
  
  // Read Green Filtered Frequency
  digitalWrite(S2, HIGH);
  digitalWrite(S3, HIGH);
  int greenFreq = pulseIn(sensorOut, LOW);

  // Read Blue Filtered Frequency
  digitalWrite(S2, LOW);
  digitalWrite(S3, HIGH);
  int blueFreq = pulseIn(sensorOut, LOW);

  Serial.print("R: "); Serial.print(redFreq);
  Serial.print(" | G: "); Serial.print(greenFreq);
  Serial.print(" | B: "); Serial.println(blueFreq);

  delay(500);
}
```

## Common mistakes

- **Inverting frequency and period:** `pulseIn()` measures pulse width period (microseconds). Lower period values correspond to **higher** color intensity. Remember to map low pulse durations to high RGB intensity values.
- **Ambient light interference:** External ambient light drastically alters color balance. Use an opaque hood around the sensor to shield target objects from external room lighting.

## Notes

- **TCS3200 vs TCS34725:** TCS3200 outputs digital square-wave frequencies; TCS34725 uses $I^2C$ communication with built-in IR-blocking filters.
