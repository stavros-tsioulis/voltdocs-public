## Overview

The **ATtiny84** (ATtiny84A) is a 14-pin 8-bit AVR RISC microcontroller manufactured by Microchip Technology (originally Atmel). Available in a compact **DIP-14** through-hole and **SOIC-14** surface-mount package, it bridges the gap between the compact 8-pin ATtiny85 (5 usable I/O lines) and the larger 28-pin ATmega328P.

Operating from **$1.8\text{V}$ to $5.5\text{V}$ DC** at up to **$20\text{ MHz}$**, the ATtiny84 delivers **$8\text{ KB}$ Flash**, **$512\text{ Bytes}$ SRAM**, **$512\text{ Bytes}$ EEPROM**, an **8-channel 10-bit ADC** with programmable $20\times$ differential gain, a **16-bit Timer1** with input capture, four hardware PWM outputs, and a Universal Serial Interface (**USI** for SPI and I2C). With full Arduino core support via Spence Konde's **ATTinyCore**, it is a popular choice for matrix keypad decoders, multi-sensor analog data nodes, and custom compact PCB modules requiring more pins than the ATtiny85 without the physical bulk of a 28-pin DIP chip.

## Quick reference

| | |
|---|---|
| **CPU Core** | 8-bit AVR RISC Architecture |
| **Package** | 14-pin DIP (DIP-14 / PDIP-14) / 14-pin SOIC / 20-pin QFN |
| **Max Clock Frequency** | $20\text{ MHz}$ ($8\text{ MHz}$ calibrated internal RC) |
| **Flash Memory** | $8192\text{ Bytes}$ ($8\text{ KB}$) non-volatile storage |
| **SRAM** | $512\text{ Bytes}$ internal RAM |
| **EEPROM** | $512\text{ Bytes}$ true non-volatile EEPROM |
| **Supply Voltage Range** | $1.8\text{ V}$ to $5.5\text{ V}$ DC ($2.7\text{V} \dots 5.5\text{V}$ for $10\text{MHz}$, $4.5\text{V} \dots 5.5\text{V}$ for $20\text{MHz}$) |
| **GPIO Count** | 12 Programmable I/O lines (Ports A and B) |
| **Analog Peripherals** | 8-channel 10-bit ADC + $20\times$ Differential Gain + Internal Temp Sensor |
| **Timers** | 1x 8-bit Timer0 + 1x 16-bit Timer1 with 4 PWM channels |
| **Serial Bus** | USI (Universal Serial Interface for SPI / I2C), ISP (SPI) |

## Pinout (DIP-14 Package)

```
                            ┌───┴───┐
                   VCC 1│ 1   14│ GND (0V)
     (PCINT8/XTAL1) PB0 2│       │13 PA0 (ADC0/AREF/PCINT0)
     (PCINT9/XTAL2) PB1 3│ATtiny │12 PA1 (ADC1/AIN0/PCINT1)
   (Active-Low/dW) PB3 4│  84   │11 PA2 (ADC2/AIN1/PCINT2)
    (PCINT10/INT0) PB2 5│DIP-14 │10 PA3 (ADC3/T0/PCINT3)
(ADC7/OC0B/ICP1) PA7 6│       │9  PA4 (ADC4/USCK/SCL/SCK)
(ADC6/OC0A/DI)   PA6 7│       │8  PA5 (ADC5/DO/MISO/OC1B)
                            └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply Voltage ($+1.8\text{ V}$ to $+5.5\text{ V}$ DC) |
| 2 | `PB0` | GPIO / Clock | `XTAL1` (Crystal In) / `CLKI` / `PCINT8` |
| 3 | `PB1` | GPIO / Clock | `XTAL2` (Crystal Out) / `PCINT9` |
| 4 | `PB3` | GPIO / Reset | Active-LOW Reset / `dW` (debugWIRE) / `PCINT11` |
| 5 | `PB2` | GPIO / Digital | External Interrupt `INT0` / `OC0A` / `PCINT10` |
| 6 | `PA7` | GPIO / Analog | `ADC7` / `OC0B` (PWM) / Timer1 `ICP1` / `PCINT7` |
| 7 | `PA6` | GPIO / SPI | `MOSI` (ISP) / `ADC6` / `OC0A` / USI Data Input `DI` / `SDA` |
| 8 | `PA5` | GPIO / SPI | `MISO` (ISP) / `ADC5` / `OC1B` (PWM) / USI Data Output `DO` |
| 9 | `PA4` | GPIO / SPI | `SCK` (ISP) / `ADC4` / USI Clock `USCK` / `SCL` |
| 10, 11, 12 | `PA3`-`PA1` | GPIO / Analog | `ADC3`-`ADC1` / Analog Comparator `AIN0`/`AIN1` |
| 13 | `PA0` | GPIO / Analog | `ADC0` / Analog Reference `AREF` |
| 14 | `GND` | Power | Common Ground reference ($0\text{ V}$) |

## Minimal Circuit & ISP Flashing Hookup

```
   Arduino as ISP / USBasp Programmer
   ┌────────────────────────────────┐
   │ 5V / 3.3V ─────────────────────┼─────────┬──────────────► [Pin 1: VCC]
   │                                │         │                     ATtiny84
   │                                │   [ 100nF Cap ]               DIP-14
   │                                │         │
   │ GND ───────────────────────────┼─────────┼──────────────► [Pin 14: GND]
   │ RESET (Pin 10 on Arduino) ─────┼─────────┼──────────────► [Pin 4: PB3 / RESET]
   │ MOSI (Pin 11 on Arduino) ──────┼─────────┼──────────────► [Pin 7: PA6 / MOSI]
   │ MISO (Pin 12 on Arduino) ──────┼─────────┼──────────────► [Pin 8: PA5 / MISO]
   │ SCK  (Pin 13 on Arduino) ──────┼─────────┼──────────────► [Pin 9: PA4 / SCK]
   └────────────────────────────────┘
```

## Comparison: ATtiny84 vs ATtiny85 vs ATmega328P

| Parameter | ATtiny85 | ATtiny84 | ATmega328P |
|---|---|---|---|
| **Package** | 8-pin DIP | **14-pin DIP** | 28-pin DIP |
| **Usable GPIOs** | 5 GPIOs | **12 GPIOs** | 23 GPIOs |
| **Flash Memory** | $8\text{ KB}$ | **$8\text{ KB}$** | $32\text{ KB}$ |
| **ADC Channels** | 4 channels | **8 channels** | 6 channels (DIP) |
| **16-bit Timers**| 0 (two 8-bit) | **1x 16-bit Timer1** | 1x 16-bit Timer1 |

## Common mistakes

- **SPI pin mapping confusion:** On the ATtiny85, SPI pins are on PB0/PB1/PB2. On the ATtiny84, SPI pins (`MOSI`, `MISO`, `SCK`) are located on **PA6, PA5, PA4**. Double-check wiring when porting designs from ATtiny85 to ATtiny84.
- **Floating RESET pin:** In electrically noisy motor or relay driver environments, pull Pin 4 (`RESET`) up to `VCC` using an external **$10\text{ k}\Omega$ resistor**.

## Notes

- **Arduino Core:** Fully supported by Spence Konde's open-source **ATTinyCore** board package.
