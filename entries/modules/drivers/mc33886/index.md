## Overview

The **MC33886** is a monolithic H-Bridge power IC manufactured by NXP Semiconductors (originally developed by Motorola / Freescale). Packaged in a 20-pin HSOP surface-mount package with an exposed bottom thermal heatsink slug, it is designed for controlling bidirectional DC motors, fractional horsepower actuators, and inductive loads at continuous currents up to **$5.0\text{ A}$** from supply voltages between **$5.0\text{ V}$ and $28.0\text{ V}$** (with transient survival up to $40.0\text{ V}$).

The IC integrates four low $R_{DS(on)}$ power MOSFET switches ($120\text{ m}\Omega$ per leg) and features internal charge pumps for continuous high-side gate drive (enabling $100\%$ duty cycle static ON operation). It incorporates internal current feedback (`FB`), open-drain fault status reporting (`FS`), undervoltage lockout, and thermal shutdown with hysteresis.

## Quick reference

| | |
|---|---|
| **Driver Type** | Monolithic H-Bridge DC Motor Driver IC |
| **Package** | HSOP-20 (Exposed Center Heat Slug) / Pololu Carrier |
| **Motor Supply Voltage ($V_{PWR}$)** | $5.0\text{ V}$ to $28.0\text{ V}$ DC (Operates up to $40.0\text{ V}$ transients) |
| **Continuous Load Current** | $5.0\text{ A}$ RMS continuous (with adequate heatsinking) |
| **Peak Current Limit** | $5.2\text{ A} \dots 7.8\text{ A}$ typical internal current limiting |
| **MOSFET On-Resistance ($R_{DS(ON)}$)** | $120\text{ m}\Omega$ typical per MOSFET ($240\text{ m}\Omega$ total bridge path) |
| **Maximum PWM Frequency** | $10\text{ kHz}$ recommended (internally slew-rate controlled) |
| **Logic Input Levels** | TTL / 5V CMOS compatible ($3.3\text{V}$ microcontroller compatible) |
| **Protection Features** | Overcurrent limiting, Thermal shutdown, Undervoltage lockout (UVLO), Fault status flag |

## Pinout (HSOP-20 Package)

