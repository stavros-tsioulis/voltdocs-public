## Overview

The **TDA7052** is a 1W mono Bridge-Tied Load (BTL) audio power amplifier IC manufactured by NXP Semiconductors (originally Philips). Designed specifically for battery-operated portable equipment (such as handheld radios, walkie-talkies, small battery speakers, and microcontroller voice prompts), it operates over a supply range of **3.0V to 18.0V DC**.

Utilizing a **Bridge-Tied Load (BTL)** output architecture, the speaker is connected differentially between two internal output amplifiers (`OUT1` and `OUT2`). This quadruples the output power compared to a single-ended amplifier at the same supply voltage and **eliminates the large output DC-blocking capacitor**, dramatically reducing PCB component count and physical size.

## Quick reference

| | |
|---|---|
| **Amplifier Type** | Mono Bridge-Tied Load (BTL) Audio Amplifier |
| **Output Power** | $1.2\text{ W}_{\text{RMS}}$ into $8\ \Omega$ load at $V_P = 6.0\text{V}$ ($2.0\text{W}$ into $8\ \Omega$ at $9.0\text{V}$) |
| **Supply Voltage (`VP`)** | 3.0 V to 18.0 V DC (Optimal battery supply $6.0\text{V}$) |
| **Quiescent Current** | $4.0\text{ mA}$ typical (Ultra-low standby battery drain) |
| **Fixed Voltage Gain** | $39\text{ dB}$ (Internal fixed gain — no external feedback resistors required) |
| **External Capacitor Requirement**| NO output coupling capacitors needed |
| **Package** | 8-pin DIP / SOIC-8 |

## Pinout (DIP-8 Package)

```
             ┌───┴───┐
        VP  1│ 1   8 │ GND3
      OUT1  2│       │ 7 OUT2
      GND1  3│TDA7052│ 6 NC
       IN+  4│       │ 5 GND2
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VP` | Power | Positive DC Power Supply (+3.0V to +18.0V DC) |
| 2 | `OUT1` | Output | Positive BTL Speaker Output (+) |
| 3 | `GND1` | Power | Ground Reference |
| 4 | `IN+` | Input | Audio Signal Input |
| 5 | `GND2` | Power | Ground Reference |
| 6 | `NC` | Unused | No Internal Connection |
| 7 | `OUT2` | Output | Negative BTL Speaker Output (-) |
| 8 | `GND3` | Power | Ground Reference |

## Minimal 6V Battery Application Circuit

```
  Audio Input ───[ 0.47µF Film Cap ]───► [Pin 4: IN+]
                                           TDA7052
  +6V DC Battery ──────────────────────► [Pin 1: VP]
  Battery GND ─────────────────────────► [Pins 3, 5, 8: GND]

  [Pin 2: OUT1] ───────────────────────► ( + ) $8\ \Omega$ Speaker
  [Pin 7: OUT2] ───────────────────────► ( - ) $8\ \Omega$ Speaker
```

## Common mistakes

- **Connecting BTL speaker outputs (`OUT1` or `OUT2`) to Ground:** Because the speaker is driven differentially across `OUT1` and `OUT2` (both resting at $V_P / 2$), grounding either terminal creates an immediate DC short-circuit that damages the IC.
- **Connecting a headphone jack with shared ground:** Headphone jacks share a common ground terminal between left and right channels. BTL outputs cannot drive shared-ground headphones directly.

## Notes

- **TDA7052 vs TDA7052A:** TDA7052 has a fixed $39\text{ dB}$ gain; TDA7052A includes an internal DC-voltage controlled volume control circuit on Pin 4 ($0\text{V} \dots 1.4\text{V}$ volume adjustment).
