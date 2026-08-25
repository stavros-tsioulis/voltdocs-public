## Overview

The **CA3140** (CA3140A / CA3140E) is an internally compensated 4.5MHz **BiMOS operational amplifier** manufactured by Renesas Electronics (originally developed by RCA and Intersil). Available in a standard 8-pin through-hole **DIP-8** and **TO-5 metal can** package, it features the pinout and footprint of the historic 741 / LF356 op-amps.

Combining gate-protected **PMOS field-effect transistors in the input stage** with a **rugged bipolar Class AB output stage**, the CA3140 delivers an ultra-high input impedance of **$1.5\ \text{T}\Omega$ ($1.5 \times 10^{12}\ \Omega$)**, an extremely low input bias current of **$10\text{ pA}$**, a slew rate of **$9\text{ V}/\mu\text{s}$**, and internal unity-gain stability. Operating across an ultra-wide voltage range from **$4.0\text{V}$ to $36.0\text{V}$ DC** (or $\pm 2.0\text{V} \dots \pm 18.0\text{V}$ split rails), its input common-mode voltage range extends down to $0.5\text{V}$ below the negative supply rail, making it one of the premier op-amps for **photodiode transimpedance amplifiers, smoke detector sensors, piezoelectric preamplifiers, and analog integrators**.

## Quick reference

| | |
|---|---|
| **Amplifier Type** | BiMOS (MOSFET Input, Bipolar Output) |
| **Channels** | 1 (Single Op-Amp) |
| **Package** | 8-pin DIP (DIP-8 / PDIP-8) / 8-pin SOIC / TO-5 Metal Can |
| **Supply Voltage Range ($V^+ - V^-$)** | $4.0\text{ V}$ to $36.0\text{ V}$ (Single Supply: $+4\text{V} \dots +36\text{V}$, Dual: $\pm 2\text{V} \dots \pm 18\text{V}$) |
| **Input Impedance ($R_{IN}$)** | **$1.5\ \text{T}\Omega$ ($1.5 \times 10^{12}\ \Omega$)** |
| **Input Bias Current ($I_B$)** | **$10\text{ pA}$ typical** ($40\text{ pA}$ max on CA3140A) |
| **Input Common-Mode Range** | Includes Negative Rail ($V^- - 0.5\text{V}$ to $V^+ - 2.9\text{V}$) |
| **Gain-Bandwidth Product (GBW)** | $4.5\text{ MHz}$ |
| **Slew Rate ($SR$)** | $9\text{ V}/\mu\text{s}$ |
| **Internal Compensation** | Internally compensated for unity-gain stability ($A_V \ge 1$) |
| **Offset Nulling** | Standard 741-compatible pinout (Pins 1 and 5) |

## Pinout (DIP-8 Package)

```
                            ┌───┴───┐
            OFFSET NULL  1│ 1   8 │ STROBE
       (Inverting -IN)   2│ CA3140│ 7 V+ (Positive Supply)
   (Non-Inverting +IN)   3│ DIP-8 │ 6 OUTPUT (Bipolar Class AB)
       (Negative V-)     4│       │ 5 OFFSET NULL
                            └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `OFFSET NULL` | Input | Input offset voltage nulling terminal (Connect to $100\text{ k}\Omega$ trim pot) |
| 2 | `INV. INPUT` | Analog Input | Inverting Op-Amp Input terminal (`-IN`) |
| 3 | `NON-INV. INPUT`| Analog Input | Non-Inverting Op-Amp Input terminal (`+IN`) |
| 4 | `V- / GND` | Power | Negative Supply Rail (or Ground for single-supply operation) |
| 5 | `OFFSET NULL` | Input | Input offset voltage nulling terminal |
| 6 | `OUTPUT` | Analog Output | Bipolar Class AB Output |
| 7 | `V+` | Power | Positive Supply Rail ($+4.0\text{ V}$ to $+36.0\text{ V}$) |
| 8 | `STROBE` | Digital Input | Strobe terminal (pull LOW to disable output stage) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Offset Voltage | $V_{OS}$ | — | 5.0 | 15.0 | mV | CA3140 (2.0mV typ on CA3140A) |
| Input Bias Current | $I_B$ | — | 10.0 | 50.0 | pA | $T_A = 25^\circ\text{C}, V^+ = 15\text{V}$ |
| Input Resistance | $R_{IN}$ | — | 1.5 | — | TΩ | $T_A = 25^\circ\text{C}$ |
| Large-Signal Voltage Gain | $A_{VOL}$ | 20000 | 100000 | — | V/V | $100\text{ dB}$ with $R_L = 2\text{ k}\Omega$ |
| Slew Rate | $SR$ | — | 9.0 | — | V/µs | $R_L = 2\text{ k}\Omega, C_L = 100\text{ pF}$ |
| Gain-Bandwidth Product | $GBW$ | — | 4.5 | — | MHz | $f = 1\text{ MHz}$ |
| Supply Current | $I_{CC}$ | — | 4.0 | 6.0 | mA | $V^+ = 15\text{V}, I_O = 0$ |

## Typical Application Circuit: Photodiode Transimpedance Amplifier

```
                          +15V Single Supply
                                │
                         [Pin 7: V+]
                                │
     Photodiode                 │
         ┌───┤◄├───┐            │
         │         │            │
         │   [Pin 2: -IN] ──────┼───[ Feedback Resistor: 10MΩ ]───┐
         │       CA3140E        │                                 │
         │   [Pin 3: +IN]       ├─────────────────────────────────┴──► Output Voltage (V = I_photo * R_f)
         │         │            │
         └─────────┼────────────┤
                   │            │
              [Pin 4: V-] ──────┴── Common Ground (0V)
```

## Comparison: CA3140 vs CA3130 vs TL071

| Parameter | CA3140 | CA3130 | TL071 |
|---|---|---|---|
| **Input Technology** | **PMOS ($1.5\text{ T}\Omega$)** | PMOS ($1.5\text{ T}\Omega$) | JFET ($1\text{ T}\Omega$) |
| **Input Bias Current**| **$10\text{ pA}$** | $5\text{ pA}$ | $65\text{ pA}$ |
| **Output Stage** | **Bipolar Class AB** | CMOS Rail-to-Rail | Bipolar Class AB |
| **Max Supply Voltage**| **$36\text{ V}$ ($\pm 18\text{V}$)** | $16\text{ V}$ ($\pm 8\text{V}$) | $36\text{ V}$ ($\pm 18\text{V}$) |
| **Unity-Gain Stability**| **Internally Compensated**| External Cap Required | Internally Compensated |

## Common mistakes

- **Expecting rail-to-rail positive output swing:** Unlike the CA3130, the CA3140's output stage is bipolar. While its output swings down to within $0.13\text{V}$ of ground on a single supply, its positive swing is limited to approximately $V^+ - 2.0\text{V}$ under load.
- **Handling without ESD precautions:** The gate-protected PMOS input transistors are rated for $400\text{V}$ ESD, but static charges from ungrounded workbenches can degrade the ultra-low picoamp input bias characteristics over time.

## Notes

- **Suffix Guide:** `CA3140E` designates through-hole 8-pin plastic DIP; `CA3140T` designates 8-pin TO-5 hermetic metal can; `CA3140M` designates 8-pin SOIC.
