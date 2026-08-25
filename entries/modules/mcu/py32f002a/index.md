## Overview

The **PY32F002A** is an ultra-low-cost 32-bit ARM Cortex-M0+ microcontroller manufactured by Puya Semiconductor (Shanghai). Available in **TSSOP-20, SOP-16, and ultra-compact SOP-8** packages, it made headlines globally for offering a 32-bit ARM processor and modern peripherals at a unit price below **$\$0.10** in modest volumes.

Unlike traditional STM32 microcontrollers that are restricted to $2.0\text{V} \dots 3.6\text{V}$, the PY32F002A supports an ultra-wide supply voltage operating range from **$1.7\text{V}$ all the way to $5.5\text{V}$ DC**, allowing direct drop-in integration into both 3.3V battery systems and 5V legacy/automotive circuits without level shifters. Packing **$20\text{ KB}$ Flash**, **$3\text{ KB}$ SRAM**, a **12-bit $1.0\text{ Msps}$ ADC**, a 16-bit advanced motor-control timer, and standard serial buses (USART, SPI, I2C), it is supported by open-source toolchains (GCC, PyOCD, and the `Puya-Arduino` core) as a modern replacement for 8-bit ATtiny and 8051 chips.

## Quick reference

| | |
|---|---|
| **CPU Core** | ARM 32-bit Cortex-M0+ RISC |
| **Package Options** | TSSOP-20 (PY32F002AL15S) / SOP-8 / SOP-16 / QFN-20 |
| **Max Clock Frequency** | $24\text{ MHz}$ (Internal factory RC, overclockable to $48\text{ MHz}$) |
| **Flash Memory** | $20\text{ KB}$ (32KB physically on die in many batches) |
| **SRAM** | $3\text{ KB}$ high-speed SRAM |
| **Supply Voltage Range** | **$1.7\text{ V}$ to $5.5\text{ V}$ DC** (Direct 5V and 3.3V compatible) |
| **Analog Peripherals** | 12-bit 1 Msps SAR ADC (up to 9 channels) + 2x Analog Comparators |
| **Advanced Timer** | 1x 16-bit Motor Control Timer (TIM1) with 4 complementary PWM outputs |
| **Digital Interfaces** | 1x USART, 1x SPI, 1x I2C, 1x Low-Power Timer (LPTIM) |
| **Programming / Debug** | Standard Serial Wire Debug (SWD: `SWCLK` / `SWDIO` via J-Link / DAPLink / ST-Link) |

## Pinout (TSSOP-20 Package)

```
                       ┌───┴───┐
      (BOOT0) PB7 / BOOT0 1│ 1   20│ PA14 (SWCLK / USART1_TX)
 (OSC_IN) PF0 / PA0       2│       │19 PA13 (SWDIO / IR_OUT)
(OSC_OUT) PF1 / PA1       3│       │18 PA10 (USART1_RX / TIM1_CH3)
        (Active-Low) NRST 4│ PY32F │17 PA9  (USART1_TX / TIM1_CH2 / I2C_SCL)
                     VDD  5│ 002A  │16 PB6  (TIM1_CH3N / I2C_SCL)
     (ADC_IN0) PA0        6│ TSSOP │15 VSS  (Ground 0V)
     (ADC_IN1) PA1        7│  -20  │14 PB3  (TIM1_CH1N / SPI1_SCK)
     (ADC_IN2) PA2        8│       │13 PA7  (ADC_IN7 / TIM1_CH1N / SPI1_MOSI)
     (ADC_IN3) PA3        9│       │12 PA6  (ADC_IN6 / TIM3_CH1 / SPI1_MISO)
     (ADC_IN4) PA4       10│       │11 PA5  (ADC_IN5 / TIM1_CH1 / SPI1_SCK)
                       └───────┘
```

## Minimal Circuit & Flashing Connections

```
                    +1.7V to +5.5V DC (e.g. 3.3V or 5.0V Rail)
                              │
               ┌──────────────┴───────────────┐
               │                              │
         [Pin 5: VDD]                         │
               │                        [ 10kΩ Pull-Down ]
        [ 100nF Cap ]                         │
               │                       [Pin 1: PB7 / BOOT0]
         [Pin 15: VSS] ───────────────────────┼─── Common System GND
                              │               │
  DAPLink / J-Link / ST-Link  │               │
  ┌─────────────────────────┐ │               │
  │ SWCLK ──────────────────┼─┼───────────────► [Pin 20: PA14 / SWCLK]
  │ SWDIO ──────────────────┼─┼───────────────► [Pin 19: PA13 / SWDIO]
  │ NRST (Optional) ────────┼─┼───────────────► [Pin 4: NRST] ──[ 100nF Cap ]── GND
  │ GND ────────────────────┼─┴───────────────► Common Ground
  └─────────────────────────┘
```

## Comparison: PY32F002A vs STM32F030 vs ATtiny85

| Feature | Puya PY32F002A | ST STM32F030F4 | Microchip ATtiny85 |
|---|---|---|---|
| **Core Architecture** | 32-bit Cortex-M0+ | 32-bit Cortex-M0 | 8-bit AVR RISC |
| **Max Clock Speed** | $24\text{ MHz} \dots 48\text{ MHz}$ | $48\text{ MHz}$ | $20\text{ MHz}$ |
| **Flash / RAM** | $20\text{ KB} / 3\text{ KB}$ | $16\text{ KB} / 4\text{ KB}$ | $8\text{ KB} / 512\text{ B}$ |
| **Operating Voltage** | **$1.7\text{V} \dots 5.5\text{V}$** | $2.4\text{V} \dots 3.6\text{V}$ | $2.7\text{V} \dots 5.5\text{V}$ |
| **ADC Resolution** | 12-bit ($1.0\text{ Msps}$) | 12-bit ($1.0\ \mu\text{s}$) | 10-bit ($15\text{ ksps}$) |
| **Typical Cost** | **$\approx \$0.10$** | $\approx \$0.45$ | $\approx \$1.10$ |

## Common mistakes

- **Assuming 3.3V-only limits like STM32:** Developers accustomed to ST chips often add unnecessary 3.3V regulators. The PY32F002A runs natively at full 5.0V logic.
- **Using outdated OpenOCD forks:** Official OpenOCD releases may not recognize Puya's custom CoreSight device IDs out-of-the-box. Use PyOCD with the `py32f0` CMSIS pack or standard DAPLink / J-Link with the `py32f0-template` configuration.

## Notes

- **Arduino Core:** Supported via the community **Arduino-Puya** core in the Arduino IDE and PlatformIO.
