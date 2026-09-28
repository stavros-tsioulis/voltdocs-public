## Overview

The **DRV8871** (DRV8871DDA) is a high-voltage, high-current single brushed-DC motor driver integrated circuit developed by Texas Instruments. Packaged in an 8-pin PowerPAD HSOP (standard SOIC-8 dimensions with a bottom thermal pad) and widely adopted through maker breakout boards such as the Adafruit DRV8871 carrier, it is designed for robotics, automated window blinds, power tools, printers, and industrial actuators.

Operating over an expansive motor voltage range of **$6.5\text{ V}$ to $45.0\text{ V}$**, the DRV8871 can deliver up to **$3.6\text{ A}$ peak** or **$2.1\text{ A}$ continuous RMS** current. A standout feature of the device is its internal current sensing circuitry: an integrated current mirror eliminates the need for expensive, bulky high-power external shunt resistors. A single standard $0.125\text{W}$ resistor connected to the **`ILIM`** pin programs the maximum chopping current threshold ($I_{TRIP}$), safeguarding motors against stall overheating and limiting inrush currents.

## Quick reference

| | |
|---|---|
| **Driver Topology** | Single Full H-Bridge (N-Channel Power MOSFETs) |
| **Motor Supply Voltage ($V_M$)** | $6.5\text{ V}$ to $45.0\text{ V}$ DC ($50\text{ V}$ absolute max) |
| **Peak Output Current ($I_{PEAK}$)** | $3.6\text{ A}$ |
| **Continuous RMS Current ($I_{RMS}$)** | $2.1\text{ A}$ (at $25^\circ\text{C}$ with PCB thermal dissipation) |
| **Total MOSFET $R_{DS(ON)}$** | $565\text{ m}\Omega$ typical ($300\text{ m}\Omega$ HS + $265\text{ m}\Omega$ LS at $25^\circ\text{C}$) |
| **Current Limiting Resistor ($R_{ILIM}$)** | Adjustable via external resistor ($I_{TRIP} = 64000 / R_{ILIM}$) |
| **PWM Speed Modulation** | Supported up to $100\text{ kHz}$ on `IN1` and `IN2` |
| **Low-Power Sleep Mode** | Automatic sleep ($< 10\,\mu\text{A}$) when `IN1` and `IN2` are LOW for $> 1\text{ ms}$ |
| **Protection Circuitry** | Undervoltage Lockout (UVLO), Overcurrent Protection (OCP), Thermal Shutdown (TSD) |
| **Package Options** | 8-pin HSOP with PowerPAD (DDA, SOIC-8 size) |

## Pin configuration

### 8-Pin HSOP Package (DDA Top View)

```
              ┌─────────┐
         GND 1│ 1     8 │ OUT2 (Motor Output 2)
         IN2 2│         │ 7 PGND (Power Ground)
         IN1 3│ DRV8871 │ 6 OUT1 (Motor Output 1)
        ILIM 4│ (Thermal│ 5 VM (Motor Power)
              │   Pad)  │
              └─────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` | Power / Ground | Logic reference ground ($0\text{ V}$) |
| 2 | `IN2` | Digital Input | Control logic / PWM input 2 |
| 3 | `IN1` | Digital Input | Control logic / PWM input 1 |
| 4 | `ILIM` | Analog I/O | Current limit setting terminal; connect resistor $R_{ILIM}$ to `GND` |
| 5 | `VM` | Power Supply | Motor power supply input ($+6.5\text{ V}$ to $+45.0\text{ V}$) |
| 6 | `OUT1` | Power Output | Full-bridge output 1 |
| 7 | `PGND` | Power / Ground | High-current power ground return |
| 8 | `OUT2` | Power Output | Full-bridge output 2 |
| PAD | `PowerPAD` | Thermal Ground | Underside thermal ground pad; must be soldered to PCB copper plane |

## Functional description

### Function Truth Table

