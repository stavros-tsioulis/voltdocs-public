## Overview

The **MCP3008** is a low-cost 10-bit Analog-to-Digital Converter (ADC) IC manufactured by Microchip Technology. Featuring 8 single-ended input channels (programmable as 4 pseudo-differential pairs), an internal successive-approximation register (SAR) architecture, and a 4-wire SPI serial interface, it is the standard component recommended across Raspberry Pi ecosystem tutorials for reading analog sensors (such as potentiometers, photoresistors, thermistors, and joysticks).

Capable of sampling up to **200 kSPS** at 5.0 V supply (and **75 kSPS** at 2.7 V), the MCP3008 provides a reliable, low-power bridge between analog signals and digital microprocessors.

## Quick reference

| | |
|---|---|
| **Supply voltage (`VDD`)** | 2.7 V to 5.5 V DC |
| **Resolution** | 10-bit (1,024 discrete levels) |
| **Input channels** | 8 single-ended or 4 pseudo-differential pairs |
| **Max sampling rate** | 200 kSPS (at $V_{DD}=5.0\text{V}$) / 75 kSPS (at $V_{DD}=2.7\text{V}$) |
| **Interface** | SPI (Mode 0,0 and Mode 1,1) |
| **Reference voltage (`VREF`)** | $0.25\text{ V}$ to $V_{DD}$ |
| **Active supply current** | $425\ \mu\text{A}$ typical (at 5V) / $500\text{ nA}$ standby |

## Pinout (DIP-16 Package)

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
| 11 | `DIN` | Digital Input | SPI Data Input (MOSI) |
| 12 | `DOUT` | Digital Output | SPI Data Output (MISO) |
| 13 | `CLK` | Digital Input | SPI Serial Clock |
| 14 | `AGND` | Power | Analog Ground reference |
| 15 | `VREF` | Analog Input | Voltage Reference input ($0.25\text{ V}$ to $V_{DD}$) |
| 16 | `VDD` | Power | Power supply input (+2.7 V to +5.5 V DC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 2.7 | 3.3 / 5.0 | 5.5 | V | DC |
| Reference Voltage | $V_{REF}$ | 0.25 | — | $V_{DD}$ | V | Analog reference |
| Integral Nonlinearity | $INL$ | -1 | $\pm 0.5$ | +1 | LSB | $V_{DD} = V_{REF} = 5.0\text{ V}$ |
| Differential Nonlinearity | $DNL$ | -1 | $\pm 0.25$ | +1 | LSB | No missing codes |
| Clock Frequency ($V_{DD}=5\text{V}$) | $f_{CLK}$ | 0.01 | — | 3.6 | MHz | 200 kSPS rate |
| Clock Frequency ($V_{DD}=2.7\text{V}$)| $f_{CLK}$ | 0.01 | — | 1.35 | MHz | 75 kSPS rate |

## SPI Command Framing

To read an analog channel, the host MCU pulls `CS` Low and transmits 3 bytes over SPI (`DIN`):

1. **Byte 1:** `0x01` (Start Bit).
2. **Byte 2:** `0x80` | `(channel << 4)` (`0x80` = single-ended mode; bits 6–4 specify channel 0–7).
3. **Byte 3:** `0x00` (Dummy byte to clock out remaining data).

The MCP3008 returns 10 data bits on `DOUT`:

$$ V_{in} = \frac{\text{ADC Reading}}{1023} \times V_{REF} $$

## Wiring

| MCP3008 Pin | → | Raspberry Pi GPIO | Arduino Uno | Notes |
|---|---|---|---|---|
| 16 (`VDD`) | | 3.3V | 5V | $0.1\ \mu\text{F}$ bypass capacitor required |
| 15 (`VREF`)| | 3.3V | 5V | Tied to $V_{DD}$ rail |
| 14 (`AGND`)| | GND | GND | Analog ground |
| 9 (`DGND`) | | GND | GND | Digital ground |
| 13 (`CLK`) | | GPIO 11 (SPI0_SCLK)| D13 | SPI Clock |
| 12 (`DOUT`)| | GPIO 9 (SPI0_MISO) | D12 | SPI MISO |
| 11 (`DIN`) | | GPIO 10 (SPI0_MOSI)| D11 | SPI MOSI |
| 10 (`CS`)   | | GPIO 8 (SPI0_CE0)  | D10 | Active-Low Chip Select |

## Example (Python gpiozero on Raspberry Pi)

```python
from gpiozero import MCP3008
from time import sleep

# Read analog potentiometer on Channel 0
pot = MCP3008(channel=0)

while True:
    print(f"Potentiometer Value: {pot.value:.3f} (Voltage: {pot.value * 3.3:.2f} V)")
    sleep(0.5)
```

## Common mistakes

- **Powering `VDD` with 5V when interfacing with 3.3V Raspberry Pi GPIOs:** Supplying 5V to `VDD` causes `DOUT` (MISO) to output 5V logic signals, which will damage 3.3V-unbuffered Raspberry Pi GPIO pins. Power `VDD` from the 3.3V rail on Raspberry Pi setups.
- **Floating `VREF` pin:** Leaving Pin 15 un-connected causes ADC outputs to fluctuate randomly or max out at 1023. Connect `VREF` to 3.3V or 5V.

## Notes

- **MCP3008 vs MCP3208:** MCP3008 is 10-bit (1,024 steps); MCP3208 is 12-bit (4,096 steps). Both use the identical 16-pin DIP footprint.
