## Overview

The **ESP-12E** (and its refined successor the **ESP-12F**) is a surface-mount $2.4\text{ GHz}$ $802.11\text{ b/g/n}$ Wi-Fi microcontroller module manufactured by AI-Thinker based on the Espressif Systems **ESP8266EX** SoC. Featuring a castellated 22-pad SMD package ($24.0 \times 16.0\text{ mm}$) with an integrated meandered PCB trace antenna, it is the module at the heart of the **NodeMCU v2/v3**, **Wemos D1 Mini**, and **Sonoff smart home devices**.

Powered by a 32-bit Tensilica Xtensa L106 Diamond core operating at **$80\text{ MHz} \dots 160\text{ MHz}$**, the ESP-12E integrates **$4\text{ MB}$ ($32\text{ Mbit}$) SPI Flash**, a full TCP/IP networking stack, 11 accessible GPIO lines, hardware UART, SPI, I2C, and a 10-bit ADC channel. Operating from **$3.0\text{V}$ to $3.6\text{V}$ DC**, it supports deep-sleep power consumption down to **$20\ \mu\text{A}$**, making it the premier bare module for custom IoT sensor nodes and Wi-Fi actuators.

## Quick reference

| | |
|---|---|
| **SoC / Processor** | Espressif ESP8266EX (32-bit Tensilica L106 RISC) |
| **Package** | 22-pin Castellated SMD Module ($24.0 \times 16.0 \times 3.0\text{ mm}$) |
| **Clock Frequency** | $80\text{ MHz}$ default (Configurable to $160\text{ MHz}$) |
| **Flash Memory** | $4\text{ MB}$ ($32\text{ Mbit}$) SPI Flash |
| **RAM** | $80\text{ KB}$ User Data RAM + $32\text{ KB}$ Instruction RAM |
| **Operating Voltage Range** | $3.0\text{ V}$ to $3.6\text{ V}$ DC ($3.3\text{ V}$ nominal) |
| **Peak Current Consumption** | $170\text{ mA} \dots 300\text{ mA}$ during Wi-Fi transmission bursts |
| **Deep Sleep Current** | $\sim 20\ \mu\text{A}$ (Requires `GPIO16` tied to `RST`) |
| **Wi-Fi Protocols** | $802.11\text{ b/g/n}$ ($2.4\text{ GHz} \dots 2.5\text{ GHz}$, up to $+19.5\text{ dBm}$ output) |
| **ADC Channel** | 10-bit SAR ADC ($0.0\text{ V}$ to $1.0\text{ V}$ maximum input range) |

## Module Pinout (22-Pin SMD Package)

