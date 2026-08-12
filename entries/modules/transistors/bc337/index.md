## Overview

The **BC337** (BC337-40) is a high-current NPN bipolar junction transistor (BJT) manufactured by ON Semiconductor, Nexperia, and STMicroelectronics. Enclosed in a standard **TO-92 package**, it is widely used across European and global electronics designs as a step-up current driver compared to the standard BC547.

Capable of handling collector-emitter voltages up to **$45\text{ Volts}$** and continuous collector currents up to **$800\text{ mA}$** (with peak currents up to $1.0\text{ A}$), the BC337 is ideal for driving small DC motors, relay coils, buzzers, high-brightness LEDs, and medium-power audio output stages. Its complementary PNP transistor is the **BC327**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | NPN Bipolar Junction Transistor (BJT) |
| **Package** | TO-92 (Flat face front, leads pointing down) |
| **Collector-Emitter Voltage ($V_{CEO}$)**| $45\text{ V}$ max |
| **Collector-Base Voltage ($V_{CBO}$)**   | $50\text{ V}$ max |
| **Continuous Collector Current ($I_C$)**| $800\text{ mA}$ continuous ($1000\text{ mA}$ peak) |
| **DC Current Gain ($h_{FE}$)** | 100 to 630 (BC337-16: 100–250, BC337-25: 160–400, BC337-40: 250–630) |
| **Transition Frequency ($f_T$)** | $100\text{ MHz}$ min ($210\text{ MHz}$ typical) |
| **Power Dissipation ($P_D$)** | $625\text{ mW}$ ($T_A = 25^\circ\text{C}$) |

## Pinout (TO-92 Package)

Looking at the **flat face** of the TO-92 package with leads pointing down:

```
        ┌─────────────┐
        │    BC337    │  (Flat Package Face)
        └─┬───┬───┬───┘
          1   2   3
          C   B   E
```

| Pin | Name | Description |
|---|---|---|
| 1 | `COLLECTOR` (`C`) | Collector terminal (Load connection) |
| 2 | `BASE` (`B`) | Base terminal (Control input via base resistor) |
| 3 | `EMITTER` (`E`) | Emitter terminal (Ground reference 0 V) |

> [!WARNING]
> Pinout Warning: European C-B-E Pinout!
> - **BC337 (TO-92):** Pin 1 = Collector, Pin 2 = Base, Pin 3 = Emitter (**C-B-E**).
> - **2N3904 (TO-92):** Pin 1 = Emitter, Pin 2 = Base, Pin 3 = Collector (**E-B-C**).
> - Always double-check European BC-series pinouts when replacing American 2N-series transistors.

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Voltage | $V_{CEO}$ | 45 | — | — | V | $I_C = 10\text{mA}, I_B = 0$ |
| Collector Cutoff Current | $I_{CBO}$ | — | — | 100 | nA | $V_{CB} = 20\text{V}, I_E = 0$ |
| DC Current Gain (BC337-40)| $h_{FE}$ | 250 | — | 630 | — | $V_{CE} = 1\text{V}, I_C = 100\text{mA}$ |
| Collector Saturation Volts| $V_{CE(sat)}$| — | 350 | 700 | mV | $I_C = 500\text{mA}, I_B = 50\text{mA}$ |
| Base-Emitter On Voltage | $V_{BE(on)}$ | — | — | 1.2 | V | $V_{CE} = 1\text{V}, I_C = 300\text{mA}$ |

## Common mistakes

- **Exceeding $625\text{ mW}$ thermal dissipation:** When operating near the maximum $800\text{ mA}$ collector current, ensure $V_{CE(sat)}$ is minimized by supplying adequate base drive current ($I_B \ge I_C / 10$). High $V_{CE}$ under heavy load causes thermal breakdown.
- **Connecting Base directly to MCU GPIO:** Connecting a 5V or 3.3V GPIO pin directly to the Base destroys the transistor. Always insert a series Base resistor (e.g. $220\ \Omega$ to $1\text{ k}\Omega$).

## Notes

- **BC337 vs BC547:** BC337 handles $800\text{ mA}$ continuous current; BC547 is rated for $100\text{ mA}$. Use BC337 when driving relays, motors, or power indicators.
