## Overview

The **STM32F401CCU6** is a high-performance 32-bit ARM Cortex-M4 microcontroller IC manufactured by STMicroelectronics. Operating at clock speeds up to **$84\text{ MHz}$** with a hardware Floating Point Unit (FPU), it is the brain behind the widely popular **"Black Pill"** (WeAct Studio) development board.

Equipped with **$256\text{ KB}$ of Flash memory**, **$64\text{ KB}$ of SRAM**, a native **USB 2.0 OTG Full-Speed controller**, a 12-bit ADC ($2.4\text{ MSPS}$), and advanced communication interfaces (I2C, SPI/I2S, USART), it offers significant performance gains over older Cortex-M3 boards (like the STM32F103 "Blue Pill").

## Quick reference

| | |
|---|---|
| **CPU Core** | ARM 32-bit Cortex-M4 with FPU & DSP instructions |
| **Max Clock Frequency** | $84\text{ MHz}$ (105 DMIPS) |
| **Flash Memory** | $256\text{ KB}$ |
| **SRAM** | $64\text{ KB}$ |
| **Operating Voltage (`VDD`)** | 1.7 V to 3.6 V DC (3.3 V nominal) |
| **Package** | 48-pin UFQFPN ($7 \times 7\text{ mm}$) / "Black Pill" PCB |
| **ADC Peripheral** | 1x 12-bit ADC (16 channels, $2.4\text{ MSPS}$) |
| **Communication Buses** | 1x USB 2.0 OTG FS, 3x USART, 4x SPI/I2S, 3x $I^2C$ |
| **Debug Interface** | SWD (Serial Wire Debug) & JTAG |

## Pinout (Black Pill V3.0 Development Board Header)

```
                       ┌─────────────┐
                 [GND] │             │ [GND]
                [3.3V] │   STM32F4   │ [3.3V]
               [RESET] │ Black Pill  │ [VBAT]
       (PA0)   [ PA0 ] │  F401CCU6   │ [ PC13 ] (Onboard LED)
       (PA1)   [ PA1 ] │             │ [ PC14 ] (32.768kHz Crystal)
       (PA2)   [ PA2 ] │             │ [ PC15 ] (32.768kHz Crystal)
       (PA3)   [ PA3 ] │             │ [ PA8  ]
       (PA4)   [ PA4 ] │             │ [ PA9  ] (USART1 TX)
       (PA5)   [ PA5 ] │             │ [ PA10 ] (USART1 RX)
       (PA6)   [ PA6 ] │             │ [ PA11 ] (USB D-)
       (PA7)   [ PA7 ] │             │ [ PA12 ] (USB D+)
       (PB0)   [ PB0 ] │             │ [ PA15 ]
       (PB1)   [ PB1 ] │             │ [ PB3  ] (SWO)
       (PB2)   [ PB2 ] │             │ [ PB4  ]
       (PB10)  [ PB10] │             │ [ PB5  ]
       (PB12)  [ PB12] │             │ [ PB6  ] (I2C1 SCL)
       (PB13)  [ PB13] │             │ [ PB7  ] (I2C1 SDA)
       (PB14)  [ PB14] │             │ [ PB8  ]
       (PB15)  [ PB15] │             │ [ PB9  ]
                       └─────────────┘
```

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Operating Supply Voltage| $V_{DD}$ | 1.7 | 3.3 | 3.6 | V | DC supply |
| Run Mode Current | $I_{DD}$ | — | 20 | 35 | mA | Run mode at 84 MHz |
| Stop Mode Current | $I_{stop}$| — | 15 | 45 | µA | Low power stop mode |
| Standby Mode Current | $I_{stby}$| — | 2.4 | 5.0 | µA | Backup domain powered |
| GPIO Output Current | $I_{IO}$ | -25 | — | +25 | mA | Single GPIO pin |
| ADC Conversion Speed | $f_{ADC}$| — | 2.4 | — | MSPS | 12-bit resolution |

## Wiring (ST-Link V2 SWD Programming Connection)

```
  ST-Link V2 Programmer            STM32F401 (Black Pill Header)
  ┌──────────────────┐            ┌─────────────────────────────┐
  │      3.3V        ├───────────►│ 3.3V                        │
  │      GND         ├───────────►│ GND                         │
  │      SWDIO       ├───────────►│ PA13 (SWDIO)                │
  │      SWCLK       ├───────────►│ PA14 (SWCLK)                │
  └──────────────────┘            └─────────────────────────────┘
```

## Example (Arduino Core for STM32 - Blinking PC13 LED)

```cpp
// Onboard LED on Black Pill is connected to PC13 (Active LOW)
const int ledPin = PC13;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
  Serial.println("STM32F401CCU6 Cortex-M4 Active!");
}

void loop() {
  digitalWrite(ledPin, LOW);  // Turn LED ON (Active Low)
  delay(250);
  digitalWrite(ledPin, HIGH); // Turn LED OFF
  delay(250);
}
```

## Common mistakes

- **Confusing STM32F401CCU6 with STM32F411CEU6:** The Black Pill board is sold in both STM32F401 ($84\text{ MHz}$, $256\text{ KB}$ Flash) and STM32F411 ($100\text{ MHz}$, $512\text{ KB}$ Flash) variants. Select the correct board definition in STM32CubeIDE or Arduino IDE.
- **Supplying > 3.6V to $V_{DD}$:** While many I/O pins are 5V tolerant, the power supply input ($V_{DD}$) must be **3.3V DC**. Exceeding 3.6V on $V_{DD}$ destroys the silicon.

## Notes

- **STM32F401 vs STM32F103:** STM32F401 features an ARM Cortex-M4 with hardware FPU at 84MHz, USB OTG, and 256KB Flash; STM32F103 is Cortex-M3 at 72MHz without FPU and with 64KB Flash.
