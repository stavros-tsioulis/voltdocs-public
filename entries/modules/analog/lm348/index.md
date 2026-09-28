## Overview

The **LM348** is a true quadruple operational amplifier manufactured by Texas Instruments, STMicroelectronics, and ON Semiconductor (originally developed by National Semiconductor). Designed as a high-density "quad 741", the LM348 houses four independent, internally compensated operational amplifiers on a single monolithic chip, delivering performance characteristics functionally equivalent to four standalone **µA741** op-amps.

While maintaining the beloved stability and ruggedness of the 741 architecture, the LM348 offers notable improvements: supply current drain is reduced to just **$0.6\text{ mA}$ per amplifier** (less than half the power of four discrete 741s), input bias current and input offset current are significantly lower, and inter-amplifier crosstalk is minimized by internal shielding. It is widely used in legacy audio processing boards, active Butterworth/Chebyshev filter banks, analog computers, and university teaching laboratories.

## Quick reference

| | |
|---|---|
| **Function** | Quadruple 741 General-Purpose Operational Amplifier |
| **Supply Voltage (Split Supply)** | $\pm 4.0\text{ V}$ to $\pm 18.0\text{ V}$ DC ($\pm 15.0\text{ V}$ standard) |
| **Supply Voltage (Single Supply)** | $8.0\text{ V}$ to $36.0\text{ V}$ DC |
| **Op-Amp Channels** | 4 independent 741-type op-amps |
| **Gain Bandwidth Product (GBW)** | $1.0\text{ MHz}$ typ |
| **Slew Rate (SR)** | $0.5\text{ V/}\mu\text{s}$ typ |
| **Input Offset Voltage ($V_{IO}$)** | $1.0\text{ mV}$ typ ($6.0\text{ mV}$ max) |
| **Input Bias Current ($I_B$)** | $100\text{ nA}$ typ ($200\text{ nA}$ max) |
| **Large-Signal Voltage Gain ($A_{VD}$)**| $160\text{ V/mV}$ ($104\text{ dB}$) typ |
| **Supply Current (Total, 4 channels)**| $2.4\text{ mA}$ typ ($0.6\text{ mA}$ per channel) |
| **Packages** | 14-pin PDIP (N), SOIC-14 (D) |

## Pin configuration

### 14-Pin DIP / SOIC Package

