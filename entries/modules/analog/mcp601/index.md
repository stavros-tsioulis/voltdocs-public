## Overview

The **MCP601** (MCP601-I/P, MCP601T-I/OT) is a single, low-power, general-purpose operational amplifier manufactured by Microchip Technology. Fabricated on an advanced CMOS process, the MCP601 is optimized for battery-powered, single-supply systems operating from **$2.7\text{ V}$ to $6.0\text{ V}$** DC.

The amplifier provides a full **rail-to-rail output swing** (driving within $15\text{ mV}$ of either supply rail with high-impedance loads), a wide gain-bandwidth product of **$2.8\text{ MHz}$**, and a respectable **$2.3\text{ V}/\mu\text{s}$** slew rate, all while consuming just **$230\,\mu\text{A}$** of quiescent supply current. With an ultra-low input bias current of only **$1\text{ pA}$** typical, the MCP601 is extensively used in high-impedance sensor signal conditioning, portable medical devices, battery monitors, photodiode transimpedance amplifiers, and active anti-aliasing filters.

## Quick reference

| | |
|---|---|
| **Op-Amp Channels** | 1 (Single Op-Amp) |
| **Supply Voltage Range ($V_{DD}$)** | $2.7\text{ V}$ to $6.0\text{ V}$ Single Supply (or $\pm 1.35\text{ V} \dots \pm 3.0\text{ V}$ Split) |
| **Gain-Bandwidth Product ($GBW$)** | $2.8\text{ MHz}$ typical |
| **Slew Rate ($SR$)** | $2.3\text{ V}/\mu\text{s}$ typical |
| **Input Bias Current ($I_B$)** | $1\text{ pA}$ typical ($100\text{ pA}$ max at $85^\circ\text{C}$) |
| **Input Offset Voltage ($V_{OS}$)** | $\pm 0.7\text{ mV}$ typical ($\pm 2.0\text{ mV}$ max) |
| **Output Swing Range** | Rail-to-rail ($V_{OL} = V_{SS} + 15\text{ mV}$, $V_{OH} = V_{DD} - 15\text{ mV}$ at $R_L = 25\text{ k}\Omega$) |
| **Input Common-Mode Range** | $V_{SS} - 0.3\text{ V}$ to $V_{DD} - 1.2\text{ V}$ (Ground-sensing input) |
| **Quiescent Current ($I_Q$)** | $230\,\mu\text{A}$ typical ($325\,\mu\text{A}$ max) |
| **Package Options** | 8-pin DIP (P), SOIC-8 (SN), 5-pin SOT-23 (OT) |

## Pin configuration

### 8-Pin DIP / SOIC Package

