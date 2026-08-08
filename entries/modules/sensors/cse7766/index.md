## Overview

The **CSE7766** is a single-phase electricity metering IC manufactured by China Silergy (CSE). Embedded inside popular commercial Wi-Fi smart plugs—most notably the **Sonoff S31** and **Sonoff POW R2**—it measures RMS AC voltage, RMS AC current, active power (W), and cumulative energy consumption.

Selected by manufacturers as the successor to pulse-counting ICs like the HLW8012, the CSE7766 offloads pulse-timing calculations from the microcontroller. It streams pre-calculated 24-byte telemetry data frames continuously over a **4,800 baud TTL UART interface**. It is natively supported in **Tasmota**, **ESPHome**, and **Home Assistant**.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VDD`)** | 4.5 V to 5.5 V DC (5.0 V nominal) |
| **Interface** | TTL UART (4,800 bps, 8-E-1: 8 data bits, Even parity, 1 stop bit) |
| **Baud rate** | Fixed 4,800 bps |
| **Measurement parameters** | $V_{RMS}$, $I_{RMS}$, Active Power ($P$), Energy Accumulator ($E$) |
| **Telemetry frame frequency** | Automatically streams 1 frame every ~1.0 second |
| **Measurement accuracy** | Class 0.5 ($\pm 0.5\%$) |
| **Operating current** | $3.5\text{ mA}$ typical |

## Pinout (SOP-8 Package)

```
             ┌───┴───┐
          VDD ─┤ 1    8├─ GND
          V1P ─┤ 2    7├─ NC
          V1N ─┤ 3    6├─ RX
           V2P ─┤ 4    5├─ TX
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VDD` | Power | Core supply (+4.5 V to +5.5 V DC) |
| 2 | `V1P` | Analog Input | Positive current sense input (from $1\ \text{m}\Omega$ shunt) |
| 3 | `V1N` | Analog Input | Negative current sense input |
| 4 | `V2P` | Analog Input | Voltage sense input (from resistor divider; $V_{2N}$ connected to GND) |
| 5 | `TX` | Digital Output | UART Transmit output pin (4,800 bps) |
| 6 | `RX` | Digital Input | UART Receive input pin |
| 8 | `GND` | Power | Ground reference (0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 4.5 | 5.0 | 5.5 | V | DC |
| Supply Current | $I_{DD}$ | — | 3.5 | 5.0 | mA | Active operation |
| Current Channel Input Range| $V_{V1P-V1N}$| -43.7 | — | +43.7 | mV Peak | Differential shunt voltage |
| Voltage Channel Input Range| $V_{V2P}$ | -43.7 | — | +43.7 | mV Peak | Single-ended voltage |
| Measurement Accuracy | $E_{meter}$ | -0.5% | $\pm 0.1\%$| +0.5%| — | Active power range 1000:1 |
| Internal Voltage Ref | $V_{REF}$ | 1.20 | 1.25 | 1.30 | V | Low temperature coefficient |

## Telemetry Frame Structure

The CSE7766 streams 24-byte binary frames every second over 4,800 baud serial (8-E-1):

- **Header Bytes (0–1):** `0x55 0x5A` (or `0x5A 0x5A`).
- **Voltage Coefficients & Data (Bytes 2–7):** 24-bit Voltage coefficient ($K_V$) and 24-bit Voltage cycle count ($T_V$).
- **Current Coefficients & Data (Bytes 8–13):** 24-bit Current coefficient ($K_I$) and 24-bit Current cycle count ($T_I$).
- **Power Coefficients & Data (Bytes 14–19):** 24-bit Power coefficient ($K_P$) and 24-bit Power cycle count ($T_P$).
- **Status & Pulse Count (Bytes 20–22):** Error flags and cumulative energy pulse counter.
- **Checksum Byte (23):** 8-bit sum of bytes 2 through 22.

$$ V_{RMS}\text{ (V)} = \frac{K_V}{T_V} \quad \text{Volts} $$

$$ I_{RMS}\text{ (A)} = \frac{K_I}{T_I} \quad \text{Amperes} $$

$$ P\text{ (W)} = \frac{K_P}{T_P} \quad \text{Watts} $$

## Wiring (Sonoff S31 / POW R2 Internal PCB)

| CSE7766 Pin | → | ESP8266 / ESP32 GPIO | Notes |
|---|---|---|---|
| `VDD` | | 3.3V / 5V | Power rail |
| `GND` | | GND | Common ground (tied to Neutral AC mains) |
| `TX`  | | MCU RX Pin (GPIO 3 or 13) | **4800 baud 8-E-1** |
| `RX`  | | MCU TX Pin (GPIO 1) | Command input |

> [!WARNING]
> High Voltage Safety Warning:
> - The CSE7766 `GND` pin is connected directly to AC Neutral. Connecting a serial programmer to the UART pins while the smart plug is plugged into mains power will blow computer USB ports and cause electric shock. **Program/debug smart plugs ONLY while unplugged from 120V/230V AC wall outlets.**

## Example (ESPHome Configuration)

```yaml
uart:
  rx_pin: GPIO13
  baud_rate: 4800
  parity: EVEN

sensor:
  - platform: cse7766
    voltage:
      name: "Sonoff S31 Voltage"
    current:
      name: "Sonoff S31 Current"
    power:
      name: "Sonoff S31 Power"
    energy:
      name: "Sonoff S31 Energy"
```

## Common mistakes

- **Setting incorrect serial parity:** The CSE7766 uses **Even parity (`8-E-1`)**, not standard No-parity (`8-N-1`). Setting `NONE` parity results in frame checksum validation failures.
- **Using 9600 or 115200 baud:** The CSE7766 UART clock is fixed at **4800 baud**.

## Notes

- **CSE7766 vs HLW8012:** CSE7766 sends pre-calculated telemetry over UART (8-E-1); HLW8012 outputs variable frequency pulse trains (`CF`/`CF1`).