```
               ┌──────────┐
         1OUT ─┤ 1     14 ├─ 4OUT
         1IN- ─┤ 2     13 ├─ 4IN-
         1IN+ ─┤ 3     12 ├─ 4IN+
          VCC ─┤ 4     11 ├─ VEE (or GND)
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
| 4 | `VCC` | Power Supply | Positive DC power supply rail ($+V_S$, typically $+12\text{V} \dots +15\text{V}$) |
| 5 | `2IN+` | Analog Input | Op-amp 2 non-inverting input |
| 6 | `2IN-` | Analog Input | Op-amp 2 inverting input |
| 7 | `2OUT` | Analog Output | Op-amp 2 output terminal |
| 8 | `3OUT` | Analog Output | Op-amp 3 output terminal |
| 9 | `3IN-` | Analog Input | Op-amp 3 inverting input |
| 10 | `3IN+` | Analog Input | Op-amp 3 non-inverting input |
| 11 | `VEE` | Power Supply | Negative DC power supply rail ($-V_S$, typically $-12\text{V} \dots -15\text{V}$) |
| 12 | `4IN+` | Analog Input | Op-amp 4 non-inverting input |
| 13 | `4IN-` | Analog Input | Op-amp 4 inverting input |
| 14 | `4OUT` | Analog Output | Op-amp 4 output terminal |

## Functional description

- **True 741 Internal Topologies:** Each of the four amplifiers uses standard bipolar differential input pairs with active collector loads and a Class-AB push-pull output stage.
- **Continuous Short-Circuit Protection:** Outputs feature internal current-limiting circuitry protecting against continuous shorts to ground or either supply rail.
- **No Latch-Up:** Circuit design ensures immunity from latch-up when input common-mode ratings are momentarily exceeded.
- **Inter-Amplifier Isolation:** Deep isolation diffusions provide $>120\text{ dB}$ of channel separation across audio frequencies ($1\text{ kHz}$).

## Absolute maximum ratings

> [!WARNING]
> Stresses beyond these ratings cause permanent damage. Functional operation at these limits is not guaranteed.

| Parameter | Rating | Unit |
|---|---|---|
| Supply Voltage ($V_{CC} - V_{EE}$) | 36 ($\pm 18$) | V |
| Differential Input Voltage | $\pm 30$ | V |
| Input Common-Mode Voltage Range | $\pm 15$ (not to exceed supply rails) | V |
| Output Short-Circuit Duration | Continuous | — |
| Operating Ambient Temperature ($T_A$, LM348) | 0 to 70 | °C |
| Operating Ambient Temperature ($T_A$, LM248) | -25 to 85 | °C |
| Operating Ambient Temperature ($T_A$, LM148) | -55 to 125 | °C |
| Storage Temperature Range | -65 to 150 | °C |

## Electrical characteristics

$V_{CC} = +15\text{ V}$, $V_{EE} = -15\text{ V}$, $T_A = 25^\circ\text{C}$, unless otherwise noted.

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Offset Voltage | $V_{IO}$ | — | 1.0 | 6.0 | mV | $R_S \le 10\text{ k}\Omega$ |
| Input Offset Current | $I_{IO}$ | — | 4.0 | 50 | nA | Over temperature |
| Input Bias Current | $I_B$ | — | 100 | 200 | nA | Over temperature |
| Common-Mode Input Range | $V_{ICR}$ | $\pm 12.0$ | $\pm 13.5$ | — | V | $V_S = \pm 15\text{ V}$ |
| Output Voltage Swing | $V_{OM}$ | $\pm 12.0$ | $\pm 13.5$ | — | V | $R_L \ge 2\text{ k}\Omega$ |
| Large-Signal Voltage Gain | $A_{VD}$ | 25 | 160 | — | $\text{V/mV}$ | $R_L \ge 2\text{ k}\Omega, V_O = \pm 10\text{ V}$ |
| Common-Mode Rejection Ratio | $\text{CMRR}$ | 70 | 90 | — | dB | $R_S \le 10\text{ k}\Omega$ |
| Power Supply Rejection Ratio | $\text{PSRR}$ | 77 | 96 | — | dB | $V_S = \pm 9\text{ V}$ to $\pm 15\text{ V}$ |
| Slew Rate | $\text{SR}$ | — | 0.5 | — | $\text{V/}\mu\text{s}$ | Unity gain |
| Gain Bandwidth Product | $\text{GBW}$ | — | 1.0 | — | MHz | Unity gain |
| Channel Separation (Crosstalk) | $C_S$ | — | 120 | — | dB | $f = 1\text{ kHz}$ |
| Total Supply Current | $I_{CC}$ | — | 2.4 | 4.5 | mA | All 4 op-amps, outputs open |

## Typical application

### Quad State-Variable Filter or Cascaded Active Filter Bank

The LM348 provides four identical, well-matched 741 operational amplifiers in a single DIP-14 footprint, ideal for building four-pole active Butterworth or Sallen-Key low-pass filter cascades in audio crossovers and telemetry systems.

```
  Audio Input
      │
   [ R1 ]
      │
      ├───[ R2 ]──────┬────────────────┐
      │               │                │
     [C1]             │            ┌───┴───┐
      │               └───[C2]─────┤ -IN   │
     GND                           │ LM348 ├───► Filtered Output
                         GND ──────┤ +IN   │
                                   └───────┘
```

## Common mistakes

- **Attempting Single-Supply 0V-to-5V Operation:** Unlike the LM324, the LM348 does **not** have ground-sensing inputs. Its common-mode input range stops $2\text{ V}$ to $3\text{ V}$ above the negative rail ($V_{EE} + 2\text{V}$). Attempting to run it on a single $5\text{ V}$ supply without artificial mid-supply biasing causes severe signal clipping or saturation. For single-supply designs, use the **LM324** or **MCP6004**.
- **Expecting External Offset Null Pins:** Individual 741 op-amps provide offset null pins (pins 1 and 5 in DIP-8). Because the LM348 packs four amplifiers into a standard 14-pin DIP, there are not enough pins for offset nulling. If sub-millivolt offset trimming is required, use the **OP07** or external summing trimpots.
- **Using for High-Frequency / High-Slew Signals:** With a slew rate of $0.5\text{ V/}\mu\text{s}$ and bandwidth of $1.0\text{ MHz}$, large high-frequency waveforms ($>10\text{ kHz}$) will exhibit triangle distortion. Use the **TL074** for audio applications requiring high fidelity and fast transient response.

## Notes

- **Part Family:** **LM148** (military grade, $-55^\circ\text{C}$ to $+125^\circ\text{C}$), **LM248** (industrial grade, $-25^\circ\text{C}$ to $+85^\circ\text{C}$), **LM348** (commercial grade, $0^\circ\text{C}$ to $+70^\circ\text{C}$).
- **Comparison with LM324:** While both share the exact same 14-pin pinout, the LM324 is optimized for single-supply ground-sensing DC operation ($3\text{V}$ to $32\text{V}$), whereas the LM348 is optimized for symmetric split-supply operation ($\pm 15\text{V}$) with lower crossover distortion.