| `IN1` | `IN2` | `OUT1` | `OUT2` | Operating Mode |
|---|---|---|---|---|
| **`LOW`** | **`LOW`** | **`High-Z`** | **`High-Z`** | Coast / Standby (Enters low-power sleep $< 10\,\mu\text{A}$ after $1\text{ ms}$) |
| **`HIGH`** | **`LOW`** | **`HIGH`** | **`LOW`** | Forward drive (Current flows from OUT1 to OUT2) |
| **`LOW`** | **`HIGH`** | **`LOW`** | **`HIGH`** | Reverse drive (Current flows from OUT2 to OUT1) |
| **`HIGH`** | **`HIGH`** | **`LOW`** | **`LOW`** | Dynamic braking (Both low-side FETs ON; shorts motor terminals) |

- **Automatic Sleep State:** The DRV8871 does not require a dedicated sleep pin. Bringing both `IN1` and `IN2` LOW for more than $1\text{ ms}$ automatically drops the device into an ultra-low quiescent state ($I_{VM} < 10\,\mu\text{A}$). Pulsing either input HIGH restores full operation within $25\,\mu\text{s}$.
- **PWM Speed Modulation:** 
  - **Drive / Brake PWM (Recommended):** Apply PWM to one input while holding the other input HIGH. During the PWM OFF period, both outputs switch LOW (brake), offering tighter speed regulation and superior low-speed torque.
  - **Drive / Coast PWM:** Apply PWM to one input while holding the other input LOW. During the PWM OFF period, the outputs enter high impedance, allowing the motor to coast.

### Adjustable Current Regulation via ILIM

When current through the motor exceeds the programmed threshold $I_{TRIP}$, the DRV8871 automatically limits current by disabling the driving MOSFETs for a fixed off-time ($t_{OFF} \approx 25\,\mu\text{s}$) before switching back ON. The current trip threshold is calculated by:

$$I_{TRIP} = \frac{64000}{R_{ILIM}}$$

Where $R_{ILIM}$ is in ohms ($\Omega$) and $I_{TRIP}$ is in amperes ($\text{A}$).

| Desired $I_{TRIP}$ | Standard $R_{ILIM}$ Resistor | Notes |
|---|---|---|
| **$1.0\text{ A}$** | $64.9\text{ k}\Omega$ | Ideal for small $12\text{V}$ gearmotors |
| **$2.0\text{ A}$** | $32.4\text{ k}\Omega$ | General-purpose robotic drive |
| **$3.0\text{ A}$** | $21.5\text{ k}\Omega$ | High-torque actuators |
| **$3.6\text{ A}$** | $17.8\text{ k}\Omega$ (or tied directly to GND) | Maximum rated current threshold |

## Absolute maximum ratings

> [!WARNING]
> Stresses beyond these ratings cause permanent breakdown. Operating voltages near $45\text{V}$ require generous bulk capacitance to suppress inductive voltage spikes.

| Parameter | Symbol | Min | Max | Unit |
|---|---|---|---|---|
| Motor Supply Voltage | $V_M$ | $-0.3$ | $+50.0$ | V |
| Output Voltages (`OUT1`, `OUT2`) | $V_{OUT}$ | $-0.7$ | $V_M + 0.7$ | V |
| Logic Input Voltages (`IN1`, `IN2`) | $V_{IN}$ | $-0.3$ | $+5.5$ | V |
| Peak Output Current | $I_{OUT(PEAK)}$ | — | $3.6$ | A |
| Continuous Output Current | $I_{OUT(RMS)}$ | — | $2.1$ | A |
| Operating Ambient Temperature Range | $T_A$ | $-40$ | $+125$ | °C |
| Junction Temperature Range | $T_J$ | $-40$ | $+150$ | °C |
| Storage Temperature Range | $T_{stg}$ | $-65$ | $+150$ | °C |

## Electrical characteristics

