## Overview

The **LM358** (and DIP-8 **LM358N**) is an industry-standard dual operational amplifier IC manufactured by Texas Instruments, ON Semiconductor, and STMicroelectronics. Ubiquitous across sensor breakout boards (such as ZMPT101B AC voltage modules, LM393/LM358 sound/vibration modules, active analog filters, and microphone pre-amps), it contains two independent, high-gain, internally frequency-compensated op-amps.

Designed to operate from either a **single supply ($3.0\text{V}$ to $32.0\text{V}$ DC)** or **split supplies ($\pm 1.5\text{V}$ to $\pm 16.0\text{V}$)**, the LM358's common-mode input range includes ground ($0\text{V}$), making it ideal for single-supply $5\text{V}$ or $3.3\text{V}$ microcontroller applications.

## Quick reference

| | |
|---|---|
| **Op-Amp Channels** | 2 Independent Operational Amplifiers |
| **Package** | 8-pin DIP / SOIC-8 / MSOP-8 |
| **Single Supply Voltage Range** | $3.0\text{ V}$ to $32.0\text{ V}$ DC |
| **Split Supply Voltage Range** | $\pm 1.5\text{ V}$ to $\pm 16.0\text{ V}$ DC |
| **Gain-Bandwidth Product (GBW)**| $1.0\text{ MHz}$ |
| **Slew Rate** | $0.3\text{ V}/\mu\text{s}$ |
| **Input Offset Voltage** | $2.0\text{ mV}$ typical / $5.0\text{ mV}$ max |
| **Input Common-Mode Range** | Includes Ground ($0\text{V}$) on single supply |
| **Quiescent Supply Current** | $500\ \mu\text{A}$ typical (independent of supply voltage) |

## Pinout (DIP-8 Package)

```
             ┌───┴───┐
      OUTPUT A ─┤ 1   8 ├─ VCC (+VCC)
    -INPUT A ─┤ 2   7 ├─ OUTPUT B
    +INPUT A ─┤ 3   6 ├─ -INPUT B
  GND (-VCC) ─┤ 4   5 ├─ +INPUT B
             └───────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `OUTPUT A` | Op-Amp A Output |
| 2 | `-INPUT A` | Op-Amp A Inverting Input |
| 3 | `+INPUT A` | Op-Amp A Non-Inverting Input |
| 4 | `GND` / `-VCC` | Ground reference (0 V) or Negative Power Supply ($-\text{V}_{CC}$) |
| 5 | `+INPUT B` | Op-Amp B Non-Inverting Input |
| 6 | `-INPUT B` | Op-Amp B Inverting Input |
| 7 | `OUTPUT B` | Op-Amp B Output |
| 8 | `VCC` / `+VCC` | Positive Power Supply Input ($+3.0\text{V} \dots +32\text{V}$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Single Supply Voltage | $V_{CC}$ | 3.0 | 5.0 | 32.0 | V | DC |
| Quiescent Current | $I_{CC}$ | — | 500 | 700 | µA | Over full supply range |
| Input Offset Voltage | $V_{IO}$ | — | 2.0 | 5.0 | mV | $T_A = 25^\circ\text{C}$ |
| Input Bias Current | $I_{IB}$ | — | 45 | 100 | nA | $V_{CM} = 0\text{V}$ |
| Large Signal Voltage Gain| $A_{VD}$ | 25 | 100 | — | V/mV | $V_{CC} = 15\text{V}, R_L \ge 2\text{k}\Omega$ |
| Common-Mode Rejection | $CMRR$ | 65 | 80 | — | dB | $V_{CM} = 0\text{V} \dots V_{CC}-1.5\text{V}$ |
| Output Voltage Swing High| $V_{OH}$ | $V_{CC}-1.5$| $V_{CC}-1.2$| — | V | $R_L = 2\text{k}\Omega, V_{CC} = 5.0\text{V}$ |
| Output Voltage Swing Low | $V_{OL}$ | — | 5 | 20 | mV | $R_L = 10\text{k}\Omega, V_{CC} = 5.0\text{V}$ |

## Common Op-Amp Circuit Configurations

### Non-Inverting Amplifier

$$ V_{OUT} = V_{IN} \times \left( 1 + \frac{R_f}{R_{in}} \right) $$

### Inverting Amplifier

$$ V_{OUT} = -V_{IN} \times \left( \frac{R_f}{R_{in}} \right) $$

### Unity-Gain Voltage Follower (Buffer)

Connect `OUTPUT` directly to `-INPUT`. $V_{OUT} = V_{IN}$ with high input impedance and low output impedance.

## Common mistakes

- **Expecting Rail-to-Rail Output Swing on $V_{CC}$:** The LM358 is NOT a rail-to-rail output op-amp. On a single $5.0\text{V}$ power supply, its maximum output voltage swings up to **$\sim 3.5\text{V} \dots 3.7\text{V}$** ($V_{CC} - 1.5\text{V}$). For full $0\text{V} \dots 5.0\text{V}$ rail-to-rail output swing, use a rail-to-rail op-amp like the MCP6002 or LMC6482.
- **Leaving unused op-amp channels floating:** Leaving an unused op-amp channel floating causes high-frequency oscillations and excessive power supply noise. Connect `-INPUT` directly to `OUTPUT` (unity gain buffer) and connect `+INPUT` to a fixed DC bias voltage (or ground).

## Notes

- **LM358 vs LM324 vs NE5532:** LM358 is a dual general-purpose op-amp; LM324 is a quad (4-channel) version of the LM358; NE5532 is a low-noise high-speed audio op-amp.