```
         ┌──────────────┐
    AGND ─│ 1         20 │─ FB
    ~FS~ ─│ 2         19 │─ VPWR
     DNC ─│ 3   EP    18 │─ PGND
     IN1 ─│ 4 (Tab)   17 │─ PGND
     IN2 ─│ 5         16 │─ OUT2
      D1 ─│ 6         15 │─ OUT2
    ~D2~ ─│ 7         14 │─ PGND
     CCP ─│ 8         13 │─ PGND
    VPWR ─│ 9         12 │─ OUT1
    VPWR ─│ 10        11 │─ OUT1
         └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `AGND` | Analog low-noise signal ground reference |
| 2 | `~FS~` | Open-drain active-LOW fault status output (Pull up to MCU logic VCC) |
| 3 | `DNC` | Do Not Connect (Leave floating) |
| 4 | `IN1` | Logic control input 1 (TTL/CMOS compatible) |
| 5 | `IN2` | Logic control input 2 (TTL/CMOS compatible) |
| 6 | `D1` | Disable input 1 (Active-HIGH disable; internally pulled HIGH to disable) |
| 7 | `~D2~` | Disable input 2 (Active-LOW disable; internally pulled LOW to disable) |
| 8 | `CCP` | External charge pump capacitor pin (Connect 33nF to VPWR) |
| 9, 10 | `VPWR` | Main positive power supply input (+5.0V to +28.0V DC) |
| 11, 12 | `OUT1` | H-Bridge output 1 (Internally paralleled output pins) |
| 13, 14 | `PGND` | Power ground return for H-Bridge output stages |
| 15, 16 | `OUT2` | H-Bridge output 2 (Internally paralleled output pins) |
| 17, 18 | `PGND` | Power ground return for H-Bridge output stages |
| 19 | `VPWR` | Main positive power supply input |
| 20 | `FB` | Current feedback sense output (Provides current mirror output proportional to load current) |

## Control Logic Truth Table

To enable the H-bridge, `D1` must be held **LOW** and `~D2~` must be held **HIGH**:

| `D1` | `~D2~` | `IN1` | `IN2` | `OUT1` | `OUT2` | Operating Mode |
|---|---|---|---|---|---|---|
| High (`1`) | X | X | X | High-Z | High-Z | **Disabled / Coast** (Standby) |
| X | Low (`0`) | X | X | High-Z | High-Z | **Disabled / Coast** (Standby) |
| Low (`0`) | High (`1`) | Low (`0`) | Low (`0`) | Low | Low | **Brake to Ground** (Low-side recirculation) |
| Low (`0`) | High (`1`) | High (`1`) | Low (`0`) | High | Low | **Forward Drive** |
| Low (`0`) | High (`1`) | Low (`0`) | High (`1`) | Low | High | **Reverse Drive** |
| Low (`0`) | High (`1`) | High (`1`) | High (`1`) | High | High | **Brake to VPWR** (High-side recirculation) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Operating Supply Voltage | $V_{PWR}$ | 5.2 | 13.5 | 28.0 | V | Normal operation |
| Transient Voltage Rating | $V_{PWR(PK)}$ | — | — | 40.0 | V | $t < 500\text{ ms}$ |
| Continuous Output Current | $I_{OUT}$ | 5.0 | — | — | A | $T_J \le 125^\circ\text{C}$ with heatsink |
| Overcurrent Limiting Threshold | $I_{LIM}$ | 5.2 | 6.5 | 7.8 | A | $T_J = 25^\circ\text{C}$ |
| MOSFET On-Resistance ($R_{DS(on)}$) | $R_{ON}$ | — | 120 | 225 | $\text{m}\Omega$ | Per switch at $T_J = 25^\circ\text{C}, I_{OUT} = 3.0\text{A}$ |
| PWM Switching Frequency | $f_{PWM}$ | 0 | — | 10 | kHz | Continuous switching |
| Charge Pump Capacitor | $C_{CP}$ | — | 33 | — | nF | Ceramic connected from Pin 8 to VPWR |
| Thermal Shutdown Temp | $T_{SD}$ | 150 | 175 | 200 | °C | Junction temperature |

## Common mistakes

- **Leaving D1 and ~D2~ floating:** `D1` has an internal pull-up and `~D2~` has an internal pull-down. Leaving both unconnected permanently holds the H-bridge in its high-impedance disable state. Tie `D1` to `GND` and `~D2~` to `VCC` (or MCU GPIO HIGH) to enable.
- **Omitting the CCP charge pump capacitor:** Pin 8 (`CCP`) requires a $33\text{ nF}$ ($50\text{V}$) ceramic capacitor connected directly to `VPWR`. Without this capacitor, the internal high-side gate drive charge pump cannot operate, preventing continuous high-side conduction.
- **Exceeding 10 kHz PWM frequency:** The MC33886 has controlled output rise and fall times ($t_r \approx 1.5\ \mu\text{s}$) to reduce electromagnetic interference (EMI). Driving PWM frequencies above $10\text{ kHz} \dots 20\text{ kHz}$ dramatically increases switching losses and causes rapid thermal buildup.
- **Neglecting the exposed pad soldering:** The bottom slug is essential for heat extraction. Soldering the slug to a copper plane with thermal vias is mandatory for continuous loads exceeding $2\text{ A}$.

## Notes

- **Current Feedback (`FB` Pin):** Pin 20 outputs a current proportional to the total high-side load current (ratio $\approx 1/375$). Connecting a precision ground resistor (e.g. $1\text{ k}\Omega$) produces a $0\text{V} \dots 3.3\text{V}$ voltage readable by an MCU ADC for real-time torque and stall detection.
