## Overview

The **RP2350** is Raspberry Pi's second-generation high-performance microcontroller IC. Operating at clock speeds up to **$150\text{ MHz}$**, it features a unique **dual-architecture core setup**: developers can select at boot between dual **ARM Cortex-M33** cores with hardware floating point (FPU) and ARM TrustZone security, or dual **Hazard3 32-bit RISC-V** open-source cores.

It doubles the on-chip SRAM of its predecessor (RP2040) to **$520\text{ KB}$**, expands the Programmable I/O (PIO) capacity to **12 independent state machines**, and introduces hardware-accelerated SHA-256, TRNG, and OTP memory for secure boot and cryptography.

## Quick reference

| | |
|---|---|
| **CPU Core Architecture** | Selectable Dual ARM Cortex-M33 (with FPU/TrustZone) or Dual Hazard3 RISC-V |
| **Max Clock Frequency** | $150\text{ MHz}$ |
| **SRAM** | $520\text{ KB}$ (10 independent banks) |
| **External Flash Support** | Up to $16\text{ MB}$ QSPI Flash with XIP & 8KB Cache (RP2354 variants include 2MB internal QSPI Flash) |
| **PIO State Machines** | 12 (3 PIO blocks $\times$ 4 state machines) |
| **Core Supply Voltage** | 1.1 V DC (internal buck regulator) |
| **I/O Supply Voltage** | 1.8 V to 3.3 V DC |
| **ADC Channels** | 4 channels (RP2350A) / 8 channels (RP2350B) (12-bit, $500\text{ ksps}$) |
| **High-Speed Serial Output** | HSTX (High-Speed Serial Transmit for DVI/HDMI output) |
| **Package** | 56-pin QFN (RP2350A) / 80-pin QFN (RP2350B) / Raspberry Pi Pico 2 |

## Pinout (Raspberry Pi Pico 2 Board Header Layout)

```
                       ┌─────────────┐
        (GP0 / UART0 TX) 1│ 1   40│ VBUS (5V USB Power)
       (GP1 / UART0 RX) 2│       │39 VSYS (Main Supply Input 1.8-5.5V)
                  [GND] 3│       │38 GND
        (GP2 / I2C1 SDA) 4│       │37 3V3_EN (Enable 3.3V Regulator)
        (GP3 / I2C1 SCL) 5│ RP2350│36 3V3 (3.3V Output)
        (GP4 / SPI0 RX)  6│ Pico 2│35 ADC_VREF (ADC Reference Voltage)
        (GP5 / SPI0 CS)  7│       │34 GP28 / ADC2
                  [GND] 8│       │33 GND
        (GP6 / SPI0 SCK) 9│       │32 GP27 / ADC1
        (GP7 / SPI0 TX) 10│       │31 GP26 / ADC0
                        └─────────────┘
```

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Core Supply Voltage | $V_{DD\_CORE}$ | 0.95 | 1.1 | 1.3 | V | Internal buck regulator |
| I/O Supply Voltage | $V_{DD\_IO}$ | 1.8 | 3.3 | 3.63 | V | I/O power rails |
| Run Mode Current | $I_{RUN}$ | — | 18 | 35 | mA | Dual Cortex-M33 at 150 MHz |
| DORMANT Mode Current | $I_{DORMANT}$| — | 10 | 25 | µA | All clocks stopped |
| GPIO Output Drive | $I_{IO}$ | 2 | 4 | 12 | mA | Configurable drive strength |
| ADC Sample Rate | $f_{ADC}$ | — | 500 | — | ksps | 12-bit ENOB ~ 10.5 bits |

## Example (C/C++ Pico SDK - Dual Core Execution)

```cpp
#include "pico/stdlib.h"
#include "pico/multicore.h"

void core1_entry() {
    while (1) {
        // Task running on Core 1
        tight_loop_contents();
    }
}

int main() {
    stdio_init_all();
    
    // Launch function on Core 1
    multicore_launch_core1(core1_entry);
    
    const uint LED_PIN = 25; // Onboard LED on Pico 2
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);
    
    while (1) {
        gpio_put(LED_PIN, 1);
        sleep_ms(250);
        gpio_put(LED_PIN, 0);
        sleep_ms(250);
    }
}
```

## Common mistakes

- **Ignoring the RP2350 A2 stepping latch-up glitch on GPIO inputs:** Early production A2 silicon revisions had an erratum where pulling certain GPIO pins high with weak internal pull-up enabled could cause a pin latch-up state ($\sim 2.1\text{V}$ voltage lock). Ensure firmware uses active external pull-ups or firmware workarounds provided in updated Pico SDK releases.
- **Powering core without adequate bypass capacitors:** RP2350 requires low-ESR $1\ \mu\text{F}$ decoupling capacitors on the DVDD internal regulator output pins for stable 150MHz execution.

## Notes

- **RP2350 vs RP2040:** RP2350 increases clock speed from 133MHz to 150MHz, doubles SRAM from 264KB to 520KB, upgrades CPU architecture (Cortex-M33 / RISC-V vs Cortex-M0+), increases PIO state machines from 8 to 12, and adds hardware security features.
