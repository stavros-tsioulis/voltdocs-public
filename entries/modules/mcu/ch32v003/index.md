## Overview

The **CH32V003** (CH32V003F4P6) is an ultra-low-cost 32-bit RISC-V microcontroller manufactured by WCH (Nanjing Qinheng Microelectronics). Available in **TSSOP-20, QFN-20, SOP-16, and SOP-8** packages, it caused a sensation across the global maker community by providing a full 32-bit RISC-V core for less than **$\$0.15** in single-unit hobbyist quantities.

Built around WCH's custom **QingKe 32-bit RISC-V2A core (RV32EC)** running at up to **$48\text{ MHz}$**, the CH32V003 features **$16\text{ KB}$ Flash**, **$2\text{ KB}$ SRAM**, an **8-channel 10-bit $1.0\ \mu\text{s}$ ADC**, a 16-bit advanced motor-control timer with complementary PWM and dead-time, standard serial buses (USART, SPI, I2C), and a proprietary **Single-Wire Serial Debug Interface (1-Wire SDI / SWIO)**. Supported by the popular open-source bare-metal **`ch32v003fun`** framework and the official Arduino core, it has become the standard microcontroller for low-cost mass production and minimalist DIY builds.

## Quick reference

| | |
|---|---|
| **CPU Core** | QingKe 32-bit RISC-V2A (RV32EC Architecture) |
| **Package Options** | TSSOP-20 (CH32V003F4P6) / QFN-20 / SOP-16 / SOP-8 (CH32V003J4M6) |
| **Max Clock Frequency** | $48\text{ MHz}$ (Internal factory RC with on-chip PLL) |
| **Flash Memory** | $16\text{ KB}$ non-volatile program storage |
| **SRAM** | $2\text{ KB}$ high-speed SRAM |
| **Supply Voltage Range** | $2.7\text{ V}$ to $5.5\text{ V}$ DC (Direct 3.3V and 5.0V compatible) |
| **GPIO Count** | 18 GPIOs (TSSOP-20) / 6 GPIOs (SOP-8) |
| **Analog Peripherals** | 8-channel 10-bit ADC ($1.0\ \mu\text{s}$ conversion) + Analog Op-Amp/Comparator |
| **Advanced Timer** | 1x 16-bit Motor Control Timer (TIM1) with complementary PWM |
| **Serial Bus** | 1x USART, 1x SPI (18 Mbps), 1x I2C (400kHz Fast Mode) |
| **Programming / Debug** | 1-Wire Single-Wire Serial Debug Interface (SWIO on Pin `PD1`) via WCH-LinkE |

## Pinout (TSSOP-20 Package - CH32V003F4P6)

```
                       ┌───┴───┐
      (TIM1_CH1)  PD2 1│ 1   20│ PD1 (SWIO / Debug)
     (TIM1_CH2)  PD3 2│       │19 PD0 (TIM1_CH1N)
     (TIM1_CH4)  PD4 3│       │18 PC7 (USART1_TX)
         (OSC1)  PD5 4│CH32V003│17 PC6 (USART1_RX)
         (OSC2)  PD6 5│  F4P6  │16 PC5 (SPI1_SCK)
        (Active) NRST 6│ TSSOP │15 PC4 (I2C1_SDA)
           (0V)  VSS  7│  -20  │14 PC3 (I2C1_SCL)
        (+3.3V)  VDD  8│       │13 PC2 (ADC_IN2)
        (ADC0)   PA1  9│       │12 PC1 (ADC_IN1)
        (ADC1)   PA2 10│       │11 PC0 (ADC_IN0)
                       └───────┘
```

| Pin | Name | Type | Key Multiplexed Functions |
|---|---|---|---|
| 1, 2, 3 | `PD2`, `PD3`, `PD4`| GPIO / Digital | `TIM1_CH1`, `TIM1_CH2`, `TIM1_CH4` / `USART1_RX` |
| 4, 5 | `PD5`, `PD6` | GPIO / Clock | External Crystal Input/Output (`OSC1`, `OSC2`) |
| 6 | `NRST` | Reset / GPIO | Active-LOW Reset / GPIO `PD7` |
| 7 | `VSS` | Power | Common Ground reference ($0\text{ V}$) |
| 8 | `VDD` | Power | Supply Voltage ($+2.7\text{ V}$ to $+5.5\text{ V}$ DC) |
| 9, 10 | `PA1`, `PA2` | GPIO / Analog | `ADC_IN0`, `ADC_IN1` / `OSC32_IN`, `OSC32_OUT` |
| 11, 12, 13 | `PC0`, `PC1`, `PC2`| GPIO / Analog | `ADC_IN6`, `ADC_IN7`, `ADC_IN8` |
| 14, 15 | `PC3`, `PC4` | GPIO / Digital | `I2C1_SCL`, `I2C1_SDA` / `TIM1_CH3` |
| 16 | `PC5` | GPIO / Digital | `SPI1_SCK` / `TIM2_CH1` |
| 17, 18 | `PC6`, `PC7` | GPIO / Digital | `USART1_RX`, `USART1_TX` / `SPI1_MISO`, `SPI1_MOSI` |
| 19 | `PD0` | GPIO / Digital | `TIM1_CH1N` (Complementary PWM output) |
| 20 | `PD1 / SWIO` | GPIO / Debug | **Single-Wire Debug I/O (SWIO)** / Programming interface |

## Minimal Circuit & WCH-LinkE Flashing Hookup

```
                     +3.3V or +5.0V Regulated DC
                                 │
                          [Pin 8: VDD]
                                 │
                          [ 100nF Ceramic Bypass ]
                                 │
                          [Pin 7: VSS] ─── Common GND
                                 │
  WCH-LinkE Programmer           │
  ┌──────────────────┐           │
  │ 3.3V / 5V ───────┼───────────┘
  │ SWIO ────────────┼──────────────────────────► [Pin 20: PD1 / SWIO]
  │ GND ─────────────┼──────────────────────────► [Pin 7: VSS / GND]
  └──────────────────┘
```

## Common mistakes

- **Using standard ARM SWD programmers:** The CH32V003 uses WCH's proprietary **1-wire SDI protocol**, not ARM 2-wire SWD. An official **WCH-LinkE** programmer (or an ESP32/RP2040 running an open-source 1-wire programmer firmware like `minichlink`) is required to flash the chip.
- **Pulling PD1/SWIO to ground or high-capacitance loads:** Pin 20 is the sole debug interface pin. If connected to heavy capacitive loads or strong pull-downs, the programmer will fail to establish a link.

## Notes

- **Software Ecosystem:** Supported by the open-source **`ch32v003fun`** bare-metal development environment (extremely small binaries), MounRiver Studio, and the official Arduino core.
