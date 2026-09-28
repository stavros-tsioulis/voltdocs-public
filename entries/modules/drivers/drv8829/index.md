## Overview

The **DRV8829** (DRV8829PWP) is a high-power single full-bridge brushed DC motor driver integrated circuit developed by Texas Instruments. Built on the same robust 45V power silicon platform as the industry-standard DRV8825 stepper driver, the DRV8829 is engineered to drive high-load brushed DC motors, linear actuators, high-force solenoids, and magnetic clutches requiring up to **$5.0\text{ A}$ peak** or **$3.5\text{ A}$ continuous RMS** current across a wide supply rail of **$8.2\text{ V}$ to $45.0\text{ V}$**.

Featuring a low combined MOSFET on-resistance of just **$300\text{ m}\Omega$**, the DRV8829 incorporates an autonomous **PWM current-regulation loop** with programmable fixed off-time decay modes (slow, fast, and mixed decay). This allows precise current limiting during motor stall and high-inertia startup conditions without burdening the host microcontroller with high-frequency current sampling.

## Quick reference

| | |
|---|---|
| **Driver Topology** | High-Current Single Full-Bridge (N-Channel Power MOSFETs) |
| **Motor Supply Voltage ($V_M$)** | $8.2\text{ V}$ to $45.0\text{ V}$ DC |
| **Peak Output Current ($I_{PEAK}$)** | $5.0\text{ A}$ |
| **Continuous RMS Current ($I_{RMS}$)** | $3.5\text{ A}$ (with appropriate PCB thermal heatsinking) |
| **Total MOSFET $R_{DS(ON)}$** | $300\text{ m}\Omega$ typical ($150\text{ m}\Omega$ HS + $150\text{ m}\Omega$ LS at $25^\circ\text{C}$) |
| **Current Regulation** | Built-in fixed off-time PWM current chopper |
| **Decay Modes** | Slow decay, fast decay, and mixed decay (via `DECAY` pin) |
| **Control Interface** | PHASE / ENABLE with PWM speed modulation |
| **Internal Reference Output** | $+3.3\text{ V}$ LDO output (`V3P3OUT`, up to $1\text{ mA}$) |
| **Package Options** | 28-pin HTSSOP ($9.7\text{mm} \times 4.4\text{mm}$ PWP) with PowerPAD |

## Pin configuration

### 28-Pin HTSSOP (PWP Package)

