## Overview

The **Capacitive Soil Moisture Sensor (v1.2 / v2.0)** is an analog soil moisture probe designed to overcome the rapid electrode oxidation and electrolysis corrosion that plague traditional resistive soil sensors (like the YL-69 / FC-28). 

Instead of passing direct electric current through the soil, the module forms a coplanar capacitive element using insulated copper traces embedded within the fiberglass PCB probe. An onboard 555 timer IC (typically the low-power CMOS TL555I or NE555) generates a high-frequency square wave (~1.5 MHz). As soil moisture increases, the dielectric constant ($\epsilon_r$) of the surrounding soil rises significantly (water $\approx 80$ vs dry soil $\approx 3-5$), changing the capacitance and producing an analog output voltage that decreases inversely with moisture levels.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.5 V DC |
| **Output signal** | Analog DC voltage ($1.2\text{ V}$ wet to $3.0\text{ V}$ dry at 3.3V supply) |
| **Operating current** | ~5 mA |
| **Sensing principle** | High-frequency capacitive dielectric measurement |
| **Probe dimensions** | 98 mm × 23 mm (insertion depth ~70 mm) |
| **Connector** | 3-pin PH2.0 or 0.1" (2.54 mm) header |

## Terminals

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` | Power | Ground (0 V) |
| 2 | `VCC` | Power | Supply voltage (+3.3 V to +5.5 V DC) |
| 3 | `AOUT` | Analog Output | Analog voltage proportional to inverse moisture content |

## Electrical specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 3.3 | 5.0 | 5.5 | V | DC supply |
| Operating Current | $I_{CC}$ | 3.0 | 5.0 | 8.0 | mA | $V_{CC} = 5.0\text{ V}$ |
| Output Voltage (Air / Dry Soil) | $V_{dry}$ | 2.8 | 3.0 | 4.2 | V | Air reference ($V_{CC}=5.0\text{V}$) |
| Output Voltage (Saturated Water) | $V_{wet}$ | 1.0 | 1.2 | 1.5 | V | Fully submerged in water |
| Oscillator Frequency | $f_{osc}$ | 1.0 | 1.5 | 2.0 | MHz | Onboard 555 timer circuit |
| Operating Temperature | $T_{opr}$ | -10 | — | 50 | °C | Non-condensing |

## Operating principle & calibration

1. **Inverse Voltage Relationship:** Unlike resistive sensors, **higher moisture results in LOWER output voltage**. In air (0% moisture), the output is highest ($\approx 3.0\text{ V}$ at 3.3V supply); in pure water (100% saturation), the output is lowest ($\approx 1.2\text{ V}$).
2. **Two-Point Calibration:** Calibration requires recording two ADC values for each individual sensor:
   - $ADC_{air}$: Sensor held in free air (0% moisture baseline).
   - $ADC_{water}$: Sensor submerged up to the white line in a cup of water (100% moisture baseline).

$$ \text{Moisture \%} = \frac{ADC_{air} - ADC_{raw}}{ADC_{air} - ADC_{water}} \times 100\% $$

## Wiring

| Sensor Pin | → | Arduino (5V Logic) | ESP32 (3.3V ADC) | Notes |
|---|---|---|---|---|
| `VCC` | | 5V (or 3.3V) | 3.3V | Match supply to MCU ADC reference voltage |
| `GND` | | GND | GND | System ground |
| `AOUT` | | Analog Pin A0 | VP / GPIO36 (ADC1) | Analog input pin |

> [!WARNING]
> Waterproofing notice:
> - Only insert the sensor into soil up to the white warning line marked on the PCB probe. 
> - The top electronics portion (containing the 555 timer IC, resistors, and header connector) is **not waterproof**. Exposing top components to rain or irrigation water will short the circuit. Apply heat-shrink tubing or conformal coating / hot glue over the top PCB edge for outdoor deployment.

## Example

```cpp
const int sensorPin = A0;

// Replace these values with your 2-point calibration readings
const int AirValue = 620;   // ADC reading in dry air (3.3V reference)
const int WaterValue = 310; // ADC reading in water cup

void setup() {
  Serial.begin(9600);
}

void loop() {
  int rawADC = analogRead(sensorPin);
  
  // Constrain ADC reading within calibrated bounds
  int constrainedADC = constrain(rawADC, WaterValue, AirValue);
  
  // Map inverse voltage to 0-100% moisture percentage
  int moisturePercent = map(constrainedADC, AirValue, WaterValue, 0, 100);

  Serial.print("Raw ADC: ");
  Serial.print(rawADC);
  Serial.print(" | Moisture: ");
  Serial.print(moisturePercent);
  Serial.println("%");

  delay(2000);
}
```

## Common mistakes

- **Assuming 0 V is dry and 5 V is wet:** Reversing the polarity interpretation leads to inverted readings (reporting 100% moisture in dry soil).
- **Powering from 5 V when reading with a 3.3 V ADC (ESP32 / STM32):** Supplying 5 V to $V_{CC}$ causes the $V_{dry}$ output to reach up to ~4.2 V, exceeding the 3.3 V maximum input limit of ESP32 GPIO pins. Always power from 3.3 V when using 3.3 V microcontrollers.
- **Submerging the top electronics:** Water contacting the 555 timer IC and surface-mount components alters the oscillator frequency or causes corrosion.
- **Clone resistor errors:** Some cheap v1.2 clones ship with an incorrect voltage regulator or missing zero-ohm resistor on the output buffer line. If output voltage stays constant regardless of moisture, inspect the R4/R5 surface-mount components near the connector.

## Notes

- **v1.2 vs v2.0:** Version 2.0 adds a reverse polarity diode protection and a 3.3V voltage regulator (such as XC6206) to ensure consistent readings even when supply voltage fluctuates between 3.3 V and 5 V.
