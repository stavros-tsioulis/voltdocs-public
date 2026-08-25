## Overview

The **CD4007** (CD4007UB / CD4007UBE) is a versatile CMOS transistor array IC manufactured by Texas Instruments and onsemi. Housed in a standard 14-pin through-hole **DIP-14** package, it consists of **three P-channel and three N-channel enhancement-mode MOSFETs** on a single monolithic substrate with unbuffered, directly accessible gate, drain, and source terminals.

Operating across an ultra-wide supply voltage range of **$3.0\text{V}$ to $18.0\text{V}$ DC** with extremely high input impedance ($10^{12}\ \Omega$), the CD4007UB is one of the most famous educational and experimental ICs in electrical engineering. Because the internal transistors can be interconnected flexibly by external jumper wires, it serves as a Swiss-army-knife component for building **custom analog operational amplifiers, crystal oscillators, analog transmission gates, current mirrors, differential amplifiers, Schmitt triggers, and unbuffered CMOS inverters**.

## Quick reference

| | |
|---|---|
| **Device Type** | Dual Complementary Transistor Pair Plus Inverter |
| **Internal MOSFETs** | 3 P-Channel MOSFETs + 3 N-Channel MOSFETs |
| **Package** | 14-pin DIP (DIP-14 / PDIP-14) / 14-pin SOIC |
| **Supply Voltage Range ($V_{DD} - V_{SS}$)** | $3.0\text{ V}$ to $18.0\text{ V}$ DC ($20\text{ V}$ absolute max) |
| **Input Impedance** | $10^{12}\ \Omega$ ($1\text{ T}\Omega$) typical |
| **Gate-to-Source Threshold ($V_{GS(th)}$)**| $\approx 1.5\text{ V}$ (NMOS) / $\approx -1.5\text{ V}$ (PMOS) |
| **Output Drive Current** | $\sim 1.0\text{ mA} \dots 10\text{ mA}$ (dependent on $V_{DD}$) |
| **Propagation Delay ($t_{pd}$)** | $20\text{ ns}$ typ at $10\text{V}$ / $35\text{ ns}$ typ at $5\text{V}$ |

## Internal Transistor Schematic & Pinout (DIP-14)

```
                            ┌───┴───┐
       (PMOS 1 Drain)   D1 1│ 1   14│ VDD (Positive Supply & PMOS Substrate)
      (PMOS 1 Source)   S1 2│       │13 D3 (PMOS 3 Drain)
       (Common Gate)  G1/2 3│ CD4007│12 D3 (NMOS 3 Drain)
       (NMOS 1 Drain)   D1 4│   UB  │11 S3 (NMOS 3 Source)
      (NMOS 1 Source)   S1 5│ DIP-14│10 G3 (Common Gate 3)
      (Inverter Gate)  G_INV 6│     │9  (Center-notch bottom)
           (Ground)    VSS 7│       │8  OUT_INV (Inverter Common Drain)
                            └───────┘
```

### Transistor Connections Table

| Pin | Name | Internal Transistor Terminal |
|---|---|---|
| 1 | `D1_P` | Transistor 1 (PMOS) Drain |
| 2 | `S1_P` | Transistor 1 (PMOS) Source |
| 3 | `G1` | Transistor 1 Gate (Common to PMOS 1 and NMOS 1) |
| 4 | `D1_N` | Transistor 1 (NMOS) Drain |
| 5 | `S1_N` | Transistor 1 (NMOS) Source |
| 6 | `IN_INV`| Inverter Input (Gate of PMOS 2 and NMOS 2) |
| 7 | `VSS` | Negative Supply Reference / NMOS Substrate (Connect to system GND) |
| 8 | `OUT_INV`| Inverter Output (Common Drain of PMOS 2 and NMOS 2) |
| 10 | `G3` | Transistor 3 Gate (Common to PMOS 3 and NMOS 3) |
| 11 | `S3_N` | Transistor 3 (NMOS) Source |
| 12 | `D3_N` | Transistor 3 (NMOS) Drain |
| 13 | `D3_P` | Transistor 3 (PMOS) Drain |
| 14 | `VDD` | Positive Supply / PMOS Substrate (Connect to most positive rail) |

*(Note: Transistor 2 PMOS Source is internally hardwired to Pin 14 $V_{DD}$, and NMOS Source is hardwired to Pin 7 $V_{SS}$; Transistor 3 PMOS Source is internally hardwired to Pin 14 $V_{DD}$).*

## Common Circuit Configurations

### 1. High-Gain Linear Inverting Analog Amplifier
By adding negative feedback across the unbuffered inverter pair, the CD4007 acts as a high-speed linear amplifier:
```
           ┌──────────[ Feedback: 1MΩ Resistor ]──────────┐
           │                                              │
  Input ───┴───[ 100kΩ ]───► [Pin 6: IN_INV]              │
                              CD4007UB                    ├────► Output
                             [Pin 8: OUT_INV] ────────────┘
```

### 2. High-Frequency Crystal Oscillator
```
  [Pin 6: IN_INV] ───┬───[ Crystal: 32.768kHz - 10MHz ]───┬───► [Pin 8: OUT_INV]
                     │                                    │
               [ 22pF Cap ]                          [ 22pF Cap ]
                     │                                    │
                    GND                                  GND
```

## Common mistakes

- **Leaving Pin 14 ($V_{DD}$) or Pin 7 ($V_{SS}$) disconnected:** Pin 14 and Pin 7 serve as the bulk substrate bias connections for all internal PMOS and NMOS wells. If they are not connected to the absolute highest and lowest DC voltages in the circuit, substrate parasitic PN diodes will forward bias and cause chip latchup.
- **Unused gate pins left floating:** As high-impedance CMOS inputs ($10^{12}\ \Omega$), floating gates pick up static charge and cause excessive shoot-through current dissipation between $V_{DD}$ and $V_{SS}$. Tie unused gate pins (Pins 3, 6, 10) to $V_{SS}$ (Ground) or $V_{DD}$.

## Notes

- **"UB" Suffix:** Denotes **Unbuffered** single-stage CMOS topology, providing linear analog characteristics ideal for amplifiers, active filters, and oscillators compared to buffered (B-series) digital gates.
