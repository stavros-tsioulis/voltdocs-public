## Overview

The **nRF52832** is an ultra-low power multiprotocol System-on-Chip (SoC) manufactured by Nordic Semiconductor. Powered by a 32-bit **ARM Cortex-M4 processor with floating point unit (FPU)** running at **$64\text{ MHz}$**, it integrates a full **Bluetooth 5** qualified 2.4 GHz radio transceiver, **$512\text{ KB}$ of Flash**, **$64\text{ KB}$ of RAM**, and an **NFC-A tag** module.

Designed specifically for battery-powered wearable devices, wireless sensors, smart home products, and medical telemetry, the nRF52832 delivers high processing efficiency alongside ultra-low radio current consumption ($5.3\text{ mA}$ peak TX current).

## Quick reference

| | |
|---|---|
| **CPU Core** | ARM 32-bit Cortex-M4 with FPU |
| **Clock Speed** | $64\text{ MHz}$ |
| **Flash Memory** | $512\text{ KB}$ |
| **SRAM** | $64\text{ KB}$ |
| **Operating Voltage (`VDD`)** | 1.7 V to 3.6 V DC |
| **Wireless Support** | Bluetooth 5.0, Bluetooth Low Energy, ANT, 2.4 GHz Proprietary |
| **Max Output Power** | $+4\text{ dBm}$ (configurable down to $-20\text{ dBm}$) |
| **RX Sensitivity** | $-96\text{ dBm}$ at 1 Mbps BLE |
| **TX Current (0 dBm)** | $5.3\text{ mA}$ |
| **Sleep Current (System OFF)** | $0.3\ \mu\text{A}$ |
| **Package** | QFN48 ($6 \times 6\text{ mm}$) / WLCSP50 |

## Pinout (QFN-48 Package)

```
                    ┌───┴───┐
          DEC1  1│ 1   48│ DEC4 (1V3)
           P0.00 2│       │47 XC2
(NFC1)     P0.01 3│       │46 XC1
(NFC2)     P0.02 4│nRF52832│45 DEC3
           P0.03 5│ QFN48 │44 DEC2
           P0.04 6│       │43 VDD
           P0.05 7│       │42 ANT
           P0.06 8│       │41 VSS_PA
           P0.07 9│       │40 DEC5
          P0.08 10│       │39 P0.31
   (NRESET) P0.21 21│     │25 P0.17
                    └───────┘
```

| Pin | Name | Description |
|---|---|---|
| 2 | `P0.00` / `XL1` | General Purpose I/O / 32.768 kHz Crystal Input |
| 3 | `P0.01` / `XL2` | General Purpose I/O / 32.768 kHz Crystal Output |
| 4 | `P0.02` / `NFC1` | General Purpose I/O / NFC Antenna Pin 1 |
| 5 | `P0.03` / `NFC2` | General Purpose I/O / NFC Antenna Pin 2 |
| 21 | `P0.21` / `nRESET` | General Purpose I/O / Hardware Reset Input |
| 25 | `P0.17` | General Purpose I/O |
| 42 | `ANT` | 2.4 GHz Antenna RF Output |
| 43 | `VDD` | Power supply input (1.7 V to 3.6 V) |
| 46 | `XC1` | 64 MHz Crystal Input |
| 47 | `XC2` | 64 MHz Crystal Output |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 1.7 | 3.0 | 3.6 | V | DC |
| TX Peak Current | $I_{TX}$ | — | 5.3 | 7.5 | mA | $+0\text{ dBm}$ output power, DC-DC |
| RX Peak Current | $I_{RX}$ | — | 5.4 | 6.5 | mA | 1 Mbps BLE, DC-DC mode |
| System ON Idle Current | $I_{ON}$ | — | 1.9 | — | µA | RTC active, 64KB RAM retained |
| System OFF Current | $I_{OFF}$ | — | 0.3 | 1.5 | µA | No RAM retention |
| ADC Resolution | $N_{ADC}$ | — | 12 | — | Bit | 200 ksps conversion rate |

## Programming & Debugging Interface

Programming the nRF52832 requires a **J-Link** or **CMSIS-DAP** SWD programmer:

| Programmer | → | nRF52832 Pin |
|---|---|---|
| `VDD` | | `VDD` (Pin 43) |
| `GND` | | `VSS` (Ground) |
| `SWDIO` | | `SWDIO` |
| `SWDCLK` | | `SWDCLK` |

## Common mistakes

- **Omitting external decoupling capacitors on `DEC` pins:** The nRF52832 relies on internal switching regulators (DC-DC / LDO) requiring external ceramic capacitors connected to `DEC1`, `DEC2`, `DEC3`, `DEC4`, and `DEC5`. Omitting them prevents the core from booting.
- **Using `P0.09` / `P0.10` as GPIO without disabling NFC:** Pins `P0.09` and `P0.10` default to NFC antenna pins in software. To use them as standard GPIOs, `CONFIG_NFCT_PINS_AS_GPIOS` must be set in the build system.

## Notes

- **nRF52832 vs ESP32:** nRF52832 consumes significantly lower power ($5.3\text{ mA}$ TX vs $240\text{ mA}$ on ESP32), making it ideal for coin-cell battery devices; ESP32 includes Wi-Fi and higher CPU clock speeds ($240\text{ MHz}$).
