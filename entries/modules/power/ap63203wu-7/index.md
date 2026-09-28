## Overview

The **AP63203WU-7** (commonly referred to as the **AP63203**) is a fully integrated fixed **$+3.3\text{ V}$**, 2A synchronous step-down (buck) DC-DC converter manufactured by Diodes Incorporated. Housed in an ultra-compact 6-lead TSOT26 package, it is specifically optimized to supply modern $3.3\text{ V}$ microcontrollers (such as ESP32, STM32, RP2040, and ARM Cortex processors) and RF transceivers directly from wide industrial supply voltages ($4.5\text{ V}$ to $32.0\text{ V}$ DC).

As part of Diodes Incorporated's AP6320x family, the AP63203 distinguishes itself from the adjustable AP63200 in two vital ways:
1. **Internal Precision Resistor Divider:** The feedback network is integrated and factory-laser-trimmed on-chip. Pin 1 connects directly to the $+3.3\text{ V}$ output rail (`VFB` / `VOUT`), eliminating external feedback resistors, reducing component count to just four external parts ($C_{IN}$, $L$, $C_{OUT}$, $C_{BST}$), and preventing external resistor tolerance drift.
2. **Elevated Switching Frequency ($1.1\text{ MHz}$):** Operating at more than double the frequency of the AP63200 ($1.1\text{ MHz}$ vs. $500\text{ kHz}$), the AP63203 enables the use of smaller inductors ($2.2\ \mu\text{H}$ to $3.3\ \mu\text{H}$) and ultra-compact 0805/0603 ceramic capacitors, making it one of the smallest point-of-load (POL) buck solutions in the industry.

The device includes integrated **Frequency Spread Spectrum (FSS)** ($\pm 6\%$ jitter) and proprietary gate-driver ringing reduction for effortless compliance with CISPR 25 Class 5 EMI limits, alongside ultra-low $22\ \mu\text{A}$ light-load quiescent current in PFM mode.

## Quick reference

| Parameter | Value | Notes |
|---|---|---|
| **Converter Architecture** | Synchronous Step-Down (Buck) | Integrated high-side and low-side MOSFETs |
| **Input Supply Voltage ($V_{IN}$)** | $3.8\text{ V}$ to $32.0\text{ V}$ DC | Absolute maximum $35.0\text{ V}$ |
| **Fixed Output Voltage ($V_{OUT}$)** | $+3.3\text{ V}$ DC ($\pm 2.5\%$) | Internally trimmed; no external resistors |
| **Continuous Output Current** | $2.0\text{ A}$ | Across industrial temperature range |
| **Switching Frequency ($f_{SW}$)** | $1.1\text{ MHz}$ nominal | Frequency Spread Spectrum ($\pm 6\%$ jitter) |
| **Quiescent Current ($I_Q$)** | $22\ \mu\text{A}$ typical | Light-load PFM operation |
| **Shutdown Current ($I_{SD}$)** | $1.0\ \mu\text{A}$ typical | When `EN` pin is grounded |
| **MOSFET On-Resistance** | $125\text{ m}\Omega$ (HS) / $68\text{ m}\Omega$ (LS) | Synchronous rectification |
| **Package** | TSOT26 (`WU-7` = Tape & Reel) | $2.9\times 2.8\times 1.0\text{ mm}$ footprint |

## Terminals

The AP63203 shares the 6-lead TSOT26 footprint, with Pin 1 acting as the direct output sense line:

```
          +---+--+---+
   VOUT --| 1    6 |-- BST
     EN --| 2    5 |-- SW
    VIN --| 3    4 |-- GND
          +----------+
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VOUT` (`FB`) | Power / Sense | Output voltage feedback sensing. Connect directly to regulated $+3.3\text{ V}$ rail. |
| 2 | `EN` | Digital Input | Enable control input. Pull High ($>1.2\text{ V}$) to enable, Low ($<0.4\text{ V}$) to shut down. |
| 3 | `VIN` | Power Input | Main power input rail ($+3.8\text{ V}$ to $+32.0\text{ V}$ DC). Bypass with ceramic capacitor. |
| 4 | `GND` | Ground | Circuit ground reference ($0\text{ V}$). |
| 5 | `SW` | Switching Output | Inductor switching node. Connect to output inductor and bootstrap capacitor. |
| 6 | `BST` | Bootstrap Input | High-side gate driver boost supply. Connect $100\text{ nF}$ ceramic capacitor between `BST` and `SW`. |

## The technical core

### Linear regulator replacement economics

Supplying $3.3\text{ V}$ at $500\text{ mA}$ from a standard industrial $24\text{ V}$ DC rail using a linear LDO (such as an AMS1117-3.3):
- **Power Dissipation in Linear Regulator:**
  $$ P_D = (V_{IN} - V_{OUT}) \times I_L = (24\text{ V} - 3.3\text{ V}) \times 0.5\text{ A} = 10.35\text{ W} $$
  This requires a massive heatsink and wastes over $86\%$ of the energy as heat.
