## Overview

The **ATM90E32** (ATM90E32AS) is a high-performance 3-phase polyphase Analog Front End (AFE) energy metering IC manufactured by Microchip Technology (formerly Atmel). Built for utility-grade electricity meters, smart solar inverters, and whole-house panel energy monitors, it integrates **six 16-bit ADCs** to simultaneously measure 3-phase AC voltage and 3-phase AC current.

Achieving Class 0.2 accuracy across a **6000:1 dynamic range**, the ATM90E32 computes active power (W), reactive power (VAR), apparent power (VA), active energy (kWh), RMS voltage ($V_{RMS}$), RMS current ($I_{RMS}$), grid frequency (Hz), power factor (PF), phase angles, and harmonic distortion per phase over a 4-wire SPI bus. It is widely used in ESPHome multi-channel energy monitors and IoTaWatt hardware.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VDD`)** | 3.0 V to 3.6 V DC (3.3 V nominal) |
| **Phases supported** | 3-Phase 4-Wire (Wye), 3-Phase 3-Wire (Delta), or 3 Single-Phase Circuits |
| **ADC architecture** | 6 independent 16-bit Sigma-Delta ADCs (3 Voltage + 3 Current) |
| **Metering accuracy** | Class 0.2 ($\pm 0.2\%$) |
| **Dynamic range** | 6000 : 1 |
| **Interface** | 4-Wire SPI (up to 2 MHz) |
| **Current inputs** | Supports Current Transformers (CT coils) or Rogowski coils |
| **Voltage inputs** | Supports AC-AC Voltage Transformers (VT) or resistor dividers |

## Pinout (48-Pin TQFP Package & SPI Header)

SPI Header & Analog Sensing Pins:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VDD` | Power | Digital core supply (+3.3 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `CS` / `SS` | Digital Input | Active-Low SPI Chip Select |
| 4 | `SCLK` | Digital Input | SPI Serial Clock |
| 5 | `SDI` / `MOSI`| Digital Input | SPI Data Input |
| 6 | `SDO` / `MISO`| Digital Output | SPI Data Output |
| 7 | `IRQ0` / `WARN`| Digital Output | Active-Low interrupt output (voltage sag / over-current) |
| 8–10| `VP`, `VN`, `VP2`| Analog Input | Phase A, B, C Voltage sense inputs ($V_{peak} \le 800\text{ mV}$) |
| 11–16| `I1P`/`I1N`, `I2P`/`I2N`, `I3P`/`I3N`| Analog Input | Phase A, B, C Current transformer differential inputs ($V_{peak} \le 800\text{ mV}$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 3.0 | 3.3 | 3.6 | V | DC |
| Active Supply Current | $I_{DD}$ | — | 13.0 | 18.0 | mA | All 6 ADCs active |
| Active Energy Accuracy | $E_{act}$ | -0.2% | $\pm 0.1\%$| +0.2%| — | Dynamic range 6000:1 |
| Reactive Energy Accuracy| $E_{react}$| -0.2% | $\pm 0.1\%$| +0.2%| — | Dynamic range 6000:1 |
| Voltage Analog Input | $V_{IN\_V}$ | -800 | — | +800 | mV Peak | Differential peak voltage |
| Current Analog Input | $V_{IN\_I}$ | -800 | — | +800 | mV Peak | Differential peak voltage |
| SPI Clock Frequency | $f_{SPI}$ | 0 | 1.0 | 2.0 | MHz | SPI Mode 3 ($CPOL=1, CPHA=1$) |

## Polyphase Register Map

Registers are 16-bit words accessed over SPI:

| Address | Register Name | Unit | Description |
|---|---|---|---|
| `0xD1` | `UrmsA` | $0.01\text{ V}$ | Phase A RMS Voltage |
| `0xD2` | `UrmsB` | $0.01\text{ V}$ | Phase B RMS Voltage |
| `0xD3` | `UrmsC` | $0.01\text{ V}$ | Phase C RMS Voltage |
| `0xDD` | `IrmsA` | $0.001\text{ A}$ | Phase A RMS Current |
| `0xDE` | `IrmsB` | $0.001\text{ A}$ | Phase B RMS Current |
| `0xDF` | `IrmsC` | $0.001\text{ A}$ | Phase C RMS Current |
| `0xE1` | `PmeanA` | $0.001\text{ W}$ | Phase A Active Power |
| `0xF1` | `PFmeanA` | $0.001$ | Phase A Power Factor |

## Wiring

| ATM90E32 Pin | → | ESP32 GPIO | Arduino (3.3V) | Notes |
|---|---|---|---|---|
| `VDD` | | 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `SCLK`| | GPIO 18 | Digital D13 | SPI Clock |
| `SDO` (MISO)| | GPIO 19 | Digital D12 | SPI MISO |
| `SDI` (MOSI)| | GPIO 23 | Digital D11 | SPI MOSI |
| `CS`  | | GPIO 5 | Digital D10 | SPI Chip Select |

## Example (ESPHome Configuration snippet)

```yaml
sensor:
  - platform: atm90e32
    cs_pin: GPIO5
    phase_a:
      voltage:
        name: "Phase A Voltage"
      current:
        name: "Phase A Current"
      power:
        name: "Phase A Power"
      gain_voltage: 36704
      gain_current: 38532
    phase_b:
      voltage:
        name: "Phase B Voltage"
      current:
        name: "Phase B Current"
      power:
        name: "Phase B Power"
      gain_voltage: 36704
      gain_current: 38532
    phase_c:
      voltage:
        name: "Phase C Voltage"
      current:
        name: "Phase C Current"
      power:
        name: "Phase C Power"
      gain_voltage: 36704
      gain_current: 38532
    frequency:
      name: "Grid Frequency"
```

## Common mistakes

- **SPI Mode Misconfiguration:** The ATM90E32 requires **SPI Mode 3** ($CPOL=1, CPHA=1$). Setting Mode 0 results in corrupted SPI register reads (`0xFFFF` or zero values).
- **Exceeding $\pm 800\text{ mV}$ peak analog inputs:** The differential current/voltage inputs connect directly to internal 16-bit Sigma-Delta ADCs. Signals exceeding $800\text{ mV}$ peak saturate the ADCs and distort calculations. Ensure burden resistors on CT coils step down current signals below $500\text{ mV}$ RMS.

## Notes

- **ATM90E32 vs ATM90E26:** ATM90E26 is single-phase ($1\times \text{Voltage}, 2\times \text{Current}$); ATM90E32 is 3-phase polyphase ($3\times \text{Voltage}, 3\times \text{Current}$).
