## Overview

The **LM2902** is an automotive- and industrial-grade quad operational amplifier manufactured by Texas Instruments, STMicroelectronics, and ON Semiconductor. It is the extended-temperature, ruggedized version of the ubiquitous **LM324** op-amp, engineered specifically to withstand harsh operating environments from **$-40^\circ\text{C}$ to $+125^\circ\text{C}$** (AEC-Q100 qualified variants up to $150^\circ\text{C}$).

Internally consisting of four independent, high-gain, internally frequency-compensated operational amplifiers, the LM2902 is designed to operate from a single power supply across a wide voltage range ($3.0\text{ V}$ to $32.0\text{ V}$), or from split supplies ($\pm 1.5\text{ V}$ to $\pm 16.0\text{ V}$). Its input common-mode voltage range includes Ground ($0\text{ V}$), enabling direct ground-referenced sensing in single-supply automotive 12V and industrial 24V electronics without negative supply rails.

## Quick reference

| | |
|---|---|
| **Function** | Automotive / Industrial Extended-Temperature Quad Op-Amp |
| **Supply Voltage (Single Supply)** | $3.0\text{ V}$ to $32.0\text{ V}$ DC ($26.0\text{ V}$ standard, $32.0\text{ V}$ for B-suffix) |
| **Supply Voltage (Split Supply)** | $\pm 1.5\text{ V}$ to $\pm 16.0\text{ V}$ DC |
| **Operating Temperature Range** | **$-40^\circ\text{C}$ to $+125^\circ\text{C}$** (Automotive Grade 1) |
| **Op-Amp Channels** | 4 independent operational amplifiers |
| **Input Common-Mode Range** | Includes Ground ($0\text{ V}$ to $V_{CC} - 1.5\text{ V}$) |
| **Gain Bandwidth Product (GBW)** | $1.2\text{ MHz}$ typ |
| **Slew Rate (SR)** | $0.5\text{ V/}\mu\text{s}$ typ |
| **Input Offset Voltage ($V_{IO}$)** | $2.0\text{ mV}$ typ ($7.0\text{ mV}$ max over full temp) |
| **Supply Current (Total, 4 channels)**| $800\text{ }\mu\text{A}$ typ ($200\text{ }\mu\text{A}$ per channel, supply-independent) |
| **Packages** | 14-pin PDIP (N), SOIC-14 (D), TSSOP-14 (PW) |

## Pin configuration

### 14-Pin DIP / SOIC Package