```
                       ┌───────[ Antenna ]───────┐
                       │   ESP-12E / ESP-12F     │
       (Active-Low) RST│ 1                     22│ TXD0 (UART0 TX / GPIO1)
     (0-1V Input)  ADC0│ 2                     21│ RXD0 (UART0 RX / GPIO3)
          (Pull-Up)  EN│ 3                     20│ GPIO5
                 GPIO16│ 4                     19│ GPIO4
                 GPIO14│ 5                     18│ GPIO0 (Boot Mode Select)
                 GPIO12│ 6                     17│ GPIO2 (Pull-Up)
          (+3.3V)   VCC│ 7                     16│ GPIO15 (Pull-Down)
          (Ground)  GND│ 8                     15│ GND
                       └──┬──┬──┬──┬──┬──┬───────┘
                          9 10 11 12 13 14
                          (Internal SPI Flash Pads)
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `RST` | Reset | Active-LOW Reset input (Pull up to $3.3\text{V}$ via $10\text{ k}\Omega$) |
| 2 | `ADC` | Analog In | 10-bit ADC Input ($0.0\text{V} \dots 1.0\text{V}$ max; use divider for 3.3V) |
| 3 | `EN / CH_PD` | Enable | Chip Enable (Must be pulled HIGH to $3.3\text{V}$ via $10\text{ k}\Omega$ to run) |
| 4 | `GPIO16` | GPIO | Deep sleep wakeup pin (Connect to `RST` to enable auto-wake) |
| 5 | `GPIO14` | GPIO / SPI | `HSPI_CLK` / GPIO14 |
| 6 | `GPIO12` | GPIO / SPI | `HSPI_MISO` / GPIO12 |
| 7 | `VCC` | Power | Supply Voltage ($+3.0\text{ V}$ to $+3.6\text{ V}$ DC) |
| 8, 15 | `GND` | Power | Common Ground reference ($0\text{ V}$) |
| 9–14 | `CS0, MISO, ...`| SPI Flash | Internal SPI Flash connection pads (**Do NOT connect on PCB**) |
| 16 | `GPIO15` | GPIO / Boot | Strapping pin: **Must be pulled LOW to GND via $10\text{ k}\Omega$** |
| 17 | `GPIO2` | GPIO / Boot | Strapping pin: **Must be pulled HIGH to $3.3\text{V}$ via $10\text{ k}\Omega$** / Onboard Blue LED |
| 18 | `GPIO0` | GPIO / Boot | Boot Select: **HIGH for normal boot, LOW for UART Flash mode** |
| 19, 20 | `GPIO4`, `GPIO5`| GPIO / I2C | General purpose I/O (Standard for `SDA` and `SCL`) |
| 21 | `RXD0` | GPIO / UART | UART0 Receive (`RXD0` / `GPIO3`) |
| 22 | `TXD0` | GPIO / UART | UART0 Transmit (`TXD0` / `GPIO1`) |

## Boot Strapping Configurations

| Boot Mode | `CH_PD (EN)` | `RST` | `GPIO15` | `GPIO0` | `GPIO2` |
|---|---|---|---|---|---|
| **Normal Flash Boot (Run)** | HIGH ($3.3\text{V}$) | HIGH | **LOW (GND)** | **HIGH ($3.3\text{V}$)** | **HIGH ($3.3\text{V}$)** |
| **UART Flashing (Download)** | HIGH ($3.3\text{V}$) | HIGH | **LOW (GND)** | **LOW (GND)** | **HIGH ($3.3\text{V}$)** |

## Minimal Schematic Hookup for Custom PCBs

```
                           +3.3V DC (Minimum 500mA LDO like AP2112 / AMS1117)
                                 │
             ┌───────────────────┼───────────────────┬───────────────────┐
             │                   │                   │                   │
       [ 10kΩ Pull-Up ]    [ 10kΩ Pull-Up ]    [ 10kΩ Pull-Up ]    [ 10kΩ Pull-Up ]
             │                   │                   │                   │
             ├─────────────► [Pin 1: RST]            │                   │
             │                   │                   │                   │
             ├─────────────► [Pin 3: EN]             │                   │
             │                                       │                   │
             ├───────────────────────────────────────┼─────────────► [Pin 17: GPIO2]
             │                                       │
             │                                 [ Flash Switch ] ──► [Pin 18: GPIO0]
             │                                       │
             │                                      GND
             │
       [Pin 7: VCC] ──┬──[ 10µF Tantalum / Ceramic ]──┐
                      └──[ 100nF Ceramic MLCC ]───────┤
                                                      │
       [Pin 16: GPIO15] ──[ 10kΩ Pull-Down ]──────────┼──► [Pin 8, 15: GND] ── Common GND
```

## Common mistakes

- **Inadequate power supply regulation:** During Wi-Fi calibration and RF transmissions, the ESP8266 draws sharp current pulses up to $300\text{ mA}$. Powering directly from a weak 3.3V FTDI adapter or high-impedance regulator will cause brownout resets (`rst cause:2, boot mode:(3,6)`). Always place at least a **$10\ \mu\text{F}$ low-ESR capacitor** directly across `VCC` and `GND`.
- **Applying 5V logic signals directly:** The ESP8266 is strictly a **$3.3\text{V}$ device**. Use bidirectional level shifters or resistor voltage dividers on `RXD0` when interfacing with 5V microcontrollers.
- **Overdriving the ADC pin:** The onboard ADC pin accepts a maximum input of **$1.0\text{V}$**. Connecting $3.3\text{V}$ directly to Pin 2 will saturate or damage the ADC. Use a resistor divider ($220\text{ k}\Omega / 100\text{ k}\Omega$).
- **Routing copper traces under the PCB antenna:** For proper Wi-Fi range, the antenna section must overhang the edge of your carrier board with zero copper traces or ground planes directly underneath.

## Notes

- **ESP-12E vs ESP-12F:** ESP-12F features an improved 4-layer PCB layout and optimized antenna impedance matching for $30\%$ greater RF range.
