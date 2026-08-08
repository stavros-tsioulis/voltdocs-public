## Overview

The **PZEM-004T** (specifically Version 3.0) is a single-phase AC electrical energy monitoring module manufactured by Peacefair. Designed for safe, non-invasive AC power measurement, it pairs an onboard SD2004/V9881 metering IC with a Current Transformer (CT) coil—either a closed-core or open/split-core transformer—to calculate six electrical parameters: voltage, current, active power, total energy consumption, grid frequency, and power factor.

The module features internal optocouplers that provide **galvanic isolation** between high-voltage mains AC ($80\text{V}$ to $260\text{V}$) and the low-voltage 5 V TTL UART communication lines. It uses a standard Modbus-RTU serial protocol over UART (9,600 bps), making it widely deployed in ESPHome, Home Assistant, and Arduino whole-house energy monitor builds.

## Quick reference

| | |
|---|---|
| **Mains AC voltage range** | 80 V to 260 V AC (50 Hz / 60 Hz) |
| **Max AC current** | 100 A (with 100A external CT coil) or 10 A (internal shunt) |
| **Active power range** | 0 W to 23,000 W ($23\text{ kW}$) |
| **Energy accumulator** | 0 kWh to 99,999 kWh |
| **Interface** | Optocoupled 5 V TTL UART (9,600 bps, Modbus-RTU) |
| **Measurement accuracy** | Class 1.0 ($\pm 1.0\%$) |
| **Safety isolation** | Optocoupler isolation between mains AC and UART header |

## Terminals & Connection Blocks

### High-Voltage Mains Terminals (Screw Terminal Block)

| Pin | Signal | Description |
|---|---|---|
| `N` | AC Neutral | Connect to mains Neutral wire ($80\text{V}$ to $260\text{V}$ AC) |
| `L` | AC Live | Connect to mains Live wire |
| `CT1` | Current Transformer (+) | Connect to external CT transformer lead 1 |
| `CT2` | Current Transformer (-) | Connect to external CT transformer lead 2 |

### Low-Voltage Control Header (4-pin 0.1" Header)

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply input for UART optocoupler (+5.0 V DC) |
| 2 | `RX` | Digital Input | UART Receive data pin (connect to MCU TX) |
| 3 | `TX` | Digital Output | UART Transmit data pin (connect to MCU RX) |
| 4 | `GND` | Power | Low-voltage ground reference (0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| AC Voltage Range | $V_{AC}$ | 80.0 | 120 / 230 | 260.0 | V RMS | 45 Hz–65 Hz |
| AC Current Range | $I_{AC}$ | 0.01 | — | 100.0 | A RMS | 100A CT transformer |
| Active Power Range | $P_{active}$ | 0.0 | — | 23000 | W | Resolution 0.1 W |
| Power Factor Range | $PF$ | 0.00 | — | 1.00 | — | Resolution 0.01 |
| Grid Frequency | $f_{grid}$ | 45.0 | 50.0 / 60.0| 65.0 | Hz | Resolution 0.1 Hz |
| UART Baud Rate | $Baud$ | — | 9600 | — | bps | 8 data bits, 1 stop, no parity |
| Isolation Voltage | $V_{iso}$ | 2000 | — | — | V AC | Optocoupler rating |

## Modbus-RTU Protocol Overview

The PZEM-004T v3.0 uses Modbus-RTU over 9,600 baud serial. Default Modbus slave address is `0x01` (programmable from `0x01` to `0xF8`).

- **Read Input Registers:** Send `0x01 0x04 0x00 0x00 0x00 0x0A [CRC16]`.
- **Response Payload (10 Registers / 20 Bytes):**
  - Voltage (2 bytes, $/10 \to \text{Volts}$)
  - Current (4 bytes, $/1000 \to \text{Amperes}$)
  - Power (4 bytes, $/10 \to \text{Watts}$)
  - Energy (4 bytes, $/1 \to \text{Watt-hours}$)
  - Frequency (2 bytes, $/10 \to \text{Hz}$)
  - Power Factor (2 bytes, $/100 \to \text{PF}$)

## Wiring

| PZEM-004T Pin | → | ESP32 | Arduino (SoftwareSerial) | Notes |
|---|---|---|---|---|
| `VCC` | | 5V | 5V | Powers the TTL optocouplers |
| `GND` | | GND | GND | System ground |
| `TX`  | | GPIO 16 (RX2) | Digital D10 (Software RX) | 5V logic output |
| `RX`  | | GPIO 17 (TX2) | Digital D11 (Software TX) | 5V logic input |

> [!WARNING]
> High Voltage Safety Hazard:
> - The screw terminal block carries lethal **110V/230V mains AC voltage**.
> - Pass only **one** current-carrying conductor (either Live OR Neutral) through the hole of the Current Transformer (CT) coil. Passing both Live and Neutral through the CT simultaneously cancels the magnetic fields, resulting in 0.00 A current reading.

## Example

```cpp
#include <PZEM004Tv30.h>

// SoftwareSerial or HardwareSerial (e.g. Serial2 on ESP32)
PZEM004Tv30 pzem(Serial2, 16, 17); // RX=16, TX=17

void setup() {
  Serial.begin(115200);
}

void loop() {
  float voltage = pzem.voltage();
  float current = pzem.current();
  float power   = pzem.power();
  float energy  = pzem.energy();
  float pf      = pzem.pf();

  if (!isnan(voltage)) {
    Serial.print("Voltage: "); Serial.print(voltage); Serial.println(" V");
    Serial.print("Current: "); Serial.print(current); Serial.println(" A");
    Serial.print("Power: ");   Serial.print(power);   Serial.println(" W");
    Serial.print("Energy: ");  Serial.print(energy);  Serial.println(" kWh");
    Serial.print("PF: ");      Serial.println(pf);
  } else {
    Serial.println("Error reading PZEM-004T!");
  }

  delay(2000);
}
```

## Common mistakes

- **Looping both Live and Neutral through the CT coil:** Net magnetic flux equals zero; current reads 0.00 A.
- **Conflating v1.0 and v3.0 modules:** Legacy PZEM-004T v1.0 used a custom ASCII protocol at 9,600 baud. Version 3.0 uses Modbus-RTU commands. Modern software libraries (ESPHome `pzemac`) require v3.0.
- **Forgetting `VCC` supply to 4-pin header:** The UART optocouplers are powered from the 4-pin header `VCC`/`GND`. Leaving `VCC` un-powered prevents serial data transmission.

## Notes

- **Split-Core vs Solid-Core CT:** Split-core CT models feature a snap-open hinge, allowing installation around existing house wiring without disconnecting mains power circuits.
