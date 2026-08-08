## Overview

The **AM312** (also sold as the MB-102 or Senba AM312) is an ultra-miniature passive infrared (PIR) motion detection module engineered for low-power, battery-operated IoT sensors. Measuring just **$13\text{ mm} \times 10\text{ mm}$**, it integrates a dual-element pyroelectric sensor and a digital signal processing (DSP) ASIC underneath a tiny white dome Fresnel lens.

Consuming a standby current of just **$15\ \mu\text{A}$** and supporting a wide input voltage range (**$2.7\text{V}$ to $12.0\text{V}$ DC**), the AM312 is the preferred motion sensor for battery-powered ESP32/ESP8266 ESPHome nodes, Home Assistant motion sensors, and Zigbee/LoRa occupancy detectors.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 2.7 V to 12.0 V DC (3.3V or 5V nominal) |
| **Standby current** | $15\ \mu\text{A}$ typical |
| **Detection distance** | 3.0 to 5.0 meters ($10\text{ to }16\text{ feet}$) |
| **Detection angle** | $<100^\circ$ cone |
| **Output logic level** | 3.3V Active-High ($3.3\text{V}$ when motion detected, $0\text{V}$ idle) |
| **Delay time ($t_{delay}$)** | ~2.3 seconds fixed automatic pulse width |
| **Block time ($t_{block}$)** | ~2.0 seconds non-repeatable re-trigger block time |
| **Dimensions** | $13\text{ mm} \times 10\text{ mm}$ PCB ($12\text{ mm}$ lens diameter) |

## Pinout

3-pin 0.1" (2.54 mm) connector header:

```
        ┌───────────────────┐
        │  [Mini Dome Lens] │
        └─┬───────┬───────┬─┘
         VCC     OUT     GND
          1       2       3
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Power supply input (+2.7 V to +12.0 V DC) |
| 2 | `OUT` | Digital Output | Active-High digital output (3.3V logic HIGH during motion) |
| 3 | `GND` | Power | Ground reference (0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.7 | 3.3 / 5.0 | 12.0 | V | DC |
| Standby Current | $I_{standby}$| — | 15 | 20 | µA | $V_{CC} = 3.3\text{ V}$, idle |
| High Output Voltage | $V_{OH}$ | 3.0 | 3.3 | 3.6 | V | Motion detected |
| Low Output Voltage | $V_{OL}$ | 0.0 | 0.0 | 0.2 | V | No motion |
| Motion Hold Delay | $t_{delay}$ | 2.0 | 2.3 | 2.8 | s | Fixed internal timer |
| Re-trigger Block Time | $t_{block}$ | 1.5 | 2.0 | 2.5 | s | Sensor reset lockout period |
| Operating Temperature | $T_{opr}$ | -20 | — | 80 | °C | Ambient air |

## Signal Timing Diagram

```
 Motion Event:      [ Human Passes Sensor ]
 OUT (Pin 2):   ────┐                     ┌────────────────────
                    │<──── 2.3 sec ──────>│
                    └─────────────────────┘
```

1. **Idle State:** Pin 2 (`OUT`) sits at 0V ($15\ \mu\text{A}$ standby draw).
2. **Motion Trigger:** When a thermal IR body ($9.4\ \mu\text{m}$ wavelength) moves across the Fresnel zones, `OUT` goes **High (3.3V)** for ~2.3 seconds.
3. **Block Period:** After returning to 0V, the module blocks new triggers for ~2.0 seconds to allow pyroelectric elements to thermally re-stabilize.

## Wiring

| AM312 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Works down to 2.7V (battery direct) |
| `OUT` | | Digital D2 (INT0) | GPIO 4 | Direct 3.3V logic output |
| `GND` | | GND | GND | System ground |

## Example (ESPHome Motion Sensor)

```yaml
binary_sensor:
  - platform: gpio
    pin:
      number: GPIO4
      mode: INPUT_PULLDOWN
    name: "Living Room Motion Detector"
    device_class: motion
```

## Common mistakes

- **Misidentifying pinout order:** Looking at the rear PCB with header pins pointing down: Pin 1 (Left) = `VCC`, Pin 2 (Center) = `OUT`, Pin 3 (Right) = `GND`. Connecting `VCC` to `GND` damages the internal ASIC.
- **Expecting continuous high output during static presence:** Like all PIR sensors, the AM312 detects **change in thermal IR position**. Sitting completely motionless causes `OUT` to return to 0V after 2.3 seconds.

## Notes

- **AM312 vs HC-SR501:** AM312 is $10\times$ smaller, draws $15\ \mu\text{A}$ (vs $50\ \mu\text{A}$), operates down to 2.7V, and eliminates bulky potentiometers.
