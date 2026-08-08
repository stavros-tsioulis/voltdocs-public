## Overview

The **YF-S201** is a popular 1/2-inch (DN15) inline liquid flow rate sensor widely used in smart irrigation systems, water dispensers, solar heating loops, and home automation water meters.

Housed in a durable black nylon body with standard 1/2" male parallel threads ($G1/2\text{"}$), the sensor contains a pinwheel turbine rotor embedded with a permanent magnet, separated from a digital Hall effect sensor. As water flows through the chamber, it spins the turbine, causing the magnet to pass by the Hall sensor and generate a **digital 50% duty-cycle square-wave pulse train** on the yellow signal wire. The output pulse frequency is directly proportional to water flow velocity ($1\text{ to }30\text{ L/min}$).

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 4.5 V to 18.0 V DC (5.0 V nominal) |
| **Max water pressure** | $\le 1.75\text{ MPa}$ ($17.5\text{ bar} / 253\text{ PSI}$) |
| **Flow rate range** | 1.0 L/min to 30.0 L/min ($\pm 3\%$ accuracy) |
| **Pulse characteristic ($F$)** | $F = 7.5 \times Q \quad (\text{where } Q = \text{L/min}, F = \text{Hz})$ |
| **Pulses per Liter** | $\approx 450\text{ pulses/Liter}$ |
| **Thread connection** | Standard 1/2" male parallel threads ($G1/2\text{"}$) |
| **Output type** | 5V TTL Open-Collector Square Wave (requires pull-up resistor) |
| **Operating current** | $15\text{ mA}$ at 5V supply |

## Pinout

3-wire color-coded 0.1" (2.54 mm) connector:

| Lead | Cable Color | Name | Type | Description |
|---|---|---|---|---|
| 1 | Red | `VCC` | Power | Supply voltage input (+4.5 V to +18.0 V DC) |
| 2 | Black | `GND` | Power | Ground reference (0 V) |
| 3 | Yellow | `SIGNAL` / `OUT` | Digital Output | Pulse frequency output pin (Active-Low pulses) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 4.5 | 5.0 | 18.0 | V | DC |
| Active Supply Current | $I_{CC}$ | — | 15 | 20 | mA | $V_{CC} = 5.0\text{ V}$ |
| Flow Rate Range | $Q$ | 1.0 | — | 30.0 | L/min | Clean water |
| Max Liquid Pressure | $P_{max}$ | — | — | 1.75 | MPa | Burst pressure test |
| Pulse Frequency Formula | $F$ | — | $7.5 \times Q$| — | Hz | $Q$ in Liters per minute |
| Output High Voltage | $V_{OH}$ | 4.5 | 4.8 | $V_{CC}$ | V | With $10\text{ k}\Omega$ pull-up to $V_{CC}$ |
| Output Low Voltage | $V_{OL}$ | 0.0 | 0.2 | 0.4 | V | $I_{sink} = 10\text{ mA}$ |
| Liquid Temp Range | $T_{water}$ | 0 | 25 | 80 | °C | Non-freezing liquid |

## Flow Calculation & Math

The relationship between pulse frequency ($F$ in Hz) and flow rate ($Q$ in L/min) is given by the empirical manufacturer calibration curve:

$$ F\text{ (Hz)} = 7.5 \times Q\text{ (L/min)} \implies Q\text{ (L/min)} = \frac{F}{7.5} $$

To compute flow rate and total volume (in Liters) over time:

1. **Flow Rate ($Q$):** Measure pulse count $N$ over a 1-second interval ($F = N\text{ pulses/sec}$):

$$ \text{Flow Rate (L/min)} = \frac{\text{Pulses per Second}}{7.5} $$

2. **Total Volume ($V$):** Each individual pulse corresponds to approximately $\frac{1}{450}\text{ Liters} \approx 2.22\text{ mL}$:

$$ \text{Total Volume (Liters)} = \frac{\text{Cumulative Pulse Count}}{450} $$

## Wiring

| YF-S201 Lead | → | Arduino Uno | ESP32 | Notes |
|---|---|---|---|---|
| Red (`VCC`) | | 5V | 5V | Power from 5V rail |
| Black (`GND`) | | GND | GND | System ground |
| Yellow (`SIGNAL`)| | Digital D2 (INT0) | GPIO 4 | **Requires $10\text{ k}\Omega$ pull-up to 3.3V/5V** |

> [!WARNING]
> Flow Direction & Horizontal Mounting:
> - Note the **arrow molded on the nylon housing** indicating the required water flow direction. Installing the sensor backwards causes inaccurate pulse counts.
> - Mount the sensor with the turbine axis horizontal to prevent air bubbles from trapping inside the chamber.

## Example

```cpp
const int flowPin = 2; // Interrupt 0 on Arduino Uno
volatile unsigned int pulseCount = 0;
float flowRateLmin = 0.0;
float totalLiters = 0.0;

void countPulse() {
  pulseCount++;
}

void setup() {
  Serial.begin(9600);
  pinMode(flowPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(flowPin), countPulse, RISING);
}

void loop() {
  pulseCount = 0;
  delay(1000); // Measure pulses for 1 second

  // Q (L/min) = Hz / 7.5
  flowRateLmin = (pulseCount / 7.5);
  // Volume added in 1 sec = Flow Rate / 60
  totalLiters += (flowRateLmin / 60.0);

  Serial.print("Flow Rate: "); Serial.print(flowRateLmin); Serial.print(" L/min");
  Serial.print(" | Total Volume: "); Serial.print(totalLiters); Serial.println(" L");
}
```

## Common mistakes

- **Testing with compressed air instead of liquid:** Spinning the dry turbine with compressed air over-speeds the nylon bearings and destroys the internal shaft.
- **Forgetting pull-up resistor:** The Hall sensor output is open-collector. Enable internal micro-controller pull-ups (`INPUT_PULLUP`) or add an external $10\text{ k}\Omega$ resistor.

## Notes

- **YF-S201 vs YF-S401:** YF-S201 is 1/2" DN15 ($1\text{--}30\text{ L/min}$); YF-S401 is 6mm micro-tubing ($0.3\text{--}6\text{ L/min}$).
