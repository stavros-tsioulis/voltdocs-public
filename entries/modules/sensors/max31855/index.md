## Overview

The **MAX31855** is a cold-junction compensated thermocouple-to-digital converter manufactured by Maxim Integrated (Analog Devices). Designed to interface with K-Type (and J, N, R, S, T, E variant) thermocouples, it measures extreme temperatures ranging from **$-270^\circ\text{C}$ to $+1372^\circ\text{C}$** in kilns, 3D printer hotends, ovens, and automotive exhaust systems.

Integrating a 14-bit Signed ADC, internal cold-junction temperature compensation sensor, open-thermocouple / short-circuit fault detection, and a read-only **SPI interface (up to 5 MHz)**, the MAX31855 outputs temperature data in $0.25^\circ\text{C}$ resolution steps over a 32-bit SPI telemetry frame.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VIN`)** | 3.3 V to 5.0 V DC (breakout includes 3.3V LDO regulator) |
| **IC supply voltage (`VDD`)** | 3.0 V to 3.6 V DC (3.3 V nominal) |
| **Interface** | SPI Read-Only (3-wire interface: `CS`, `SCK`, `SO` / `MISO`) |
| **Supported Thermocouple** | K-Type (Chromel-Alumel) standard variant (`MAX31855K`) |
| **Probe Temperature Range**| $-270^\circ\text{C}\text{ to }+1372^\circ\text{C}$ |
| **ADC Resolution** | 14-bit Signed ($0.25^\circ\text{C}$ LSB resolution) |
| **Cold-Junction Range & Acc**| $-40^\circ\text{C}\text{ to }+125^\circ\text{C}$ ($\pm 2.0^\circ\text{C}$ accuracy) |
| **Fault Detection** | Detects open thermocouple, short to GND, and short to VCC |

## Pinout

Breakout module 5-pin header & 2-pin screw terminal block:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VIN` | Power | Supply power input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `DO` / `SO` | Digital Output | SPI Serial Data Output (MISO) |
| 4 | `CS` | Digital Input | Active-Low SPI Chip Select |
| 5 | `CLK` / `SCK` | Digital Input | SPI Serial Clock |
| `+` / `-` | Screw Terminals | Analog Input | Thermocouple lead wire terminals (Yellow = `+`, Red = `-`) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{VIN}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with LDO |
| Active Supply Current | $I_{CC}$ | — | 1.5 | 2.5 | mA | SPI clock active |
| Thermocouple Accuracy | $T_{err}$ | -2.0 | $\pm 2.0$ | +2.0 | °C | Probe temp $0^\circ\text{C} \dots 700^\circ\text{C}$ |
| ADC Resolution | $Res_{ADC}$| — | 14 | — | bits | Signed 14-bit output ($0.25^\circ\text{C}$ step) |
| SPI Clock Frequency | $f_{CLK}$ | 0 | — | 5.0 | MHz | Read-only SPI transfer |
| Conversion Time | $t_{conv}$ | — | 100 | 140 | ms | Conversion interval |

## 32-Bit SPI Telemetry Frame Structure

When `CS` goes Low, 32 bits of data are clocked out on `SO` on the falling edges of `SCK`:

- **Bits 31–18 (14 bits):** Thermocouple 14-bit signed temperature data ($0.25^\circ\text{C}$ resolution).
- **Bit 16:** Fault flag ($1 = \text{Fault present}$).
- **Bits 15–4 (12 bits):** Internal cold-junction reference temperature data ($0.0625^\circ\text{C}$ resolution).
- **Bit 2:** Short to $V_{CC}$ fault flag.
- **Bit 1:** Short to GND fault flag.
- **Bit 0:** Open Circuit (Thermocouple Disconnected) fault flag.

### Temperature Calculation ($^\circ\text{C}$)

$$ \text{Thermocouple Temp } (^\circ\text{C}) = \frac{\text{Bits 31..18 Signed 14-Bit Integer}}{4.0} $$

## Wiring

| MAX31855 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VIN` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `CS`  | | Digital D10 | GPIO 5 | SPI Chip Select |
| `DO` (MISO) | | Digital D12 | GPIO 19 | SPI MISO / Data Out |
| `CLK` (SCK) | | Digital D13 | GPIO 18 | SPI Clock |

## Example (Adafruit_MAX31855 Library)

```cpp
#include <SPI.h>
#include "Adafruit_MAX31855.h"

#define MAXDO   19
#define MAXCS   5
#define MAXCLK  18

// Software SPI initialization
Adafruit_MAX31855 thermocouple(MAXCLK, MAXCS, MAXDO);

void setup() {
  Serial.begin(115200);
  Serial.println("Adafruit MAX31855 Thermocouple Test");
  delay(500);
}

void loop() {
  double c = thermocouple.readCelsius();

  if (isnan(c)) {
    uint8_t e = thermocouple.readError();
    if (e & MAX31855_FAULT_OPEN) Serial.println("FAULT: Thermocouple is OPEN (Disconnected)!");
    if (e & MAX31855_FAULT_SHORT_GND) Serial.println("FAULT: Thermocouple shorted to GND!");
    if (e & MAX31855_FAULT_SHORT_VCC) Serial.println("FAULT: Thermocouple shorted to VCC!");
  } else {
    Serial.print("Probe Temperature: "); Serial.print(c); Serial.println(" °C");
  }

  delay(1000);
}
```

## Common mistakes

- **Inverting K-type wire polarity:** K-Type thermocouple leads use ANSI color codes (**Yellow = Positive `+`**, **Red = Negative `-`**). Connecting Red to `+` causes temperature readings to drop when the probe is heated.
- **Grounded thermocouple probe shorts:** Standard non-insulated metal braid thermocouples can short to grounded metal frames, triggering the `SHORT TO GND` fault bit. Use insulated probe sheaths.

## Notes

- **MAX31855 vs MAX6675 vs MAX31856:** MAX6675 is older (0°C to 1024°C only); MAX31855 supports negative temperatures (-270°C to +1372°C); MAX31856 supports all thermocouple types (K, J, N, R, S, T, E, B) via SPI write commands.
