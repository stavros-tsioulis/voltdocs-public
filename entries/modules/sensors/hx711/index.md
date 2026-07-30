## Overview

The **HX711** is a precision 24-bit analog-to-digital converter (ADC) specifically designed for weigh scales and industrial process-control applications to interface directly with a wheatstone bridge sensor (load cell).

Manufactured by Avia Semiconductor, the IC integrates a low-noise programmable gain amplifier (PGA), an internal oscillator, an analog power regulator circuit, and a 2-wire serial interface (`PD_SCK` clock and `DOUT` data). It is universally used in DIY electronic weight scales, smart beehives, and force-measurement rigs.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 2.6 V – 5.5 V |
| **ADC Resolution** | 24-bit differential input ADC |
| **Selectable Gain / Channels** | Channel A (Gain 128 or 64); Channel B (Gain 32) |
| **Output Data Rate** | 10 SPS (Hz) or 80 SPS (selectable via `RATE` pin) |
| **Current Draw** | 1.5 mA operating / < 1 µA power-down |
| **Interface** | 2-wire serial interface (Clock & Data) |

## Pinout

### Standard HX711 Module Breakout

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Logic supply voltage (2.6 V to 5.5 V) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `DT` / `DOUT` | Digital Output | Serial Data Output (Active-LOW data ready signal) |
| 4 | `SCK` / `PD_SCK` | Digital Input | Power-Down and Serial Clock Input pin |
| 5 | `E+` / `AVDD` | Power | Load Cell Excitation Power Positive |
| 6 | `E-` / `AGND` | Power | Load Cell Excitation Power Ground |
| 7 | `A+` | Analog Input | Channel A Differential Signal Positive |
| 8 | `A-` | Analog Input | Channel A Differential Signal Negative |
| 9 | `B+` | Analog Input | Channel B Differential Signal Positive (optional second sensor) |
| 10 | `B-` | Analog Input | Channel B Differential Signal Negative (optional second sensor) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | `VCC` | 2.6 | 5.0 | 5.5 | V | Normal operation |
| Operating Current | `IVCC` | — | 1.5 | 1.8 | mA | $V_{CC} = 5\text{ V}$ |
| Power-Down Current | `IPD` | — | 0.5 | 1.0 | µA | $PD\_SCK = HIGH$ (> 60 µs) |
| Full-Scale Differential Input | $V_{id}$ | — | $\pm 20$ | — | mV | Channel A, Gain = 128 ($V_{AVDD} = 5\text{ V}$) |
| Common-Mode Input | $V_{cm}$ | `AGND` + 1.2 | — | `AVDD` - 1.3 | V | PGA operating range |
| Output Data Rate (10 Hz) | `fADC` | 9 | 10 | 11 | SPS | `RATE` pin tied to `GND` |
| Output Data Rate (80 Hz) | `fADC` | 72 | 80 | 88 | SPS | `RATE` pin tied to `VCC` |

## Communication

The HX711 communicates using a simple 2-wire serial format.

1. When output data is NOT ready for retrieval, `DOUT` remains `HIGH`.
2. When data becomes ready, `DOUT` drops to `LOW`.
3. The MCU applies 24 clock pulses to `PD_SCK`. Each rising edge of `PD_SCK` shifts out one bit of the 24-bit 2's complement binary data on `DOUT` (MSB first).
4. Pulses 25, 26, or 27 select the gain factor and input channel for the **NEXT** conversion:
   - **25 pulses:** Channel A, Gain 128
   - **26 pulses:** Channel B, Gain 32
   - **27 pulses:** Channel A, Gain 64

```
SCK  : __/‾\_/‾\_/‾\ ... (24 to 27 pulses) ... _
DOUT : D23  D22  D21 ... D0
```

## Wiring

### Standard Strain Gauge Load Cell Wire Colors to HX711 Module

| Load Cell Wire | → | HX711 Module Pin | Signal Name |
|---|---|---|---|
| Red Wire | | `E+` / `VCC` | Excitation Voltage + |
| Black Wire | | `E-` / `GND` | Excitation Voltage - |
| White Wire | | `A-` | Signal Output - |
| Green Wire | | `A+` | Signal Output + |

### HX711 Module to Microcontroller (Arduino Uno)

| HX711 Module Pin | → | Arduino Uno Pin | Notes |
|---|---|---|---|
| `VCC` | | `5V` | Logic & Excitation Power |
| `GND` | | `GND` | Ground |
| `DT` / `DOUT` | | Pin `A1` (or any GPIO) | Serial Data Line |
| `SCK` / `PD_SCK` | | Pin `A0` (or any GPIO) | Serial Clock Line |

## Common mistakes

- **Keeping SCK HIGH for > 60 µs:** Holding `PD_SCK` in a `HIGH` state for more than 60 microseconds forces the HX711 into ultra-low-power Sleep Mode. Ensure your GPIO bit-bang clock pulses complete cleanly without long interrupts.
- **Swapping load cell signal wires (A+ / A-):** Reversing `A+` and `A-` results in negative scale readings. Swap the green and white wires if weight readings decrease when load is applied.
- **Floating RATE pin:** Tie the `RATE` pin explicitly to `GND` for 10 Hz (low noise, recommended for scales) or `VCC` for 80 Hz dynamic sampling.

## Notes

- **Calibration & Tare:** Raw 24-bit integer values must be converted to physical mass (grams/kg) using a 2-point linear calibration equation:
  $$\text{Weight} = \frac{\text{Raw Reading} - \text{Tare Offset}}{\text{Scale Calibration Factor}}$$
