## Overview

The **CD4069UB** (CD4069) is a monolithic CMOS integrated circuit containing six independent **unbuffered** inverting circuits. Unlike "B-series" buffered inverters (such as the CD4049B or 74HC04) which cascade three internal inverter stages per gate to maximize digital switching gain, the CD4069UB uses a **single complementary MOSFET pair** per inverter.

Because it lacks internal cascaded stages, the CD4069UB features lower open-loop voltage gain ($A_v \approx 20\text{ to }30\text{ dB}$ at $V_{DD} = 10\text{V}$) and minimal phase shift across its operating range. This makes the CD4069UB the industry-standard CMOS chip for **RC multi-vibrators, crystal oscillators, pulse generators**, and **linear analog audio circuits** (such as synthesizer filters, preamplifiers, and classic guitar overdrive/fuzz distortion pedals like the Craig Anderton Tube Sound Fuzz and Way Huge Red Llama).

## Quick reference

| | |
|---|---|
| **Supply Voltage Range (`VDD`)** | 3.0 V to 18.0 V DC (20.0 V maximum limit) |
| **Logic Family** | CMOS 4000UB Series (Unbuffered) |
| **Circuit Topology** | Single CMOS complementary inverter pair per gate |
| **Inverters Count** | 6 Independent Inverters ($Y = \overline{A}$) |
| **Propagation Delay ($t_{pd}$)** | $30\text{ ns}$ typ at $VDD = 10\text{V}$ ($50\text{ ns}$ at $5\text{V}$) |
| **Linear Voltage Gain ($A_v$)** | $\approx 25\text{ dB}$ (Moderate gain; does not oscillate in linear biasing) |
| **Package Options** | 14-pin DIP / SOIC-14 / TSSOP-14 |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
          1A 1│ 1   14│ VDD
          1Y 2│       │13 6A
          2A 3│       │12 6Y
          2Y 4│CD4069UB 11 5A
          3A 5│       │10 5Y
          3Y 6│       │9  4A
         VSS 7│       │8  4Y
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `1A` | Digital / Analog Input | Inverter 1 Input |
| 2 | `1Y` | Digital / Analog Output | Inverter 1 Output ($1Y = \overline{1A}$) |
| 3 | `2A` | Digital / Analog Input | Inverter 2 Input |
| 4 | `2Y` | Digital / Analog Output | Inverter 2 Output |
| 5 | `3A` | Digital / Analog Input | Inverter 3 Input |
| 6 | `3Y` | Digital / Analog Output | Inverter 3 Output |
| 7 | `VSS` | Power | Ground / Negative Supply reference (0 V) |
| 8 | `4Y` | Digital / Analog Output | Inverter 4 Output |
| 9 | `4A` | Digital / Analog Input | Inverter 4 Input |
| 10 | `5Y` | Digital / Analog Output | Inverter 5 Output |
| 11 | `5A` | Digital / Analog Input | Inverter 5 Input |
| 12 | `6Y` | Digital / Analog Output | Inverter 6 Output |
| 13 | `6A` | Digital / Analog Input | Inverter 6 Input |
| 14 | `VDD` | Power | Positive Supply Voltage (+3.0 V to +18.0 V DC) |

## Function Table

| Input A | Output Y ($\overline{A}$) |
|---|---|
| Low ($L$) | High ($H$) |
| High ($H$) | Low ($L$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 3.0 | — | 18.0 | V | Operating DC voltage |
| Low-Level Input Voltage | $V_{IL}$ | — | — | 1.0 | V | $V_{DD} = 5\text{V}, V_O = 4.5\text{V}$ |
| High-Level Input Voltage | $V_{IH}$ | 4.0 | — | — | V | $V_{DD} = 5\text{V}, V_O = 0.5\text{V}$ |
| Output Sink Current | $I_{OL}$ | 0.51 | 1.0 | — | mA | $V_{DD} = 5\text{V}, V_{OUT} = 0.4\text{V}$ |
| Output Source Current | $I_{OH}$ | -0.51 | -1.0 | — | mA | $V_{DD} = 5\text{V}, V_{OUT} = 4.6\text{V}$ |
| Propagation Delay | $t_{PLH}, t_{PHL}$ | — | 50 | 100 | ns | $V_{DD} = 5\text{V}, C_L = 50\text{ pF}$ |
| Propagation Delay (10V) | $t_{PLH}, t_{PHL}$ | — | 30 | 60 | ns | $V_{DD} = 10\text{V}, C_L = 50\text{ pF}$ |
| Quiescent Device Current | $I_{DD}$ | — | 0.01 | 1.0 | µA | $V_{DD} = 5\text{V}, 25^\circ\text{C}$ |

## Typical Applications

### 1. Self-Biased Linear Audio Amplifier / Distortion Stage

Connecting a large feedback resistor ($1\text{ M}\Omega \dots 10\text{ M}\Omega$) from output to input biases the inverter into its linear region at $V_{DD} / 2$:

```
               ┌─────[ R_f = 1MΩ ]─────┐
               │                       │
 Audio In ──[ C_in ]───► [Pin 1: 1A]    │
                         CD4069UB       ├────[ C_out ]───► Amplified Audio Out
                         [Pin 2: 1Y] ───┘
```

When driven past its linear region, the single-stage MOSFET pair produces **gradual, tube-like soft saturation** rather than harsh digital rail clipping.

### 2. High-Stability 32.768 kHz / Megahertz Crystal Oscillator

```
             ┌─────[ R1 = 10MΩ ]─────┐
             │                       │
             ├───[ XTAL ]───┬────────┤
             │              │        │
      [Pin 1: 1A]     [Pin 2: 1Y]    └──► [Pin 3: 2A] (Buffer) ──► Square Wave Out
          │                 │
       [ C1 = 22pF ]     [ C2 = 22pF ]
          │                 │
         GND               GND
```

## Common mistakes

- **Substituting a buffered inverter (CD4049B / 74HC04) into oscillator or linear audio circuits:** Buffered ICs have extreme voltage gain ($>1000$) and three internal stages; using them in place of unbuffered CD4069UB causes severe high-frequency self-oscillation and parasitic RF noise.
- **Leaving unused inverter inputs open:** Unconnected high-impedance inputs float to midpoint voltages, turning both internal P- and N-channel MOSFETs simultaneously ON and drawing excessive supply current. Tie unused inputs directly to `VDD` or `VSS`.

## Notes

- **Suffix Identification:** Always verify the **UB** suffix (**CD4069UB**, **HEF4069UB**, **TC4069UBP**). Standard "B" series equivalents without the UB designation have buffered outputs.
