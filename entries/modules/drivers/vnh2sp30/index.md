## Overview

The **VNH2SP30** (VNH2SP30-E) is an automotive-grade, monolithic full-bridge DC motor driver IC manufactured by STMicroelectronics. Packaged in a specialized **MultiPowerSO-30** power package with dual high-side and low-side power MOSFET stages, it is famed in robotics for powering the widely used **SparkFun Monster Moto Shield** and dual-motor robotics platforms.

Designed to drive automotive actuators and heavy DC motors from a nominal **$5.5\text{ V}$ to $16.0\text{ V}$ supply** (with transient survival up to $41\text{ V}$ load dump), it provides up to **$30\text{ A}$ peak stall current** ($14\text{ A}$ continuous with heatsinking) with a low combined total on-resistance of **$34\text{ m}\Omega$**. It includes linear current sense feedback (`CS`), dual diagnostic status outputs (`ENA/DIAGA`, `ENB/DIAGB`), overtemperature shutdown, undervoltage/overvoltage protection, and PWM speed control up to **$20\text{ kHz}$**.

## Quick reference

| | |
|---|---|
| **Driver Type** | Full-Bridge Automotive DC Motor Driver IC |
| **Package** | MultiPowerSO-30 / Monster Moto Shield / Pololu Carrier |
| **Operating Voltage ($V_{CC}$)** | $5.5\text{ V}$ to $16.0\text{ V}$ DC (Load dump protected up to $41\text{V}$) |
| **Peak Current Limit** | $30.0\text{ A}$ minimum (typically $45.0\text{ A}$ trip) |
| **Continuous Current Rating** | $14.0\text{ A}$ continuous (with adequate heatsink) |
| **Total Bridge On-Resistance ($R_{ON}$)** | $34\text{ m}\Omega$ typical ($18\text{ m}\Omega$ high-side + $16\text{ m}\Omega$ low-side) |
| **PWM Switching Frequency** | Up to $20\text{ kHz}$ (DC to 20 kHz) |
| **Logic Supply ($V_{DD}$)** | $5.0\text{ V}$ compatible ($3.3\text{V}$ logic compatible inputs) |
| **Diagnostics & Sensing** | Real-time current sensing proportional output (`CS`) + Dual Diagnostic flags |

## MultiPowerSO-30 Pin Configuration

```
         ┌──────────────────┐
    OUTA ─│ 1             30 │─ OUTB
    OUTA ─│ 2             29 │─ OUTB
     VCC ─│ 3             28 │─ VCC
    INA  ─│ 4     TAB     27 │─ INB
   ENA/  ─│ 5    (GND)    26 │─ ENB/
   DIAGA  │                  │  DIAGB
     PWM ─│ 6             25 │─ CS
     GND ─│ 7             24 │─ GND
         └──────────────────┘
   (Additional pins connect to internal power legs & heat slug)
```

| Pin | Name | Description |
|---|---|---|
| 1, 2 | `OUTA` | H-Bridge Motor Output A |
| 3, 28 | `VCC` | Main battery/motor power supply input (+5.5V to +16.0V DC) |
| 4 | `INA` | Direction control logic input for Leg A |
| 5 | `ENA/DIAGA` | Leg A Enable input and open-drain Diagnostic Output |
| 6 | `PWM` | Logic PWM input for motor speed regulation (Active-HIGH) |
| 7, 24 | `GND` | Ground return for logic and power stages (connected to exposed Tab) |
| 25 | `CS` | Analog current sense output (Generates current proportional to motor load) |
| 26 | `ENB/DIAGB` | Leg B Enable input and open-drain Diagnostic Output |
| 27 | `INB` | Direction control logic input for Leg B |
| 29, 30 | `OUTB` | H-Bridge Motor Output B |

## Control Logic Truth Table

To operate the motor, both `ENA/DIAGA` and `ENB/DIAGB` must be held **HIGH**:

