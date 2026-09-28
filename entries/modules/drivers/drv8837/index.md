## Overview

The **DRV8837** (DRV8837DSG) is an ultra-compact single H-bridge brushed DC motor driver IC manufactured by Texas Instruments, popular in miniature robotics, electronic battery locks, motorized toys, hand-held medical instruments, and consumer electronics. Housed in a microscopic $2\text{mm} \times 2\text{mm}$ 8-pin WSON package (and accessible to makers via the Pololu DRV8837 carrier breakout), it provides a modern, high-efficiency alternative to legacy bipolar drivers like the L293D and L298N.

The device operates with a motor supply voltage ($V_M$) ranging from **$1.8\text{ V}$ to $11.0\text{ V}$**, making it ideal for systems powered by 1-cell or 2-cell Li-ion batteries ($3.7\text{V} \dots 7.4\text{V}$) or $2\times$ to $4\times$ AA/AAA alkaline packs. Featuring an exceptionally low combined MOSFET on-resistance of only **$280\text{ m}\Omega$**, it can supply up to **$1.8\text{ A}$ peak** ($1.0\text{ A}$ continuous RMS) while dissipating negligible heat. Crucially for battery longevity, its sleep mode draws a miniscule **$120\text{ nA}$** typical standby current.

## Quick reference

| | |
|---|---|
| **Driver Topology** | Single Low-Voltage Full H-Bridge (N-Channel MOSFETs) |
| **Motor Supply Voltage ($V_M$)** | $1.8\text{ V}$ to $11.0\text{ V}$ DC ($0\text{ V} \dots 11\text{ V}$ absolute) |
| **Logic Supply Voltage ($V_{CC}$)** | $1.8\text{ V}$ to $7.0\text{ V}$ DC (Compatible with 1.8V, 3.3V, 5V logic) |
| **Peak Output Current ($I_{PEAK}$)** | $1.8\text{ A}$ |
| **Continuous RMS Current ($I_{RMS}$)** | $1.0\text{ A}$ (with adequate PCB thermal ground plane) |
| **Total MOSFET $R_{DS(ON)}$** | $280\text{ m}\Omega$ typical ($140\text{ m}\Omega$ HS + $140\text{ m}\Omega$ LS at $25^\circ\text{C}$) |
| **Sleep Mode Current ($I_{Q(SLEEP)}$)** | $120\text{ nA}$ typical ($35\text{ nA}$ max on $V_M$, $1.0\,\mu\text{A}$ max on $V_{CC}$) |
| **Control Interface** | Dual PWM inputs (`IN1`, `IN2`) with forward, reverse, brake, coast |
| **Protection Circuitry** | Undervoltage Lockout (UVLO), Overcurrent Protection (OCP), Thermal Shutdown (TSD) |
| **Package Options** | 8-pin WSON ($2.0\text{mm} \times 2.0\text{mm}$ DSG) with PowerPAD |

## Pin configuration

### 8-Pin WSON Package (Top View)

```
              ┌─────────┐
          VM 1│ 1     8 │ VCC (Logic Power)
        OUT1 2│         │ 7 ~nSLEEP~ (Active-Low Sleep)
        OUT2 3│ DRV8837 │ 6 IN1 (Direction / PWM 1)
         GND 4│ (Thermal│ 5 IN2 (Direction / PWM 2)
              │   Pad)  │
              └─────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VM` | Power Supply | Motor power supply input ($+1.8\text{ V}$ to $+11.0\text{ V}$) |
| 2 | `OUT1` | Power Output | H-bridge output 1 |
| 3 | `OUT2` | Power Output | H-bridge output 2 |
| 4 | `GND` | Power / Ground | Device ground reference ($0\text{ V}$) |
| 5 | `IN2` | Digital Input | Control logic / PWM input 2 |
| 6 | `IN1` | Digital Input | Control logic / PWM input 1 |
| 7 | `~nSLEEP~` | Digital Input | Active-low sleep control (`LOW` = sleep $< 120\text{ nA}$, `HIGH` = active) |
| 8 | `VCC` | Power Supply | Logic supply input ($+1.8\text{ V}$ to $+7.0\text{ V}$) |
| PAD | `PowerPAD` | Thermal Ground | Exposed underside thermal ground tab; solder to PCB ground plane |

