## Overview

The **STM32F103C8T6** is a 32-bit ARM Cortex-M3 microcontroller IC manufactured by STMicroelectronics. Operating at clock speeds up to **$72\text{ MHz}$**, it is the brain behind the widely popular, low-cost **"Blue Pill"** development board used across robotics, 3D printer controller boards (Klipper/Marlin), motor drivers, and industrial automation devices.

Equipped with **$64\text{ KB}$ of Flash memory** (frequently $128\text{ KB}$ in practice), **$20\text{ KB}$ of SRAM**, a native **USB 2.0 Full-Speed device controller**, two 12-bit ADCs, CAN 2.0B interface, and multiple USART, SPI, and $I^2C$ peripherals, it delivers 32-bit ARM performance at an 8-bit price point.

## Quick reference

| | |
|---|---|
| **CPU Core** | ARM 32-bit Cortex-M3 RISC processor |
| **Max Clock Frequency** | $72\text{ MHz}$ (1.25 DMIPS/MHz) |
| **Flash Memory** | $64\text{ KB}$ (or $128\text{ KB}$ on Medium-Density devices) |
| **SRAM** | $20\text{ KB}$ |
| **Operating Voltage (`VDD`)** | 2.0 V to 3.6 V DC (3.3 V nominal) |
| **Package** | 48-pin LQFP ($7 \times 7\text{ mm}$) / "Blue Pill" PCB |
| **ADC Peripherals** | 2x 12-bit ADCs (10 multiplexed channels, $1\ \mu\text{s}$ conversion) |
| **Communication Buses** | 1x USB 2.0 FS, 1x CAN 2.0B, 3x USART, 2x SPI, 2x $I^2C$ |
| **Debug Interface** | SWD (Serial Wire Debug via ST-Link V2) & JTAG |

## Pinout (Blue Pill Development Board Header)

```
                       ┌─────────────┐
                 [GND] │             │ [GND]
                [3.3V] │   STM32F1   │ [3.3V]
               [RESET] │ Blue Pill   │ [VBAT]
       (PA0)   [ PA0 ] │             │ [ PC13 ] (Onboard LED)
       (PA1)   [ PA1 ] │             │ [ PC14 ] (32.768kHz Crystal)
       (PA2)   [ PA2 ] │             │ [ PC15 ] (32.768kHz Crystal)
       (PA3)   [ PA3 ] │             │ [ PA8  ]
       (PA4)   [ PA4 ] │             │ [ PA9  ] (USART1 TX)
       (PA5)   [ PA5 ] │             │ [ PA10 ] (USART1 RX)
       (PA6)   [ PA6 ] │             │ [ PA11 ] (USB D-)
       (PA7)   [ PA7 ] │             │ [ PA12 ] (USB D+)
       (PB0)   [ PB0 ] │             │ [ PA15 ]
       (PB1)   [ PB1 ] │             │ [ PB3  ] (SWO)
       (PB10)  [ PB10] │             │ [ PB4  ]
       (PB11)  [ PB11] │             │ [ PB5  ]
       (PB12)  [ PB12] │             │ [ PB6  ] (I2C1 SCL)
       (PB13)  [ PB13] │             │ [ PB7  ] (I2C1 SDA)
       (PB14)  [ PB14] │             │ [ PB8  ]
       (PB15)  [ PB15] │             │ [ PB9  ]
                       └─────────────┘
```

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Operating Supply Voltage| $V_{DD}$ | 2.0 | 3.3 | 3.6 | V | DC supply |
| Operating Current | $I_{DD}$ | — | 36 | 50 | mA | Run mode at 72 MHz |
| Stop Mode Current | $I_{stop}$| — | 15 | 24 | µA | Low power stop mode |
| Standby Mode Current | $I_{stby}$| — | 2 | 3.4 | µA | Backup domain powered |
| GPIO Sink/Source Current| $I_{IO}$ | -25 | — | +25 | mA | Single GPIO pin |
| ADC Conversion Time | $t_S$ | 1.0 | — | 17.1 | µs | 12-bit resolution |

## Wiring (ST-Link V2 SWD Programming Connection)

Programming the STM32F103C8T6 requires an **ST-Link V2** USB dongle:

| ST-Link V2 Dongle | → | STM32F103C8T6 (Blue Pill Header) | Notes |
|---|---|---|---|
| `3.3V` | | `3.3V` | Target power input |
| `GND` | | `GND` | Common ground |
| `SWDIO` | | `PA13` (`SWDIO`) | Serial Wire Data IO |
| `SWCLK` | | `PA14` (`SWCLK`) | Serial Wire Clock |

## Example (Arduino Core for STM32 - Blinking PC13 LED)

```cpp
// Onboard green LED on Blue Pill is connected to PC13 (Active LOW)
const int ledPin = PC13;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
  Serial.println("STM32F103C8T6 ARM Cortex-M3 Active!");
}

void loop() {
  digitalWrite(ledPin, LOW);  // Turn LED ON (Active Low)
  delay(500);
  digitalWrite(ledPin, HIGH); // Turn LED OFF
  delay(500);
}
```

## Common mistakes

- **Incorrect `BOOT0` jumper position when flashing via USB:** Flashing code via USB Bootloader requires `BOOT0` jumper set to `1` (High). Flashing via ST-Link V2 SWD requires `BOOT0` set to `0` (Low).
- **Applying 5.0V power to 3.3V `VDD` pins:** While many GPIO pins on the STM32F103 are 5V tolerant, the main power supply pins (`VDD`) MUST be powered by **3.3V DC**. Supplying 5V directly to `VDD` destroys the MCU.

## Notes

- **STM32F103C8T6 vs ATmega328P vs ESP32:** STM32F103 offers 72MHz 32-bit ARM processing with USB; ATmega328P is 16MHz 8-bit AVR; ESP32 is 240MHz dual-core with Wi-Fi/Bluetooth.
