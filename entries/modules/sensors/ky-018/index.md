## Overview

The **KY-018** is a classic photoresistor (Light Dependent Resistor / LDR) module from the Keyes 37-in-1 sensor kit series. Built around a 5mm Cadmium Sulfide (CdS) photoconductive cell, its internal electrical resistance decreases continuously as ambient light exposure increases.

The module pairs the LDR in series with an onboard **$10\ \text{k}\Omega$ fixed pull-down resistor** to form a simple voltage divider circuit. It outputs a continuous **analog voltage (`AO`)** that rises under bright illumination and drops in dark environments, making it ideal for automatic nightlights, solar panel trackers, and light level monitors.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.5 V DC (5.0 V nominal) |
| **Sensor type** | 5mm CdS Photoconductive LDR Cell |
| **Dark resistance ($R_{dark}$)** | $> 1.0\ \text{M}\Omega$ (in pitch darkness) |
| **Light resistance ($R_{10lux}$)**| $10\ \text{k}\Omega \dots 20\ \text{k}\Omega$ (at 10 Lux ambient light) |
| **Peak spectral response** | $540\text{ nm}$ (closely matches human eye visual response) |
| **Output signal** | Analog voltage ($0\text{V} \dots V_{CC}$) |
| **Fixed resistor** | $10\ \text{k}\Omega$ onboard pull-down resistor |

## Pinout

Standard 3-pin 0.1" (2.54 mm) module header:

```
        ┌───────────────────┐
        │  [CdS LDR Sensor] │
        └─┬───────┬───────┬─┘
          S      VCC     GND
          1       2       3
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 (`S`) | `AO` / `SIGNAL` | Analog Output | Voltage divider output pin (high voltage = bright, low voltage = dark) |
| 2 (`middle`) | `VCC` | Power | Supply power input (+3.3 V to +5.5 V DC) |
| 3 (`-`) | `GND` | Power | Ground reference (0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 3.3 | 5.0 | 5.5 | V | DC |
| Dark Resistance | $R_{dark}$ | 1.0 | 5.0 | 10.0 | MΩ | 10 seconds after light removal |
| Light Resistance (10 Lux)| $R_{10}$ | 10 | 15 | 20 | kΩ | 10 Lux illumination (2854K) |
| Response Time (Rise) | $t_{rise}$| — | 20 | 30 | ms | Dark to light step |
| Response Time (Fall) | $t_{fall}$| — | 30 | 40 | ms | Light to dark step |
| Spectral Peak | $\lambda_{peak}$| — | 540 | — | nm | Green/yellow light sensitivity |

## Voltage Divider Circuit Math

$$ V_{AO} = V_{CC} \times \left( \frac{10\text{k}\Omega}{R_{LDR} + 10\text{k}\Omega} \right) $$

- **Bright Room ($R_{LDR} \approx 2\ \text{k}\Omega$):**

$$ V_{AO} = 5.0\text{V} \times \left( \frac{10\text{k}}{2\text{k} + 10\text{k}} \right) \approx 4.16\text{V} \quad (ADC \approx 850) $$

- **Pitch Darkness ($R_{LDR} \approx 2\ \text{M}\Omega$):**

$$ V_{AO} = 5.0\text{V} \times \left( \frac{10\text{k}}{2000\text{k} + 10\text{k}} \right) \approx 0.02\text{V} \quad (ADC \approx 5) $$

## Wiring

| KY-018 Pin | → | Arduino Uno | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` (Middle) | | 5V / 3.3V | 3.3V | Power rail |
| `GND` (`-`) | | GND | GND | System ground |
| `S` (`SIGNAL`)| | Analog Pin A0 | VP / GPIO36 | Analog light level voltage |

## Example

```cpp
const int ldrPin = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int rawADC = analogRead(ldrPin);
  float voltage = (rawADC / 1023.0) * 5.0;

  Serial.print("Raw ADC: "); Serial.print(rawADC);
  Serial.print(" | Voltage: "); Serial.print(voltage); Serial.print(" V | Status: ");

  if (rawADC > 700) {
    Serial.println("Bright Daylight");
  } else if (rawADC > 300) {
    Serial.println("Indoor Lighting");
  } else {
    Serial.println("Dark Environment");
  }

  delay(300);
}
```

## Common mistakes

- **Expecting calibrated Lux values:** CdS photoresistors have high batch tolerances ($\pm 40\%$) and non-linear logarithmic response curves. They are qualitative ambient light indicators rather than precision Lux meters (use BH1750 or TSL2591 for calibrated Lux).
- **Inverting power and ground pins:** Connecting `VCC` to Pin 3 (`-`) short-circuits the supply rail through the $10\ \text{k}\Omega$ resistor when the LDR becomes bright.

## Notes

- **KY-018 vs TEMT6000 vs BH1750:** KY-018 uses a simple CdS photoresistor; TEMT6000 uses an NPN phototransistor; BH1750 uses a calibrated digital $I^2C$ sensor.
