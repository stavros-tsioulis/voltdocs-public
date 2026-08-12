## Overview

The **ATmega32U4** is a low-power 8-bit AVR RISC microcontroller IC manufactured by Microchip Technology (formerly Atmel). Featuring **$32\text{ KB}$ of Flash memory**, **$2.5\text{ KB}$ of SRAM**, **$1\text{ KB}$ of EEPROM**, and a built-in hardware **USB 2.0 Full-Speed device controller**, it eliminates the need for an external USB-to-Serial bridge chip (such as CH340 or FT232R).

Because of its native USB capabilities, the ATmega32U4 can emulate USB Human Interface Devices (HID)—such as USB keyboards, mice, gamepads, and MIDI devices. It is the core processor powering the **Arduino Leonardo**, **SparkFun Pro Micro**, and countless custom mechanical keyboards running **QMK** or **VIA** firmware.

## Quick reference

| | |
|---|---|
| **CPU Core** | 8-bit AVR RISC |
| **Max Clock Frequency** | $16\text{ MHz}$ (at $5\text{V}$) / $8\text{ MHz}$ (at $3.3\text{V}$) |
| **Flash Memory** | $32\text{ KB}$ ($4\text{ KB}$ reserved for bootloader) |
| **SRAM** | $2.5\text{ KB}$ |
| **EEPROM** | $1\text{ KB}$ |
| **Operating Voltage (`VCC`)** | 2.7 V to 5.5 V DC |
| **USB Support** | Integrated USB 2.0 Full-Speed (12 Mbps) Device Controller |
| **GPIO Count** | 26 I/O pins |
| **ADC Channels** | 12 channels (10-bit resolution) |
| **Package** | 44-pin TQFP / 44-pin QFN / Pro Micro Board |

## Pinout (Pro Micro Board Header Layout)

```
                       ┌─────────────┐
                 [TX0] │ 1   (D2) 12 │ [RAW] (Power Input 5-12V)
                 [RX1] │ 2   (D3) 11 │ [GND]
                 [GND] │ 3        10 │ [RESET]
                 [GND] │ 4   (D4)  9 │ [VCC] (5V / 3.3V Output)
           (SDA)  [D2] │ 5   (D5)  8 │ [A3]  (ADC3)
           (SCL)  [D3] │ 6   (D6)  7 │ [A2]  (ADC2)
                  [D4] │ 7   (D7)  6 │ [A1]  (ADC1)
           (PWM)  [D5] │ 8   (D8)  5 │ [A0]  (ADC0)
           (PWM)  [D6] │ 9   (D9)  4 │ [D15] (SCK)
                  [D7] │ 10 (D10)  3 │ [D14] (MISO)
           (PWM)  [D8] │ 11 (D16)  2 │ [D16] (MOSI)
           (PWM)  [D9] │ 12 (D14)  1 │ [D10] (PWM)
                       └─────────────┘
```

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Operating Voltage (16 MHz) | $V_{CC}$ | 4.5 | 5.0 | 5.5 | V | 16 MHz crystal |
| Operating Voltage (8 MHz) | $V_{CC}$ | 2.7 | 3.3 | 5.5 | V | 8 MHz crystal |
| Active Supply Current | $I_{CC}$ | — | 15 | 25 | mA | 16 MHz at 5V, USB active |
| Power-Down Current | $I_{PD}$ | — | 0.2 | 2.0 | µA | WDT disabled |
| USB Operating Voltage | $V_{USB}$ | 4.4 | 5.0 | 5.25 | V | Bus-powered USB |
| Max Current per GPIO Pin | $I_{DC}$ | -40 | — | +40 | mA | Absolute maximum rating |

## Example (Arduino Keyboard Emulation)

```cpp
#include <Keyboard.h>

const int buttonPin = 2;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  // Initialize USB Keyboard emulation
  Keyboard.begin();
}

void loop() {
  if (digitalRead(buttonPin) == LOW) {
    // Send a keystroke over USB HID
    Keyboard.print("Hello from ATmega32U4!");
    Keyboard.write(KEY_RETURN);
    delay(500); // Debounce
  }
}
```

## Common mistakes

- **Selecting 5V 16MHz bootloader for a 3.3V 8MHz Pro Micro:** Pro Micro boards exist in both 5V/16MHz and 3.3V/8MHz versions. Flashing a 5V/16MHz bootloader onto a 3.3V board causes the board to brick or fail USB enumeration.
- **Overloading total VCC current limits:** While single GPIO pins can handle up to $40\text{ mA}$, the total combined current across all GPIOs must not exceed **$200\text{ mA}$**.

## Notes

- **ATmega32U4 vs ATmega328P:** ATmega32U4 features hardware USB 2.0 (enabling USB HID mouse/keyboard emulation) and 2.5KB SRAM; ATmega328P requires an external USB-to-UART bridge IC and has 2KB SRAM.
