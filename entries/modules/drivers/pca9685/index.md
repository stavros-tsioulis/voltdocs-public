## Overview

The **PCA9685** is an I2C-bus controlled 16-channel 12-bit PWM controller manufactured by NXP Semiconductors. Originally designed as an RGBA LED driver, its 12-bit resolution ($4096$ steps) and internal 25 MHz oscillator make it the industry-standard driver for driving up to 16 RC servo motors using a single I2C bus connection.

Breakout boards incorporate power regulation, a reverse-polarity protection MOSFET for motor power (`V+`), $220\text{ }\Omega$ series resistors on output lines, and 3-pin headers (Signal, V+, GND) for direct servo plug-in.

## Quick reference

| | |
|---|---|
| **Logic supply (`VCC`)** | 2.3 V to 5.5 V DC |
| **Servo / Load supply (`V+`)** | Up to 6.0 V DC (dependent on connected servos) |
| **PWM channels** | 16 independent outputs (`PWM0` to `PWM15`) |
| **PWM resolution** | 12-bit (4096 duty-cycle steps per period) |
| **PWM frequency range** | Programmable from 24 Hz to 1526 Hz (typically set to 50 Hz for servos) |
| **I2C slave address** | Base `0x40` (selectable `0x40` to `0x47` via jumpers A0–A5) |
| **All-Call / Software Reset** | Responds to I2C All-Call address `0x70` |

## Pinout

### Standard PCA9685 Servo Breakout Board Pinout

| Pin / Header | Name | Type | Description |
|---|---|---|---|
| Power Terminal | `V+` / `GND` | Power Input | External high-current power supply input for servos (e.g. 5V–6V DC, 2A–10A) |
| Bus Header Pin 1 | `VCC` | Power | Logic supply (+3.3 V to +5.0 V DC) |
| Bus Header Pin 2 | `V+` | Power Output | Pass-through external motor voltage |
| Bus Header Pin 3 | `SDA` | Digital I/O | I2C Serial Data line |
| Bus Header Pin 4 | `SCL` | Digital Input | I2C Serial Clock line |
| Bus Header Pin 5 | `OE` | Digital Input | Active-LOW Output Enable pin (Must be `LOW` to enable outputs) |
| Bus Header Pin 6 | `GND` | Power | Logic Ground (0 V) |
| Servo Ports 0–15 | `PWM` / `V+` / `GND` | Servo Connector | 3-pin 0.1" headers for standard servo connectors |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Logic Supply Voltage | $V_{CC}$ | 2.3 | 3.3 / 5.0 | 5.5 | V | DC |
| Motor Supply Voltage | $V_+$ | — | 5.0 | 6.0 | V | Via Terminal Block |
| Output Sink Current | $I_{sink}$ | — | 25 | — | mA | Per pin at $V_{OL} = 0.4\text{ V}$ |
| Output Source Current | $I_{source}$ | — | 10 | — | mA | Per pin at $V_{OH} = V_{CC} - 0.4\text{ V}$ |
| Internal Clock Frequency | $f_{osc}$ | 23 | 25 | 27 | MHz | Internal oscillator |
| PWM Frequency | $f_{PWM}$ | 24 | 50 | 1526 | Hz | $PRE\_SCALE = 3 \text{ to } 255$ |

## Prescaler & 50 Hz Servo Timing

The PWM frequency is set by configuring the `PRE_SCALE` register (`0xFE`):

$$PRE\_SCALE = \text{round}\left(\frac{f_{osc}}{4096 \times f_{PWM}}\right) - 1$$

For a 50 Hz servo control signal with $f_{osc} = 25\text{ MHz}$:
$$PRE\_SCALE = \text{round}\left(\frac{25000000}{4096 \times 50}\right) - 1 = \text{round}(122.07) - 1 = 121 \quad (\text{Hex: } 0x79)$$

### Servo Position Pulse Width (at 50 Hz, Period = 20 ms)

Each 20 ms period is divided into 4096 steps ($4.88\text{ }\mu\text{s/step}$):
- **0° (0.5 ms pulse):** $\approx 102$ counts
- **90° (1.5 ms pulse):** $\approx 307$ counts
- **180° (2.5 ms pulse):** $\approx 512$ counts

## Wiring

| PCA9685 Breakout | → | Microcontroller / Power Supply | Notes |
|---|---|---|---|
| `VCC` | | `5V` (or `3.3V`) | Logic supply from MCU |
| `GND` | | `GND` | Common ground |
| `SDA` | | `SDA` (A4 on Uno, GPIO21 on ESP32) | I2C Data line |
| `SCL` | | `SCL` (A5 on Uno, GPIO22 on ESP32) | I2C Clock line |
| Terminal `V+` / `GND` | | External 5V/6V Power Supply | **Dedicated high-current supply for servos** |

> [!WARNING]
> Do NOT power servos from the microcontroller 5V rail:
> Connecting multiple servos to the PCA9685 without a dedicated external power supply on the screw terminal will overload the MCU power regulator and cause constant brownouts.

## Common mistakes

- **Forgetting to set PRE_SCALE while in SLEEP mode:** The `PRE_SCALE` register (`0xFE`) can ONLY be written when the `SLEEP` bit (bit 4 of `MODE1` register `0x00`) is set to `1`.
- **Leaving Output Enable (`OE`) floating or HIGH:** `OE` is active-LOW. If `OE` is pulled HIGH, all 16 PWM outputs are disabled (high-impedance).
- **Inaccurate internal clock frequency:** The internal 25 MHz oscillator can drift $\pm 5\%$. For ultra-precise positioning, measure actual output pulse width with an oscilloscope or feed an external clock into `EXTCLK`.

## Notes

- Up to 62 PCA9685 boards can be cascaded on a single I2C bus to control up to 992 servos.
