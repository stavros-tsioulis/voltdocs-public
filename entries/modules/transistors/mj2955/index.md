## Overview

The **MJ2955** is a classic -60V, -15A silicon power PNP bipolar junction transistor manufactured by onsemi and STMicroelectronics. Housed in a rugged, hermetic **TO-3 metal can package**, it is renowned across the electronics industry as the definitive PNP complementary counterpart to the legendary **2N3055** NPN transistor.

Capable of dissipating up to **115 Watts** at a case temperature of $25^\circ\text{C}$ ($\theta_{JC} = 1.52^\circ\text{C/W}$), the MJ2955 is engineered for high-power audio amplifiers, dual-polarity linear bench power supplies, motor speed controllers, and heavy-duty DC switching circuits. Together with the 2N3055, it forms the bedrock complementary output pair for high-power Class-AB audio amplifiers delivering 60W to 100W RMS into 4Ω and 8Ω speaker loads.

## Quick reference

| | |
|---|---|
| **Transistor Type** | Silicon Power PNP Bipolar Junction Transistor |
| **Package** | TO-3 (Hermetic Metal Can — Case is connected to COLLECTOR) |
| **Collector-Emitter Voltage ($V_{CEO}$)** | $-60\text{ V}$ max |
| **Collector-Base Voltage ($V_{CBO}$)** | $-100\text{ V}$ max |
| **Emitter-Base Voltage ($V_{EBO}$)** | $-7.0\text{ V}$ max |
| **Continuous Collector Current ($I_C$)** | $-15.0\text{ A}$ continuous |
| **Base Current ($I_B$)** | $-7.0\text{ A}$ max |
| **DC Current Gain ($h_{FE}$)** | 20 to 70 at $I_C = -4.0\text{A}, V_{CE} = -4.0\text{V}$ ($\ge 5$ at $-10\text{A}$) |
| **Collector Saturation ($V_{CE(sat)}$)** | $-1.1\text{ V}$ typ ($-3.0\text{ V}$ max at $I_C = -10\text{A}, I_B = -3.3\text{A}$) |
| **Transition Frequency ($f_T$)** | $2.5\text{ MHz}$ min |
| **Total Power Dissipation ($P_D$)** | $115\text{ W}$ at $T_C = 25^\circ\text{C}$ with heatsink |
| **Complementary NPN Pair** | **2N3055** (60V 15A NPN in TO-3) |

## Terminal identification

Looking at the **bottom pin side** of the TO-3 metal can with pins pointing toward you:

```
               ┌─────────────────┐
               │    ( ( O ) )    │  Mounting Hole 1
               │                 │
               │   (1)     (2)   │
               │    B       E    │
               │                 │
               │    ( ( O ) )    │  Mounting Hole 2
               └─────────────────┘
           Metal Case = ( C ) COLLECTOR
```

| Pin | Terminal | Type | Description |
|---|---|---|---|
| 1 | `BASE` (`B`) | Control Input | Base control terminal (Thinner pin, off-center offset left) |
| 2 | `EMITTER` (`E`) | Power Emitter | Emitter terminal (Thinner pin, off-center offset right) |
| Case | `COLLECTOR` (`C`) | Power Collector | Outer metal case and mounting flanges (Collector terminal) |

> [!WARNING]
> Live Metal Case: The TO-3 outer metal envelope and mounting flanges are internally connected to the **Collector** terminal. When mounting onto an aluminum heatsink or grounded metal enclosure, you **must** use a mica or silicone insulating pad with nylon shoulder washers on the mounting screws to prevent shorting the supply rail to chassis ground.

