## Overview

The **OPA2140** is a precision, low-noise, high-speed JFET-input dual operational amplifier manufactured by Texas Instruments under the Burr-Brown product line. Engineered using TI's proprietary e-Trim™ technology, it delivers a rare combination of exceptional DC precision (ultra-low $120\text{ }\mu\text{V}$ maximum input offset voltage and $1\text{ }\mu\text{V/}^\circ\text{C}$ drift) and outstanding dynamic AC performance ($11\text{ MHz}$ gain bandwidth and $20\text{ V/}\mu\text{s}$ slew rate).

Featuring an ultra-low input bias current of just $\pm 0.5\text{ pA}$ (typically) and $10\text{ pA}$ maximum, along with rail-to-rail output swing and low voltage noise of $5.1\text{ nV/}\sqrt{\text{Hz}}$ at $1\text{ kHz}$, the OPA2140 is widely used in high-impedance medical instrumentation, precision photodiode transimpedance amplifiers (TIA), high-end audiophile preamplifiers, 16-bit to 24-bit data acquisition systems, and laboratory measurement bridges.

## Quick reference

| | |
|---|---|
| **Function** | Precision Low-Noise JFET-Input Dual Operational Amplifier |
| **Supply Voltage (Single Supply)** | $4.5\text{ V}$ to $36.0\text{ V}$ DC |
| **Supply Voltage (Split Supply)** | $\pm 2.25\text{ V}$ to $\pm 18.0\text{ V}$ DC |
| **Input Offset Voltage ($V_{OS}$)** | $120\text{ }\mu\text{V}$ max ($30\text{ }\mu\text{V}$ typ) |
| **Input Offset Drift ($dV_{OS}/dT$)** | $1.0\text{ }\mu\text{V/}^\circ\text{C}$ max ($0.35\text{ }\mu\text{V/}^\circ\text{C}$ typ) |
| **Input Bias Current ($I_B$)** | $10\text{ pA}$ max ($0.5\text{ pA}$ typ at $25^\circ\text{C}$) |
| **Voltage Noise Density ($e_n$)** | $5.1\text{ nV/}\sqrt{\text{Hz}}$ at $1\text{ kHz}$ |
| **Gain Bandwidth Product (GBW)** | $11.0\text{ MHz}$ |
| **Slew Rate (SR)** | $20.0\text{ V/}\mu\text{s}$ |
| **Output Type** | Rail-to-Rail Output (RRO) |
| **Quiescent Current** | $1.8\text{ mA}$ per channel typ |
| **Packages** | 8-pin SOIC (D), VSSOP-8 (DGK) |

## Pin configuration

### 8-Pin SOIC / VSSOP Package

