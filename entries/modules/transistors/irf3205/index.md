## Overview

The **IRF3205** (IRF3205PBF) is an iconic high-current, low on-resistance N-channel power HEXFET MOSFET manufactured by Infineon Technologies (originally International Rectifier). Housed in a through-hole **TO-220AB** package, it is one of the most widely used power MOSFETs in the world for high-power switching applications.

Rated for a drain-to-source voltage of **$55\text{V}$**, a massive continuous drain current up to **$110\text{A}$** (silicon die limit; $75\text{A}$ package lead bond wire limit), and an ultra-low on-resistance of just **$8.0\text{ m}\Omega$ ($0.008\ \Omega$) at $V_{GS} = 10\text{V}$**, the IRF3205 delivers phenomenal thermal efficiency. Operating with a maximum junction temperature of **$175^\circ\text{C}$**, it is the industry standard for **12V-to-220V/110V DC-AC power inverters, high-power H-bridge DC motor speed controllers, electric scooter/e-bike ESCs, solar battery charge controllers, and automotive high-side/low-side switches**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | High-Current N-Channel HEXFET Power MOSFET |
| **Package** | TO-220AB (3-pin through-hole) / D2PAK (SMD) |
| **Drain-Source Voltage ($V_{DSS}$)** | $55\text{ V}$ max |
| **Continuous Drain Current ($I_D$)** | **$110\text{ A}$** ($T_C = 25^\circ\text{C}$, Silicon limit; $75\text{ A}$ Package Lead limit) |
| **Pulsed Drain Current ($I_{DM}$)** | **$390\text{ A}$** |
| **On-Resistance ($R_{DS(on)}$ at 10V)**| **$8.0\text{ m}\Omega$ ($0.008\ \Omega$) max** |
| **Gate Threshold Voltage ($V_{GS(th)}$)**| **$2.0\text{ V}$ to $4.0\text{ V}$** (Requires $10\text{V} \dots 12\text{V}$ gate drive) |
| **Gate-to-Source Voltage ($V_{GS}$)** | $\pm 20\text{ V}$ max |
| **Total Gate Charge ($Q_g$)** | $97\text{ nC}$ typ ($146\text{ nC}$ max) |
| **Total Power Dissipation ($P_D$)** | $200\text{ Watts}$ ($T_C = 25^\circ\text{C}$) |
| **Operating Junction Temp** | $-55^\circ\text{C}$ to $+175^\circ\text{C}$ |

## Pinout (TO-220AB Package)

Looking at the **front labeled face** with leads pointing downward:

```
        ┌──────────────┐
        │  O  [Metal]  │ ── Tab is internally connected to Pin 2 (Drain)
        ├──────────────┤
        │   IRF3205    │
        └─┬────┬────┬──┘
          1    2    3
          G    D    S
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GATE` | Gate Input | Gate control terminal (Drive with $10\text{V} \dots 15\text{V}$ for full $8\text{m}\Omega$ saturation) |
| 2 (Tab) | `DRAIN` | Power Drain | Drain switching terminal (Internally connected to metal mounting tab) |
| 3 | `SOURCE`| Power Source | Source terminal (Connect to ground or negative return path) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Drain-Source Breakdown | $V_{(BR)DSS}$ | 55 | — | — | V | $V_{GS} = 0\text{V}, I_D = 250\ \mu\text{A}$ |
| Static Drain-Source $R_{DS(on)}$ | $R_{DS(on)}$ | — | 6.5 | 8.0 | mΩ | $V_{GS} = 10\text{V}, I_D = 62\text{A}$ |
| Gate Threshold Voltage | $V_{GS(th)}$ | 2.0 | — | 4.0 | V | $V_{DS} = V_{GS}, I_D = 250\ \mu\text{A}$ |
| Drain-Source Leakage | $I_{DSS}$ | — | — | 25 | µA | $V_{DS} = 55\text{V}, V_{GS} = 0\text{V}$ |
| Gate-Body Leakage Current | $I_{GSS}$ | — | — | $\pm 100$ | nA | $V_{GS} = \pm 20\text{V}$ |
| Diode Forward Voltage | $V_{SD}$ | — | — | 1.3 | V | $I_S = 62\text{A}, V_{GS} = 0\text{V}$ |
| Thermal Resistance | $R_{\theta JC}$ | — | — | 0.75 | °C/W | Junction-to-Case |

## Typical Push-Pull Power Inverter / Motor Driver Stage

```
                      +12V to +24V High-Current Battery Rail
                                   │
                               [ + Load / Motor - ]
                                   │
                                   ├───[ Flyback Catch Diode (e.g. MBR20100) ]──┐
                                   │   (Anode to Drain, Cathode to Supply)     │
                             [Pin 2: DRAIN]                                    │
                                IRF3205                                        │
  Gate Driver (10V - 12V)    [Pin 1: GATE]                                     │
  (e.g. TC4420 / IR2104)           │                                           │
          │                        ├───[ 10kΩ Gate Pull-Down Resistor ]────────┤
          ├───[ 10Ω Gate Resistor ]┤                                           │
         GND                       │                                           │
                             [Pin 3: SOURCE]                                   │
                                   │                                           │
                                  GND ─────────────────────────────────────────┴─── Heavy System GND
```

## Comparison: IRF3205 vs IRFZ44N vs IRLB8721

| Parameter | IRF3205 | IRFZ44N | IRLB8721 |
|---|---|---|---|
| **$V_{DSS}$ Rating** | **$55\text{ V}$** | $55\text{ V}$ | $30\text{ V}$ |
| **Max Current ($I_D$)** | **$110\text{ A}$** | $49\text{ A}$ | $62\text{ A}$ |
| **$R_{DS(on)}$ at 10V** | **$8.0\text{ m}\Omega$** | $17.5\text{ m}\Omega$ | $8.7\text{ m}\Omega$ |
| **Logic-Level 5V Drive**| **No ($10\text{V}$ Required)** | No ($10\text{V}$ Required) | **Yes ($4.5\text{V}$ Logic Level)** |

## Common mistakes

- **Attempting to drive directly from a 3.3V or 5V microcontroller pin:** The IRF3205 is a **standard-gate MOSFET**, NOT a logic-level device. Driving its gate with $3.3\text{V}$ or $5\text{V}$ will leave the transistor operating in the linear resistive region, causing severe overheating and destructive thermal runaway under load. Use a dedicated gate driver IC (such as **TC4420, IR2104, or a discrete BJT totem-pole driver**) with a $10\text{V} \dots 12\text{V}$ supply. (For direct 5V logic drive, use the **IRLZ44N** or **IRLB8721** instead).
- **Forgetting that the metal tab is live Drain:** In TO-220 packages, the metal mounting tab is internally bonded to Pin 2 (Drain). When mounting multiple IRF3205s to a shared aluminum heatsink, isolate each tab using **silicone thermal pads and plastic insulating bushings**.

## Notes

- **Package Rating:** The silicon die handles 110A; standard TO-220 copper lead wires are rated for continuous currents up to 75A.
