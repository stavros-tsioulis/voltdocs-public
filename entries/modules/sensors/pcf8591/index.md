## Overview

The **PCF8591** is a single-chip 8-bit CMOS data acquisition IC manufactured by NXP Semiconductors. It integrates four single-ended (or two differential) 8-bit analog inputs, one 8-bit Digital-to-Analog converter (DAC) output, an internal track-and-hold circuit, and a standard $I^2C$ bus interface.

Standard blue PCB breakout modules bundle the PCF8591 alongside three onboard analog components: an NTC thermistor, a photoresistor (LDR), and a trimmer potentiometer connected to `AIN0`–`AIN2` via removable jumpers. It is widely used in beginner Raspberry Pi and Arduino projects to learn analog-to-digital and digital-to-analog conversion over $I^2C$.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 2.5 V to 6.0 V DC |
| **ADC resolution** | 8-bit (256 discrete levels) |
| **ADC channels** | 4 single-ended, 2 differential, or mixed |
| **DAC resolution** | 8-bit (1 analog voltage output pin `AOUT`) |
| **Interface** | $I^2C$ (Standard 100 kHz) |
| **Default $I^2C$ address** | `0x48` (3 hardware address pins $A_0, A_1, A_2 \to \text{GND}$) |
| **Operating current** | $250\ \mu\text{A}$ active / $10\ \mu\text{A}$ standby |

## Pinout

Common 4-pin $I^2C$ + 4-pin Analog breakout header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+2.5 V to +6.0 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 4 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 5 | `AIN0` | Analog Input | Analog Channel 0 (connected to LDR on module jumper P5) |
| 6 | `AIN1` | Analog Input | Analog Channel 1 (connected to Thermistor on jumper P4) |
| 7 | `AIN2` | Analog Input | Analog Channel 2 (connected to Potentiometer on jumper P6) |
| 8 | `AIN3` | Analog Input | Analog Channel 3 (free external analog input) |
| 9 | `AOUT` | Analog Output | 8-bit DAC output voltage pin |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.5 | 3.3 / 5.0 | 6.0 | V | DC |
| Reference Voltage | $V_{AGND} \dots V_{REF}$ | $V_{SS}$ | — | $V_{DD}$ | V | Analog reference range |
| ADC Conversion Time | $t_{conv}$ | — | 90 | — | µs | Limited by $I^2C$ clock speed |
| ADC Non-Linearity | $E_L$ | -1 | $\pm 0.5$ | +1 | LSB | 8-bit resolution |
| DAC Slew Rate | $SR_{dac}$ | — | 100 | — | V/ms | Full-scale step output |
| DAC Load Resistance | $R_L$ | 10 | — | — | kΩ | Connected to `AOUT` |

## Control Byte & Protocol

The PCF8591 uses a single control byte sent immediately following the $I^2C$ device address (`0x48`):

- **Bit 7:** Always 0.
- **Bit 6:** `ANALOG OUTPUT ENABLE` (1 = DAC `AOUT` output enabled, 0 = High impedance).
- **Bits 5–4:** Analog Input Programming Mode (`00` = 4 single-ended inputs).
- **Bit 3:** Always 0.
- **Bit 2:** Auto-increment flag (1 = automatically cycle through `AIN0`–`AIN3` on sequential reads).
- **Bits 1–0:** Channel Select (`00` = AIN0, `01` = AIN1, `10` = AIN2, `11` = AIN3).

$$ V_{AIN} = \frac{\text{Byte Value}}{255} \times V_{CC} $$

$$ V_{AOUT} = \frac{\text{DAC Write Byte}}{255} \times V_{CC} $$

## Wiring

| PCF8591 Pin | → | Arduino / Raspberry Pi | Notes |
|---|---|---|---|
| `VCC` | | 5V / 3.3V | Match logic level of host MCU |
| `GND` | | GND | System ground |
| `SDA` | | A4 / GPIO 2 (SDA) | $I^2C$ Data |
| `SCL` | | A5 / GPIO 3 (SCL) | $I^2C$ Clock |

## Example

```cpp
#include <Wire.h>

#define PCF8591_ADDRESS 0x48

void setup() {
  Serial.begin(9600);
  Wire.begin();
}

void loop() {
  // Enable DAC output and read AIN0 (Channel 0)
  Wire.beginTransmission(PCF8591_ADDRESS);
  Wire.write(0x40); // 0x40 = Enable DAC (bit 6), read AIN0
  Wire.write(128);  // Set DAC AOUT to mid-rail (~2.5V)
  Wire.endTransmission();

  Wire.requestFrom(PCF8591_ADDRESS, 2);
  Wire.read(); // First byte returned is previous conversion result; discard
  uint8_t adcValue = Wire.read();

  float voltage = (adcValue / 255.0) * 5.0;
  Serial.print("AIN0 ADC: "); Serial.print(adcValue);
  Serial.print(" | Voltage: "); Serial.print(voltage); Serial.println(" V");

  delay(500);
}
```

## Common mistakes

- **Discarding first $I^2C$ read byte:** The PCF8591 uses a pipelined conversion architecture. When reading a channel over $I^2C$, the first byte returned is the *previous* channel sample. Always discard the first byte or issue two sequential reads.
- **Forgetting jumper removal for external signals:** On standard blue modules, jumpers P4, P5, and P6 hardwire `AIN0`–`AIN2` to the onboard sensors. To read external analog voltages on `AIN0`–`AIN2`, remove the corresponding shunt jumper.

## Notes

- **PCF8591 vs ADS1115:** PCF8591 is 8-bit (256 steps) with DAC output; ADS1115 is 16-bit (65,536 steps) precision ADC without DAC.