($V_M = 24\text{ V}, T_A = 25^\circ\text{C}$ unless otherwise noted)

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Motor Supply Voltage | $V_M$ | 6.5 | — | 45.0 | V | Normal operation |
| Sleep Current | $I_{VM(SLEEP)}$ | — | 1.0 | 10.0 | µA | `IN1` = `IN2` = 0 for $> 1\text{ ms}$ |
| Quiescent Operating Current | $I_{VM}$ | — | 3.0 | 5.5 | mA | $f_{PWM} = 0\text{ Hz}$, no motor load |
| High-Side FET On-Resistance | $R_{DS(ON)H}$ | — | 300 | 400 | mΩ | $I_{OUT} = 1.0\text{ A}$ |
| Low-Side FET On-Resistance | $R_{DS(ON)L}$ | — | 265 | 350 | mΩ | $I_{OUT} = 1.0\text{ A}$ |
| Total Bridge On-Resistance | $R_{DS(ON)}$ | — | 565 | 750 | mΩ | Combined HS + LS |
| Logic High Input Voltage | $V_{IH}$ | 1.5 | — | — | V | Compatible with 1.8V, 3.3V, 5V logic |
| Logic Low Input Voltage | $V_{IL}$ | — | — | 0.5 | V | — |
| Fixed PWM Off-Time | $t_{OFF}$ | 16 | 25 | 34 | µs | In current regulation |
| Overcurrent Protection Limit | $I_{OCP}$ | 3.7 | 4.5 | 5.5 | A | Instantaneous bridge trip |
| Thermal Shutdown Temperature | $T_{TSD}$ | 150 | 175 | 190 | °C | Die junction temp |

## Typical application circuit

```
       +12V ... +36V Motor Power (VM)
       ────────────────────────┬───────────────────────────────────────────────┐
                               │                                               │
                             ┌─┴──┐ 47µF ... 100µF                          ┌──┴──┐
                             │    │ 50V Low-ESR                             │ 5   │ (VM)
                             └─┬──┘                                       ┌─┴─────┴─┐
                               │                                          │ DRV8871 │
       GND ────────────────────┴──────┬───────────────────────────────────┤ 1 (GND) │
                                      │                                   │ 7 (PGND)│
       Microcontroller                │                                   │         │
     ┌─────────────────┐              │                                   │ 6 (OUT1)├───[ BRUSHED DC ]───┐
     │        GPIO_IN1 ┼──────────────┼───────────────────────────────────┤ 3 (IN1) │       MOTOR        │
     │                 │              │                                   │         │                    │
     │        GPIO_IN2 ┼──────────────┼───────────────────────────────────┤ 2 (IN2) │ 8 (OUT2)───────────┘
     │                 │              │                                   │         │
     └─────────────────┘              │                                   │ 4 (ILIM)│
                                      │                                   └──┬──────┘
                                      │                                      │
                                      │                                     ┌┴┐ Rilim (30k for 2.1A limit)
                                      │                                     │ │ 1/8W
                                      │                                     └┬┘
                                      │                                      │
                                    ┌─┴─────────────┴────────────────────────┴───┐
                                    │               Power Ground                 │
                                    │                   GND                      │
                                    └────────────────────────────────────────────┘
```

## Design considerations & common mistakes

- **PowerPAD Soldering is Essential:** Continuous operation above $1.0\text{ A}$ requires efficient heat evacuation ($P \approx I^2 R = 2^2 \times 0.565 \approx 2.26\text{ W}$). Solder the underside PowerPAD directly to a large multi-layer copper ground plane with at least 6–8 thermal vias. Running the device without soldering the thermal pad will cause rapid thermal shutdown ($175^\circ\text{C}$).
- **Bulk Capacitance on VM:** Brushed DC motors generate significant inductive noise and flyback currents. Connect a $47\,\mu\text{F} \dots 100\,\mu\text{F}$ low-ESR electrolytic capacitor together with a $0.1\,\mu\text{F}$ ceramic capacitor immediately adjacent to pin 5 (`VM`) and pin 7 (`PGND`). Omitting bulk capacitance can cause supply voltage overshoot that exceeds the $50\text{ V}$ absolute maximum breakdown voltage.
- **Do Not Leave ILIM Open:** The `ILIM` pin must never be left floating. If `ILIM` is disconnected, current limit is undetermined, which can cause erratic chopping or failure to deliver current. Tie a $18\text{ k}\Omega \dots 200\text{ k}\Omega$ resistor from `ILIM` to ground, or connect `ILIM` directly to `GND` for maximum continuous drive.
- **PWM Frequency Selection:** The DRV8871 supports PWM frequencies up to $100\text{ kHz}$. Recommended frequencies are between $20\text{ kHz}$ and $50\text{ kHz}$ to eliminate audible motor whine while minimizing MOSFET switching losses.
