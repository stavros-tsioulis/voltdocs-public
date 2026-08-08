## Overview

The **JSN-SR04T** (and updated V2.0 / V3.0 / AJ-SR04M versions) is a waterproof ultrasonic distance ranging module designed for outdoor environmental monitoring, water tank level sensing, automotive reverse parking alarms, and industrial bin fill-level systems.

Consisting of a sealed IP68 waterproof transducer probe ($2.5\text{ meter}$ cable) connected to a driver board, it measures distances from **$20\text{ cm}$ to $600\text{ cm}$ ($6.0\text{ meters}$)**. The JSN-SR04T V2.0/V3.0 features solder jumpers on the back of the PCB allowing operation in standard **HC-SR04 Trigger/Echo mode**, Automatic UART mode, or Low-Power Serial mode.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.0 V to 5.5 V DC (5.0 V nominal) |
| **Interface Modes** | Mode 0 (Trigger/Echo), Mode 1 (Auto UART), Mode 2 (Controlled UART) |
| **Distance Range** | $20\text{ cm}$ to $600\text{ cm}$ ($0.2\text{m} \dots 6.0\text{m}$) |
| **Blind Zone (Min Distance)**| $20\text{ cm}$ ($8\text{"}$) due to single-transducer ring-down time |
| **Ultrasonic Frequency** | $40\text{ kHz}$ |
| **Sensing Beam Angle** | $45^\circ \text{ to } 75^\circ$ wide conical beam |
| **Transducer Probe** | Sealed IP68 waterproof single-element transceiver |
| **Operating current** | $30\text{ mA}$ active / $<5\ \mu\text{A}$ low-power mode |

## Pinout

Driver processing board 4-pin header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply power input (+3.0 V to +5.5 V DC) |
| 2 | `Trig` / `TX`| Digital Input | Trigger pulse input (Mode 0) / UART TX Output (Mode 1 & 2) |
| 3 | `Echo` / `RX`| Digital Output | Echo pulse output (Mode 0) / UART RX Input (Mode 2) |
| 4 | `GND` | Power | Ground reference (0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 3.0 | 5.0 | 5.5 | V | DC |
| Active Supply Current | $I_{CC}$ | — | 30 | 50 | mA | Active 40 kHz ping |
| Min Distance (Blind Spot)| $Dist_{min}$| — | 20 | 25 | cm | Ring-down decay limit |
| Max Distance | $Dist_{max}$| 450 | 600 | 650 | cm | Large flat hard target |
| Beam Angle | $\theta$ | 45 | 60 | 75 | ° | Wide acoustic cone |
| Trigger Pulse Width | $t_{trig}$ | 10 | 20 | — | µs | High pulse on `Trig` pin |

## PCB Solder Jumper Modes (JSN-SR04T V2.0 / V3.0)

- **Mode 0 (Default - Open Jumpers `R27` & `M1`):** **HC-SR04 Compatible Mode.** Send $10\ \mu\text{s}$ High pulse to `Trig`, measure High pulse width on `Echo`.
- **Mode 1 (`R27` soldered with $47\text{ k}\Omega$ or Short):** **Automatic UART Output.** Sensor continuously outputs 4-byte serial telemetry at 9600 bps (`0xFF`, `Data_H`, `Data_L`, `Checksum`).
- **Mode 2 (`R27` soldered with $120\text{ k}\Omega$):** **Controlled UART Output.** Send byte `0x55` over UART to request a single distance reading.

## Speed of Sound Calculation Math (Mode 0)

$$ \text{Distance (cm)} = \frac{\text{Echo High Time } (\mu\text{s}) \times 0.0343}{2} $$

$$ \text{Distance (cm)} = \frac{\text{Echo High Time } (\mu\text{s})}{58.3} $$

## Wiring (Mode 0 - HC-SR04 Mode)

| JSN-SR04T Pin | → | Arduino Uno | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V | 5V | **5V supply recommended for 6m range** |
| `GND` | | GND | GND | System ground |
| `Trig` | | Digital D12 | GPIO 5 | $10\ \mu\text{s}$ Trigger pulse |
| `Echo` | | Digital D13 | GPIO 18 | High pulse width output |

## Example (Mode 0 - Trigger / Echo Code)

```cpp
const int trigPin = 5;
const int echoPin = 18;

void setup() {
  Serial.begin(115200);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  digitalWrite(trigPin, LOW);
}

void loop() {
  // Send 10us High pulse to Trigger pin
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read Echo pulse width (timeout 35ms for ~6m range)
  long duration = pulseIn(echoPin, HIGH, 35000);
  
  if (duration == 0) {
    Serial.println("JSN-SR04T Out of range / No Echo received");
  } else {
    float distance_cm = duration / 58.3;
    float distance_m = distance_cm / 100.0;

    Serial.print("Water Level / Distance: ");
    Serial.print(distance_cm); Serial.print(" cm (");
    Serial.print(distance_m); Serial.println(" m)");
  }

  delay(500);
}
```

## Common mistakes

- **Attempting to measure distances under 20 cm:** Because the JSN-SR04T uses a single piezoelectric transducer element for both transmitting and receiving (unlike the dual-cylinder HC-SR04), mechanical ring-down oscillations create a **$20\text{ cm}$ blind zone**. Objects closer than 20 cm return erroneous 20 cm readings.
- **Submerging the processing driver PCB:** Only the sealed transducer cylinder and cable are IP68 waterproof. The green processing driver circuit board must be housed in a dry enclosure.

## Notes

- **JSN-SR04T vs HC-SR04 vs AJ-SR04M:** HC-SR04 uses 2 non-waterproof transducers ($2\text{cm}\dots 400\text{cm}$); JSN-SR04T uses 1 waterproof transducer ($20\text{cm}\dots 600\text{cm}$).
