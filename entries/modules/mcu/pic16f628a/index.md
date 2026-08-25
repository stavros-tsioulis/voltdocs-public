## Overview

The **PIC16F628A** is an 18-pin Flash-based 8-bit CMOS microcontroller manufactured by Microchip Technology. Available in a **DIP-18** through-hole and **SOIC-18** package, it was engineered as the direct modernized drop-in replacement for the legendary PIC16F84A.

Operating from **$2.0\text{V}$ to $5.5\text{V}$ DC** at up to **$20\text{ MHz}$** (or via its internal $4\text{ MHz}$ calibrated RC oscillator without external crystals), the PIC16F628A vastly outperforms the older 16F84A by providing **double the Flash memory ($2\text{K words} / 3.5\text{ KB}$)**, **more than triple the RAM ($224\text{ Bytes}$)**, **double the EEPROM ($128\text{ Bytes}$)**, a full **addressable hardware USART (`RX`/`TX`)**, dual analog comparators with programmable internal voltage reference ($V_{REF}$), and a Capture/Compare/PWM (CCP) module. It is a workhorse for hobbyist digital clocks, frequency counters, and serial display modules.

## Quick reference

| | |
|---|---|
| **CPU Core** | 8-bit PIC Mid-Range RISC (35 instructions) |
| **Package** | 18-pin DIP (DIP-18 / PDIP-18) / 18-pin SOIC / 20-pin SSOP |
| **Max Clock Frequency** | $20\text{ MHz}$ ($4\text{ MHz}$ factory internal RC) |
| **Flash Program Memory** | 2048 words ($3.5\text{ KB}$, 14-bit words) |
| **Data RAM** | 224 bytes |
| **Data EEPROM** | 128 bytes |
| **Operating Voltage (`VDD`)** | $2.0\text{ V}$ to $5.5\text{ V}$ DC ($3.0\text{V} \dots 5.5\text{V}$ for $20\text{MHz}$) |
| **GPIO Count** | 16 I/O pins (Ports A and B) |
| **Hardware USART** | Full duplex addressable USART (`RB1/RX`, `RB2/TX`) |
| **Analog Peripherals** | 2x Analog Comparators + Programmable internal $V_{REF}$ module |
| **Timers / PWM** | 3 Timers (Timer0/1/2) + 1x CCP module (10-bit PWM) |

## Pinout (DIP-18 Package)

```
                            ┌───┴───┐
      (AN2/VREF)      RA2  1│ 1   18│ RA1 (AN1)
      (AN3/CMP1)      RA3  2│       │17 RA0 (AN0)
      (T0CKI/CMP2)    RA4  3│       │16 RA7 (OSC1/CLKIN)
      (Active-Low)   RA5/ 4│PIC16F │15 RA6 (OSC2/CLKOUT)
                 MCLR/VPP   │ 628A  │14 VDD (+5V)
                      VSS  5│DIP-18 │13 RB7 (T1OSI/PGD)
              (INT)   RB0  6│       │12 RB6 (T1OSO/T1CKI/PGC)
             (RX/DT)  RB1  7│       │11 RB5
             (TX/CK)  RB2  8│       │10 RB4 (PGM)
             (CCP1)   RB3  9│       │9  (Center-notch bottom)
                            └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1, 2 | `RA2`, `RA3` | GPIO / Analog | `AN2` / `VREF` / `AN3` / Comparator 1 Input |
| 3 | `RA4` | GPIO / Digital | Timer0 Clock Input `T0CKI` / Open-drain output |
| 4 | `RA5 / MCLR`| Digital Input | Active-LOW Reset / `VPP` / General Input |
| 5 | `VSS` | Power | Common Ground reference ($0\text{ V}$) |
| 6 | `RB0` | GPIO / Digital | External Interrupt `INT` / `PCINT` |
| 7 | `RB1` | GPIO / Digital | Hardware UART Receive `RX` / Data `DT` |
| 8 | `RB2` | GPIO / Digital | Hardware UART Transmit `TX` / Clock `CK` |
| 9 | `RB3` | GPIO / Digital | Capture/Compare/PWM Output `CCP1` |
| 10, 11 | `RB4`, `RB5` | GPIO / Digital | Port B GPIOs / Low-Voltage ICSP `PGM` |
| 12 | `RB6` | GPIO / Digital | In-Circuit Serial Programming Clock `PGC` / `T1CKI` |
| 13 | `RB7` | GPIO / Digital | In-Circuit Serial Programming Data `PGD` / `T1OSI` |
| 14 | `VDD` | Power | Positive Supply Voltage ($+2.0\text{ V}$ to $+5.5\text{ V}$) |
| 15, 16 | `RA6`, `RA7` | GPIO / Clock | `OSC2`/`CLKOUT` and `OSC1`/`CLKIN` (usable as GPIO with internal RC) |
| 17, 18 | `RA0`, `RA1` | GPIO / Analog | `AN0`, `AN1` / Comparator Inputs |

## Comparison: PIC16F628A vs PIC16F84A

| Parameter | PIC16F628A | PIC16F84A |
|---|---|---|
| **Pinout / Socket** | **Identical DIP-18** | Identical DIP-18 |
| **Internal Oscillator** | **Yes ($4\text{ MHz}$ calibrated RC)** | No (Requires crystal or RC network) |
| **Flash Memory** | **$2048\text{ Words}$ ($3.5\text{ KB}$)** | $1024\text{ Words}$ ($1.75\text{ KB}$) |
| **Data RAM** | **$224\text{ Bytes}$** | $68\text{ Bytes}$ |
| **Hardware USART** | **Yes (Pins RB1/RB2)** | No (Software Bit-Bang Only) |
| **Timers / PWM** | **3 Timers + CCP (PWM)** | 1 Timer (Timer0 only, no PWM) |

## Common mistakes

- **PORTA analog comparator defaults:** On power-up, PORTA pins default to analog comparator inputs. To use PORTA as general digital I/O, write `CMCON = 0x07;` at the beginning of the program to turn off the comparators.
- **Pin RA4 open-drain behavior:** Pin 3 (`RA4`) has an **open-drain output**. When driven HIGH, it floats; it requires an external pull-up resistor to output a logic HIGH voltage.

## Notes

- **Programming:** Compatible with PICkit 2, 3, 4, SNAP, and standard ICSP programmers using MPLAB X IDE and the XC8 compiler.
