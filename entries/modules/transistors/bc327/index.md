## Overview

The **BC327** (BC327-40) is a high-current PNP general-purpose bipolar junction transistor (BJT) manufactured by ON Semiconductor, Nexperia, and STMicroelectronics. Packaged in a **TO-92 plastic housing**, it is the direct PNP complementary transistor to the **BC337**.

With a high continuous collector current rating of **$-800\text{ mA}$** (peak $-1.0\text{ A}$) and a collector-emitter breakdown voltage of **$-45\text{ Volts}$**, the BC327 is widely used for high-side power switching, relay and solenoid driving, audio power amplifier push-pull driver stages, and LED power control.

## Quick reference

| | |
|---|---|
| **Transistor Type** | PNP Bipolar Junction Transistor (BJT) |
| **Package** | TO-92 (Flat face front, leads pointing down) |
| **Collector-Emitter Voltage ($V_{CEO}$)**| $-45\text{ V}$ max |
| **Collector-Base Voltage ($V_{CBO}$)**   | $-50\text{ V}$ max |
| **Continuous Collector Current ($I_C$)**| $-800\text{ mA}$ continuous ($-1000\text{ mA}$ peak) |
| **DC Current Gain ($h_{FE}$)** | 100 to 630 (BC327-16: 100–250, BC327-25: 160–400, BC327-40: 250–630) |
| **Transition Frequency ($f_T$)** | $100\text{ MHz}$ min ($200\text{ MHz}$ typical) |
| **Power Dissipation ($P_D$)** | $625\text{ mW}$ ($T_A = 25^\circ\text{C}$) |

## Pinout (TO-92 Package)

Looking at the **flat face** of the TO-92 package with leads pointing down:

```
        ┌─────────────┐
        │    BC327    │  (Flat Package Face)
        └─┬───┬───┬───┘
          1   2   3
          C   B   E
```

| Pin | Name | Description |
|---|---|---|
| 1 | `COLLECTOR` (`C`) | Collector terminal (Load output connection) |
| 2 | `BASE` (`B`) | Base terminal (Control input via base resistor) |
| 3 | `EMITTER` (`E`) | Emitter terminal (High-side power rail $+V_{CC}$) |

> [!WARNING]
> Pinout Warning: European C-B-E Pinout!
> - **BC327 (TO-92):** Pin 1 = Collector, Pin 2 = Base, Pin 3 = Emitter (**C-B-E**).
> - **PN2907A (TO-92):** Pin 1 = Emitter, Pin 2 = Base, Pin 3 = Collector (**E-B-C**).

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Voltage | $V_{CEO}$ | -45 | — | — | V | $I_C = -10\text{mA}, I_B = 0$ |
| Collector Cutoff Current | $I_{CBO}$ | — | — | -100 | nA | $V_{CB} = -20\text{V}, I_E = 0$ |
| DC Current Gain (BC327-40)| $h_{FE}$ | 250 | — | 630 | — | $V_{CE} = -1\text{V}, I_C = -100\text{mA}$ |
| Collector Saturation Volts| $V_{CE(sat)}$| — | -350 | -700 | mV | $I_C = -500\text{mA}, I_B = -50\text{mA}$ |
| Base-Emitter On Voltage | $V_{BE(on)}$ | — | — | -1.2 | V | $V_{CE} = -1\text{V}, I_C = -300\text{mA}$ |

## Common mistakes

- **Exceeding $625\text{ mW}$ package dissipation:** Under heavy collector current (e.g. $-800\text{ mA}$), keep base drive sufficiently strong ($I_B \ge I_C / 10$) so the transistor stays fully saturated.
- **Direct MCU connection for high-side supply rails $> 5\text{V}$:** When switching a $12\text{V}$ rail using a BC327, driving the base directly from a 3.3V or 5V MCU pin will keep the transistor ON permanently. Use an NPN transistor to pull the BC327 base LOW.

## Notes

- **BC327 vs BC337:** BC327 is PNP ($800\text{ mA}$ high-side switch); BC337 is NPN ($800\text{ mA}$ low-side switch).
