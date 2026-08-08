## Overview

The **BC547** (and its gain sub-variants **BC547A**, **BC547B**, and **BC547C**) is the standard European general-purpose NPN Bipolar Junction Transistor (BJT) manufactured by STMicroelectronics, ON Semiconductor, and Fairchild. It is widely used in audio preamplifiers, sensor signal conditioning, low-current LED driving, and digital logic switching.

Housed in a 3-pin **TO-92 plastic package**, the BC547 is rated for a collector-emitter breakdown voltage ($V_{CEO}$) of **$45\text{ Volts}$** and continuous collector current ($I_C$) of **$100\text{ mA}$**. Its complementary PNP counterpart is the **BC557**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | General-Purpose NPN Bipolar Junction Transistor (BJT) |
| **Package** | TO-92 (Flat face front, leads pointing down) / SOT-23 (BC847) |
| **Pinout (TO-92)** | Pin 1: Collector (`C`), Pin 2: Base (`B`), Pin 3: Emitter (`E`) — **C-B-E** |
| **Collector-Emitter Voltage ($V_{CEO}$)**| $45\text{ V}$ max |
| **Collector-Base Voltage ($V_{CBO}$)**  | $50\text{ V}$ max |
| **Continuous Collector Current ($I_C$)**| $100\text{ mA}$ continuous |
| **DC Current Gain ($h_{FE}$)** | $110\dots 220$ (A) / $200\dots 450$ (B) / $420\dots 800$ (C) |
| **Transition Frequency ($f_T$)** | $300\text{ MHz}$ typ |
| **Power Dissipation ($P_D$)** | $500\text{ mW}$ at $T_A = 25^\circ\text{C}$ |

## Pinout (TO-92 Package)

Looking at the **flat face** of the TO-92 package with leads pointing down:

```
        ┌─────────────┐
        │   BC547B    │  (Flat Package Face)
        └─┬───┬───┬───┘
          1   2   3
          C   B   E
```

| Pin | Name | Description |
|---|---|---|
| 1 | `COLLECTOR` (`C`) | Collector terminal (Low-side load connection) |
| 2 | `BASE` (`B`) | Base input control terminal (Connect via resistor) |
| 3 | `EMITTER` (`E`) | Emitter terminal (Ground reference 0 V) |

> [!IMPORTANT]
> Pinout Differences (BC547 vs 2N3904):
> - **BC547 (European standard):** Pin 1 = Collector, Pin 2 = Base, Pin 3 = Emitter (**C-B-E**).
> - **2N3904 (US standard):** Pin 1 = Emitter, Pin 2 = Base, Pin 3 = Collector (**E-B-C**).

## Gain Classification Suffixes

- **BC547A:** Low DC Current Gain ($h_{FE} = 110 \dots 220$).
- **BC547B:** Medium DC Current Gain ($h_{FE} = 200 \dots 450$) — **Most common kit variant**.
- **BC547C:** High DC Current Gain ($h_{FE} = 420 \dots 800$) — Ideal for weak sensor amplifiers.

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector Breakdown Voltage| $V_{(BR)CEO}$| 45 | — | — | V | $I_C = 10\text{mA}, I_B = 0$ |
| Emitter Breakdown Voltage | $V_{(BR)EBO}$| 6.0 | — | — | V | $I_E = 10\ \mu\text{A}, I_C = 0$ |
| Collector Saturation Volts| $V_{CE(sat)}$| — | 90 | 250 | mV | $I_C = 10\text{mA}, I_B = 0.5\text{mA}$ |
| Base Saturation Voltage | $V_{BE(sat)}$| — | 700| 900 | mV | $I_C = 10\text{mA}, I_B = 0.5\text{mA}$ |

## Common mistakes

- **Exceeding 100mA continuous load current:** The BC547 is a small-signal transistor limited to $100\text{ mA}$. Driving motors or relays requiring $>100\text{ mA}$ causes thermal breakdown. Use a 2N2222 ($800\text{mA}$) or IRLZ44N MOSFET instead.
- **Direct MCU pin connection without base resistor:** Always use a series base resistor ($1\ \text{k}\Omega \dots 10\ \text{k}\Omega$) to limit base current.

## Notes

- **BC547 vs BC557:** BC547 is NPN; BC557 is its complementary PNP transistor.
