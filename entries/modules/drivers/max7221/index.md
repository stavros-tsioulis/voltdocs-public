## Overview

The **MAX7221** is a compact, serial input/output common-cathode display driver IC manufactured by Maxim Integrated (Analog Devices). It interfaces microcontrollers to up to **8 digits of 7-segment numeric LED displays**, bar-graph displays, or an **8x8 LED dot-matrix array**.

While functionally similar to the MAX7219, the MAX7221 incorporates two major improvements:
1. **Full SPI / QSPI / MICROWIRE Compatibility:** The active-low Chip Select ($\overline{CS}$) input gates internal clocking. Serial data on `DIN` is only shifted while $\overline{CS}$ is LOW, allowing the MAX7221 to reliably **share an SPI bus** (sharing `MOSI` and `SCK`) with other SPI peripherals without unintentional data corruption.
2. **Slew-Rate-Limited Segment Drivers:** The segment output driver edges are intentionally slew-rate controlled to minimize electromagnetic interference (**EMI**) and reduce capacitive radiated noise across display wiring harnesses.

## Quick reference

| | |
|---|---|
| **Operating Voltage (`V+`)** | 4.0 V to 5.5 V DC (5.0 V nominal) |
| **Display Support** | 8 digits $\times$ 7-segments + DP OR 64 individual LEDs (8x8 Matrix) |
| **Bus Interface** | 4-wire SPI / QSPI / MICROWIRE (`DIN`, `CLK`, `\overline{CS}`, `DOUT`) |
| **SPI Compatibility** | True SPI slave with gated clocking; safe for multi-device bus sharing |
| **EMI Reduction** | Slew-rate-limited segment output drivers |
| **Daisy-Chaining** | Supported via `DOUT` serial output pin |
| **Brightness Control** | 16-level digital intensity control via internal PWM |
| **Current Setting** | Single external resistor ($R_{SET}$, typically $10\text{ k}\Omega$) sets peak LED current |
| **Shutdown Mode** | 150 µA low-power standby retaining display memory |

## Pinout (24-Pin DIP / SOIC-24)

