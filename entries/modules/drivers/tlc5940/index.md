## Overview

The TLC5940 is a 16-channel constant-current sink LED driver IC manufactured by Texas Instruments. Designed for high-density LED displays, RGB LED matrices, backlighting, and precision PWM control, it provides 12-bit (4096-step) grayscale pulse-width modulation (PWM) timing per channel alongside 6-bit (64-step) dot correction for individual channel brightness calibration.

The constant-current outputs sink up to 120 mA per channel (for `VCC` > 3.6V) and withstand up to 17V off-state voltage, making it suitable for driving long LED strings or high-power LEDs. All 16 channel currents are globally configured by a single external reference resistor (`IREF`). Multiple TLC5940 ICs can be easily daisy-chained using the serial data input (`SIN`) and serial data output (`SOUT`) pins.

## Quick reference

| | |
|---|---|
| **Function** | 16-Channel Constant-Current PWM LED Sink Driver |
| **Logic Supply Range (`VCC`)** | 3.0 V to 5.5 V DC |
| **Max Output Load Voltage (`VOUT`)** | 17.0 V DC |
| **Max Channel Current** | 120 mA (`VCC` > 3.6V) / 80 mA (`VCC` < 3.6V) |
| **PWM Resolution** | 12-Bit (4096 Steps per channel) |
| **Dot Correction** | 6-Bit (64 Adjustment Levels per channel) |
| **Max Clock Rate** | 30 MHz (`SCLK`), 30 MHz (`GSCLK`) |
| **Packages** | 28-pin PDIP, HTSSOP-28, QFN-32 |

## Pin configuration

| Pin (DIP-28) | Name | Type | Description |
|---|---|---|---|
| 1–5 | `OUT0`–`OUT4` | Output | Constant-current LED sink outputs 0 through 4 |
| 6 | `VPRG` | Input | Voltage Program Mode: Low = Grayscale Mode; High = Dot Correction Mode |
| 7 | `SIN` | Input | Serial Data Input for Grayscale and Dot Correction data |
| 8 | `SCLK` | Input | Serial Data Shift Clock (data shifted in on rising edge) |
| 9 | `XLAT` | Input | Latch Signal: Rising edge latches shifted data into internal registers |
| 10 | `BLANK` | Input | Blanking Signal: High turns off all `OUTn` outputs and resets internal GS counter |
| 11 | `GSRP` | Input | Grayscale Register Select Power: Internal pull-up |
| 12 | `GSCLK` | Input | Grayscale Clock: Drives the 12-bit internal PWM timing counter |
| 13 | `SOUT` | Output | Serial Data Output for daisy-chaining to next TLC5940 `SIN` |
| 14 | `XERR` | Output | Thermal Error & LED Open Signal (Open Drain, active low) |
| 15 | `IEF` | Output | Reference Current Output (connect `IREF` resistor to GND) |
| 16–27 | `OUT5`–`OUT15` | Output | Constant-current LED sink outputs 5 through 15 |
| 28 | `VCC` | Power | Logic supply input (3.0 V to 5.5 V) |
| — | `GND` | Power | Ground (Thermal pad on HTSSOP/QFN packages) |

## Functional description

The TLC5940 operates in two distinct data programming modes depending on the state of the `VPRG` pin:

1. **Grayscale (GS) Mode (`VPRG` = Low):** Shifts 192 bits (16 channels × 12 bits) of PWM duty cycle data into the serial shift register via `SIN` on `SCLK` rising edges. A high pulse on `XLAT` latches the data into the grayscale registers. The internal 12-bit counter increments on each `GSCLK` pulse, turning off each `OUTn` channel when the counter reaches its programmed 12-bit value.
2. **Dot Correction (DC) Mode (`VPRG` = High):** Shifts 96 bits (16 channels × 6 bits) of dot correction data into the registers to adjust individual LED channel gain between 0% and 100% of `IMAX`.

### Output Current Calculation

The maximum output current `IMAX` across all channels is set by a single resistor `RIREF` connected between pin `IEF` (`IREF`) and `GND`:

