## Overview

The **NCP81074** (available in **NCP81074A** split-output and **NCP81074B** single-output configurations) is a single-channel, ultra-high-speed low-side MOSFET and GaN gate driver manufactured by ON Semiconductor (onsemi). Engineered to source and sink up to **$\pm 10\text{ A}$ peak current**, it drives large capacitive gate loads with industry-leading rise and fall times of just **$4\text{ ns}$** into a $1.8\text{ nF}$ load.

Operating from a wide supply range of **$4.5\text{ V}$ to $20.0\text{ V}$**, the NCP81074 drastically minimizes switching transition losses ($E_{on}$ and $E_{off}$) in high-frequency power electronics applications, including synchronous buck converters, secondary synchronous rectifiers, active clamp flybacks, high-speed laser diode drivers, and class-D amplifiers.

## Quick reference

| | |
|---|---|
| **Driver Type** | Single-Channel High-Speed Low-Side MOSFET Gate Driver |
| **Package** | SOIC-8 / WDFN8 (2mm × 2mm) |
| **Supply Voltage Range ($V_{DD}$)** | $4.5\text{ V}$ to $20.0\text{ V}$ DC |
| **Peak Output Current** | $\pm 10.0\text{ A}$ Peak (10A Source / 10A Sink) |
| **Rise / Fall Time** | $4\text{ ns}$ typical ($C_{LOAD} = 1.8\text{ nF}$) |
| **Propagation Delay** | $15\text{ ns}$ typical (matched rise/fall delays) |
| **Output Architecture** | Split output (`OUTH` / `OUTL` on A-version) or combined (`OUT` on B-version) |
| **Input Options** | Dual inputs (`IN+` non-inverting & `IN-` inverting) or Enable + Input |
| **Operating Junction Temp** | $-40^\circ\text{C}$ to $+140^\circ\text{C}$ |

## Pin Configuration (SOIC-8 Package)

### NCP81074A (Split Output with Enable)

```
        ┌──────────────┐
     EN ─│ 1          8 │─ OUTH (Source)
    IN+ ─│ 2          7 │─ OUTL (Sink)
    GND ─│ 3          6 │─ VDD
     NC ─│ 4          5 │─ NC
        └──────────────┘
```

### NCP81074B (Dual Input Differential with Single Output)

