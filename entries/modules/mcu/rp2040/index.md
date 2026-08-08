## Overview

The **RP2040** is the flagship custom-designed microcontroller IC manufactured by Raspberry Pi Ltd. Powering the **Raspberry Pi Pico**, **Pico W**, Adafruit Feather RP2040, SparkFun Thing Plus, and hundreds of commercial keyboards and audio synthesizers, it features a **dual-core 32-bit ARM Cortex-M0+ processor** running at **$133\text{ MHz}$**.

The RP2040 stands out for its large **$264\text{ KB}$ multi-bank SRAM**, native **USB 1.1 Host and Device controller** (supporting Drag-and-Drop UF2 bootloading over USB), and groundbreaking **Programmable I/O (PIO)** subsystem—8 independent state machines capable of executing user assembly code to emulate hardware protocols (VGA video output, DVI/HDMI, I2S audio, WS2812 LED timing, and custom parallel interfaces) offloading the main CPU cores completely.

## Quick reference

| | |
|---|---|
| **CPU Architecture** | Dual-core ARM Cortex-M0+ at $133\text{ MHz}$ (Flexible clock up to $250\text{ MHz}+$) |
| **SRAM Memory** | $264\text{ KB}$ in 6 independent SRAM banks |
| **External Flash (XIP)** | Supports up to $16\text{ MB}$ external QSPI NOR Flash with XIP cache |
| **Package** | 56-pin QFN ($7 \times 7\text{ mm}$) with exposed ePad |
| **Programmable I/O (PIO)**| 8 state machines across 2 PIO blocks |
| **USB Interface** | Integrated USB 1.1 Controller (Host and Device) with internal PHY |
| **I/O & Analog** | 30 GPIO pins, 4-channel 12-bit ADC ($500\text{ kSPS}$) |
| **DMA Controller** | 12-channel DMA controller |
| **Bootloader** | Built-in ROM USB Mass Storage Bootloader (UF2 Drag-and-Drop) |

## Pinout (Raspberry Pi Pico Board Form Factor)

```
                       ┌─────────────┐
        (GP0/UART0 TX) [ GP0     VBUS] (5V USB Input)
        (GP1/UART0 RX) [ GP1    VSYS ] (1.8V-5.5V Main Power Input)
                       [ GND     GND ]
                 (GP2) [ GP2    3V3_EN] (3.3V Regulator Enable)
                 (GP3) [ GP3    3V3_OUT] (3.3V Power Output)
        (GP4/I2C0 SDA) [ GP4    ADC_VREF]
        (GP5/I2C0 SCL) [ GP5    GP28 ] (ADC2)
                       [ GND     GND ]
                 (GP6) [ GP6    GP27 ] (ADC1)
                 (GP7) [ GP7    GP26 ] (ADC0)
        (GP8/SPI0 RX)  [ GP8    RUN  ] (Reset Pin)
        (GP9/SPI0 CS)  [ GP9    GP22 ]
                       [ GND     GND ]
        (GP10/SPI0 SCK)[ GP10   GP21 ]
        (GP11/SPI0 TX) [ GP11   GP20 ]
        (GP12/I2C1 SDA)[ GP12   GP19 ] (SPI1 TX)
        (GP13/I2C1 SCL)[ GP13   GP18 ] (SPI1 SCK)
                       [ GND     GND ]
                (GP14) [ GP14   GP17 ] (SPI1 CS)
                (GP15) [ GP15   GP16 ] (SPI1 RX)
                       └─────────────┘
```

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Core Voltage | $V_{DD}$ | 1.05 | 1.10 | 1.20 | V | Internal LDO regulated |
| I/O Voltage | $IOVDD$ | 1.8 | 3.3 | 3.6 | V | GPIO supply rail |
| Active Core Current | $I_{RUN}$ | — | 18 | 30 | mA | Dual cores active at 133 MHz |
| Dormant Power Current | $I_{dorm}$| — | 0.18 | 1.0 | mA | Clock shut down |
| GPIO Output Drive Current| $I_{OH/OL}$| 2 | 4 / 8 | 12 | mA | Programmable 2/4/8/12mA |
| ADC Sample Rate | $f_{SAMP}$| — | 500 | — | kSPS | 12-bit ENOB = 8.7 bits |

## Wiring (Bare RP2040 Minimal Chip Implementation)

Designing a custom PCB with the bare RP2040 IC requires:
1. **QSPI Flash IC:** Winbond `W25Q16` ($2\text{ MB}$) or `W25Q128` ($16\text{ MB}$) connected to QSPI pins.
2. **Crystal Oscillator:** $12.000\text{ MHz}$ crystal connected to `XIN` and `XOUT` with $27\text{ pF}$ load capacitors.
3. **Decoupling Capacitors:** $100\text{ nF}$ ceramic caps on all `DVDD`, `IOVDD`, and `ADC_AVDD` supply pins.

## Example (MicroPython Dual-Core Code)

```python
import time
import _thread
from machine import Pin

led = Pin(25, Pin.OUT)

# Task running independently on Core 1
def core1_task():
    while True:
        print("Hello from RP2040 Core 1!")
        time.sleep(2)

# Start Core 1 thread
_thread.start_new_thread(core1_task, ())

# Main loop running on Core 0
while True:
    led.toggle()
    time.sleep(0.5)
```

## Common mistakes

- **Leaving `RUN` pin floating:** The `RUN` reset pin on the RP2040 has no internal pull-up. Leaving it floating causes random MCU resets. Connect a $10\ \text{k}\Omega$ pull-up resistor to 3.3V.
- **Forgetting 33 ohm series termination resistors on USB D+/D-:** The internal USB PHY requires $27\ \Omega \dots 33\ \Omega$ external series resistors on `USB_DP` and `USB_DM` lines for USB 1.1 signal integrity.

## Notes

- **RP2040 vs STM32F103 vs ESP32:** RP2040 offers $264\text{ KB}$ RAM with PIO state machines; STM32F103 offers $20\text{ KB}$ RAM; ESP32 adds Wi-Fi/Bluetooth.
