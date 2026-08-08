## Overview

The **2N3904** is the quintessential general-purpose NPN Bipolar Junction Transistor (BJT) manufactured by ON Semiconductor, STMicroelectronics, and Fairchild. Included in virtually all beginner electronics kits and breadboard prototyping assortments, it is designed for low-power amplification and medium-speed digital switching applications.

Housed in a 3-pin **TO-92 plastic package**, the 2N3904 is rated for a collector-emitter breakdown voltage ($V_{CEO}$) of **$40\text{ Volts}$** and continuous collector current ($I_C$) of **$200\text{ mA}$**. Its complementary PNP counterpart is the **2N3906**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | General-Purpose NPN Bipolar Junction Transistor (BJT) |
| **Package** | TO-92 (Flat face front, leads pointing down) / SOT-23 (MMBT3904) |
| **Pinout (TO-92)** | Pin 1: Emitter (`E`), Pin 2: Base (`B`), Pin 3: Collector (`C`) — **E-B-C** |
| **Collector-Emitter Voltage ($V_{CEO}$)**| $40\text{ V}$ max |
| **Collector-Base Voltage ($V_{CBO}$)**  | $60\text{ V}$ max |
| **Continuous Collector Current ($I_C$)**| $200\text{ mA}$ continuous |
| **DC Current Gain ($h_{FE}$)** | $100 \dots 300$ at $I_C = 10\text{mA}, V_{CE} = 1.0\text{V}$ |
| **Transition Frequency ($f_T$)** | $300\text{ MHz}$ min |
| **Power Dissipation ($P_D$)** | $625\text{ mW}$ at $T_A = 25^\circ\text{C}$ |

## Pinout (TO-92 Package)

Looking at the **flat face** of the TO-92 package with leads pointing down:

```
        ┌─────────────┐
        │   2N3904    │  (Flat Package Face)
        └─┬───┬───┬───┘
          1   2   3
          E   B   C
```

| Pin | Name | Description |
|---|---|---|
| 1 | `EMITTER` (`E`) | Emitter terminal (Ground reference 0 V) |
| 2 | `BASE` (`B`) | Base input control terminal (Connect via resistor) |
| 3 | `COLLECTOR` (`C`) | Collector terminal (Low-side load connection) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector Breakdown Voltage| $V_{(BR)CEO}$| 40 | — | — | V | $I_C = 1.0\text{mA}, I_B = 0$ |
| Emitter Breakdown Voltage | $V_{(BR)EBO}$| 6.0 | — | — | V | $I_E = 10\ \mu\text{A}, I_C = 0$ |
| Collector Saturation Volts| $V_{CE(sat)}$| — | 0.2 | 0.3 | V | $I_C = 50\text{mA}, I_B = 5.0\text{mA}$ |
| Base Saturation Voltage | $V_{BE(sat)}$| 0.65| — | 0.95| V | $I_C = 50\text{mA}, I_B = 5.0\text{mA}$ |

## Low-Side NPN Switch Calculation

To drive a small $50\text{ mA}$ relay or indicator LED from a $3.3\text{V}$ or $5.0\text{V}$ MCU GPIO pin:

$$ R_B = \frac{V_{MCU} - 0.7\text{V}}{I_B} \quad \text{where } I_B = \frac{I_C}{10} = 5.0\text{ mA} $$

- For $5.0\text{V}$ MCU: $R_B = \frac{4.3\text{V}}{0.005\text{A}} = 860\ \Omega \implies \text{Use } 1\ \text{k}\Omega$.
- For $3.3\text{V}$ MCU: $R_B = \frac{2.6\text{V}}{0.005\text{A}} = 520\ \Omega \implies \text{Use } 470\ \Omega \text{ or } 560\ \Omega$.

## Common mistakes

- **Confusing 2N3904 (E-B-C) and BC547 (C-B-E) pinouts:** Although both are TO-92 NPN transistors, **2N3904 is E-B-C**, whereas **BC547 is C-B-E**. Inserting a BC547 into a circuit designed for 2N3904 reverses the Collector and Emitter pins.
- **Exceeding 200mA collector current:** Attempting to drive solenoids or motors drawing $>200\text{ mA}$ exceeds the 2N3904 rating. Use a 2N2222 ($800\text{mA}$) or an N-channel MOSFET instead.

## Notes

- **2N3904 vs 2N3906:** 2N3904 is NPN; 2N3906 is the complementary PNP transistor.
