## Overview

The **ATmega2560** is a high-performance, low-power 8-bit AVR RISC microcontroller IC manufactured by Microchip Technology (formerly Atmel). Featuring **$256\text{ KB}$ of Flash memory**, **$8\text{ KB}$ of SRAM**, and **$4\text{ KB}$ of EEPROM**, it is best known as the core processor of the **Arduino Mega 2560 R3** development board.

With **86 general-purpose I/O lines**, 16 analog input channels (10-bit ADC), 15 PWM outputs, 4 hardware USART serial ports, and a hardware SPI and $I^2C$ controller, it is a staple for complex 3D printer controllers (RAMPS 1.4), robotics control systems, multi-sensor weather stations, and automation rigs.

## Quick reference

| | |
|---|---|
| **CPU Core** | 8-bit AVR RISC |
| **Max Clock Frequency** | $16\text{ MHz}$ (at $5\text{V}$) / $20\text{ MHz}$ max |
| **Flash Memory** | $256\text{ KB}$ ($8\text{ KB}$ used by bootloader) |
| **SRAM** | $8\text{ KB}$ |
| **EEPROM** | $4\text{ KB}$ |
| **Operating Voltage (`VCC`)** | 4.5 V to 5.5 V DC (for 16 MHz operation) |
| **GPIO Count** | 86 I/O pins |
| **ADC Channels** | 16 channels (10-bit resolution) |
| **PWM Outputs** | 15 channels |
| **Hardware USARTs** | 4 independent serial ports (`Serial`, `Serial1`, `Serial2`, `Serial3`) |
| **Package** | 100-pin TQFP ($14 \times 14\text{ mm}$) / Arduino Mega 2560 Board |

## Pinout (Arduino Mega 2560 Board Pin Groups)

```
                         Arduino Mega 2560 Headers
                   ┌──────────────────────────────────┐
     (Power)       │ 5V, 3.3V, GND, VIN, RESET        │
     (Analog Inputs)│ A0 – A15 (16x 10-bit ADC)        │
     (Digital I/O) │ D0 – D53 (PWM on 2–13, 44–46)    │
     (Communication)│ 4x USART (Serial 0-3), SPI, I2C │
                   └──────────────────────────────────┘
```

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 4.5 | 5.0 | 5.5 | V | 16 MHz operation |
| Active Supply Current | $I_{CC}$ | — | 10 | 20 | mA | 16 MHz at 5.0V |
| Power-down Current | $I_{PD}$ | — | 0.1 | 2.0 | µA | $WDT$ disabled, 5.0V |
| DC Current per I/O Pin | $I_{DC}$ | -40 | — | +40 | mA | Maximum rating per pin |
| ADC Clock Frequency | $f_{ADC}$ | 50 | 200 | 1000 | kHz | 10-bit resolution |

## Example (Arduino Code - 4x Hardware Serial Monitor)

```cpp
void setup() {
  // Initialize all 4 hardware serial ports at different baud rates
  Serial.begin(115200); // Main USB Serial (Pins 0 & 1)
  Serial1.begin(9600);  // Serial 1 (Pins 19 RX1, 18 TX1) - e.g. GPS
  Serial2.begin(9600);  // Serial 2 (Pins 17 RX2, 16 TX2) - e.g. Bluetooth
  Serial3.begin(9600);  // Serial 3 (Pins 15 RX3, 14 TX3) - e.g. RS485

  Serial.println("ATmega2560 Quad-USART Initialized!");
}

void loop() {
  // Relay data from Serial1 (GPS) to USB Serial
  while (Serial1.available()) {
    char c = Serial1.read();
    Serial.write(c);
  }
}
```

## Common mistakes

- **Attempting to run at 16 MHz from a 3.3V power rail:** The ATmega2560 safe operating frequency chart specifies a minimum supply of $4.5\text{V}$ for $16\text{ MHz}$ operation. Running at $3.3\text{V}$ requires reducing clock speed to $\le 8\text{ MHz}$.
- **Exceeding total VCC/GND bus current limits:** While individual GPIO pins can sink/source up to $40\text{ mA}$, the total combined current through all $V_{CC}$ or $GND$ supply pins must not exceed **$200\text{ mA}$**.

## Notes

- **ATmega2560 vs ATmega328P:** ATmega2560 provides 8x Flash ($256\text{ KB}$ vs $32\text{ KB}$), 4x SRAM ($8\text{ KB}$ vs $2\text{ KB}$), 4x USARTs (vs 1), and 86 GPIOs (vs 23).
