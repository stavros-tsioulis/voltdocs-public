## Overview

The **TLC5947** is a 24-channel constant-current sink LED driver IC manufactured by Texas Instruments. It features individually programmable **12-bit (4,096 step) PWM grayscale brightness control** for each of its 24 outputs.

Widely featured on Adafruit 24-channel PWM LED breakout boards, the TLC5947 is designed for LED matrix displays, RGB LED mood lighting, backlighting, and servo control arrays. Operating from **3.0V to 5.5V DC**, its open-drain constant-current outputs withstand up to **30V DC**, allowing multiple series-connected LEDs per channel. Peak current across all channels is set globally using a single external resistor ($R_{IREF}$).

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | 3.0 V to 5.5 V DC |
| **Output Voltage Limit (`VOUT`)**| Up to 30.0 V DC (Open-drain constant-current outputs) |
| **LED Channels** | 24 Open-Drain Constant-Current Outputs (`OUT0` to `OUT23`) |
| **PWM Grayscale Resolution**| 12-bit (4096 brightness levels per output channel) |
| **Constant Current Range** | $2.0\text{ mA}$ to $30.0\text{ mA}$ per channel (Set via $R_{IREF}$) |
| **Serial Interface Speed** | Up to $30.0\text{ MHz}$ (`SCLK`) |
| **Internal Oscillator** | $4.0\text{ MHz}$ internal PWM clock oscillator |
| **Package** | 32-pin HTSSOP (Pad Down) / 32-pin QFN |

## Pinout (HTSSOP-32 Package)

```
                       ┌─────────────┐
                 [GND] 1│ 1        32│ [VCC] (+3.0V to +5.5V)
                [BLANK] 2│            │31 [SOUT] (Daisy-Chain Out)
                 [SCLK] 3│            │30 [IREF] (Current Set Resistor)
                  [SIN] 4│  TLC5947   │29 [LAT] (Latch Pulse Input)
                 [OUT0] 5│  HTSSOP-32 │28 [OUT23]
                 [OUT1] 6│            │27 [OUT22]
                  ...   │            │...
                [OUT11] 16│            │17 [OUT12]
                       └─────────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` | Power | Ground reference (0 V) |
| 2 | `BLANK` | Input | Blanking Control Input (High = Turn off all outputs; Low = Enable PWM) |
| 3 | `SCLK` | Input | Serial Data Clock Input |
| 4 | `SIN` | Input | Serial Data Input |
| 5–16 | `OUT0`–`OUT11` | Output | Channels 0 to 11 Constant-Current Sink Outputs |
| 17–28 | `OUT12`–`OUT23` | Output | Channels 12 to 23 Constant-Current Sink Outputs |
| 29 | `LAT` | Input | Latch Pulse Input (Rising edge transfers shift register data into PWM latches) |
| 30 | `IREF` | Input | Reference Current Setting Pin (Connect resistor $R_{IREF}$ to GND) |
| 31 | `SOUT` | Output | Serial Data Output for Daisy-Chaining (Connect to `SIN` of next TLC5947) |
| 32 | `VCC` | Power | Power Supply Input (+3.0V to +5.5V DC) |

## Output Current Formula

The maximum constant-current sink capability ($I_{MAX}$) per channel is programmed via a single resistor $R_{IREF}$ connected between `IREF` (Pin 30) and `GND`:

$$ I_{MAX} = \frac{V_{IREF}}{R_{IREF}} \times 41.5 \approx \frac{1.20\text{V}}{R_{IREF}} \times 41.5 = \frac{49.8}{R_{IREF}} \text{ (Amps)} $$

$$\text{For } I_{MAX} = 20\text{ mA} \implies R_{IREF} \approx \frac{49.8}{0.020\text{A}} \approx 2.49\text{ k}\Omega.$$

## Common mistakes

- **Leaving `BLANK` (Pin 2) floating:** `BLANK` disables all outputs when HIGH. If left floating, internal noise causes unexpected dimming or flashing. Connect `BLANK` to MCU GPIO or pull LOW to GND.
- **Exceeding package thermal dissipation limit:** Operating 24 channels simultaneously at $30\text{ mA}$ with high voltage drop ($V_{DS} > 3\text{V}$) generates significant heat ($24 \times 0.03\text{A} \times 3\text{V} = 2.16\text{ W}$). Ensure the PowerPAD thermal pad is soldered to a large PCB ground plane.

## Notes

- **TLC5947 vs PCA9685:** TLC5947 has 24 channels, 12-bit PWM, and constant-current outputs (no series LED resistors needed); PCA9685 has 16 channels, 12-bit PWM, and voltage-driven open-drain outputs (requires external resistors).
