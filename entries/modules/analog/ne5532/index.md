## Overview

The **NE5532** (NE5532P) is a dual high-performance operational amplifier IC manufactured by Texas Instruments and other leading semiconductor vendors. Renowned in the audio engineering industry as a standard workhorse, it offers exceptional AC and DC characteristics.

Featuring an ultra-low input noise voltage density of **$5\text{ nV}/\sqrt{\text{Hz}}$ at $1\text{ kHz}$**, a **$10\text{ MHz}$ gain bandwidth product**, a high slew rate of **$9\text{ V}/\mu\text{s}$**, and the ability to drive $600\ \Omega$ loads directly, the NE5532 is heavily utilized in high-end audio preamplifiers, studio mixing consoles, active crossovers, equalizers, and precision instrumentation.

## Quick reference

| | |
|---|---|
| **Channels** | 2 (Dual Operational Amplifier) |
| **Supply Voltage (Split Rail)** | $\pm 3\text{ V}$ to $\pm 20\text{ V}$ DC |
| **Supply Voltage (Single Rail)** | $6\text{ V}$ to $40\text{ V}$ DC |
| **Gain Bandwidth Product** | $10\text{ MHz}$ |
| **Slew Rate** | $9\text{ V}/\mu\text{s}$ |
| **Equivalent Input Noise** | $5\text{ nV}/\sqrt{\text{Hz}}$ at $1\text{ kHz}$ |
| **Output Load Drive** | $600\ \Omega$ load capability at $10\text{ V}_{\text{RMS}}$ |
| **Package** | 8-pin DIP / SOIC-8 |

## Pinout (DIP-8 / SOIC-8 Package)

```
             ┌───┴───┐
       1OUT 1│ 1   8 │ V+ (VCC)
      1IN-  2│       │ 7 2OUT
      1IN+  3│ NE5532│ 6 2IN-
   V- (GND) 4│       │ 5 2IN+
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `1OUT` | Analog Output | Op-Amp 1 Output |
| 2 | `1IN-` | Analog Input | Op-Amp 1 Inverting Input |
| 3 | `1IN+` | Analog Input | Op-Amp 1 Non-Inverting Input |
| 4 | `V-` | Power | Negative Supply ($V-$ or GND for single supply) |
| 5 | `2IN+` | Analog Input | Op-Amp 2 Non-Inverting Input |
| 6 | `2IN-` | Analog Input | Op-Amp 2 Inverting Input |
| 7 | `2OUT` | Analog Output | Op-Amp 2 Output |
| 8 | `V+` | Power | Positive Supply ($V+$ or $V_{CC}$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Split) | $V_{CC\pm}$ | $\pm 3$ | $\pm 15$ | $\pm 20$ | V | Dual power rails |
| Input Noise Voltage | $e_n$ | — | 5.0 | 8.0 | nV/√Hz | $f = 1\text{ kHz}$ |
| Unity Gain Bandwidth | $GBW$ | 8.0 | 10.0 | — | MHz | $V_{CC} = \pm 15\text{V}$ |
| Slew Rate | $SR$ | 6.0 | 9.0 | — | V/µs | $V_{CC} = \pm 15\text{V}, R_L = 600\ \Omega$ |
| Input Bias Current | $I_{IB}$ | — | 200 | 800 | nA | $T_A = 25^\circ\text{C}$ |
| Input Offset Voltage | $V_{IO}$ | — | 0.5 | 4.0 | mV | $T_A = 25^\circ\text{C}$ |
| Quiescent Supply Current | $I_{CC}$ | — | 8.0 | 16.0 | mA | Dual op-amp total, no load |

## Typical Applications

### Audio Preamplifier Circuit (Non-Inverting Gain = 11)

```
        Audio Input ───► [3: 1IN+] ──┐
                                     │   NE5532
                                     ├───► [1: 1OUT] ───► Audio Output
                                     │
                        [2: 1IN-] ───┼─── R_feedback (10k) ───┐
                                     │                        │
                                     └─── R_ground (1k) ──────┴── GND
```

## Common mistakes

- **Operating with single supply without proper DC biasing:** The NE5532 is a bipolar-input op-amp optimized for dual split rails ($\pm 15\text{V}$). When powered from a single supply (e.g. $12\text{V}$ and GND), inputs must be biased to half-supply ($V_{CC}/2$) with AC-coupling capacitors.
- **Ignoring high input bias current:** Unlike JFET op-amps (such as TL072 with picoamp bias currents), NE5532 has a bipolar input stage drawing around $200\text{ nA}$ input bias current. High input resistor values ($> 100\text{ k}\Omega$) can create noticeable DC offset errors.

## Notes

- **NE5532 vs TL072:** NE5532 has significantly lower voltage noise ($5\text{ nV}/\sqrt{\text{Hz}}$ vs $18\text{ nV}/\sqrt{\text{Hz}}$) and higher current drive, making it superior for low-impedance audio paths. TL072 has JFET inputs with near-zero input bias current, better suited for high-impedance guitar pickups or sensor buffers.
