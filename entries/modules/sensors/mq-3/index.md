## Overview

The **MQ-3** is a low-cost semiconductor gas sensor manufactured by Winsen Electronics, engineered specifically for detecting ethanol ($\text{C}_2\text{H}_5\text{OH}$) gas and alcohol vapor in ambient air.

The sensor element consists of a micro ceramic tube coated with Tin Dioxide ($\text{SnO}_2$), heated internally by a nickel-chromium heating coil. Clean air exhibits low electrical conductivity; when alcohol vapor is present, the surface conductivity of $\text{SnO}_2$ increases proportionally to gas concentration.

Standard MQ-3 breakout boards pair the 6-pin sensor head with an LM393 voltage comparator, providing both a **continuous analog voltage output (`AO`)** for concentration measurement and a **digital threshold output (`DO`)** with an adjustable potentiometer. It is widely used in DIY breathalyzers, alcohol detection alarms, and environmental monitors.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 5.0 V DC (required for internal heater) |
| **Heater resistance ($R_H$)** | $31\ \Omega \pm 3\ \Omega$ at room temp |
| **Heater power consumption** | $\le 800\text{ mW}$ (~150 mA at 5V) |
| **Detection gas** | Alcohol / Ethanol vapor |
| **Concentration range** | $0.05\text{ mg/L}$ to $10.0\text{ mg/L}$ ($25\text{ ppm}$ to $500\text{ ppm}$) |
| **Outputs** | Analog Voltage (`AO`) & Digital Threshold (`DO`) |
| **Warm-up time** | 24–48 hours initial preheating / 3 minutes before sampling |

## Pinout

Standard 4-pin 0.1" (2.54 mm) breakout module header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply input (+5.0 V DC required for heater) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `DO` | Digital Output | LM393 comparator digital output (Low when gas exceeds threshold) |
| 4 | `AO` | Analog Output | Analog output voltage proportional to alcohol concentration |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 4.9 | 5.0 | 5.1 | V | DC |
| Heater Voltage | $V_H$ | 4.9 | 5.0 | 5.1 | V | AC or DC |
| Heater Current | $I_H$ | 130 | 150 | 180 | mA | $V_{CC} = 5.0\text{ V}$ |
| Sensing Resistance | $R_s$ | 1.0 | — | 10.0 | kΩ | In $0.4\text{ mg/L}$ Alcohol |
| Concentration Ratio | $R_s/R_o$ | 0.2 | — | 0.6 | — | $R_s(0.4\text{mg/L}) / R_s(\text{Clean Air})$ |
| Response Time | $t_{res}$ | — | — | $\le 10$ | s | $90\%$ response |
| Recovery Time | $t_{rec}$ | — | — | $\le 30$ | s | $90\%$ recovery |

## Calibration & Sensor Resistance Formula

The analog output voltage ($V_{AO}$) is measured across a load resistor ($R_L$, typically $10\text{ k}\Omega$ on breakout boards):

$$ R_s = \left( \frac{V_{CC} - V_{AO}}{V_{AO}} \right) \times R_L $$

1. **Clean Air Calibration ($R_o$):** Measure $V_{AO}$ in fresh air, calculate $R_s$, and divide by the clean air constant ($\approx 60$) to obtain $R_o$.
2. **Gas Concentration Calculation:** Calculate ratio $\frac{R_s}{R_o}$ and apply log-log interpolation based on the datasheet sensitivity curve:

$$\text{Alcohol Concentration (mg/L)} = 0.4 \times \left( \frac{R_s/R_o}{0.4} \right)^{-1.4}$$

## Wiring

| MQ-3 Pin | → | Arduino Uno | ESP32 (with 3.3V ADC divider) | Notes |
|---|---|---|---|---|
| `VCC` | | 5V | External 5V Power Supply | **Do not power from 3.3V** |
| `GND` | | GND | GND | System ground |
| `AO`  | | Analog Pin A0 | VP / GPIO36 (ADC1) | **Use voltage divider on ESP32** |
| `DO`  | | Digital Pin D2 | GPIO 4 | Digital threshold trigger |

> [!WARNING]
> High Heater Power & Warm-Up Time Warning:
> - The MQ-3 internal heater draws up to **180 mA** at 5V, getting warm to the touch during normal operation. Do not attempt to power `VCC` from low-current 3.3V pins or FTDI serial adapters.
> - New MQ-3 sensors require an initial **24 to 48-hour burn-in period** powered continuously to burn off factory coating and stabilize baseline readings.

## Example

```cpp
const int mq3AnalogPin = A0;

void setup() {
  Serial.begin(9600);
  Serial.println("MQ-3 Alcohol Sensor Warming Up...");
  delay(10000); // 10 second quick warm-up
}

void loop() {
  int rawADC = analogRead(mq3AnalogPin);
  float voltage = (rawADC / 1023.0) * 5.0;

  Serial.print("Raw ADC: "); Serial.print(rawADC);
  Serial.print(" | Voltage: "); Serial.print(voltage); Serial.print(" V -> ");

  if (voltage > 2.0) {
    Serial.println("ALCOHOL DETECTED!");
  } else {
    Serial.println("Air Clean");
  }

  delay(1000);
}
```

## Common mistakes

- **Powering `VCC` with 3.3V:** Operating the heater below 4.9V prevents $\text{SnO}_2$ from reaching its operating temperature ($300^\circ\text{C}$), rendering the sensor insensitive.
- **Skipping preheating:** Taking readings immediately after applying power results in false high readings during the first 3 minutes of heater warm-up.

## Notes

- **MQ Sensor Family:** MQ-2 (Gas/Smoke), MQ-3 (Alcohol), MQ-7 (Carbon Monoxide), MQ-135 (Air Quality/Ammonia).
