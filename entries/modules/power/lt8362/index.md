## Overview

The **LT8362** (LT8362EMSE / LT8362HDD) is a high-efficiency 60V, 2A low-EMI switching regulator IC manufactured by Analog Devices (Linear Technology). Packaged in a compact **16-lead MSOP** or **10-lead DFN** ($3 \times 3\text{ mm}$), it can be configured in **Boost**, **SEPIC** (Step-Up/Step-Down), or **Inverting (Negative Output)** topologies.

Operating over a wide input supply voltage range of **2.8V to 60.0V DC**, the LT8362 features an integrated **60V, 2.0A power switch**, an ultra-low **$9\ \mu\text{A}$ quiescent current** in Burst Mode operation, Spread Spectrum Frequency Modulation (SSFM) for low-EMI compliance, and programmable switching frequencies from **300 kHz to 2.0 MHz**.

## Quick reference

| | |
|---|---|
| **Input Supply Voltage (`VIN`)** | 2.8 V to 60.0 V DC |
| **Output Voltage Limit** | Up to $60.0\text{ V}$ DC (Positive or Negative output) |
| **Integrated Power Switch** | $60\text{ V}, 2.0\text{ A}$ continuous switch rating |
| **Quiescent Current (`IQ`)** | $9\ \mu\text{A}$ typical (Burst Mode operation) |
| **Programmable Frequency** | $300\text{ kHz}$ to $2.0\text{ MHz}$ (Syncable to external clock) |
| **EMI Mitigation** | Spread Spectrum Frequency Modulation (SSFM) |
| **Topologies Supported** | Boost, SEPIC, Inverting (Single feedback pin `FB` senses positive or negative output) |
| **Package** | 16-lead MSOP (PowerPAD) / 10-lead DFN ($3 \times 3\text{ mm}$) |

## Pinout (16-Lead MSOP Package — PowerPAD)

```
                       ┌─────────────┐
                 [EN] 1│ 1        16│ [SW] (Switch Drain Output 60V)
               [SYNC] 2│            │15 [SW]
                [BIAS]3│   LT8362   │14 [VIN] (2.8V to 60V Input)
               [INTVCC]4│   MSOP-16E │13 [VIN]
                 [FB] 5│            │12 [GND]
                 [SS] 6│            │11 [GND]
                 [RT] 7│            │10 [VC] (Compensation Node)
                 [NC] 8│            │9  [NC]
                       └─────────────┘
```

| Pin Name | Type | Description |
|---|---|---|
| `EN/UVLO` | Input | Active-HIGH Enable & Undervoltage Lockout Input |
| `SYNC/MODE` | Input | Clock Synchronization & Mode Select (Burst Mode / Pulse-Skipping / SSFM) |
| `BIAS` | Input | Internal Regulator Bias Power Input (Connect to Output for higher efficiency) |
| `INTVCC` | Power | Internal $3.2\text{V}$ LDO Regulator Output (Bypass with 1.0µF capacitor) |
| `FB` | Input | Single Feedback Input Pin (Senses Positive or Negative Output Voltages) |
| `SS` | Input | Soft-Start Programming Pin (Connect capacitor to GND) |
| `RT` | Input | Frequency Programming Resistor Pin (Connect resistor $R_T$ to GND) |
| `VC` | Output | Error Amplifier Output Node for Loop Compensation |
| `VIN` | Power | Main Power Supply Input (+2.8V to +60V DC) |
| `SW` | Output | Internal 60V 2A Power Switch Drain Pins |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Operating Supply Voltage | $V_{IN}$ | 2.8 | 12.0/24.0| 60.0 | V | DC |
| Switch Current Limit | $I_{SW}$ | 2.0 | 2.5 | — | A | $V_{IN} = 12\text{V}$ |
| Switch On-Resistance | $R_{DS(on)}$| — | 165 | 240 | mΩ | $V_{INTVCC} = 3.2\text{V}$ |
| Positive Feedback Voltage | $V_{FB+}$ | 1.57 | 1.60 | 1.63 | V | Positive Output Mode |
| Negative Feedback Voltage | $V_{FB-}$ | -10 | 0 | +10 | mV | Negative Output Mode ($V_{FB}$ grounded through internal resistor) |

## Common mistakes

- **Forgetting ground plane connection on MSOP PowerPAD:** Thermal dissipation at $2\text{A}$ switch currents relies on soldering the exposed metal pad beneath the MSOP-16E package to a solid PCB ground plane.
- **Applying $> 60\text{V}$ to SW pins:** Inductive ringing spikes on `SW` (Pin 15/16) must not exceed $60\text{V}$. Use a snubber circuit in high-voltage SEPIC/Boost configurations.

## Notes

- **LT8362 vs LM2577:** LT8362 operates at 2.0 MHz with 9µA quiescent current and low EMI SSFM in a tiny 3x3mm DFN package; LM2577 is a legacy 52kHz bulky TO-220 part.
