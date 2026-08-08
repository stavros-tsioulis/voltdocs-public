## Overview

The **GP2Y0A21YK0F** (often shortened to GP2Y0A21) is a popular analog infrared distance measuring sensor unit manufactured by Sharp. It incorporates an infrared LED emitter, a linear Position Sensitive Detector (PSD), and an internal signal processing circuit inside a black plastic package fitted with twin optical lenses.

Using **optical triangulation**, the sensor measures distance ($10\text{ cm to }80\text{ cm}$) by assessing the angle at which reflected IR light hits the PSD array. Because distance is determined by angle rather than reflected light intensity, readings remain largely immune to variations in target color, surface reflectivity, or ambient temperature. It is widely used for obstacle avoidance in mobile robotics and wall-following mini-sumo bots.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 4.5 V to 5.5 V DC (5.0 V nominal) |
| **Measuring distance range** | 10 cm to 80 cm ($3.9\text{" to }31.5\text{"}$) |
| **Output type** | Non-linear Analog Voltage ($3.1\text{V}$ at 10 cm to $0.4\text{V}$ at 80 cm) |
| **Average supply current** | 30 mA typical (peak pulse current ~200 mA) |
| **Response update period** | $38.3\text{ ms} \pm 9.6\text{ ms}$ |
| **Connector type** | 3-pin JST-PH 2.0 mm connector |

## Pinout

The sensor terminates in a 3-pin JST-PH connector (wired cable provided):

| Pin | Cable Color | Name | Type | Description |
|---|---|---|---|---|
| 1 | Red | `VCC` | Power | Power supply input (+4.5 V to +5.5 V DC) |
| 2 | Black | `GND` | Power | Ground reference (0 V) |
| 3 | Yellow / White | `Vo` / `OUT` | Analog Output | Non-linear analog distance voltage output |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 4.5 | 5.0 | 5.5 | V | DC |
| Average Current | $I_{CC}$ | — | 30 | 40 | mA | $V_{CC} = 5.0\text{ V}$ |
| Peak Current | $I_{peak}$ | — | 200 | — | mA | During IR LED pulse bursts |
| Distance Range | $L$ | 10 | — | 80 | cm | Reliable range |
| Output Voltage (at 10 cm)| $V_{10}$ | 2.8 | 3.1 | 3.4 | V | $V_{CC} = 5.0\text{ V}$ |
| Output Voltage (at 80 cm)| $V_{80}$ | 0.25 | 0.4 | 0.55 | V | $V_{CC} = 5.0\text{ V}$ |
| Update Period | $T_{sample}$ | 28.7 | 38.3 | 47.9 | ms | Optical measurement cycle |

## Output Curve & Distance Math

The output voltage follows an inverse non-linear relationship:

- At $<10\text{ cm}$ (blind zone), voltage drops sharply back down to 0V (causing ambiguity!).
- At $10\text{ cm}$, output peaks at $\approx 3.1\text{V}$.
- At $80\text{ cm}$, output drops to $\approx 0.4\text{V}$.

Distance $D$ (in cm) can be calculated from 10-bit ADC voltage $V_{out}$ using empirical inverse linear approximation:

$$ D\text{ (cm)} = \frac{27.86}{V_{out} - 0.1} \quad \text{or} \quad D\text{ (cm)} = \frac{4800}{ADC_{raw} - 20} $$

## Wiring

| Sharp Sensor Pin | → | Arduino Uno | ESP32 (with divider) | Notes |
|---|---|---|---|---|
| Red (`VCC`) | | 5V | External 5V Power | Power from 5V rail |
| Black (`GND`) | | GND | GND | Shared system ground |
| Yellow (`Vo`) | | Analog A0 | VP / GPIO36 (ADC1) | **Use voltage divider for 3.3V ADCs** |

> [!WARNING]
> Pulsed Current & Blind Zone Hazards:
> - The internal IR LED pulses at high current (~200 mA peak). Always place a **$10\ \mu\text{F}$ to $47\ \mu\text{F}$ electrolytic capacitor** across `VCC` and `GND` right at the sensor connector to stabilize the power rail and eliminate ADC voltage ripple.
> - Objects closer than **10 cm** produce output voltages identical to objects at 30–80 cm. Ensure mechanical mounting recessed back from outer bumpers.

## Example

```cpp
const int sensorPin = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int rawADC = analogRead(sensorPin);
  
  // Convert ADC reading (0-1023) to Voltage (0-5V)
  float voltage = rawADC * (5.0 / 1023.0);
  
  // Calculate distance in cm using empirical formula
  float distanceCM = 27.86 / (voltage - 0.1);

  if (distanceCM >= 10.0 && distanceCM <= 80.0) {
    Serial.print("Voltage: "); Serial.print(voltage);
    Serial.print(" V | Distance: "); Serial.print(distanceCM); Serial.println(" cm");
  } else {
    Serial.println("Target out of valid 10-80cm range");
  }

  delay(200);
}
```

## Common mistakes

- **Operating within the $<10\text{ cm}$ blind zone:** Causes false long-range readings when an obstacle is right against the lens.
- **Powering without decoupling capacitors:** Inductive current pulses corrupt neighboring ADC measurements on the microcontroller board.

## Notes

- **Sharp Distance Family:** GP2Y0A21YK (10–80 cm), GP2Y0A02YK (20–150 cm), GP2Y0A41SK (4–30 cm).
