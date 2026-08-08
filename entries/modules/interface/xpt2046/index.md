## Overview

The **XPT2046** is a 4-wire resistive touchscreen controller IC manufactured by Shenzhen XPT (fully pin-compatible with the Texas Instruments ADS7843 / ADS7846). Commonly pre-soldered on the back of 2.4", 2.8", 3.2", and 3.5" color TFT LCD breakout boards (such as ILI9341, ST7789, or HX8357 displays), it converts mechanical touch pressure on resistive glass overlays into precise digital X and Y screen coordinates.

Integrating a 12-bit Successive Approximation Register (SAR) ADC, internal $2.5\text{V}$ voltage reference, low-on-resistance internal MOSFET switches ($R_{ON} \approx 5\ \Omega$), and a synchronous **SPI interface (up to 2.5 MHz)**, the XPT2046 also includes an active-low **touch interrupt output (`T_IRQ`)** that pulls Low whenever a stylus or finger presses the screen.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 2.7 V to 5.5 V DC (3.3 V nominal) |
| **Interface** | SPI (Mode 0,0, up to 2.5 MHz) |
| **Compatible touch panel** | 4-Wire Resistive Touch Panels ($X^+, X^-, Y^+, Y^-$) |
| **ADC resolution** | 12-bit (0 to 4,095 digital counts per axis) |
| **Max sample rate** | 125,000 samples per second (125 kSPS) |
| **Auxiliary channels** | Battery voltage measurement (`VBAT`) + Temperature sensor |
| **Interrupt Output (`T_IRQ`)**| Active-Low open-drain output (Low during screen contact) |
| **Operating current** | $350\ \mu\text{A}$ active / $1.0\ \mu\text{A}$ power-down mode |

## Pinout (TSSOP-16 Package & TFT Module Headers)

```
             ┌───┴───┐
          X+ ─┤ 1   16├─ DCLK
          Y+ ─┤ 2   15├─ CS
          X- ─┤ 3   14├─ DIN (MOSI)
          Y- ─┤ 4   13├─ BUSY
         GND ─┤ 5   12├─ DOUT (MISO)
        VBAT ─┤ 6   11├─ PENIRQ (T_IRQ)
        AUX  ─┤ 7   10├─ VREF
         VCC ─┤ 8    9├─ VCC
             └───────┘
```

| Pin Label | Name | Type | Description |
|---|---|---|---|
| `T_CLK` / `DCLK`| `DCLK` | Digital Input | SPI Clock input (up to 2.5 MHz) |
| `T_CS` / `CS`  | `CS` | Digital Input | Active-Low SPI Chip Select |
| `T_DIN` / `MOSI`| `DIN` | Digital Input | SPI Serial Data In |
| `T_DO` / `MISO` | `DOUT` | Digital Output | SPI Serial Data Out |
| `T_IRQ` | `PENIRQ`| Digital Output | Active-Low touch interrupt pin (Low on touch) |
| `X+`, `X-`, `Y+`, `Y-`| Analog Pins | Analog I/O | Connected to 4-wire resistive glass panel |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.7 | 3.3 | 5.5 | V | DC |
| Active Supply Current | $I_{CC}$ | — | 350 | 500 | µA | Continuous conversion at 125 kSPS |
| Power-Down Current | $I_{pd}$ | — | 1.0 | 3.0 | µA | `PENIRQ` enabled |
| ADC Resolution | $Res_{ADC}$| — | 12 | — | bits | 0 to 4095 raw count output |
| Max SPI Clock Frequency | $f_{CLK}$ | 0 | — | 2.5 | MHz | SPI Mode 0,0 |
| Internal Driver MOSFET $R_{ON}$| $R_{ON}$ | — | 5 | 8 | Ω | Panel driver switch resistance |

## Command Control Byte Format

To initiate a 12-bit ADC conversion, the host MCU transmits an 8-bit Control Byte over SPI:

- **Bit 7:** Start Bit (Must be `1`).
- **Bits 6–4:** Channel Select (`101` = X-Position, `001` = Y-Position, `011` = $Z_1$ Touch Pressure, `100` = $Z_2$ Touch Pressure).
- **Bit 3:** Resolution (`0` = 12-Bit Mode, `1` = 8-Bit Mode).
- **Bit 2:** SER/$\bar{DFR}$ Mode (`0` = Differential Reference, `1` = Single-Ended Reference).
- **Bits 1–0:** Power-Down Mode (`00` = Low power with `PENIRQ` enabled).

### Command Byte Table

| Axis / Channel | Binary Command Byte | Hex Value |
|---|---|---|
| Read X-Position | `11010000` | `0xD0` |
| Read Y-Position | `10010000` | `0x90` |
| Read $Z_1$ Touch Pressure | `10110000` | `0xB0` |

## Wiring (ILI9341 SPI TFT with Touch)

| TFT Touch Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 3.3V / 5V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `T_CLK` | | Digital D13 (Shared SPI SCK) | GPIO 18 | Shared SPI Clock line |
| `T_DIN` (MOSI)| | Digital D11 (Shared SPI MOSI)| GPIO 23 | Shared SPI MOSI line |
| `T_DO` (MISO) | | Digital D12 (Shared SPI MISO)| GPIO 19 | Shared SPI MISO line |
| `T_CS` | | Digital D4 | GPIO 14 | **Dedicated Touch CS Pin** |
| `T_IRQ` | | Digital D2 | GPIO 27 | Touch interrupt line |

## Example (Arduino `XPT2046_Touchscreen` Library)

```cpp
#include <SPI.h>
#include <XPT2046_Touchscreen.h>

#define CS_PIN  4
#define TIRQ_PIN 2

// Initialize XPT2046 on CS_PIN 4 with Hardware Interrupt on TIRQ_PIN 2
XPT2046_Touchscreen ts(CS_PIN, TIRQ_PIN);

void setup() {
  Serial.begin(115200);
  ts.begin();
  ts.setRotation(1); // Set orientation to match TFT screen rotation
  Serial.println("XPT2046 Touch Controller Ready");
}

void loop() {
  if (ts.touched()) {
    TS_Point p = ts.getPoint();

    Serial.print("Touch Detected! Raw X: "); Serial.print(p.x);
    Serial.print(" | Raw Y: "); Serial.print(p.y);
    Serial.print(" | Pressure Z: "); Serial.println(p.z);
  }
  delay(100);
}
```

## Common mistakes

- **Exceeding 2.5 MHz SPI clock frequency:** The XPT2046 SPI interface is rated for max **2.5 MHz**. If sharing the SPI bus with high-speed TFT display drivers (like ILI9341 running at 40 MHz), the MCU must reduce SPI clock frequency down to $\le 2.5\text{ MHz}$ when asserting `T_CS`.
- **Confusing raw ADC counts with pixel coordinates:** The XPT2046 returns raw 12-bit ADC values ($~200 \dots 3800$). Map raw coordinates to screen pixel dimensions ($320 \times 240$) using 2-point calibration in code.

## Notes

- **XPT2046 vs FT6236:** XPT2046 handles resistive single-point touch panels over SPI; FT6236 handles capacitive multi-touch glass panels over $I^2C$.
