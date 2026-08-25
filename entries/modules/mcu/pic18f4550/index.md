## Overview

The **PIC18F4550** is a high-performance enhanced Flash 8-bit microcontroller manufactured by Microchip Technology. Available in a 40-pin through-hole **DIP-40** package (as well as 44-pin TQFP/QFN), it was Microchip's flagship USB microcontroller that brought native **USB 2.0 Full-Speed (12 Mbps)** capabilities to the 8-bit PIC family.

Operating at clock frequencies up to **$48\text{ MHz}$ ($12\text{ MIPS}$)** via its internal 96MHz PLL, the PIC18F4550 combines **$32\text{ KB}$ of Flash memory**, **$2048\text{ Bytes}$ of RAM** (including 1KB dual-port RAM dedicated to USB endpoints), **$256\text{ Bytes}$ EEPROM**, a **13-channel 10-bit $100\text{ ksps}$ ADC**, an Enhanced CCP (ECCP) PWM module with full-bridge motor control, and Master Synchronous Serial Port (MSSP for SPI and I2C). It famously powered the open-source **PICkit 2 programmer clones**, DIY USB oscilloscopes, flight-simulator joystick panels, and custom USB HID peripherals.

## Quick reference

| | |
|---|---|
| **CPU Core** | 8-bit PIC18 RISC (75 instructions + 8 extended instructions) |
| **Package** | 40-pin DIP (DIP-40 / PDIP-40) / 44-pin TQFP / 44-pin QFN |
| **Max Clock Frequency** | $48\text{ MHz}$ ($12\text{ MIPS}$ instruction execution) |
| **USB Peripheral** | Universal Serial Bus 2.0 Full-Speed (12 Mbps) / Low-Speed (1.5 Mbps) |
| **Flash Program Memory** | 32768 bytes ($32\text{ KB}$, 16384 words) |
| **Data RAM** | 2048 bytes ($2\text{ KB}$, including 1KB dedicated USB buffer RAM) |
| **Data EEPROM** | 256 bytes true non-volatile EEPROM |
| **Operating Voltage (`VDD`)** | $4.2\text{ V}$ to $5.5\text{ V}$ DC (USB operation) / $2.0\text{V} \dots 5.5\text{V}$ (PIC18LF4550) |
| **GPIO Count** | 35 I/O pins (Ports A, B, C, D, E) |
| **ADC Channels** | 13 channels (10-bit resolution, 100 ksps) |
| **PWM / Timers** | 1x ECCP (Full Bridge) + 1x CCP + 4 Timers (Timer0/1/2/3) |
| **Serial Bus** | Enhanced USART (LIN / Auto-baud), MSSP (SPI / I2C) |

## Pinout (DIP-40 Package)

```
                            ┌───┴───┐
      (Active-Low) MCLR/VPP 1│ 1   40│ RB7 (KBI3/PGD)
          (AN0/C1IN-) RA0   2│       │39 RB6 (KBI2/PGC)
          (AN1/C2IN-) RA1   3│       │38 RB5 (KBI1/PGM)
        (AN2/VREF-/CVREF)RA2 4│       │37 RB4 (KBI0/AN11)
             (AN3/VREF+) RA3 5│PIC18F│36 RB3 (AN9/CCP2/VPO)
          (T0CKI/C1OUT) RA4 6│ 4550  │35 RB2 (AN8/INT2/VMO)
          (AN4/SS/HLVD) RA5 7│DIP-40 │34 RB1 (AN10/INT1/SCK/SCL)
             (AN5/CK1SP) RE0 8│       │33 RB0 (AN12/INT0/FLT0/SDI/SDA)
             (AN6/CK2SP) RE1 9│       │32 VDD (+5V Digital)
             (AN7/OESPR) RE2 10│      │31 VSS (GND)
                    VDD 11│       │30 RD7 (PSP7)
                    VSS 12│       │29 RD6 (PSP6)
      (OSC1/CLKI/RA7)  OSC1 13│      │28 RD5 (PSP5/P1B)
      (OSC2/CLKO/RA6)  OSC2 14│      │27 RD4 (PSP4/P1D)
              (T1OSO/T13CKI) RC0 15│ │26 RC7 (RX/DT/SDO)
             (T1OSI/CCP2) RC1 16│     │25 RC6 (TX/CK)
             (CCP1/P1A) RC2 17│       │24 RC5 (D+ / VP)
             (USB 3.3V) VUSB 18│      │23 RC4 (D- / VM)
             (SPP0/RD0) RD0 19│       │22 RD3 (PSP3)
             (SPP1/RD1) RD1 20│       │21 RD2 (PSP2)
                            └───────┘
```

## Minimal Circuit & USB Hookup

```
         USB Type-B / Type-C Connector
         ┌─────────────────────────────┐
         │ VBUS (+5V) ─────────────────┼─────────┬──────────────► [Pin 11 & 32: VDD]
         │                             │         │                     PIC18F4550
         │                             │   [ 100nF Cap ]               DIP-40
         │                             │         │              [Pin 18: VUSB] ──[ 470nF Cap ]── GND
         │                             │         │
         │ D- ─────────────────────────┼─────────┼──────────────► [Pin 23: RC4 / D-]
         │ D+ ─────────────────────────┼─────────┼──────────────► [Pin 24: RC5 / D+]
         │                             │         │
         │ GND ────────────────────────┼─────────┴──────────────► [Pin 12 & 31: VSS]
         └─────────────────────────────┘
         
  20MHz Crystal + Internal 96MHz PLL Configuration:
    OSC1 (Pin 13) ───┬───[ 20MHz Crystal ]───┬─── OSC2 (Pin 14)
                     │                       │
               [ 22pF Cap ]             [ 22pF Cap ]
                     │                       │
                    GND                     GND
```

## Common mistakes

- **Missing the VUSB bypass capacitor:** Pin 18 (`VUSB`) is the output of the internal 3.3V USB regulator. If using the internal transceiver, Pin 18 **must be connected to ground through a $220\text{ nF}$ to $470\text{ nF}$ low-ESR ceramic capacitor**. Without this capacitor, the USB engine will fail to initialize or drop packets.
- **Incorrect Configuration Fuses for USB Clock:** To operate the USB engine at 48MHz from a 20MHz crystal, the configuration bits must divide by 5 (`PLLDIV = 5`), enable the 96MHz PLL (`CPUDIV = OSC1_PLL2`), and select the USB clock from PLL (`USBDIV = 2`).

## Notes

- **Programming:** Supported by PICkit 2/3/4, MPLAB ICD, and custom USB bootloaders using MPLAB X IDE and the XC8 compiler.
