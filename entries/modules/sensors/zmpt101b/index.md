## Overview

The **ZMPT101B** module is an active single-phase AC voltage measurement sensor designed to safely step down high-voltage mains AC ($100\text{V}$ to $250\text{V}$ RMS) into a low-voltage analog sine wave suitable for microcontroller ADC inputs.

The module incorporates a precision micro current-type voltage transformer (ZMPT101B, 1:1 ratio) that provides galvanic isolation up to **$4000\text{V}$ AC** between the mains grid and low-voltage logic circuits. An onboard LM358 operational amplifier circuit adds a $\frac{V_{CC}}{2}$ DC offset bias ($2.5\text{V}$ at 5V supply) and amplification potentiometer adjustment, allowing microcontrollers to sample true AC waveforms and compute RMS voltage.

## Quick reference

| | |
|---|---|
| **Module supply voltage (`VCC`)** | 5.0 V DC nominal (4.5 V to 5.5 V) |
| **AC input voltage range** | 0 V to 250 V AC RMS (50 Hz / 60 Hz) |
| **Galvanic isolation rating** | 4000 V AC |
| **Output signal** | Analog AC sine wave centered at $\frac{V_{CC}}{2}$ ($2.5\text{V}$) |
| **Transformer ratio** | 1000 : 1000 ($2\text{ mA}$ rated primary/secondary current) |
| **Onboard adjustment** | Multi-turn trimmer potentiometer for output gain calibration |

## Terminals

### High-Voltage Mains Terminals (2-pin Screw Terminal)

| Pin | Signal | Description |
|---|---|---|
| `L` | AC Live | Connect to mains Live wire ($100\text{V}$ to $250\text{V}$ AC) |
| `N` | AC Neutral | Connect to mains Neutral wire |

### Low-Voltage Control Header (4-pin 0.1" Header)

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply input (+5.0 V DC) |
| 2 | `OUT` / `OUT1` | Analog Output | Analog AC output voltage centered at 2.5 V |
| 3 | `NC` / `OUT2` | Unused | Duplicate ground or unconnected pin |
| 4 | `GND` | Power | System ground (0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 4.5 | 5.0 | 5.5 | V | DC |
| AC Input Voltage Range | $V_{in\_AC}$ | 0 | 230 | 250 | V RMS | 50 Hz / 60 Hz mains |
| Rated Primary Current | $I_{pri}$ | — | 2.0 | 2.0 | mA | Through internal limiting resistor |
| Rated Secondary Current | $I_{sec}$ | — | 2.0 | 2.0 | mA | Transformer output |
| Dielectric Strength | $V_{iso}$ | 4000 | — | — | V AC | Isolation barrier |
| DC Offset Voltage | $V_{offset}$ | 2.4 | 2.5 | 2.6 | V | $V_{CC} = 5.0\text{ V}$ |
| Phase Error | $\phi$ | — | $\le 20$ | — | min | At $50\text{ Hz}$ ($2\text{ mA}$) |
| Operating Temperature | $T_{opr}$ | -40 | — | 70 | °C | Ambient |

## Sampling & RMS Calculation

The `OUT` pin produces an analog sine wave oscillating around $2.5\text{V}$. To calculate true Root-Mean-Square ($V_{RMS}$) voltage:

1. **High-Frequency Sampling:** Sample the `OUT` analog pin over 1–2 complete mains cycles ($20\text{ ms}$ for 50 Hz, $16.6\text{ ms}$ for 60 Hz), taking at least 100–200 ADC readings.
2. **DC Bias Subtraction:** Subtract the DC mid-rail offset ($ADC_{zero} \approx 512$ for 10-bit ADC at 5V) from each reading: $v[i] = ADC[i] - ADC_{zero}$.
3. **Square & Average:** Compute the mean of squared samples: $V_{mean\_sq} = \frac{1}{N} \sum v[i]^2$.
4. **Scale Factor:** Multiply $\sqrt{V_{mean\_sq}}$ by the calibrated gain constant ($K_{cal}$):

$$ V_{RMS} = K_{cal} \times \sqrt{ \frac{1}{N} \sum_{i=1}^{N} \left( ADC[i] - ADC_{zero} \right)^2 } $$

## Wiring

| ZMPT101B Pin | → | Arduino (5V ADC) | ESP32 (3.3V ADC) | Notes |
|---|---|---|---|---|
| `VCC` | | 5V | 5V (or 3.3V) | Powers LM358 op-amp |
| `GND` | | GND | GND | System ground |
| `OUT` | | Analog Pin A0 | VP / GPIO36 (ADC1) | **Use voltage divider on 3.3V ADCs** |

> [!WARNING]
> High Voltage Safety & ESP32 ADC Warning:
> - The blue screw terminal block connects directly to 230V AC mains. Ensure proper insulating enclosure protection.
> - At 5V supply, peak-to-peak output voltage on `OUT` can swing from $0.5\text{V}$ to $4.5\text{V}$. When connecting to a 3.3V ADC (such as ESP32), adjust the onboard trimmer potentiometer down so peak output voltage does not exceed $3.3\text{V}$, or power the module from 3.3V.

## Example

```cpp
const int sensorPin = A0;
const float calibrationFactor = 0.525; // Adjust based on multimeter reading

void setup() {
  Serial.begin(9600);
}

void loop() {
  long sumSquare = 0;
  int sampleCount = 0;
  unsigned long startTime = millis();

  // Sample over 200 ms (10 full 50 Hz AC cycles)
  while (millis() - startTime < 200) {
    int raw = analogRead(sensorPin);
    int zeroCentered = raw - 512; // Subtract 2.5V DC offset
    sumSquare += (long)zeroCentered * zeroCentered;
    sampleCount++;
  }

  float meanSquare = (float)sumSquare / sampleCount;
  float rmsADC = sqrt(meanSquare);
  float voltageRMS = rmsADC * calibrationFactor;

  Serial.print("Sampled: "); Serial.print(sampleCount);
  Serial.print(" | AC Voltage: "); Serial.print(voltageRMS); Serial.println(" V RMS");

  delay(1000);
}
```

## Common mistakes

- **Single-sample `analogRead()`:** Taking a single instantaneous sample of an AC sine wave yields random values between 0V and 250V depending on where in the 50 Hz cycle the ADC triggers. Always compute RMS over complete periods.
- **Forgetting potentiometer gain calibration:** Fresh ZMPT101B modules ship with uncalibrated potentiometer positions. Use a multimeter to measure mains AC voltage and adjust the blue trimmer resistor until your code matches the multimeter reading.

## Notes

- **ZMPT101B vs Resistor Dividers:** ZMPT101B provides $4000\text{V}$ magnetic isolation; direct resistor voltage dividers connect mains AC directly to microcontroller ground, creating severe shock and equipment hazards.
