## Overview

The **Flex Sensor 2.2"** (manufactured by Spectra Symbol and distributed by SparkFun and Adafruit) is a flexible carbon-based variable resistor strip. As the sensor is physically bent, conductive carbon particles printed on its flexible polymer substrate separate, causing electrical resistance to increase proportionally to the bend angle.

Unbent (flat), the 2.2-inch sensor has a nominal baseline resistance of **$10\ \text{k}\Omega$**. Bending the sensor $90^\circ$ away from the ink-printed surface increases its resistance to approximately **$30\ \text{k}\Omega$ to $40\ \text{k}\Omega$**. It is widely used in VR data gloves (finger flexion tracking), animatronic puppet controls, robotic joint position sensing, and wearable motion capture.

## Quick reference

| | |
|---|---|
| **Length** | 2.2 inches ($55.88\text{ mm}$) active length |
| **Flat resistance ($R_{flat}$)** | $10.0\ \text{k}\Omega \pm 30\%$ |
| **Bent resistance ($90^\circ$)** | $30.0\ \text{k}\Omega$ to $40.0\ \text{k}\Omega$ |
| **Resistance tolerance** | $\pm 30\%$ |
| **Power rating** | 0.5 Watts continuous |
| **Flexing life cycle** | $>1,000,000$ bends |
| **Interface** | 2-terminal passive variable resistor (requires voltage divider) |

## Terminal Layout & Physical Structure

```
       ┌──────────────────────────────────────────────┐  [=== Pin 1
       │  Spectra Symbol Flex Sensor 2.2" (Ink Facing) │  [=== Pin 2
       └──────────────────────────────────────────────┘
       <--------------- 55.88 mm Active --------------->
```

- **Pin 1 & Pin 2:** Non-polarized 2-pin solder tab header ($0.1\text{"} / 2.54\text{ mm}$ spacing).
- **Direction of Bend:** Bend **away** from the printed text/ink side (so the ink layer is stretched on the outer curve of the bend) for maximum resistance increase and longest mechanical life.

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Flat Resistance | $R_{flat}$ | 7.0 | 10.0 | 13.0 | kΩ | Completely unbent / flat |
| 90° Bend Resistance | $R_{90}$ | 25.0 | 35.0 | 45.0 | kΩ | Bent 90 degrees away from ink |
| 180° Bend Resistance | $R_{180}$ | 40.0 | 60.0 | 90.0 | kΩ | Bent 180 degrees |
| Continuous Power Rating | $P_{max}$ | — | 0.5 | 1.0 | W | Thermal rating |
| Continuous Current Limit| $I_{max}$ | — | — | 1.0 | mA | Recommended loop current |
| Operating Temperature | $T_{opr}$ | -35 | 25 | 80 | °C | Ambient |

## Voltage Divider Circuit Math

To convert variable resistance into a voltage readable by a microcontroller ADC, place the flex sensor in series with a fixed **$10\ \text{k}\Omega$ pull-down resistor ($R_F$)**:

$$ V_{OUT} = V_{CC} \times \left( \frac{R_F}{R_{flex} + R_F} \right) $$

- **Flat State ($R_{flex} = 10\ \text{k}\Omega$):**

$$ V_{OUT} = 5.0\text{V} \times \left( \frac{10\text{k}}{10\text{k} + 10\text{k}} \right) = 2.50\text{V} \quad (ADC \approx 512) $$

- **$90^\circ$ Bent State ($R_{flex} = 30\ \text{k}\Omega$):**

$$ V_{OUT} = 5.0\text{V} \times \left( \frac{10\text{k}}{30\text{k} + 10\text{k}} \right) = 1.25\text{V} \quad (ADC \approx 256) $$

## Wiring

| Flex Sensor Terminal | → | Connection | Notes |
|---|---|---|---|
| Pin 1 | | $V_{CC}$ (5V or 3.3V Rail) | Power rail |
| Pin 2 | | Microcontroller Analog ADC Pin & $10\ \text{k}\Omega$ Resistor | Voltage divider junction |
| $10\ \text{k}\Omega$ Resistor Other End | | `GND` | Ground reference |

> [!WARNING]
> Mechanical Strain Relief:
> - The solder tab base pins are fragile. Bending the sensor directly at the solder pin junction will snap the electrical traces. **Always apply heat-shrink tubing or hot glue over the pin base** for strain relief and mount the active flex section on a flexible substrate (such as a glove finger).

## Example

```cpp
const int flexPin = A0;
const float VCC = 5.0;      // ADC Reference Voltage
const float R_DIV = 10000.0; // Fixed 10k resistor

void setup() {
  Serial.begin(9600);
}

void loop() {
  int flexADC = analogRead(flexPin);
  float flexV = flexADC * (VCC / 1023.0);
  
  // Calculate Flex Sensor Resistance
  float R_flex = R_DIV * (VCC / flexV - 1.0);

  // Map estimated angle (10k = 0 deg, 30k = 90 deg)
  float angle = map(R_flex, 10000, 30000, 0, 90);
  angle = constrain(angle, 0, 90);

  Serial.print("ADC: "); Serial.print(flexADC);
  Serial.print(" | Resistance: "); Serial.print(R_flex / 1000.0); Serial.print(" kOhm");
  Serial.print(" | Angle: "); Serial.print(angle); Serial.println(" deg");

  delay(200);
}
```

## Common mistakes

- **Bending near the base connector:** Concentrating mechanical stress at the solder tabs snaps internal metal contacts. Keep bends within the middle 2-inch flexible zone.
- **Forgetting per-sensor calibration:** Resistance values vary $\pm 30\%$ between manufacturing lots ($R_{flat}$ can range from $7\ \text{k}\Omega$ to $13\ \text{k}\Omega$). Always calibrate flat and bent ADC thresholds in code using `map()`.

## Notes

- **Flex Sensor Lengths:** Available in 2.2-inch (short) and 4.5-inch (long) formats.
