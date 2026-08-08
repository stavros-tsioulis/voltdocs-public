## Overview

The **SPS30** is an industrial-grade optical particulate matter (PM) sensor manufactured by Sensirion. Engineered for HVAC systems, air purifiers, and professional environmental monitoring stations, it measures mass concentration ($\mu\text{g/m}^3$) and number concentration ($\text{particles/cm}^3$) across four distinct size bins: **PM1.0, PM2.5, PM4.0, and PM10.0**.

Featuring Sensirion's patented **contamination-resistant technology** and an **automatic fan self-cleaning routine** (which spins the fan at maximum speed periodically to blow out accumulated dust), the SPS30 achieves an operational lifetime exceeding **10 years**. It supports both **$I^2C$ (`0x69`)** and **TTL UART (115,200 bps)** interface modes.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VDD`)** | 4.5 V to 5.5 V DC (5.0 V nominal) |
| **Interfaces** | $I^2C$ (Default address `0x69`) & TTL UART (115,200 bps) |
| **Mass Concentration bins** | PM1.0, PM2.5, PM4.0, PM10.0 ($0\text{ to }1000\ \mu\text{g/m}^3$) |
| **Number Concentration bins**| PM0.5, PM1.0, PM2.5, PM4.0, PM10.0 ($\text{particles/cm}^3$) |
| **Mass Accuracy (PM2.5)** | $\pm 10\ \mu\text{g/m}^3$ ($0\dots 100\ \mu\text{g/m}^3$) / $\pm 10\%$ ($100\dots 1000\ \mu\text{g/m}^3$) |
| **Particle Size Limit** | Minimum detectable particle size $0.3\ \mu\text{m}$ |
| **Lifetime** | $>10\text{ years}$ continuous 24/7 operation |
| **Self-Cleaning** | Automatic programmable fan cleaning cycle (default once every 7 days) |
| **Operating current** | $55\text{ mA}$ measurement active / $50\ \mu\text{A}$ sleep |

## Pinout (5-Pin JST-ZH 1.5mm Pitch Connector)

```
        ┌─────────────────────────┐
        │  [Sensirion SPS30 Module]│
        └─┬───┬───┬───┬───────────┘
          1   2   3   4   5
         VDD RX  TX  SEL GND
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VDD` | Power | Supply power input (+4.5 V to +5.5 V DC) |
| 2 | `SDA` / `RX` | Digital Input / Output | $I^2C$ Serial Data / UART Receive |
| 3 | `SCL` / `TX` | Digital Input / Output | $I^2C$ Serial Clock / UART Transmit |
| 4 | `SEL` | Digital Input | Interface Select pin (**GND = $I^2C$ mode**, Floating/High = UART mode) |
| 5 | `GND` | Power | Ground reference (0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 4.5 | 5.0 | 5.5 | V | DC |
| Supply Current (Active) | $I_{active}$| — | 55 | 80 | mA | Fan & laser active |
| Supply Current (Sleep) | $I_{sleep}$ | — | 50 | — | µA | Sleep mode |
| Mass Concentration Range| $Range_{PM}$| 0 | — | 1000 | µg/m³ | PM1.0, PM2.5, PM4, PM10 |
| Lower Particle Limit | $Size_{min}$| — | 0.3 | — | µm | Laser scattering threshold |
| Fan Cleaning Duration | $t_{clean}$ | — | 10 | — | s | Max speed fan blow-out |
| Operating Temperature | $T_{opr}$ | -10 | — | 60 | °C | Ambient air |

## $I^2C$ vs UART Interface Selection

- **$I^2C$ Mode (`0x69`):** Connect Pin 4 (`SEL`) to **`GND`**. Use $I^2C$ Clock on Pin 3 (`SCL`) and $I^2C$ Data on Pin 2 (`SDA`).
- **UART Mode (115,200 bps):** Leave Pin 4 (`SEL`) **unconnected (Floating)**. Connect Pin 3 (`TX`) to MCU RX, and Pin 2 (`RX`) to MCU TX.

## Wiring ($I^2C$ Mode)

| SPS30 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| 1 (`VDD`) | | 5V | 5V | **Requires 5.0V supply** |
| 2 (`SDA`) | | A4 | GPIO 21 | $I^2C$ Data |
| 3 (`SCL`) | | A5 | GPIO 22 | $I^2C$ Clock |
| 4 (`SEL`) | | GND | GND | **Tie to GND for $I^2C$ mode** |
| 5 (`GND`) | | GND | GND | System ground |

## Example (ESPHome Configuration)

```yaml
sps30:
  id: sps30_sensor
  i2c_id: i2c_bus
  address: 0x69
  auto_cleaning_interval: 86400s # Clean fan once every 24 hours

sensor:
  - platform: sps30
    pm_1_0:
      name: "SPS30 PM1.0"
    pm_2_5:
      name: "SPS30 PM2.5"
    pm_4_0:
      name: "SPS30 PM4.0"
    pm_10_0:
      name: "SPS30 PM10.0"
```

## Common mistakes

- **Leaving `SEL` floating in $I^2C$ mode:** Pin 4 (`SEL`) must be pulled Low to `GND` at boot time to select $I^2C$ mode; floating `SEL` defaults the module to UART mode.
- **Powering with 3.3V:** The SPS30 laser diode and internal fan require a regulated **$5.0\text{V}$ supply**. Supplying 3.3V causes communication failures.

## Notes

- **SPS30 vs PMS5003 vs SDS011:** SPS30 provides 4 PM mass binnings (adds PM4.0), includes hardware fan self-cleaning for a 10-year lifespan, and supports both $I^2C$ and UART natively.
