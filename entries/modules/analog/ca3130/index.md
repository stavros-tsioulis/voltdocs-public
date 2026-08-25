## Overview

The **CA3130** (CA3130A / CA3130E) is an iconic 15MHz **BiMOS operational amplifier** manufactured by Renesas Electronics (originally developed by RCA and Intersil). Available in an 8-pin through-hole **DIP-8** and **TO-5 metal can** package, it combines gate-protected **PMOS field-effect transistors in the input stage** with a **CMOS output stage** capable of swinging rail-to-rail.

Operating from **$5.0\text{V}$ to $16.0\text{V}$ DC** (or $\pm 2.5\text{V} \dots \pm 8.0\text{V}$ split rails), the CA3130 boasts an ultra-high input impedance of **$1.5\ \text{T}\Omega$ ($1.5 \times 10^{12}\ \Omega$)**, an extremely low input bias current of **$5\text{ pA}$**, a wide gain-bandwidth product of **$15\text{ MHz}$**, and a rapid slew rate of **$30\text{ V}/\mu\text{s}$**. Because its CMOS output stage swings within millivolts of ground and the positive supply rail, the CA3130 has been a legendary staple in **analog modular synthesizers (VCO core reset circuits, sample-and-hold buffers), electrometer preamplifiers, pH meter probes, and ultra-high-impedance touch switches**.

## Quick reference

| | |
|---|---|
| **Amplifier Type** | BiMOS (MOSFET Input, CMOS Rail-to-Rail Output) |
| **Channels** | 1 (Single Op-Amp) |
| **Package** | 8-pin DIP (DIP-8 / PDIP-8) / 8-pin SOIC / TO-5 Metal Can |
| **Supply Voltage Range ($V^+ - V^-$)** | $5.0\text{ V}$ to $16.0\text{ V}$ (Single Supply: $+5\text{V} \dots +16\text{V}$, Dual: $\pm 2.5\text{V} \dots \pm 8\text{V}$) |
| **Input Impedance ($R_{IN}$)** | **$1.5\ \text{T}\Omega$ ($1.5 \times 10^{12}\ \Omega$)** |
| **Input Bias Current ($I_B$)** | **$5\text{ pA}$ typical** ($15\text{ pA}$ max on CA3130A) |
| **Gain-Bandwidth Product (GBW)** | $15\text{ MHz}$ |
| **Slew Rate ($SR$)** | $30\text{ V}/\mu\text{s}$ (uncompensated) / $10\text{ V}/\mu\text{s}$ (compensated) |
| **Output Voltage Swing** | True Rail-to-Rail ($10\text{ mV}$ from $V^+$ and $V^-$ with $100\text{ k}\Omega$ load) |
| **Strobe Terminal** | Pin 8 allows digital shutdown/strobing of output stage |

## Pinout (DIP-8 Package)

```
                            ┌───┴───┐
            OFFSET NULL  1│ 1   8 │ STROBE / COMPENSATION
       (Inverting -IN)   2│ CA3130│ 7 V+ (Positive Supply)
   (Non-Inverting +IN)   3│ DIP-8 │ 6 OUTPUT (CMOS Rail-to-Rail)
       (Negative V-)     4│       │ 5 OFFSET NULL
                            └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `OFFSET NULL` | Input | Offset voltage nulling / Phase compensation connection |
| 2 | `INV. INPUT` | Analog Input | Inverting Op-Amp Input terminal (`-IN`) |
| 3 | `NON-INV. INPUT`| Analog Input | Non-Inverting Op-Amp Input terminal (`+IN`) |
| 4 | `V- / GND` | Power | Negative Supply Rail (or Ground for single-supply operation) |
| 5 | `OFFSET NULL` | Input | Offset voltage nulling terminal |
| 6 | `OUTPUT` | Analog Output | CMOS Rail-to-Rail Output |
| 7 | `V+` | Power | Positive Supply Rail ($+5.0\text{ V}$ to $+16.0\text{ V}$) |
| 8 | `STROBE / COMP`| Control/Input | Strobe (pull LOW to disable output) / Phase compensation capacitor |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Offset Voltage | $V_{OS}$ | — | 8.0 | 15.0 | mV | CA3130 (2.0mV typ on CA3130A) |
| Input Bias Current | $I_B$ | — | 5.0 | 50.0 | pA | $T_A = 25^\circ\text{C}, V^+ = 15\text{V}$ |
| Input Resistance | $R_{IN}$ | — | 1.5 | — | TΩ | $T_A = 25^\circ\text{C}$ |
| Large-Signal Voltage Gain | $A_{VOL}$ | 32000 | 320000 | — | V/V | $110\text{ dB}$ with $R_L = 2\text{ k}\Omega$ |
| Slew Rate | $SR$ | — | 30 | — | V/µs | Uncompensated, $R_L = 2\text{ k}\Omega$ |
| Gain-Bandwidth Product | $GBW$ | — | 15 | — | MHz | $f = 1\text{ MHz}$ |
| Supply Current | $I_{CC}$ | — | 10.0 | 15.0 | mA | $V^+ = 15\text{V}, I_O = 0$ |

## Typical Application Circuit: High-Impedance Electrometer Buffer

```
                            +12V to +15V Single Supply
                                  │
                           [Pin 7: V+]
                                  │
     High-Z Signal In             │
     (pH probe / Piezo)           │
           │                      │
           └───► [Pin 3: +IN]     │
                  CA3130E         ├────► [Pin 6: OUTPUT] ─── Low-Z Buffered Output
           ┌───► [Pin 2: -IN] ────┘
           │
           │      [Pin 4: V-]
           │          │
           └──────────┴──────────────── Common GND
           
  Phase Compensation (Required for Unity-Gain Stability):
    Pin 1 ───[ 47pF - 56pF Ceramic Cap ]─── Pin 8
```

## Common mistakes

- **Omitting the unity-gain phase compensation capacitor:** The CA3130 is **not internally unity-gain compensated**. When wired as a voltage follower ($A_V = 1$) or low-gain amplifier, it will oscillate violently unless a **$47\text{ pF} \dots 56\text{ pF}$ ceramic capacitor** is placed directly between Pin 1 and Pin 8. (For an internally compensated alternative with bipolar output, use the **CA3140**).
- **Exceeding the 16V supply rating:** Unlike standard 36V op-amps (LM741, TL072), the CA3130's maximum supply voltage rating is **$16.0\text{V}$ total** ($+16\text{V}$ single or $\pm 8\text{V}$ split). Connecting $\pm 15\text{V}$ rails will instantly destroy the CMOS output transistors.

## Notes

- **CA3130 vs CA3140:** CA3130 features a rail-to-rail CMOS output stage ($15\text{MHz}$, uncompensated, 16V max); CA3140 features a Class AB Bipolar output stage ($4.5\text{MHz}$, internally unity-gain compensated, 36V max).
