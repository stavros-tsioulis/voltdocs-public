## Overview

The **ULN2803A** is an 8-channel high-voltage, high-current NPN Darlington transistor array IC manufactured by Texas Instruments, STMicroelectronics, and Toshiba. Featuring 8 independent open-collector Darlington pairs with common emitters, each channel is capable of sinking up to **500mA continuous collector current** (600mA peak) and sustaining up to **50V** off-state output voltage.

Each input includes an internal **$2.7\text{ k}\Omega$ series base resistor**, allowing direct connection to $5\text{V}$ TTL or CMOS outputs (Arduino, Raspberry Pi, 74HC logic). Integral **suppression (flyback) clamp diodes** are connected to a shared Common (`COM`) pin to safely absorb inductive kickback spikes when driving relays, solenoids, unipolar stepper motors, and DC motor loads.

## Quick reference

| | |
|---|---|
| **Max Output Voltage (`VCE`)** | 50.0 V DC |
| **Max Collector Current (`IC`)** | $500\text{ mA}$ per channel continuous ($600\text{ mA}$ peak) |
| **Input Base Resistor** | $2.7\text{ k}\Omega$ (Direct 5V TTL / CMOS interface) |
| **Independent Channels** | 8 |
| **Flyback Protection Diodes** | Built-in (shared Pin 10 `COM` terminal) |
| **Saturation Voltage (`VCE(sat)`)** | $1.1\text{V}$ typical at $I_C = 200\text{mA}$ |
| **Package** | 18-pin DIP / SOIC-18 |

## Pinout (DIP-18 Package)

```
             ┌───┴───┐
          1B 1│ 1   18│ 1C
          2B 2│       │17 2C
          3B 3│       │16 3C
          4B 4│       │15 4C
          5B 5│ULN2803│14 5C
          6B 6│       │13 6C
          7B 7│       │12 7C
          8B 8│       │11 8C
         GND 9│       │10 COM
             └───────┘
```

| Pin | Name | Description |
|---|---|---|
| 1–8 | `1B`–`8B` | Digital Channel Inputs 1 through 8 (Connect to MCU GPIO) |
| 9 | `GND` | Common Emitter ground connection |
| 10 | `COM` | Common Cathode terminal for flyback suppression diodes (Connect to load $V+$) |
| 11–18 | `8C`–`1C` | Open-Collector Channel Outputs 8 through 1 (Sink current to GND when input HIGH) |

## Internal Channel Schematics

```
  Input 1B..8B ───[2.7kΩ Resistor]───┬───[Base Q1]
                                     │
                                   [Zener]   [Output 1C..8C]
                                     │              │
                                     └───[Base Q2]──┤
                                                    ├───►|─── COM (Pin 10)
                                                    │   Flyback
                                                   GND (Pin 9)
```

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Output Sustaining Voltage | $V_{CE(SUST)}$ | 50 | — | — | V | $I_C = 10\text{mA}$ |
| Continuous Collector Current | $I_C$ | — | — | 500 | mA | Single channel active |
| Input Voltage | $V_{IN}$ | — | 5.0 | 30 | V | Channel active |
| Collector-Emitter Saturation Voltage | $V_{CE(sat)}$ | — | 1.1 | 1.6 | V | $I_C = 350\text{mA}, I_B = 500\mu\text{A}$ |
| Diode Reverse Voltage | $V_R$ | — | — | 50 | V | Clamp diode |
| Diode Forward Current | $I_F$ | — | — | 500 | mA | Clamp diode continuous |

## Typical Applications

### 8-Relay Bank Drive Circuit

```
  +12V Relay Power Rail ───────────────────────────────┬───────────────── [Pin 10: COM]
                                                        │
                                                 (+) [ 12V RELAY COIL ] (-)
                                                        │
  5V MCU Pin ──────────────► [Pin 1: 1B]   [Pin 18: 1C] ┘
                              ULN2803A
                              [Pin 9: GND] ────────────────────────────── GND
```

- When MCU Pin is **HIGH (5V)**: Transistor turns ON, sinking relay current to GND (Relay energizes).
- When MCU Pin is **LOW (0V)**: Transistor turns OFF, internal clamp diode (Pin 10 `COM`) safely discharges inductive coil energy back to +12V.

## Common mistakes

- **Forgetting to connect Pin 10 (`COM`) to the inductive load supply ($V+$):** If `COM` is left unconnected when driving relays, solenoids, or motors, the internal flyback diodes cannot discharge inductive voltage spikes, destroying the Darlington output transistors.
- **Assuming 500mA per channel across ALL 8 channels simultaneously:** Total package power dissipation ($P_D$) is limited to approx $1.5\text{ W}$ for DIP-18. Sinking $500\text{mA}$ per channel across all 8 channels simultaneously ($8 \times 0.5\text{A} \times 1.1\text{V} = 4.4\text{W}$) will overheat and destroy the IC. Parallel channels or reduce duty cycle for high-current loads.
- **Expecting positive voltage output:** Outputs are **open-collector current sinks**, not current sources. Loads must be wired between the supply voltage ($V+$) and the output pins (`1C`–`8C`).

## Notes

- **ULN2803A vs ULN2003A:** ULN2803A contains **8 channels** in an 18-pin DIP package; ULN2003A contains **7 channels** in a 16-pin DIP package.
- **ULN2803A vs ULN2804A:** ULN2803A has $2.7\text{k}\Omega$ resistors for 5V TTL/CMOS; ULN2804A has $10.5\text{k}\Omega$ resistors for 6V–15V CMOS.
