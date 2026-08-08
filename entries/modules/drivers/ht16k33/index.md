## Overview

The **HT16K33** is a memory-mapped and multi-function LED controller IC manufactured by Holtek Semiconductors. Communicating via an **$I^2C$ bus interface** ($400\text{ kHz}$ Fast Mode), it can drive up to **128 individual LEDs** ($16 \times 8$ matrix or up to 8 digits of 7-segment / 14-segment displays) while simultaneously scanning a $13 \times 3$ key matrix.

Equipped with an internal RC oscillator, 16-step global PWM dimming control, and hardware $I^2C$ address selection jumpers ($0\text{x}70 \dots 0\text{x}77$), the HT16K33 is the standard driver IC powering Adafruit's 7-segment display backpacks, 14-segment alphanumeric displays, and $8 \times 8$ dot matrix LED modules.

## Quick reference

| | |
|---|---|
| **Operating Voltage (`VDD`)** | 4.5 V to 5.5 V DC (I2C SDA/SCL lines 3.3V compatible) |
| **Max LED Output Capacity** | 128 LEDs ($16 \text{ Anodes} \times 8 \text{ Cathodes}$) |
| **Keyscan Capability** | Up to 39 switches ($13 \times 3$ matrix) |
| **PWM Dimming Control** | 16 Levels ($1/16$ to $16/16$ duty cycle) |
| **I2C Bus Speed** | $100\text{ kHz}$ Standard Mode / $400\text{ kHz}$ Fast Mode |
| **I2C Address Range** | $0\text{x}70$ to $0\text{x}77$ (Configured via A0, A1, A2 jumpers) |
| **Package** | 28-pin SOP / 24-pin SOP / Breakout Module |

## Pinout & Module Terminals

### SOP-28 Package IC

```
             ┌───┴───┐
       VSS 1 │ 1   28│ VDD
     COM0 2  │       │ 27 ROW15 / A15
     COM1 3  │       │ 26 ROW14 / A14
     COM2 4  │       │ 25 ROW13 / A13
     COM3 5  │ HT16K │ 24 ROW12 / A12
     COM4 6  │  33   │ 23 ROW11 / A11
     COM5 7  │       │ 22 ROW10 / A10
     COM6 8  │       │ 21 ROW9 / A9
     COM7 9  │       │ 20 ROW8 / A8
   ROW0/A0 10│       │ 19 SCL
   ROW1/A1 11│       │ 18 SDA
   ROW2/A2 12│       │ 17 VDD
   ROW3/A3 13│       │ 16 INT / KEY INT
   ROW4/A4 14│       │ 15 ROW5 / A5
             └───────┘
```

### Module Header Terminals (Adafruit LED Backpack)

| Terminal | Function | Description |
|---|---|---|
| `VCC` | Power | Supply Voltage (+4.5V to +5.5V DC) |
| `GND` | Power | System Ground (0 V) |
| `SDA` | I2C Data | Serial Data line (Connect to MCU SDA; 3.3V / 5V tolerant) |
| `SCL` | I2C Clock | Serial Clock line (Connect to MCU SCL; 3.3V / 5V tolerant) |
| `A0, A1, A2` | Jumpers | Solder jumpers to change I2C address from default $0\text{x}70$ |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 4.5 | 5.0 | 5.5 | V | DC |
| Operating Current | $I_{DD}$ | — | 2.0 | 4.0 | mA | No load, $V_{DD} = 5\text{V}$ |
| Standby Current | $I_{STB}$ | — | 0.1 | 10.0 | µA | Standby mode |
| I2C Clock Frequency | $f_{SCL}$ | — | — | 400 | kHz | $V_{DD} = 5\text{V}$ |
| Segment Drive Current | $I_{SEG}$ | 20 | 25 | 30 | mA | $V_{DD} = 5\text{V}, V_{OUT} = V_{DD}-1.0\text{V}$ |
| COM Drive Current | $I_{COM}$ | 120 | 150 | 180 | mA | $V_{DD} = 5\text{V}, V_{OUT} = 0.6\text{V}$ |

## Wiring & Code Example (Arduino)

```
   HT16K33 Backpack                        Arduino Uno
    [ VCC ] ───────────────────────────── 5V
    [ GND ] ───────────────────────────── GND
    [ SDA ] ───────────────────────────── A4 (SDA)
    [ SCL ] ───────────────────────────── A5 (SCL)
```

```cpp
#include <Wire.h>
#include <Adafruit_GFX.h>
#include "Adafruit_LEDBackpack.h"

Adafruit_7segment matrix = Adafruit_7segment();

void setup() {
  matrix.begin(0x70); // Initialize HT16K33 at I2C address 0x70
  matrix.setBrightness(10); // Set brightness (0 to 15)
  matrix.print(1234, DEC);
  matrix.writeDisplay();
}

void loop() {}
```

## Common mistakes

- **Forgetting System Clock Enable command over I2C:** The HT16K33 powers up in standby mode with its internal RC oscillator disabled. You must issue the **System Setup command `0x21` (Oscillator ON)** followed by **Display Setup command `0x81` (Display ON, No Blink)** over I2C before any LEDs will turn on.
- **Wrong I2C address:** The default I2C address is **$0\text{x}70$** (when A0, A1, A2 solder jumpers are open). If solder jumpers are bridged, the address shifts up to $0\text{x}77$. Run an I2C scanner sketch if the display fails to respond.
- **Powering from 3.3V without checking VDD range:** Official HT16K33 spec lists $V_{DD} = 4.5\text{V} \dots 5.5\text{V}$. While 3.3V logic signals on SDA/SCL work fine, powering $V_{DD}$ itself from 3.3V may leave blue or white LEDs under-powered due to their higher forward voltage drop ($V_f \approx 3.2\text{V}$).

## Notes

- **HT16K33 vs MAX7219 vs TM1637:** HT16K33 uses **I2C** ($0\text{x}70$) and drives 128 LEDs ($16 \times 8$); MAX7219 uses **SPI** and drives 64 LEDs ($8 \times 8$); TM1637 uses a 2-wire custom bitbang protocol for 6 digits.
