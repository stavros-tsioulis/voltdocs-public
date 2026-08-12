## Overview

The **TIP120** is an iconic NPN power Darlington transistor manufactured by STMicroelectronics, ON Semiconductor, and Texas Instruments. Packaged in a heavy-duty **TO-220AB enclosure**, it combines two cascading bipolar transistors on a single monolithic chip to achieve an ultra-high current gain ($h_{FE} \ge 1000$).

Because of its extreme current gain, a tiny microamp base current from an Arduino, ESP32, or Raspberry Pi GPIO pin can switch continuous loads up to **$5.0\text{ Amps}$** at up to **$60\text{ Volts}$**. The TIP120 includes internal base-emitter stabilization resistors and an anti-parallel freewheeling diode across the collector and emitter.

## Quick reference

| | |
|---|---|
| **Transistor Type** | NPN Monolithic Power Darlington Transistor |
| **Package** | TO-220AB (Metal tab connected to COLLECTOR) |
| **Collector-Emitter Voltage ($V_{CEO}$)**| $60\text{ V}$ max |
| **Continuous Collector Current ($I_C$)**| $5.0\text{ A}$ continuous ($8.0\text{ A}$ peak) |
| **Base Current ($I_B$)** | $120\text{ mA}$ max |
| **DC Current Gain ($h_{FE}$)** | $1000$ min (at $I_C = 3.0\text{A}, V_{CE} = 3.0\text{V}$) |
| **Collector Saturation Voltage ($V_{CE(sat)}$)**| $2.0\text{ V}$ max at $I_C = 3.0\text{A}, I_B = 12\text{mA}$ |
| **Power Dissipation ($P_D$)** | $65\text{ W}$ ($T_C = 25^\circ\text{C}$) / $2.0\text{ W}$ ($T_A = 25^\circ\text{C}$) |

## Pinout (TO-220AB Package)

Looking at the **front labeled face** of the TO-220 package with leads pointing down:

```
        ┌─────────────┐
        │   O   [TAB] │  (Metal Mounting Tab = COLLECTOR)
        ├─────────────┤
        │   TIP120    │  (Front Package Face)
        └─┬───┬───┬───┘
          1   2   3
          B   C   E
```

| Pin | Name | Description |
|---|---|---|
| 1 | `BASE` (`B`) | Base control input (Connect to MCU GPIO via $1\text{k}\Omega$ resistor) |
| 2 | `COLLECTOR` (`C`) | Collector terminal (Connected internally to tab) |
| 3 | `EMITTER` (`E`) | Emitter terminal (Ground reference 0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Breakdown | $V_{(BR)CEO}$| 60 | — | — | V | $I_C = 100\text{mA}, I_B = 0$ |
| DC Current Gain | $h_{FE}$ | 1000 | — | — | — | $V_{CE} = 3\text{V}, I_C = 3\text{A}$ |
| Collector Saturation Volts| $V_{CE(sat)}$| — | 1.2 | 2.0 | V | $I_C = 3\text{A}, I_B = 12\text{mA}$ |
| Base Saturation Voltage | $V_{BE(sat)}$| — | 1.8 | 2.5 | V | $I_C = 3\text{A}, I_B = 12\text{mA}$ |
| Base-Emitter On Voltage | $V_{BE(on)}$ | — | — | 2.5 | V | $V_{CE} = 3\text{V}, I_C = 3\text{A}$ |

## Microcontroller DC Load Driver Circuit

```
            +12V DC Load Power Rail
                     │
             [Solenoid / Relay / Motor]
                     │
                     ├─── [Pin 2 & Tab: COLLECTOR]
                     │         TIP120
  MCU GPIO ───[1kΩ]──┼─── [Pin 1: BASE]
                     │
                     └─── [Pin 3: EMITTER] ─── GND
```

## Common mistakes

- **Ignoring high Darlington saturation voltage ($V_{CE(sat)} \approx 1.2\text{V} \dots 2.0\text{V}$):** Because a Darlington pair consists of two cascaded VBE junctions, $V_{CE(sat)}$ is higher than a single BJT ($0.2\text{V}$). At $3\text{A}$ load, power dissipation in the TIP120 is $3\text{A} \times 1.5\text{V} = 4.5\text{ Watts}$. A heatsink is mandatory for loads $>1.5\text{A}$.
- **Applying 5V directly to Base without resistor:** Although the Darlington has internal base resistors, always place an external $1\text{ k}\Omega$ resistor in series with the MCU GPIO pin to protect the pin from excessive current.

## Notes

- **TIP120 vs TIP121 vs TIP122:** TIP120 is rated for 60V; TIP121 is rated for 80V; TIP122 is rated for 100V. All three share identical pinouts and current ratings.