| `INA` | `INB` | `ENA/DIAGA` | `ENB/DIAGB` | `PWM` | `OUTA` | `OUTB` | Motor State |
|---|---|---|---|---|---|---|---|
| `1` | `0` | `1` | `1` | `1` | High | Low | **Clockwise (CW / Forward)** |
| `1` | `0` | `1` | `1` | `0` | Low | Low | **Brake to Ground (Slow decay during PWM)** |
| `0` | `1` | `1` | `1` | `1` | Low | High | **Counter-Clockwise (CCW / Reverse)** |
| `0` | `1` | `1` | `1` | `0` | Low | Low | **Brake to Ground (Slow decay during PWM)** |
| `0` | `0` | `1` | `1` | X | Low | Low | **Brake to Ground** |
| `1` | `1` | `1` | `1` | X | High | High | **Brake to VCC** |
| X | X | `0` | X | X | High-Z | High-Z | **Disabled / Coast (High-Z)** |
| X | X | X | `0` | X | High-Z | High-Z | **Disabled / Coast (High-Z)** |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Motor Supply Voltage | $V_{CC}$ | 5.5 | 13.5 | 16.0 | V | Operating range |
| Undervoltage Shutdown | $V_{USD}$ | — | 4.5 | 5.5 | V | $V_{CC}$ falling |
| Overvoltage Shutdown | $V_{OV}$ | 16.0 | 19.0 | 22.0 | V | $V_{CC}$ rising |
| Continuous Output Current | $I_{OUT}$ | — | 14.0 | — | A | $T_C = 85^\circ\text{C}$ with heatsink |
| Current Limit Trip Threshold | $I_{LIM}$ | 30.0 | 45.0 | — | A | Short-circuit trip |
| High-Side On-Resistance | $R_{ON(HS)}$ | — | 18.0 | 34.0 | $\text{m}\Omega$ | $I_{OUT} = 12\text{A}, T_J = 25^\circ\text{C}$ |
| Low-Side On-Resistance | $R_{ON(LS)}$ | — | 16.0 | 30.0 | $\text{m}\Omega$ | $I_{OUT} = 12\text{A}, T_J = 25^\circ\text{C}$ |
| Current Sense Ratio ($I_{OUT} / I_{CS}$)| $K$ | — | 11300 | — | — | $I_{OUT} = 5\text{A} \dots 15\text{A}$ |
| Thermal Shutdown Temp | $T_{TSD}$ | 150 | 175 | 200 | °C | Junction temperature |

## Common mistakes

- **Leaving ENA/DIAGA or ENB/DIAGB low or floating:** These pins are bidirectional enable/diagnostic pins. They must be actively pulled HIGH (via MCU output or a $10\text{ k}\Omega$ pull-up resistor to $5\text{V}$) for the bridge to enable. If a thermal or electrical fault occurs, the internal pull-down will drag the pin LOW.
- **Exceeding 16V operating supply:** Unlike 24V-rated drivers (like BTS7960), the VNH2SP30 has an overvoltage shutdown mechanism that triggers at $\approx 19\text{V}$. Operating from an unregulated 4S LiPo battery (16.8V max) can trigger overvoltage shutdown. It is strictly optimized for 12V automotive and 3S LiPo battery systems.
- **Inadequate heatsinking at loads $> 6\text{A}$:** While capable of handling 30A in short bursts, sustained loads without a dedicated aluminum heatsink on the exposed thermal pad will cause thermal throttling within seconds.

## Notes

- **Current Sensing Formula:** Pin 25 (`CS`) outputs a current $I_{CS} = I_{OUT} / 11300$. Placing a $1.5\text{ k}\Omega$ resistor between `CS` and `GND` generates:
  $$ V_{CS} = I_{OUT} \times \frac{1500}{11300} \approx 0.133\text{ V per Ampere} $$
  allowing an Arduino ADC to directly measure motor stall current.
