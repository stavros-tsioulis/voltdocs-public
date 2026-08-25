## Overview

The **ATmega644P** is an 8-bit AVR RISC microcontroller manufactured by Microchip Technology (originally Atmel). Housed in a large, breadboard-friendly **40-pin DIP (DIP-40)** package (as well as 44-pin TQFP/QFN), it provides an expansive step up from the ATmega328P with double the Flash memory (**$64\text{ KB}$**), double the SRAM (**$4\text{ KB}$**), **32 GPIO pins**, and **two independent hardware USARTs**.

Operating from **$1.8\text{V}$ to $5.5\text{V}$ DC** at up to **$20\text{ MHz}$**, the ATmega644P achieved legendary status in the maker community as the brain of the **Sanguino** open-source development board, early RepRap 3D printer controller boards (**Gen6, Melzi**), and the **Uzebox** retro gaming console. It is the premier choice when full DIP through-hole prototyping is required for projects needing dual hardware serial ports (e.g. GPS + Bluetooth, or MIDI + Debug), large display framebuffers, or 32 dedicated digital I/O lines without multiplexers.

## Quick reference

| | |
|---|---|
| **CPU Core** | 8-bit AVR RISC Architecture |
| **Package** | 40-pin DIP (DIP-40 / PDIP-40) / 44-pin TQFP |
| **Max Clock Frequency** | $20\text{ MHz}$ ($16\text{ MHz}$ standard on Arduino / Sanguino) |
| **Flash Memory** | $64\text{ KB}$ (In-system self-programmable) |
| **SRAM** | $4\text{ KB}$ internal SRAM |
| **EEPROM** | $2\text{ KB}$ true non-volatile EEPROM |
| **Supply Voltage Range** | $1.8\text{ V}$ to $5.5\text{ V}$ DC ($4.5\text{ V} \dots 5.5\text{ V}$ for $16\text{ MHz}$) |
| **GPIO Count** | 32 Programmable I/O lines (Ports A, B, C, D) |
| **Analog** | 8-channel 10-bit ADC with differential input and $10\times/200\times$ programmable gain |
| **Serial Communication** | **2x Hardware USARTs** (USART0, USART1), 1x SPI, 1x I2C (TWI) |
| **Programming** | ISP (SPI) / JTAG / Serial Bootloader |

## Pinout (DIP-40 Package)

```
                            ┌───┴───┐
      (PCINT8/XCK0/T0) PB0 1│ 1   40│ PA0 (ADC0/PCINT0)
       (PCINT9/CLKO/T1) PB1 2│       │39 PA1 (ADC1/PCINT1)
   (PCINT10/INT2/AIN0) PB2 3│       │38 PA2 (ADC2/PCINT2)
    (PCINT11/OC0A/AIN1) PB3 4│       │37 PA3 (ADC3/PCINT3)
         (PCINT12/OC0B) PB4 5│       │36 PA4 (ADC4/PCINT4)
          (PCINT13/MOSI) PB5 6│       │35 PA5 (ADC5/PCINT5)
          (PCINT14/MISO) PB6 7│ATmega│34 PA6 (ADC6/PCINT6)
           (PCINT15/SCK) PB7 8│ 644P │33 PA7 (ADC7/PCINT7)
          (Active-Low) RESET 9│DIP-40│32 AREF
                   VCC 10│       │31 GND (AGND)
                   GND 11│       │30 AVCC
                 XTAL2 12│       │29 PC7 (TOSC2/PCINT23)
                 XTAL1 13│       │28 PC6 (TOSC1/PCINT22)
          (PCINT24/RXD0) PD0 14│       │27 PC5 (TDI/PCINT21)
          (PCINT25/TXD0) PD1 15│       │26 PC4 (TDO/PCINT20)
    (PCINT26/INT0/RXD1) PD2 16│       │25 PC3 (TMS/PCINT19)
    (PCINT27/INT1/TXD1) PD3 17│       │24 PC2 (TCK/PCINT18)
         (PCINT28/OC1B) PD4 18│       │23 PC1 (SDA/PCINT17)
         (PCINT29/OC1A) PD5 19│       │22 PC0 (SCL/PCINT16)
         (PCINT30/OC2B) PD6 20│       │21 PD7 (OC2A/PCINT31)
                            └───────┘
```

## Minimal Circuit Hookup (16MHz Standard Setup)

```
                            +5.0V Regulated DC
                                   │
              ┌────────────────────┼───────────────────┐
              │                    │                   │
        [Pin 10: VCC]        [Pin 30: AVCC]      [ 10kΩ Pull-Up ]
              │                    │                   │
        [ 100nF Cap ]        [ 100nF Cap ]       [Pin 9: RESET]
              │                    │                   │
        [Pin 11: GND] ─────────────┼─────────────[ 100nF DTR Cap ] ◄── FTDI DTR
              │                    │
              ├──────────────[Pin 31: GND]
              │
             GND
              │
  16MHz Crystal Setup:
    XTAL1 (Pin 13) ───┬───[ 16MHz Crystal ]───┬─── XTAL2 (Pin 12)
                      │                       │
                [ 22pF Cap ]             [ 22pF Cap ]
                      │                       │
                     GND                     GND
```

## Comparison: ATmega644P vs ATmega328P

| Parameter | ATmega644P | ATmega328P |
|---|---|---|
| **Package** | **40-pin DIP** | 28-pin DIP |
| **Flash Memory** | **$64\text{ KB}$** | $32\text{ KB}$ |
| **SRAM** | **$4\text{ KB}$ (4096 B)** | $2\text{ KB}$ (2048 B) |
| **EEPROM** | **$2\text{ KB}$ (2048 B)** | $1\text{ KB}$ (1024 B) |
| **GPIO Lines** | **32 GPIOs** | 23 GPIOs |
| **Hardware USARTs** | **2x USARTs (`Serial`, `Serial1`)** | 1x USART (`Serial`) |

## Common mistakes

- **Leaving AVCC disconnected:** Pin 30 (`AVCC`) powers the entire Port A analog multiplexer and ADC circuitry. Even if ADC is not used, `AVCC` must be connected to `VCC` with a $100\text{ nF}$ decoupling capacitor.
- **Pinout numbering difference from 328P:** The ATmega644P pinout mapping is non-identical to the 328P. When targeting Arduino code, install the **MightyCore** board package and select the correct standard pinout mapping.

## Notes

- **Arduino Core:** Supported in the Arduino IDE and PlatformIO via the open-source **MightyCore** package.
