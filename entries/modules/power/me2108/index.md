## Overview

The **ME2108** (ME2108A33) is an ultra-low power Pulse-Frequency Modulation (PFM) step-up (boost) DC-DC converter IC manufactured by Nanjing Micro One Electronics (MicroOne). Housed in a tiny **3-pin SOT-23-3**, **SOT-89-3**, or **TO-92** package, it steps up single-cell or dual-cell battery voltages ($0.9\text{V} \dots 3.0\text{V}$ AA/AAA/NiMH batteries) to a fixed **3.3V DC** output voltage rail.

Drawing an ultra-low quiescent current of just **$5.5\ \mu\text{A}$**, the ME2108 is widely used in low-power microcontroller battery boards, wireless sensor nodes, electronic toys, and handheld meters.

## Quick reference

| | |
|---|---|
| **Input Voltage Range (`VIN`)** | 0.9 V to 5.0 V DC (Startup voltage $0.9\text{ V}$) |
| **Output Voltage (`VOUT`)** | Fixed **3.3 V DC** (`ME2108A33`) / Fixed 5.0V (`ME2108A50`) ($\pm 2\%$ accuracy) |
| **Quiescent Current (`IQ`)** | $5.5\ \mu\text{A}$ typical standby drain |
| **Switching Control** | PFM (Pulse-Frequency Modulation, up to $180\text{ kHz}$) |
| **Internal Switch** | Integrated N-channel power MOSFET (up to $400\text{ mA}$ switch current) |
| **Efficiency** | Up to $85\%$ typical |
| **Package** | SOT-23-3 / SOT-89-3 / TO-92 |

## Pinout (SOT-23-3 Package)

```
             ┌───┴───┐
       VSS  1│ 1   3 │ LX (Inductor Switch Node)
       OUT  2│       │
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VSS` | Power | Ground Reference (0 V) |
| 2 | `OUT` | Power / Sense | Fixed Voltage Output (3.3V DC) & Internal Feedback Sense Pin |
| 3 | `LX` | Output | Internal N-MOSFET Drain Switch Node (Connect to Inductor & Schottky Diode) |

## Standard Single-Cell Battery Boost Circuit

```
  Single AA Battery (+1.5V DC) ───[ Inductor 22µH to 47µH ]───┬─── [Pin 3: LX]
                                                               │
                                                       [Schottky Diode 1N5819]
                                                               │
  Regulated Output (+3.3V DC) ◄────────────────────────────────┼─── [Pin 2: OUT]
                                                               │
                                                      [10µF Capacitor to VSS]
```

## Common mistakes

- **Attempting to draw high currents ($> 150\text{mA}$) from a 0.9V input:** Single 1.5V AA batteries can supply up to $100\text{ mA} \dots 150\text{ mA}$ at 3.3V. Attempting to draw higher currents collapses the input battery voltage below the $0.9\text{V}$ cutoff.
- **Using slow silicon diodes instead of Schottky:** The PFM switching frequency ($180\text{ kHz}$) requires a low-forward-voltage Schottky diode (such as **1N5819** or **SS14**).

## Notes

- **ME2108 vs HT7733:** ME2108A33 and HT7733A are pin-compatible 3.3V PFM boost regulators designed for single-cell battery applications.