- **Power Dissipation in AP63203:**
  At $91\%$ conversion efficiency:
  $$ P_{loss} = (3.3\text{ V} \times 0.5\text{ A}) \times \left(\frac{1}{0.91} - 1\right) = 1.65\text{ W} \times 0.0989 \approx 0.163\text{ W} $$
  The AP63203 operates completely cool to the touch on a standard PCB with no heatsink.

### Electrical specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Voltage Range | $V_{IN}$ | 3.8 | 12.0 / 24.0 | 32.0 | V | Operating range |
| Regulated Output Voltage | $V_{OUT}$ | 3.217 | 3.300 | 3.383 | V | $V_{IN} = 4.5 \dots 32\text{ V}$, $I_O = 0 \dots 2\text{ A}$ |
| High-Side Switch On-Resistance | $R_{DS(ON)\_H}$ | — | 125 | 170 | $\text{m}\Omega$ | $V_{IN} = 12\text{ V}$ |
| Low-Side Switch On-Resistance | $R_{DS(ON)\_L}$ | — | 68 | 95 | $\text{m}\Omega$ | $V_{IN} = 12\text{ V}$ |
| Nominal Switching Frequency | $f_{SW}$ | 0.95 | 1.10 | 1.25 | MHz | Internal clock |
| FSS Jitter Range | $\Delta f_{FSS}$ | — | $\pm 6$ | — | % | Spread spectrum modulation |
| Quiescent Current (PFM) | $I_Q$ | — | 22 | 40 | µA | No load, $V_{IN} = 12\text{ V}$ |
| Shutdown Current | $I_{SD}$ | — | 1.0 | 3.0 | µA | $V_{EN} = 0\text{ V}$ |
| Peak Switch Current Limit | $I_{PEAK}$ | 2.5 | 3.0 | 3.6 | A | High-side current trip |
| Thermal Shutdown Temp | $T_{TSD}$ | — | 160 | — | °C | Auto-recovery |

## Usage

### Minimal 4-component application circuit

Because the feedback divider is integrated internally, the entire circuit requires only four passive components:

```
       +4.5V to +32V DC
  VIN o--------+-------------------------+
               |                         |
              === C_IN (10uF)            |
              --- 50V Ceramic            |
               |                         |
               |        +-------+        |
               |      3 |       | 6      |
               +--------|VIN BST|--------+---||---+ (100nF C_BST)
               |      2 |       | 5               |
   EN o--------+--------|EN   SW|-----------------+----CCCC----+------> +3.3V DC (2.0A)
                        |       |                      L1 (2.2uH|
                        |   VOUT|-------------------------------+
                        |       | 1                             |
                        |    GND|                              === C_OUT (22uF x 2)
                        +---+---+                              --- Ceramic
                            |                                   |
  GND o---------------------+-----------------------------------+------> 0V GND
```

#### Component specifications for 1.1 MHz operation:
- **Inductor ($L_1$):** $2.2\ \mu\text{H}$ to $3.3\ \mu\text{H}$ shielded power inductor with $I_{SAT} \ge 3.0\text{ A}$ (e.g., Würth 74438335022 or Coilcraft XFL4020-222ME).
- **Input Capacitor ($C_{IN}$):** $10\ \mu\text{F}$ 50V X7R ceramic placed within $2\text{ mm}$ of pins 3 and 4.
- **Output Capacitors ($C_{OUT}$):** Two $22\ \mu\text{F}$ 10V or 16V X7R ceramic capacitors in parallel.
- **Bootstrap Capacitor ($C_{BST}$):** $100\text{ nF}$ 16V ceramic capacitor between pins 5 and 6.

## Common mistakes

- **Attempting to add external feedback resistors:** Pin 1 is connected to the internal feedback node. Connecting an external resistor divider will offset the trimmed voltage or prevent regulation. Wire Pin 1 directly to the $+3.3\text{ V}$ output node.
- **Using large $10\ \mu\text{H}$ or $22\ \mu\text{H}$ inductors:** Because the AP63203 switches at $1.1\text{ MHz}$, oversized inductors degrade transient response and increase DC resistance. Use $2.2\ \mu\text{H}$ or $3.3\ \mu\text{H}$.
- **Input capacitor placement:** High-frequency switching loop currents flow through $C_{IN} \to \text{Pin 3} \to \text{Pin 4} \to C_{IN}$. Placing $C_{IN}$ on the opposite side of the PCB with vias will cause excessive voltage ringing and EMI.

## Notes

- **Current Rating Note:** Some distributor listings inadvertently designate the AP63203 as "3A" due to its peak current trip threshold ($3.0\text{ A}$ typical). The rated continuous operating current is $2.0\text{ A}$. For applications requiring $3.0\text{ A}$ continuous current, refer to Diodes Incorporated's companion **AP63300** family.
