## Overview

The **ADXL335** is a classic 3-axis analog MEMS accelerometer manufactured by Analog Devices. Housed in a compact $4 \times 4\text{ mm}$ 16-lead LFCSP package, it measures dynamic acceleration (motion, vibration, shock) and static acceleration (gravity tilt) across a **$\pm 3g$** full-scale range.

Unlike digital accelerometers (such as the ADXL345 or MPU6050) that output $I^2C$ or SPI registers, the ADXL335 features pure **ratiometric analog voltage outputs** for X, Y, and Z axes. Each axis output voltage is centered at $\frac{V_{CC}}{2}$ ($1.65\text{V}$ at 3.3V supply) and shifts by $300\text{ mV/g}$. It is widely used in simple tilt switches, RC model leveling, and analog microcontroller projects.

## Quick reference

| | |
|---|---|
| **Module supply voltage (`VCC`)** | 3.3 V to 5.0 V DC (GY-61 module includes 3.3V regulator) |
| **IC supply voltage (`VDD`)** | 1.8 V to 3.6 V DC (3.3 V nominal) |
| **Output signal** | 3 Ratiometric Analog Voltages ($V_X, V_Y, V_Z$) |
| **Full-scale range** | $\pm 3g$ (typical) |
| **Sensitivity** | $300\text{ mV/g}$ (at 3.3V supply) |
| **Zero-$g$ bias voltage** | $\frac{V_{CC}}{2}$ ($1.65\text{V}$ at 3.3V supply) |
| **Operating current** | $350\ \mu\text{A}$ typical |

## Pinout

Common 5-pin GY-61 breakout board header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `X` / `XOUT` | Analog Output | X-axis acceleration analog voltage |
| 4 | `Y` / `YOUT` | Analog Output | Y-axis acceleration analog voltage |
| 5 | `Z` / `ZOUT` | Analog Output | Z-axis acceleration analog voltage |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{CC}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with 3.3V regulator |
| Active Supply Current | $I_{CC}$ | — | 350 | 450 | µA | $V_{DD} = 3.0\text{ V}$ |
| Full-Scale Range | $Range$ | $\pm 3.0$ | $\pm 3.6$ | — | g | Minimum range $\pm 3.0g$ |
| Sensitivity | $S_{acc}$ | 270 | 300 | 330 | mV/g | Ratiometric to $V_{DD} = 3.3\text{V}$ |
| Zero-$g$ Voltage Output | $V_{0g}$ | 1.5 | 1.65 | 1.8 | V | $V_{DD} = 3.3\text{ V}$ |
| Bandwidth (X, Y) | $f_{XY}$ | 0.5 | 500 | 1600 | Hz | Set by external filtering caps $C_X, C_Y$ |
| Bandwidth (Z) | $f_Z$ | 0.5 | 500 | 550 | Hz | Set by external filtering cap $C_Z$ |

## Analog Voltage Conversion Formula

Because outputs are **ratiometric** (proportional to supply voltage $V_{DD}$), acceleration in $g$-force is calculated as:

$$ \text{Acceleration } (g) = \frac{V_{out} - V_{zero\_g}}{\text{Sensitivity}} = \frac{V_{out} - (V_{DD} / 2)}{0.300\text{ V/g}} $$

For a 10-bit ADC reading on Arduino (3.3V reference $V_{REF} = 3.3\text{V}$):

$$ g_x = \frac{\left( ADC_x - 512 \right) \times 3.3}{1023 \times 0.300} $$

## Wiring

| ADXL335 Pin | → | Arduino Uno | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 3.3V | 3.3V | Connect 3.3V pin to Arduino `AREF` pin |
| `GND` | | GND | GND | System ground |
| `X`   | | Analog A0 | VP / GPIO36 (ADC1) | X-axis analog signal |
| `Y`   | | Analog A1 | VN / GPIO39 (ADC1) | Y-axis analog signal |
| `Z`   | | Analog A2 | GPIO34 (ADC1) | Z-axis analog signal |

> [!WARNING]
> ADC Reference Matching:
> - Because ADXL335 output sensitivity scales with supply voltage ($300\text{ mV/g}$ at 3.3V vs $450\text{ mV/g}$ at 5V), the microcontroller ADC reference ($V_{REF}$) **MUST** match the ADXL335 supply voltage.
> - On 5V Arduino boards, connect the Arduino 3.3V pin to the `AREF` pin and call `analogReference(EXTERNAL)` in software.

## Example

```cpp
const int xPin = A0;
const int yPin = A1;
const int zPin = A2;

// Zero-g ADC baselines (calibrated per sensor)
int zeroG_X = 512;
int zeroG_Y = 512;
int zeroG_Z = 512;

void setup() {
  Serial.begin(9600);
  // Set ADC reference to 3.3V AREF pin on 5V Arduino Uno
  analogReference(EXTERNAL);
}

void loop() {
  int rawX = analogRead(xPin);
  int rawY = analogRead(yPin);
  int rawZ = analogRead(zPin);

  // 3.3V / 1024 = 3.22 mV per count; 300 mV/g sensitivity -> 0.0107 g per count
  float gx = (rawX - zeroG_X) * 0.0107;
  float gy = (rawY - zeroG_Y) * 0.0107;
  float gz = (rawZ - zeroG_Z) * 0.0107;

  Serial.print("X: "); Serial.print(gx); Serial.print(" g\t");
  Serial.print("Y: "); Serial.print(gy); Serial.print(" g\t");
  Serial.print("Z: "); Serial.print(gz); Serial.println(" g");

  delay(200);
}
```

## Common mistakes

- **Not setting `analogReference(EXTERNAL)` on 5V Arduino:** Reading a 3.3V analog sensor using a default 5.0V ADC reference reduces measurement resolution and distorts $g$-force math.
- **Forgetting per-sensor zero-$g$ offset calibration:** Manufacturing tolerances introduce $\pm 150\text{ mV}$ offset shifts. Place the sensor flat on a level surface and calibrate zero-$g$ ADC constants for X and Y, and $+1g$ for Z.

## Notes

- **ADXL335 vs ADXL345:** ADXL335 is 3-axis analog ($\pm 3g$ max); ADXL345 is 13-bit digital $I^2C$/SPI ($\pm 16g$ max).
