## Overview

The **MAX7219** is a compact, serial input/output common-cathode display driver IC manufactured by Maxim Integrated (Analog Devices). It interfaces microcontrollers to up to **8 digits of 7-segment numeric LED displays**, bar-graph displays, or an **8x8 LED dot-matrix display**.

It integrates a BCD Code-B decoder, multiplex scan circuitry, segment and digit drivers, and an internal static RAM that stores display data. Communication uses a simple 3-wire serial SPI interface (`DIN`, `CLK`, `LOAD`/`CS`), and multiple MAX7219 modules can be daisy-chained together to form large LED ticker displays.

## Quick reference

| | |
|---|---|
| **Operating Voltage (`VCC`)** | 4.0 V to 5.5 V DC (5.0 V nominal) |
| **Display Support** | 8 digits $\times$ 7-segments + DP OR 64 individual LEDs (8x8 Matrix) |
| **Interface** | 3-wire SPI serial interface (`DIN`, `CLK`, `LOAD` / `CS`) |
| **Daisy-chaining** | Supported via `DOUT` pin |
| **Brightness Control** | 16-level digital intensity control via internal PWM |
| **Current Control** | Single external resistor ($R_{SET}$, typically $10\text{ k}\Omega$) sets peak LED current |
| **Shutdown Mode** | 150 µA low-power feature retain state |

## Pinout

```pinout
package
```


### 24-Pin DIP / SO Package

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `DIN` | Digital Input | Serial data input |
| 2, 3, 5–8, 10, 11 | `DIG0`, `DIG4`, `DIG6`, `DIG2`, `DIG3`, `DIG7`, `DIG5`, `DIG1` | Driver Output | Digit cathode-current sinks |
| 4, 9 | `GND` | Power | Ground; connect both pins |
| 12 | `LOAD` / `CS` | Digital Input | Active-low chip select and latch input |
| 13 | `CLK` | Digital Input | Serial clock |
| 14–17, 20–23 | `SEGA`, `SEGF`, `SEGB`, `SEGG`, `SEGC`, `SEGE`, `SEGDP`, `SEGD` | Driver Output | Segment current sources |
| 18 | `ISET` | Analog Input | Segment-current programming resistor terminal |
| 19 | `V+` | Power Input | +4.0 V to +5.5 V supply |
| 24 | `DOUT` | Digital Output | Push-pull serial data output for daisy chaining |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 4.0 | 5.0 | 5.5 | V | DC |
| Logic High Input | $V_{IH}$ | 3.5 | — | $V_{CC}$ | V | `DIN`, `CLK`, `LOAD` |
| Logic Low Input | $V_{IL}$ | 0 | — | 0.8 | V | `DIN`, `CLK`, `LOAD` |
| Segment Drive Current | $I_{SEG}$ | -30 | -40 | -45 | mA | $V_{CC} = 5.0\text{ V}$, $R_{SET} = 9.53\text{ k}\Omega$ |
| Shutdown Supply Current | $I_{CC,off}$ | — | 150 | — | µA | $Shutdown = 0x00$ |
| Clock Frequency | $f_{CLK}$ | — | — | 10 | MHz | SPI clock rate |

## Control Register Map (16-Bit Word Transferred MSB First)

A 16-bit serial frame consists of an 8-bit Address byte (`D15`–`D8`) followed by an 8-bit Data byte (`D7`–`D0`):

| Address Hex | Register Name | Data Byte Functions |
|---|---|---|
| `0x00` | `NO-OP` | No Operation (Used when passing data through daisy-chained modules) |
| `0x01` to `0x08` | `DIGIT 0` to `DIGIT 7` | Segment / Dot Matrix row data byte (`0x00` to `0xFF`) |
| `0x09` | `DECODE MODE` | `0x00` = No BCD decode (Raw matrix mode); `0xFF` = BCD Code-B decode for Digits 0–7 |
| `0x0A` | `INTENSITY` | `0x00` (Min brightness, 1/32 duty cycle) to `0x0F` (Max brightness, 31/32 duty cycle) |
| `0x0B` | `SCAN LIMIT` | `0x00` (Display Digit 0 only) to `0x07` (Display Digits 0–7) |
| `0x0C` | `SHUTDOWN` | `0x00` = Shutdown mode (Display off); `0x01` = Normal operation |
| `0x0F` | `DISPLAY TEST` | `0x00` = Normal operation; `0x01` = Display Test mode (All LEDs ON) |

## Initialization Sequence Example

1. Write `0x0C01` (Exit Shutdown mode -> Normal operation).
2. Write `0x0B07` (Set Scan Limit to all 8 digits / 8 matrix rows).
3. Write `0x0900` (Set Decode Mode to No-Decode for matrix or raw 7-segment drive).
4. Write `0x0A07` (Set Intensity to medium brightness 8/16).
5. Write `0x0F00` (Disable Display Test mode).

## Wiring

| MAX7219 Module Pin | → | Microcontroller (Arduino / ESP32) | Notes |
|---|---|---|---|
| `VCC` | | `5V` | Must be 5V DC (3.3V power is insufficient for red LEDs) |
| `GND` | | `GND` | Ground |
| `DIN` | | MOSI / Serial Data Out (e.g. D11 on Uno / GPIO23 on ESP32) | Serial Data |
| `CS` / `LOAD` | | SS / Chip Select Pin (e.g. D10 on Uno / GPIO5 on ESP32) | Latch signal |
| `CLK` | | SCK / Serial Clock Pin (e.g. D13 on Uno / GPIO18 on ESP32) | Clock signal |

## Common mistakes

- **Leaving chip in Shutdown mode (`0x0C00`):** On initial power-up, the MAX7219 defaults to Shutdown mode with the display turned off. Software MUST write `0x01` to register `0x0C` during startup.
- **Powering from 3.3V:** The MAX7219 requires $V_{CC} \ge 4.0\text{ V}$. Operating on 3.3V causes dim, flickering, or unlit LED segments.
- **Daisy-chaining without proper power distribution:** Cascading 4 or 8 dot-matrix modules in a chain draws $> 1.5\text{ A}$ when all LEDs are illuminated. Power the $V_{CC}$ and $GND$ rails of downstream matrix panels directly from a dedicated 5V power supply rather than passing current through thin PCB traces.

## Notes

- Uses standard libraries like `MD_MAX72XX` and `LedControl` for scrolling marquee text and matrix graphics.
