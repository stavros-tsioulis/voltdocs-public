## Overview

The **MSP430G2553** is a 16-bit ultra-low-power RISC microcontroller manufactured by Texas Instruments. Available in an easy-to-prototype through-hole **DIP-20** package (as well as TSSOP-20 and QFN-32), it is the premier microcontroller that shipped with the iconic **TI MSP-EXP430G2 LaunchPad** evaluation kit.

Operating from **$1.8\text{V}$ to $3.6\text{V}$ DC** at up to **$16\text{ MHz}$**, the MSP430G2553 is renowned for its energy-saving architectures: drawing just **$0.1\ \mu\text{A}$ in RAM-retention standby (LPM4)**, **$0.5\ \mu\text{A}$ in real-time clock mode (LPM3)**, and **$230\ \mu\text{A}/\text{MHz}$ in active mode**. Featuring an 8-channel 10-bit $200\text{ ksps}$ ADC with internal temperature sensor, dual 16-bit timers, hardware Universal Serial Communication Interface (**USCI** supporting hardware UART, SPI, and I2C), and capacitive-touch PinOsc hardware, it is a staple for battery-powered data loggers, wireless sensors, and energy-harvesting gadgets.

## Quick reference

| | |
|---|---|
| **CPU Core** | 16-bit MSP430 RISC Architecture |
| **Package** | 20-pin DIP (DIP-20 / N20) / 20-pin TSSOP / 32-pin QFN |
| **Max Clock Frequency** | $16\text{ MHz}$ (Calibrated internal DCO) |
| **Flash Memory** | $16\text{ KB}$ non-volatile program memory |
| **SRAM** | $512\text{ Bytes}$ high-speed RAM |
| **Supply Voltage Range** | $1.8\text{ V}$ to $3.6\text{ V}$ DC ($4.1\text{ V}$ absolute max) |
| **Low-Power Modes** | LPM3 (RTC): $0.5\ \mu\text{A}$ / LPM4 (Off): $0.1\ \mu\text{A}$ |
| **Analog Peripherals** | 10-bit 200 ksps SAR ADC (8 channels) + Temp Sensor + Comparator |
| **Serial Communication** | USCI_A0 (UART / IrDA / SPI) + USCI_B0 (SPI / I2C) |
| **Debugging Interface** | Spy-Bi-Wire (2-wire JTAG: `SBWTDIO` / `SBWTCK`) |

## Pinout (DIP-20 Package)

```
                       ┌───┴───┐
                  VCC 1│ 1   20│ GND (DVSS)
     (A0/PinOsc) P1.0 2│       │19 P2.7 (XOUT)
(TA0.0/UCA0RXD) P1.1 3│       │18 P2.6 (XIN)
(TA0.1/UCA0TXD) P1.2 4│       │17 TEST / SBWTCK
       (ADC10CLK) P1.3 5│MSP430│16 RST / NMI / SBWTDIO
(TA0.1/UCB0CLK) P1.4 6│ G2553 │15 P1.7 (UCB0SDA / SCLK)
(TA0.0/UCB0SOMI)P1.5 7│       │14 P1.6 (UCB0SCL / MISO / TA0.1)
                 P2.0 8│       │13 P2.5 (TA1.2)
                 P2.1 9│       │12 P2.4 (TA1.2)
                 P2.2 10│      │11 P2.3 (TA1.0)
                       └───────┘
```

