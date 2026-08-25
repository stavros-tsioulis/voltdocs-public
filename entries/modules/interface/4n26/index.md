## Overview

The **4N26** (along with 4N25, 4N27, and 4N28) is an industry-standard general-purpose 6-pin DIP optocoupler (optoisolator) manufactured by Vishay, onsemi, Lite-On, and Everlight. It consists of a gallium arsenide (GaAs) infrared light-emitting diode optically coupled to a silicon NPN phototransistor in a 6-pin through-hole **DIP-6** and surface-mount **SMD-6** package.

Providing up to **$5000\text{ V}_{RMS}$ of galvanic isolation** between the input LED and output transistor, the key distinguishing feature of the 4N26 compared to 4-pin optocouplers (like the PC817) is that its **phototransistor base terminal is brought out to Pin 6**. This allows designers to connect a base-emitter bleed resistor to dramatically speed up turn-off switching times or bias the base for linear AC zero-crossing detection. The 4N26 is widely used in **MIDI instrument input isolation, AC mains zero-cross detectors, SMPS feedback networks, industrial PLC 24V inputs, and microprocessor ground-loop breaking**.

## Quick reference

| | |
|---|---|
| **Device Type** | GaAs IR LED to Silicon NPN Phototransistor Optocoupler |
| **Package** | 6-pin DIP (DIP-6 / PDIP-6) / SMD-6 |
| **Galvanic Isolation Voltage** | **$5000\text{ V}_{RMS}$** (1 minute test) |
| **Collector-Emitter Breakdown ($V_{CEO}$)**| **$30\text{ V}$ min** |
| **Input LED Forward Current ($I_F$)** | **$60\text{ mA}$ max** ($10\text{mA} \dots 20\text{mA}$ typical) |
| **Current Transfer Ratio (CTR)** | **$\ge 20\%$ min** ($50\% \dots 100\%$ typ at $I_F = 10\text{mA}$) |
| **Phototransistor Base Terminal** | **Accessible on Pin 6** (Allows base-drain resistor speedup) |
| **Switching Speed ($t_{on} / t_{off}$)**| **$2.0\ \mu\text{s} / 2.0\ \mu\text{s}$ typ** |
| **4-Pin Alternative** | **PC817** (4-pin optocoupler without base access) |

## Pinout (DIP-6 Package)

```
                            ┌───┴───┐
             (LED Anode)  A 1│ 1   6│ B (Phototransistor Base)
           (LED Cathode)  K 2│ 4N26│5│ C (Phototransistor Collector)
        (No Connection)  NC 3│ DIP-6│4│ E (Phototransistor Emitter)
                            └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `ANODE (A)` | LED Input (+) | Infrared LED anode (Driven with current via series resistor) |
| 2 | `CATHODE (K)`| LED Input (-) | Infrared LED cathode (Connect to ground or open-collector driver) |
| 3 | `NC` | No Connect | Unconnected internal lead |
| 4 | `EMITTER (E)`| Transistor Out | Phototransistor emitter (Connect to ground or pulldown resistor) |
| 5 | `COLLECTOR (C)`| Transistor Out| Phototransistor collector (Connect to pull-up resistor or load) |
| 6 | `BASE (B)` | Transistor Base| Phototransistor base (Leave floating, or tie resistor to Pin 4 to speed up switching) |

## Typical Application Circuit: Standard Microcontroller Galvanic Logic Isolator

```
  +5V Transmitting Logic                       +3.3V / +5V Isolated Logic
           │                                                │
    [ 220Ω - 330Ω ]                                 [ 4.7kΩ - 10kΩ Pull-Up ]
           │                                                │
           ├───► [Pin 1: ANODE]                             ├───► Isolated Logic Out (to MCU GPIO)
           │        4N26                                    │
  MCU GPIO ┴───► [Pin 2: CATHODE]                  [Pin 5: COLLECTOR]
                                                        4N26
                                                   [Pin 4: EMITTER] ──► Isolated GND
                                                   [Pin 6: BASE]
                                                        │
                                          [ Optional 100kΩ - 470kΩ ] ──► Isolated GND (Speeds up turn-off)
```

## Comparison: 4N26 vs 4N25 vs 4N35 vs PC817

| Parameter | 4N26 | 4N25 | 4N35 | PC817 |
|---|---|---|---|---|
| **Package** | 6-Pin DIP | 6-Pin DIP | 6-Pin DIP | **4-Pin DIP (Compact)** |
| **Base Pin Out** | **Yes (Pin 6)** | **Yes (Pin 6)** | **Yes (Pin 6)** | No (Floating Base) |
| **CTR Minimum** | **$20\%$** | $20\%$ | **$100\%$ (High CTR)** | $50\%$ |
| **Isolation Voltage**| **$5000\text{ V}_{RMS}$** | $5000\text{ V}_{RMS}$ | $5000\text{ V}_{RMS}$ | $5000\text{ V}_{RMS}$ |

## Common mistakes

- **Leaving Pin 6 (Base) floating in high-noise environments without awareness:** When Pin 6 is left open, the high base impedance makes the phototransistor sensitive to external electrostatic or magnetic noise pickup. In noisy industrial environments, placing a **$100\text{k}\Omega \dots 1\text{M}\Omega$ resistor between Pin 6 (Base) and Pin 4 (Emitter)** bleeds off stray charge and substantially increases switching speed.
- **Exceeding LED reverse voltage ($V_R = 6.0\text{V}$):** In AC mains detection circuits, always place a standard 1N4148 diode in anti-parallel across Pins 1 and 2 to protect the GaAs LED from reverse voltage breakdown on the negative AC half-cycle.

## Notes

- **MIDI Standard:** The classic MIDI specification specifically prescribes 6-pin/8-pin optocouplers (such as 4N26, 4N28, or 6N138) on all MIDI IN DIN-5 jacks to ensure absolute ground isolation between musical instruments.
