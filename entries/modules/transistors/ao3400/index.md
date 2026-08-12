## Overview

The **AO3400** (AO3400A) is an ultra-popular N-channel logic-level power MOSFET manufactured by Alpha & Omega Semiconductor. Packaged in a subminiature **SOT-23 enclosure**, it delivers exceptionally high current capability and extremely low $R_{DS(on)}$ resistance in an SMD footprint.

Featuring a drain-source breakdown voltage of **$30\text{ Volts}$**, continuous drain current handling up to **$5.7\text{ Amps}$**, and an $R_{DS(on)}$ of just **$33\text{ m}\Omega$ at $4.5\text{V}$** (and $52\text{ m}\Omega$ at $2.5\text{V}$), the AO3400 is widely used in battery-powered electronics, Li-ion protection circuits, high-current load switches, motor drivers, and LED strip controllers driven by 3.3V and 2.5V microcontrollers.

## Quick reference

| | |
|---|---|
| **Transistor Type** | N-Channel Logic-Level Enhancement Mode MOSFET |
| **Package** | SOT-23 (3-pin SMD) |
| **Drain-Source Voltage ($V_{DSS}$)**| $30\text{ V}$ max |
| **Continuous Drain Current ($I_D$)**| $5.7\text{ A}$ at $V_{GS} = 10\text{V}$ ($5.0\text{ A}$ at $4.5\text{V}$, $2.8\text{ A}$ at $2.5\text{V}$) |
| **Gate Threshold Voltage ($V_{GS(th)}$)**| $0.6\text{ V}$ min to $1.5\text{ V}$ max ($1.0\text{ V}$ typical) |
| **On-State Resistance ($R_{DS(on)}$)**| $28\text{ m}\Omega$ at $10\text{V}$ / $33\text{ m}\Omega$ at $4.5\text{V}$ / $52\text{ m}\Omega$ at $2.5\text{V}$ |
| **Pulsed Drain Current ($I_{DM}$)**| $30\text{ A}$ |
| **Total Power Dissipation** | $1.4\text{ W}$ ($T_A = 25^\circ\text{C}$) |

## Pinout (SOT-23 Package)

Looking at the top of the SOT-23 surface-mount component with single lead on top:

```
               ┌─────────┐
               │    3    │  (DRAIN)
               └─┐     ┌─┘
                 │AO340│
               ┌─┘     └─┐
               │ 1     2 │
               └─────────┘
            (GATE)   (SOURCE)
```

| Pin | Name | Description |
|---|---|---|
| 1 | `GATE` (`G`) | Gate control input (Connect to MCU GPIO pin) |
| 2 | `SOURCE` (`S`) | Source terminal (Ground reference 0 V) |
| 3 | `DRAIN` (`D`) | Drain terminal (Low-side load connection) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Drain-Source Breakdown Volts| $V_{(BR)DSS}$| 30 | — | — | V | $V_{GS} = 0\text{V}, I_D = 250\ \mu\text{A}$ |
| Gate Threshold Voltage | $V_{GS(th)}$| 0.6 | 1.0 | 1.5 | V | $V_{DS} = V_{GS}, I_D = 250\ \mu\text{A}$ |
| On-Resistance ($V_{GS}=10\text{V}$)| $R_{DS(on)}$| — | 22 | 28 | mΩ | $V_{GS} = 10\text{V}, I_D = 5.7\text{A}$ |
| On-Resistance ($V_{GS}=4.5\text{V}$)| $R_{DS(on)}$| — | 26 | 33 | mΩ | $V_{GS} = 4.5\text{V}, I_D = 5.0\text{A}$ |
| On-Resistance ($V_{GS}=2.5\text{V}$)| $R_{DS(on)}$| — | 38 | 52 | mΩ | $V_{GS} = 2.5\text{V}, I_D = 2.8\text{A}$ |
| Total Gate Charge | $Q_g$ | — | 7.2 | 10.0 | nC | $V_{GS} = 4.5\text{V}, V_{DS} = 15\text{V}$ |

## Common mistakes

- **Exceeding package thermal dissipation limit ($1.4\text{ W}$):** While the die can handle up to $5.7\text{ A}$, running continuous high currents on a small PCB without sufficient copper pour heatsink area can cause thermal throttling.
- **Applying Gate voltage $> 12\text{V}$:** The absolute maximum Gate-Source voltage ($V_{GS}$) rating for the AO3400 is **$\pm 12\text{V}$** (unlike standard power FETs rated for $\pm 20\text{V}$). Driving the gate directly from $15\text{V}$ or $24\text{V}$ rails destroys the gate oxide layer.

## Notes

- **AO3400 vs 2N7002:** AO3400 has $33\text{ m}\Omega$ $R_{DS(on)}$ and $5.7\text{ A}$ rating; 2N7002 has $5.0\ \Omega$ $R_{DS(on)}$ and $115\text{ mA}$ rating. AO3400 is suited for heavy load switching; 2N7002 is for signal switching.
