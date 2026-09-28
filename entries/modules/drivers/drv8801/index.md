## Overview

The **DRV8801** (DRV8801RTY) is a single full-bridge brushed DC motor driver integrated circuit manufactured by Texas Instruments, widely used in robotics, camera motorized focus systems, automated locks, and industrial actuation via standalone IC layouts and popular carrier breakout boards (e.g., the Pololu DRV8801 carrier).

Operating across an $8.0\text{ V}$ to $38.0\text{ V}$ motor supply range, the DRV8801 can supply up to $2.8\text{ A}$ peak ($1.5\text{ A}$ continuous RMS with adequate copper heatsinking). It features a streamlined **PHASE/ENABLE** control interface, dedicated **BRAKE** input, low-power sleep mode ($< 10\,\mu\text{A}$), open-drain fault notification (`~nFAULT~`), and an integrated current-sense amplifier that outputs a real-time analog voltage proportional to motor winding current (`VPROPI`).

## Quick reference

| | |
|---|---|
| **Driver Topology** | Single Full H-Bridge (N-Channel Power MOSFETs) |
| **Motor Supply Voltage ($V_{MM}$)** | $8.0\text{ V}$ to $38.0\text{ V}$ DC |
| **Logic Supply Voltage ($V_{CC}$)** | Internally generated from $V_{MM}$ (3.3V/5V tolerant logic inputs) |
| **Peak Output Current ($I_{PEAK}$)** | $2.8\text{ A}$ |
| **Continuous RMS Current ($I_{RMS}$)** | $1.5\text{ A}$ (at $25^\circ\text{C}$ ambient with thermal dissipation) |
| **Total MOSFET $R_{DS(ON)}$** | $650\text{ m}\Omega$ typical (High-Side + Low-Side at $25^\circ\text{C}$) |
| **Current Sense Output ($V_{PROPI}$)** | Analog output current proportional to load current ($I_{OUT} / 1100$) |
| **Control Mode** | PHASE / ENABLE with active-high BRAKE input |
| **Protection Features** | Overcurrent (OCP), Thermal Shutdown (TSD), Undervoltage (UVLO) |
| **Package Options** | 16-pin QFN ($4\text{mm} \times 4\text{mm}$ RTY) with exposed thermal pad |

## Pin configuration

### 16-Pin QFN (RTY Package)

