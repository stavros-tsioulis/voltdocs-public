## Overview

The **NJM4558** (historically branded as **JRC4558** or **JRC4558D**) is a dual high-gain operational amplifier manufactured by New Japan Radio (NJR / Nisshinbo Micro Devices). Pin-compatible with industry-standard dual op-amps like the MC1458 and LM358, it incorporates internal frequency compensation and phase margin optimization into an 8-pin DIP package.

The NJM4558 achieved legendary status in analog audio history after being chosen as the heart of the iconic **Ibanez TS808 / TS9 Tube Screamer** overdrive pedal. Audio engineers and musicians favor its moderate $1.0\text{ V}/\mu\text{s}$ slew rate and subtle input stage clipping characteristics, which yield a warm, musically pleasing mid-range distortion tone.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`V+ / V-`)** | $\pm 4.0\text{V}$ to $\pm 18.0\text{V}$ (Split) or $+8.0\text{V}$ to $+36.0\text{V}$ (Single) |
| **Open-Loop Voltage Gain** | $100\text{ dB}$ typical |
| **Gain Bandwidth Product** | $3.0\text{ MHz}$ typical |
| **Slew Rate** | $1.0\text{ V}/\mu\text{s}$ typical |
| **Input Bias Current** | $50\text{ nA}$ typical ($500\text{ nA}$ max) |
| **Quiescent Supply Current** | $3.5\text{ mA}$ typical for both channels |
| **Package** | 8-pin DIP (NJM4558D) / SOIC-8 (NJM4558M) |

## Pinout (DIP-8 Package)

```
             ┌───┴───┐
       1OUT 1│ 1   8 │ V+
       1-IN 2│       │ 7 2OUT
       1+IN 3│NJM4558│ 6 2-IN
         V- 4│       │ 5 2+IN
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `1OUT` | Output | Amplifier Channel 1 Output |
| 2 | `1-IN` | Input | Amplifier Channel 1 Inverting Input |
| 3 | `1+IN` | Input | Amplifier Channel 1 Non-Inverting Input |
| 4 | `V-` | Power | Negative Supply Voltage (or GND in single 9V battery mode) |
| 5 | `2+IN` | Input | Amplifier Channel 2 Non-Inverting Input |
| 6 | `2-IN` | Input | Amplifier Channel 2 Inverting Input |
| 7 | `2OUT` | Output | Amplifier Channel 2 Output |
| 8 | `V+` | Power | Positive Supply Voltage (+4.0V to +18.0V DC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V^+/V^-$ | $\pm 4.0$ | $\pm 15.0$ | $\pm 18.0$ | V | Split supply |
| Input Offset Voltage | $V_{IO}$ | — | 0.5 | 6.0 | mV | $R_S \le 10\text{k}\Omega$ |
| Input Offset Current | $I_{IO}$ | — | 5.0 | 200 | nA | $T_A = 25^\circ\text{C}$ |
| Large Signal Voltage Gain | $A_V$ | 86 | 100 | — | dB | $R_L \ge 2\text{k}\Omega, V_O = \pm 10\text{V}$ |
| Maximum Output Voltage Swing| $V_{OM}$ | $\pm 12.0$ | $\pm 14.0$ | — | V | $R_L \ge 10\text{k}\Omega, V_{SUPPLY} = \pm 15\text{V}$ |
| Common Mode Rejection | $CMR$ | 70 | 90 | — | dB | $R_S \le 10\text{k}\Omega$ |

## Typical Application Circuit (Guitar Overdrive Gain Stage)

A symmetrical clipping feedback loop around the NJM4558 inverting stage (as found in classic guitar overdrive pedals):

```
                                  9V Battery
                                      │
                                [Pin 8: V+]
                                      │
  Guitar In ───[0.047µF]───[10k]───┬──┼──[500k Drive Pot]──┬──►[Pin 1: 1OUT]──► Output
                                   │  │                    │
                                   │  ├───►|──[1N4148]──|◄─┤ Symmetrical Diode
                                   │  └───|◄──[1N4148]───►|┤ Clipping Pair
                                   │                       │
                             [Pin 2: 1-IN]                 │
                             [Pin 3: 1+IN] ───[ 4.5V Virtual Ground ]
                             [Pin 4: V-]   ─── GND
```

## Common mistakes

- **Forgetting the 4.5V Virtual Ground in single 9V battery pedals:** When running from a single $9\text{V}$ battery ($V+ = 9\text{V}, V- = \text{GND}$), non-inverting inputs must be biased to half supply voltage ($4.5\text{V}$) via a voltage divider ($2 \times 10\text{k}\Omega$ resistors + $47\ \mu\text{F}$ capacitor). Connecting inputs directly to 0V GND cuts off half the AC audio waveform.
- **Assuming rail-to-rail output swing:** The NJM4558 cannot swing all the way to its supply rails. When powered from $+9\text{V}$ single supply, output clipping occurs at approx $+1.5\text{V}$ and $+7.5\text{V}$.
- **Unused second channel oscillation:** If only one op-amp channel is used (e.g. Channel 1), leave Channel 2 configured as a voltage follower with its non-inverting input ($2+IN$) tied to $4.5\text{V}$ or GND. Leaving it floating causes power supply noise and instability.

## Notes

- **NJM4558 vs RC4558 vs LM358:** NJM4558 (JRC4558) is optimized for dual supply audio; RC4558 is Texas Instruments' equivalent; LM358 is optimized for single supply ground-sensing DC control.
