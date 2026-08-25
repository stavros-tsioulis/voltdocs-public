## Overview

The **BD135** is a classic medium-power complementary silicon NPN bipolar junction transistor manufactured by STMicroelectronics, onsemi, and NXP. Housed in a through-hole **TO-126 (SOT-32)** plastic package with an integrated central mounting screw hole, it provides a rugged, heatsinkable alternative to small-signal TO-92 transistors.

Rated for a collector-emitter voltage ($V_{CEO}$) of **$45\text{V}$**, a continuous collector current of **$1.5\text{A}$** ($3.0\text{A}$ peak pulse), a transition frequency ($f_T$) of **$190\text{ MHz}$**, and up to **$12.5\text{ Watts}$** of power dissipation when heatsinked, the BD135 is widely used in **audio amplifier pre-driver and driver stages, medium-current relay and solenoid drivers, linear power supply series-pass elements, and discrete H-bridge motor controllers**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | Medium-Power Complementary Silicon NPN BJT |
| **Package** | TO-126 / SOT-32 (3-pin through-hole with mounting hole) |
| **Collector-Emitter Voltage ($V_{CEO}$)**| **$45\text{ V}$ max** |
| **Collector-Base Voltage ($V_{CBO}$)** | **$45\text{ V}$ max** |
| **Continuous Collector Current ($I_C$)** | **$1.5\text{ A}$ max** ($3.0\text{ A}$ peak pulse) |
| **Base Current ($I_B$)** | **$0.5\text{ A}$ max** |
| **DC Current Gain ($h_{FE}$)** | **$40$ to $250$** (BD135-10: 63–160, BD135-16: 100–250) |
| **Transition Frequency ($f_T$)** | **$190\text{ MHz}$ typ** ($> 50\text{ MHz}$ min) |
| **Power Dissipation ($P_D$)** | **$12.5\text{ Watts}$** ($T_C = 25^\circ\text{C}$ with heatsink) / $1.25\text{ W}$ in free air |
| **Complementary PNP Pair** | **BD136** (45V PNP) |

## Pinout (TO-126 / SOT-32 Package - E-C-B Standard)

Looking at the **printed front face** of the TO-126 package with leads pointing downward:

```
        ┌───────────────┐
        │   O [Mount]   │
        ├───────────────┤
        │     BD135     │
        └─┬─────┬─────┬─┘
          1     2     3
          E     C     B
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `EMITTER` | Emitter Terminal | Emitter (Connect to ground or negative supply rail) |
| 2 | `COLLECTOR`| Collector Terminal| Collector (Connected to switched load; internally bonded to rear metal tab) |
| 3 | `BASE` | Base Terminal | Base control input (Driven with base current via series resistor) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$ | 45 | — | — | V | $I_C = 10\text{mA}, I_B = 0$ |
| Collector-Base Breakdown | $V_{(BR)CBO}$ | 45 | — | — | V | $I_C = 100\ \mu\text{A}, I_E = 0$ |
| Emitter-Base Breakdown | $V_{(BR)EBO}$ | 5.0 | — | — | V | $I_E = 10\ \mu\text{A}, I_C = 0$ |
| Collector Cutoff Current | $I_{CBO}$ | — | — | 100 | nA | $V_{CB} = 30\text{V}, I_E = 0$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 40 | — | 250 | — | $I_C = 150\text{mA}, V_{CE} = 2.0\text{V}$ |
| DC Current Gain ($h_{FE}$) | $h_{FE}$ | 25 | — | — | — | $I_C = 500\text{mA}, V_{CE} = 2.0\text{V}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | — | 0.50 | V | $I_C = 500\text{mA}, I_B = 50\text{mA}$ |
| Base Saturation Voltage | $V_{BE(sat)}$ | — | — | 1.00 | V | $I_C = 500\text{mA}, I_B = 50\text{mA}$ |

## Typical Application Circuit: 12V 1A High-Power Relay / Lamp Driver

```
                       +12V DC Supply
                             │
                     [ + High-Current Load / Relay - ]
                             │
                             ├───[ 1N4007 Flyback Diode ]──────────┐
                             │   (Anode to Collector, Cathode to +12V)
                       [Pin 2: COLLECTOR]                          │
                            BD135                                  │
  MCU GPIO (3.3V / 5V) [Pin 3: BASE]                               │
          │                  │                                     │
          ├───[ 330Ω - 1kΩ ]─┤                                     │
          │                  ├───[ 10kΩ Base Pull-Down Resistor ]──┤
         GND                 │                                     │
                       [Pin 1: EMITTER]                            │
                             │                                     │
                            GND ───────────────────────────────────┴─── Common GND
```

## Comparison: BD135 vs BD137 vs BD139

| Parameter | BD135 | BD137 | BD139 |
|---|---|---|---|
| **$V_{CEO}$ Voltage** | **$45\text{ V}$** | $60\text{ V}$ | **$80\text{ V}$** |
| **Max Current ($I_C$)** | $1.5\text{ A}$ | $1.5\text{ A}$ | $1.5\text{ A}$ |
| **Transition Freq ($f_T$)**| $190\text{ MHz}$ | $190\text{ MHz}$ | $190\text{ MHz}$ |
| **Complementary PNP** | **BD136** | BD138 | **BD140** |

## Common mistakes

- **Assuming TO-92 (E-B-C) pinout:** The TO-126 BD135 uses the European standard **`Emitter - Collector - Base` (E-C-B)** sequence from left to right. Swapping the base and collector leads is the most common assembly error.
- **Operating above 1W without a heatsink:** While the silicon die is rated for 12.5W, in free air without a heatsink the package can only dissipate 1.25W before exceeding safe junction temperatures. Mount to a small aluminum clip-on or stamped heatsink for loads $> 500\text{mA}$.

## Notes

- **Gain Grouping:** Sub-grades are marked on the package: `-6` ($h_{FE} = 40 \dots 100$), `-10` ($h_{FE} = 63 \dots 160$), and `-16` ($h_{FE} = 100 \dots 250$).
