## Overview

The **ATtiny85** is a famous low-power 8-bit AVR RISC microcontroller IC manufactured by Microchip Technology (Atmel). Housed in an ultra-compact **8-pin DIP package (DIP-8)**, it is the favored MCU for miniature DIY electronics projects, wearable devices, keychains, and Digispark USB development boards.

Despite its tiny footprint, the ATtiny85 features **$8\text{ KB}$ of Flash memory**, **$512\text{ Bytes}$ of SRAM**, **$512\text{ Bytes}$ of EEPROM**, a 4-channel 10-bit ADC, high-speed 64MHz PWM timer, and an internal $8\text{ MHz} \dots 16\text{ MHz}$ calibrated RC oscillator, allowing operation without any external crystal or supporting components.

## Quick reference

| | |
|---|---|
| **CPU Architecture** | 8-bit AVR RISC |
| **Package** | 8-pin DIP (ATtiny85-20PU) / 8-pin SOIC / Digispark Module |
| **Max Clock Frequency** | $20\text{ MHz}$ (Internal $8\text{ MHz}$ or $16\text{ MHz}$ PLL default) |
| **Memory Breakdown** | $8\text{ KB}$ Flash, $512\text{ B}$ SRAM, $512\text{ B}$ EEPROM |
| **Operating Voltage (`VCC`)**| 2.7 V to 5.5 V DC (1.8 V for ATtiny85V) |
| **GPIO Lines** | 6 Pins (`PB0` to `PB5`, including `PB5` Reset pin) |
| **PWM & Timers** | 2 Timers, 4 PWM channels (High-speed 64MHz PLL timer) |
| **Analog Input** | 4-channel 10-bit ADC (`ADC0` to `ADC3`) |
| **Serial Hardware Interface** | USI (Universal Serial Interface for $I^2C$ & SPI) |

## Pinout (DIP-8 Package)

```
                       ┌───┴───┐
     (PCINT5/RESET) PB5 ─┤ 1   8 ├─ VCC (+2.7V to +5.5V)
    (PCINT3/ADC3)   PB3 ─┤ 2   7 ├─ PB2 (SCK/SCL/ADC1)
    (PCINT4/ADC2)   PB4 ─┤ 3   6 ├─ PB1 (MISO/DO/PWM1)
                    GND ─┤ 4   5 ├─ PB0 (MOSI/SDA/PWM0)
                       └───────┘
```

| Pin | Name | Primary Functions | Arduino Pin Mapping |
|---|---|---|---|
| 1 | `PB5` | `/RESET`, ADC3, PCINT5 | Reset Pin (Pin 5) |
| 2 | `PB3` | ADC3, PCINT3, XTAL1 | Physical Pin 2 (Analog A3) |
| 3 | `PB4` | ADC2, PCINT4, XTAL2, PWM | Physical Pin 3 (Analog A2, PWM) |
| 4 | `GND` | Ground Reference (0V) | Ground |
| 5 | `PB0` | MOSI, SDA, AREF, PWM0 | Digital Pin 0 (PWM / $I^2C$ SDA) |
| 6 | `PB1` | MISO, DO, PWM1 | Digital Pin 1 (PWM / SPI MISO) |
| 7 | `PB2` | SCK, SCL, ADC1 | Digital Pin 2 (Analog A1 / $I^2C$ SCL) |
| 8 | `VCC` | Positive Supply Input (+2.7V to +5.5V DC) | Power Rail |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.7 | 5.0 | 5.5 | V | Standard ATtiny85-20PU |
| Active Supply Current | $I_{CC}$ | — | 300 | 800 | µA | $V_{CC} = 3.0\text{V}, f_{CLK} = 1\text{MHz}$ |
| Power-down Current | $I_{pd}$ | — | 0.1 | 1.0 | µA | $V_{CC} = 3.0\text{V}, T_A = 25^\circ\text{C}$ |
| Internal Calibrated Clock| $f_{RC}$ | 7.3 | 8.0 | 8.7 | MHz | Internal RC oscillator |
| GPIO Output Sink/Source | $I_{IO}$ | -40 | — | +40 | mA | Absolute max per pin |

## Minimal Circuit (Internal 8MHz Clock - Zero External Parts Needed)

```
        +5V DC Power Supply
           │
        [Pin 8: VCC] ─── [ 0.1µF Capacitor ] ─── GND
           │
        [Pin 1: PB5/RESET] ─── [ 10kΩ Resistor ] ─── +5V
           │
        [Pin 6: PB1] ─── [ 220Ω Resistor ] ─── (LED) ─── GND
```

## Flashing ATtiny85 using Arduino Uno as ISP

1. Open Arduino IDE $\to$ **Examples** $\to$ **11.ArduinoISP** $\to$ Upload to Arduino Uno.
2. Install **ATTinyCore** board package in Arduino IDE.
3. Select Board: **ATtiny25/45/85**, Processor: **ATtiny85**, Clock: **Internal 8 MHz**.

| Arduino Uno (ISP Programmer) | → | ATtiny85 DIP Pin |
|---|---|---|
| `5V` | | Pin 8 (`VCC`) |
| `GND` | | Pin 4 (`GND`) |
| `Digital 10` | | Pin 1 (`PB5 / RESET`) |
| `Digital 11` | | Pin 5 (`PB0 / MOSI`) |
| `Digital 12` | | Pin 6 (`PB1 / MISO`) |
| `Digital 13` | | Pin 7 (`PB2 / SCK`) |

## Example (Arduino ATTinyCore Blink Code)

```cpp
// On ATtiny85, PB1 corresponds to Arduino Pin 1
const int ledPin = 1; 

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  digitalWrite(ledPin, HIGH);
  delay(1000);
  digitalWrite(ledPin, LOW);
  delay(1000);
}
```

## Common mistakes

- **Disabling the RESET pin (`RSTDISBL` fuse):** Reprogramming `PB5` as a standard GPIO pin via the `RSTDISBL` fuse permanently disables serial ISP programming. High-Voltage Serial Programming (HVSP) is required to recover the chip.
- **Forgetting that `PB0` and `PB1` are used by the Digispark USB bootloader:** On Digispark boards, `PB3` and `PB4` are tied to USB $D+/D-$ pull-up lines.

## Notes

- **ATtiny85 Family:** ATtiny25 ($2\text{KB}$ Flash), ATtiny45 ($4\text{KB}$ Flash), **ATtiny85 ($8\text{KB}$ Flash)**.