```
                 ┌───────────┐
            CP1 1│ 1      28 │ VCP
            CP2 2│           │ 27 VM (Motor Supply)
           VINT 3│           │ 26 OUT1
        V3P3OUT 4│           │ 25 OUT1
       ~nFAULT~ 5│           │ 24 ISEN (Current Sense)
       ~nRESET~ 6│  DRV8829  │ 23 ISEN (Current Sense)
       ~nSLEEP~ 7│  (Thermal │ 22 GND
          DECAY 8│    Pad)   │ 21 GND
         ENABLE 9│           │ 20 OUT2
          PHASE 10           │ 19 OUT2
           VREF 11           │ 18 VM (Motor Supply)
             NC 12           │ 17 NC
             NC 13           │ 16 NC
            GND 14     15 │ NC
                 └───────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1, 2 | `CP1`, `CP2` | Analog I/O | Charge pump flying capacitor connections ($0.01\,\mu\text{F}$) |
| 3 | `VINT` | Power Supply | Internal digital core bypass capacitor ($0.1\,\mu\text{F}, 6.3\text{V}$) |
| 4 | `V3P3OUT` | Power Output | $+3.3\text{ V}$ internal regulator output (decouple with $0.47\,\mu\text{F}$) |
| 5 | `~nFAULT~` | Digital Output | Active-low open-drain fault indicator (trips on OCP, TSD, UVLO) |
| 6 | `~nRESET~` | Digital Input | Active-low reset input; clears faults and enables internal logic |
| 7 | `~nSLEEP~` | Digital Input | Active-low sleep control (`LOW` = sleep mode $< 10\,\mu\text{A}$) |
| 8 | `DECAY` | 3-Level Input | Current decay mode (`LOW` = slow, `HIGH` = fast, `OPEN` = mixed) |
| 9 | `ENABLE` | Digital Input | Bridge enable control (`HIGH` = outputs active, `LOW` = High-Z) |
| 10 | `PHASE` | Digital Input | Rotation direction (`HIGH` = OUT1 H / OUT2 L, `LOW` = OUT1 L / OUT2 H) |
| 11 | `VREF` | Analog Input | Reference voltage input setting current regulation limit ($0\text{V} \dots 3.3\text{V}$) |
| 12,13,15,16,17 | `NC` | Unconnected | No internal connection |
| 14, 21, 22 | `GND` | Power / Ground | Device ground reference |
| 18, 27 | `VM` | Power Supply | Motor power supply input ($+8.2\text{ V}$ to $+45.0\text{ V}$) |
| 19, 20 | `OUT2` | Power Output | Full-bridge output 2 (internally tied) |
| 23, 24 | `ISEN` | Power Terminal | Low-side FET sense resistor connection to ground |
| 25, 26 | `OUT1` | Power Output | Full-bridge output 1 (internally tied) |
| 28 | `VCP` | Power Supply | Charge pump reservoir capacitor terminal |
| PAD | `PowerPAD` | Thermal Ground | Underside thermal ground pad; must be soldered to PCB ground plane |

## Functional description

### Current Chopping Regulation

The DRV8829 continuously measures motor current through an external low-value resistor ($R_{ISEN}$) connected between `ISEN` (pins 23/24) and `GND`. When motor current reaches the trip limit $I_{TRIP}$, the internal comparator turns off the driving MOSFETs for a fixed off-time ($t_{OFF} \approx 25\,\mu\text{s}$), recirculating current through the bridge:

$$I_{TRIP} = \frac{V_{REF}}{5 \times R_{ISEN}}$$

For example, selecting $R_{ISEN} = 0.1\,\Omega$ and supplying $V_{REF} = 1.65\text{ V}$ (half of $V3P3OUT$) sets a maximum continuous motor current limit of:
$$I_{TRIP} = \frac{1.65\text{ V}}{5 \times 0.1\,\Omega} = 3.30\text{ A}$$

### Control Truth Table

| `~nSLEEP~` | `~nRESET~` | `ENABLE` | `PHASE` | `OUT1` | `OUT2` | Operating State |
|---|---|---|---|---|---|---|
| **`LOW`** | X | X | X | **`High-Z`** | **`High-Z`** | Sleep state ($< 10\,\mu\text{A}$) |
| `HIGH` | **`LOW`** | X | X | **`High-Z`** | **`High-Z`** | Logic reset (bridge disabled) |
| `HIGH` | `HIGH` | **`LOW`** | X | **`High-Z`** | **`High-Z`** | Coast / Freewheel |
| `HIGH` | `HIGH` | `HIGH` | **`HIGH`** | **`HIGH`** | **`LOW`** | Forward drive |
| `HIGH` | `HIGH` | `HIGH` | **`LOW`** | **`LOW`** | **`HIGH`** | Reverse drive |

## Absolute maximum ratings

> [!WARNING]
> Stresses beyond these ratings cause immediate permanent failure. Solder the underside PowerPAD to a multi-layer ground plane.

| Parameter | Symbol | Min | Max | Unit |
|---|---|---|---|---|
| Motor Supply Voltage | $V_M$ | $-0.3$ | $+47.0$ | V |
| Output Voltages (`OUT1`, `OUT2`) | $V_{OUT}$ | $-0.6$ | $V_M + 0.6$ | V |
| Sense Resistor Terminal Voltage | $V_{ISEN}$ | $-0.8$ | $+0.8$ | V |
| Digital Logic Input Voltages | $V_{IN}$ | $-0.5$ | $+7.0$ | V |
| Peak Output Motor Current | $I_{OUT(PEAK)}$ | — | $5.0$ | A |
| Operating Temperature Range | $T_A$ | $-40$ | $+85$ | °C |
| Junction Temperature | $T_J$ | $-40$ | $+150$ | °C |
| Storage Temperature Range | $T_{stg}$ | $-65$ | $+150$ | °C |

## Electrical characteristics

($V_M = 24\text{ V}, T_A = 25^\circ\text{C}$ unless otherwise noted)

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Motor Supply Voltage | $V_M$ | 8.2 | — | 45.0 | V | Normal operation |
| Sleep Current | $I_{VM(SLEEP)}$ | — | 5.0 | 10.0 | µA | `~nSLEEP~` = 0 |
| Quiescent Operating Current | $I_{VM}$ | — | 4.0 | 7.0 | mA | No load, bridge enabled |
| High-Side FET On-Resistance | $R_{DS(ON)H}$ | — | 150 | 200 | mΩ | $I_{OUT} = 2.5\text{ A}$ |
| Low-Side FET On-Resistance | $R_{DS(ON)L}$ | — | 150 | 200 | mΩ | $I_{OUT} = 2.5\text{ A}$ |
| Total Bridge On-Resistance | $R_{DS(ON)}$ | — | 300 | 400 | mΩ | Combined HS + LS |
| Logic High Input Voltage | $V_{IH}$ | 2.0 | — | — | V | — |
| Logic Low Input Voltage | $V_{IL}$ | — | — | 0.8 | V | — |
| V3P3OUT Output Voltage | $V_{3P3}$ | 3.15 | 3.30 | 3.45 | V | $I_{OUT} \le 1\text{ mA}$ |
| Overcurrent Protection Limit | $I_{OCP}$ | 5.0 | 6.0 | 7.0 | A | — |
| Thermal Shutdown Temperature | $T_{TSD}$ | 150 | 160 | 175 | °C | Die junction |

## Typical application circuit

```
       +24V / +36V Motor Supply (VM)
       ────────────────────────┬───────────────────────────────────────────────┐
                               │                                               │
                             ┌─┴──┐ 100µF                                   ┌──┴──┐
                             │    │ 50V Low-ESR                             │ 18, │ (VM)
                             └─┬──┘                                         │ 27  │
                               │                                          ┌─┴─────┴─┐
       GND ────────────────────┴──────────────────────────────────────────┤ 14,21,22│ (GND)
                                                                          │         │
       Microcontroller                                                    │ 25,26   ├───[ HIGH-POWER ]───┐
     ┌─────────────────┐                                                  │ (OUT1)  │     MOTOR          │
     │        GPIO_PWM ┼──────────────────────────────────────────────────┤ 9(ENABLE│                    │
     │                 │                                                  │         │ 19,20              │
     │        GPIO_DIR ┼──────────────────────────────────────────────────┤ 10(PHASE│ (OUT2) ────────────┘
     │                 │                                                  │         │
     │      GPIO_RESET ┼──────────────────────────────────────────────────┤ 6(~RST) │ 23,24(ISEN)
     │                 │                                                  │         └──┬─────────┐
     │      GPIO_SLEEP ┼──────────────────────────────────────────────────┤ 7(~SLP)    │         │
     │                 │                                                  │          ┌─┴──┐    ┌─┴──┐
     │       FAULT_INT ┼──────────────┬───────────────────────────────────┤ 5(~FLT)  │Risen│   │ C  │ 0.1µF
     │                 │             ┌┴┐ 10k                              │          │0.05Ω│   │    │
     │                 │             │ │ Pull-up                          │          └─┬──┘    └─┬──┘
     │                 │             └┬┘                                  │            │         │
     │                 │              ├────── +3.3V                       │          ┌─┴─────────┴─┐
     │                 │              │                                   │          │Power Ground │
     │                 │           ┌──┴──┐                                │          │    GND      │
     │                 │           │ 4   │ (V3P3OUT)                      │          └─────────────┘
     │                 │           │     ├───[ 0.47µF ]─── GND            │
     │                 │           └──┬──┘                                │
     │                 │              │                                   │
     │                 │             ┌┴┐ R1 (10k)                         │
     │                 │             │ │                                  │
     │                 │             └┬┘                                  │
     │                 │              ├───────────────────────────────────┤ 11 (VREF)
     │                 │             ┌┴┐ R2 (10k, Vref = 1.65V)           │
     │                 │             │ │                                  │
     │                 │             └┬┘                                  │
     └─────────────────┘              │                                   └─────────┘
                                     GND
```

## Design considerations & common mistakes

- **PowerPAD Thermal Dissipation:** Delivering continuous currents of $3.0\text{ A} \dots 3.5\text{ A}$ dissipates $P \approx I^2 R = (3.5\text{A})^2 \times 0.30\,\Omega = 3.68\text{ W}$. The central PowerPAD must be soldered with thermal paste/solder to a copper ground plane containing an array of at least 9–15 thermal vias to the back layer; otherwise the part will enter thermal shutdown within seconds of load application.
- **Bulk Capacitance is Mandatory:** High-current PWM chopping generates severe voltage transients ($L \cdot di/dt$) on the $V_M$ power rail. Place a $100\,\mu\text{F} \dots 220\,\mu\text{F}$ low-ESR electrolytic capacitor directly across the $V_M$ pins (18, 27) and GND (21, 22), backed by a $0.1\,\mu\text{F}$ high-frequency ceramic capacitor.
- **Parallel Pin Connections:** Pins 25 & 26 (`OUT1`), 19 & 20 (`OUT2`), 23 & 24 (`ISEN`), and 18 & 27 (`VM`) are paired internally. Both pins of each pair **must** be tied together on the PCB using thick, heavy copper traces to avoid overstressing individual internal bond wires.
- **Noise Filtering on ISEN:** The current-sense resistor traces must be routed as a Kelvin-connection directly to pins 23 and 24, with a small parallel $0.1\,\mu\text{F}$ capacitor to suppress parasitic inductive ringing that could cause false current-limit tripping.
