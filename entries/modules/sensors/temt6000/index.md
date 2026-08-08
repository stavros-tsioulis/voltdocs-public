## Overview

The **TEMT6000** is an analog silicon NPN epitaxial planar phototransistor manufactured by Vishay Semiconductors. Mounted on a compact 3-pin breakout module, it detects ambient light levels and outputs an analog voltage proportional to illuminance.

Designed specifically to adapt to the human eye's spectral sensitivity curve (photopic vision response peaking at **$570\text{ nm}$**), the TEMT6000 inhibits infrared (IR) wavelengths, serving as an eco-friendly, RoHS-compliant replacement for toxic Cadmium Sulfide (CdS) photoresistors (LDRs) in display backlight control, daylight harvesting, and automotive automatic headlamp triggers.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.0 V DC |
| **Output signal** | Linear Analog Voltage (0 V to $V_{CC}$) |
| **Peak spectral response** | 570 nm (human photopic vision curve) |
| **Half-sensitivity angle** | $\pm 60^\circ$ |
| **Collector current ($I_{CA}$)** | $50\ \mu\text{A}$ at 100 Lux ($V_{CE} = 5.0\text{V}$) |
| **Dark current ($I_{CEO}$)** | $2\text{ nA}$ typical ($0\text{ Lux}$) |
| **Onboard load resistor** | $10\text{ k}\Omega$ pull-down resistor on breakout module |

## Pinout

Standard 3-pin 0.1" (2.54 mm) header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` / `V` | Power | Supply voltage (+3.3 V to +5.0 V DC) |
| 2 | `GND` / `G` | Power | Ground (0 V) |
| 3 | `OUT` / `S` | Analog Output | Analog voltage output proportional to ambient light |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 3.3 | 5.0 | 5.5 | V | DC |
| Collector Light Current | $I_{CA}$ | 20 | 50 | 100 | µA | $E_v = 100\text{ Lux}$, $V_{CE} = 5.0\text{V}$ |
| Dark Current | $I_{CEO}$ | — | 2 | 50 | nA | $E_v = 0\text{ Lux}$, $V_{CE} = 5.0\text{V}$ |
| Wavelength of Peak Sensitivity| $\lambda_p$| — | 570 | — | nm | Human eye sensitivity curve |
| Range of Spectral Bandwidth | $\lambda_{0.5}$ | 440 | — | 800 | nm | Half-sensitivity range |
| Rise / Fall Time | $t_r / t_f$ | — | 15 / 15 | — | µs | $R_L = 1\text{ k}\Omega, I_C = 1\text{ mA}$ |

## Circuit Principle & Lux Approximation

On standard breakout boards, the TEMT6000 phototransistor collector connects to `VCC`, and the emitter connects to `GND` through a **$10\text{ k}\Omega$ pull-down resistor** ($R_L$). The `OUT` voltage is measured across $R_L$:

$$ V_{OUT} = I_{CA} \times R_L = I_{CA} \times 10,000\ \Omega $$

At $100\text{ Lux}$, $I_{CA} \approx 50\ \mu\text{A} \implies V_{OUT} \approx 50\ \mu\text{A} \times 10\text{ k}\Omega = 0.5\text{V}$.

Approximate Lux calculation formula:

$$ \text{Illuminance (Lux)} = \frac{V_{OUT}}{V_{CC}} \times 1000 \quad \text{(or } \text{Lux} = \frac{ADC_{raw}}{ADC_{max}} \times 1000 \text{)} $$

## Wiring

| TEMT6000 Pin | → | Arduino Uno | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Match supply to ADC reference voltage |
| `GND` | | GND | GND | System ground |
| `OUT` | | Analog Pin A0 | VP / GPIO36 (ADC1) | Linear analog output |

## Example

```cpp
const int lightSensorPin = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int rawADC = analogRead(lightSensorPin);
  float voltage = (rawADC / 1023.0) * 5.0;
  
  // Approximate Lux calculation
  float lux = (voltage / 5.0) * 1000.0;

  Serial.print("Raw ADC: "); Serial.print(rawADC);
  Serial.print(" | Voltage: "); Serial.print(voltage); Serial.print(" V");
  Serial.print(" | Lux: "); Serial.println(lux);

  delay(500);
}
```

## Common mistakes

- **Conflating phototransistor behavior with CdS LDRs:** CdS photoresistors decrease resistance with light (requiring a voltage divider circuit); the TEMT6000 module outputs a direct positive voltage that **increases linearly with light**.
- **Expecting precision lux meter accuracy:** The TEMT6000 provides excellent relative illuminance sensing, but component tolerances ($\pm 50\%$ on $I_{CA}$) mean uncalibrated Lux values are approximations.

## Notes

- **TEMT6000 vs LDR (CdS):** CdS photoresistors are banned in many countries under RoHS environmental regulations due to cadmium content; TEMT6000 is RoHS compliant and IR-filtered.
