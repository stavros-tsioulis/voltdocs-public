## Overview

The **SW-420** is a popular vibration and shock detection sensor module included in SunFounder, Elegoo, and generic Arduino sensor kits. Built around an SW-420 metallic spring roller-ball vibration switch capsule, an **LM393 differential comparator IC**, and a multi-turn sensitivity potentiometer, it detects mechanical shocks, shaking, knocking, and seismic movement.

Under non-vibrating stationary conditions, the internal contact spring remains closed (**Normally Closed / NC state**), causing the module digital output (**`DO`**) to sit **Low (0V)**. When physical vibration or shock occurs, internal contacts momentarily bounce open, triggering `DO` to pulse **High ($V_{CC}$)**.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.5 V DC (5.0 V nominal) |
| **Switch element** | SW-420 Normally Closed (NC) Vibration Switch |
| **Comparator IC** | LM393 voltage comparator chip |
| **Quiescent Output (`DO`)**| Low (0V) when stationary / High ($V_{CC}$) when vibrating |
| **Indicators** | Power LED (red) + Vibration Trigger LED (green) |
| **Sensitivity adjustment** | Multi-turn trimmer potentiometer on PCB |
| **Operating current** | $15\text{ mA}$ typical |

## Pinout

Standard 3-pin 0.1" (2.54 mm) module header:

```
        ┌──────────────────────┐
        │  [SW-420 Cylinder]   │
        └─┬───────┬──────────┬─┘
         VCC     GND        DO
          1       2          3
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` / `+` | Power | Supply power input (+3.3 V to +5.0 V DC) |
| 2 | `GND` / `-` | Power | Ground reference (0 V) |
| 3 | `DO` / `S`  | Digital Output | LM393 digital output (Low = Stationary, High = Vibrating) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 3.3 | 5.0 | 5.5 | V | DC |
| Active Supply Current | $I_{CC}$ | — | 15 | 20 | mA | $V_{CC} = 5.0\text{V}$ |
| Switch Resistance (Closed)| $R_{closed}$| — | 0.1 | 5.0 | Ω | Stationary state |
| Switch Resistance (Open) | $R_{open}$  | 10 | — | — | MΩ | Momentary shock bounce |
| Output Drive Current | $I_{sink}$  | — | 15 | 20 | mA | LM393 output sink/source |
| Response Time | $t_{resp}$  | — | 2 | 5 | ms | Shock pulse bounce |

## Operating Principle & Signal Behavior

- **Stationary State:** The internal conductive spring rests against the metallic barrel casing, shorting the circuit. The LM393 output pin (`DO`) stays **Low (0V)**, and the green onboard LED lights up.
- **Vibration / Impact State:** Physical shaking causes the internal spring to vibrate and break electrical contact momentarily. The circuit opens, pulling `DO` **High ($V_{CC}$)** and extinguishing the green LED.

```
 Stationary:  [ DO = LOW (0V) ]  ---> Green LED ON
 Vibrating:   [ DO = HIGH (5V) ] ---> Green LED OFF
```

## Wiring

| SW-420 Pin | → | Arduino Uno | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` (`+`) | | 5V / 3.3V | 3.3V | Power rail |
| `GND` (`-`) | | GND | GND | System ground |
| `DO` (`S`)  | | Digital D2 (INT0) | GPIO 4 | Interrupt-driven shock trigger |

## Example (Arduino Intrusion / Theft Alarm)

```cpp
const int vibrationPin = 2; // Connected to DO
const int buzzerPin = 13;

void setup() {
  Serial.begin(9600);
  pinMode(vibrationPin, INPUT);
  pinMode(buzzerPin, OUTPUT);
  Serial.println("SW-420 Vibration Alarm Active");
}

void loop() {
  int val = digitalRead(vibrationPin);

  // HIGH state indicates mechanical vibration/shock contact bounce
  if (val == HIGH) {
    digitalWrite(buzzerPin, HIGH);
    Serial.println("WARNING: VIBRATION DETECTED!");
    delay(500); // Alarm duration
    digitalWrite(buzzerPin, LOW);
  }
}
```

## Common mistakes

- **Polling instead of using hardware interrupts:** Mechanical contact bounce pulses last only a few milliseconds ($2\text{--}10\text{ ms}$). Simple `loop()` delays will miss short vibration shocks. Attach an external hardware interrupt (`attachInterrupt(digitalPinToInterrupt(2), ISR, RISING)`).
- **Mis-adjusting sensitivity potentiometer:** Turning the potentiometer too far causes `DO` to latch permanently High or Low. Adjust until the green LED is ON while motionless.

## Notes

- **SW-420 vs ADXL345 vs SW-520D:** SW-420 is a simple 1-bit binary vibration switch; ADXL345 is a 3-axis accelerometer measuring numeric g-force; SW-520D is a tilt ball switch.
