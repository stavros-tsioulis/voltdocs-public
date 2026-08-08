## Overview

The **KY-026** is an infrared (IR) flame and fire detection sensor module from the Keyes 37-in-1 sensor kit series. Engineered to detect naked flames, lighter fire, and combustion sources, it incorporates a high-speed black epoxy-encapsulated NPN phototransistor tuned to infrared light wavelengths between **$760\text{ nm}$ and $1100\text{ nm}$** (the primary IR emission spectrum of open flames).

The module pairs the IR photodiode with an LM393 differential voltage comparator and a multi-turn sensitivity potentiometer. It provides two output channels: a continuous **analog voltage output (`AO`)** for proximity/intensity estimation, and a **digital threshold output (`DO`)** that pulls Low when IR intensity exceeds the potentiometer setpoint. It is widely used in fire-fighting mini-sumo robots, stove safety alarms, and flame monitoring.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.5 V DC |
| **Spectral sensitivity** | $760\text{ nm}$ to $1100\text{ nm}$ (peak sensitivity at $940\text{ nm}$) |
| **Detection angle** | $60^\circ$ directional cone |
| **Detection distance** | Up to $80\text{ cm}$ to $100\text{ cm}$ (for a standard lighter flame) |
| **Outputs** | Dual Analog Voltage (`AO`) & Digital LM393 Comparator (`DO`) |
| **Onboard indicators** | Power LED (red) + Digital Alarm Output LED (green) |
| **Operating current** | $15\text{ mA}$ typical |

## Pinout

Standard 4-pin 0.1" (2.54 mm) breakout module header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `AO` | Analog Output | Analog voltage output (voltage drops as flame IR intensity increases) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `VCC` / `+` | Power | Supply input (+3.3 V to +5.5 V DC) |
| 4 | `DO` | Digital Output | LM393 comparator digital output (Low when flame detected) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 3.3 | 5.0 | 5.5 | V | DC |
| Peak Wavelength | $\lambda_{peak}$ | — | 940 | — | nm | Fire/flame IR spectrum |
| Spectral Bandwidth | $\lambda_{range}$| 760 | — | 1100 | nm | Response range |
| Detection Angle | $\theta$ | — | 60 | — | deg | Half-sensitivity angle |
| Lighter Flame Distance | $Dist_{flame}$| 10 | 50 | 100 | cm | Standard lighter flame in dark room |
| Response Time | $t_{res}$ | — | 15 | — | µs | Phototransistor response time |

## Operating Principle & Signal Behavior

- **No Flame / Dark:** Photodiode conductivity is near zero ($R_{dark} > 1\ \text{M}\Omega$). Analog output `AO` sits near $V_{CC}$ ($\sim 5\text{V}$), and `DO` is High ($V_{CC}$).
- **Flame Present:** IR radiation from the flame increases photodiode conductivity, drawing current through the onboard pull-down resistor. Analog voltage `AO` **drops towards 0V**. When `AO` drops below the threshold set by the trimmer potentiometer, `DO` switches **Low (0V)** and the green LED illuminates.

$$ V_{AO} \propto \frac{1}{\text{Flame IR Intensity}} $$

## Wiring

| KY-026 Pin | → | Arduino Uno | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` (`+`) | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `AO`  | | Analog Pin A0 | VP / GPIO36 (ADC1) | Analog flame intensity signal |
| `DO`  | | Digital Pin D2 | GPIO 4 | Digital threshold trigger |

> [!WARNING]
> Sunlight & Incandescent Light False Triggers:
> - Direct sunlight, halogen bulbs, and incandescent light bulbs emit significant $760\text{--}1100\text{ nm}$ IR radiation, triggering false positives on the KY-026. Keep the sensor shielded from direct sunlight or calibrate the potentiometer threshold under ambient room lighting.

## Example

```cpp
const int flameAnalogPin = A0;
const int flameDigitalPin = 2;
const int buzzerPin = 13;

void setup() {
  Serial.begin(9600);
  pinMode(flameDigitalPin, INPUT);
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  int rawAnalog = analogRead(flameAnalogPin);
  int digitalVal = digitalRead(flameDigitalPin);

  float voltage = (rawAnalog / 1023.0) * 5.0;

  Serial.print("Analog AO: "); Serial.print(rawAnalog);
  Serial.print(" ("); Serial.print(voltage); Serial.print(" V)\t| Digital DO: ");

  if (digitalVal == LOW) {
    Serial.println("FLAME DETECTED! ALARM ON!");
    digitalWrite(buzzerPin, HIGH);
  } else {
    Serial.println("Safe (No Flame)");
    digitalWrite(buzzerPin, LOW);
  }

  delay(200);
}
```

## Common mistakes

- **Inverting analog logic:** Remember that **lower analog voltages mean HIGHER flame intensity**. A reading near 0V indicates an intense flame right in front of the photodiode.
- **Melting the photodiode lens:** The black epoxy photodiode lens is plastic. Do not hold an open lighter flame closer than $10\text{ cm}$ to prevent melting the lens.

## Notes

- **KY-026 vs MQ-2:** KY-026 detects optical IR flame radiation instantly ($15\ \mu\text{s}$ response); MQ-2 detects combustible gas concentrations (LPG, smoke, propane) via chemical reaction.
