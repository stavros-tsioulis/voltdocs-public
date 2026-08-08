## Overview

The **KY-038** is an electret condenser microphone sound detection sensor module from the Keyes 37-in-1 sensor kit series. Engineered to detect acoustic sound, voice, clapping, and loud noises, it combines a high-sensitivity electret microphone capsule with an onboard **LM393 differential voltage comparator** and a multi-turn sensitivity potentiometer.

The module provides dual output channels:
1. **Analog Output (`AO`):** Continuous real-time analog AC voltage waveform reflecting sound wave amplitude centered around $V_{CC} / 2$.
2. **Digital Output (`DO`):** Pulls Low (0V) when sound amplitude exceeds the threshold set by the potentiometer.

It is widely used in DIY clap-activated light switches, noise-activated alarms, and sound level indicators.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.5 V DC (5.0 V nominal) |
| **Microphone element** | Electret Condenser Microphone (ECM) |
| **Frequency response** | 50 Hz to 20 kHz |
| **Outputs** | Dual Analog Voltage (`AO`) & Digital LM393 Comparator (`DO`) |
| **Indicators** | Power LED (red) + Digital Sound Trigger LED (green) |
| **Sensitivity adjustment** | 10-turn multi-turn potentiometer on PCB |
| **Operating current** | $10\text{ mA}$ typical |

## Pinout

Standard 4-pin 0.1" (2.54 mm) module header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `AO` | Analog Output | Analog audio waveform output (centered around $V_{CC}/2$) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `VCC` / `+` | Power | Supply power input (+3.3 V to +5.5 V DC) |
| 4 | `DO` | Digital Output | LM393 comparator digital output (Low when sound threshold exceeded) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 3.3 | 5.0 | 5.5 | V | DC |
| Active Current | $I_{CC}$ | — | 10 | 15 | mA | $V_{CC} = 5.0\text{V}$ |
| Mic Sensitivity | $Sens_{mic}$| -48 | -44 | -40 | dB | $1\text{ kHz}$ at $1\text{ Pa}$ |
| Frequency Response | $Freq$ | 50 | — | 20000 | Hz | Human audible audio spectrum |
| Analog Output Offset | $V_{offset}$| — | $V_{CC}/2$ | — | V | Quiescent quiet room output |
| Digital Output Sink | $I_{sink}$ | — | 10 | 20 | mA | Open-collector output |

## Operating Principle & Signal Behavior

- **Quiet Room:** Photodiode/mic AC output is zero; `AO` sits at half supply voltage ($\sim 2.5\text{V}$ on 5V supply). `DO` sits High ($V_{CC}$).
- **Sound / Clap Detected:** Sound pressure waves vibrate the internal electret diaphragm, producing AC voltage spikes above and below $2.5\text{V}$. When negative peaks drop below the potentiometer reference, `DO` switches **Low (0V)** for the duration of the acoustic pulse, illuminating the green LED.

## Wiring

| KY-038 Pin | → | Arduino Uno | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` (`+`) | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `AO`  | | Analog Pin A0 | VP / GPIO36 | Real-time audio waveform |
| `DO`  | | Digital Pin D2 (INT0) | GPIO 4 | Digital clap/sound trigger |

## Example (Arduino Clap Switch Demo)

```cpp
const int soundDigitalPin = 2;
const int relayPin = 13;
bool relayState = false;

void setup() {
  Serial.begin(9600);
  pinMode(soundDigitalPin, INPUT);
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, relayState);
}

void loop() {
  int digitalVal = digitalRead(soundDigitalPin);

  // Active-Low trigger on clap sound
  if (digitalVal == LOW) {
    relayState = !relayState;
    digitalWrite(relayPin, relayState);
    Serial.print("CLAP DETECTED! Relay state toggled to: ");
    Serial.println(relayState ? "ON" : "OFF");
    delay(500); // Debounce delay
  }
}
```

## Common mistakes

- **Attempting FFT audio spectrum analysis on `AO`:** The electret microphone on the KY-038 lacks an onboard pre-amplifier stage (such as the MAX4466 or MAX9814), resulting in weak AC peak-to-peak voltages ($\sim 50\text{ mV}$). It is designed for threshold clap detection rather than high-fidelity voice recording.
- **Over-sensitivity lockup:** Turning the potentiometer too far counter-clockwise causes `DO` to lock permanently Low. Adjust the potentiometer until the green LED just turns OFF under quiet room conditions.

## Notes

- **KY-038 vs MAX4466 vs MAX9814:** KY-038 is a simple comparator-based sound threshold sensor; MAX4466/MAX9814 are precision audio pre-amplifiers with automatic gain control for voice recording.
