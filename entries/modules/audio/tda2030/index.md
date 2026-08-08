## Overview

The **TDA2030** is a classic monolithic integrated circuit in a 5-pin Pentawatt package intended for use as a Class-AB audio power amplifier. Manufactured by STMicroelectronics, it delivers up to **14W of output power** into a $4\ \Omega$ load or $9\W$ into an $8\ \Omega$ load at a supply voltage of $\pm 14\text{V}$ or $+28\text{V}$ single supply.

The chip incorporates short-circuit protection and an automatic thermal shutdown mechanism to protect against overheating. It is widely found in low-cost active multimedia speakers, home audio amplifiers, and standalone DIY audio breakout modules.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VS`)** | 12.0 V to 36.0 V DC (Single Supply) or $\pm 6\text{V}$ to $\pm 18\text{V}$ (Split Supply) |
| **Output Power** | $14\text{W}$ RMS into $4\ \Omega$ ($VS = \pm 14\text{V}, \text{THD} = 0.5\%$) |
| **Total Harmonic Distortion (THD)** | $0.08\%$ typical ($P_{OUT} = 0.1 \dots 10\text{W}, f = 1\text{kHz}$) |
| **Frequency Response** | $20\text{ Hz}$ to $140\text{ kHz}$ ($-3\text{ dB}$) |
| **Peak Output Current** | $3.5\text{ A}$ (internally limited) |
| **Quiescent Current** | $50\text{ mA}$ typical |

## Pin configuration (Pentawatt Package)

```
        ┌───┴───┐
      1 │  +IN  │ Non-inverting Input
      2 │  -IN  │ Inverting Input
      3 │  -VS  │ Negative Supply / Ground (Single Supply)
      4 │  OUT  │ Amplified Audio Output
      5 │  +VS  │ Positive Supply
        └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `+IN` | Input | Non-inverting audio signal input |
| 2 | `-IN` | Input | Inverting audio signal input (feedback network connection) |
| 3 | `-VS` | Power | Negative supply voltage pin (or GND in single-supply mode) |
| 4 | `OUT` | Output | Amplified audio output to speaker (via decoupling cap for single supply) |
| 5 | `+VS` | Power | Positive supply voltage pin (+12V to +36V DC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage Range | $V_S$ | 12.0 | 28.0 | 36.0 | V | Single supply mode |
| Quiescent Drain Current | $I_d$ | — | 50 | 80 | mA | $V_S = \pm 14\text{V}$ |
| Output Power ($4\ \Omega$) | $P_o$ | 12 | 14 | — | W | $d = 0.5\%, f = 1\text{kHz}$ |
| Output Power ($8\ \Omega$) | $P_o$ | 8 | 9 | — | W | $d = 0.5\%, f = 1\text{kHz}$ |
| Input Resistance | $R_i$ | 0.5 | 5.0 | — | MΩ | Pin 1 / Pin 2 |
| Thermal Shutdown Temp | $T_j$ | — | 145 | — | °C | Junction temperature |

## Typical Application Circuit (Single Supply 28V)

```
                       +28V Power Supply
                          │
                       [Pin 5: +VS]
                          │
  Audio In ───[1µF Cap]─┬─┤ [Pin 1: +IN]
                        │ │
                      [R_in] [Pin 4: OUT] ───[2000µF Cap]─── (+) [ 4Ω / 8Ω SPEAKER ] (-) ─── GND
                        │ │
                       GND┤ [Pin 2: -IN] ───[Feedback R/C Network]───┤
                          │                                           │
                       [Pin 3: -VS] ───────────────────────────────── GND
```

## Common mistakes

- **Operating without a heatsink:** The TDA2030 generates substantial heat when driving speakers at high volume. Running the IC without a heatsink attached to its metal tab will trigger thermal shutdown almost immediately or damage the device.
- **Forgetting output clamp diodes on legacy TDA2030:** Unlike TDA2030A, the original TDA2030 requires external flyback/protection diodes (1N4001) connected between Output (Pin 4) and +VS/GND to protect the output transistors against inductive speaker kickback voltages.
- **Forgetting output AC coupling capacitor in single-supply mode:** Pin 4 DC offset is half the supply voltage ($V_S / 2$). Connecting a speaker directly to Pin 4 in a single-supply configuration without a $1000\ \mu\text{F} \dots 2200\ \mu\text{F}$ electrolytic capacitor will burn out the speaker.

## Notes

- **TDA2030 vs TDA2030A:** TDA2030A is a higher-voltage variant ($V_S$ up to $\pm 22\text{V} / 44\text{V}$ single supply, output up to 18W) with internal clamping diodes.
