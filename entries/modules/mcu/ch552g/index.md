## Overview

The **CH552G** is an ultra-low-cost enhanced 8-bit E8051-core microcontroller manufactured by WCH (Nanjing Qinheng Microelectronics). Available in a compact **SOP-16** surface-mount package, it integrates a hardware **USB 2.0 Full-Speed device/host controller and transceiver** with built-in capacitive touch detection and an on-chip factory USB bootloader.

Costing under $\$0.30$, the CH552G replaces expensive legacy USB microcontrollers (like the ATmega32U4) for simple USB peripheral projects. Because it executes single-cycle instructions (**1T architecture**) at up to **$24\text{ MHz}$**, it performs 8x to 15x faster than standard 8051 processors. Featuring open-source toolchain support (SDCC and the **ch55xduino** Arduino core), the CH552G is widely used in DIY **macro-pads, custom mechanical keyboards, USB HID mouse/joystick emulators, USB-to-UART bridges, and hardware security keys**.

## Quick reference

| | |
|---|---|
| **CPU Core** | Enhanced E8051 (1T Single Clock Architecture) |
| **Package** | SOP-16 (CH552G) / TSSOP-20 (CH552T) / MSOP-10 (CH552E) |
| **Max Clock Frequency** | $24\text{ MHz}$ internal RC oscillator ($\pm 0.5\%$ accuracy) |
| **Flash Memory** | $16\text{ KB}$ ($14\text{ KB}$ user code + $2\text{ KB}$ pre-flashed USB bootloader) |
| **SRAM** | $1280\text{ Bytes}$ ($256\text{ B}$ internal RAM + $1024\text{ B}$ xRAM) |
| **Data Flash** | $128\text{ Bytes}$ non-volatile data storage |
| **Operating Voltage Range** | $2.8\text{ V}$ to $5.0\text{ V}$ DC (Built-in $3.3\text{ V}$ LDO for USB transceiver) |
| **USB Peripheral** | USB 2.0 Full-Speed (12 Mbps) Device / Host with built-in transceiver |
| **Analog & Touch** | 6-channel Capacitive Touch-Key + 4-channel 8-bit ADC |
| **Serial Interfaces** | 2x UART, 1x SPI, 3x Timers, 2x PWM channels |

## Pinout (SOP-16 Package)

```
                       ┌───┴───┐
     (AIN3/INT0) P3.2 1│ 1   16│ P1.3 (XO / TXD)
     (AIN1/UCC1) P1.4 2│       │15 VCC (Power In)
     (AIN2/MOSI) P1.5 3│       │14 GND
     (RXD1/MISO) P1.6 4│ CH552G│13 P3.7 / UDM (USB D-)
      (SCK/TXD1) P1.7 5│ SOP-16│12 P3.6 / UDP (USB D+)
   (Active-High) RESET 6│       │11 P3.4 (PWM2 / T0)
       (PWM2/TXD) P3.1 7│       │10 V33 (3.3V LDO Output)
                   GND 8│       │9  P3.0 (PWM1 / RXD)
                       └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `P3.2` | GPIO / Analog | `INT0` / `AIN3` / `TXD1` / `VBUS` detection |
| 2 | `P1.4` | GPIO / Analog | `AIN1` / `TIN2` / `T2` / SPI `SCS` / Touch Key 2 |
| 3 | `P1.5` | GPIO / Analog | `AIN2` / `MOSI` / `PWM1` / Touch Key 3 |
| 4 | `P1.6` | GPIO / Digital | `MISO` / `RXD1` / `TIN4` / Touch Key 4 |
| 5 | `P1.7` | GPIO / Digital | `SCK` / `TXD1` / `TIN5` / Touch Key 5 |
| 6 | `RESET` | Digital Input | External Hardware Reset (Active-HIGH, internal pull-down) |
| 7 | `P3.1` | GPIO / Digital | `PWM2` / UART0 `TXD` |
| 8, 14 | `GND` | Power | Common Ground ($0\text{ V}$) |
| 9 | `P3.0` | GPIO / Digital | `PWM1` / UART0 `RXD` |
| 10 | `V33` | Power Output/Input | Internal $3.3\text{V}$ LDO output (Connect $0.1\ \mu\text{F}$ bypass cap to GND) |
| 11 | `P3.4` | GPIO / Digital | `PWM2` / `RXD1` / Timer0 `T0` |
| 12 | `P3.6 / UDP` | USB Data | USB $D+$ Signal (Direct connection to USB Type-C/A D+ pad) |
| 13 | `P3.7 / UDM` | USB Data | USB $D-$ Signal (Direct connection to USB Type-C/A D- pad) |
| 15 | `VCC` | Power Input | Main $+5\text{V}$ (or $+3.3\text{V}$) DC power rail from USB VBUS |
| 16 | `P1.3` | GPIO / Digital | Clock Output / `TXD` |

## Minimal USB Peripheral Hookup

```
         USB Type-C / USB-A Connector
         ┌───────────────────────────┐
         │ VBUS (+5V) ───────────────┼─────────┬──────────────► [Pin 15: VCC]
         │                           │         │                     CH552G
         │                           │   [ 100nF Cap ]               SOP-16
         │                           │         │              [Pin 10: V33] ──[ 100nF Cap ]── GND
         │                           │         │
         │ D- ───────────────────────┼─────────┼──────────────► [Pin 13: UDM / P3.7]
         │ D+ ───────────────────────┼─────────┼──────────────► [Pin 12: UDP / P3.6]
         │                           │         │
         │ GND ──────────────────────┼─────────┴──────────────► [Pin 8, 14: GND]
         └───────────────────────────┘
```

## Flashing & Bootloader Mode

The CH552 comes with a factory-programmed USB ISP bootloader in hardware ROM:
- **Entering Bootloader:** Hold `P3.6 / UDP` (Pin 12) pulled to $+3.3\text{V}$ (`V33`) while inserting the USB cable (or during power-on/reset).
- **Flashing Software:** Open-source command-line flashers such as **`vnproch55x`**, **`wchisp`**, or the Arduino IDE with the **ch55xduino** board package can flash user code directly over USB in $< 2\text{ seconds}$.

## Common mistakes

- **Adding series resistors to USB D+ / D- lines:** Unlike STM32 or AVR microcontrollers that require $22\ \Omega$ series damping resistors, the CH552 has internal integrated termination matching resistors. Adding external series resistors will cause USB enumeration errors. Connect `UDP` and `UDM` directly to the USB connector.
- **Forgetting the capacitor on Pin 10 (`V33`):** Pin 10 is the internal 3.3V power regulator for the USB physical PHY. If $VCC = 5\text{V}$, Pin 10 must have a $100\text{ nF}$ ceramic bypass capacitor connected to GND. If powered from a $3.3\text{V}$ rail, tie Pin 10 directly to Pin 15 (`VCC`).
- **Active-HIGH Reset:** The `RESET` pin on the CH552 is **Active-HIGH** (standard 8051 convention), unlike AVR/ARM/STM32 where reset is Active-LOW (`NRST`). Leaving it disconnected is fine as it has an internal pull-down.

## Notes

- **Pin Count Variants:** CH552E (MSOP-10, ultra-compact), CH552G (SOP-16, standard), CH552T (TSSOP-20, full GPIO breakout).
