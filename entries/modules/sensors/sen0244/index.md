## Overview

The **SEN0244** (DFRobot Gravity Analog TDS Sensor / Meter) is an analog water quality sensor designed for hydroponics, aquarium monitoring, swimming pool chemistry, and drinking water testing. It measures **Total Dissolved Solids (TDS)**—the total concentration of dissolved inorganic salts (calcium, magnesium, potassium, sodium) and organic matter expressed in **Parts Per Million (PPM)** or milligrams per liter (mg/L).

Built around an AC excitation signal generator circuit (which prevents electrochemical probe polarization and extends probe lifespan), the SEN0244 outputs a continuous **analog voltage ($0\text{V} \dots 2.3\text{V}$)** across a 3-pin DFRobot Gravity connector.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.5 V DC (3.3 V or 5.0 V nominal) |
| **Output voltage (`A`)** | $0.0\text{V}$ to $2.3\text{V}$ analog DC voltage |
| **Measurement Range** | $0\text{ to }1000\text{ PPM}$ ($mg/L$) |
| **Measurement Accuracy** | $\pm 10\%\ \text{F.S.}$ (at $25^\circ\text{C}$) |
| **Probe Excitation** | AC square wave signal (anti-polarization) |
| **Waterproof Probe** | 2-needle black submersible IP68 probe ($60\text{ cm}$ cable) |
| **Operating current** | $3.0\text{ mA} \dots 6.0\text{ mA}$ |

## Pinout

Breakout board 3-pin 0.1" (2.54 mm) DFRobot Gravity connector:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 (`A`) | `SIGNAL` | Analog Output | $0\text{V} \dots 2.3\text{V}$ analog voltage output |
| 2 (`+`) | `VCC` | Power | Supply power input (+3.3 V to +5.5 V DC) |
| 3 (`-`) | `GND` | Power | Ground reference (0 V) |
| 2-Pin Terminal | `PROBE` | Analog Input | 2-pin JST connector for waterproof TDS probe |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 3.3 | 5.0 | 5.5 | V | DC |
| Active Supply Current | $I_{CC}$ | 3.0 | 4.5 | 6.0 | mA | Active measurement |
| Output Voltage Range | $V_{out}$ | 0.0 | — | 2.3 | V | $0 \dots 1000\text{ PPM}$ range |
| TDS Measurement Range| $TDS$ | 0 | — | 1000 | PPM | Parts Per Million (mg/L) |
| TDS Full-Scale Accuracy| $Acc_{TDS}$| -10.0 | $\pm 10.0$ | +10.0 | % F.S. | $T_{water} = 25^\circ\text{C}$ |
| Probe Cable Length | $Len$ | — | 60 | — | cm | Submersible probe cable |

## Temperature Compensation & TDS Math

TDS conductivity is highly temperature-dependent ($+2\%/^\circ\text{C}$ increase per degree Celsius).

1. **Calculate Temperature Compensation Factor ($TCF$):**

$$ TCF = 1.0 + 0.02 \times (T_{water} - 25.0) $$

2. **Calculate Compensated Voltage ($V_{comp}$):**

$$ V_{comp} = \frac{V_{raw}}{TCF} $$

3. **Calculate TDS Value (PPM):**

$$ \text{TDS (PPM)} = \left( 133.42 \cdot V_{comp}^3 - 255.86 \cdot V_{comp}^2 + 857.39 \cdot V_{comp} \right) \times 0.5 $$

## Wiring

| SEN0244 Pin | → | Arduino Uno | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` (`+`) | | 5V / 3.3V | 3.3V | Power rail |
| `GND` (`-`) | | GND | GND | System ground |
| `A` (`SIGNAL`)| | Analog Pin A0 | VP / GPIO36 | Analog voltage output |

## Example (Arduino Code with Temp Compensation)

```cpp
#define TdsSensorPin A0
#define VREF 5.0      // Analog reference voltage (5.0V or 3.3V)
#define SCOUNT  30    // Sum sample count for median filtering

int analogBuffer[SCOUNT];
int analogBufferTemp[SCOUNT];
int analogBufferIndex = 0, copyIndex = 0;
float averageVoltage = 0, tdsValue = 0, temperature = 25.0; // Water temp 25°C

void setup() {
  Serial.begin(115200);
  pinMode(TdsSensorPin, INPUT);
}

void loop() {
  static unsigned long sampleTimepoint = millis();
  if (millis() - sampleTimepoint > 40U) {
    sampleTimepoint = millis();
    analogBuffer[analogBufferIndex] = analogRead(TdsSensorPin);
    analogBufferIndex++;
    if (analogBufferIndex == SCOUNT) analogBufferIndex = 0;
  }

  static unsigned long printTimepoint = millis();
  if (millis() - printTimepoint > 800U) {
    printTimepoint = millis();
    for (copyIndex = 0; copyIndex < SCOUNT; copyIndex++) {
      analogBufferTemp[copyIndex] = analogBuffer[copyIndex];
    }
    averageVoltage = getMedianNum(analogBufferTemp, SCOUNT) * (float)VREF / 1024.0;
    
    // Temperature compensation formula
    float compensationCoefficient = 1.0 + 0.02 * (temperature - 25.0);
    float compensationVoltage = averageVoltage / compensationCoefficient;
    
    // Convert voltage to TDS value
    tdsValue = (133.42 * pow(compensationVoltage, 3) - 255.86 * pow(compensationVoltage, 2) + 857.39 * compensationVoltage) * 0.5;

    Serial.print("Voltage: "); Serial.print(averageVoltage, 2); Serial.print(" V | ");
    Serial.print("TDS Value: "); Serial.print(tdsValue, 0); Serial.println(" PPM");
  }
}

int getMedianNum(int bArray[], int iFilterLen) {
  int i, j, bTemp;
  for (j = 0; j < iFilterLen - 1; j++) {
    for (i = 0; i < iFilterLen - j - 1; i++) {
      if (bArray[i] > bArray[i + 1]) {
        bTemp = bArray[i];
        bArray[i] = bArray[i + 1];
        bArray[i + 1] = bTemp;
      }
    }
  }
  return bArray[(iFilterLen - 1) / 2];
}
```

## Common mistakes

- **Submerging the entire probe connector:** Only the black needle tip of the TDS probe is IP68 waterproof. The 2-pin JST connector cap and signal adapter PCB must remain dry.
- **Forgetting temperature compensation:** Reading $20^\circ\text{C}$ water without temperature compensation introduces a $-10\%$ error in calculated PPM.

## Notes

- **TDS vs EC (Electrical Conductivity):** $1\text{ ms/cm EC} \approx 500\text{ PPM TDS}$ (using standard 0.5 conversion factor).
