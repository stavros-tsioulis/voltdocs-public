## Overview

The **CP2102** (CP2102-GM / CP2102N) is a single-chip USB-to-UART bridge controller IC manufactured by Silicon Labs. It is one of the most widely integrated USB serial bridge chips in embedded systems, widely featured on ESP8266 NodeMCU, ESP32 development boards, custom Arduino clones, and USB-to-TTL serial adapter cables.

The CP2102 integrates a USB 2.0 Full-Speed function controller, USB transceiver, internal voltage regulator, internal EEPROM, and an **internal precision clock oscillator**, requiring **zero external clock crystals** or passive timing components. It handles UART baud rates up to **921,600 bps** (and up to $3\text{ Mbps}$ on CP2102N).

## Quick reference

| | |
|---|---|
| **USB Specification** | USB 2.0 Full-Speed ($12\text{ Mbps}$) |
| **Supply Voltage (`VDD`)** | 3.0 V to 3.6 V DC (Powered from USB +5V via internal 3.3V LDO) |
| **Internal Regulator Output**| $3.3\text{ V}$ DC ($100\text{ mA}$ max output capability) |
| **Max Baud Rate** | $921,600\text{ bps}$ ($3\text{ Mbps}$ for CP2102N) |
| **Clock Source** | Integrated Precision Oscillator ($\pm 1.5\%$ accuracy) |
| **UART Signals** | TXD, RXD, RTS, CTS, DTR, DSR, DCD, RI |
| **Buffers** | 512-byte Receive buffer, 512-byte Transmit buffer |
| **Package** | 28-pin QFN ($5 \times 5\text{ mm}$) |

## Pinout (QFN-28 Package)

```
                     ┌──────────────────┐
                 D+ 1│1               28│ VDD (3.3V Output)
                 D- 2│                27│ REGIN (5V Input)
                GND 3│   CP2102-GM    26│ VBUS (USB Sense)
                 NC 4│    QFN-28      25│ NC
           RST/ /RST 5│                24│ NC
                 NC 6│                23│ CTS
                 NC 7│                22│ RTS
                     └──────────────────┘
                      8 9 10 11 12 13 14
                      N N N  N  N  T  R
                      C C C  C  C  X  X
                                   D  D
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `D+` | I/O | USB Differential Data Plus |
| 2 | `D-` | I/O | USB Differential Data Minus |
| 3 | `GND` | Power | Ground reference (0 V) |
| 8 | `VBUS` | Input | USB Bus Power Sense Input (Connect to USB 5V VBUS) |
| 9 | `RST` | Input | Active-LOW Reset Input |
| 23 | `CTS` | Input | Clear to Send Modem Control Line |
| 24 | `RTS` | Output | Request to Send Modem Control Line |
| 25 | `RXD` | Input | UART Serial Receive Input (Connect to MCU TXD) |
| 26 | `TXD` | Output | UART Serial Transmit Output (Connect to MCU RXD) |
| 27 | `REGIN` | Power | Integrated 5V LDO Regulator Input (Connect to USB 5V) |
| 28 | `VDD` | Power | Integrated 3.3V Regulator Output (Bypass with 4.7µF + 0.1µF) |

## ESP32 / ESP8266 Auto-Reset Circuit

The CP2102 `DTR` and `RTS` pins are commonly connected to an NPN dual-transistor circuit (S8050/BC847) to put ESP32 / ESP8266 microcontrollers into bootloader mode automatically during `esptool` flashing:

```
  CP2102 DTR ─────[ R1 10k ]───── Base Q2 (NPN) ─── Collector ─── ESP32 EN (RESET)
  CP2102 RTS ─────[ R2 10k ]───── Base Q1 (NPN) ─── Collector ─── ESP32 IO0 (BOOT)
```

## Common mistakes

- **Forgetting decoupling capacitors on VDD (Pin 28):** The internal 3.3V LDO regulator requires a $4.7\ \mu\text{F}$ tantalum or ceramic capacitor in parallel with a $0.1\ \mu\text{F}$ ceramic capacitor directly on `VDD` (Pin 28) for stable USB operation.
- **Floating `VBUS` (Pin 8):** In self-powered designs where the board has an independent 3.3V supply, `VBUS` must still be connected to the USB connector 5V line so the CP2102 detects when the USB cable is plugged in.

## Notes

- **CP2102 vs CP2102N vs CH340G:** CP2102 requires no external crystal and has integrated EEPROM; CP2102N is the pin-compatible replacement supporting faster baud rates ($3\text{ Mbps}$); CH340G is a budget Chinese competitor requiring an external $12\text{ MHz}$ crystal.
