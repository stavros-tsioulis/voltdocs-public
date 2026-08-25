## Overview

The **IRFB4110** (IRFB4110PBF) is an ultra-high-current, benchmark low on-resistance N-channel power HEXFET MOSFET manufactured by Infineon Technologies (originally International Rectifier). Housed in a through-hole **TO-220AB** package, it has achieved legendary status across the DIY engineering community as the ultimate power MOSFET for high-voltage, high-current switching.

Rated for a drain-to-source breakdown voltage of **$100\text{V}$**, a massive continuous drain current of **$180\text{A}$** (silicon die limit; $75\text{A}$ lead limit), and an astonishingly low typical on-resistance of just **$3.7\text{ m}\Omega$ ($0.0037\ \Omega$) at $V_{GS} = 10\text{V}$**, the IRFB4110 dissipates up to **$370\text{ Watts}$** with a maximum junction temperature of **$175^\circ\text{C}$**. Because it combines a high $100\text{V}$ voltage rating with sub-$4\text{m}\Omega$ conduction losses, it is the premier component of choice for **DIY lithium battery spot welders (e.g. kWeld), 48V–72V e-bike and electric motorcycle BLDC speed controllers (ESCs), high-power ZVS induction heaters, and heavy-duty 24V/48V solar inverters**.

## Quick reference

| | |
|---|---|
| **Transistor Type** | Ultra-High-Power N-Channel HEXFET Power MOSFET |
| **Package** | TO-220AB (3-pin through-hole) / D2PAK |
| **Drain-Source Voltage ($V_{DSS}$)** | **$100\text{ V}$ max** |
| **Continuous Drain Current ($I_D$)** | **$180\text{ A}$** ($T_C = 25^\circ\text{C}$, Silicon limit; $75\text{ A}$ Package Lead limit) |
| **Pulsed Drain Current ($I_{DM}$)** | **$670\text{ A}$** |
| **On-Resistance ($R_{DS(on)}$ at 10V)**| **$3.7\text{ m}\Omega$ typ / $4.5\text{ m}\Omega$ ($0.0045\ \Omega$) max** |
| **Gate Threshold Voltage ($V_{GS(th)}$)**| **$2.0\text{ V}$ to $4.0\text{ V}$** (Requires $10\text{V} \dots 15\text{V}$ gate drive) |
| **Gate-to-Source Voltage ($V_{GS}$)** | $\pm 20\text{ V}$ max |
| **Total Gate Charge ($Q_g$)** | $150\text{ nC}$ typ ($230\text{ nC}$ max) |
| **Total Power Dissipation ($P_D$)** | **$370\text{ Watts}$** ($T_C = 25^\circ\text{C}$) |
| **Operating Junction Temp** | $-55^\circ\text{C}$ to $+175^\circ\text{C}$ |

## Pinout (TO-220AB Package)

Looking at the **front labeled face** with leads pointing downward:

```
        ┌──────────────┐
        │  O  [Metal]  │ ── Tab is internally connected to Pin 2 (Drain)
        ├──────────────┤
        │   IRFB4110   │
        └─┬────┬────┬──┘
          1    2    3
          G    D    S
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GATE` | Gate Input | Gate control terminal (Drive with $10\text{V} \dots 15\text{V}$ with fast peak current capability) |
| 2 (Tab) | `DRAIN` | Power Drain | Drain switching terminal (Internally connected to metal mounting tab) |
| 3 | `SOURCE`| Power Source | Source terminal (Connect to ground or negative return busbar) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Drain-Source Breakdown | $V_{(BR)DSS}$ | 100 | — | — | V | $V_{GS} = 0\text{V}, I_D = 250\ \mu\text{A}$ |
| Static Drain-Source $R_{DS(on)}$ | $R_{DS(on)}$ | — | 3.7 | 4.5 | mΩ | $V_{GS} = 10\text{V}, I_D = 75\text{A}$ |
| Gate Threshold Voltage | $V_{GS(th)}$ | 2.0 | — | 4.0 | V | $V_{DS} = V_{GS}, I_D = 250\ \mu\text{A}$ |
| Drain-Source Leakage | $I_{DSS}$ | — | — | 20 | µA | $V_{DS} = 100\text{V}, V_{GS} = 0\text{V}$ |
| Gate-Body Leakage Current | $I_{GSS}$ | — | — | $\pm 100$ | nA | $V_{GS} = \pm 20\text{V}$ |
| Diode Forward Voltage | $V_{SD}$ | — | — | 1.3 | V | $I_S = 75\text{A}, V_{GS} = 0\text{V}$ |
| Thermal Resistance | $R_{\theta JC}$ | — | — | 0.40 | °C/W | Junction-to-Case |

