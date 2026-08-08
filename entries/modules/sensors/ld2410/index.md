## Overview

The **LD2410** (along with variants LD2410B with Bluetooth and LD2410C with 2.0 mm connector) is a high-sensitivity 24 GHz Frequency-Modulated Continuous Wave (FMCW) radar human presence sensing module manufactured by Hi-Link. 

Unlike traditional PIR motion sensors that rely on thermal infrared movement and fail when a person sits still, the LD2410 transmits 24 GHz radio waves capable of penetrating plastic enclosures and detecting microscopic chest movements caused by human breathing. It divides its range into 8 distance gates (0.75 m resolution up to 6.0 m) and reports moving presence, static presence, and distance metrics via a 256,000 bps UART interface or a simple digital High/Low `OUT` pin. It is the leading presence sensor choice for Home Assistant and ESPHome smart home lighting systems.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 5.0 V to 12.0 V DC (5 V nominal) |
| **Operating frequency** | 24.00 GHz to 24.25 GHz (ISM band) |
| **Detection distance** | 0.75 m to 6.0 m (divided into 8 gate zones) |
| **Detection angle** | $\pm 60^\circ$ Azimuth / $\pm 60^\circ$ Elevation |
| **Interface** | UART (256,000 bps) & Digital GPIO Output (`OUT`) |
| **Logic level** | 3.3 V TTL logic on `TX`/`RX` and `OUT` |
| **Operating current** | 79 mA typical at 5.0 V |
| **Configuration tool** | HLKRadarTool mobile app (Bluetooth variant) or serial commands |

## Pinout

5-pin 0.1" (2.54 mm) connector header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply input (+5.0 V to +12.0 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `OUT` | Digital Output | High = Human presence detected, Low = No presence |
| 4 | `TX` | Digital Output | UART Transmit data pin (3.3V logic, default 256,000 bps) |
| 5 | `RX` | Digital Input | UART Receive command pin (3.3V logic) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 4.75 | 5.0 | 12.0 | V | DC supply |
| Operating Current | $I_{CC}$ | 70 | 79 | 120 | mA | Active radar transmission |
| Transmit Frequency | $f_{radar}$ | 24.00 | 24.125 | 24.25 | GHz | ISM ISM band |
| Max Detection Range | $D_{max}$ | 0.75 | 5.0 | 6.0 | m | Configurable per gate |
| Range Gate Resolution | $D_{gate}$ | — | 0.75 | — | m | 8 configurable distance gates |
| Detection Angle | $\theta$ | -60 | $\pm 60$ | +60 | ° | Conical radiation pattern |
| UART Baud Rate | $Baud$ | — | 256000 | — | bps | 8 data bits, 1 stop bit, no parity |
| Operating Temperature | $T_{opr}$ | -40 | — | 85 | °C | Ambient |

## UART Frame Structure & Protocol

The LD2410 streams binary status frames at 256,000 baud every 100 ms:

- **Header:** `F4 F3 F2 F1`
- **Data length & Command:** `0D 00 02 AA`
- **Target Status Byte:** `00` (No target), `01` (Moving target), `02` (Static target), `03` (Moving & Static targets).
- **Moving Target Distance:** 2 bytes (in cm).
- **Moving Target Energy:** 1 byte (0–100%).
- **Static Target Distance:** 2 bytes (in cm).
- **Static Target Energy:** 1 byte (0–100%).
- **Detection Distance:** 2 bytes (in cm).
- **Footer:** `F8 F7 F6 F5`

## Sensitivity Calibration per Gate

The LD2410 allows setting motion and static sensitivity thresholds (0–100) independently for each of the 8 distance gates (Gate 0 = $0–0.75\text{ m}$, Gate 1 = $0.75–1.5\text{ m}$, up to Gate 7 = $5.25–6.0\text{ m}$). Lowering sensitivity on distant gates prevents false triggers caused by ceiling fans, swaying curtains, or air conditioners.

## Wiring

| LD2410 Pin | → | ESP32 | Arduino (Hardware Serial) | Notes |
|---|---|---|---|---|
| `VCC` | | 5V | 5V | Requires 5V power supply |
| `GND` | | GND | GND | System ground |
| `OUT` | | GPIO 15 | Digital Pin D2 | Simple binary presence pin |
| `TX` | | GPIO 16 (RX2) | Hardware RX (Serial1) | 3.3V logic output |
| `RX` | | GPIO 17 (TX2) | Hardware TX (Serial1) | 3.3V logic input |

> [!WARNING]
> High baud rate requirement:
> - The default UART baud rate is **256,000 bps**. Standard 8-bit Arduino microcontrollers using SoftwareSerial **cannot reliably receive 256,000 baud**.
> - Always connect `TX`/`RX` to a 32-bit MCU with hardware UART peripherals (such as ESP32, ESP8266, or STM32) or rely strictly on the binary `OUT` pin.

## Example (ESPHome Configuration)

```yaml
uart:
  id: uart_bus
  tx_pin: GPIO17
  rx_pin: GPIO16
  baud_rate: 256000

ld2410:
  id: my_ld2410

binary_sensor:
  - platform: ld2410
    has_target:
      name: "Human Presence Detected"
    has_moving_target:
      name: "Moving Target Detected"
    has_still_target:
      name: "Static Target Detected"

sensor:
  - platform: ld2410
    moving_target_distance:
      name: "Moving Target Distance"
    still_target_distance:
      name: "Static Target Distance"
```

## Common mistakes

- **Attempting to use SoftwareSerial at 256,000 baud:** Causes garbage bytes and continuous packet parsing failures.
- **Powering from weak 3.3V rails:** The LD2410 requires a stable 5.0V supply rail and draws up to 120 mA during active radar bursts.
- **False triggers from metallic objects:** Placing the radar probe directly facing metal surfaces or mirrors causes multipath microwave reflections.
- **Vibrating mounting surface:** Mounting the radar on a flimsy partition wall that vibrates when doors close triggers false motion detection.

## Notes

- **LD2410 vs PIR:** PIR sensors cannot detect stationary seated people; the LD2410 continuously detects stationary breathing targets without needing movement.