## Functional description

### Function Truth Table

| `~nSLEEP~` | `IN1` | `IN2` | `OUT1` | `OUT2` | Operating Mode |
|---|---|---|---|---|---|
| **`LOW`** | X | X | **`High-Z`** | **`High-Z`** | Sleep state (Ultra-low standby current $< 120\text{ nA}$) |
| `HIGH` | **`LOW`** | **`LOW`** | **`High-Z`** | **`High-Z`** | Coast / Fast decay (Motor freewheels to a stop) |
| `HIGH` | **`HIGH`** | **`LOW`** | **`HIGH`** | **`LOW`** | Forward rotation (OUT1 driven high, OUT2 low) |
| `HIGH` | **`LOW`** | **`HIGH`** | **`LOW`** | **`HIGH`** | Reverse rotation (OUT1 driven low, OUT2 high) |
| `HIGH` | **`HIGH`** | **`HIGH`** | **`LOW`** | **`LOW`** | Brake / Slow decay (Both low-side FETs ON; dynamic braking) |

- **PWM Speed Modulation:**
  - **Drive / Brake PWM (Recommended):** Hold one input HIGH (e.g. `IN1 = 1`) and pulse the other input with PWM (`IN2 = PWM`). When PWM is LOW, the motor drives; when PWM is HIGH, both outputs short to ground (brake). This produces highly linear speed control with excellent low-speed torque.
  - **Drive / Coast PWM:** Hold one input LOW (e.g. `IN2 = 0`) and apply PWM to the other (`IN1 = PWM`). The motor alternates between driving and freewheeling.

## Absolute maximum ratings

> [!WARNING]
> Stresses beyond these ratings cause irreversible breakdown. Ensure motor supply transients never exceed $12.0\text{ V}$.

| Parameter | Symbol | Min | Max | Unit |
|---|---|---|---|---|
| Motor Supply Voltage | $V_M$ | $-0.3$ | $+12.0$ | V |
| Logic Supply Voltage | $V_{CC}$ | $-0.3$ | $+7.0$ | V |
| Output Voltages (`OUT1`, `OUT2`) | $V_{OUT}$ | $-0.3$ | $V_M + 0.3$ | V |
| Logic Input Voltages (`IN1`, `IN2`, `~nSLEEP~`) | $V_{IN}$ | $-0.3$ | $V_{CC} + 0.3$ | V |
| Peak Output Current | $I_{OUT(PEAK)}$ | — | $1.8$ | A |
| Operating Ambient Temperature Range | $T_A$ | $-40$ | $+85$ | °C |
| Operating Junction Temperature Range | $T_J$ | $-40$ | $+150$ | °C |
| Storage Temperature Range | $T_{stg}$ | $-65$ | $+150$ | °C |

## Electrical characteristics

($V_M = 5.0\text{ V}, V_{CC} = 3.3\text{ V}, T_A = 25^\circ\text{C}$ unless otherwise specified)

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Motor Supply Voltage | $V_M$ | 1.8 | — | 11.0 | V | Operating range |
| Logic Supply Voltage | $V_{CC}$ | 1.8 | — | 7.0 | V | Operating range |
| $V_M$ Sleep Current | $I_{VMQ}$ | — | 35 | 100 | nA | `~nSLEEP~` = 0 |
| $V_{CC}$ Sleep Current | $I_{VCCQ}$ | — | 85 | 300 | nA | `~nSLEEP~` = 0 |
| $V_{CC}$ Operating Current | $I_{VCC}$ | — | 0.8 | 1.5 | mA | $f_{PWM} = 50\text{ kHz}$ |
| High-Side MOSFET $R_{DS(ON)}$ | $R_{DS(ON)H}$ | — | 140 | 200 | mΩ | $V_M = 5.0\text{ V}, I_{OUT} = 0.8\text{ A}$ |
| Low-Side MOSFET $R_{DS(ON)}$ | $R_{DS(ON)L}$ | — | 140 | 200 | mΩ | $V_M = 5.0\text{ V}, I_{OUT} = 0.8\text{ A}$ |
| Total Bridge On-Resistance | $R_{DS(ON)}$ | — | 280 | 400 | mΩ | Combined HS + LS |
| Logic Input High Voltage | $V_{IH}$ | $0.7 \times V_{CC}$ | — | — | V | — |
| Logic Input Low Voltage | $V_{IL}$ | — | — | $0.3 \times V_{CC}$ | V | — |
| Overcurrent Protection Trip Point | $I_{OCP}$ | 1.8 | 2.5 | 3.2 | A | — |
| Thermal Shutdown Temperature | $T_{TSD}$ | 150 | 160 | 175 | °C | Die junction temp |

