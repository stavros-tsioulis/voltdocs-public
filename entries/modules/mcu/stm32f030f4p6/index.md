## Overview

The **STM32F030F4P6** is a budget-tier 32-bit ARM Cortex-M0 microcontroller manufactured by STMicroelectronics. Available in a compact, hand-solderable 20-pin **TSSOP-20** package, it brings 32-bit processing power and advanced peripherals into entry-level and price-sensitive hardware designs.

Running at clock speeds up to **$48\text{ MHz}$**, the STM32F030F4P6 features **$16\text{ KB}$ of Flash memory**, **$4\text{ KB}$ of SRAM**, an **11-channel 12-bit $1.0\ \mu\text{s}$ ADC**, a 16-bit advanced motor-control timer with 6 PWM channels and dead-time generation, and hardware serial peripherals (I2C with Fast-Mode Plus 1MHz, SPI up to 18 Mbit/s, and USART). It is widely used across maker projects for mini quadcopter speed controllers (BLHeli ESCs), smart LED drivers, sensor interfaces, and compact custom breakout boards.

## Quick reference

| | |
|---|---|
| **CPU Core** | ARM 32-bit Cortex-M0 RISC |
| **Package** | 20-pin TSSOP (TSSOP-20 / 6.5 x 4.4 mm) |
| **Max Clock Frequency** | $48\text{ MHz}$ |
| **Flash Memory** | $16\text{ KB}$ non-volatile program storage |
| **SRAM** | $4\text{ KB}$ with parity check |
| **Supply Voltage Range** | $2.4\text{ V}$ to $3.6\text{ V}$ DC ($3.3\text{ V}$ nominal) |
| **GPIO Count** | 15 I/Os (Up to 12 are 5V-tolerant) |
| **ADC** | 12-bit resolution, $1.0\ \mu\text{s}$ conversion time (Up to 11 channels) |
| **Advanced Timer** | 1x 16-bit Motor Control Timer (TIM1) with complementary PWM outputs |
| **Communication** | 1x USART, 1x SPI (18 Mbps), 1x I2C (Fast Mode+ 1MHz) |
| **Programming / Debug** | Serial Wire Debug (SWD: `SWCLK` / `SWDIO`) |

## Pinout (TSSOP-20 Package)

```
                       ┌───┴───┐
       (BOOT0) BOOT0  1│ 1   20│ PA14 (SWCLK / USART1_TX)
 (OSC_IN) PF0 / PA0   2│       │19 PA13 (SWDIO / IR_OUT)
(OSC_OUT) PF1 / PA1   3│STM32F0│18 PA10 (USART1_RX / TIM1_CH3)
        (Active-Low) NRST 4│  030F4 │17 PA9  (USART1_TX / TIM1_CH2 / I2C1_SCL)
                VDDA  5│ TSSOP │16 VDD  (Digital Supply +3.3V)
     (ADC_IN0) PA0    6│  -20  │15 VSS  (Ground 0V)
     (ADC_IN1) PA1    7│       │14 PB1  (TIM3_CH4 / TIM1_CH3N)
     (ADC_IN2) PA2    8│       │13 PA7  (ADC_IN7 / TIM1_CH1N / SPI1_MOSI)
     (ADC_IN3) PA3    9│       │12 PA6  (ADC_IN6 / TIM3_CH1 / SPI1_MISO)
     (ADC_IN4) PA4   10│       │11 PA5  (ADC_IN5 / TIM2_CH1 / SPI1_SCK)
                       └───────┘
```

