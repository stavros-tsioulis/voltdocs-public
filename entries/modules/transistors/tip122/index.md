## Overview

The **TIP122** is a 100V 5A complementary silicon NPN power Darlington transistor manufactured by STMicroelectronics, onsemi, and Texas Instruments. Housed in an industry-standard **TO-220AB** through-hole package, it is the highest-voltage member of the ubiquitous TIP120 series (TIP120: 60V, TIP121: 80V, TIP122: 100V).

Featuring a monolithic Darlington pair with built-in base-emitter bleed resistors and an integrated reverse collector-emitter **flywheel protection diode**, the TIP122 provides an immense DC current gain ($h_{FE} \ge 1000$). With a $100\text{V}$ breakdown voltage rating, it provides substantial voltage safety margin against inductive kickback, making it the most popular Darlington transistor for **driving $24\text{V} \dots 48\text{V}$ unipolar stepper motors (in 3D printers and CNC machines), pinball machine high-power solenoid coils, electromagnetic brakes, and automotive power actuators directly from 3.3V/5V microcontroller pins**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | Monolithic NPN Silicon Power Darlington BJT |
| **Package** | TO-220AB (3-pin through-hole) |
| **Collector-Emitter Voltage ($V_{CEO}$)**| **$100\text{ V}$ max** (Highest in TIP120 family) |
| **Collector-Base Voltage ($V_{CBO}$)** | **$100\text{ V}$ max** |
| **Continuous Collector Current ($I_C$)** | **$5.0\text{ A}$ max** ($8.0\text{ A}$ pulsed) |
| **Base Current ($I_B$)** | **$0.12\text{ A}$** ($120\text{ mA}$) |
| **DC Current Gain ($h_{FE}$)** | **$1000$ min** ($1000 \dots 5000$ at $I_C = 3.0\text{A}, V_{CE} = 3.0\text{V}$) |
| **Collector Saturation ($V_{CE(sat)}$)** | **$2.0\text{ V}$ max** at $I_C = 3.0\text{A}$ ($4.0\text{ V}$ max at $5.0\text{A}$) |
| **Total Power Dissipation ($P_D$)** | **$65\text{ Watts}$** ($T_C = 25^\circ\text{C}$ with heatsink) / $2.0\text{ W}$ free air |
| **Integrated Components** | Base-Emitter Bleed Resistors + Flywheel Protection Diode |
| **Complementary PNP Pair** | **TIP127** (100V PNP Darlington) |

## Pinout (TO-220AB Package - B-C-E Standard)

Looking at the **front labeled face** with leads pointing downward:

```
        ┌──────────────┐
        │  O  [Metal]  │ ── Tab is internally connected to Pin 2 (Collector)
        ├──────────────┤
        │    TIP122    │
        └─┬────┬────┬──┘
          1    2    3
          B    C    E
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `BASE` | Base Input | Base control input (Driven with logic current from MCU via $1\text{ k}\Omega$ resistor) |
| 2 (Tab) | `COLLECTOR` | Power Collector | Collector output (Internally connected to metal mounting tab) |
| 3 | `EMITTER` | Power Emitter | Emitter terminal (Connect to common system ground / $0\text{ V}$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$ | 100 | — | — | V | $I_C = 30\text{mA}, I_B = 0$ |
| Collector-Base Breakdown | $V_{(BR)CBO}$ | 100 | — | — | V | $I_C = 1.0\text{mA}, I_E = 0$ |
| Emitter-Base Breakdown | $V_{(BR)EBO}$ | 5.0 | — | — | V | $I_E = 2.0\text{mA}, I_C = 0$ |
| Collector Cutoff Current | $I_{CEO}$ | — | — | 500 | µA | $V_{CE} = 50\text{V}, I_B = 0$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 1000 | — | — | — | $I_C = 0.5\text{A}, V_{CE} = 3.0\text{V}$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 1000 | — | — | — | $I_C = 3.0\text{A}, V_{CE} = 3.0\text{V}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | — | 2.0 | V | $I_C = 3.0\text{A}, I_B = 12\text{mA}$ |
| Base-Emitter On Voltage | $V_{BE(on)}$ | — | — | 2.5 | V | $I_C = 3.0\text{A}, V_{CE} = 3.0\text{V}$ |

## Typical Application Circuit: Arduino 4-Phase Unipolar Stepper Motor Driver

In unipolar stepper motor systems (such as 28BYJ-48 or 6-wire NEMA 17/23 motors), four TIP122 transistors drive the coil phases:

```
                            +24V to +36V Motor Supply Rail
                                          │
                               [ + Motor Coil Phase - ]
                                          │
                                          ├───[ External 1N4007 Diode ]────────┐
                                          │   (Anode to Collector, Cathode to +V)
                                    [Pin 2: COLLECTOR]                         │
                                         TIP122                                │
  Arduino Digital Pin (0 - 5V)      [Pin 1: BASE]                              │
          │                               │                                    │
          ├───[ 1kΩ Resistor ]────────────┤                                    │
          │                               ├───[ 10kΩ Base Pull-Down Resistor ]─┤
         GND                              │                                    │
                                    [Pin 3: EMITTER]                           │
                                          │                                    │
                                         GND ──────────────────────────────────┴─── Common GND
```

## Comparison: TIP120 vs TIP121 vs TIP122

| Parameter | TIP120 | TIP121 | TIP122 |
|---|---|---|---|
| **$V_{CEO}$ Voltage** | $60\text{ V}$ | $80\text{ V}$ | **$100\text{ V}$** |
| **Max Current ($I_C$)** | $5.0\text{ A}$ | $5.0\text{ A}$ | **$5.0\text{ A}$** |
| **DC Gain ($h_{FE}$)** | $\ge 1000$ | $\ge 1000$ | **$\ge 1000$** |
| **Saturation $V_{CE(sat)}$**| $2.0\text{ V}$ | $2.0\text{ V}$ | **$2.0\text{ V}$** |
| **Complementary PNP** | TIP125 | TIP126 | **TIP127** |

## Common mistakes

- **Operating above 1.5A continuous without a heatsink:** Darlington transistors have a higher saturation voltage ($V_{CE(sat)} \approx 1.5\text{V} \dots 2.0\text{V}$) than single BJTs or low-$R_{DS(on)}$ MOSFETs. Dissipated power ($P = V_{CE(sat)} \times I_C$) reaches $6\text{W}$ at $3\text{A}$. Always attach a stamped aluminum heatsink for currents above $1.5\text{A}$.
- **Driving fast PWM (> 20kHz) without considering storage time:** Darlington pairs exhibit longer turn-off storage times ($t_{off} \approx 2\ \mu\text{s} \dots 4\ \mu\text{s}$) than modern MOSFETs. For ultrasonic PWM motor speed control above $20\text{kHz}$, a logic-level power MOSFET (such as **IRLZ44N** or **IRLB8721**) is recommended.

## Notes

- **Pinball Machine Standard:** The TIP122 and TIP102 are standard replacement transistors for Bally, Williams, and Stern pinball solenoid driver boards.