```
               ┌──────────┐
        OUT A ─┤ 1      8 ├─ V+
       -IN A  ─┤ 2      7 ├─ OUT B
       +IN A  ─┤ 3      6 ├─ -IN B
          V-  ─┤ 4      5 ├─ +IN B
               └──────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `OUT A` | Analog Output | Op-amp A output terminal |
| 2 | `-IN A` | Analog Input | Op-amp A inverting input |
| 3 | `+IN A` | Analog Input | Op-amp A non-inverting input |
| 4 | `V-` | Power Supply | Negative supply voltage ($-\text{V}_{S}$) or Ground in single-supply mode |
| 5 | `+IN B` | Analog Input | Op-amp B non-inverting input |
| 6 | `-IN B` | Analog Input | Op-amp B inverting input |
| 7 | `OUT B` | Analog Output | Op-amp B output terminal |
| 8 | `V+` | Power Supply | Positive supply voltage ($+\text{V}_{S}$) |

## Functional description

The OPA2140 combines high-voltage precision JFET transistors with modern laser-trimmed CMOS current mirrors:

- **JFET Input Stage:** True JFET inputs provide input impedances of $10^{13}\text{ }\Omega$, virtually eliminating input bias current errors even when interfaced with high-impedance sources (such as piezoelectric sensors, pH probes, or reverse-biased photodiodes). The inputs do not experience phase reversal when driven to the negative supply rail.
- **Common-Mode Range:** The input common-mode range extends from $(V-) + 3.5\text{ V}$ to $(V+) - 0.1\text{ V}$ over the full operating temperature range.
- **Rail-to-Rail Output:** The class-AB output stage swings to within $20\text{ mV}$ of either supply rail under a $10\text{ k}\Omega$ load, maximizing dynamic range in single-supply 5V and 12V measurement systems.
- **No Phase Reversal:** Internal protection circuitry prevents output phase reversal when an input exceeds the specified common-mode range.

## Absolute maximum ratings

> [!WARNING]
> Stresses beyond these ratings cause permanent damage. Functional operation at these limits is not guaranteed.

| Parameter | Rating | Unit |
|---|---|---|
| Supply Voltage ($V_S = V+ - V-$) | 40 | V |
| Differential Input Voltage | $\pm 40$ | V |
| Input Voltage Range | $(V-) - 0.5$ to $(V+) + 0.5$ | V |
| Output Short-Circuit Duration | Continuous to either supply rail | — |
| Operating Temperature Range | -40 to 125 | °C |
| Junction Temperature ($T_J$) | 150 | °C |
| Storage Temperature Range | -65 to 150 | °C |

## Electrical characteristics

$V_S = \pm 15\text{ V}$, $R_L = 2\text{ k}\Omega$, $T_A = 25^\circ\text{C}$, unless otherwise specified.

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Offset Voltage | $V_{OS}$ | — | $\pm 30$ | $\pm 120$ | $\mu\text{V}$ | $V_{CM} = 0\text{ V}$ |
| Input Offset Voltage Drift | $dV_{OS}/dT$ | — | $\pm 0.35$ | $\pm 1.0$ | $\mu\text{V/}^\circ\text{C}$ | $T_A = -40^\circ\text{C}$ to $+125^\circ\text{C}$ |
| Input Bias Current | $I_B$ | — | $\pm 0.5$ | $\pm 10$ | pA | $V_{CM} = 0\text{ V}$ |
| Input Offset Current | $I_{OS}$ | — | $\pm 0.2$ | $\pm 5$ | pA | $V_{CM} = 0\text{ V}$ |
| Input Voltage Noise Density | $e_n$ | — | 5.1 | — | $\text{nV/}\sqrt{\text{Hz}}$ | $f = 1\text{ kHz}$ |
| Low-Frequency 1/f Noise | $e_{n,p-p}$ | — | 250 | — | $\text{nV}_{p-p}$ | $0.1\text{ Hz}$ to $10\text{ Hz}$ |
| Gain Bandwidth Product | $\text{GBW}$ | — | 11.0 | — | MHz | $C_L = 10\text{ pF}$ |
| Slew Rate | $\text{SR}$ | — | 20.0 | — | $\text{V/}\mu\text{s}$ | $G = +1$ |
| Common-Mode Rejection Ratio | $\text{CMRR}$ | 110 | 120 | — | dB | $(V-) + 3.5\text{ V} \le V_{CM} \le (V+) - 1.5\text{ V}$ |
| Power Supply Rejection Ratio | $\text{PSRR}$ | 110 | 120 | — | dB | $V_S = \pm 2.25\text{ V}$ to $\pm 18\text{ V}$ |
| Total Harmonic Distortion + Noise | $\text{THD+N}$ | — | 0.00005 | — | % | $f = 1\text{ kHz}, G = 1, V_O = 3\text{ V}_{RMS}$ |
| Quiescent Current (per channel) | $I_Q$ | — | 1.8 | 2.0 | mA | $I_O = 0$ |

## Typical application

### Precision High-Speed Photodiode Transimpedance Amplifier (TIA)

```
        Photodiode
        (Reverse-Biased)
            ┌──┤◄├──┐
            │       │
           GND      ├───[ Rf = 1MΩ ]────┬────────► Output Voltage Vout
                    │       │           │
                    │   ┌───┴───┐       │
                    └───┤ -IN   │       │
                        │ OPA   ├───────┘
                    ┌───┤ +IN   │
                    │   └───────┘
                   GND
```

Due to the sub-pA input bias current and $11\text{ MHz}$ bandwidth, the OPA2140 produces negligible offset error from the large $1\text{ M}\Omega$ feedback resistor ($V_{offset} = I_B \times R_f = 0.5\text{ pA} \times 1\text{ M}\Omega = 0.5\text{ }\mu\text{V}$) while preserving high signal bandwidth and minimal phase lag.

## Common mistakes

- **Omitting High-Frequency Power Supply Decoupling:** Due to its wide $11\text{ MHz}$ bandwidth and high $20\text{ V/}\mu\text{s}$ slew rate, poor power supply bypassing leads to parasitic oscillation. Place low-ESR $0.1\text{ }\mu\text{F}$ ceramic surface-mount capacitors within $3\text{ mm}$ of pins 4 and 8 directly to a solid ground plane.
- **Driving Heavy Capacitive Loads Directly:** Like many high-speed precision amplifiers, driving large capacitive loads ($C_L > 100\text{ pF}$) directly from the output pin causes phase lag and ringing. Add a small series isolation resistor ($22\text{ }\Omega$ to $50\text{ }\Omega$) between the op-amp output pin and the capacitive load.
- **Surface Contamination / Leakage on PCB Traces:** With an input bias current of only $0.5\text{ pA}$, residual solder flux or humidity on PCB surfaces can create leakage currents that dwarf the amplifier's input bias current. Implement guard rings around the inverting input pins (`-IN`) tied to the non-inverting input potential.
- **Violating Positive Common-Mode Input Limit:** The input common-mode range stops $1.5\text{ V}$ below the positive supply rail ($(V+) - 1.5\text{ V}$). Attempting to drive inputs all the way to $V+$ in single-supply configurations will distort the signal.

## Notes

- **Family Variants:** **OPA140** (single op-amp in SOT-23/SOIC-8), **OPA2140** (dual op-amp in SOIC-8/VSSOP-8), and **OPA4140** (quad op-amp in SOIC-14/TSSOP-14).
- **Comparison with OPA2134:** The OPA2140 is a modern upgrade offering substantially lower offset voltage ($120\text{ }\mu\text{V}$ vs $2000\text{ }\mu\text{V}$), lower input bias current ($10\text{ pA}$ vs $50\text{ pA}$), wider bandwidth ($11\text{ MHz}$ vs $8\text{ MHz}$), and rail-to-rail output swing.
