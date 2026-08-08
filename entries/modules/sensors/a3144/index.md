## Overview

The **A3144** (also sold under part numbers 3144, A3144E, A3144L) is a popular unipolar digital Hall effect switch IC manufactured by Allegro MicroSystems and generic semiconductor vendors. Integrated into a 3-pin TO-92 package or mounted on a 3-pin / 4-pin breakout board, it detects the presence of a magnetic field and switches its output state digitally.

Operating as an active-low **unipolar switch**, the A3144 turns **ON** (pulling its open-collector output to `GND`) when exposed to a sufficiently strong **South magnetic pole** perpendicular to its branded face. When the magnetic field is removed, the output turns **OFF** (returning to High impedance). It is universally used for motor RPM tachometers, wheel speed sensing, magnetic door proximity switches, and contactless limit switches.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 4.5 V to 24.0 V DC |
| **Output type** | Open-Collector NPN (Active Low; requires external $10\text{ k}\Omega$ pull-up resistor) |
| **Magnetic response** | Unipolar (responds to South magnetic pole face) |
| **Operating Point ($B_{OP}$)** | 350 Gauss max (typical ~175 Gauss) |
| **Release Point ($B_{RP}$)** | 10 Gauss min (typical ~120 Gauss) |
| **Hysteresis ($B_{HYS}$)** | 55 Gauss typical |
| **Max output sink current** | 25 mA continuous |

## Pinout (TO-92 Package & Breakout Board)

### TO-92 Package (Front Branded Face)

```
        ┌─────────┐
        │  A3144  │
        └────┬────┘
             │ │ │
             1 2 3
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+4.5 V to +24.0 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `OUT` | Open-Collector Output | Active-Low digital output pin |

### Breakout Module Header (3-Pin Header)

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` / `+` | Power | Supply input (+3.3 V to +5.0 V DC) |
| 2 | `GND` / `-` | Power | Ground reference (0 V) |
| 3 | `OUT` / `S` | Digital Output | Digital signal output (High = No Magnet, Low = South Pole Detected) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 4.5 | 5.0 | 24.0 | V | DC |
| Supply Current | $I_{CC}$ | 4.0 | 7.0 | 11.0 | mA | Output OFF ($V_{CC} = 24\text{V}$) |
| Output Saturation Voltage | $V_{SAT}$ | — | 175 | 400 | mV | $I_{OUT} = 20\text{ mA}, B > B_{OP}$ |
| Output Leakage Current | $I_{OFF}$ | — | 0.1 | 10.0 | µA | $V_{OUT} = 24\text{ V}, B < B_{RP}$ |
| Output Rise / Fall Time | $t_r / t_f$ | — | 0.04 / 0.18 | 2.0 | µs | $R_L = 820\ \Omega, C_L = 20\text{ pF}$ |
| Operating Temperature | $T_A$ | -40 | — | 150 | °C | Automotive rating |

## Operating Principle & Magnetic Orientation

- **No Magnetic Field:** Output transitors are OFF; the `OUT` pin floats High via the pull-up resistor ($V_{OUT} = V_{CC}$).
- **South Magnetic Pole Brought Near Branded Face:** When magnetic flux density exceeds $B_{OP}$, the NPN transistor conducts, pulling `OUT` Low ($V_{OUT} \approx 0.175\text{ V}$).
- **North Magnetic Pole:** The unipolar A3144 ignores North magnetic fields.
- **Hysteresis:** Built-in magnetic hysteresis ($B_{HYS} \approx 55\text{ Gauss}$) prevents chatter and false triggering when magnets pass near the threshold distance.

## Wiring

| A3144 TO-92 Pin | → | Arduino Uno | ESP32 | Notes |
|---|---|---|---|---|
| Pin 1 (`VCC`) | | 5V | 5V / 3.3V | Operating voltage 4.5V+ (3.3V modules include booster/LDO) |
| Pin 2 (`GND`) | | GND | GND | System ground |
| Pin 3 (`OUT`) | | Digital D2 (INT0) | GPIO 4 | **Requires $10\text{ k}\Omega$ pull-up resistor to $V_{CC}$** |

## Example (RPM Tachometer Counter)

```cpp
const int hallPin = 2; // Interrupt 0 on Arduino Uno
volatile unsigned int pulseCount = 0;

void countPulse() {
  pulseCount++;
}

void setup() {
  Serial.begin(9600);
  pinMode(hallPin, INPUT_PULLUP); // Enable internal pull-up
  attachInterrupt(digitalPinToInterrupt(hallPin), countPulse, FALLING);
}

void loop() {
  pulseCount = 0;
  delay(1000); // Measure pulses in 1 second
  
  // Calculate RPM assuming 1 magnet on rotating shaft
  unsigned int rpm = pulseCount * 60;

  Serial.print("Pulse Count: "); Serial.print(pulseCount);
  Serial.print(" | Motor Speed: "); Serial.print(rpm); Serial.println(" RPM");
}
```

## Common mistakes

- **Forgetting the open-collector pull-up resistor:** Raw TO-92 A3144 ICs have open-collector outputs. Leaving `OUT` without a $10\text{ k}\Omega$ pull-up resistor (or enabling `INPUT_PULLUP` in software) results in floating readings that never return High.
- **Presenting the North pole of the magnet:** The A3144 is unipolar and only responds to South magnetic poles presented to the front face. Flip the magnet over if no pulses are detected.

## Notes

- **A3144 vs US1881:** A3144 is a *unipolar switch* (turns ON with South, turns OFF when magnet leaves); US1881 is a *bipolar latching sensor* (turns ON with South, stays ON until a North pole arrives).
