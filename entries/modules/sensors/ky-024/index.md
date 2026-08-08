## Overview

The **KY-024** is a linear magnetic field sensor module from the Keyes sensor kit series. Unlike latching or digital Hall switches (such as the A3144), the KY-024 incorporates a **49E / SS49E linear Hall-effect element** that outputs a continuous analog voltage proportional to magnetic field strength and polarity (North vs. South magnetic poles).

Equipped with an onboard LM393 differential voltage comparator and a multi-turn trimmer potentiometer, the module provides dual outputs:
1. **Analog Output (`AO`):** Continuous analog voltage reflecting magnetic flux density ($1.4\text{ to }3.0\text{ mV/Gauss}$).
2. **Digital Output (`DO`):** Switches Low (0V) when magnetic field intensity exceeds the threshold set by the potentiometer.

It is widely used for measuring motor shaft RPM, detecting magnet proximity, sensing current strength, and contactless position measurement.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.5 V DC (5.0 V nominal) |
| **Sensor element** | 49E Linear Hall-Effect Sensor |
| **Quiescent voltage ($V_{0G}$)** | $V_{CC} / 2 \approx 2.5\text{V}$ (at zero magnetic field) |
| **Sensitivity** | $1.4\text{ to }3.0\text{ mV/Gauss}$ |
| **Magnetic polarity response** | South pole increases $V_{AO}$ above $2.5\text{V}$; North pole decreases $V_{AO}$ below $2.5\text{V}$ |
| **Outputs** | Dual Analog Voltage (`AO`) & Digital LM393 Comparator (`DO`) |
| **Indicators** | Power LED (red) + Digital Alarm Output LED (green) |

## Pinout

Standard 4-pin 0.1" (2.54 mm) breakout module header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `AO` | Analog Output | Continuous analog voltage output ($0.5\text{V}$ to $V_{CC}-0.5\text{V}$) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `VCC` / `+` | Power | Supply input (+3.3 V to +5.5 V DC) |
| 4 | `DO` | Digital Output | LM393 comparator digital output (Low when magnetic field threshold exceeded) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 3.3 | 5.0 | 5.5 | V | DC |
| Quiescent Output Voltage| $V_{0G}$ | 2.25 | 2.50 | 2.75 | V | $B = 0\text{ Gauss}$, $V_{CC} = 5.0\text{V}$ |
| Sensitivity | $Sens$ | 1.4 | 1.8 | 3.0 | mV/G | Measured at $25^\circ\text{C}$ |
| Magnetic Range | $B_{range}$ | -1000 | — | +1000 | Gauss | Linear operating range |
| Output Current Sink/Source| $I_{out}$ | — | 1.5 | 10 | mA | Analog output pin |
| Operating Current | $I_{CC}$ | — | 15 | 20 | mA | Board operating current |

## Analog Output Voltage Math

The analog output voltage $V_{AO}$ responds linearly to magnetic flux density $B$ (in Gauss):

$$ V_{AO} = V_{0G} + (Sens \times B) $$

For a typical $5.0\text{V}$ supply ($V_{0G} = 2.50\text{V}$ and $Sens = 1.8\text{ mV/Gauss}$):
- **No Magnet Present ($B = 0\text{ G}$):** $V_{AO} = 2.50\text{V} \quad (ADC \approx 512)$
- **South Pole Approaching ($B = +500\text{ G}$):** $V_{AO} = 2.50\text{V} + (0.0018 \times 500) = 3.40\text{V} \quad (ADC \approx 696)$
- **North Pole Approaching ($B = -500\text{ G}$):** $V_{AO} = 2.50\text{V} - (0.0018 \times 500) = 1.60\text{V} \quad (ADC \approx 327)$

## Wiring

| KY-024 Pin | → | Arduino Uno | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` (`+`) | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `AO`  | | Analog Pin A0 | VP / GPIO36 | Analog magnetic flux voltage |
| `DO`  | | Digital Pin D2 | GPIO 4 | Digital threshold trigger |

## Example

```cpp
const int hallAnalogPin = A0;
const int hallDigitalPin = 2;

void setup() {
  Serial.begin(9600);
  pinMode(hallDigitalPin, INPUT);
}

void loop() {
  int rawADC = analogRead(hallAnalogPin);
  int digitalState = digitalRead(hallDigitalPin);

  float voltage = (rawADC / 1023.0) * 5.0;
  // Estimate Gauss relative to 2.5V zero-point (1.8 mV/Gauss)
  float gauss = (voltage - 2.50) / 0.0018;

  Serial.print("Raw ADC: "); Serial.print(rawADC);
  Serial.print(" | Voltage: "); Serial.print(voltage); Serial.print(" V");
  Serial.print(" | Field: "); Serial.print(gauss); Serial.print(" Gauss");
  Serial.print(" | DO: "); Serial.println(digitalState == LOW ? "TRIGGERED" : "NORMAL");

  delay(200);
}
```

## Common mistakes

- **Expecting digital latching behavior:** Unlike the A3144 (which latches digital output state), the KY-024 phototransistor output is linear. The digital `DO` pin only triggers while the magnet is physically close to the sensor.
- **Ignoring magnetic orientation:** Placing a magnet upside down flips the voltage direction (e.g. from $>2.5\text{V}$ to $<2.5\text{V}$). Reverse the magnet face if `DO` fails to trigger.

## Notes

- **KY-024 vs A3144:** KY-024 provides continuous analog voltage and dual outputs using the 49E linear element; A3144 provides open-collector digital switching only.
