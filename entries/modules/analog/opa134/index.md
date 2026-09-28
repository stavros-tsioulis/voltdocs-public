## Overview

The **OPA134** is an ultra-low distortion, low-noise single operational amplifier belonging to the **SoundPlus™** audio line developed by Burr-Brown (Texas Instruments). Featuring a true FET-input stage with cascode circuitry, the OPA134 delivers extraordinary audio fidelity characterized by an ultra-low total harmonic distortion plus noise (THD+N) of just **0.00008%** at 1 kHz, a low noise density of **8 nV/√Hz**, and a negligible input bias current of **5 pA**.

With a high slew rate of **20 V/µs**, an **8 MHz** gain-bandwidth product, and superior capacitive-load drive capability, the OPA134 is a premier standard in professional audio equipment, high-end preamplifiers, headphone amplifiers, digital-to-analog converter (DAC) I/V post-filters, and active audiophile cross-overs.

## Quick reference

| | |
|---|---|
| **Op-Amp Channels** | 1 (Single Op-Amp) |
| **Input Architecture** | High-Impedance True FET Input |
| **Supply Voltage Range ($V_S$)** | $\pm 2.5\text{ V}$ to $\pm 18.0\text{ V}$ (Dual) / $5.0\text{ V}$ to $36.0\text{ V}$ (Single) |
| **Total Harmonic Distortion + Noise** | $0.00008\%$ ($1\text{ kHz}, G = 1, V_O = 3\text{ V}_{RMS}$) |
| **Input Voltage Noise Density ($e_n$)** | $8.0\text{ nV}/\sqrt{\text{Hz}}$ at $1\text{ kHz}$ |
| **Slew Rate ($SR$)** | $20.0\text{ V}/\mu\text{s}$ typical |
| **Gain Bandwidth Product ($GBW$)** | $8.0\text{ MHz}$ typical |
| **Input Bias Current ($I_B$)** | $5\text{ pA}$ typical ($20\text{ pA}$ max at $25^\circ\text{C}$) |
| **Output Voltage Swing** | Rail-to-rail within $1.2\text{ V}$ of supplies ($R_L = 2\text{ k}\Omega$) |
| **Quiescent Current ($I_Q$)** | $4.0\text{ mA}$ typical ($5.0\text{ mA}$ max) |
| **Packages** | 8-pin PDIP (PA), SOIC-8 (UA) |

## Pin configuration

### 8-Pin DIP / SOIC Package

