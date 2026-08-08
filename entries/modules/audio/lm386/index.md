## Overview

The **LM386** (and DIP-8 **LM386N-1**) is an iconic low-voltage audio power amplifier IC manufactured by Texas Instruments. Bundled in Elegoo, SunFounder, and generic Arduino starter kits (both as a bare 8-pin DIP chip and as a ready-to-use breakout module with a volume potentiometer), it drives small $4\ \Omega \dots 32\ \Omega$ speakers in battery-powered audio devices, DIY radios, intercoms, and synthesizer projects.

Operating on a wide voltage supply range of **$4.0\text{V}$ to $12.0\text{V}$ DC** (up to 18V for LM386N-4), the LM386 features an internally set voltage gain of **20 ($26\text{ dB}$)**, which can be increased up to **200 ($46\text{ dB}$)** by adding a single $10\ \mu\text{F}$ electrolytic capacitor between pins 1 and 8.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VS`)** | 4.0 V to 12.0 V DC (LM386N-1) / up to 18.0 V DC (LM386N-4) |
| **Output Power** | $700\text{ mW}$ ($0.7\text{W}$) into $8\ \Omega$ speaker at $9\text{V}$ supply |
| **Quiescent Current** | $4.0\text{ mA}$ typical (low battery drain) |
| **Default Voltage Gain** | 20 ($26\text{ dB}$, pins 1 & 8 left open) |
| **Maximum Voltage Gain** | 200 ($46\text{ dB}$, $10\ \mu\text{F}$ capacitor across pins 1 & 8) |
| **Total Harmonic Distortion (THD)**| $0.2\%$ typical at $P_{OUT} = 125\text{ mW}, f = 1\text{ kHz}$ |
| **Compatible Speakers** | $4\ \Omega, 8\ \Omega, 16\ \Omega, 32\ \Omega$ dynamic speakers |

## Pinout (DIP-8 Package)

```
             ┌───┴───┐
       GAIN ─┤ 1   8 ├─ GAIN
     -INPUT ─┤ 2   7 ├─ BYPASS
     +INPUT ─┤ 3   6 ├─ VS (+VCC)
        GND ─┤ 4   5 ├─ VOUT (Speaker)
             └───────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `GAIN` | Gain setting pin 1 (Connect $10\ \mu\text{F}$ cap to Pin 8 for 200x gain) |
| 2 | ` -INPUT` | Inverting audio signal input |
| 3 | ` +INPUT` | Non-inverting audio signal input (Connect audio source via 10k potentiometer) |
| 4 | `GND` | Ground reference (0 V) |
| 5 | `VOUT` | Amplified AC audio output pin (Connect to speaker through $250\ \mu\text{F}$ cap) |
| 6 | `VS` | Positive DC supply power input (+4V to +12V DC) |
| 7 | `BYPASS` | Decoupling bypass pin (Connect $10\ \mu\text{F}$ cap to GND to prevent hum) |
| 8 | `GAIN` | Gain setting pin 2 |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (LM386N-1) | $V_S$ | 4.0 | 9.0 | 12.0 | V | DC |
| Supply Current (Quiescent)| $I_S$ | — | 4.0 | 8.0 | mA | $V_S = 6\text{V}, V_{IN} = 0$ |
| Output Power ($8\ \Omega, 9\text{V}$)| $P_{OUT}$ | 500 | 700 | — | mW | THD = 10% |
| Default Voltage Gain | $A_V$ | 15 | 20 | 25 | V/V | Pins 1 & 8 open |
| Max Voltage Gain | $A_{V\_max}$| — | 200 | — | V/V | $10\ \mu\text{F}$ cap across pins 1 & 8 |
| Input Resistance | $R_{IN}$ | — | 50 | — | kΩ | Audio input impedance |

## Basic Application Circuit (Gain = 20 vs Gain = 200)

```
        +9V Power Supply
           │
        [Pin 6: VS]
        LM386N
        [Pin 4: GND] ─── GND
           │
  Audio In ├─── [10k Potentiometer] ─── [Pin 3: +INPUT]
           │
        [Pin 5: VOUT] ─── [220µF Cap] ─── (+) [ 8Ω SPEAKER ] (-) ─── GND
```

- **Gain = 20 (Standard Audio Input):** Leave Pin 1 and Pin 8 **unconnected**.
- **Gain = 200 (Weak Microphone Input):** Connect the positive lead of a **$10\ \mu\text{F}$ electrolytic capacitor to Pin 1** and negative lead to **Pin 8**.

## Wiring (Breakout Module)

| LM386 Module Pin | → | Arduino / Audio Source | Notes |
|---|---|---|---|
| `VCC` | | 5V / 9V DC | Power rail |
| `GND` | | GND | System ground |
| `IN`  | | Audio Source / DAC Pin | Connect via 10k volume potentiometer |
| `OUT` | | Speaker Terminals | Connect 8 ohm 0.5W speaker |

## Common mistakes

- **Forgetting the output DC blocking capacitor:** Pin 5 (`VOUT`) sits at half supply voltage ($V_S / 2$). Connecting an $8\ \Omega$ speaker directly to Pin 5 without a **$220\ \mu\text{F} \dots 470\ \mu\text{F}$ coupling capacitor** burns out the speaker coil and overheats the IC.
- **Power supply noise hum:** The LM386 is sensitive to ripple noise on the power rail. Connect a $10\ \mu\text{F}$ capacitor between Pin 7 (`BYPASS`) and GND to filter out power supply hum.

## Notes

- **LM386 vs PAM8403 vs TDA2822:** LM386 is a mono Class-AB amplifier ($0.7\text{W}$); PAM8403 is a stereo Class-D amplifier ($3\text{W}+3\text{W}$ at $90\%$ efficiency).
