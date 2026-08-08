## Overview

The **FSR 402** is a robust single-zone Force Sensitive Resistor (FSR) manufactured by Interlink Electronics. Featuring a 0.5-inch ($12.7\text{ mm}$) active circular sensing diameter in a thin ($0.45\text{ mm}$) polymer package, it exhibits a non-linear inverse relationship between applied mechanical force and electrical resistance.

Unpressed, the FSR 402 acts as an open circuit with a baseline resistance exceeding **$1\ \text{M}\Omega$**. Applying a light touch ($\approx 20\text{ grams} / 0.2\text{ N}$) breaks the contact threshold, causing resistance to drop sharply to $\sim 100\ \text{k}\Omega$; pushing firmly with heavy force ($\approx 2\text{ kg} / 20\text{ N}$) drops resistance below **$1\ \text{k}\Omega$**. It is widely used in electronic drum pads, touch-sensitive musical instruments, robot gripper force feedback, and bed occupancy sensing.

## Quick reference

| | |
|---|---|
| **Active sensing area** | 0.5" diameter ($12.7\text{ mm}$) circular disc |
| **Overall dimensions** | $18.28\text{ mm} \times 60.96\text{ mm} \times 0.45\text{ mm}$ |
| **Force sensitivity range** | $0.2\text{ N}$ to $20.0\text{ N}$ ($20\text{ grams}$ to $2000\text{ grams}$) |
| **Unpressed resistance** | $> 1.0\ \text{M}\Omega$ (open circuit) |
| **Full-load resistance (20N)**| $< 1.0\ \text{k}\Omega$ |
| **Break force (turn-on threshold)**| ~20 grams ($0.2\text{ N}$) |
| **Switching life** | $>10,000,000$ actuations |
| **Interface** | 2-terminal passive variable resistor (requires voltage divider or op-amp) |

## Terminal Layout & Mechanical Geometry

```
       ┌───────────────────────┐
       │     (O) Active Area   │  [=== Pin 1
       │       Ø 12.7 mm       │  [=== Pin 2
       └───────────────────────┘
```

- **Pin 1 & Pin 2:** Non-polarized 2-pin female solder tab connector ($0.1\text{"} / 2.54\text{ mm}$ spacing).
- **Actuator Tip:** For maximum force transfer, apply force through a soft rubber pad or hemispherical rubber bumper (actuator tip) placed over the active circular center area. Avoid pressing with sharp metal edges.

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Break Force | $F_{break}$ | 0.1 | 0.2 | 0.3 | N | Initial contact threshold (~20 g) |
| Force Sensitivity Range| $F_{range}$ | 0.2 | — | 20.0 | N | Continuous sensing range |
| Standoff Resistance | $R_{stand}$ | 1.0 | 10.0 | — | MΩ | Unpressed |
| Full-Load Resistance | $R_{full}$ | 0.5 | 1.0 | 2.0 | kΩ | Applied force 20 N (~2 kg) |
| Repeatability | $Rep$ | -5% | $\pm 2.5\%$| +5%| — | Single part repeatability |
| Hysteresis | $Hys$ | — | 10% | — | — | $(R_{increase} - R_{decrease}) / R$ |
| Continuous Power Rating| $P_{max}$ | — | 0.5 | — | W | Max continuous thermal power |

## Voltage Divider Circuit Math

To read force on an analog microcontroller ADC, place the FSR 402 in series with a fixed **$10\ \text{k}\Omega$ pull-down resistor ($R_M$)**:

$$ V_{OUT} = V_{CC} \times \left( \frac{R_M}{R_{FSR} + R_M} \right) $$

- **Unpressed State ($R_{FSR} > 1\ \text{M}\Omega$):**

$$ V_{OUT} \approx 5.0\text{V} \times \left( \frac{10\text{k}}{1000\text{k} + 10\text{k}} \right) \approx 0.05\text{V} \quad (ADC \approx 0) $$

- **Light Press ($R_{FSR} \approx 30\ \text{k}\Omega$):**

$$ V_{OUT} = 5.0\text{V} \times \left( \frac{10\text{k}}{30\text{k} + 10\text{k}} \right) = 1.25\text{V} \quad (ADC \approx 256) $$

- **Firm Press ($R_{FSR} \approx 1\ \text{k}\Omega$):**

$$ V_{OUT} = 5.0\text{V} \times \left( \frac{10\text{k}}{1\text{k} + 10\text{k}} \right) = 4.54\text{V} \quad (ADC \approx 930) $$

## Wiring

| FSR 402 Pin | → | Connection | Notes |
|---|---|---|---|
| Pin 1 | | $V_{CC}$ (5V or 3.3V Rail) | Power rail |
| Pin 2 | | Microcontroller Analog ADC Pin & $10\ \text{k}\Omega$ Resistor | Voltage divider junction |
| $10\ \text{k}\Omega$ Resistor Other End | | `GND` | Ground reference |

## Example

```cpp
const int fsrPin = A0;
const float VCC = 5.0;       // ADC Reference Voltage
const float R_DIV = 10000.0;  // Fixed 10k resistor

void setup() {
  Serial.begin(9600);
}

void loop() {
  int fsrADC = analogRead(fsrPin);
  
  if (fsrADC > 10) { // If pressure detected
    float fsrV = fsrADC * (VCC / 1023.0);
    float fsrR = R_DIV * (VCC / fsrV - 1.0); // Calculate FSR Resistance

    Serial.print("Raw ADC: "); Serial.print(fsrADC);
    Serial.print(" | Voltage: "); Serial.print(fsrV); Serial.print(" V");
    Serial.print(" | Resistance: "); Serial.print(fsrR / 1000.0); Serial.println(" kOhm");
  } else {
    Serial.println("No force applied (Unpressed)");
  }

  delay(200);
}
```

## Common mistakes

- **Soldering directly to the silver flexible solder tabs:** Direct soldering melts the flexible polyester substrate. Use male/female jumper header pins or crimp connectors.
- **Using FSRs for precision weight scales:** FSR 402 sensors are qualitative force/touch sensors ($\pm 15\%$ to $\pm 25\%$ accuracy) rather than precision weight measurement load cells. For precision scale builds, use load cells paired with an HX711 ADC.

## Notes

- **FSR Family:** FSR 400 (5mm micro disc), FSR 402 (12.7mm round disc), FSR 406 (38mm square), FSR 408 (600mm long strip).
