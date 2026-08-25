## Overview

The **NCP1200** (including **NCP1200P44**, **NCP1200P60**, and **NCP1200P100**) is an innovative current-mode PWM controller IC engineered by onsemi for low-power off-line switch-mode power supplies (SMPS) and flyback converters. Housed in a through-hole **DIP-8** and surface-mount **SOIC-8** package, it revolutionized power supply design with its patented **Dynamic Self-Supply (DSS)** technology.

By integrating a high-voltage internal startup current source rated up to **$500\text{V}$** directly on Pin 8 (HV), the NCP1200 powers itself directly from the rectified high-voltage DC mains bus, completely eliminating the need for an auxiliary transformer winding, auxiliary diode, or bulky dropping resistors. Featuring automatic **Skip-Cycle standby mode** at light loads (consuming $< 100\text{mW}$ in standby), leading-edge current blanking, and cycle-by-cycle overcurrent protection, the NCP1200 is widely used in **AC-DC wall adapters, battery chargers, TV/monitor standby power supplies, smart meter auxiliary power, and SMPS repair projects**.

## Quick reference

| | |
|---|---|
| **Device Type** | Offline Current-Mode SMPS PWM Controller |
| **Package** | 8-pin DIP (DIP-8 / PDIP-8) / SOIC-8 |
| **High-Voltage Startup ($V_{HV}$)**| **$500\text{ V}$ max** (Direct Connection to High-Voltage DC Bus) |
| **Internal Operating Voltage ($V_{CC}$)**| **$11.0\text{ V}$ typ** (Regulated internally via DSS) |
| **Switching Frequencies** | **$40\text{ kHz}$ (P44)** / **$60\text{ kHz}$ (P60)** / **$100\text{ kHz}$ (P100)** |
| **Gate Driver Peak Current** | **$250\text{ mA}$ source / sink** (Direct power MOSFET drive) |
| **Standby Power Optimization** | Automatic Skip-Cycle Mode at light loads |
| **Protection Features** | Internal Thermal Shutdown, Cycle-by-Cycle Current Limit, Short-Circuit Protection |

## Pinout (DIP-8 Package)

```
                            ┌───┴───┐
     (Skip Adjust)   Adj   1│ 1    8│ HV (High-Voltage Startup / 500V)
     (Opto Feedback) FB    2│ NCP  7│ NC (High-Voltage Creepage Gap)
     (Current Sense) CS    3│ 1200 6│ VCC (Bypass / Bulk Capacitor)
     (IC Ground)     GND   4│ DIP-8 5│ Drv (MOSFET Gate Drive)
                            └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `Adj` | Analog Input | Skip cycle peak current level adjust (Leave floating or tie to GND via resistor) |
| 2 | `FB` | Feedback Input | Feedback signal input (Connected directly to optocoupler collector) |
| 3 | `CS` | Analog Input | Primary current sense input (Connected to source shunt resistor via LEB filter) |
| 4 | `GND` | Power | Primary circuit common ground ($0\text{ V}$) |
| 5 | `Drv` | Output | Totem-pole gate driver output (Drives external high-voltage power MOSFET gate) |
| 6 | `VCC` | Power / Bypass | Internal supply rail (Decouple with $10\ \mu\text{F}$ electrolytic / $100\text{nF}$ ceramic) |
| 7 | `NC` | No Connect | Omitted pin / No internal connection (Ensures creepage distance from HV pin) |
| 8 | `HV` | High Voltage | High-voltage startup pin (Connected directly to rectified $+400\text{V}$ DC bus) |

## Typical Application Circuit: Isolated Off-Line Flyback Converter (No Aux Winding)

```
    Rectified 85V - 265V AC Mains (+400V DC Bulk Bus)
                 │
                 ├───► Primary Transformer Winding ───► Drain of External MOSFET (e.g. 2SK2645 / FQP6N80)
                 │                                        │
                 ├───► [Pin 8: HV]                        │
                 │        NCP1200P44                      │
                 │     [Pin 5: Drv] ───[ 22Ω - 47Ω ]──────┴── Gate of MOSFET
                 │     [Pin 3: CS]  ───────────────────────── Source Sense Resistor (0.5Ω - 1Ω to GND)
                 │     [Pin 6: VCC] ───[ 10µF Capacitor ]───┐
                 │     [Pin 2: FB]  ───[ PC817 Opto Collector ]
                 │     [Pin 4: GND] ────────────────────────┴── Primary GND (Negative DC Bus)
```

## Frequency Versions Guide

| Part Number | Switching Frequency | Typical Application |
|---|---|---|
| **NCP1200P44 / D40** | **$40\text{ kHz}$** | **Lowest EMI, high efficiency in compact adapters** |
| **NCP1200P60 / D60** | **$60\text{ kHz}$** | **Standard general-purpose flyback supplies** |
| **NCP1200P100 / D100**| **$100\text{ kHz}$** | **Ultra-compact miniature transformers** |

## Common mistakes

- **Omitting the VCC bulk capacitor:** While the NCP1200 self-supplies from the HV pin, a low-ESR bulk capacitor ($10\ \mu\text{F} \dots 47\ \mu\text{F}$) on Pin 6 (VCC) is mandatory to store energy and maintain $V_{CC}$ ripple within the $9.8\text{V} \dots 11.4\text{V}$ regulation window.
- **Ignoring thermal dissipation from DSS in high-line continuous operation:** Dynamic Self-Supply drops high voltage ($400\text{V} - 11\text{V}$) across an internal linear current regulator. In high-power designs ($> 15\text{W}$), using an optional small auxiliary diode to back-feed VCC from the transformer eliminates DSS continuous power dissipation.

## Notes

- **Suffix Guide:** `P44` denotes $40\text{kHz}$ in DIP-8 plastic package; `D40` denotes $40\text{kHz}$ in SOIC-8 package.