## Typical High-Power Battery Spot Welder Stage (Paralleled Array)

In DIY battery spot welders switching $800\text{A} \dots 1500\text{A}$ pulses for $5\text{ ms} \dots 20\text{ ms}$, multiple IRFB4110 MOSFETs are wired in parallel across heavy copper busbars:

```
                      +12V Car Battery / Ultra-Capacitor Bank
                                         │
                                [ Welding Probes & Nickel Strip ]
                                         │
                                         ├───► [Pin 2: DRAIN (Heavy Copper Busbar)]
                                         │
       Gate Driver (12V, 6A Peak)        │
       (e.g. MIC4452 / TC4422)           │
               │                         │
               ├──[ 4.7Ω Gate Resistor ]─┼───► [Pin 1: GATE of MOSFET 1 (IRFB4110)]
               ├──[ 4.7Ω Gate Resistor ]─┼───► [Pin 1: GATE of MOSFET 2 (IRFB4110)]
               ├──[ 4.7Ω Gate Resistor ]─┼───► [Pin 1: GATE of MOSFET 3 (IRFB4110)]
               └──[ 4.7Ω Gate Resistor ]─┼───► [Pin 1: GATE of MOSFET 4 (IRFB4110)]
                                         │
                                         └───► [Pin 3: SOURCE (Heavy Ground Busbar)] ── Common GND
```

## Comparison: IRFB4110 vs IRF3205 vs IRFZ44N

| Parameter | IRFB4110 | IRF3205 | IRFZ44N |
|---|---|---|---|
| **$V_{DSS}$ Voltage** | **$100\text{ V}$** | $55\text{ V}$ | $55\text{ V}$ |
| **Max Current ($I_D$)** | **$180\text{ A}$** | $110\text{ A}$ | $49\text{ A}$ |
| **$R_{DS(on)}$ at 10V** | **$3.7\text{ m}\Omega$** | $8.0\text{ m}\Omega$ | $17.5\text{ m}\Omega$ |
| **Power Dissipation ($P_D$)**| **$370\text{ W}$** | $200\text{ W}$ | $94\text{ W}$ |
| **Thermal Res. ($\theta_{JC}$)**| **$0.40^\circ\text{C/W}$** | $0.75^\circ\text{C/W}$ | $1.5^\circ\text{C/W}$ |

## Common mistakes

- **Driving large gate capacitance with high source impedance:** With a total gate charge of $Q_g \approx 150\text{ nC}$ ($C_{iss} \approx 9600\text{ pF}$), driving IRFB4110s at high PWM frequencies requires high-current gate driver ICs (capable of $2\text{A} \dots 6\text{A}$ peak current). Driving directly from high-impedance logic outputs will result in slow rise times and extreme switching losses.
- **Paralleling gates directly without individual series resistors:** When paralleling multiple IRFB4110s, always give each individual gate its own dedicated **$2.2\ \Omega \dots 10\ \Omega$ series resistor** directly at the pin to prevent high-frequency gate oscillations (ringing) caused by PCB parasitic inductances.

## Notes

- **Suffix Guide:** `IRFB4110PBF` denotes lead-free through-hole TO-220AB; `IRFS4110PBF` denotes surface-mount D2PAK.
