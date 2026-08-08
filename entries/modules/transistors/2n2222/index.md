## Overview

The **2N2222** (and improved **2N2222A**) is arguably the most famous general-purpose NPN Bipolar Junction Transistor (BJT) in electronic engineering. Designed by Motorola in 1962, it is bundled in virtually every electronics component starter kit (Elegoo, SunFounder, SparkFun, Adafruit).

Housed in either a metal **TO-18 can** or a plastic **TO-92 package** (often designated P2N2222A / PN2222A), the 2N2222 is rated for collector-emitter breakdown voltages up to **$40\text{ Volts}$** and high continuous collector currents up to **$800\text{ mA}$** with a fast $300\text{ MHz}$ transition frequency. It serves as a low-side switch for driving relays, small DC motors, buzzers, and LEDs from microcontroller GPIO pins.

## Quick reference

| | |
|---|---|
| **Transistor Type** | General-Purpose NPN Bipolar Junction Transistor (BJT) |
| **Package** | TO-18 Metal Can (2N2222A) / TO-92 Plastic (PN2222A / P2N2222A) |
| **Collector-Emitter Voltage ($V_{CEO}$)**| $40\text{ V}$ max (2N2222A) / $30\text{ V}$ max (2N2222) |
| **Collector-Base Voltage ($V_{CBO}$)**  | $75\text{ V}$ max (2N2222A) |
| **Continuous Collector Current ($I_C$)**| $800\text{ mA}$ continuous ($1.0\text{ A}$ peak pulse) |
| **DC Current Gain ($h_{FE}$)** | $100 \dots 300$ at $I_C = 150\text{mA}, V_{CE} = 10\text{V}$ |
| **Transition Frequency ($f_T$)** | $300\text{ MHz}$ min (High speed switching/RF) |
| **Collector Saturation Volts ($V_{CE(sat)}$)**| $0.3\text{ V}$ max at $I_C = 150\text{mA}, I_B = 15\text{mA}$ |

## Pinout (TO-92 vs TO-18 Package Comparison)

Looking at the **flat face** of the plastic TO-92 package with leads pointing down:

```
        ┌─────────────┐
        │   2N2222A   │  (Flat Package Face)
        └─┬───┬───┬───┘
          1   2   3
          E   B   C
```

| Pin | Name | Description |
|---|---|---|
| 1 | `EMITTER` (`E`) | Emitter terminal (Ground reference 0 V) |
| 2 | `BASE` (`B`) | Base control input terminal (Connect via current limiting resistor) |
| 3 | `COLLECTOR` (`C`) | Collector terminal (Low-side load connection) |

> [!WARNING]
> TO-92 Variant Pinout Warning (2N2222 vs P2N2222A):
> - **Standard 2N2222 / PN2222A (TO-92):** Emitter - Base - Collector (**E-B-C**).
> - **ON Semi P2N2222A (TO-92):** Collector - Base - Emitter (**C-B-E**).
> - Always check pin ordering with a multimeter component tester before soldering.

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector Breakdown Voltage| $V_{(BR)CEO}$| 40 | — | — | V | $I_C = 10\text{mA}, I_B = 0$ |
| Emitter Breakdown Voltage | $V_{(BR)EBO}$| 6.0 | — | — | V | $I_E = 10\ \mu\text{A}, I_C = 0$ |
| Base-Emitter Saturation | $V_{BE(sat)}$| 0.6 | — | 1.2 | V | $I_C = 150\text{mA}, I_B = 15\text{mA}$ |
| Collector Cutoff Current | $I_{CEX}$ | — | — | 10 | nA | $V_{CE} = 60\text{V}, V_{EB(off)} = 3.0\text{V}$ |
| Power Dissipation | $P_D$ | — | — | 625 | mW | $T_A = 25^\circ\text{C}$ (TO-92) |

## Standard Low-Side NPN Switching Circuit

To use the 2N2222 as a saturated low-side switch driving a $100\text{ mA}$ relay from a $5\text{V}$ Arduino GPIO pin:

1. **Calculate Base Current ($I_B$):** For saturation, set $I_B \approx \frac{I_C}{10} = \frac{100\text{mA}}{10} = 10\text{ mA}$.
2. **Calculate Base Resistor ($R_B$):**

$$ R_B = \frac{V_{GPIO} - V_{BE}}{I_B} = \frac{5.0\text{V} - 0.7\text{V}}{0.01\text{A}} = 430\ \Omega \quad (\text{Use standard } 470\ \Omega \text{ or } 1\text{ k}\Omega \text{ resistor}) $$

```
        +5V - 12V Load Supply Rail
             │
        [ 5V Relay / Motor Load ] ─── (Flyback Diode)
             │
        [Pin 3: COLLECTOR]
         2N2222A
        [Pin 1: EMITTER] ─── GND
             │
   MCU ── [ R_B = 1kΩ ] ─── [Pin 2: BASE]
```

## Common mistakes

- **Connecting base pin directly to microcontroller GPIO without a resistor:** Connecting a GPIO output pin directly to the Base pin creates a short circuit through the internal $V_{BE}$ PN diode ($\sim 0.7\text{V}$), destroying the MCU pin. Always place a $220\ \Omega \dots 1\ \text{k}\Omega$ resistor in series with the Base.
- **Using 2N2222 instead of a logic-level MOSFET for high currents (>500mA):** At high currents ($>500\text{mA}$), BJTs require significant base drive current ($50\text{mA}+$) and drop $0.3\text{V} \dots 1.0\text{V}$ $V_{CE(sat)}$, leading to excessive thermal heating. For loads $>500\text{mA}$, prefer an N-channel logic-level MOSFET.

## Notes

- **2N2222 vs 2N3904 vs BC547:** 2N2222 handles up to $800\text{mA}$ continuous current; 2N3904 handles up to $200\text{mA}$; BC547 handles up to $100\text{mA}$ (European pinout C-B-E).
