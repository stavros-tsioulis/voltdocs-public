## Overview

The **MPR121** is a 12-channel capacitive touch sensing controller manufactured by NXP Semiconductors. Communicating over $I^2C$, it converts up to 12 individual conductive surfaces (copper pads, conductive paint, fruit, metal foil) into independent touch and proximity inputs.

Featuring an internal state machine that continually measures electrode capacitance, applies hardware digital filtering, and continuously updates baseline reference levels, the MPR121 automatically adjusts to environmental changes (humidity, temperature, dust). Electrodes `ELE4` through `ELE11` can double as 8 independent LED driver GPIO output pins, making the IC ideal for touch keypads, interactive installations, and musical instruments.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.0 V DC (breakout module with 3.3V LDO) |
| **IC supply voltage (`VDD`)** | 1.71 V to 3.6 V DC (3.3 V nominal) |
| **Interface** | $I^2C$ (Fast Mode up to 400 kHz) |
| **Default $I^2C$ address** | `0x5A` (`ADDR` pin to GND) |
| **Configurable $I^2C$ addresses**| `0x5A` (GND), `0x5B` (3.3V), `0x5C` (SDA), `0x5D` (SCL) |
| **Touch electrodes** | 12 channels (`ELE0` through `ELE11`) |
| **Low power current** | $29\ \mu\text{A}$ at 16 ms sampling interval / $3\ \mu\text{A}$ standby |
| **Interrupt line** | Active-Low `IRQ` pin (triggers on touch / release events) |

## Pinout

Standard breakout board / Raspberry Pi HAT header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` / `3.3V` | Power | Supply input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 4 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 5 | `IRQ` | Digital Output | Active-Low interrupt output (pull-up required) |
| 6 | `ADDR` | Digital Input | $I^2C$ Address select pin |
| 7–18| `ELE0`–`ELE11`| Touch Inputs | Capacitive electrode pads 0 to 11 |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{CC}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with LDO |
| Active Supply Current | $I_{DD}$ | — | 29 | 40 | µA | 16 ms sampling period |
| Standby Current | $I_{sb}$ | — | 3 | 8 | µA | Stop mode |
| Electrode Capacitance Range| $C_{elec}$ | 10 | — | 2000 | pF | Per electrode channel |
| Charge Current | $I_{charge}$| 1 | 16 | 63 | µA | Programmable constant current source |
| Charge Time | $t_{charge}$| 0.5 | 1 | 32 | µs | Programmable charge duration |
| Operating Temperature | $T_{opr}$ | -40 | — | 85 | °C | Ambient |

## Operating Principle & Baseline Tracking

For each electrode pin (`ELE0`–`ELE11`), the MPR121 applies a constant current ($I_{charge}$) for a fixed duration ($t_{charge}$) and measures the resulting voltage across the electrode capacitance $C$:

$$ V = \frac{I_{charge} \times t_{charge}}{C} $$

When a finger approaches an electrode, body capacitance increases total capacitance $C$, causing the measured voltage $V$ to drop below the calibrated baseline. If the delta exceeds the programmable **Touch Threshold** (`0x41`–`0x57`), a touch event is registered.

## Wiring

| MPR121 Pin | → | Arduino Uno | ESP32 / Raspberry Pi | Notes |
|---|---|---|---|---|
| `VCC` | | 3.3V | 3.3V | Power from 3.3V rail |
| `GND` | | GND | GND | Shared system ground |
| `SCL` | | A5 | GPIO 22 / Pin 5 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 / Pin 3 | $I^2C$ Data |
| `IRQ` | | Digital D2 | GPIO 4 / Pin 11 | Active-Low interrupt (optional) |

## Example (Arduino Adafruit_MPR121)

```cpp
#include <Wire.h>
#include "Adafruit_MPR121.h"

Adafruit_MPR121 cap = Adafruit_MPR121();

// Keeps track of the last pins touched
uint16_t lasttouched = 0;
uint16_t currtouched = 0;

void setup() {
  Serial.begin(9600);
  while (!Serial);

  Serial.println("Adafruit MPR121 Capacitive Touch sensor test");
  
  // Default address 0x5A
  if (!cap.begin(0x5A)) {
    Serial.println("MPR121 not found, check wiring!");
    while (1);
  }
  Serial.println("MPR121 found!");
}

void loop() {
  currtouched = cap.touched();
  
  for (uint8_t i=0; i<12; i++) {
    // Check if electrode i was just touched
    if ((currtouched & _BV(i)) && !(lasttouched & _BV(i)) ) {
      Serial.print("Electrode "); Serial.print(i); Serial.println(" touched");
    }
    // Check if electrode i was just released
    if (!(currtouched & _BV(i)) && (lasttouched & _BV(i)) ) {
      Serial.print("Electrode "); Serial.print(i); Serial.println(" released");
    }
  }

  lasttouched = currtouched;
  delay(100);
}
```

## Common mistakes

- **Using excessively long unshielded wires to electrodes:** Long wire leads add parasitic capacitance ($>200\text{ pF}$), saturating the MPR121 baseline tracker and preventing touch detection. Keep electrode leads under $20\text{ cm}$.
- **Touching electrode leads during power-on calibration:** The MPR121 initializes baseline values immediately upon reset. Touching an electrode during power-on sets a false high baseline, making the pin unresponsive until reset.

## Notes

- **MPR121 vs TTP229:** MPR121 includes dynamic baseline autocalibration; TTP229 uses static threshold comparisons.
