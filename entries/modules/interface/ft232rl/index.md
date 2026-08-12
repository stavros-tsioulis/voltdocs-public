## Overview

The **FT232RL** is an iconic USB-to-serial UART interface IC manufactured by FTDI (Future Technology Devices International). As one of the most famous chips in USB peripheral history, it converts USB 2.0 signals into asynchronous serial UART data with full hardware handshaking lines.

Featuring an **internal integrated clock oscillator** (eliminating external crystals), **128-byte internal EEPROM** for custom USB Vendor ID (VID), Product ID (PID), and serial strings, and **CBUS multi-function GPIO pins** (for LED status indicators), the FT232RL supports baud rates from **300 bps to 3 Mbps** at TTL signal levels.

## Quick reference

| | |
|---|---|
| **USB Specification** | USB 2.0 Full-Speed ($12\text{ Mbps}$) |
| **Supply Voltage (`VCC`)** | 3.3 V to 5.25 V DC |
| **Internal LDO Regulator** | $3.3\text{ V}$ DC ($50\text{ mA}$ max output on 3V3OUT pin) |
| **Max Baud Rate** | $3.0\text{ Mbps}$ (RS-422 / RS-485 / TTL logic) |
| **Internal EEPROM** | 128 Bytes (Stores custom VID, PID, Product Name, Serial Number) |
| **Clock Source** | Integrated Internal Clock Generator (No external crystal needed) |
| **Buffer Sizes** | 128-byte Receive Buffer, 256-byte Transmit Buffer |
| **Package** | 28-pin SSOP / 32-pin QFN |

## Pinout (SSOP-28 Package)

```
             ┌───┴───┐
       TXD  1│ 1   28│ OSCO (NC)
       DTR  2│       │27 OSCI (NC)
       RTS  3│       │26 TEST (GND)
     VCCIO  4│ FT232 │25 AGND
        RXD 5│   RL  │24 NC
       RI   6│       │23 CBUS0 (TXLED)
       GND  7│       │22 CBUS1 (RXLED)
        NC  8│       │21 GND
       DSR  9│       │20 VCC (+5V)
       DCD 10│       │19 RESET (VCC)
       CTS 11│       │18 CBUS2
     CBUS4 12│       │17 3V3OUT (3.3V Out)
       SSD 13│       │16 USBDM (D-)
     USBDP 14│       │15 USBDM / USBDP
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `TXD` | Output | Transmit Asynchronous Data Output (Connect to MCU RXD) |
| 2 | `DTR` | Output | Data Terminal Ready Handshake Line (Used for Arduino Auto-Reset) |
| 3 | `RTS` | Output | Request to Send Control Line |
| 4 | `VCCIO` | Power | Power supply pin for UART I/O pins (+1.8V to +5.25V DC) |
| 5 | `RXD` | Input | Receive Asynchronous Data Input (Connect to MCU TXD) |
| 7 | `GND` | Power | Ground reference (0 V) |
| 15 | `USBDM` | I/O | USB D- Differential Data Line |
| 16 | `USBDP` | I/O | USB D+ Differential Data Line |
| 17 | `3V3OUT` | Output | 3.3V Internal LDO Regulator Output (Requires 0.1µF decoupling cap) |
| 20 | `VCC` | Power | Main Power Supply (+4.0V to +5.25V DC) |
| 22 | `CBUS1` | I/O | Multi-function Configurable Pin 1 (Default RX LED Drive) |
| 23 | `CBUS0` | I/O | Multi-function Configurable Pin 0 (Default TX LED Drive) |

## Arduino Uno / Pro Mini Auto-Reset Circuit

```
  FT232RL DTR (Pin 2) ───[ 0.1µF Ceramic Cap ]───┬─── ATmega328P RESET Pin
                                                 │
                                         [ 10kΩ Pullup to 5V ]
```

## Common mistakes

- **Leaving `VCCIO` (Pin 4) floating:** `VCCIO` determines the voltage level of the UART signal pins (TXD, RXD, RTS, CTS). Tie `VCCIO` to **`VCC` (+5V)** for 5V TTL logic, or to **`3V3OUT` (Pin 17)** for 3.3V logic. Leaving `VCCIO` unpowered stops UART communication.
- **Forgetting `TEST` (Pin 26) ground connection:** Pin 26 is a factory test pin that **must be tied directly to GND**. Leaving `TEST` floating puts the chip into test mode.

## Notes

- **FT232RL vs CH340G vs CP2102:** FT232RL has integrated EEPROM and Configurable CBUS pins for custom hardware behavior; CH340G is a budget alternative requiring a 12MHz crystal; CP2102 is a compact 5x5 QFN alternative.