| Pin | Name | Type | Key Multiplexed Functions |
|---|---|---|---|
| 1 | `BOOT0` | Digital Input | Boot configuration (Pull to GND via $10\text{ k}\Omega$ for Flash execution) |
| 2 | `PF0` / `OSC_IN` | GPIO / Clock | High-speed external crystal input or GPIO |
| 3 | `PF1` / `OSC_OUT`| GPIO / Clock | High-speed external crystal output or GPIO |
| 4 | `NRST` | Reset | Active-LOW microcontroller reset with internal weak pull-up |
| 5 | `VDDA` | Power Input | Analog power supply rail (Connect to VDD with $100\text{ nF} + 1\ \mu\text{F}$ bypass) |
| 6 | `PA0` | GPIO / Analog | `ADC_IN0` / `USART1_CTS` / `TIM2_CH1_ETR` |
| 7 | `PA1` | GPIO / Analog | `ADC_IN1` / `USART1_RTS` / `TIM2_CH2` |
| 8 | `PA2` | GPIO / Analog | `ADC_IN2` / `USART1_TX` / `TIM2_CH3` |
| 9 | `PA3` | GPIO / Analog | `ADC_IN3` / `USART1_RX` / `TIM2_CH4` |
| 10 | `PA4` | GPIO / Analog | `ADC_IN4` / `SPI1_NSS` / `TIM14_CH1` |
| 11 | `PA5` | GPIO / Analog | `ADC_IN5` / `SPI1_SCK` / `TIM2_CH1` |
| 12 | `PA6` | GPIO / Analog | `ADC_IN6` / `SPI1_MISO` / `TIM3_CH1` / `TIM1_BKIN` |
| 13 | `PA7` | GPIO / Analog | `ADC_IN7` / `SPI1_MOSI` / `TIM3_CH2` / `TIM1_CH1N` |
| 14 | `PB1` | GPIO / Digital | `TIM3_CH4` / `TIM1_CH3N` / `TIM14_CH1` |
| 15 | `VSS` | Ground | Common Ground reference ($0\text{ V}$) |
| 16 | `VDD` | Power Input | Digital Core and I/O Supply ($+2.4\text{ V}$ to $+3.6\text{ V}$) |
| 17 | `PA9` | GPIO / Digital | `USART1_TX` / `I2C1_SCL` / `TIM1_CH2` (5V-tolerant) |
| 18 | `PA10` | GPIO / Digital | `USART1_RX` / `I2C1_SDA` / `TIM1_CH3` (5V-tolerant) |
| 19 | `PA13` | GPIO / Debug | `SWDIO` (Serial Wire Data Input/Output) |
| 20 | `PA14` | GPIO / Debug | `SWCLK` (Serial Wire Clock) |

## Minimal Circuit & Programming Hookup

```
                       +3.3V DC Regulated
                              │
               ┌──────────────┼───────────────┐
               │              │               │
         [Pin 16: VDD]  [Pin 5: VDDA]         │
               │              │          [ 10kΩ Pull-Down ]
        [ 100nF Cap ]  [ 100nF Cap ]          │
               │              │         [Pin 1: BOOT0]
               └──────────────┼───────────────┘
                              │
  ST-Link V2 Debugger         │
  ┌─────────────────┐         │
  │ SWCLK ──────────┼─────────┼──────────────► [Pin 20: PA14 / SWCLK]
  │ SWDIO ──────────┼─────────┼──────────────► [Pin 19: PA13 / SWDIO]
  │ NRST (Optional) ┼─────────┼──────────────► [Pin 4: NRST] ──[ 100nF Cap ]── GND
  │ GND ────────────┼─────────┴──────────────► [Pin 15: VSS] ── Common GND
  └─────────────────┘
```

## Common mistakes

- **Leaving BOOT0 floating:** If Pin 1 (`BOOT0`) floats, the MCU may randomly power up into the system ROM UART bootloader instead of running user firmware from Flash. Always pull Pin 1 to **GND via a $10\text{ k}\Omega$ resistor**.
- **Leaving VDDA disconnected:** Pin 5 (`VDDA`) supplies the internal analog domain and power-on reset circuitry. If `VDDA` is not connected to `+3.3V`, the chip will not start. Connect Pin 5 directly to `VDD` (Pin 16) with a $100\text{ nF}$ bypass capacitor.
- **Overwriting SWD pins in firmware:** Reconfiguring PA13 or PA14 as regular GPIO outputs without delay will lock out the SWD programmer on subsequent boots. To recover, hold `NRST` LOW (or pull `BOOT0` HIGH) while initiating the flash command ("Connect Under Reset").

## Notes

- **Software Toolchains:** Supported natively by STM32CubeIDE, Keil MDK, PlatformIO, and the official `STM32duino` Arduino core.
