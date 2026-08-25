## Overview

The **VIPer22A** (VIPer22A-E / VIPer22ADIP-E) is an off-line monolithic switch-mode power supply (SMPS) primary switcher IC manufactured by STMicroelectronics. Available in an 8-pin through-hole **DIP-8** and surface-mount **SO-8** package, it monolithically integrates a state-of-the-art current-mode PWM controller with a rugged **$730\text{V}$ breakdown avalanche-rugged power MOSFET** on a single silicon die.

Delivering up to **$12\text{ Watts}$** of isolated output power across universal mains ($85\text{V} \dots 265\text{V}$ AC) or up to **$20\text{ Watts}$** at European line voltage ($230\text{V}$ AC) at a fixed switching frequency of **$60\text{ kHz}$**, the VIPer22A dramatically reduces component count in offline power systems. It supports both **isolated flyback converters** (with optocoupler feedback) and **non-isolated offline buck converters** (with direct resistor divider feedback), making it the premier choice for **smart appliances (washing machines, microwaves, air conditioners), IoT gateways, LED drivers, and compact auxiliary power modules**.

## Quick reference

| | |
|---|---|
| **Device Type** | Monolithic Off-Line SMPS Primary Switcher IC |
| **Package** | 8-pin DIP (DIP-8 / SDIP-8) / SO-8 |
| **Integrated MOSFET Rating ($V_{DSS}$)**| **$730\text{ V}$ min** (Avalanche rugged) |
| **Fixed Switching Frequency** | **$60\text{ kHz}$** |
| **Output Power Capability** | **$12\text{ Watts}$** (Wide mains 85–265V AC) / **$20\text{ Watts}$** (230V AC) |
| **Operating Supply Range ($V_{DD}$)**| **$8.0\text{ V}$ to $50.0\text{ V}$** (Wide operating window) |
| **Startup High-Voltage Current Source**| Integrated on Drain pins (Charges $V_{DD}$ at startup) |
| **Protection Features** | Hysteretic Thermal Shutdown ($170^\circ\text{C}$), Undervoltage Lockout (UVLO), Overvoltage Protection |

## Pinout (DIP-8 Package)

```
                            ┌───┴───┐
       (Source / GND) SOURCE 1│ 1   8│ DRAIN (Integrated 730V MOSFET)
       (Source / GND) SOURCE 2│ VIPer 7│ DRAIN (Integrated 730V MOSFET)
       (Opto Feedback)    FB 3│  22A  6│ DRAIN (Integrated 730V MOSFET)
       (Supply Voltage)  VDD 4│ DIP-8 5│ DRAIN (Integrated 730V MOSFET)
                            └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1, 2 | `SOURCE` | Power / Ground | Primary Source connection (Connects to primary circuit Ground; internal sense FET return) |
| 3 | `FB` | Feedback Input | Feedback control pin (Connected to optocoupler collector for PWM regulation) |
| 4 | `VDD` | Power Input | Controller supply voltage pin (Connected to auxiliary winding diode and $10\ \mu\text{F}$ capacitor) |
| 5, 6, 7, 8 | `DRAIN` | Power / High-Voltage | Integrated 730V MOSFET Drain (Connected to primary flyback transformer winding and startup bus) |

## Typical Application Circuit: Isolated 12V 1A Offline Flyback Converter

```
  Rectified 85V - 265V AC (+400V DC Bus)
                 │
                 ├───► [ Transformer Primary ] ───► [Pins 5-8: DRAIN]
                 │                                      VIPer22A
                 │                                  [Pins 1-2: SOURCE] ──► Primary GND
                 │
  Auxiliary Winding ──► [ 1N4148 Diode ] ──┬──────► [Pin 4: VDD]
                                           │            │
                                     [ 10µF Cap ]       └──► [Pin 3: FB] ──► [ PC817 Opto Collector ]
                                           │
                                      Primary GND
```

## Non-Isolated Offline Buck Topology

In cost-sensitive smart home appliances, the VIPer22A can be configured as a non-isolated offline **buck converter** stepping $+325\text{V}$ rectified DC directly down to $+5\text{V}$ or $+12\text{V}$ without any custom transformer:

```
  +325V DC In ───► [Pins 5-8: DRAIN]
                      VIPer22A
                   [Pins 1-2: SOURCE] ───► [ 1mH Power Inductor ] ───► +12V DC Out (Non-Isolated)
                                                 │
                                      [ Ultrafast Catch Diode ]
                                                 │
                                            Primary GND
```

## Common mistakes

- **Leaving Pins 5, 6, 7, 8 unconnected from each other:** Pins 5, 6, 7, and 8 are all internally connected to the internal power MOSFET's drain and act as the device's primary heatsink. On the PCB, connect all four pins to a **broad copper pour** for optimal thermal dissipation.
- **Exceeding 50V on VDD pin:** The $V_{DD}$ pin has an absolute maximum rating of $50\text{V}$. Ensure the auxiliary transformer winding turns ratio does not generate excessive voltage during light-load conditions.

## Notes

- **Suffix Guide:** `VIPer22ADIP-E` is standard through-hole DIP-8; `VIPer22AS-E` is SO-8 surface-mount.