```
             ┌───┴───┐
     OFFSET 1│ 1   8 │ NC (No Connection)
        -IN 2│       │ 7 V+ (Positive Supply)
        +IN 3│ OPA134│ 6 OUT (Op-Amp Output)
         V- 4│       │ 5 OFFSET (Trim)
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `OFFSET` | Analog Input | Input offset voltage trim terminal (optional null network) |
| 2 | `-IN` | Analog Input | Inverting signal input |
| 3 | `+IN` | Analog Input | Non-inverting signal input |
| 4 | `V-` | Power Supply | Negative supply rail ($-2.5\text{ V}$ to $-18.0\text{ V}$ or GND) |
| 5 | `OFFSET` | Analog Input | Input offset voltage trim terminal (optional null network) |
| 6 | `OUT` | Analog Output | Amplifier signal output |
| 7 | `V+` | Power Supply | Positive supply rail ($+2.5\text{ V}$ to $+18.0\text{ V}$) |
| 8 | `NC` | Unconnected | No internal connection |

## Absolute maximum ratings

> [!WARNING]
> Stresses above these limits cause permanent damage. Exceeding input voltage beyond supply rails causes destructive substrate latch-up.

| Parameter | Symbol | Min | Max | Unit |
|---|---|---|---|---|
| Supply Voltage ($V+ - V-$) | $V_S$ | — | $40.0$ | V |
| Input Voltage Range | $V_{IN}$ | $(V-) - 0.7$ | $(V+) + 0.7$ | V |
| Differential Input Voltage | $V_{ID}$ | $(V-) - 0.7$ | $(V+) + 0.7$ | V |
| Output Short-Circuit Duration to Ground | $t_{sc}$ | Continuous | Continuous | — |
| Operating Temperature Range | $T_A$ | $-40$ | $+85$ | °C |
| Junction Temperature | $T_J$ | — | $+150$ | °C |
| Storage Temperature Range | $T_{stg}$ | $-55$ | $+125$ | °C |

## Electrical characteristics

($V_S = \pm 15\text{ V}, R_L = 2\text{ k}\Omega, T_A = 25^\circ\text{C}$ unless otherwise noted)

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Offset Voltage | $V_{OS}$ | — | $\pm 0.5$ | $\pm 2.0$ | mV | — |
| Offset Voltage Drift | $dV_{OS}/dT$ | — | $2.0$ | $5.0$ | µV/°C | $T_A = -40^\circ\text{C} \dots +85^\circ\text{C}$ |
| Input Bias Current | $I_B$ | — | $5$ | $20$ | pA | $V_{CM} = 0\text{ V}$ |
| Input Offset Current | $I_{OS}$ | — | $2$ | $10$ | pA | — |
| Common-Mode Rejection Ratio | $CMRR$ | $86$ | $100$ | — | dB | $V_{CM} = -11\text{V to } +11\text{V}$ |
| Power Supply Rejection Ratio | $PSRR$ | $86$ | $100$ | — | dB | $V_S = \pm 2.5\text{V to } \pm 18\text{V}$ |
| Open-Loop Voltage Gain | $A_{VOL}$ | $106$ | $120$ | — | dB | $V_O = \pm 10\text{V}, R_L = 2\text{ k}\Omega$ |
| Slew Rate | $SR$ | — | $20$ | — | V/µs | $G = 1$ |
| Gain-Bandwidth Product | $GBW$ | — | $8.0$ | — | MHz | — |
| Total Harmonic Distortion + Noise | $THD+N$ | — | $0.00008$ | — | % | $f = 1\text{ kHz}, G = 1, V_O = 3\text{ V}_{RMS}$ |
| Input Voltage Noise Density | $e_n$ | — | $8.0$ | — | nV/√Hz | $f = 1\text{ kHz}$ |
| Maximum Output Voltage Swing | $V_O$ | $\pm 13.5$ | $\pm 13.8$ | — | V | $R_L = 2\text{ k}\Omega$ |
| Short-Circuit Output Current | $I_{SC}$ | — | $+40 / -35$ | — | mA | — |
| Quiescent Current | $I_Q$ | — | $4.0$ | $5.0$ | mA | $I_O = 0\text{ A}$ |

## Typical application circuit: High-Fidelity Non-Inverting Audio Preamp

```
                 +15V
                  │
                ┌─┴──┐
                │ 7  │ (V+)
                │    │
       Audio In │    │
       ──┤├───┬─┤ 3  │
        1µF   │ │(+IN)    OPA134
       Film   │ │          Audio
             ┌┴┐│           Amp
       100k  │ ││ 2         6
        Cin  └┬┘│(-IN)    (OUT)
              │ └───┬───────┬───────────────── Audiophile Output
              │     │       │
             GND    │      ┌┴┐ Rf
                    │      │ │ 10k
                    │      └┬┘
                    │       │
                    ├───────┘
                    │
                   ┌┴┐ Rg
                   │ │ 2.2k (Gain = 1 + Rf/Rg ≈ +14.9 dB)
                   └┬┘
                    │
                   ┌┴──┐
                   │   │ Cg (47µF Bipolar electrolytic)
                   └───┘
                    │
                   GND
                    │
                ┌───┴───┐
                │ 4 (V-)│
                └───────┘
                  │
                 -15V
```

### Component Guidelines
- **Gain Formula:** $A_v = 1 + \frac{R_f}{R_g}$. With $R_f = 10\text{ k}\Omega$ and $R_g = 2.2\text{ k}\Omega$, gain is $\approx 5.54\times$ ($+14.9\text{ dB}$).
- **Feedback Network Values:** Keep resistors below $20\text{ k}\Omega$ to ensure the amplifier thermal Johnson noise ($e_{nR} = \sqrt{4kTR}$) does not exceed the OPA134 intrinsic input noise floor ($8\text{ nV}/\sqrt{\text{Hz}}$).
- **Decoupling:** Solder a $0.1\,\mu\text{F}$ film or X7R ceramic capacitor along with a $10\,\mu\text{F}$ low-ESR electrolytic capacitor directly from pin 7 ($V+$) and pin 4 ($V-$) to signal ground.

## Design considerations & common mistakes

- **Capacitive Load Compensation:** The OPA134 can drive capacitive loads up to $100\text{ pF}$ directly without oscillation. For heavier capacitive loads (e.g., long studio audio interconnect cables exceeding several meters), insert a small $22\,\Omega \dots 47\,\Omega$ series isolation resistor inside or immediately following the feedback loop to isolate cable capacitance from the output stage.
- **Offset Null Terminals (Pins 1 & 5):** Pins 1 and 5 provide offset trim. In almost all audio applications, DC offset is negligible ($0.5\text{ mV}$ typ) or blocked by output coupling capacitors. Leave pins 1 and 5 **completely floating** if offset nulling is unneeded; connecting them to ground will introduce large offsets.
- **Supply Decoupling Integrity:** Because of its wide $8\text{ MHz}$ bandwidth and fast $20\text{ V}/\mu\text{s}$ slew rate, poor PCB layout or lack of high-frequency power supply decoupling can trigger ultrasonic oscillation ($5\text{ MHz} \dots 15\text{ MHz}$) that degrades audio transparency and causes chip overheating.
