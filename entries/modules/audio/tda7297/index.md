## Overview

The **TDA7297** (packaged in a 15-pin vertical Multiwatt power package **TDA7297V**) is a $15\text{ W} + 15\text{ W}$ dual bridge audio power amplifier IC manufactured by STMicroelectronics. Extremely popular on low-cost $12\text{ V}$ DIY stereo amplifier breakout boards, it delivers $15\text{ W}$ continuous RMS power per channel into $8\ \Omega$ speakers from a single DC supply.

Because the TDA7297 uses a **Bridge-Tied Load (BTL)** output topology on both channels, it drives speakers directly between output terminal pairs without requiring large, expensive AC coupling capacitors.

## Quick reference

| | |
|---|---|
| **Amplifier Type** | Dual BTL Class-AB Stereo Audio Power Amplifier |
| **Package** | Multiwatt-15 (15-Pin Vertical Power Package) / Stereo Module |
| **Supply Voltage Range ($V_{CC}$)** | $6.0\text{ V}$ to $18.0\text{ V}$ DC ($12.0\text{ V} \dots 16.5\text{ V}$ recommended) |
| **Output Power ($P_{OUT}$)** | $15\text{ W} + 15\text{ W}$ RMS ($V_{CC} = 16.5\text{V}, R_L = 8\Omega, \text{THD} = 10\%$) |
| **Recommended Speaker Load** | $4\ \Omega$ to $8\ \Omega$ |
| **Total Harmonic Distortion** | $0.1\%$ typical ($P_O = 1\text{W}, f = 1\text{kHz}$) |
| **Control Functions** | Microprocessor-compatible Mute and Standby control pins |

## Pinout (Multiwatt-15 Package)

```
       ┌───────────────────────────────┐
       │            TDA7297            │  (Front Package Face)
       └─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬──┬──┬──┬──┘
         1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
```

| Pin | Name | Description |
|---|---|---|
| 1 | `OUT1+` | Channel 1 Positive BTL Output |
| 2 | `OUT1-` | Channel 1 Negative BTL Output |
| 3 | `VCC1` | Channel 1 Power Supply (+6V to +18V DC) |
| 4 | `IN1` | Channel 1 Audio Signal Input (via 220nF coupling cap) |
| 5 | `MUTE` | Mute Control Input (High = Play, Low = Muted) |
| 6 | `ST-BY` | Standby Control Input (High = Normal, Low = Standby Low-Power) |
| 7 | `S-GND` | Signal Ground reference |
| 8, 9 | `PW-GND` | Power Ground 1 and 2 |
| 10 | `SVR` | Supply Voltage Ripple Rejection (10µF cap to GND) |
| 11 | `IN2` | Channel 2 Audio Signal Input (via 220nF coupling cap) |
| 12 | `N.C.` | No Connection |
| 13 | `VCC2` | Channel 2 Power Supply (+6V to +18V DC) |
| 14 | `OUT2-` | Channel 2 Negative BTL Output |
| 15 | `OUT2+` | Channel 2 Positive BTL Output |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage Range | $V_{CC}$ | 6.0 | 12.0 | 18.0 | V | Operating DC supply |
| Continuous Output Power | $P_{OUT}$ | 13.0 | 15.0 | — | W | $V_{CC} = 16.5\text{V}, R_L = 8\Omega, \text{THD} = 10\%$ |
| Total Harmonic Distortion | $\text{THD}$ | — | 0.1 | 0.3 | % | $P_{OUT} = 1\text{W}, f = 1\text{kHz}, R_L = 8\Omega$ |
| Signal-to-Noise Ratio | $SNR$ | 80 | 90 | — | dB | $f = 1\text{kHz}$ |
| Quiescent Current | $I_Q$ | — | 50 | 65 | mA | No signal |
| Standby Current | $I_{STBY}$ | — | 100 | 300 | $\mu\text{A}$ | $V_{STBY} \le 1.5\text{V}$ |

## Typical Application Circuit (12V Stereo Amplifier)

```
       +12V DC Supply ────┬─── [Pin 3: VCC1] & [Pin 13: VCC2]
                          │
       Audio IN1 ── [220nF Cap] ── [Pin 4: IN1] ─── TDA7297 ─── [Pin 1: OUT1+] ──── ( Speaker 1 + )
                                                  │             [Pin 2: OUT1-] ──── ( Speaker 1 - )
                                                  │
       Audio IN2 ── [220nF Cap] ── [Pin 11: IN2] ──│─────────── [Pin 15: OUT2+] ─── ( Speaker 2 + )
                                                  │             [Pin 14: OUT2-] ─── ( Speaker 2 - )
                          GND ─── [Pin 8/9: PW-GND] & [Pin 7: S-GND]
```

## Common mistakes

- **Shorting speaker negative outputs (`OUT-`) to GND:** Because the TDA7297 uses Bridge-Tied Load outputs, both output terminals (`OUT+` and `OUT-`) carry DC bias. **NEVER connect speaker negative terminals to GND or to each other.**
- **Operating without a heatsink:** Generating 30W total output power requires an aluminum heatsink mounted to the Multiwatt-15 package tab. Running without a heatsink triggers thermal shutdown within seconds.

## Notes

- **TDA7297 vs TDA2030:** The TDA7297 is a dual-channel BTL amplifier (no output coupling caps required), whereas the TDA2030 is a single-channel amplifier.