```
        ┌──────────────┐
    IN+ ─│ 1          8 │─ OUT
    IN- ─│ 2          7 │─ OUT
    GND ─│ 3          6 │─ VDD
     NC ─│ 4          5 │─ NC
        └──────────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `EN` / `IN+` | Input | Enable pin (active-HIGH, NCP81074A) or Non-Inverting Logic Input (NCP81074B) |
| 2 | `IN+` / `IN-` | Input | Non-inverting input (NCP81074A) or Inverting Logic Input (NCP81074B) |
| 3 | `GND` | Power | Low-noise ground reference |
| 4 | `NC` | — | No connection |
| 5 | `NC` | — | No connection |
| 6 | `VDD` | Power | Supply voltage input (+4.5V to +20.0V DC) |
| 7 | `OUTL` / `OUT` | Output | Low-side pull-down sink output (NCP81074A) or Gate Output (NCP81074B) |
| 8 | `OUTH` / `OUT` | Output | High-side pull-up source output (NCP81074A) or Gate Output (NCP81074B) |

## Control Logic Truth Tables

### NCP81074A (Split Output with Enable)

| `EN` | `IN+` | `OUTH` (Turn-ON) | `OUTL` (Turn-OFF) | Gate State |
|---|---|---|---|---|
| Low (`0`) | X | High-Z | High-Z | **Disabled (High-Z)** |
| High (`1`) | Low (`0`) | High-Z | Low (Sinking) | **MOSFET OFF (Grounded)** |
| High (`1`) | High (`1`) | High (Sourcing) | High-Z | **MOSFET ON (Pulled to VDD)** |

### NCP81074B (Dual Inverting/Non-Inverting Inputs)

| `IN+` (Non-inverting) | `IN-` (Inverting) | `OUT` Output | MOSFET State |
|---|---|---|---|
| Low (`0`) | Low (`0`) | Low (`0`) | **OFF** |
| Low (`0`) | High (`1`) | Low (`0`) | **OFF** |
| High (`1`) | Low (`0`) | High (`1`) | **ON** |
| High (`1`) | High (`1`) | Low (`0`) | **OFF** |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 4.5 | 12.0 | 20.0 | V | Operating range |
| Peak Sourcing Current | $I_{SRC(PK)}$ | — | 10.0 | — | A | $V_{DD} = 12\text{V}, C_L = 10\ \mu\text{F}$ |
| Peak Sinking Current | $I_{SNK(PK)}$ | — | 10.0 | — | A | $V_{DD} = 12\text{V}, C_L = 10\ \mu\text{F}$ |
| Rise Time | $t_r$ | — | 4.0 | 7.0 | ns | $C_{LOAD} = 1.8\text{ nF}, V_{DD} = 12\text{V}$ |
| Fall Time | $t_f$ | — | 4.0 | 7.0 | ns | $C_{LOAD} = 1.8\text{ nF}, V_{DD} = 12\text{V}$ |
| Turn-On Delay | $t_{D(ON)}$ | — | 15.0 | 25.0 | ns | $C_{LOAD} = 1.8\text{ nF}, V_{DD} = 12\text{V}$ |
| Turn-Off Delay | $t_{D(OFF)}$ | — | 15.0 | 25.0 | ns | $C_{LOAD} = 1.8\text{ nF}, V_{DD} = 12\text{V}$ |
| Input High Voltage | $V_{IH}$ | 2.0 | — | — | V | TTL/CMOS compatible |
| Input Low Voltage | $V_{IL}$ | — | — | 0.8 | V | TTL/CMOS compatible |
| Undervoltage Lockout | $V_{UVLO}$ | 3.8 | 4.1 | 4.4 | V | $V_{DD}$ rising threshold |

## Split Output Drive Topology (NCP81074A)

The split output (`OUTH` and `OUTL`) allows independent tuning of the MOSFET's turn-on and turn-off speeds without adding a parallel reverse diode across a single gate resistor:

```
        NCP81074A
     ┌──────────────┐
     │         OUTH ├───[ R_G(ON) 10Ω ]───┐
     │              │                     ├───── Gate of Power MOSFET
     │         OUTL ├───[ R_G(OFF) 2.2Ω ]─┘
     └──────────────┘
```

- **$R_{G(ON)}$ (e.g. $10\ \Omega$):** Sets a controlled turn-on $dV/dt$ to minimize EMI and switch-node ringing.
- **$R_{G(OFF)}$ (e.g. $2.2\ \Omega$):** Provides an aggressive, ultra-low impedance discharge path to eliminate parasitic Miller-effect induced shoot-through.

## Common mistakes

- **Inadequate high-frequency decoupling on VDD:** A 10A current spike drawn in $4\text{ ns}$ will cause huge voltage droop on $V_{DD}$ without localized decoupling. Place at least one $1.0\ \mu\text{F} \dots 4.7\ \mu\text{F}$ low-ESR ceramic capacitor (X7R) directly between Pin 6 (`VDD`) and Pin 3 (`GND`) within $2\text{ mm}$ of the IC package.
- **Excessive gate trace inductance:** Long PCB traces between the driver and the MOSFET gate introduce parasitic inductance that rings severely with the MOSFET input capacitance ($C_{iss}$). Keep gate traces under $10\text{ mm}$ in length and route over an unbroken ground reference plane.

## Notes

- **Version Differences:** Choose **NCP81074A** if independent turn-on/turn-off resistor control is desired; choose **NCP81074B** if inverting input control or dual complementary PWM signals are required.