```
               ┌──────────┐
         1OUT ─┤ 1     14 ├─ 4OUT
         1IN- ─┤ 2     13 ├─ 4IN-
         1IN+ ─┤ 3     12 ├─ 4IN+
         VCC+ ─┤ 4     11 ├─ GND (or VCC-)
         2IN+ ─┤ 5     10 ├─ 3IN+
         2IN- ─┤ 6      9 ├─ 3IN-
         2OUT ─┤ 7      8 ├─ 3OUT
               └──────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `1OUT` | Analog Output | Op-amp 1 output terminal |
| 2 | `1IN-` | Analog Input | Op-amp 1 inverting input |
| 3 | `1IN+` | Analog Input | Op-amp 1 non-inverting input |
| 4 | `VCC+` | Power Supply | Positive DC power supply ($+3.0\text{V} \dots +32.0\text{V}$) |
| 5 | `2IN+` | Analog Input | Op-amp 2 non-inverting input |
| 6 | `2IN-` | Analog Input | Op-amp 2 inverting input |
| 7 | `2OUT` | Analog Output | Op-amp 2 output terminal |
| 8 | `3OUT` | Analog Output | Op-amp 3 output terminal |
| 9 | `3IN-` | Analog Input | Op-amp 3 inverting input |
| 10 | `3IN+` | Analog Input | Op-amp 3 non-inverting input |
| 11 | `GND` | Power Supply | Ground ($0\text{V}$) in single-supply or negative rail ($-V_S$) |
| 12 | `4IN+` | Analog Input | Op-amp 4 non-inverting input |
| 13 | `4IN-` | Analog Input | Op-amp 4 inverting input |
| 14 | `4OUT` | Analog Output | Op-amp 4 output terminal |

## Functional description

- **Ground-Sensing Input Stage:** Uses lateral PNP differential input transistors. Because the base-emitter junctions are forward-biased toward the positive rail, the input common-mode range includes negative supply/ground ($V_{EE} - 0.3\text{ V}$). This allows direct amplification of low-side current shunts or thermocouple signals without requiring a split power supply.
- **Low Power Consumption:** Total quiescent drain is only $800\text{ }\mu\text{A}$ across all four channels combined, remaining essentially constant over the entire supply voltage range.
- **Automotive Reliability:** Tested and rated for full parametric performance from $-40^\circ\text{C}$ to $+125^\circ\text{C}$, ensuring stability under automotive hood temperatures, industrial PLCs, and outdoor solar charge controllers.

## Absolute maximum ratings

> [!WARNING]
> Stresses beyond these ratings cause permanent damage. Functional operation at these limits is not guaranteed.

| Parameter | Rating | Unit |
|---|---|---|
| Supply Voltage ($V_{CC} - V_{EE}$) | 32 (36 for LM2902B) | V |
| Differential Input Voltage | 32 | V |
| Input Voltage Range ($V_I$) | $-0.3$ to 32 | V |
| Output Short-Circuit Duration | Continuous to Ground or $V_{CC}$ (single amplifier) | — |
| Operating Free-Air Temperature ($T_A$) | -40 to 125 | °C |
| Maximum Junction Temperature ($T_J$) | 150 | °C |
| Storage Temperature Range | -65 to 150 | °C |

## Electrical characteristics

$V_{CC} = 5.0\text{ V}$, $V_{EE} = 0\text{ V}$, $T_A = 25^\circ\text{C}$, unless otherwise noted.

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Offset Voltage | $V_{IO}$ | — | 2.0 | 7.0 | mV | Full temperature range: $-40^\circ\text{C} \dots +125^\circ\text{C}$ |
| Input Offset Drift | $dV_{IO}/dT$ | — | 7.0 | — | $\mu\text{V/}^\circ\text{C}$ | Over temperature range |
| Input Bias Current | $I_B$ | — | 45 | 200 | nA | $V_{CM} = 0\text{ V}$, full temperature |
| Common-Mode Input Range | $V_{ICR}$ | 0 | — | $V_{CC}-1.5$ | V | Single supply, $T_A = 25^\circ\text{C}$ |
| Large-Signal Voltage Gain | $A_{VD}$ | 25 | 100 | — | $\text{V/mV}$ | $R_L \ge 2\text{ k}\Omega, V_O = 1\text{ V}$ to $11\text{ V}$ (at $V_{CC}=15\text{V}$) |
| Common-Mode Rejection Ratio | $\text{CMRR}$ | 50 | 70 | — | dB | Over full common-mode range |
| Power Supply Rejection Ratio | $\text{PSRR}$ | 65 | 100 | — | dB | $V_{CC} = 5\text{ V}$ to $30\text{ V}$ |
| Output Voltage Swing (High) | $V_{OH}$ | $V_{CC}-1.5$ | $V_{CC}-1.2$ | — | V | $R_L = 2\text{ k}\Omega$ to GND |
| Output Voltage Swing (Low) | $V_{OL}$ | — | 5 | 20 | mV | $R_L = 10\text{ k}\Omega$ to GND |
| Output Sinking Current | $I_{SINK}$ | 12 | 20 | — | mA | $V_{IN-} = 1\text{ V}, V_{IN+} = 0\text{ V}, V_O = 2\text{ V}$ |
| Gain Bandwidth Product | $\text{GBW}$ | — | 1.2 | — | MHz | $f = 100\text{ kHz}$ |
| Slew Rate | $\text{SR}$ | — | 0.5 | — | $\text{V/}\mu\text{s}$ | Unity gain |
| Total Supply Current | $I_{CC}$ | — | 0.8 | 1.5 | mA | All 4 op-amps, outputs open |

## Typical application

### Quad-Channel Low-Side Current Sense / DC Voltage Transducer

The LM2902 senses voltages down to $0\text{ V}$ (GND), making it standard for conditioning four independent motor phase currents or battery cell voltages:

```
        Load Current Return
                 │
                 ├───► To Load
                 │
             [Rshunt = 0.05Ω]
                 │
                GND
                 │
                 ├───[ R1 = 1kΩ ]──────┐
                 │                     │
                 │                 ┌───┴───┐
                 │                 │ -IN   │
                 │                 │ LM2902├───► Output to ADC (0V to 3.3V)
                 └───[ R2 = 1kΩ ]──┤ +IN   │
                                   └───┬───┘
                                       │
                                   [Rf = 66kΩ Feedback]
                                       │
                                      OUT
```

## Common mistakes

- **Using for Hi-Fi Audio:** The LM2902 output stage incorporates a Class-B deadband. As output signals transition through zero current, crossover distortion produces measurable notch distortion in audio waveforms. For audio, choose the **TL074** or **OPA4134**.
- **Assuming Rail-to-Rail Output:** The high-level output voltage stops $1.5\text{ V}$ below $V_{CC}$ ($V_{OH} \le V_{CC} - 1.5\text{ V}$). When powering from 5V, the output cannot swing above $\sim 3.5\text{ V}$. If $0\text{V}$ to $5\text{V}$ output is needed from a 5V supply, use a true rail-to-rail op-amp like the **MCP6004**.
- **Leaving Unused Channels Floating:** Always wire unused channels as unity-gain buffers (output connected to inverting input) with the non-inverting input tied to a voltage within the valid input range (e.g. Ground or a resistive divider).

## Notes

- **LM2902 vs LM324:** The LM324 is rated for commercial temperatures ($0^\circ\text{C}$ to $+70^\circ\text{C}$), whereas the LM2902 is fully guaranteed across the automotive/industrial range ($-40^\circ\text{C}$ to $+125^\circ\text{C}$).
- **Variants:** **LM2902** (standard), **LM2902K** (automotive Grade 1 with higher ESD protection), **LM2902B** (latest TI upgrade with 36V capability and lower offset). **LM2904** is the dual op-amp equivalent.