```
           ┌──────────┐
      DIN ─│ 1     24 │─ DOUT
    DIG 0 ─│ 2     23 │─ SEGD
    DIG 4 ─│ 3     22 │─ SEGDP
      GND ─│ 4     21 │─ SEGE
    DIG 6 ─│ 5     20 │─ SEGC
    DIG 2 ─│ 6     19 │─ V+
    DIG 3 ─│ 7     18 │─ ISET
    DIG 7 ─│ 8     17 │─ SEGG
      GND ─│ 9     16 │─ SEGB
    DIG 5 ─│ 10    15 │─ SEGF
    DIG 1 ─│ 11    14 │─ SEGA
      /CS ─│ 12    13 │─ CLK
           └──────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `DIN` | Digital Input | Serial Data Input. Data is shifted into the internal 16-bit register on `CLK` rising edges while `\overline{CS}` is LOW |
| 2, 3, 5, 6, 7, 8, 10, 11 | `DIG 0`–`DIG 7` | Driver Output | 8 Digit Cathode Drive lines (sink up to 320 mA from common-cathode LEDs) |
| 4, 9 | `GND` | Power | Ground (0 V) — both pins must be connected to ground plane |
| 12 | `\overline{CS}` | Digital Input | Active-Low Chip Select input. Latches data on rising edge |
| 13 | `CLK` | Digital Input | Serial Clock input (supports SPI clock rates up to 10 MHz) |
| 14–17, 20, 21, 22, 23 | `SEGA`–`SEGG`, `SEGDP` | Driver Output | 8 Slew-Rate-Limited Segment Anode Drive lines (source up to 40 mA per segment) |
| 18 | `ISET` | Analog Input | Connects through resistor $R_{SET}$ to $V+$ to set peak segment drive current |
| 19 | `V+` | Power Input | Supply voltage (+4.0 V to +5.5 V DC) |
| 24 | `DOUT` | Digital Output | Serial Data Output for cascading data to the next MAX7221 in a daisy chain |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V+$ | 4.0 | 5.0 | 5.5 | V | DC |
| Logic High Input | $V_{IH}$ | 3.5 | — | $V+$ | V | `DIN`, `CLK`, `\overline{CS}` |
| Logic Low Input | $V_{IL}$ | 0 | — | 0.8 | V | `DIN`, `CLK`, `\overline{CS}` |
| Segment Drive Current | $I_{SEG}$ | -30 | -40 | -45 | mA | $V+ = 5.0\text{ V}, R_{SET} = 9.53\text{ k}\Omega$ |
| Segment Rise/Fall Slew | $t_{r}, t_{f}$ | — | 50 | 100 | ns | Slew-rate-limited driver outputs |
| Shutdown Supply Current | $I_{CC,off}$ | — | 150 | — | µA | Shutdown Register = `0x00` |
| Max SPI Clock Frequency | $f_{CLK}$ | — | — | 10 | MHz | SPI bus clock |

## Register Map (16-Bit Word Transferred MSB First)

Each SPI transmission comprises an 8-bit Register Address (`D15`–`D8`) followed by an 8-bit Data payload (`D7`–`D0`):

| Address Hex | Register Name | Data Byte Functions |
|---|---|---|
| `0x00` | `NO-OP` | No Operation (Used when cascading data through daisy-chained drivers) |
| `0x01` to `0x08` | `DIGIT 0` to `DIGIT 7` | Digit 0 to Digit 7 segment or LED matrix row pattern data (`0x00` to `0xFF`) |
| `0x09` | `DECODE MODE` | `0x00` = No-decode (Direct bit pattern); `0xFF` = Code B decode for Digits 0–7 |
| `0x0A` | `INTENSITY` | `0x00` (Min brightness, 1/32 PWM duty) to `0x0F` (Max brightness, 31/32 PWM duty) |
| `0x0B` | `SCAN LIMIT` | `0x00` (Digit 0 only) to `0x07` (All 8 digits / 8 matrix rows active) |
| `0x0C` | `SHUTDOWN` | `0x00` = Low-power Shutdown mode (Display blank); `0x01` = Normal operation |
| `0x0F` | `DISPLAY TEST` | `0x00` = Normal operation; `0x01` = Display Test mode (All LEDs ON at full brightness) |

## Comparison: MAX7221 vs MAX7219

| Feature | MAX7221 | MAX7219 |
|---|---|---|
| **Pin 12 Function** | `\overline{CS}` (Active-Low Chip Select) | `LOAD` (Latch on rising edge) |
| **SPI Clock Gating** | Clock disabled while `\overline{CS}` is HIGH | Shifts on every clock pulse regardless of `LOAD` |
| **SPI Bus Sharing** | **Fully supported** (Can share `MOSI`/`SCK` with sensors, SD cards) | **Not recommended** (Corrupted by other SPI traffic) |
| **Output Drivers** | Slew-rate limited (Low EMI) | Fast transitions |

## Wiring

| MAX7221 Pin | → | Microcontroller (Arduino Uno / ESP32) | Notes |
|---|---|---|---|
| `V+` (Pin 19) | | `5V` | Regulated +5.0V supply rail |
| `GND` (Pins 4, 9) | | `GND` | Common ground reference |
| `DIN` (Pin 1) | | `MOSI` (Pin 11 on Uno / GPIO 23 on ESP32) | Hardware SPI Data Out |
| `CLK` (Pin 13) | | `SCK` (Pin 13 on Uno / GPIO 18 on ESP32) | Hardware SPI Clock |
| `\overline{CS}` (Pin 12) | | `SS` / Dedicated GPIO (Pin 10 on Uno / GPIO 5 on ESP32) | Active-Low Chip Select |

## Common mistakes

- **Leaving in default Shutdown mode:** On power-up, the MAX7221 defaults to shutdown mode (`0x0C` = `0x00`) with blank displays. Your initialization firmware must write `0x01` to register `0x0C`.
- **Missing decoupling capacitors:** High transient current pulses from multiplexing 8 digits can inject noise onto logic supplies. Place a $100\text{ nF}$ ceramic capacitor and a $10\ \mu\text{F}$ electrolytic capacitor directly adjacent to Pin 19 ($V+$) and Pin 4/9 ($GND$).
- **Missing current setting resistor ($R_{SET}$):** Never connect Pin 18 (`ISET`) directly to $V+$. Always include $R_{SET} \ge 9.53\text{ k}\Omega$ to establish safe current limits ($I_{SEG} \le 40\text{ mA}$) and avoid frying the internal driver stage or LEDs.

## Notes

- **Software Libraries:** Compatible with `LedControl`, `MD_MAX72XX`, and Adafruit GFX display drivers.
