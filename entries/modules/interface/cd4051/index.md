## Overview

The CD4051B (and high-speed CMOS 74HC4051) is a single 8-channel analog multiplexer/demultiplexer IC manufactured by Texas Instruments, ON Semiconductor, NXP, and others. It acts as an 8-position digitally controlled solid-state rotary switch, connecting one of 8 independent channel inputs/outputs (`CH0` to `CH7`) to a single common input/output pin (`COM` / `COMMON IN/OUT`).

Widely used to expand analog inputs on microcontrollers (such as reading 8 analog sensors through a single ADC pin on an ESP32 or Arduino), the CD4051 is bidirectional and can route both analog signals (up to 20V peak-to-peak with dual supplies) and digital signals without level conversion between channels.

## Quick reference

| | |
|---|---|
| **Function** | Single 8-Channel Analog Multiplexer / Demultiplexer (8:1 Mux) |
| **Single Supply Voltage (`VDD` to `VSS`)** | 3.0 V to 20.0 V DC (CD4051B) / 2.0 V to 6.0 V (74HC4051) |
| **Split Supply Range (`VDD` to `VEE`)** | Up to 20.0 V peak-to-peak (e.g. `VDD` = +5V, `VEE` = -5V) |
| **ON Resistance (`RON`)** | 80 Ω Typ (`VDD`-`VEE` = 15V) / 125 Ω Typ (`VDD`-`VEE` = 10V) |
| **Control Inputs** | 3 Select lines (`A`, `B`, `C`) + 1 Inhibit (`INH`) |
| **Bandwidth** | 20 MHz (-3 dB) |
| **Packages** | 16-pin DIP, SOIC-16, TSSOP-16 |

## Pin configuration

| Pin (DIP-16) | Name | Type | Description |
|---|---|---|---|
| 13, 14, 15, 12, 1, 5, 2, 4 | `CH0`–`CH7` | Analog I/O | Independent channels 0 through 7 (`IN/OUT 0-7`) |
| 3 | `COM` | Analog I/O | Common channel terminal (`COMMON OUT/IN`) |
| 6 | `INH` | Input | Inhibit (Enable) control: High = all channels OFF; Low = selected channel ON |
| 7 | `VEE` | Power | Negative Analog Supply (connect to GND for single-supply 0-5V operation) |
| 8 | `VSS` | Power | Digital Ground (0V) |
| 9 | `C` | Input | Binary Select Address bit 2 (MSB) |
| 10 | `B` | Input | Binary Select Address bit 1 |
| 11 | `A` | Input | Binary Select Address bit 0 (LSB) |
| 16 | `VDD` | Power | Positive Power Supply (+3V to +20V DC) |

## Functional description & truth table

The CD4051B features built-in level shifters between digital control inputs (`A`, `B`, `C`, `INH`) and internal bilateral transmission gates. This allows low-voltage digital control signals (e.g. 5V logic) to switch higher-voltage or negative-voltage analog signals (`VEE` down to -5V or -10V).

### Channel Select Truth Table

| Inhibit (`INH`) | Select `C` | Select `B` | Select `A` | Selected Channel Connected to `COM` |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | `CH0` (Pin 13) |
| 0 | 0 | 0 | 1 | `CH1` (Pin 14) |
| 0 | 0 | 1 | 0 | `CH2` (Pin 15) |
| 0 | 0 | 1 | 1 | `CH3` (Pin 12) |
| 0 | 1 | 0 | 0 | `CH4` (Pin 1) |
| 0 | 1 | 0 | 1 | `CH5` (Pin 5) |
| 0 | 1 | 1 | 0 | `CH6` (Pin 2) |
| 0 | 1 | 1 | 1 | `CH7` (Pin 4) |
| 1 | X | X | X | **None** (All channels isolated / High-Z) |

## Absolute maximum ratings

> [!WARNING] Stresses beyond these values cause permanent damage. Limits, not operating conditions.

| Parameter | Rating | Unit |
|---|---|---|
| DC Supply Voltage (`VDD` - `VSS` or `VDD` - `VEE`) | -0.5 to +20.0 | V |
| DC Input Voltage (`VIN`) | `VEE` - 0.5 to `VDD` + 0.5 | V |
| Input Diode Current | ±10 | mA |
| Operating Temperature Range | -55 to +125 | °C |
| Storage Temperature Range | -65 to +150 | °C |

## Electrical characteristics

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Peak Switch ON Resistance | `RON` | — | 125 | 240 | Ω | `VDD` = 10V, `VEE` = 0V, `VIS` = `VEE` to `VDD` |
| Peak Switch ON Resistance | `RON` | — | 80 | 160 | Ω | `VDD` = 15V, `VEE` = 0V |
| Off Channel Leakage Current | `IOFF` | — | 0.1 | 100 | nA | `VDD` = 15V, `VEE` = 0V, `INH` = 5V |
| Propagation Delay (`A, B, C` to `COM`) | `tPHL` / `tPLH` | — | 150 | 360 | ns | `VDD` = 5V, `RL` = 10 kΩ, `CL` = 50 pF |
| Cut-off Frequency (-3 dB) | `fMAX` | — | 20 | — | MHz | `VDD` = 5V, `VEE` = -5V, `RL` = 1 kΩ |

## Typical application

```
       +5V DC VCC
           |
     +-----+-----+
     |           |
   100nF       10uF
     |           |
    GND         GND
     |           |
     +-----+-----+--------------+
           |                    |
        +--+--------------------+--+
        | 16                     3 |
        | VDD                  COM |---> MCU ADC Pin (A0)
        |                          |
        | 6 INH (GND)       CH0 13 |<--- Sensor 0 (Analog 0-5V)
        | 7 VEE (GND)       CH1 14 |<--- Sensor 1
        | 8 VSS (GND)       CH2 15 |<--- Sensor 2
        |                   CH3 12 |<--- Sensor 3
MCU GPIO-> 11 A             CH4  1 |<--- Sensor 4
MCU GPIO-> 10 B             CH5  5 |<--- Sensor 5
MCU GPIO->  9 C             CH6  2 |<--- Sensor 6
        |                   CH7  4 |<--- Sensor 7
        +---------------+----------+
                        |
                       GND
```

## Common mistakes

- **Leaving `VEE` Unconnected in Single-Supply Systems:** In standard single-supply 0-5V circuits, `VEE` (Pin 7) MUST be tied to `GND` (Pin 8). Leaving `VEE` floating will cause analog signals near 0V to be severely distorted or cut off.
- **Exceeding Supply Voltage Rails:** The voltage of any analog signal passed through `CHn` or `COM` must stay strictly within `VEE` and `VDD`. Signals exceeding `VDD` or dropping below `VEE` will clamp through internal ESD diodes and distort other channels.
- **High Source Impedance Errors:** `RON` (80–200 Ω) forms a voltage divider with downstream loads or ADC sampling capacitors. If reading high-impedance sensors, buffer the `COM` pin output with an op-amp voltage follower before feeding an MCU ADC.

## Notes & further reading

- 74HC4051 Variant: The 74HC4051 is a high-speed 2V–6V CMOS version with much lower `RON` (~30 Ω at 4.5V) and faster switching times (< 20 ns), preferred for 3.3V/5V microcontroller digital and ADC multiplexing.
- Related Multiplexers: CD4052 (Dual 4-channel multiplexer), CD4053 (Triple 2-channel multiplexer).
