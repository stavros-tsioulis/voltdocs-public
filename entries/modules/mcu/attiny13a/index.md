## Overview

The **ATtiny13A** is an ultra-compact, ultra-low-cost 8-bit AVR RISC microcontroller manufactured by Microchip Technology (originally Atmel). Housed in an 8-pin through-hole **DIP-8** and surface-mount **SOIC-8** package, it provides the most minimalist bare-bones AVR processing platform available.

Operating from **$1.8\text{V}$ to $5.5\text{V}$ DC** with **picoPower technology** ($< 0.1\ \mu\text{A}$ sleep current), the ATtiny13A integrates **$1\text{ KB}$ Flash ($1024\text{ Bytes}$)**, **$64\text{ Bytes}$ SRAM**, **$64\text{ Bytes}$ EEPROM**, 6 programmable GPIOs, a 4-channel 10-bit ADC, and 2 hardware PWM outputs from its internal 8-bit timer. With dedicated Arduino core support via **MicroCore**, it is celebrated across DIY electronics communities for powering **tactical LED flashlight firmware (Biscotti / Guppydrv / ToyKeeper AMC7135 drivers), simple servo decoders, RGB LED mood candles, and tiny smart battery monitors**.

## Quick reference

| | |
|---|---|
| **CPU Core** | 8-bit AVR RISC Architecture |
| **Package** | 8-pin DIP (DIP-8) / 8-pin SOIC / 10-pin QFN |
| **Internal Oscillators** | $9.6\text{ MHz}$ / $4.8\text{ MHz}$ / $128\text{ kHz}$ calibrated RC |
| **Flash Memory** | $1024\text{ Bytes}$ ($1\text{ KB}$) non-volatile storage |
| **SRAM** | $64\text{ Bytes}$ internal RAM |
| **EEPROM** | $64\text{ Bytes}$ non-volatile data EEPROM |
| **Supply Voltage Range** | $1.8\text{ V}$ to $5.5\text{ V}$ DC ($4.5\text{V} \dots 5.5\text{V}$ for $20\text{MHz}$) |
| **Deep Sleep Current** | $< 0.1\ \mu\text{A}$ at $1.8\text{V}$ (Power-Down Mode) |
| **GPIO Count** | 6 Programmable I/O lines (PB0 through PB5) |
| **Analog Peripherals** | 4-channel 10-bit ADC (15 ksps) + Analog Comparator |
| **Timer / PWM** | 1x 8-bit Timer/Counter with 2 PWM channels (`OC0A`, `OC0B`) |
| **Programming Interface** | In-System Programming (ISP via SPI: MOSI, MISO, SCK, RESET) |

## Pinout (DIP-8 Package)

```
                            ┌───┴───┐
      (Active-Low/ADC0) PB5 1│ 1   8 │ VCC (+1.8V to +5.5V)
       (ADC3/CLKI/PCINT3) PB3 2│ATtiny│ 7 PB2 (SCK/ADC1/PCINT2)
       (ADC2/CLKO/PCINT4) PB4 3│ 13A  │ 6 PB1 (MISO/OC0B/PCINT1)
                          GND 4│DIP-8 │ 5 PB0 (MOSI/OC0A/PCINT0)
                            └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `PB5` | GPIO / Reset | Active-LOW Reset / `ADC0` / `PCINT5` / `dW` (debugWIRE) |
| 2 | `PB3` | GPIO / Analog | `ADC3` / External Clock Input (`CLKI`) / `PCINT3` |
| 3 | `PB4` | GPIO / Analog | `ADC2` / Clock Output (`CLKO`) / `PCINT4` |
| 4 | `GND` | Power | Common Ground reference ($0\text{ V}$) |
| 5 | `PB0` | GPIO / Digital | `MOSI` (ISP) / `OC0A` (PWM Output 0) / `AIN0` / `PCINT0` |
| 6 | `PB1` | GPIO / Digital | `MISO` (ISP) / `OC0B` (PWM Output 1) / `AIN1` / `PCINT1` |
| 7 | `PB2` | GPIO / Digital | `SCK` (ISP) / `ADC1` / `T0` (Timer Clock) / `PCINT2` |
| 8 | `VCC` | Power | Supply Voltage ($+1.8\text{ V}$ to $+5.5\text{ V}$ DC) |

## Minimal Circuit & ISP Flashing Hookup

```
   Arduino as ISP / USBasp Programmer
   ┌────────────────────────────────┐
   │ 5V / 3.3V ─────────────────────┼─────────┬──────────────► [Pin 8: VCC]
   │                                │         │                     ATtiny13A
   │                                │   [ 100nF Cap ]               DIP-8
   │                                │         │
   │ GND ───────────────────────────┼─────────┼──────────────► [Pin 4: GND]
   │ RESET (Pin 10 on Arduino) ─────┼─────────┼──────────────► [Pin 1: PB5 / RESET]
   │ MOSI (Pin 11 on Arduino) ──────┼─────────┼──────────────► [Pin 5: PB0 / MOSI]
   │ MISO (Pin 12 on Arduino) ──────┼─────────┼──────────────► [Pin 6: PB1 / MISO]
   │ SCK  (Pin 13 on Arduino) ──────┼─────────┼──────────────► [Pin 7: PB2 / SCK]
   └────────────────────────────────┘
```

## Comparison: ATtiny13A vs ATtiny85

| Parameter | ATtiny13A | ATtiny85 |
|---|---|---|
| **Pinout** | **Identical 8-pin DIP / SOIC** | Identical 8-pin DIP / SOIC |
| **Flash Memory** | $1024\text{ Bytes}$ ($1\text{ KB}$) | $8192\text{ Bytes}$ ($8\text{ KB}$) |
| **SRAM** | $64\text{ Bytes}$ | $512\text{ Bytes}$ |
| **EEPROM** | $64\text{ Bytes}$ | $512\text{ Bytes}$ |
| **Timers** | 1x 8-bit Timer (2 PWM) | 2x Timers (1x 8-bit, 1x High-Speed 64MHz 8-bit) |
| **Price** | $\approx \$0.30 - \$0.50$ | $\approx \$1.10 - \$1.50$ |

## Common mistakes

- **RAM exhaustion with standard C libraries:** With only $64\text{ Bytes}$ of RAM, avoid using `sprintf`, heavy string manipulations, or large global arrays. Keep local variables minimal.
- **Flashing with stock Arduino core instead of MicroCore:** Standard Arduino core overhead will exceed the $1024\text{ Byte}$ Flash limit instantly. Install **MicroCore** by MCUdude, which strips runtime bloat and allows full `digitalWrite()`, `analogRead()`, and `delay()` within a few hundred bytes.
- **Disabling the RESET pin (`RSTDISBL` fuse):** Disabling Reset to gain Pin 1 as PB5 prevents future SPI programming. High-Voltage Serial Programming (HVSP with 12V on Reset) will be required to erase and restore the chip.

## Notes

- **Arduino Core:** Supported via the open-source **MicroCore** board package.
