## Overview

The **PIC12F683** is a compact 8-pin Flash-based 8-bit CMOS microcontroller manufactured by Microchip Technology. Available in an 8-pin through-hole **DIP-8** and surface-mount **SOIC-8** package, it features Microchip's **nanoWatt technology** ($< 1\ \mu\text{A}$ standby power) and an internal software-selectable $8\text{ MHz}$ precision RC oscillator.

Equipped with **2K words ($3.5\text{ KB}$) of Flash program memory**, **128 bytes of RAM**, **256 bytes of EEPROM**, a 4-channel 10-bit ADC, three hardware timers, an analog comparator, and a Capture/Compare/PWM (CCP) module, the PIC12F683 gained widespread fame in DIY electronics for **game console modifications (rapid-fire modchips), servo exercisers, smart RGB lighting controllers, and ultra-compact battery monitors**.

## Quick reference

| | |
|---|---|
| **CPU Core** | 8-bit PIC Mid-Range RISC (35 instructions) |
| **Package** | 8-pin DIP (DIP-8 / PDIP-8) / 8-pin SOIC / 8-pin DFN |
| **Max Clock Frequency** | $20\text{ MHz}$ ($8\text{ MHz}$ software-calibrated internal RC) |
| **Flash Program Memory** | 2048 words ($3.5\text{ KB}$, 14-bit word width) |
| **Data RAM** | 128 bytes |
| **Data EEPROM** | 256 bytes true non-volatile EEPROM |
| **Operating Voltage (`VDD`)** | $2.0\text{ V}$ to $5.5\text{ V}$ DC ($4.5\text{V} \dots 5.5\text{V}$ for $20\text{MHz}$) |
| **GPIO Count** | 6 I/O pins (GP0 through GP5; GP3 is input-only) |
| **ADC Channels** | 4 channels (10-bit resolution) |
| **CCP / PWM** | 1 Capture/Compare/PWM module (10-bit PWM resolution) |
| **In-Circuit Serial Programming** | ICSP via `GP0` (ICSPDAT), `GP1` (ICSPCLK), and `GP3` (MCLR/VPP) |

## Pinout (DIP-8 Package)

```
                            ┌───┴───┐
                  VDD (+5V) 1│ 1   8 │ VSS (GND 0V)
 (T1CKI/OSC1/CLKIN)     GP5 2│PIC12F │ 7 GP0 (AN0/CIN+/ICSPDAT)
 (AN3/T1G/OSC2/CLKOUT)  GP4 3│  683  │ 6 GP1 (AN1/CIN-/VREF/ICSPCLK)
 (Active-Low/VPP/MCLR)  GP3 4│ DIP-8 │ 5 GP2 (AN2/T0CKI/INT/COUT/CCP1)
                            └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VDD` | Power | Positive Supply Voltage ($+2.0\text{ V}$ to $+5.5\text{ V}$ DC) |
| 2 | `GP5` | GPIO / Clock | `T1CKI` (Timer1 Clock) / `OSC1` / `CLKIN` |
| 3 | `GP4` | GPIO / Analog | `AN3` / `T1G` (Timer1 Gate) / `OSC2` / `CLKOUT` |
| 4 | `GP3` | Digital Input | `MCLR` (Master Clear / Reset) / `VPP` (Programming Voltage) (Input-only) |
| 5 | `GP2` | GPIO / Analog | `AN2` / `T0CKI` / `INT` / `COUT` / `CCP1` (PWM Output) |
| 6 | `GP1` | GPIO / Analog | `AN1` / `CIN-` / `VREF` / `ICSPCLK` (Programming Clock) |
| 7 | `GP0` | GPIO / Analog | `AN0` / `CIN+` / `ICSPDAT` (Programming Data) |
| 8 | `VSS` | Power | Common Ground reference ($0\text{ V}$) |

## Programming Connections (PICkit 3 / 4 / Snap ICSP Header)

```
   PICkit ICSP Pin                  PIC12F683 DIP-8 Pin
   ┌──────────────┐                ┌──────────────────────┐
   │ 1: VPP / MCLR├───────────────►│ Pin 4: GP3 / MCLR/VPP│
   │ 2: VDD (+5V) ├───────────────►│ Pin 1: VDD (+5V)     │
   │ 3: VSS (GND) ├───────────────►│ Pin 8: VSS (GND)     │
   │ 4: PGD (Data)├───────────────►│ Pin 7: GP0 / ICSPDAT │
   │ 5: PGC (Clock)───────────────►│ Pin 6: GP1 / ICSPCLK │
   └──────────────┘                └──────────────────────┘
```

## Common mistakes

- **Attempting to configure GP3 as an output:** Pin 4 (`GP3`) is **input-only** in hardware due to the high-voltage `VPP`/`MCLR` circuitry. It cannot be driven as an output pin.
- **Forgetting to set `ANSEL` for digital I/O:** Pins GP0, GP1, GP2, and GP4 default to analog input mode on power-up. Write `ANSEL = 0;` and `CMCON0 = 7;` in software to use pins as standard digital GPIOs.
- **Floating MCLR pin:** If `MCLRE` configuration bit is ON, Pin 4 must be tied to $V_{DD}$ via a **$10\text{ k}\Omega$ pull-up resistor**. Alternatively, configure internal MCLR in the configuration word (`_MCLRE_OFF`).

## Notes

- **Software Ecosystem:** Programmed using MPLAB X IDE with the free Microchip XC8 C compiler, or open-source SDCC (`sdcc -mpic14`).