```
             ┌───┴───┐
          NC 1│ 1   8 │ NC (No Connection)
        VIN- 2│       │ 7 VDD (Positive Supply)
        VIN+ 3│ MCP601│ 6 VOUT (Op-Amp Output)
         VSS 4│       │ 5 NC
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1, 5, 8 | `NC` | Unconnected | No internal connection |
| 2 | `VIN-` | Analog Input | Inverting op-amp input |
| 3 | `VIN+` | Analog Input | Non-inverting op-amp input |
| 4 | `VSS` | Power / Ground | Negative power supply rail or system ground ($0\text{ V}$) |
| 6 | `VOUT` | Analog Output | Rail-to-rail amplifier output |
| 7 | `VDD` | Power Supply | Positive power supply rail ($+2.7\text{ V}$ to $+6.0\text{ V}$) |

### 5-Pin SOT-23-5 Package

```
             ┌─────────┐
       VOUT 1│ 1     5 │ VDD
        VSS 2│         │
       VIN+ 3│         │ 4 VIN-
             └─────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VOUT` | Analog Output | Rail-to-rail amplifier output |
| 2 | `VSS` | Power / Ground | Ground reference ($0\text{ V}$) |
| 3 | `VIN+` | Analog Input | Non-inverting signal input |
| 4 | `VIN-` | Analog Input | Inverting signal input |
| 5 | `VDD` | Power Supply | Positive supply voltage ($+2.7\text{ V}$ to $+6.0\text{ V}$) |

## Functional description

- **Rail-to-Rail Output Drive:** The output stage employs complementary CMOS transistors that allow output voltages to swing virtually to the supply rails. Driving a $25\text{ k}\Omega$ load, output voltage reaches within $15\text{ mV}$ of $V_{SS}$ and $V_{DD}$, maximizing the dynamic range of $3.3\text{ V}$ and $5\text{ V}$ microcontroller analog-to-digital converters (ADCs).
- **Sub-Picoampere Input Bias Current:** With an input bias current of only $1\text{ pA}$ at room temperature, the MCP601 creates negligible voltage errors when paired with megaohm-level feedback resistors in pH probes, ionization detectors, and photodiode amplifiers.
- **Phase Inversion Immunity:** Internal circuitry prevents phase reversal when the common-mode input voltage exceeds operating limits, protecting feedback systems from latch-up.

## Absolute maximum ratings

> [!WARNING]
> Stresses beyond these ratings cause permanent destruction. Input voltages must not exceed supply rails by more than $0.3\text{ V}$.

| Parameter | Symbol | Min | Max | Unit |
|---|---|---|---|---|
| Supply Voltage ($V_{DD} - V_{SS}$) | $V_S$ | — | $+7.0$ | V |
| Input Voltages (`VIN+`, `VIN-`) | $V_{IN}$ | $V_{SS} - 0.3$ | $V_{DD} + 0.3$ | V |
| Differential Input Voltage | $V_{ID}$ | — | $\pm (V_{DD} - V_{SS})$ | V |
| Input Current (all input pins) | $I_{IN}$ | — | $\pm 2.0$ | mA |
| Output Short-Circuit Current Duration | $t_{sc}$ | Continuous | Continuous | — |
| Operating Temperature Range | $T_A$ | $-40$ | $+85$ | °C |
| Storage Temperature Range | $T_{stg}$ | $-65$ | $+150$ | °C |

## Electrical characteristics

($V_{DD} = +5.0\text{ V}, V_{SS} = 0\text{ V}, V_{CM} = V_{DD}/2, R_L = 25\text{ k}\Omega\text{ to } V_{DD}/2, T_A = 25^\circ\text{C}$ unless otherwise noted)

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Offset Voltage | $V_{OS}$ | — | $\pm 0.7$ | $\pm 2.0$ | mV | — |
| Offset Voltage Drift | $\Delta V_{OS}/\Delta T$ | — | $\pm 3.0$ | — | µV/°C | $T_A = -40^\circ\text{C} \dots +85^\circ\text{C}$ |
| Input Bias Current | $I_B$ | — | 1.0 | 100.0 | pA | $T_A = 25^\circ\text{C}$ |
| | | — | 100.0 | 500.0 | pA | $T_A = 85^\circ\text{C}$ |
| Input Offset Current | $I_{OS}$ | — | 1.0 | — | pA | — |
| Common-Mode Input Range | $V_{CMR}$ | $V_{SS} - 0.3$ | — | $V_{DD} - 1.2$ | V | — |
| Common-Mode Rejection Ratio | $CMRR$ | 65 | 80 | — | dB | $V_{CM} = -0.3\text{V to } 3.8\text{V}$ |
| Power Supply Rejection Ratio | $PSRR$ | 65 | 80 | — | dB | $V_{DD} = 2.7\text{V to } 6.0\text{V}$ |
| Open-Loop DC Gain | $A_{OL}$ | 90 | 110 | — | dB | $V_O = 0.2\text{V to } 4.8\text{V}$ |
| Maximum High Output Voltage | $V_{OH}$ | $4.985$ | $4.992$ | — | V | $R_L = 25\text{ k}\Omega$ to GND |
| Minimum Low Output Voltage | $V_{OL}$ | — | $0.008$ | $0.015$ | V | $R_L = 25\text{ k}\Omega$ to $V_{DD}$ |
| Slew Rate | $SR$ | — | 2.3 | — | V/µs | $G = +1$ |
| Gain-Bandwidth Product | $GBW$ | — | 2.8 | — | MHz | — |
| Quiescent Supply Current | $I_Q$ | — | 230 | 325 | µA | $I_{OUT} = 0\text{ A}$ |

## Typical application circuit: High-Sensitivity Photodiode Transimpedance Amplifier

```
                 +3.3V
                  │
                ┌─┴──┐
                │ 7  │ (VDD)
                │    │
       Photodiode    │
          Cathode    │
          ┌────┴─────┤ 2 (VIN-)       MCP601
          │   ▲      │                Low-Power
          │   │      │                Op-Amp
          │ ┌─┴────┐ │ 3 (VIN+)
          │ │ Anode│ │
          │ └─┬────┘ └───┬─────────────┬────────────── Output to ADC (0V ... 3.3V)
          │   │          │             │
          │  GND        GND            │
          │                            │
          ├──────────────[ 1MΩ ]───────┤ (Rf: 1V per 1µA light current)
          │               Rf           │
          │                            │
          └──────────────┤├───[10pF]───┘
                          Cf (Phase Stability Capacitor)
```

### Operation
The photodiode operates in zero-bias (photovoltaic) mode to virtually eliminate dark leakage current. The $1\text{ pA}$ input bias current of the MCP601 ensures that light currents down into the low nanoamperes are converted into measurable output voltages ($1.0\text{ V}$ per $1.0\,\mu\text{A}$ of photocurrent) with high accuracy and zero DC offset loading.

## Design considerations & common mistakes

- **Input Common-Mode Range Limit ($V_{DD} - 1.2\text{ V}$):** While the MCP601 output swings rail-to-rail, its **input stage is ground-sensing, not rail-to-rail**. The input common-mode range extends down to $V_{SS} - 0.3\text{ V}$, but only up to $V_{DD} - 1.2\text{ V}$. For a $3.3\text{ V}$ supply, input signals must not exceed $2.1\text{ V}$. If the input signal must reach the positive rail, use a full rail-to-rail input device like the **MCP6001**.
- **Compensation for Large Feedback Resistors ($C_f$):** When using large feedback resistors ($R_f \ge 100\text{ k}\Omega$) in transimpedance or summing circuits, stray input capacitance ($C_{IN} \approx 6\text{ pF}$) introduces a high-frequency pole in the feedback path that can cause peaking or oscillation. Place a small compensation capacitor ($C_f \approx 5\text{ pF} \dots 22\text{ pF}$) in parallel with $R_f$ to maintain phase margin.
- **Supply Decoupling:** Connect a $0.1\,\mu\text{F}$ low-ESR ceramic capacitor directly between pin 7 (`VDD`) and pin 4 (`VSS`) using short traces.
