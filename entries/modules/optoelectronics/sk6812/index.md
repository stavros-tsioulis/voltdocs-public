## Overview

The SK6812 is a smart, individually addressable RGB/RGBW LED light source produced by Opsco Optoelectronics. Integrating a control IC and three or four LED emitters (Red, Green, Blue, and optional White) inside a single 5050 (5.0 × 5.0 mm) SMD surface-mount package, it provides 256 levels of dimming per channel across a 24-bit (RGB) or 32-bit (RGBW) color depth.

Functionally and pin-compatible with the WS2812B, the SK6812 uses an asynchronous single-wire NRZ protocol operating at 800 kbps. It features an integrated signal-reshaping circuit that regenerates data pulses before passing them to the next cascade pixel via the `DOUT` pin, preventing signal degradation in long LED strip installations. The RGBW variants add a dedicated white LED element available in Warm White (3000K), Neutral White (4000K), or Cool White (6000K), offering superior white color rendering and power efficiency compared to mixing RGB channels.

## Quick reference

| | |
|---|---|
| **Type** | Addressable Smart RGB / RGBW Integrated LED |
| **Forward Voltage (`VDD`)** | 4.5 V to 5.5 V DC |
| **Max Forward Current (`IF`)** | ~50 mA total max per pixel (12 mA per channel) |
| **Protocol** | Single-Wire NRZ Asynchronous (800 kbps) |
| **Color Channels** | 3 (RGB) or 4 (RGBW: Red, Green, Blue, White) |
| **Color Depth** | 256 PWM levels (24-bit RGB / 32-bit RGBW) |
| **Package** | 5050 SMD / 3535 SMD / 4020 Side-view |

## Polarity & pin configuration

| Pin | Name | Function | Description |
|---|---|---|---|
| 1 | `VDD` | Power | Positive supply voltage (+5V DC) |
| 2 | `DOUT` | Data Output | Cascaded serial data output to next LED `DIN` pin |
| 3 | `VSS` | Power | Ground connection (0V) |
| 4 | `DIN` | Data Input | Serial NRZ control data input from MCU or previous LED |

> [!INFO] Package orientation: The notch or bevel on one corner of the 5050 package indicates Pin 1 (`VDD`). Ground is Pin 3 (`VSS`).

## Key parameters

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | `VDD` | 4.5 | 5.0 | 5.5 | V | |
| Logical Input High | `VIH` | 0.7 × `VDD` | — | `VDD` + 0.5 | V | `DIN` pin |
| Logical Input Low | `VIL` | -0.5 | — | 0.3 × `VDD` | V | `DIN` pin |
| Channel Drive Current | `IOUT` | 11.0 | 12.0 | 13.0 | mA | Constant current sink per color channel |
| Data Transfer Rate | `fDATA` | — | 800 | — | kbps | Single-wire NRZ timing |
| Reset Pulse Time | `TRESET` | 80 | — | — | µS | `DIN` held low to latch frame |

## Forward & reverse characteristics

### Protocol & Bit Timing

Control data is transmitted as a stream of NRZ pulses. Each bit is represented by a pulse with fixed high and low durations:

- **T0H (0-bit High time):** 0.3 µs ± 0.15 µs
- **T0L (0-bit Low time):** 0.9 µs ± 0.15 µs
- **T1H (1-bit High time):** 0.9 µs ± 0.15 µs
- **T1L (1-bit Low time):** 0.3 µs ± 0.15 µs
- **TRESET (Reset Low time):** > 80 µs

For RGBW models, each pixel consumes 32 bits of data in **G-R-B-W** order (8 bits Green, 8 bits Red, 8 bits Blue, 8 bits White). For standard RGB models, each pixel consumes 24 bits in **G-R-B** order.

## Typical circuits

```
       +5V DC Power
           |
     +-----+------+---------------+---------+
     |            |               |         |
   100nF        100nF           100nF     1000uF
     |            |               |         |
    GND          GND             GND       GND
     |            |               |         |
     +-----+------+---------------+---------+
           |                      |
      +----+----+            +----+----+
      | 1     3 |            | 1     3 |
      | VDD VSS |            | VDD VSS |
      | SK6812  |            | SK6812  |
MCU ->| 4     2 |----------->| 4     2 |------> DOUT to next pixel
GPIO  | DIN DOUT|            | DIN DOUT|
 (330R)|         |            |         |
      +---------+            +---------+
```

> [!WARNING] Always place a 330 Ω to 470 Ω resistor in series on the `DIN` line near the first LED to prevent voltage spikes from damaging the input pin. Place a 100 nF ceramic decoupling capacitor across `VDD` and `VSS` near every LED, and a 1000 µF bulk electrolytic capacitor across the main +5V power rail.

## Common mistakes

- **Sending 24-bit data to an RGBW SK6812 LED:** Standard NeoPixel/FastLED color arrays send 24 bits (G-R-B). When sent to an RGBW SK6812 strip, colors will shift out of phase because each pixel expects 32 bits (G-R-B-W).
- **Driving 5V `VDD` LEDs from a 3.3V GPIO without a logic level shifter:** At `VDD` = 5.0V, `VIH` requires at least 3.5V (0.7 × 5.0V). A 3.3V signal from an ESP32 or RP2040 may cause flicker or ignored data. Use a high-speed level shifter (e.g. 74AHCT125).
- **Insuffcient Power Supply Grounding:** High peak currents (up to 3.6 A per 60-LED strip) cause ground bounce if power wire gauge is inadequate. Connect MCU GND directly to the LED strip GND at multiple injection points.

## Notes & further reading

- Software Support: Supported by FastLED (use `SK6812` or `SK6812RGBW`), Adafruit_NeoPixel (`NEO_RGBW`), and WLED firmware.
- Signal Reshaping: Each SK6812 pixel buffers and regenerates the clock and data pulse shapes before outputting to `DOUT`, ensuring signal integrity over hundreds of cascaded pixels.
