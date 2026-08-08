## Overview

The **IRF520 MOSFET Driver Module** is a widely used power switching breakout board included in Arduino starter kits (Elegoo, SunFounder, Keyes). It allows 3.3V or 5V microcontrollers to control high-power DC loads—such as 12V LED strips, 24V solenoids, DC motors, Peltier coolers, and heating elements—over a single digital PWM signal pin.

The module incorporates an **IRF520 N-channel power MOSFET** in a TO-220 package, onboard gate drive support components, power status LEDs, and two 2-pin screw terminal blocks (one for external load power supply input, and one for the load output connection).

## Quick reference

| | |
|---|---|
| **Control signal voltage (`SIG`)** | 3.3 V to 5.0 V DC (Microcontroller GPIO logic level) |
| **Output load voltage (`VIN`)** | 0.0 V to 24.0 V DC |
| **Max continuous load current** | Up to $1.0\text{ A}$ (without heatsink) / Up to $5.0\text{ A}$ (with heatsink) |
| **Switching type** | Low-side N-Channel MOSFET switching (sinks load negative to GND) |
| **PWM frequency range** | 0 Hz to 20 kHz PWM speed control |
| **Connectors** | 3-pin 0.1" logic header + 2 screw terminal blocks |

## Module Interface & Terminal Layout

```
         Logic Header Pinout          Screw Terminal Block
            ┌─────────┐                ┌─────────────────┐
        SIG │ 1   (o) │                │ VIN (+)  GND (-)│ Power Supply Input (0-24V)
        VCC │ 2   (o) │                ├─────────────────┤
        GND │ 3   (o) │                │ V+  (+)  V-  (-)│ Load Output Connection
            └─────────┘                └─────────────────┘
```

### 3-Pin Logic Header

| Pin Label | Name | Type | Description |
|---|---|---|---|
| `SIG` | Digital Signal | Digital Input | Microcontroller GPIO pin (3.3V / 5V PWM logic input) |
| `VCC` | Power (Optional)| Power | Auxiliary power connection (NC or 5V rail) |
| `GND` | Ground | Power | Microcontroller ground reference (0 V) |

### Screw Terminals

| Terminal Label | Function | Description |
|---|---|---|
| `VIN` (`+` / `-`) | External Power Input | Connect external DC power supply ($0\text{V}$ to $24\text{V}$ DC) |
| `V+` / `V-` | Load Output | Connect load device (DC Motor, LED Strip, Solenoid) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Signal Voltage | $V_{SIG}$ | 3.3 | 5.0 | 5.5 | V | MCU logic HIGH |
| Load Voltage Range | $V_{LOAD}$| 0.0 | 12.0 | 24.0 | V | External supply voltage |
| Continuous Load Current (Uncooled)| $I_{load1}$| — | 1.0 | 1.5 | A | $V_{SIG} = 5.0\text{V}$, no heatsink |
| Max Load Current (Heatsinked) | $I_{load2}$| — | 3.5 | 5.0 | A | $V_{SIG} = 5.0\text{V}$, aluminum heatsink |
| Peak Pulsed Drain Current | $I_{DM}$ | — | — | 9.2 | A | $<300\ \mu\text{s}$ pulse |
| Static $R_{DS(on)}$ at 5V Gate | $R_{DS}$ | — | 0.27 | 0.40 | Ω | $V_{GS} = 5.0\text{V}$ |
| Module Weight | $W$ | — | 10.0 | — | g | PCB with terminals |

## Internal Schematic Circuit

```
  SIG ────[ 1kΩ ]────┬─── Gate (IRF520)
                     │
                  [10kΩ] (Pull-Down to GND)
                     │
  GND ───────────────┴─── Source (IRF520) ────── VIN (-) Ground
                               │
                             Drain (IRF520) ──── V- Output Terminal
```

- When `SIG` is High ($5\text{V}$), the IRF520 turns on, pulling terminal `V-` down to `GND`, completing the circuit for the connected load.
- Terminal `V+` is connected directly to `VIN (+)` on the PCB trace.

## Wiring (12V LED Strip / DC Motor Control)

| Module Connection | → | Target Device | Notes |
|---|---|---|---|
| Header `SIG` | | Arduino Digital D3 (PWM) | PWM dimming / speed control pin |
| Header `GND` | | Arduino GND | Shared common ground |
| Terminal `VIN (+)`| | +12V Power Supply Positive | External load power |
| Terminal `VIN (-)`| | +12V Power Supply Negative | External load ground |
| Terminal `V+` | | LED Strip Positive / Motor Red | Power output terminal |
| Terminal `V-` | | LED Strip Negative / Motor Black| Switched ground output terminal |

## Example (Arduino AnalogWrite PWM Speed Control)

```cpp
const int mosfetSigPin = 3; // PWM output pin

void setup() {
  pinMode(mosfetSigPin, OUTPUT);
}

void loop() {
  // Ramp PWM brightness/speed from 0% to 100%
  for (int pwmVal = 0; pwmVal <= 255; pwmVal += 5) {
    analogWrite(mosfetSigPin, pwmVal);
    delay(30);
  }

  delay(1000);

  // Ramp down
  for (int pwmVal = 255; pwmVal >= 0; pwmVal -= 5) {
    analogWrite(mosfetSigPin, pwmVal);
    delay(30);
  }

  delay(1000);
}
```

## Common mistakes

- **Drawing $>1.5\text{A}$ continuously without a heatsink:** Because the onboard IRF520 is a standard-gate MOSFET ($R_{DS(on)} \approx 0.27\ \Omega$ at $5\text{V}$ gate drive), running $>1.5\text{A}$ dissipates $>0.6\text{ Watts}$ of heat on the TO-220 tab. Attach an aluminum heatsink for currents $>1.5\text{A}$.
- **Attempting to switch AC mains:** The IRF520 is a DC-only N-channel MOSFET. Attempting to switch 120V/230V AC mains power will destroy the module. Use a relay module or SSR for AC loads.

## Notes

- **IRF520 Module vs Relay Module:** The IRF520 module supports fast PWM speed/brightness control without mechanical clicking; relays support AC loads but cannot perform fast PWM.