```
                 ┌──────────┐
           CP2  1│ 1     16 │ CP1
           VCP  2│          │ 15 VMM (Motor Supply)
         VPROPI 3│          │ 14 GND
          PHASE 4│  DRV8801 │ 13 OUT1
         ENABLE 5│          │ 12 SENSE
         ~nFAULT 6│ (Thermal │ 11 OUT2
         ~nSLEEP 7│   Pad)  │ 10 VMM (Motor Supply)
          BRAKE 8│ 8      9 │ NC
                 └──────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `CP2` | Analog I/O | Charge pump flying capacitor terminal 2 |
| 2 | `VCP` | Power Supply | Charge pump reservoir capacitor connection |
| 3 | `VPROPI` | Analog Output | Proportional current sensing output (connect external resistor to GND) |
| 4 | `PHASE` | Digital Input | Motor rotation direction (`HIGH` = Forward, `LOW` = Reverse) |
| 5 | `ENABLE` | Digital Input | Motor drive enable / PWM speed control input |
| 6 | `~nFAULT~` | Digital Output | Active-low open-drain fault indicator (OCP, TSD, UVLO) |
| 7 | `~nSLEEP~` | Digital Input | Active-low sleep control (`LOW` = sleep mode $< 10\,\mu\text{A}$, `HIGH` = active) |
| 8 | `BRAKE` | Digital Input | Active-high dynamic braking input (`HIGH` = shorts motor terminals to GND) |
| 9 | `NC` | Unconnected | No internal connection |
| 10, 15 | `VMM` | Power Supply | Motor power supply input ($+8.0\text{ V}$ to $+38.0\text{ V}$) |
| 11 | `OUT2` | Power Output | Full-bridge output terminal 2 |
| 12 | `SENSE` | Power Terminal | Low-side FET source return; connect low-value current sense resistor to GND |
| 13 | `OUT1` | Power Output | Full-bridge output terminal 1 |
| 14 | `GND` | Power / Ground | Device signal and power ground |
| 16 | `CP1` | Analog I/O | Charge pump flying capacitor terminal 1 |
| PAD | `PowerPAD` | Thermal Ground | Exposed backside heatsink pad; solder to ground plane |

## Functional description

### Function Truth Table

| Mode | `~nSLEEP~` | `BRAKE` | `PHASE` | `ENABLE` | `OUT1` | `OUT2` | Description |
|---|---|---|---|---|---|---|---|
| **Sleep** | **`LOW`** | X | X | X | **`High-Z`** | **`High-Z`** | Low-power standby ($I_{MM} < 10\,\mu\text{A}$) |
| **Brake** | `HIGH` | **`HIGH`** | X | X | **`LOW`** | **`LOW`** | Both low-side FETs ON; dynamic braking |
| **Forward** | `HIGH` | `LOW` | **`HIGH`** | **`HIGH`** | **`HIGH`** | **`LOW`** | Motor drives clockwise / forward |
| **Reverse** | `HIGH` | `LOW` | **`LOW`** | **`HIGH`** | **`LOW`** | **`HIGH`** | Motor drives counter-clockwise / reverse |
| **Coast** | `HIGH` | `LOW` | X | **`LOW`** | **`High-Z`** | **`High-Z`** | Fast decay / passive freewheeling |

### Current Sensing via VPROPI

The DRV8801 mirrors the load current flowing through the low-side sense resistor $R_{SENSE}$ and sources a scaled mirror current out of the `VPROPI` pin:
$$I_{VPROPI} = rac{I_{OUT}}{1100}$$
By connecting a resistor $R_{VPROPI}$ between pin 3 and ground, an analog voltage proportional to motor current is generated for a microcontroller ADC:
$$V_{VPROPI} = I_{OUT} 	imes rac{R_{VPROPI}}{1100}$$
For example, with $R_{VPROPI} = 2.2\text{ k}\Omega$, an output current of $1.0\text{ A}$ produces:
$$V_{VPROPI} = 1.0\text{ A} 	imes rac{2200\,\Omega}{1100} = 2.00\text{ V}$$

## Absolute maximum ratings

> [!WARNING]
> Stresses beyond these ratings cause permanent breakdown. Operating near absolute maximums requires effective PCB heat spreading.

| Parameter | Symbol | Min | Max | Unit |
|---|---|---|---|---|
| Motor Supply Voltage | $V_{MM}$ | $-0.3$ | $+40.0$ | V |
| Output Pin Voltages (`OUT1`, `OUT2`) | $V_{OUT}$ | $-1.0$ | $V_{MM} + 1.0$ | V |
| Sense Pin Voltage | $V_{SENSE}$ | $-0.5$ | $+0.5$ | V |
| Digital Logic Input Voltages | $V_{IN}$ | $-0.3$ | $+7.0$ | V |
| Peak Output Current | $I_{OUT(PEAK)}$ | — | $2.8$ | A |
| Operating Temperature Range | $T_A$ | $-40$ | $+85$ | °C |
| Junction Temperature Range | $T_J$ | $-40$ | $+150$ | °C |
| Storage Temperature Range | $T_{stg}$ | $-65$ | $+150$ | °C |

## Electrical characteristics

($V_{MM} = 24\text{ V}, T_A = 25^\circ\text{C}$ unless otherwise specified)

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Motor Supply Voltage | $V_{MM}$ | 8.0 | — | 38.0 | V | Operating range |
| Quiescent Sleep Current | $I_{MMSLEEP}$ | — | 1.0 | 10.0 | µA | `~nSLEEP~` = 0 |
| Operating Supply Current | $I_{MM}$ | — | 4.0 | 8.0 | mA | No motor load |
| High-Side FET On-Resistance | $R_{DS(ON)H}$ | — | 325 | 450 | mΩ | $I_{OUT} = 1.0\text{ A}$ |
| Low-Side FET On-Resistance | $R_{DS(ON)L}$ | — | 325 | 450 | mΩ | $I_{OUT} = 1.0\text{ A}$ |
| Total Bridge On-Resistance | $R_{DS(ON)}$ | — | 650 | 900 | mΩ | Combined HS + LS |
| Logic Input High Voltage | $V_{IH}$ | 2.0 | — | — | V | $3.3\text{V} \dots 5\text{V}$ compatible |
| Logic Input Low Voltage | $V_{IL}$ | — | — | 0.8 | V | — |
| `~nFAULT~` Saturation Voltage | $V_{OL(FAULT)}$ | — | 0.2 | 0.4 | V | $I_{SINK} = 1\text{ mA}$ |
| Overcurrent Protection Threshold | $I_{OCP}$ | 2.8 | 3.5 | 4.5 | A | — |
| Thermal Shutdown Threshold | $T_{TSD}$ | 150 | 165 | 180 | °C | Die junction temp |

## Typical application circuit

```
       +12V to +36V Motor Power (VMM)
       ────────────────────────┬───────────────────────────────────────────────┐
                               │                                               │
                             ┌─┴──┐ 47µF                                    ┌──┴──┐
                             │    │ 50V Electr.                             │ 10, │ (VMM)
                             └─┬──┘                                         │ 15  │
                               │                                          ┌─┴─────┴─┐
       GND ────────────────────┴──────────────────────────────────────────┤ 14(GND) │
                                                                          │         │
       Microcontroller                                                    │         │ 13(OUT1) ───[ MOTOR ]───┐
     ┌─────────────────┐                                                  │         │                         │
     │        GPIO_DIR ┼──────────────────────────────────────────────────┤ 4(PHASE)│                         │
     │                 │                                                  │         │                         │
     │        GPIO_PWM ┼──────────────────────────────────────────────────┤ 5(ENABLE│ 11(OUT2) ───────────────┘
     │                 │                                                  │         │
     │      GPIO_BRAKE ┼──────────────────────────────────────────────────┤ 8(BRAKE)│
     │                 │                                                  │         │
     │      GPIO_SLEEP ┼──────────────────────────────────────────────────┤ 7(~SLP) │
     │                 │                                                  │         │ 12(SENSE)
     │       FAULT_INT ┼──────────────┬───────────────────────────────────┤ 6(~FLT) └──┬───────────┐
     │                 │             ┌┴┐ 10k                              │            │           │
     │                 │             │ │ Pull-up                          │          ┌─┴──┐      ┌─┴──┐
     │                 │             └┬┘                                  │          │Rs  │      │ C  │ 0.1µF
     │                 │              ├────── +3.3V / +5V                 │          │0.05│      │    │
     │         ADC_IN1 ┼──────────────┼───────────────────────────────────┤ 3(VPROPI)└─┬──┘      └─┬──┘
     └─────────────────┘              │                                   └────────────┤           │
                                     ┌┴┐ Rvpropi (2.2k)                                │           │
                                     │ │                                             ┌─┴───────────┴─┐
                                     └┬┘                                             │  Power Ground │
                                      │                                              │      GND      │
                                     GND                                             └───────────────┘
```

## Design considerations & common mistakes

- **Bulk Capacitance Placement:** Switching inductive motor currents causes intense inductive kickback voltage spikes on the $V_{MM}$ supply rails. Always place a low-ESR electrolytic capacitor ($\ge 47\,\mu	ext{F} \dots 100\,\mu	ext{F}, 50	ext{V}$) alongside a $0.1\,\mu	ext{F}$ ceramic capacitor immediately adjacent to pins 10 and 15.
- **Charge Pump Capacitors:** The high-side N-channel gate driver requires a flying capacitor ($0.01\,\mu	ext{F} \dots 0.1\,\mu	ext{F}$ ceramic) between pins 1 (`CP2`) and 16 (`CP1`), and a reservoir capacitor ($0.1\,\mu	ext{F}$ ceramic) from pin 2 (`VCP`) to `VMM`. Without these capacitors, the high-side MOSFETs cannot switch ON.
- **Thermal Pad Must Be Soldered:** The 16-pin QFN package generates significant heat when continuous currents approach $1.5	ext{ A}$ ($P pprox I^2 R = 1.5^2 	imes 0.65 = 1.46	ext{ W}$). The backside exposed PowerPAD must be soldered directly to an extensive PCB ground plane with thermal vias; running the IC without soldering the thermal pad will cause rapid thermal shutdown ($165^\circ	ext{C}$).
- **Braking vs. Coasting:** When `ENABLE` is brought LOW, the motor freewheels (coasts) through the MOSFET body diodes. When `BRAKE` is driven HIGH, both low-side MOSFETs turn ON, dead-shorting the spinning motor terminals and stopping rotation rapidly via regenerative counter-electromotive force (EMF).
