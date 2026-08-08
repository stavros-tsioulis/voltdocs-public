## Overview

The **HX711** is a precision 24-bit analog-to-digital converter (ADC) manufactured by Avia Semiconductor. It is specifically designed for weigh scales, strain-gauge load cells, and industrial process control applications.

The chip integrates a low-noise programmable gain amplifier (PGA), power supply regulator for sensor and ADC analog front-end, clock oscillator, and a 2-wire serial interface (`PD_SCK` and `DOUT`).

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 2.6 V to 5.5 V DC |
| **ADC resolution** | 24-bit differential |
| **Input channels** | 2 Differential Channels (Channel A & Channel B) |
| **Programmable Gain (Ch. A)** | 128 (default) or 64 |
| **Fixed Gain (Ch. B)** | 32 |
| **Output Data Rate** | 10 SPS or 80 SPS (pin-selectable via RATE) |
| **Communication interface** | 2-wire serial (`PD_SCK`, `DOUT`) |
| **Power-down current** | < 1 µA |

## Pinout

### Standard HX711 Breakout Module Pins

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `E+` / `VCC_LOAD` | Power Output | Excitation power positive (to load cell Red wire) |
| 2 | `E-` / `GND_LOAD` | Power Output | Excitation power negative / Ground (to load cell Black wire) |
| 3 | `A+` / `INA+` | Analog Input | Channel A differential input positive (to load cell Green wire) |
| 4 | `A-` / `INA-` | Analog Input | Channel A differential input negative (to load cell White wire) |
| 5 | `B+` / `INB+` | Analog Input | Channel B differential input positive (optional second sensor) |
| 6 | `B-` / `INB-` | Analog Input | Channel B differential input negative (optional second sensor) |
| 7 | `VCC` | Power | Digital logic supply voltage (+2.6 V to +5.5 V) |
| 8 | `GND` | Power | Digital Ground (0 V) |
| 9 | `DT` / `DOUT` | Digital Output | Serial data output pin |
| 10 | `SCK` / `PD_SCK` | Digital Input | Power-down and serial clock input pin |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.6 | 5.0 | 5.5 | V | |
| Analog Input Full-Scale (Ch. A, Gain 128) | $V_{ID}$ | — | $\pm 20$ | — | mV | $V_{REF} = 4.5\text{ V}$ |
| Analog Input Full-Scale (Ch. A, Gain 64) | $V_{ID}$ | — | $\pm 40$ | — | mV | $V_{REF} = 4.5\text{ V}$ |
| Analog Input Full-Scale (Ch. B, Gain 32) | $V_{ID}$ | — | $\pm 80$ | — | mV | $V_{REF} = 4.5\text{ V}$ |
| Output Data Rate (RATE = 0) | $f_{SPS}$ | — | 10 | — | Hz | Low noise, 50/60Hz rejection |
| Output Data Rate (RATE = 1) | $f_{SPS}$ | — | 80 | — | Hz | Fast sample rate |
| Normal Operating Current | $I_{CC}$ | — | 1.5 | 2.1 | mA | $V_{CC} = 5.0\text{ V}$ |
| Power-Down Current | $I_{pd}$ | — | 0.5 | 1.0 | µA | $PD\_SCK = HIGH$ for $>60\text{ }\mu\text{s}$ |

## Communication protocol

Communication with the HX711 uses a simple bit-banging protocol over `PD_SCK` and `DOUT`:

1. When data is ready for retrieval, `DOUT` goes **LOW**.
2. Apply 24 clock pulses to `PD_SCK` to shift out the 24-bit raw conversion result (MSB first).
3. Apply 1, 2, or 3 additional clock pulses (total 25, 26, or 27 pulses) to select the channel and gain for the *next* conversion:
   - **25 pulses:** Channel A, Gain 128
   - **26 pulses:** Channel B, Gain 32
   - **27 pulses:** Channel A, Gain 64

```
DOUT    ───┐                                          ┌───
           └──────────────────────────────────────────┘
PD_SCK  _____┌─┐_┌─┐_ ... _┌─┐_┌─┐_┌─┐_______________
Pulse #      1   2         24  25  26 (Gain/Ch select)
```

## Wiring

### Load Cell to HX711 Module Wiring

| Load Cell Wire Color | Standard Signal | HX711 Terminal |
|---|---|---|
| Red | Excitation + (`E+`) | `E+` |
| Black | Excitation - (`E-`) | `E-` |
| Green | Signal + (`A+`) | `A+` |
| White | Signal - (`A-`) | `A-` |

### HX711 Module to Microcontroller

| HX711 Pin | → | Microcontroller (Arduino Uno / ESP32) |
|---|---|---|
| `VCC` | | `5V` (or `3.3V`) |
| `GND` | | `GND` |
| `DT` / `DOUT` | | Digital Pin `3` (GPIO input pin) |
| `SCK` / `PD_SCK` | | Digital Pin `2` (GPIO output pin) |

> [!WARNING]
> High `PD_SCK` Hold Time Enters Power-Down Mode:
> If `PD_SCK` is held `HIGH` for longer than **60 µs**, the HX711 enters sleep mode and powers off internal circuitry. Ensure microcontroller interrupts do not freeze `PD_SCK` HIGH during serial reads.

## Common mistakes

- **Leaving RATE pin floating:** On some modules, the `RATE` pin selects sample rate (10 Hz vs 80 Hz). Floating `RATE` can cause intermittent noise or sample rate drops.
- **Handling 24-bit 2's complement sign extension:** The HX711 returns a 24-bit signed integer. When storing in a 32-bit `int32_t` variable, if bit 23 is `1` (negative number), you must perform sign extension by OR-ing with `0xFF000000`.
- **Powering load cell from noisy rail:** Load cell readings drift significantly if supply voltage is unstable. Ensure the onboard regulator on the HX711 module is active and properly decoupled.

## Notes

- Calibration requires taking a tare (zero-weight offset) reading followed by placing a known calibration weight on the scale to compute the scale factor ($\text{Weight} = \frac{\text{Raw Reading} - \text{Tare}}{\text{Scale Factor}}$).