| Pin | Name | Primary & Multiplexed Functions |
|---|---|---|
| 1 | `VCC` | Power Supply ($+1.8\text{ V}$ to $+3.6\text{ V}$ DC) |
| 2 | `P1.0` | GPIO / ADC Input `A0` / Capacitive Touch `PinOsc` / Red LED on LaunchPad |
| 3 | `P1.1` | GPIO / `TA0.0` / UART Receive `UCA0RXD` / ADC `A1` |
| 4 | `P1.2` | GPIO / `TA0.1` / UART Transmit `UCA0TXD` / ADC `A2` |
| 5 | `P1.3` | GPIO / ADC `A3` / Push Button on LaunchPad |
| 6 | `P1.4` | GPIO / `TA0.1` / SPI `UCB0CLK` / ADC `A4` |
| 7 | `P1.5` | GPIO / `TA0.0` / SPI `UCB0SOMI` / I2C / ADC `A5` |
| 8, 9, 10 | `P2.0`-`P2.2` | Port 2 GPIOs / Timer1_A Outputs |
| 11, 12, 13 | `P2.3`-`P2.5` | Port 2 GPIOs / Timer1_A Outputs |
| 14 | `P1.6` | GPIO / `TA0.1` / SPI `UCB0SOMI` / I2C `UCB0SCL` / ADC `A6` / Green LED |
| 15 | `P1.7` | GPIO / SPI `UCB0SIMO` / I2C `UCB0SDA` / ADC `A7` |
| 16 | `RST` | Reset (Active Low) / `SBWTDIO` (Spy-Bi-Wire Data) |
| 17 | `TEST` | Test Mode Select / `SBWTCK` (Spy-Bi-Wire Clock) |
| 18, 19 | `P2.6`, `P2.7` | GPIO / $32.768\text{ kHz}$ Crystal Inputs (`XIN`, `XOUT`) |
| 20 | `GND` | Common Ground ($0\text{ V}$) |

## Minimal Standalone Breadboard Circuit

```
                      +3.3V DC (From MCP1700 or 2x AA Batteries)
                         │
                         ├───[ 100nF Ceramic ]───┐
                         │                       │
     LaunchPad / FET ────┼────────[ 47kΩ ]───┐   │
     Debugger Header     │                   │   │
                         │             [Pin 1: VCC]
                         │                   │
   [SBWTDIO / RST] ──────┼─────────────► [Pin 16: RST]
                         │                   │
                         │             [ 1.1nF Cap ] (Keep <= 2.2nF for SBW)
                         │                   │
   [SBWTCK / TEST] ──────┼─────────────► [Pin 17: TEST]
                         │                   │
   [GND] ────────────────┴─────────────► [Pin 20: GND] ─── System GND
```

## Low-Power Modes (LPM)

1. **Active Mode:** CPU and all peripherals active ($\sim 230\ \mu\text{A}/\text{MHz}$ at $3.0\text{V}$).
2. **LPM0:** CPU disabled, DCO and clocks active ($\sim 55\ \mu\text{A}$).
3. **LPM3:** CPU and high-speed DCO disabled; $32.768\text{ kHz}$ low-speed crystal (ACLK) running for RTC wakeups ($\sim 0.5\ \mu\text{A}$).
4. **LPM4:** All clocks stopped; full RAM contents retained; wake up by external GPIO interrupt within $< 1\ \mu\text{s}$ ($\sim 0.1\ \mu\text{A}$).

## Common mistakes

- **Connecting to 5V power or 5V logic signals:** The MSP430G2553 is strictly a **$3.6\text{V}$ max device**. Connecting $5.0\text{V}$ power or driving GPIOs with 5V TTL logic directly will destroy the chip's internal clamping diodes. Use a 3.3V regulator and logic level shifters.
- **Placing too large a capacitor on the RST pin during Spy-Bi-Wire debugging:** The reset pin is multiplexed with the high-speed `SBWTDIO` programming data line. If the pull-up filter capacitor on RST exceeds **$2.2\text{ nF}$**, programming tools (LaunchPad / MSP-FET) will fail to communicate. Use a **$47\text{ k}\Omega$ pull-up resistor** and a **$1.0\text{ nF}$** capacitor.

## Notes

- **Software Ecosystem:** Programmable via TI Code Composer Studio (CCS), IAR Embedded Workbench, GCC (`msp430-elf-gcc`), and the open-source **Energia** (Arduino-compatible framework).
