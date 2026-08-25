## Overview

The **STM32G030F6P6** is a modern mainstream 32-bit ARM Cortex-M0+ microcontroller manufactured by STMicroelectronics. Available in a compact 20-pin **TSSOP-20** package, it represents the next-generation architecture superseding legacy STM32F0 and 8-bit microcontrollers (like the ATmega328P).

Running at an elevated clock frequency of **$64\text{ MHz}$**, the STM32G030F6P6 integrates **$32\text{ KB}$ of Flash memory**, **$8\text{ KB}$ of parity-checked SRAM**, a high-speed **$2.5\text{ Msps}$ 12-bit ADC** (with hardware oversampling up to 16-bit resolution), a 16-bit advanced motor-control timer, and dual hardware serial channels (2x I2C, 2x SPI, 2x USART). A major innovation of the STM32G0 architecture is its **consolidated single power-supply pinout** ($1\times V_{DD}$ and $1\times V_{SS}$), freeing up pins to offer **18 GPIO lines in a 20-pin package**.

## Quick reference

| | |
|---|---|
| **CPU Core** | ARM 32-bit Cortex-M0+ RISC |
| **Package** | 20-pin TSSOP (TSSOP-20 / 6.5 x 4.4 mm) |
| **Max Clock Frequency** | $64\text{ MHz}$ |
| **Flash Memory** | $32\text{ KB}$ non-volatile program memory |
| **SRAM** | $8\text{ KB}$ with hardware parity check |
| **Supply Voltage Range** | $2.0\text{ V}$ to $3.6\text{ V}$ DC ($3.3\text{ V}$ nominal) |
| **GPIO Count** | 18 I/Os (16 are 5V-tolerant) |
| **High-Speed ADC** | 12-bit resolution, $0.4\ \mu\text{s}$ ($2.5\text{ Msps}$), hardware oversampling |
| **Timers** | 1x Advanced Motor Timer (TIM1), 4x 16-bit GP Timers, 1x Low-Power Timer |
| **Serial Communication** | 2x USART (Auto-baud), 2x SPI (32 Mbps), 2x I2C (Fast Mode+ 1MHz) |
| **Programming / Debug** | Serial Wire Debug (SWD: `SWCLK` / `SWDIO` on PA14/PA13) |

## Pinout (TSSOP-20 Package)

```
                       ┌───┴───┐
             PB7 / PB8 1│ 1   20│ PB3 / PB4 / PB5 / PB6
    PC14-OSC32_IN / PB9 2│       │19 PA14-BOOT0 / PA15 (SWCLK)
         PC15-OSC32_OUT 3│STM32G0│18 PA13 (SWDIO / IR_OUT)
       (Power +3.3V) VDD 4│ 030F6 │17 PA12 [PA10] (USART1_TX)
         (Ground 0V) VSS 5│ TSSOP │16 PA11 [PA9]  (USART1_RX / I2C1_SCL)
        (Active-Low) NRST 6│  -20  │15 PA8 (TIM1_CH1 / MCO)
             (ADC_IN0) PA0 7│       │14 PA7 (ADC_IN7 / SPI1_MOSI)
             (ADC_IN1) PA1 8│       │13 PA6 (ADC_IN6 / SPI1_MISO)
             (ADC_IN2) PA2 9│       │12 PA5 (ADC_IN5 / SPI1_SCK)
            (ADC_IN3) PA3 10│       │11 PA4 (ADC_IN4 / SPI1_NSS)
                       └───────┘
```

