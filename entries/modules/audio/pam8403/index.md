## Overview

The **PAM8403** is an ultra-compact $3\text{W} + 3\text{W}$ filterless dual-channel (stereo) Class-D audio power amplifier IC manufactured by Diodes Incorporated. Available as a tiny $15 \times 18\text{ mm}$ green breakout module (often equipped with an integrated rotary volume potentiometer and power switch), it is the most popular audio amplifier module for USB-powered speakers, portable Bluetooth audio players, arcade cabinets, and Raspberry Pi handheld consoles.

Operating on a **$2.5\text{V}$ to $5.5\text{V}$ DC supply** (ideal for $5\text{V}$ USB or single-cell Li-ion battery power), the PAM8403 delivers up to **$3.0\text{ Watts}$ per channel into $4\ \Omega$ speakers** with **$90\%$ electrical efficiency** and filterless Bridge-Tied Load (BTL) architecture.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 2.5 V to 5.5 V DC (5.0 V USB nominal) |
| **Channels** | Dual Stereo ($2 \times 3\text{W}$ Output Channels) |
| **Output Power** | $3.0\text{W}$ per channel into $4\ \Omega$ at $5.0\text{V}$ / $1.8\text{W}$ into $8\ \Omega$ |
| **Efficiency** | $> 90\%$ Class-D switching efficiency |
| **THD + Noise** | $< 0.1\%$ typical at $P_{OUT} = 1.0\text{W}, f = 1\text{ kHz}$ |
| **Quiescent Current** | $10\text{ mA}$ typical at $5.0\text{V}$ |
| **Shutdown Current** | $< 1.0\ \mu\text{A}$ (via `/SHDN` pin) |
| **Architecture** | Filterless Bridge-Tied Load (BTL) output |

## Pinout (SOP-16 Package & Module Terminals)

```
        ┌──────────────────┐
        │     PAM8403      │  (SOP-16 Package)
        └─┬───┬───┬───┬────┘
```

| Module Pin Label | Name | Type | Description |
|---|---|---|---|
| `5V` / `VCC` | `VDD` | Power | Positive supply power input (+2.5 V to +5.5 V DC) |
| `GND` | `PGND` | Power | Ground reference (0 V) |
| `L` | `LIN` | Analog Input | Left Channel audio input |
| `G` | `AGND` | Analog Input | Audio input signal ground |
| `R` | `RIN` | Analog Input | Right Channel audio input |
| `L+` / `L-` | `OUTL+` / `OUTL-` | Speaker Output | Left Channel Bridge-Tied Load (BTL) speaker outputs |
| `R+` / `R-` | `OUTR+` / `OUTR-` | Speaker Output | Right Channel Bridge-Tied Load (BTL) speaker outputs |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 2.5 | 5.0 | 5.5 | V | DC |
| Continuous Output Power | $P_{OUT1}$| — | 3.0 | — | W | $R_L = 4\ \Omega, V_{DD} = 5.0\text{V}, THD=10\%$ |
| Continuous Output Power | $P_{OUT2}$| — | 1.8 | — | W | $R_L = 8\ \Omega, V_{DD} = 5.0\text{V}, THD=10\%$ |
| Quiescent Current | $I_Q$ | — | 10 | 16 | mA | $V_{DD} = 5.0\text{V}$, no load |
| Shutdown Current | $I_{sd}$ | — | 0.4 | 1.0 | µA | `/SHDN` pulled Low to GND |
| Power Supply Rejection | $PSRR$ | — | 64 | — | dB | $f = 1\text{ kHz}$ |

## Filterless BTL Output Topology

The PAM8403 uses a **Bridge-Tied Load (BTL)** output stage. Speaker leads (`L+`/`L-` and `R+`/`R-`) drive both sides of the speaker coil differentially.

> [!WARNING]
> Speaker Ground Rules:
> - **DO NOT CONNECT `L-` OR `R-` TO SYSTEM GND.**
> - **DO NOT BRIDGING `L-` AND `R-` TOGETHER.**
> - Each speaker must be wired independently across its dedicated `+` and `-` terminal pair. Connecting negative speaker terminals to GND or joining left/right negative leads short-circuits the BTL H-bridge output, instantly destroying the PAM8403.

## Wiring

| PAM8403 Module Pin | → | Power / Audio Source / Speaker | Notes |
|---|---|---|---|
| `5V` (`VCC`) | | 5V DC (USB Power / Li-ion Boost) | **Do not exceed 5.5V** |
| `GND` | | Power GND | System ground |
| `L` | | Left Audio Channel (3.5mm Headphone Jack Left) | Input audio signal |
| `G` | | Audio Ground (3.5mm Headphone Jack Shield) | Input signal ground |
| `R` | | Right Audio Channel (3.5mm Headphone Jack Right)| Input audio signal |
| `L+` / `L-` | | 4 Ohm / 8 Ohm Left Speaker | Independent Left Speaker |
| `R+` / `R-` | | 4 Ohm / 8 Ohm Right Speaker | Independent Right Speaker |

## Common mistakes

- **Connecting power exceeding 5.5V:** The PAM8403 has an absolute maximum supply rating of **$6.0\text{V}$**. Supplying 9V or 12V DC causes immediate chip burnout.
- **Shorting speaker negative pins (`L-` / `R-`) to ground:** Common ground 3.5mm headphone sockets cannot be connected directly to the output terminals. Connect speakers directly across `L+`/`L-` and `R+`/`R-`.

## Notes

- **PAM8403 vs LM386 vs TPA3116D2:** PAM8403 is $3\text{W}+3\text{W}$ Class-D (5V USB); LM386 is $0.7\text{W}$ mono Class-AB (9V); TPA3116D2 is $50\text{W}+50\text{W}$ Class-D (12V–24V).
