## Overview

The **TMC2209** (TMC2209-LA) is an ultra-silent 2-phase stepper motor driver IC manufactured by Trinamic (Analog Devices). It represents the state-of-the-art upgrade over the TMC2208, featuring higher continuous current handling (**$1.4\text{A}$ to $2.0\text{A RMS}$**), lower internal MOSFET resistance ($R_{DS(on)} = 170\text{ m}\Omega$), and advanced **StallGuard4** load measurement for sensorless homing.

Packaged in a **28-pin QFN** or 16-pin SilentStepStick module footprint, the TMC2209 operates on motor voltages from **4.75V to 28V DC**. It incorporates **StealthChop2** for silent motor operation, **CoolStep** for up to 75% energy savings, and a **single-wire UART interface** with 4 hardware-selectable slave addresses, enabling multiple drivers to share a single UART bus.

## Quick reference

| | |
|---|---|
| **Motor Supply Voltage (`VM`)** | 4.75 V to 28 V DC |
| **Logic Supply Voltage (`VIO`)** | 3.0 V to 5.25 V DC |
| **Phase Current Rating** | $1.4\text{ A}_{\text{RMS}}$ continuous ($2.0\text{ A}_{\text{RMS}}$ with active cooling, $2.8\text{ A}$ peak) |
| **Microstep Resolutions** | Up to 1/64 native (Interpolated to 1/256 via MicroPlyer) |
| **Key Technologies** | StealthChop2 (Silent), StallGuard4 (Sensorless Homing), CoolStep, SpreadCycle |
| **UART Addressability** | Up to 4 drivers on 1 single-wire UART bus via MS1/MS2 pins |
| **Special Output** | `DIAG` pin for stall detection interrupt to MCU GPIO |
| **Package** | 28-pin QFN ($5 \times 5\text{ mm}$) / SilentStepStick 16-pin Module |

## Pinout (SilentStepStick 16-Pin Breakout Header)

```
                       ┌─────────────┐
                 [EN] 1│ 1        16│ [VM] (Motor Power 4.75-28V)
                [MS1] 2│            │15 [GND] (Motor Power GND)
                [MS2] 3│  TMC2209   │14 [2B] (Motor Phase B)
               [DIAG] 4│ SilentStep │13 [2A] (Motor Phase B)
             [UART/RX]5│   Stick    │12 [1A] (Motor Phase A)
                [VCC_IO]6│          │11 [1B] (Motor Phase A)
               [STEP] 7│            │10 [VIO] (Logic Power 3.3/5V)
                [DIR] 8│            │9  [GND] (Logic Power GND)
                       └─────────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `EN` | Input | Driver Enable (Low = Enable outputs; High = Disable) |
| 2 | `MS1` | Input | Microstep Select Pin 1 / UART Address Bit 0 |
| 3 | `MS2` | Input | Microstep Select Pin 2 / UART Address Bit 1 |
| 4 | `DIAG` | Output | StallGuard4 Stall Detect Interrupt Output (Active HIGH) |
| 5 | `UART` | I/O | Single-Wire UART Data Line (Connect to MCU TX/RX) |
| 7 | `STEP` | Input | Step Pulse Input |
| 8 | `DIR` | Input | Direction Input |
| 10 | `VIO` | Power | Logic Supply (+3.0V to +5.25V DC) |
| 11–14 | `1B, 1A, 2A, 2B` | Output | Stepper Motor Phase Connections |
| 15 | `GND` | Power | Power Ground |
| 16 | `VM` | Power | Motor Power Supply (+4.75V to +28V DC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Motor Supply Voltage | $V_M$ | 4.75 | 24.0 | 28.0 | V | DC |
| Continuous Phase Current | $I_{RMS}$ | — | 1.4 | 2.0 | A | With heatsink & cooling fan |
| Peak Output Current | $I_{PEAK}$ | — | — | 2.8 | A | Short transient peak |
| Power MOSFET On-Resistance | $R_{DS(on)}$| — | 170 | 230 | mΩ | $V_{VM} = 24\text{V}, T_J = 25^\circ\text{C}$ |
| Standby Current Reduction | $I_{HOLD}$ | — | 50 | — | % | Automatic motor idle current drop |

## Sensorless Homing with StallGuard4

StallGuard4 measures motor back-EMF during motion. When an axis hits a mechanical physical endstop, motor load spikes and StallGuard triggers the `DIAG` pin HIGH:

```cpp
// Klipper / Marlin Sensorless Homing Configuration Principle
// Connect DIAG pin directly to MCU Endstop Input (Stop on HIGH signal)
// TMC2209 UART registers set StallGuard threshold (SGTHRS) dynamically.
```

## Common mistakes

- **Exceeding $28\text{V}$ supply voltage:** Unlike the TMC2208 (rated for $36\text{V}$), the TMC2209 absolute maximum motor supply voltage is **$29\text{V}$**. Operating on a $36\text{V}$ power supply destroys the driver.
- **Forgetting a $1\text{ k}\Omega$ resistor on RX/TX single-wire UART join:** When connecting the MCU TX and RX pins to the single-wire `UART` pin on TMC2209 modules, place a $1\text{ k}\Omega$ resistor between MCU TX and the shared line to prevent bus contention.

## Notes

- **TMC2209 vs TMC2208:** TMC2209 supports higher current ($2.0\text{A}$ vs $1.2\text{A}$ RMS), lower heatsink temps ($170\text{ m}\Omega$ vs $280\text{ m}\Omega$), StallGuard4 sensorless homing, and up to 4 UART addresses on a single pin.
