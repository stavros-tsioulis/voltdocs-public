## Overview

The **TDA2822** (and 8-pin mini-DIP **TDA2822M**) is a dual low-voltage audio power amplifier IC manufactured by STMicroelectronics. Designed for portable battery-powered cassette players, radios, intercoms, and active computer speakers, it operates over a wide supply voltage range from **1.8V to 15.0V DC** with a low crossover distortion and a low quiescent current of **6mA**.

The chip can be configured in two distinct modes:
1. **Stereo Mode:** Drives two independent $4\ \Omega \dots 32\ \Omega$ channels (speakers or headphones) delivering up to $1.0\text{W}$ per channel at $9\text{V}$ supply.
2. **Bridge-Tied Load (BTL) Mono Mode:** Combines both internal amplifiers to double output voltage swing, delivering up to **$2.0\text{W}$ into an $8\ \Omega$ speaker** without requiring output DC blocking capacitors.

## Quick reference

| | |
|---|---|
| **Operating Supply Voltage (`VCC`)** | 1.8 V to 15.0 V DC (TDA2822M) / up to 12.0 V (TDA2822) |
| **Output Power (Stereo 4Ω)** | $0.65\text{W} + 0.65\text{W}$ at $6\text{V}$ / $1.0\text{W} + 1.0\text{W}$ at $9\text{V}$ |
| **Output Power (BTL Mono 8Ω)** | $1.35\text{W}$ at $6\text{V}$ / $2.0\text{W}$ at $9\text{V}$ |
| **Quiescent Current (`ICC`)** | $6.0\text{ mA}$ typical ($VCC = 6\text{V}$) |
| **Total Harmonic Distortion (THD)**| $0.2\%$ typical ($P_{OUT} = 0.5\text{W}, f = 1\text{kHz}$) |
| **Package** | 8-pin Minidip / SOIC-8 / Breakout Module |

## Pinout (TDA2822M DIP-8 / SOIC-8)

```
             ┌───┴───┐
       OUT1 1│ 1   8 │ OUT2
        VCC 2│       │ 7 +IN1
       OUT2 3│TDA2822│ 6 -IN1
        GND 4│   M   │ 5 -IN2
             └───────┘
```

*Note: Pin 1 and Pin 3 are internally shorted output connections for Channel 1/Channel 2 feedback networks depending on layout.*

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `OUT1` | Output | Channel 1 Amplifier Output |
| 2 | `VCC` | Power | Positive DC supply power input (+1.8V to +15.0V DC) |
| 3 | `OUT2` | Output | Channel 2 Amplifier Output |
| 4 | `GND` | Power | System ground reference (0 V) |
| 5 | `-IN2` | Input | Channel 2 Inverting Input |
| 6 | `+IN2` | Input | Channel 2 Non-Inverting Input |
| 7 | `+IN1` | Input | Channel 1 Non-Inverting Input |
| 8 | `-IN1` | Input | Channel 1 Inverting Input |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 1.8 | 6.0 | 15.0 | V | DC |
| Quiescent Supply Current | $I_{CC}$ | — | 6.0 | 12.0 | mA | $V_{CC} = 6.0\text{V}, R_L = \infty$ |
| Output Power (Stereo) | $P_O$ | 0.4 | 0.65 | — | W | $V_{CC}=6\text{V}, R_L=4\Omega, d=10\%$ |
| Output Power (BTL Mono) | $P_O$ | 0.9 | 1.35 | — | W | $V_{CC}=6\text{V}, R_L=8\Omega, d=10\%$ |
| Total Harmonic Distortion | $d$ | — | 0.2 | — | % | $V_{CC}=6\text{V}, R_L=4\Omega, P_O=0.5\text{W}$ |
| Closed Loop Voltage Gain | $G_V$ | 36 | 39 | 41 | dB | Stereo mode |

## Application Circuits

### 1. Stereo Application Circuit

```
  Left In  ───[10µF]─── [Pin 7: +IN1]    [Pin 1: OUT1] ───[470µF Cap]─── (+) [ LEFT SPEAKER 4Ω ] (-) ─── GND
                                TDA2822M
  Right In ───[10µF]─── [Pin 6: +IN2]    [Pin 3: OUT2] ───[470µF Cap]─── (+) [ RIGHT SPEAKER 4Ω ] (-) ── GND
                                [Pin 2: VCC] ─── +6V .. +9V DC
                                [Pin 4: GND] ─── GND
```

### 2. Bridge-Tied Load (BTL) Mono Application Circuit

In BTL mode, the speaker is connected directly **between Pin 1 (`OUT1`) and Pin 3 (`OUT2`)** without output DC blocking capacitors.

```
  Audio In ───[10µF]─── [Pin 7: +IN1]    [Pin 1: OUT1] ─────── (+) [ 8Ω SPEAKER ]
                                TDA2822M                            │
                        [Pin 6: +IN2]    [Pin 3: OUT2] ─────── (-) ─┘
                                [Pin 2: VCC] ─── +6V .. +9V DC
                                [Pin 4: GND] ─── GND
```

## Common mistakes

- **Forgetting output DC coupling capacitors in Stereo Mode:** In stereo mode, `OUT1` and `OUT2` rest at half supply voltage ($V_{CC} / 2$). Connecting speakers directly without $220\ \mu\text{F} \dots 470\ \mu\text{F}$ coupling capacitors will burn out the speaker voice coils.
- **Connecting speaker to GND in BTL Mono Mode:** In BTL mode, the speaker must be connected across `OUT1` and `OUT2`. Connecting either side of the speaker to GND in BTL mode shorts out one amplifier channel.
- **High high-frequency oscillation:** The TDA2822 has high gain. If wiring traces are long, add a **Boucherot cell** ($4.7\ \Omega$ resistor in series with a $100\text{ nF}$ ceramic capacitor) from `OUT1` and `OUT2` to GND to prevent high-frequency self-oscillation.

## Notes

- **TDA2822 vs LM386 vs PAM8403:** TDA2822 is a stereo/BTL Class-AB IC operating down to 1.8V (ideal for 2x AA batteries); LM386 is single-channel mono requiring $\ge 4\text{V}$; PAM8403 is a 3W stereo Class-D digital amplifier with high efficiency ($>90\%$).
