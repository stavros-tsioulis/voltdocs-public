## Overview

The **MCP3208** is a 12-bit Analog-to-Digital Converter (ADC) IC manufactured by Microchip Technology. It features 8 single-ended input channels (or 4 pseudo-differential pairs), an internal successive-approximation register (SAR) architecture, and a 4-wire SPI serial interface.

Capable of sampling up to **100 kSPS** (kilosamples per second) at 5 V supply, the MCP3208 is widely used to add precise multi-channel analog input capabilities to single-board computers (such as the Raspberry Pi, which lacks native onboard ADCs) and to expand resolution on 10-bit microcontrollers (like the Arduino Uno).

## Quick reference

| | |
|---|---|
| **Supply voltage (`VDD`)** | 2.7 V to 5.5 V DC |
| **Resolution** | 12-bit (4,096 discrete steps) |
| **Channels** | 8 single-ended or 4 pseudo-differential pairs |
| **Sampling rate** | 100 kSPS (at 5.0 V) / 50 kSPS (at 2.7 V) |
| **Interface** | SPI (SPI Mode 0,0 and Mode 1,1) |
| **Reference voltage (`VREF`)** | $0.25\text{ V}$ to $V_{DD}$ |
| **Active current draw** | $400\ \mu\text{A}$ typical (at 5V) / $500\text{ nA}$ standby |

## Pin Configuration (DIP-16 / SOIC-16 Package)

```
             ┌───┴───┐
       CH0 ──┤ 1   16├─ VDD
       CH1 ──┤ 2   15├─ VREF
       CH2 ──┤ 3   14├─ AGND
       CH3 ──┤ 4   13├─ CLK
       CH4 ──┤ 5   12├─ DOUT
       CH5 ──┤ 6   11├─ DIN
       CH6 ──┤ 7   10├─ CS/SHDN
       CH7 ──┤ 8    9├─ DGND
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1–8 | `CH0`–`CH7` | Analog Input | Analog input channels 0 to 7 |
| 9 | `DGND` | Power | Digital Ground reference |
| 10 | `CS/SHDN` | Digital Input | Active-Low Chip Select & Shutdown |
| 11 | `DIN` | Digital Input | SPI Data Input (MOSI from MCU) |
| 21 | `DOUT` | Digital Output | SPI Data Output (MISO to MCU) |
| 13 | `CLK` | Digital Input | SPI Serial Clock |
| 14 | `AGND` | Power | Analog Ground reference |
| 15 | `VREF` | Analog Input | Voltage Reference input ($0.25\text{ V}$ to $V_{DD}$) |
| 16 | `VDD` | Power | Power supply (+2.7 V to +5.5 V DC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 2.7 | 3.3 / 5.0 | 5.5 | V | DC supply |
| Reference Voltage | $V_{REF}$ | 0.25 | — | $V_{DD}$ | V | Analog reference |
| Integral Nonlinearity | $INL$ | -1 | $\pm 0.75$ | +1 | LSB | $V_{DD} = V_{REF} = 5.0\text{ V}$ |
| Differential Nonlinearity | $DNL$ | -1 | $\pm 0.5$ | +1 | LSB | No missing codes |
| Clock Frequency ($V_{DD}=5\text{V}$) | $f_{CLK}$ | 0.01 | — | 2.0 | MHz | 100 kSPS max rate |
| Clock Frequency ($V_{DD}=2.7\text{V}$)| $f_{CLK}$ | 0.01 | — | 1.0 | MHz | 50 kSPS max rate |
| Conversion Time | $t_{conv}$ | — | 12 | 12 | clock cycles | After sampling acquisition |

## SPI Framing & Channel Selection

To sample a channel, the MCU pulls `CS` Low and transmits 3 command bytes over `DIN`:

- **Start Bit:** First logic High bit.
- **Single/Diff Selection (`S/D`):** High = Single-ended (8 channels), Low = Differential (4 channel pairs).
- **Channel Address (`D2`, `D1`, `D0`):** 3-bit channel select (`000` for CH0 up to `111` for CH7).

During transmission, the MCP3208 samples the analog channel and returns 12 data bits on `DOUT` ($D_{11}$ to $D_0$).

$$ V_{in} = \frac{\text{ADC Output Code}}{4096} \times V_{REF} $$

## Wiring

| MCP3208 Pin | → | Raspberry Pi GPIO | Arduino Uno | Notes |
|---|---|---|---|---|
| 16 (`VDD`) | | 3.3V / 5V | 5V | Decoupling cap $0.1\ \mu\text{F}$ required |
| 15 (`VREF`)| | 3.3V / 5V | 5V | Analog reference input rail |
| 14 (`AGND`)| | GND | GND | Connect to quiet analog ground |
| 9 (`DGND`) | | GND | GND | Digital system ground |
| 13 (`CLK`) | | GPIO 11 (SPI0_SCLK)| D13 | SPI Clock |
| 12 (`DOUT`)| | GPIO 9 (SPI0_MISO) | D12 | SPI MISO |
| 11 (`DIN`) | | GPIO 10 (SPI0_MOSI)| D11 | SPI MOSI |
| 10 (`CS`)   | | GPIO 8 (SPI0_CE0)  | D10 | Active-Low Chip Select |

## Example

```cpp
#include <SPI.h>

const int CS_PIN = 10;

uint16_t readADC(uint8_t channel) {
  uint8_t command = 0xC0 | ((channel & 0x07) << 3); // Start bit (1) + Single-ended (1) + D2 bit
  
  SPI.beginTransaction(SPISettings(1000000, MSBFIRST, SPI_MODE0));
  digitalWrite(CS_PIN, LOW);
  
  SPI.transfer(command);
  uint8_t b1 = SPI.transfer(((channel & 0x07) & 0x03) << 6); // Send D1, D0
  uint8_t b2 = SPI.transfer(0x00);
  
  digitalWrite(CS_PIN, HIGH);
  SPI.endTransaction();
  
  uint16_t result = ((b1 & 0x0F) << 8) | b2;
  return result; // 0 to 4095
}

void setup() {
  Serial.begin(9600);
  pinMode(CS_PIN, OUTPUT);
  digitalWrite(CS_PIN, HIGH);
  SPI.begin();
}

void loop() {
  uint16_t raw = readADC(0); // Read Channel 0
  float voltage = (raw / 4095.0) * 5.0;

  Serial.print("CH0 Raw: "); Serial.print(raw);
  Serial.print(" | Voltage: "); Serial.print(voltage); Serial.println(" V");

  delay(500);
}
```

## Common mistakes

- **Leaving `VREF` disconnected:** The chip requires an explicit reference voltage on pin 15. If left floating, ADC output codes will read 4095 continuously.
- **Forgetting `AGND` and `DGND` connection:** Both ground pins must be connected to 0V ground. Joining them at a single star-ground point near the chip eliminates digital switching noise on analog measurements.
- **Overclocking SPI at 3.3V supply:** At 2.7V–3.3V supply, maximum SPI clock rate drops from 2.0 MHz to 1.0 MHz. Running clock speeds $>1.0\text{ MHz}$ at 3.3V causes data bit errors on `DOUT`.

## Notes

- **MCP3008 vs MCP3208:** The MCP3008 is a 10-bit version (1,024 steps); the MCP3208 provides 12-bit resolution (4,096 steps) with the exact same pinout.