| Pin | Name | Type | Key Multiplexed Functions |
|---|---|---|---|
| 1 | `PB7 / PB8` | GPIO / Digital | `I2C1_SDA` / `USART2_TX` / `TIM16_CH1` |
| 2 | `PC14 / PB9` | GPIO / Clock | $32.768\text{ kHz}$ Crystal Input or `I2C1_SCL` |
| 3 | `PC15` | GPIO / Clock | $32.768\text{ kHz}$ Crystal Output or GPIO |
| 4 | `VDD / VDDA` | Power Input | Consolidated Core and Analog Supply ($+2.0\text{ V}$ to $+3.6\text{ V}$) |
| 5 | `VSS / VSSA` | Ground | Common Ground Reference ($0\text{ V}$) |
| 6 | `NRST / PF2` | Reset / GPIO | Active-LOW Reset or GPIO |
| 7, 8 | `PA0`, `PA1` | GPIO / Analog | `ADC_IN0`, `ADC_IN1` / `USART2_CTS`, `USART2_RTS` |
| 9, 10 | `PA2`, `PA3` | GPIO / Analog | `ADC_IN2`, `ADC_IN3` / `USART2_TX`, `USART2_RX` |
| 11, 12 | `PA4`, `PA5` | GPIO / Analog | `ADC_IN4`, `ADC_IN5` / `SPI1_NSS`, `SPI1_SCK` |
| 13, 14 | `PA6`, `PA7` | GPIO / Analog | `ADC_IN6`, `ADC_IN7` / `SPI1_MISO`, `SPI1_MOSI` |
| 15 | `PA8` | GPIO / Digital | `TIM1_CH1` / Master Clock Output (`MCO`) |
| 16 | `PA11 [PA9]` | GPIO / Digital | `I2C1_SCL` / `USART1_RX` / `TIM1_CH4` |
| 17 | `PA12 [PA10]`| GPIO / Digital | `I2C1_SDA` / `USART1_TX` / `TIM1_ETR` |
| 18 | `PA13` | GPIO / Debug | `SWDIO` (Serial Wire Data Input/Output) |
| 19 | `PA14-BOOT0` | GPIO / Debug | `SWCLK` (Serial Wire Clock) / `BOOT0` alternate function |
| 20 | `PB3 / PB4` | GPIO / Digital | `SPI1_SCK` / `SPI1_MISO` / `TIM1_CH2` |

## Minimal Circuit & Programming Connections

```
                     +3.3V Regulated DC
                             │
                      [Pin 4: VDD]
                             │
                      [ 100nF Ceramic Bypass ]
                             │
                      [Pin 5: VSS] ─── Common GND
                             │
  ST-Link V2 Debugger        │
  ┌────────────────┐         │
  │ SWCLK ─────────┼─────────┼──────────────► [Pin 19: PA14 / SWCLK]
  │ SWDIO ─────────┼─────────┼──────────────► [Pin 18: PA13 / SWDIO]
  │ NRST (Opt.) ───┼─────────┼──────────────► [Pin 6: NRST] ──[ 100nF Cap ]── GND
  │ GND ───────────┼─────────┴──────────────► Common Ground
  └────────────────┘
```

## STM32G030 vs STM32F030 vs ATmega328P

| Parameter | STM32G030F6P6 | STM32F030F4P6 | ATmega328P |
|---|---|---|---|
| **CPU Core** | 32-bit Cortex-M0+ | 32-bit Cortex-M0 | 8-bit AVR RISC |
| **Max Clock** | **$64\text{ MHz}$** | $48\text{ MHz}$ | $16\text{ MHz}$ |
| **Flash / SRAM** | **$32\text{ KB} / 8\text{ KB}$** | $16\text{ KB} / 4\text{ KB}$ | $32\text{ KB} / 2\text{ KB}$ |
| **GPIOs (TSSOP20/DIP28)**| **18 GPIOs** | 15 GPIOs | 23 GPIOs |
| **ADC Speed** | **$2.5\text{ Msps}$ (0.4 µs)** | $1.0\text{ Msps}$ (1.0 µs) | $15\text{ ksps}$ (65 µs) |

## Common mistakes

- **Reconfiguring PA13 / PA14 in software without delay:** Reassigning the SWD pins (`SWCLK`/`SWDIO`) as GPIOs immediately at startup will lock the debugger. Include a $2\text{ second}$ delay at the top of `main()` or connect the `NRST` line to enable "Connect Under Reset" in STM32CubeProgrammer.
- **Floating BOOT0 pin:** On STM32G0, `BOOT0` is multiplexed onto Pin 19 (`PA14`). In the internal Option Bytes, configure `nBOOT_SEL=1` to allow software control of boot source rather than requiring physical pin pulling.

## Notes

- **Software Toolchains:** Fully supported by STM32CubeIDE, STM32CubeMX, PlatformIO, and the official `STM32duino` Arduino framework.
