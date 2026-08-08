## Overview

The **BC557** (and its gain sub-variants **BC557A**, **BC557B**, and **BC557C**) is the standard European general-purpose PNP Bipolar Junction Transistor (BJT) manufactured by STMicroelectronics, ON Semiconductor, and Fairchild. It is the direct PNP complementary match to the **BC547** NPN transistor.

Housed in a 3-pin **TO-92 plastic package**, the BC557 is rated for a collector-emitter breakdown voltage ($V_{CEO}$) of **$-45\text{ Volts}$** and continuous collector current ($I_C$) of **$-100\text{ mA}$**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | General-Purpose PNP Bipolar Junction Transistor (BJT) |
| **Package** | TO-92 (Flat face front, leads pointing down) / SOT-23 (BC857) |
| **Pinout (TO-92)** | Pin 1: Collector (`C`), Pin 2: Base (`B`), Pin 3: Emitter (`E`) — **C-B-E** |
| **Collector-Emitter Voltage ($V_{CEO}$)**| $-45\text{ V}$ max |
| **Collector-Base Voltage ($V_{CBO}$)**  | $-50\text{ V}$ max |
| **Continuous Collector Current ($I_C$)**| $-100\text{ mA}$ continuous |
| **DC Current Gain ($h_{FE}$)** | $110\dots 220$ (A) / $200\dots 450$ (B) / $420\dots 800$ (C) |
| **Transition Frequency ($f_T$)** | $300\text{ MHz}$ typ |
| **Power Dissipation ($P_D$)** | $500\text{ mW}$ at $T_A = 25^\circ\text{C}$ |

## Pinout (TO-92 Package)

Looking at the **flat face** of the TO-92 package with leads pointing down:

```
        ┌─────────────┐
        │   BC557B    │  (Flat Package Face)
        └─┬───┬───┬───┘
          1   2   3
          C   B   E
```

| Pin | Name | Description |
|---|---|---|
| 1 | `COLLECTOR` (`C`) | Collector terminal (High-side load output) |
| 2 | `BASE` (`B`) | Base input control terminal (Connect via resistor) |
| 3 | `EMITTER` (`E`) | Emitter terminal (Connect to $+V_{CC}$ positive supply rail) |

> [!IMPORTANT]
> Pinout Differences (BC557 vs 2N3906):
> - **BC557 (European standard):** Pin 1 = Collector, Pin 2 = Base, Pin 3 = Emitter (**C-B-E**).
> - **2N3906 (US standard):** Pin 1 = Emitter, Pin 2 = Base, Pin 3 = Collector (**E-B-C**).

## Gain Classification Suffixes

- **BC557A:** Low DC Current Gain ($h_{FE} = 110 \dots 220$).
- **BC557B:** Medium DC Current Gain ($h_{FE} = 200 \dots 450$) — **Most common kit variant**.
- **BC557C:** High DC Current Gain ($h_{FE} = 420 \dots 800$).

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector Breakdown Voltage| $V_{(BR)CEO}$| -45 | — | — | V | $I_C = -10\text{mA}, I_B = 0$ |
| Emitter Breakdown Voltage | $V_{(BR)EBO}$| -5.0| — | — | V | $I_E = -10\ \mu\text{A}, I_C = 0$ |
| Collector Saturation Volts| $V_{CE(sat)}$| — | -90 | -250 | mV | $I_C = -10\text{mA}, I_B = -0.5\text{mA}$ |
| Base Saturation Voltage | $V_{BE(sat)}$| — | -700| -900 | mV | $I_C = -10\text{mA}, I_B = -0.5\text{mA}$ |

## Common mistakes

- **Reversing Emitter and Collector pins:** Inserting a BC557 with its flat face facing the wrong way connects Collector to $V_{CC}$ and Emitter to Load. The transistor will operate in reverse-active mode with extremely low current gain ($h_{FE} < 5$).
- **Exceeding -100mA continuous collector current:** The BC557 is limited to $100\text{ mA}$. For high-current PNP power switching, use a power PNP transistor (like the TIP127 or BD140).

## Notes

- **BC557 vs BC547:** BC557 is PNP; BC547 is its complementary NPN transistor.
