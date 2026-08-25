## Overview

The **LM318** (LM318N / LM318P) is a precision, high-speed single operational amplifier IC developed by Texas Instruments (originally National Semiconductor). Designed for applications requiring high bandwidth, rapid transient response, and fast settling times, it features an internally compensated unity-gain bandwidth of **$15.0\text{ MHz}$** and a guaranteed minimum slew rate of **$50\text{ V/}\mu\text{s}$** ($70\text{ V/}\mu\text{s}$ typical) — more than 100 times faster than the classic LM741 ($0.5\text{ V/}\mu\text{s}$).

In addition to its internal unity-gain compensation, the LM318 provides external compensation pins (Pins 1, 5, and 8) allowing **feed-forward frequency compensation** in inverting configurations. With feed-forward techniques, the usable slew rate increases to over **$150\text{ V/}\mu\text{s}$**, making the LM318 a venerable choice for fast D/A converter output buffers, active video filters, pulse amplifiers, and high-frequency oscillators.

## Quick reference

| | |
|---|---|
| **Amplifier Type** | Single High-Speed Precision Operational Amplifier |
| **Package** | 8-pin PDIP (LM318N) / 8-pin SOIC (LM318D) |
| **Slew Rate** | $50\text{ V/}\mu\text{s}$ min / $70\text{ V/}\mu\text{s}$ typ ($> 150\text{ V/}\mu\text{s}$ with feed-forward) |
| **Unity-Gain Bandwidth** | $15.0\text{ MHz}$ typical |
| **Settling Time (to 0.1%)** | $500\text{ ns}$ typical ($10\text{V}$ step) |
| **Supply Voltage Range** | $\pm 5.0\text{ V}$ to $\pm 20.0\text{ V}$ split (or $+10\text{V}$ to $+40\text{V}$ single) |
| **Input Offset Voltage** | $4.0\text{ mV}$ typical / $10.0\text{ mV}$ maximum |
| **Input Bias Current** | $150\text{ nA}$ typical / $500\text{ nA}$ maximum |
| **Quiescent Current** | $5.0\text{ mA}$ typical / $10.0\text{ mA}$ maximum |

## Pinout (DIP-8 / SOIC-8 Package)

```
             ┌──────────────┐
     COMP1  ─│ 1          8 │─ COMP3
       IN-  ─│ 2    LM    7 │─ V+
       IN+  ─│ 3   318    6 │─ OUT
        V-  ─│ 4          5 │─ COMP2
             └──────────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `COMP1` | Frequency compensation pin 1 / Feed-forward input terminal |
| 2 | `IN-` | Inverting analog input |
| 3 | `IN+` | Non-inverting analog input |
| 4 | `V-` | Negative power supply rail ($-5\text{V}$ to $-20\text{V}$ or GND) |
| 5 | `COMP2` | Frequency compensation pin 2 / Balance / Offset null |
| 6 | `OUT` | Analog operational amplifier output |
| 7 | `V+` | Positive power supply rail ($+5\text{V}$ to $+20\text{V}$) |
| 8 | `COMP3` | Frequency compensation pin 3 / High-frequency loop bypass |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Large-Signal Slew Rate | $SR$ | 50.0 | 70.0 | — | $\text{V/}\mu\text{s}$ | $A_V = 1, V_S = \pm 15\text{V}$ |
| Small-Signal Bandwidth | $GBW$ | — | 15.0 | — | MHz | $V_S = \pm 15\text{V}, T_A = 25^\circ\text{C}$ |
| Input Offset Voltage | $V_{OS}$ | — | 4.0 | 10.0 | mV | $R_S \le 10\text{ k}\Omega$ |
| Input Bias Current | $I_B$ | — | 150 | 500 | nA | $T_A = 25^\circ\text{C}$ |
| Large-Signal Voltage Gain | $A_{VD}$ | 20 | 200 | — | V/mV | $V_O = \pm 10\text{V}, R_L \ge 2\text{ k}\Omega$ |
| Output Voltage Swing | $V_{OM}$ | $\pm 12.0$ | $\pm 13.5$ | — | V | $V_S = \pm 15\text{V}, R_L = 2\text{ k}\Omega$ |
| Power Supply Rejection Ratio | $PSRR$ | 70 | 90 | — | dB | $V_S = \pm 5\text{V} \dots \pm 20\text{V}$ |
| Supply Current | $I_{CC}$ | — | 5.0 | 10.0 | mA | $V_S = \pm 15\text{V}$ |

## Feed-Forward Compensation Circuit ($150\text{ V/}\mu\text{s}$)

In fast inverting amplifier circuits, connecting a small ceramic capacitor ($C_F \approx 10\text{ pF} \dots 50\text{ pF}$) directly between the inverting input (`IN-`) and compensation pin 1 (`COMP1`) bypasses the slower lateral PNP input transistors at high frequencies, accelerating slew rates beyond $150\text{ V/}\mu\text{s}$:

```
                 [ R_F Feedback 10kΩ ]
             ┌─────────────────────────┐
             │                         │
   V_IN ──[ R_IN 1kΩ ]──┬──[Pin 2: IN-] │
                        │   LM318      ├───── V_OUT
          [ C_F 22pF ] ─┴──[Pin 1: COMP1]
```

## Common mistakes

- **Lack of high-frequency power supply bypass capacitors:** Because the LM318 switches $50\text{V}/\mu\text{s}$ internally, un-bypassed supply lines will cause high-frequency oscillations ($10\text{ MHz} \dots 50\text{ MHz}$). Solder $0.1\ \mu\text{F}$ ceramic capacitors directly from Pin 7 (`V+`) and Pin 4 (`V-`) to ground within $5\text{ mm}$ of the package.
- **Excessive parasitic capacitance on summing node (Pin 2):** Long PCB traces to the inverting input add stray capacitance that interacts with large feedback resistors ($R_F > 50\text{ k}\Omega$) to cause peaking and ringing. Keep $R_F \le 10\text{ k}\Omega$ and trace lengths minimal.
- **Exceeding input common-mode range:** The input voltage range on $\pm 15\text{V}$ supplies is $\pm 11.5\text{V}$. Driving inputs beyond this range can cause phase reversal or output saturation latch-up.

## Notes

- **Pin Compatibility:** The pinout is pin-compatible with industry-standard single op-amps (LM741, TL071, NE5534) for basic pins 2, 3, 4, 6, 7. Pins 1, 5, and 8 function as compensation/balance nodes.
