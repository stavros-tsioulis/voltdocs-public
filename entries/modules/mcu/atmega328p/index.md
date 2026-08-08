## Overview

The **ATmega328P** is the single most iconic 8-bit AVR RISC microcontroller IC in open-source hardware history. Originally designed by Atmel (now Microchip Technology), it is the primary microcontroller chip powering the **Arduino Uno R3**, **Arduino Nano**, and **Arduino Pro Mini** development boards.

Featuring **$32\text{ KB}$ of ISP Flash memory**, **$2\text{ KB}$ of SRAM**, and **$1\text{ KB}$ of EEPROM**, the ATmega328P operates at clock speeds up to **$20\text{ MHz}$** across a broad supply voltage range of **$1.8\text{V}$ to $5.5\text{V}$ DC**. Housed in a beginner-friendly 28-pin DIP package (DIP-28), it enables breadboard prototyping of standalone microcontroller circuits.

## Quick reference

| | |
|---|---|
| **CPU Architecture** | 8-bit AVR RISC (131 powerful instructions, 32x8 working registers) |
| **Max Clock Frequency** | $20\text{ MHz}$ at $4.5\text{V} \dots 5.5\text{V}$ ($16\text{ MHz}$ standard Arduino clock) |
| **Memory Breakdown** | $32\text{ KB}$ Flash, $2\text{ KB}$ SRAM, $1\text{ KB}$ EEPROM |
| **Operating Voltage (`VCC`)**| 1.8 V to 5.5 V DC (5.0 V nominal) |
| **Package** | 28-pin DIP (ATmega328P-PU) / 32-pin TQFP (ATmega328P-AU) |
| **I/O & PWM** | 23 programmable GPIO lines, 6 PWM channels (8-bit) |
| **Analog Peripherals** | 6-channel 10-bit ADC (8-channel on TQFP) |
| **Communication Buses** | 1x USART (Hardware Serial), 1x SPI, 1x $I^2C$ (TWI) |
| **Programming Interface** | In-System Programming (ISP / ICSP) via SPI & UART Bootloader |

## Pinout (28-Pin DIP Package - ATmega328P-PU)

```
                       ┌───┴───┐
     (PC6/RESET) RESET ─┤ 1  28 ├─ PC5 (ADC5/SCL)
        (PD0/RXD) RXD ─┤ 2  27 ├─ PC4 (ADC4/SDA)
        (PD1/TXD) TXD ─┤ 3  26 ├─ PC3 (ADC3)
       (PD2/INT0) D2  ─┤ 4  25 ├─ PC2 (ADC2)
  (PD3/INT1/PWM) D3  ─┤ 5  24 ├─ PC1 (ADC1)
             (PD4) D4  ─┤ 6  23 ├─ PC0 (ADC0)
                   VCC ─┤ 7  22 ├─ GND
                   GND ─┤ 8  21 ├─ AREF
     (PB6/XTAL1) XTAL1 ─┤ 9  20 ├─ AVCC
     (PB7/XTAL2) XTAL2 ─┤ 10 19 ├─ PB5 (SCK/D13/LED)
       (PD5/PWM) D5  ─┤ 11 18 ├─ PB4 (MISO/D12)
       (PD6/PWM) D6  ─┤ 12 17 ├─ PB3 (MOSI/PWM/D11)
             (PD7) D7  ─┤ 13 16 ├─ PB2 (SS/PWM/D10)
             (PB0) D8  ─┤ 14 15 ├─ PB1 (PWM/D9)
                       └───────┘
```

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 1.8 | 5.0 | 5.5 | V | DC supply |
| Active Supply Current | $I_{CC}$ | — | 1.5 | 9.0 | mA | $V_{CC} = 5.0\text{V}, f_{CLK} = 16\text{MHz}$ |
| Power-down Sleep Current| $I_{pd}$ | — | 0.1 | 1.0 | µA | $V_{CC} = 3.0\text{V}, T_A = 25^\circ\text{C}$ |
| GPIO Output Sink/Source | $I_{IO}$ | -40 | — | +40 | mA | Absolute max per pin (20mA recommended) |
| System Clock Frequency | $f_{CLK}$ | 0 | 16.0 | 20.0 | MHz | $V_{CC} = 4.5\text{V} \dots 5.5\text{V}$ |
| Flash Endurance | $N_{END}$ | 10,000 | — | — | Cycles | Write/Erase cycles |

## Standalone Breadboard Circuit (16MHz Crystal Setup)

```
        +5V DC Power Supply
           │
        [Pin 7: VCC] ──┬── [ 0.1µF Capacitor ] ── GND
                       │
        [Pin 1: RESET] ─── [ 10kΩ Resistor ] ─── +5V
                       │
   (Crystal 16MHz)     ├─── [Pin 9: XTAL1]  ─── [ 22pF Cap ] ─── GND
                       └─── [Pin 10: XTAL2] ─── [ 22pF Cap ] ─── GND
```

## Wiring (USBasp / Arduino ISP Flashing Connections)

| ICSP Programmer | → | ATmega328P DIP Pin | Arduino Pin Mapping |
|---|---|---|---|
| `VCC` | | Pin 7 (`VCC`) | 5V Power |
| `GND` | | Pin 8 (`GND`) | GND |
| `RESET` | | Pin 1 (`RESET`) | Reset Pin |
| `MOSI` | | Pin 17 (`PB3`) | Digital D11 |
| `MISO` | | Pin 18 (`PB4`) | Digital D12 |
| `SCK` | | Pin 19 (`PB5`) | Digital D13 |

## Example (Bare-Metal C Code for Port Bit Toggling)

```c
#include <avr/io.h>
#include <util/delay.h>

int main(void) {
    // Set PB5 (Arduino Pin 13 LED) as output
    DDRB |= (1 << DDB5);

    while (1) {
        // Toggle PB5 high/low
        PORTB ^= (1 << PORTB5);
        _delay_ms(500);
    }
    return 0;
}
```

## Common mistakes

- **Exceeding 40 mA GPIO current limits:** Drawing $>40\text{ mA}$ from a single I/O pin or $>200\text{ mA}$ total across all pins burns out the output drivers.
- **Forgetting 22pF decoupling capacitors on crystal pins:** Operating a standalone ATmega328P with a $16\text{ MHz}$ crystal without two $22\text{ pF}$ ceramic load capacitors prevents clock oscillation.

## Notes

- **ATmega328P vs ATtiny85 vs ATmega2560:** ATmega328P offers $32\text{ KB}$ Flash in 28-pin DIP; ATtiny85 offers $8\text{ KB}$ in 8-pin DIP; ATmega2560 offers $256\text{ KB}$ Flash in 100-pin TQFP.