## Key parameters

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector-Emitter Sustaining Voltage | $V_{CEO(sus)}$ | -60 | — | — | V | $I_C = -200\text{ mA}, I_B = 0$ |
| Collector-Base Breakdown Voltage | $V_{(BR)CBO}$ | -100 | — | — | V | $I_C = -1.0\text{ mA}, I_E = 0$ |
| Emitter-Base Breakdown Voltage | $V_{(BR)EBO}$ | -7.0 | — | — | V | $I_E = -1.0\text{ mA}, I_C = 0$ |
| Collector Cutoff Current | $I_{CEO}$ | — | — | -0.7 | mA | $V_{CE} = -30\text{ V}, I_B = 0$ |
| Collector Cutoff Current | $I_{CEX}$ | — | — | -1.0 | mA | $V_{CE} = -100\text{ V}, V_{BE(off)} = 1.5\text{ V}$ |
| DC Current Gain | $h_{FE}$ | 20 | — | 70 | — | $V_{CE} = -4.0\text{ V}, I_C = -4.0\text{ A}$ |
| DC Current Gain | $h_{FE}$ | 5 | — | — | — | $V_{CE} = -4.0\text{ V}, I_C = -10.0\text{ A}$ |
| Collector-Emitter Saturation Voltage | $V_{CE(sat)}$ | — | -1.1 | -3.0 | V | $I_C = -10.0\text{ A}, I_B = -3.3\text{ A}$ |
| Base-Emitter On Voltage | $V_{BE(on)}$ | — | — | -1.8 | V | $V_{CE} = -4.0\text{ V}, I_C = -4.0\text{ A}$ |
| Current-Gain-Bandwidth Product | $f_T$ | 2.5 | — | — | MHz | $V_{CE} = -10\text{ V}, I_C = -1.0\text{ A}, f = 1.0\text{ MHz}$ |

## Typical circuits

### High-Power Class-AB Audio Amplifier Output Stage

In a complementary symmetry output stage, the MJ2955 conducts during the negative half-cycles of the audio waveform while the 2N3055 handles the positive half-cycles:

```
                            +35V Positive DC Rail
                                     │
                             ( C ) [Case]
                               2N3055 (NPN)
     Positive Drive ────────►( B ) [Pin 1]
                             ( E ) [Pin 2]
                                     │
                                     ├───[ 0.22Ω 5W ]───┐
                                     │                  ├───► Audio Output (Speaker)
                                     ├───[ 0.22Ω 5W ]───┘
                             ( E ) [Pin 2]
     Negative Drive ────────►( B ) [Pin 1]
                               MJ2955 (PNP)
                             ( C ) [Case]
                                     │
                            -35V Negative DC Rail
```

### Linear Dual-Tracking Power Supply (Negative Rail)

In dual linear laboratory power supplies, the MJ2955 acts as the high-current series-pass transistor on the negative regulated rail, driven by an op-amp or pre-driver BJT (such as BD140).

## Common mistakes

- **Mounting without electrical insulation on a common heatsink:** In a push-pull amplifier, the 2N3055 collector connects to the positive rail (+35V) while the MJ2955 collector connects to the negative rail (-35V). Mounting both transistors directly onto the same uninsulated heatsink causes a direct 70V rail-to-rail short circuit, instantly destroying both transistors and the power supply. Always use mica or Kapton insulator washers and thermal grease.
- **Underestimating base drive requirements:** At high collector currents ($I_C > 8\text{ A}$), current gain ($h_{FE}$) falls below 10. To source 10 A of load current, the base must be driven with at least 1 A to 2 A. A small-signal driver cannot supply this; use a medium-power driver such as the **BD140**, **MJE350**, or **TIP32C** in a Darlington or Sziklai (compound pair) topology.
- **Ignoring Safe Operating Area (SOA):** While rated for 60V and 15A, the MJ2955 cannot handle both simultaneously. Secondary breakdown limits allowable collector current at high $V_{CE}$ voltages. Check the datasheet SOA curves when designing linear supplies where high voltage and current coexist during short-circuit conditions.

## Notes

- **MJ2955 vs MJE2955T:** The MJ2955 is the TO-3 metal diamond package rated for 115W and 15A. The MJE2955T is the plastic TO-220AB package rated for 75W and 10A.
- **RoHS compliance:** The "G" suffix (MJ2955G) designates lead-free, RoHS-compliant packaging with identical electrical specifications.