## Typical application circuit: 1-Cell Li-ion Battery Robot Drive

```
       +3.7V ... +7.4V Battery (VM)
       ────────────────────────┬───────────────────────────────────────────────┐
                               │                                               │
                             ┌─┴──┐ 22µF                                    ┌──┴──┐
                             │    │ Ceramic / Tantalum                      │ 1   │ (VM)
                             └─┬──┘                                       ┌─┴─────┴─┐
                               │                                          │ DRV8837 │
       GND ────────────────────┴──────────────────────────────────────────┤ 4 (GND) │
                                                                          │         │
       Microcontroller (3.3V)                                             │ 2 (OUT1)├───[ MINIATURE ]───┐
     ┌─────────────────┐                                                  │         │     DC MOTOR      │
     │        GPIO_IN1 ┼──────────────────────────────────────────────────┤ 6 (IN1) │                   │
     │                 │                                                  │         │ 3 (OUT2)──────────┘
     │        GPIO_IN2 ┼──────────────────────────────────────────────────┤ 5 (IN2) │
     │                 │                                                  │         │
     │      GPIO_SLEEP ┼──────────────────────────────────────────────────┤ 7 (~SLP)│
     │                 │                                                  │         │
     │            +3.3V┼───────────────────────┬──────────────────────────┤ 8 (VCC) │
     └─────────────────┘                       │                          └────┬────┘
                                             ┌─┴──┐ 0.1µF                      │
                                             │    │ Ceramic                 ┌──┴──┐
                                             └─┬──┘                         │ PAD │ (Thermal Ground)
                                               │                            └──┬──┘
                                              GND                              │
                                                                             [GND]
```

## Design considerations & common mistakes

- **Separate VM and VCC Decoupling:** Never omit capacitors on the power rails. Place a $10\,\mu\text{F} \dots 22\,\mu\text{F}$ low-ESR ceramic capacitor directly across pin 1 (`VM`) and pin 4 (`GND`), and a $0.1\,\mu\text{F}$ capacitor adjacent to pin 8 (`VCC`). Inductive spikes from small DC motors can otherwise breach the $12\text{ V}$ absolute maximum limit.
- **Microscopic 2x2mm WSON Soldering:** The tiny 8-pin DSG package has a lead pitch of only $0.5\text{ mm}$ and an exposed center thermal pad. Hand-soldering requires solder paste, a hot-air rework station, or the use of pre-assembled carrier breakout boards (such as Pololu's DRV8837 module).
- **VCC Supply is Required:** Unlike some motor drivers that derive their internal gate drive logic entirely from the motor rail, the DRV8837 **requires** an active voltage on pin 8 ($V_{CC} = 1.8\text{ V} \dots 7.0\text{ V}$). If $V_{CC}$ is disconnected, the internal logic remains unpowered and the outputs will not switch.
- **Sleep Pin Must Not Float:** Pin 7 (`~nSLEEP~`) does not feature an internal pull-up. If left floating, capacitive pickup will cause the device to randomly drop into sleep mode ($< 120\text{ nA}$), cutting power to the motor. Connect to MCU GPIO or tie to $V_{CC}$ with a $10\text{ k}\Omega$ pull-up.
