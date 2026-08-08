## Overview

The **MAX6675** is a classic cold-junction-compensated K-type thermocouple-to-digital converter IC manufactured by Maxim Integrated (Analog Devices). Bundled in low-cost 3D printer hotend kits (Marlin firmware), ceramics kilns, and Arduino electronics kits, it measures high temperatures from **$0^\circ\text{C}$ to $+1024^\circ\text{C}$** ($32^\circ\text{F}$ to $1875^\circ\text{F}$).

Integrating a 12-bit Analog-to-Digital Converter (ADC), cold-junction compensation diode, open-thermocouple detection circuitry, and a simple read-only **3-wire SPI interface (`CS`, `SCK`, `SO`)**, the MAX6675 converts thermocouple microvolt signals into $0.25^\circ\text{C}$ digital temperature steps.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.0 V to 5.5 V DC (5.0 V nominal) |
| **Interface** | SPI Read-Only (3-wire: `CS`, `SCK`, `SO` / `MISO`) |
| **Supported Thermocouple** | K-Type (Chromel-Alumel) |
| **Probe Temperature Range**| $0^\circ\text{C}\text{ to }+1024^\circ\text{C}$ |
| **ADC Resolution** | 12-bit ($0.25^\circ\text{C}$ resolution per LSB) |
| **Conversion Time** | 220 ms maximum per sample |
| **Cold-Junction Compensation**| $-20^\circ\text{C}\text{ to }+85^\circ\text{C}$ ($\pm 3.0^\circ\text{C}$ accuracy) |
| **Open Thermocouple Detection**| Bit 2 of 16-bit SPI frame sets to 1 if probe disconnected |

## Pinout

Breakout module 5-pin header & 2-pin screw terminal block:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply power input (+3.0 V to +5.5 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `SO` / `MISO` | Digital Output | SPI Serial Data Output |
| 4 | `CS` | Digital Input | Active-Low SPI Chip Select |
| 5 | `SCK` | Digital Input | SPI Serial Clock |
| `+` / `-` | Screw Terminals | Analog Input | Thermocouple lead wire terminals (Yellow = `+`, Red = `-`) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 3.0 | 5.0 | 5.5 | V | DC |
| Active Supply Current | $I_{CC}$ | — | 0.7 | 1.5 | mA | Continuous conversion |
| Cold-Junction Temp Error | $T_{CJ\_err}$| -3.0 | $\pm 3.0$ | +3.0 | °C | $T_{ambient} = 25^\circ\text{C}$ |
| Thermocouple Conversion | $T_{conv}$ | 0 | — | 1024 | °C | Full scale reading |
| LSB Resolution | $LSB_{temp}$| — | 0.25 | — | °C | $1/4^\circ\text{C}$ |
| Conversion Time | $t_{conv}$ | — | 170 | 220 | ms | Interval between conversions |

## 16-Bit SPI Telemetry Protocol

To read data, drive `CS` Low and supply 16 clock pulses on `SCK`:

- **Bit 15:** Dummy sign bit (Always `0`).
- **Bits 14–3 (12 bits):** **Thermocouple 12-bit unsigned temperature data ($0.25^\circ\text{C}$ per LSB).**
- **Bit 2:** Open-Thermocouple Detection Flag ($1 = \text{Probe Disconnected}$, $0 = \text{Normal}$).
- **Bit 1:** Device ID bit (Always `0`).
- **Bit 0:** Three-state buffer flag.

### Temperature Calculation ($^\circ\text{C}$)

$$ \text{Temperature } (^\circ\text{C}) = \frac{\text{Raw 16-bit Word } \gg 3}{4.0} $$

## Wiring

| MAX6675 Pin | → | Arduino Uno | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `CS`  | | Digital D10 | GPIO 5 | SPI Chip Select |
| `SO` (MISO) | | Digital D12 | GPIO 19 | SPI Data Out |
| `SCK` (CLK)  | | Digital D13 | GPIO 18 | SPI Clock |

## Example (MAX6675 Arduino Library)

```cpp
#include "max6675.h"

int thermoSO  = 12; // MISO
int thermoCS  = 10; // CS
int thermoCLK = 13; // SCK

MAX6675 thermocouple(thermoCLK, thermoCS, thermoSO);

void setup() {
  Serial.begin(9600);
  Serial.println("MAX6675 Thermocouple Test");
  delay(500); // Wait for MAX6675 chip stabilization
}

void loop() {
  float tempC = thermocouple.readCelsius();
  float tempF = thermocouple.readFahrenheit();

  if (isnan(tempC)) {
    Serial.println("MAX6675 Error: Thermocouple probe disconnected!");
  } else {
    Serial.print("Probe Temp: "); Serial.print(tempC); Serial.print(" °C | ");
    Serial.print(tempF); Serial.println(" °F");
  }

  // MAX6675 conversion time requires 250ms delay between reads
  delay(300);
}
```

## Common mistakes

- **Polling faster than 220 ms:** The MAX6675 ADC requires **$220\text{ ms}$** to perform a single conversion. Polling the SPI interface faster than 4 Hz causes the IC to return duplicate old temperature readings.
- **Negative temperature measurement failure:** The MAX6675 cannot measure temperatures below $0^\circ\text{C}$. For sub-zero temperature monitoring (e.g. freezer telemetry), use the MAX31855 or MAX31856.

## Notes

- **MAX6675 vs MAX31855:** MAX6675 measures $0^\circ\text{C}$ to $+1024^\circ\text{C}$; MAX31855 measures $-270^\circ\text{C}$ to $+1372^\circ\text{C}$.