$$I_{\text{MAX}} = \frac{V_{\text{IREF}}}{R_{\text{IREF}}} \times 31.5 = \frac{1.24\,\text{V}}{R_{\text{IREF}}} \times 31.5 \approx \frac{39.06}{R_{\text{IREF}}}$$

For example, a $R_{\text{IREF}} = 2.0\,\text{k}\Omega$ resistor yields an $I_{\text{MAX}} \approx 19.5\,\text{mA}$ per channel.

## Absolute maximum ratings

> [!WARNING] Stresses beyond these values cause permanent damage. Limits, not operating conditions.

| Parameter | Rating | Unit |
|---|---|---|
| Logic Supply Voltage (`VCC`) | -0.3 to +6.0 | V |
| Output Voltage (`OUT0` to `OUT15`) | -0.3 to +18.0 | V |
| Input Voltage Range (`VPRG`, `SIN`, `SCLK`, `XLAT`, `BLANK`, `GSCLK`) | -0.3 to `VCC` + 0.3 | V |
| Continuous Output Current per Channel | 130 | mA |
| Operating Junction Temperature (`TJ`) | -40 to +150 | °C |

## Electrical characteristics

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | `VCC` | 3.0 | 5.0 | 5.5 | V | |
| Output Sink Voltage Range | `VOUT` | — | — | 17.0 | V | Off state |
| Constant-Current Output Range | `IOUT` | 5 | — | 120 | mA | `VCC` = 5V, `VOUT` = 1.2V |
| Reference Voltage (`IEF`) | `VIREF` | 1.20 | 1.24 | 1.28 | V | |
| `SCLK` Frequency | `fSCLK` | — | — | 30 | MHz | |
| `GSCLK` Frequency | `fGSCLK` | — | — | 30 | MHz | |

## Typical application

```
                    +5V VCC
                       |
               +-------+-------+
               |               |
             100nF           10uF
               |               |
              GND             GND
               |               |
               +-------+-------+----------+
                       |                  |
                    +--+------------------+--+
                    | 28                 15  |
                    | VCC               IEF  |
  MCU SPI MOSI ---->| 7 SIN                  |==== RIREF (2.0k) ===> GND
  MCU SPI SCK  ---->| 8 SCLK                 |
  MCU GPIO (XLAT) ->| 9 XLAT         OUT0--4 |----> [LED Cathodes] ---> +5V/+12V
  MCU GPIO (BLANK)->| 10 BLANK       OUT5-15 |----> [LED Cathodes] ---> +5V/+12V
  MCU PWM (GSCLK) ->| 12 GSCLK               |
  MCU GPIO (VPRG) ->| 6 VPRG            SOUT |---> Next TLC5940 SIN
                    | GND               XERR |---> MCU Interrupt (Optional)
                    +--+------------------+--+
                       |
                      GND
```

## Common mistakes

- **Missing `IREF` Resistor:** Leaving the `IEF` pin unconnected or shorted directly to GND will cause zero output current or excessive current that destroys the chip.
- **Forgetting `GSCLK` Pulses:** Unlike simple shift registers, TLC5940 REQUIRES a continuous clock signal on `GSCLK` (or 4096 pulses per PWM cycle) to increment the internal 12-bit PWM counter.
- **Not Pulsing `BLANK` High at Counter Rollover:** `BLANK` must be pulsed high every 4096 `GSCLK` cycles to reset the internal counter to 0 and re-enable outputs.
- **Floating `VPRG`:** `VPRG` must be driven low for normal Grayscale PWM operation. Leaving it floating puts the IC in an indeterminate mode.

## Notes & further reading

- Arduino Library: The `TLC5940` library by Alex Leone uses MCU hardware timers to generate `GSCLK` and `BLANK` signals automatically via interrupts.
- Power Dissipation: When driving 16 channels at 120 mA each, total IC dissipation can exceed 1.5 W. Ensure thermal pad (HTSSOP/QFN) is properly soldered to a ground plane heat sink.
