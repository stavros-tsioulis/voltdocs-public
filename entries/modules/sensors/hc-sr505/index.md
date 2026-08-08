## Overview

The **HC-SR505** is a miniature automatic-sensing passive infrared (PIR) motion detector module. Featuring a slim cylindrical Fresnel lens cap mounted on a narrow $40\text{ mm} \times 10\text{ mm}$ PCB, it provides reliable human presence detection across a **$100^\circ$ cone up to $3\text{ meters}$**.

Operating across a wide supply voltage range (**$4.5\text{V}$ to $20.0\text{V}$ DC**), the HC-SR505 includes internal automatic re-triggering logic: as long as motion continues within range, the **3.3V digital output (`OUT`)** remains held High. Once motion ceases, `OUT` returns Low after a fixed **8-second delay**.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 4.5 V to 20.0 V DC (5.0 V nominal) |
| **Quiescent current** | $< 60\ \mu\text{A}$ static idle |
| **Detection distance** | Up to 3.0 meters ($10\text{ feet}$) |
| **Detection angle** | $< 100^\circ$ cone angle |
| **Output logic level** | 3.3V Active-High ($3.3\text{V}$ High during motion, $0\text{V}$ Low idle) |
| **Output delay time ($t_{delay}$)**| ~8.0 seconds ($\pm 30\%$) automatic repeatable delay |
| **Form factor** | Cylindrical lens diameter $10\text{ mm}$, total module length $40\text{ mm}$ |

## Pinout

Standard 3-pin 0.1" (2.54 mm) header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 (`+`) | `VCC` | Power | Power supply input (+4.5 V to +20.0 V DC) |
| 2 (`OUT`)| `OUT` | Digital Output | Active-High digital output (3.3V logic HIGH during motion) |
| 3 (`-`) | `GND` | Power | Ground reference (0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 4.5 | 5.0 | 20.0 | V | DC |
| Quiescent Current | $I_{static}$| — | 50 | 60 | µA | Idle state |
| Output High Level | $V_{OH}$ | 3.0 | 3.3 | 3.6 | V | Motion detected |
| Output Low Level | $V_{OL}$ | 0.0 | 0.0 | 0.2 | V | No motion |
| Motion Hold Delay | $t_{delay}$ | 6.0 | 8.0 | 10.0 | s | Repeatable trigger hold time |
| Lens Diameter | $Dia_{lens}$| — | 10.0 | — | mm | Cylindrical white Fresnel lens |

## Automatic Repeatable Triggering Mode

Unlike older modules with manual jumper selects, the HC-SR505 operates strictly in **automatic repeatable trigger mode**:

- If motion is detected at second 0, `OUT` goes High (3.3V).
- If additional motion is detected at second 4, the 8-second internal timer **resets automatically**.
- `OUT` remains High until **8 seconds after the LAST detected movement**.

## Wiring

| HC-SR505 Pin | → | Arduino Uno | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` (`+`) | | 5V | 5V | **Requires $\ge 4.5\text{V}$ input** |
| `OUT` | | Digital D2 | GPIO 4 | 3.3V logic output (safe for ESP32) |
| `GND` (`-`) | | GND | GND | System ground |

> [!WARNING]
> Minimum 4.5V Supply Requirement:
> - Unlike the AM312 (which operates down to 2.7V), the HC-SR505 internal voltage regulator requires at least **4.5V** on `VCC`. Supplying 3.3V to `VCC` causes continuous false triggering or complete failure to detect motion.

## Example

```cpp
const int pirPin = 2;
const int ledPin = 13;

void setup() {
  Serial.begin(9600);
  pinMode(pirPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int pirState = digitalRead(pirPin);

  if (pirState == HIGH) {
    digitalWrite(ledPin, HIGH);
    Serial.println("MOTION DETECTED (HC-SR505)");
  } else {
    digitalWrite(ledPin, LOW);
  }

  delay(200);
}
```

## Common mistakes

- **Powering from 3.3V rails:** Always power HC-SR505 from a 5V (or higher) power rail.
- **Mounting behind glass:** Pyroelectric infrared sensors cannot detect thermal IR through glass windows, as glass reflects/absorbs long-wave infrared radiation ($9.4\ \mu\text{m}$).

## Notes

- **HC-SR505 vs HC-SR501:** HC-SR505 is significantly smaller, lacks manual adjustment potentiometers, and features a fixed 8-second delay time.
