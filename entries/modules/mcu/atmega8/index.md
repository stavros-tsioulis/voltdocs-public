## Overview

The **ATmega8** (ATmega8A / ATmega8L) is the historic 8-bit AVR RISC microcontroller manufactured by Microchip Technology (originally Atmel) in a standard **28-pin DIP (DIP-28)** package. As the direct predecessor to the ATmega168 and ATmega328P, it powered the very first generation of official **Arduino boards** (Arduino Serial, Arduino USB, and Arduino NG) and remains the standard microcontroller inside the ubiquitous **USBasp AVR In-System Programmer dongles**.

Operating from **$2.7\text{V}$ to $5.5\text{V}$ DC** (ATmega8A) at clock speeds up to **$16\text{ MHz}$**, the ATmega8 features **$8\text{ KB}$ Flash**, **$1\text{ KB}$ SRAM**, **$512\text{ Bytes}$ EEPROM**, a 6-channel 10-bit ADC, three PWM channels, and hardware serial interfaces (USART, SPI, I2C). Because it shares the **identical 28-pin DIP socket footprint as the ATmega328P**, it is widely used for budget-conscious AVR builds, legacy board repairs, and low-cost automated testers.

## Quick reference

| | |
|---|---|
| **CPU Core** | 8-bit AVR RISC Architecture |
| **Package** | 28-pin DIP (DIP-28) / 32-pin TQFP / 32-pin QFN |
| **Max Clock Frequency** | $16\text{ MHz}$ ($8\text{ MHz}$ on older ATmega8L) |
| **Flash Memory** | $8\text{ KB}$ (In-system self-programmable) |
| **SRAM** | $1024\text{ Bytes}$ ($1\text{ KB}$) |
| **EEPROM** | $512\text{ Bytes}$ |
| **Supply Voltage Range** | $2.7\text{ V}$ to $5.5\text{ V}$ DC (ATmega8A) |
| **GPIO Count** | 23 Programmable I/O lines |
| **Analog Peripherals** | 6-channel (DIP) / 8-channel (TQFP) 10-bit ADC |
| **Hardware Serial** | 1x USART, 1x Master/Slave SPI, 1x Byte-oriented 2-wire I2C (TWI) |

## Pinout (DIP-28 Package)

```
                            ┌───┴───┐
       (Active-Low) RESET 1│ 1   28│ PC5 (ADC5 / SCL / PCINT13)
             (RXD) PD0 2│       │27 PC4 (ADC4 / SDA / PCINT12)
             (TXD) PD1 3│       │26 PC3 (ADC3 / PCINT11)
            (INT0) PD2 4│       │25 PC2 (ADC2 / PCINT10)
            (INT1) PD3 5│ATmega8│24 PC1 (ADC1 / PCINT9)
              (T0) PD4 6│ DIP-28│23 PC0 (ADC0 / PCINT8)
                   VCC 7│       │22 GND (AGND)
                   GND 8│       │21 AREF
                 XTAL1 9│       │20 AVCC
                XTAL2 10│       │19 PB5 (SCK)
              (T1) PD5 11│       │18 PB4 (MISO)
            (AIN0) PD6 12│       │17 PB3 (MOSI / OC2)
            (AIN1) PD7 13│       │16 PB2 (SS / OC1B)
            (ICP1) PB0 14│       │15 PB1 (OC1A)
                            └───────┘
```

## Comparison: ATmega8 vs ATmega328P

| Parameter | ATmega8 / ATmega8A | ATmega328P |
|---|---|---|
| **Pinout / Package** | **Identical DIP-28** | Identical DIP-28 |
| **Flash Memory** | $8\text{ KB}$ | $32\text{ KB}$ |
| **SRAM** | $1\text{ KB}$ ($1024\text{ B}$) | $2\text{ KB}$ ($2048\text{ B}$) |
| **EEPROM** | $512\text{ Bytes}$ | $1024\text{ Bytes}$ |
| **PWM Outputs** | 3 channels (Timer1 & Timer2) | 6 channels (Timer0, Timer1, Timer2) |
| **Pin Change Interrupts** | Limited to INT0 / INT1 | Pin Change Interrupts on all 23 GPIOs |

## Common mistakes

- **Assuming 6 PWM channels like the 328P:** The ATmega8 only has **3 hardware PWM channels** (PB1/OC1A, PB2/OC1B, and PB3/OC2). Timer0 on the ATmega8 lacks PWM mode.
- **Bootloader size with modern Arduino sketches:** The classic ATmega8 bootloader takes $1\text{ KB}$ of Flash, leaving only $7\text{ KB}$ for user sketches. Use the optimized **MiniCore / Optiboot** bootloader (only $512\text{ Bytes}$) to maximize available sketch memory.
- **Fuses configuration for internal 8MHz RC vs external crystal:** Brand-new factory ATmega8 chips ship configured for internal 1MHz clock. When soldering a 16MHz crystal on breadboards, set the low fuse byte (`lfuse`) accordingly.

## Notes

- **Arduino Core Support:** Fully supported in modern Arduino IDE via the open-source **MiniCore** package.
