## Overview

The **ATtiny2313** (ATtiny2313A) is a classic 20-pin 8-bit AVR RISC microcontroller manufactured by Microchip Technology (originally Atmel) in a **DIP-20** through-hole and **SOIC-20** surface-mount package. Serving as the modernized replacement for the vintage AT90S2313, it provides a generous **18 GPIO lines** and a **full hardware USART** in a narrow 20-pin format.

Operating from **$1.8\text{V}$ to $5.5\text{V}$ DC** at up to **$20\text{ MHz}$**, the ATtiny2313 features **$2\text{ KB}$ Flash**, **$128\text{ Bytes}$ SRAM**, **$128\text{ Bytes}$ EEPROM**, an 8-bit timer, a 16-bit timer with **4 PWM outputs**, an analog comparator, and a Universal Serial Interface (**USI** supporting SPI and I2C). Because of its built-in hardware UART transceiver, it was prominently featured across 2000s DIY electronics magazines (*Nuts & Volts, Elektor, Circuit Cellar*) for dedicated serial display controllers, LED matrix drivers, frequency counters, and MIDI processors.

## Quick reference

| | |
|---|---|
| **CPU Core** | 8-bit AVR RISC Architecture |
| **Package** | 20-pin DIP (DIP-20 / PDIP-20) / 20-pin SOIC / 20-pin QFN |
| **Max Clock Frequency** | $20\text{ MHz}$ ($8\text{ MHz}$ calibrated internal RC) |
| **Flash Memory** | $2048\text{ Bytes}$ ($2\text{ KB}$) non-volatile storage |
| **SRAM** | $128\text{ Bytes}$ internal RAM |
| **EEPROM** | $128\text{ Bytes}$ non-volatile data storage |
| **Supply Voltage Range** | $1.8\text{ V}$ to $5.5\text{ V}$ DC ($2.7\text{V} \dots 5.5\text{V}$ for $10\text{MHz}$, $4.5\text{V} \dots 5.5\text{V}$ for $20\text{MHz}$) |
| **GPIO Count** | 18 Programmable I/O lines |
| **Hardware USART** | Full duplex hardware UART (Pins `PD0/RXD`, `PD1/TXD`) |
| **PWM Channels** | 4 PWM channels (`OC0A`, `OC0B`, `OC1A`, `OC1B`) |
| **Serial Bus** | USI (Universal Serial Interface for SPI / I2C) |

## Pinout (DIP-20 Package)

```
                            ┌───┴───┐
      (Active-Low/dW) PA2 1│ 1   20│ VCC (+1.8V to +5.5V)
             (RXD) PD0 2│       │19 PB7 (UCSK / SCL / SCK)
             (TXD) PD1 3│       │18 PB6 (DO / MISO)
           (XTAL2) PA1 4│ATtiny │17 PB5 (DI / SDA / MOSI)
           (XTAL1) PA0 5│ 2313  │16 PB4 (OC1B / PCINT4)
          (CKOUT) PD2 6│DIP-20 │15 PB3 (OC1A / PCINT3)
            (INT1) PD3 7│       │14 PB2 (OC0A / PCINT2)
              (T0) PD4 8│       │13 PB1 (AIN1 / PCINT1)
         (OC0B/T1) PD5 9│       │12 PB0 (AIN0 / PCINT0)
                   GND 10│      │11 PD6 (ICP)
                            └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `PA2 / RESET` | GPIO / Reset | Active-LOW Reset / `dW` (debugWIRE) / `PCINT9` |
| 2 | `PD0 / RXD` | GPIO / Digital | Hardware UART Receive `RXD` / `PCINT11` |
| 3 | `PD1 / TXD` | GPIO / Digital | Hardware UART Transmit `TXD` / `PCINT12` |
| 4, 5 | `PA1`, `PA0` | GPIO / Clock | Crystal Oscillator pins (`XTAL2`, `XTAL1`) |
| 6 | `PD2` | GPIO / Digital | `INT0` / `CKOUT` / `XCK` |
| 7, 8, 9 | `PD3`-`PD5` | GPIO / Digital | `INT1` / Timer0 `T0` / Timer1 `T1` / PWM `OC0B` |
| 10 | `GND` | Power | Common Ground reference ($0\text{ V}$) |
| 11 | `PD6` | GPIO / Digital | Timer1 Input Capture Pin (`ICP`) |
| 12, 13 | `PB0`, `PB1` | GPIO / Analog | Analog Comparator Inputs (`AIN0`, `AIN1`) |
| 14, 15, 16| `PB2`-`PB4` | GPIO / Digital | PWM Channels `OC0A`, `OC1A`, `OC1B` |
| 17 | `PB5 / MOSI` | GPIO / SPI | `MOSI` (ISP) / USI Data Input `DI` / I2C `SDA` |
| 18 | `PB6 / MISO` | GPIO / SPI | `MISO` (ISP) / USI Data Output `DO` |
| 19 | `PB7 / SCK` | GPIO / SPI | `SCK` (ISP) / USI Clock `UCSK` / I2C `SCL` |
| 20 | `VCC` | Power | Supply Voltage ($+1.8\text{ V}$ to $+5.5\text{ V}$ DC) |

## Minimal Serial Communications Hookup

```
   FTDI USB-to-UART Adapter
   ┌────────────────────────────────┐
   │ 5V / 3.3V ─────────────────────┼─────────┬──────────────► [Pin 20: VCC]
   │                                │         │                     ATtiny2313
   │                                │   [ 100nF Cap ]               DIP-20
   │                                │         │
   │ GND ───────────────────────────┼─────────┼──────────────► [Pin 10: GND]
   │ TXD ───────────────────────────┼─────────┼──────────────► [Pin 2: PD0 / RXD]
   │ RXD ───────────────────────────┼─────────┴──────────────► [Pin 3: PD1 / TXD]
   └────────────────────────────────┘
```

## Common mistakes

- **Lack of built-in ADC:** Unlike the ATtiny85 or ATmega328P, the ATtiny2313 has **no analog-to-digital converter (ADC)**. It only possesses an Analog Comparator (on pins `PB0/PB1`). If multi-channel ADC reading is required, select the ATtiny84 or ATmega328P.
- **RAM constraints with serial buffering:** The ATtiny2313 has only $128\text{ Bytes}$ of RAM. Standard Arduino `HardwareSerial` circular buffers take $64\text{ Bytes}$ each ($128\text{ Bytes}$ total for RX+TX), consuming 100% of RAM. When using the **ATTinyCore** Arduino board package, configure the minimal serial buffer option ($16\text{ Bytes}$ or $8\text{ Bytes}$) in the tools menu.

## Notes

- **Pin-Compatible Drop-In Upgrade:** **ATtiny4313** doubles the Flash to $4\text{ KB}$ and RAM to $256\text{ Bytes}$.
- **Arduino Core:** Fully supported by Spence Konde's open-source **ATTinyCore** board package.
