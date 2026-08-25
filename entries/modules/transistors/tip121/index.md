## Overview

The **TIP121** is an 80V 5A complementary silicon NPN power Darlington transistor manufactured by STMicroelectronics, onsemi, and Texas Instruments. Housed in an industry-standard **TO-220AB** through-hole package, it serves as the intermediate-voltage member of the famous TIP120 series (TIP120: 60V, TIP121: 80V, TIP122: 100V).

Monolithically integrating two bipolar junction transistors in a Darlington pair configuration with built-in base-emitter speed-up bleed resistors ($R_1 \approx 8\text{ k}\Omega, R_2 \approx 120\ \Omega$) and an integrated anti-parallel collector-emitter **damper clamping diode**, the TIP121 delivers an immense DC current gain ($h_{FE} \ge 1000$). It allows high-current $3\text{A} \dots 5\text{A}$ inductive loads on $24\text{V} \dots 48\text{V}$ power rails to be controlled directly from a **$3.3\text{V}$ or $5\text{V}$ microcontroller GPIO pin** with only a few milliamps of base drive current.

## Quick reference

| | |
|---|---|
| **Transistor Type** | Monolithic NPN Silicon Power Darlington BJT |
| **Package** | TO-220AB (3-pin through-hole) |
| **Collector-Emitter Voltage ($V_{CEO}$)**| **$80\text{ V}$ max** |
| **Collector-Base Voltage ($V_{CBO}$)** | **$80\text{ V}$ max** |
| **Continuous Collector Current ($I_C$)** | **$5.0\text{ A}$ max** ($8.0\text{ A}$ pulsed) |
| **Base Current ($I_B$)** | **$0.12\text{ A}$** ($120\text{ mA}$) |
| **DC Current Gain ($h_{FE}$)** | **$1000$ min** ($1000 \dots 5000$ at $I_C = 3.0\text{A}, V_{CE} = 3.0\text{V}$) |
| **Collector Saturation ($V_{CE(sat)}$)** | **$2.0\text{ V}$ max** at $I_C = 3.0\text{A}$ ($4.0\text{ V}$ max at $5.0\text{A}$) |
| **Total Power Dissipation ($P_D$)** | **$65\text{ Watts}$** ($T_C = 25^\circ\text{C}$ with heatsink) / $2.0\text{ W}$ free air |
| **Integrated Components** | Base-Emitter Bleed Resistors + Flywheel Protection Diode |
| **Complementary PNP Pair** | **TIP126** (80V PNP Darlington) |

## Pinout (TO-220AB Package - B-C-E Standard)

Looking at the **front labeled face** with leads pointing downward:

```
        ┌──────────────┐
        │  O  [Metal]  │ ── Tab is internally connected to Pin 2 (Collector)
        ├──────────────┤
        │    TIP121    │
        └─┬────┬────┬──┘
          1    2    3
          B    C    E
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `BASE` | Base Input | Base control input (Directly driven by MCU GPIO via $1\text{ k}\Omega$ resistor) |
| 2 (Tab) | `COLLECTOR` | Power Collector | Collector output (Internally connected to metal mounting tab) |
| 3 | `EMITTER` | Power Emitter | Emitter terminal (Connect to common ground / $0\text{ V}$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$ | 80 | — | — | V | $I_C = 30\text{mA}, I_B = 0$ |
| Collector-Base Breakdown | $V_{(BR)CBO}$ | 80 | — | — | V | $I_C = 1.0\text{mA}, I_E = 0$ |
| Emitter-Base Breakdown | $V_{(BR)EBO}$ | 5.0 | — | — | V | $I_E = 2.0\text{mA}, I_C = 0$ |
| Collector Cutoff Current | $I_{CEO}$ | — | — | 500 | µA | $V_{CE} = 40\text{V}, I_B = 0$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 1000 | — | — | — | $I_C = 0.5\text{A}, V_{CE} = 3.0\text{V}$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 1000 | — | — | — | $I_C = 3.0\text{A}, V_{CE} = 3.0\text{V}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | — | 2.0 | V | $I_C = 3.0\text{A}, I_B = 12\text{mA}$ |
| Base-Emitter On Voltage | $V_{BE(on)}$ | — | — | 2.5 | V | $I_C = 3.0\text{A}, V_{CE} = 3.0\text{V}$ |

## Typical Application Circuit: 24V/48V Industrial Solenoid / Valve Driver

```
                       +24V to +48V Industrial DC Supply
                                      │
                              [ + Solenoid Valve - ]
                                      │
                                      ├───[ External 1N4007 Diode (Recommended) ]──┐
                                      │   (Anode to Collector, Cathode to +V)      │
                                [Pin 2: COLLECTOR]                                 │
                                     TIP121                                        │
  MCU GPIO (3.3V / 5V)          [Pin 1: BASE]                                      │
          │                           │                                            │
          ├───[ 1kΩ - 2.2kΩ Resistor ]┤                                            │
          │                           ├───[ 10kΩ Base Pull-Down Resistor ]─────────┤
         GND                          │                                            │
                                [Pin 3: EMITTER]                                   │
                                      │                                            │
                                     GND ──────────────────────────────────────────┴─── Common GND
```

## Comparison: TIP120 vs TIP121 vs TIP122

| Parameter | TIP120 | TIP121 | TIP122 |
|---|---|---|---|
| **$V_{CEO}$ Rating** | $60\text{ V}$ | **$80\text{ V}$** | **$100\text{ V}$** |
| **Max Current ($I_C$)** | $5.0\text{ A}$ | $5.0\text{ A}$ | $5.0\text{ A}$ |
| **DC Gain ($h_{FE}$)** | $\ge 1000$ | $\ge 1000$ | $\ge 1000$ |
| **Saturation $V_{CE(sat)}$**| $2.0\text{ V}$ | $2.0\text{ V}$ | $2.0\text{ V}$ |
| **Complementary PNP** | TIP125 | **TIP126** | **TIP127** |

## Common mistakes

- **Ignoring the ~2V Darlington saturation voltage drop ($V_{CE(sat)}$):** Because a Darlington pair consists of two cascaded transistors, $V_{CE(sat)}$ cannot drop below $V_{BE2} + V_{CE(sat)1} \approx 1.2\text{V} \dots 2.0\text{V}$. At $I_C = 3\text{A}$, the transistor dissipates $P = 2.0\text{V} \times 3\text{A} = 6.0\text{ Watts}$. A heatsink is mandatory for continuous currents $> 1.5\text{A}$.
- **Relying solely on the internal damper diode for heavy inductive switching:** While the TIP121 contains an on-chip diode across collector-emitter, its current rating is limited. For large solenoids or motors, always place an external fast-recovery diode (e.g. 1N4007 or 1N5822) directly across the coil terminals.

## Notes

- **Suffix Guide:** `TIP121` is the standard through-hole TO-220AB package; `TIP121G` denotes RoHS lead-free green molding compound.
