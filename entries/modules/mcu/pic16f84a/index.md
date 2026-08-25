## Overview

The **PIC16F84A** (along with its iconic forebears the PIC16C84 and PIC16F84) is the historic 18-pin 8-bit CMOS Flash microcontroller manufactured by Microchip Technology. Housed in a through-hole **DIP-18** package, it is widely acknowledged as the single component that ignited the hobbyist and DIY microcontroller revolution in the 1990s and early 2000s.

Before the PIC16F84, microcontrollers were expensive windowed ceramic chips requiring UV erasers (UV-EPROMs) or one-time-programmable (OTP) devices. By introducing electronically re-programmable **Flash program memory** and an inexpensive serial programmer interface (ICSP), the PIC16F84 made microcontroller programming accessible to students, hobbyists, amateur radio operators, and hardware hackers worldwide.

Featuring **1K words ($1.75\text{ KB}$) of Flash memory**, **68 bytes of RAM**, **64 bytes of EEPROM**, an 8-bit Timer0, and 13 digital I/O lines, it served as the basis for thousands of classic tutorials, textbook curricula, smart-card programmers (Gold Cards), keyers, and retro hobby projects before being succeeded by the enhanced PIC16F628A.

## Quick reference

| | |
|---|---|
| **CPU Core** | 8-bit PIC Mid-Range RISC (Harvard architecture, 35 instructions) |
| **Package** | 18-pin DIP (DIP-18 / PDIP-18) / 18-pin SOIC / 20-pin SSOP |
| **Max Clock Frequency** | $20\text{ MHz}$ ($4\text{ MHz}$ on -04 grade, $20\text{ MHz}$ on -20 grade) |
| **Flash Program Memory** | 1024 words ($1.75\text{ KB}$, 14-bit words, 10,000 write cycles) |
| **Data RAM** | 68 bytes |
| **Data EEPROM** | 64 bytes true non-volatile EEPROM (10,000,000 write cycles) |
| **Operating Voltage (`VDD`)** | $4.0\text{ V}$ to $5.5\text{ V}$ DC ($2.0\text{V} \dots 5.5\text{V}$ on low-voltage PIC16LF84A) |
| **GPIO Count** | 13 I/O pins (Port A: 5 pins, Port B: 8 pins) |
| **Timers** | 1x 8-bit Timer0 with 8-bit programmable prescaler |
| **Programming Interface** | In-Circuit Serial Programming (ICSP via `RB6`, `RB7`, `MCLR/VPP`) |

## Pinout (DIP-18 Package)

```
                            ┌───┴───┐
                      RA2  1│ 1   18│ RA1
                      RA3  2│       │17 RA0
             (T0CKI)  RA4  3│PIC16F │16 OSC1 / CLKIN
         (Active-Low) RA5/ 4│  84A  │15 OSC2 / CLKOUT
                 MCLR/VPP   │ DIP-18│14 VDD (+5V)
                      VSS  5│       │13 RB7 (PGD / Data)
              (INT)   RB0  6│       │12 RB6 (PGC / Clock)
                      RB1  7│       │11 RB5
                      RB2  8│       │10 RB4
                      RB3  9│       │9  (Bottom Notch)
                            └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1, 2 | `RA2`, `RA3` | GPIO / Digital | Port A bi-directional I/O pins |
| 3 | `RA4 / T0CKI` | GPIO / Open-Drain| Port A Bit 4 / Timer0 External Clock Input (Open-drain output) |
| 4 | `MCLR / VPP` | Digital Input | Master Clear (Reset, Active LOW) / Programming Voltage Input ($+12\text{V}$–$13\text{V}$) |
| 5 | `VSS` | Power | Common Ground reference ($0\text{ V}$) |
| 6 | `RB0 / INT` | GPIO / Interrupt | Port B Bit 0 / External Interrupt input pin |
| 7, 8, 9, 10, 11 | `RB1`-`RB5` | GPIO / Digital | Port B bi-directional I/O pins (with software pull-ups) |
| 12 | `RB6 / PGC` | GPIO / Digital | Port B Bit 6 / ICSP Serial Programming Clock |
| 13 | `RB7 / PGD` | GPIO / Digital | Port B Bit 7 / ICSP Serial Programming Data |
| 14 | `VDD` | Power | Positive Power Supply ($+4.0\text{ V}$ to $+5.5\text{ V}$) |
| 15 | `OSC2 / CLKOUT`| Clock Output | Crystal oscillator output or instruction clock output ($F_{OSC}/4$) |
| 16 | `OSC1 / CLKIN` | Clock Input | Crystal oscillator input or external clock input |
| 17, 18 | `RA0`, `RA1` | GPIO / Digital | Port A bi-directional I/O pins |

## Minimal Crystal Circuit & ICSP Connections

```
                                +5.0V Regulated DC
                                       │
                  ┌────────────────────┴───────────────┐
                  │                                    │
            [Pin 14: VDD]                        [ 10kΩ Pull-Up ]
                  │                                    │
            [ 100nF Cap ]                        [Pin 4: MCLR/VPP]
                  │                                    │
            [Pin 5: VSS] ──────────────────────────────┼─── Common GND
                  │                                    │
  4MHz Crystal Setup:                                  │
    OSC1 (Pin 16) ───┬───[ 4MHz Crystal ]───┬─── OSC2 (Pin 15)
                     │                      │
               [ 22pF Cap ]            [ 22pF Cap ]
                     │                      │
                    GND                    GND
```

## Common mistakes

- **Missing external oscillator components:** Unlike modern microcontrollers (and the successor PIC16F628A), the PIC16F84A **does not have an internal RC oscillator**. It will not run without an external crystal, resonator, or external RC resistor/capacitor network connected across pins 15 and 16.
- **Forgetting that RA4 is open-drain:** Pin 3 (`RA4`) cannot source current to drive high. To output a logic HIGH, connect an external pull-up resistor (e.g. $4.7\text{ k}\Omega$).
- **No hardware UART or ADC:** The PIC16F84A possesses no built-in ADC and no hardware USART. Serial communication must be implemented via software delay-loop bit-banging.

## Notes

- **Modern Successor:** The **PIC16F628A** is pin-compatible and provides an internal 4MHz oscillator, hardware USART, 2 comparators, and 3.5KB Flash.
