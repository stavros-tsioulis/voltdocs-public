## Overview

The **VS1838B** (and equivalent HX1838 / TSOP1838) is a miniaturized 38 kHz infrared receiver module used for IR remote control command decoding in electronics kits (Elegoo, SunFounder) and consumer appliances.

It integrates a PIN photodiode, high-gain preamplifier, automatic gain control (AGC), bandpass filter tuned to **38 kHz**, and a demodulator inside a metal-shielded package. When it detects a 38 kHz modulated IR light signal from a remote, it strips away the 38 kHz carrier frequency and outputs clean **active-LOW digital logic pulses** directly to a microcontroller pin.

## Quick reference

| | |
|---|---|
| **Operating Voltage (`VCC`)** | 2.7 V to 5.5 V DC (5.0 V nominal) |
| **Carrier Frequency** | 38.0 kHz (standard consumer IR remote frequency) |
| **Peak Wavelength** | 940 nm (Infrared spectrum) |
| **Reception Range** | 15 m to 18 m |
| **Angle of Directivity** | $\pm 45^\circ$ ($90^\circ$ half-power cone) |
| **Output State** | Idle: `HIGH` (3.3V/5V); Active 38kHz IR burst: `LOW` (0V) |
| **Quiescent Current** | 0.5 mA to 1.5 mA |

## Pinout

### Standard Metal-Shielded Component Pins (Facing front bubble, pins down)

```
        ┌─────────┐
        │ [VS1838]│  (Front lens bubble facing you)
        └─────────┘
          │  │  │
          1  2  3
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `OUT` / `DAT` | Digital Output | Demodulated digital output (Active-LOW, connects to MCU GPIO) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `VCC` | Power | Supply voltage (+2.7 V to +5.5 V DC) |

> [!NOTE]
> Pinout Warning for KY-022 Breakout PCBs:
> On some 3-pin KY-022 PCB modules, the pin order on the header connector from left to right is **`DAT` - `VCC` - `GND`** or **`GND` - `VCC` - `DAT`**. Always check PCB silk markings!

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{S}$ | 2.7 | 5.0 | 5.5 | V | DC |
| Supply Current | $I_{S}$ | 0.4 | 0.6 | 1.5 | mA | No IR signal |
| Carrier Frequency | $f_{0}$ | — | 38.0 | — | kHz | Center frequency |
| Low Output Voltage | $V_{OL}$ | — | 0.2 | 0.4 | V | During 38 kHz IR burst ($I_{OSL} = 0.5\text{ mA}$) |
| High Output Voltage | $V_{OH}$ | $V_{S}-0.5$ | — | $V_{S}$ | V | Idle / No IR signal |
| Minimum Burst Length | $t_{burst}$ | 10 | — | — | cycles | 10 cycles of 38 kHz ($\approx 260\text{ }\mu\text{s}$) |

## IR Protocol Demodulation (NEC Protocol Example)

The VS1838B automatically strips the 38 kHz carrier wave from incoming remote signals:

```
Sender (38kHz IR LED Burst) ───█████─────────█████───────
                                │             │
VS1838B Output (OUT Pin)   ───┐ │ ┌─────────┐ │ ┌─────────
                              └─┘ └─────────┘ └─┘
                             (Active-LOW Pulse Payload)
```

- **NEC Protocol Start Frame:** 9 ms continuous 38 kHz burst (`LOW` pulse) followed by a 4.5 ms space (`HIGH`).
- **Bit 0:** 562.5 µs burst followed by 562.5 µs space ($1.125\text{ ms}$ total).
- **Bit 1:** 562.5 µs burst followed by 1.6875 ms space ($2.25\text{ ms}$ total).

## Wiring

| VS1838B Component Pin | → | Microcontroller (Arduino Uno / ESP32) |
|---|---|---|
| 1 (`OUT`) | | Digital Input Pin with Interrupts (e.g. D11 / GPIO15) |
| 2 (`GND`) | | `GND` |
| 3 (`VCC`) | | `5V` (or `3.3V`) |

## Common mistakes

- **Reversing VCC and GND:** Connecting power in reverse heats up the internal IC and destroys the photodiode preamplifier.
- **Interference from compact fluorescent lights (CFL) / Sunlight:** Direct sunlight or electronic ballast fluorescent lamps emit strong 38 kHz modulated infrared noise. Keep the sensor shielded from direct sunlight.
- **Forgetting Active-LOW logic:** The `OUT` pin stays `HIGH` at rest and pulses `LOW` during IR signals. Hardware interrupt triggers should use `FALLING` or `CHANGE` edge detection.

## Notes

- Compatible with standard open-source libraries such as `IRremote` (Arduino) and ESPHome `remote_receiver` component.
