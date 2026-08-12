## Overview

The **PIC16F877A** is an iconic 8-bit CMOS Flash microcontroller IC manufactured by Microchip Technology. Based on Microchip's 35-instruction RISC architecture, it operates at clock frequencies up to **$20\text{ MHz}$** ($200\text{ ns}$ instruction cycle execution).

Equipped with **8K words ($14.3\text{ KB}$) of Flash program memory**, **368 bytes of RAM**, **256 bytes of EEPROM**, an 8-channel 10-bit ADC, two Capture/Compare/PWM (CCP) modules, and a universal synchronous/asynchronous serial transceiver (USART), it remains a staple MCU in academic engineering courses, legacy industrial controllers, and hobbyist projects using PICkit programmers.

## Quick reference

| | |
|---|---|
| **CPU Core** | 8-bit PIC RISC (Harvard architecture, 35 instructions) |
| **Max Clock Frequency** | $20\text{ MHz}$ |
| **Flash Program Memory** | 8192 words ($14.3\text{ KB}$, 14-bit word size) |
| **Data RAM** | 368 bytes |
| **Data EEPROM** | 256 bytes |
| **Operating Voltage (`VDD`)** | 2.0 V to 5.5 V DC (4.5V to 5.5V for 20 MHz) |
| **GPIO Count** | 33 I/O pins (Ports A, B, C, D, E) |
| **ADC Channels** | 8 channels (10-bit resolution) |
| **CCP (PWM) Modules** | 2 independent modules |
| **In-Circuit Serial Programming** | ICSP via `RB6` (PGC), `RB7` (PGD), and `MCLR`/`VPP` |
| **Package** | 40-pin DIP / 44-pin TQFP / 44-pin PLCC |

## Pinout (DIP-40 Package)

```
                 ┌───┴───┐
     MCLR/VPP  1│ 1   40│ RB7/PGD
      RA0/AN0  2│       │39 RB6/PGC
      RA1/AN1  3│       │38 RB5
      RA2/AN2  4│       │37 RB4
      RA3/AN3  5│       │36 RB3/PGM
     RA4/T0CKI 6│       │35 RB2
      RA5/AN4  7│       │34 RB1
     RE0/RD/AN5 8│PIC16F877A│33 RB0/INT
     RE1/WR/AN6 9│ DIP-40│32 VDD (+5V)
    RE2/CS/AN7 10│       │31 VSS (GND)
           VDD 11│       │30 RD7
           VSS 12│       │29 RD6
     OSC1/CLKIN 13│      │28 RD5
    OSC2/CLKOUT 14│      │27 RD4
      RC0/T1OSO 15│      │26 RC7/RX
      RC1/T1OSI 16│      │25 RC6/TX
      RC2/CCP1 17│       │24 RC5/SDO
      RC3/SCK  18│       │23 RC4/SDI
      RD0      19│       │22 RD3
      RD1      20│       │21 RD2
                 └───────┘
```

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Operating Voltage (20 MHz) | $V_{DD}$ | 4.5 | 5.0 | 5.5 | V | HS Crystal mode |
| Operating Current | $I_{DD}$ | — | 1.6 | 3.2 | mA | 4 MHz, 5.0V |
| Standby Current | $I_{PD}$ | — | 0.1 | 5.0 | µA | WDT disabled, 5.0V |
| Single I/O Pin Current | $I_{IO}$ | -25 | — | +25 | mA | Maximum sink/source |
| ADC Conversion Time | $T_{AD}$ | 1.6 | — | — | µs | Per 10-bit sample |

## Programming Connections (PICkit 3 / 4 ICSP Header)

```
  PICkit ICSP Pin                  PIC16F877A DIP-40 Pin
  ┌──────────────┐                ┌──────────────────────┐
  │ 1: VPP / MCLR├───────────────►│ Pin 1: MCLR/VPP      │
  │ 2: VDD (+5V) ├───────────────►│ Pin 11 & 32: VDD     │
  │ 3: VSS (GND) ├───────────────►│ Pin 12 & 31: VSS     │
  │ 4: PGD (Data)├───────────────►│ Pin 40: RB7/PGD      │
  │ 5: PGC (Clock)───────────────►│ Pin 39: RB6/PGC      │
  └──────────────┘                └──────────────────────┘
```

## Common mistakes

- **Leaving `MCLR` (Pin 1) unpulled or floating:** Pin 1 is the Master Clear reset line. If left floating, electromagnetic interference causes random CPU resets. Always pull `MCLR` up to $V_{DD}$ via a **$10\text{ k}\Omega$ resistor**.
- **Forgetting to clear `ADCON1` for digital I/O on PORTA:** On power-up, PORTA pins default to analog inputs. If reading digital switches on PORTA, registers `ADCON1` must be configured (e.g. `ADCON1 = 0x06`) to switch pins to digital I/O mode.

## Notes

- **PIC16F877A vs ATmega328P:** PIC16F877A uses 35-instruction 8-bit PIC architecture with 14.3KB Flash in a 40-pin DIP package; ATmega328P uses 131-instruction AVR architecture with 32KB Flash in a 28-pin DIP package.
