## Overview

The **LM311** is an industry-standard high-speed monolithic voltage comparator designed for operation over a wide range of supply voltages, from a standard $+5\text{ V}$ single logic rail up to $\pm 15\text{ V}$ dual split supplies. Designed by analog pioneer Robert Widlar, the LM311 is considerably faster than general-purpose comparators like the LM393 ($200\text{ ns}$ response time versus $1.3\,\mu\text{s}$) while retaining low input current requirements ($100\text{ nA}$ typical input bias current).

A defining characteristic of the LM311 is its uncommitted, floating output NPN transistor stage: both the **Collector** (pin 7) and **Emitter** (pin 1) are brought out to package terminals. This allows the output to drive loads referenced to ground, the positive supply, or the negative rail, sinking up to $50\text{ mA}$ at voltages up to $40\text{ V}$. Additionally, the IC includes **Balance** and **Strobe** terminals (pins 5 and 6) that allow input offset nulling and output gating by digital logic.

## Quick reference

| | |
|---|---|
| **Comparator Channels** | 1 (Single High-Speed Comparator) |
| **Response Time ($t_{res}$)** | $200\text{ ns}$ typical ($100\text{ mV}$ step with $5\text{ mV}$ overdrive) |
| **Single Supply Voltage Range** | $5.0\text{ V}$ to $36.0\text{ V}$ DC |
| **Dual Split Supply Voltage Range** | $\pm 2.5\text{ V}$ to $\pm 18.0\text{ V}$ DC |
| **Output Sink Current ($I_{SINK}$)** | Up to $50\text{ mA}$ continuous |
| **Maximum Output Voltage** | Up to $40.0\text{ V}$ (collector-to-emitter rating) |
| **Input Offset Voltage ($V_{IO}$)** | $3.0\text{ mV}$ typical ($7.5\text{ mV}$ max at $25^\circ\text{C}$) |
| **Input Bias Current ($I_{IB}$)** | $100\text{ nA}$ typical ($250\text{ nA}$ max) |
| **Strobe / Gating Function** | Yes (via Pin 6 `STROBE`) |
| **Quiescent Supply Current** | $5.1\text{ mA}$ typical ($7.5\text{ mA}$ max) |
| **Package Options** | 8-pin DIP (P), SOIC-8 (D), TSSOP-8 (PW) |

## Pin configuration

### 8-Pin DIP / SOIC Package

```
             ┌───┴───┐
     EMITTER 1│ 1   8 │ V+ (Positive Supply)
         +IN 2│       │ 7 COLLECTOR (Open Output)
         -IN 3│ LM311 │ 6 BALANCE / STROBE
          V- 4│       │ 5 BALANCE (Offset Null)
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `EMITTER` | Output Terminal | Output transistor emitter; connect to `GND` for standard open-collector operation |
| 2 | `+IN` | Analog Input | Non-inverting comparator input |
| 3 | `-IN` | Analog Input | Inverting comparator input |
| 4 | `V-` | Power Supply | Negative supply rail ($-2.5\text{ V} \dots -18.0\text{ V}$ in dual-supply, or `GND` in single-supply) |
| 5 | `BALANCE` | Analog Input | Input offset balance trim terminal |
| 6 | `STROBE` | Digital/Analog Input | Strobe control and offset balance terminal (pull LOW to disable output) |
| 7 | `COLLECTOR` | Output Terminal | Output transistor open-collector; requires pull-up resistor or direct load |
| 8 | `V+` | Power Supply | Positive supply rail ($+5.0\text{ V} \dots +36.0\text{ V}$) |

## Functional description

### Output Stage Flexibility

Because both the collector (pin 7) and emitter (pin 1) of the internal output NPN transistor are isolated from internal power rails, the LM311 provides exceptional interface versatility:
1. **Standard Ground-Referenced Digital Logic:** Emitter (pin 1) is grounded, and Collector (pin 7) is pulled up via a resistor to $+5\text{ V}$ (TTL/CMOS) or $+3.3\text{ V}$ (low-voltage MCU), regardless of whether the LM311 is powered from $\pm 15\text{ V}$.
2. **Direct Relays and Solenoids:** Pin 1 is tied to ground; a relay coil (up to $50\text{ mA}, 40\text{ V}$) is connected directly between $+24\text{ V}$ and pin 7 with a flyback diode.
3. **Emitter-Follower Output:** Pin 7 is tied to $V+$, and pin 1 drives a load resistor to ground, producing an active-high output voltage that tracks non-inverting input states.

### Strobe Operation

Pin 6 functions as a logic strobe. When pin 6 is left open, the comparator operates normally. When pin 6 is clamped LOW (drawn down within $0.5\text{ V}$ of ground or $V-$ with an external switch or open-collector logic gate), the internal output stage is forced completely OFF (pin 7 remains High-Z), independent of differential input voltage.

## Absolute maximum ratings

> [!WARNING]
> Stresses beyond these ratings cause permanent damage. Differential input voltage must not exceed $\pm 30\text{ V}$.

| Parameter | Symbol | Min | Max | Unit |
|---|---|---|---|---|
| Total Supply Voltage ($V+ - V-$) | $V_S$ | — | $36.0$ | V |
| Output to Negative Supply Voltage ($V_{OUT} - V-$) | $V_{O(V-)}$ | — | $40.0$ | V |
| Emitter to Negative Supply Voltage ($V_{EMIT} - V-$) | $V_{E(V-)}$ | — | $30.0$ | V |
| Differential Input Voltage | $V_{ID}$ | — | $\pm 30.0$ | V |
| Input Voltage (either input) | $V_I$ | $(V-) - 0.3$ | $(V+) + 0.3$ | V |
| Output Short-Circuit Duration | $t_{sc}$ | — | $10$ | s |
| Operating Free-Air Temperature | $T_A$ | $0$ | $+70$ | °C |
| Storage Temperature Range | $T_{stg}$ | $-65$ | $+150$ | °C |

## Electrical characteristics

($V+ = 15\text{ V}, V- = -15\text{ V}, T_A = 25^\circ\text{C}$ unless otherwise specified)

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Offset Voltage | $V_{IO}$ | — | $0.7$ | $3.0$ | mV | $R_S \le 50\text{ k}\Omega$ |
| Input Offset Current | $I_{IO}$ | — | $4.0$ | $25$ | nA | — |
| Input Bias Current | $I_{IB}$ | — | $65$ | $100$ | nA | — |
| Voltage Gain | $A_V$ | $40$ | $200$ | — | V/mV | Large signal |
| Response Time | $t_{res}$ | — | $200$ | — | ns | $100\text{ mV}$ step with $5\text{ mV}$ overdrive |
| Common-Mode Input Range | $V_{ICR}$ | $-14.5$ | — | $+13.8$ | V | — |
| Output Saturation Voltage | $V_{SAT}$ | — | $0.23$ | $0.4$ | V | $V_{IN} \le -10\text{ mV}, I_{SINK} = 8\text{ mA}$ |
| | | — | $0.75$ | $1.5$ | V | $V_{IN} \le -10\text{ mV}, I_{SINK} = 50\text{ mA}$ |
| Output Leakage Current | $I_{LKG}$ | — | $0.2$ | $50$ | nA | $V_{IN} \ge 10\text{ mV}, V_{OUT} = 35\text{ V}$ |
| Positive Supply Current | $I_{CC+}$ | — | $5.1$ | $7.5$ | mA | $V_{OUT}$ High |
| Negative Supply Current | $I_{CC-}$ | — | $4.1$ | $6.0$ | mA | $V_{OUT}$ High |

## Typical application circuit: Zero-Crossing Detector with Hysteresis

The circuit below converts an AC sine wave into a clean, rapid square wave synchronized to the zero voltage crossings, with built-in positive feedback hysteresis to eliminate multi-triggering noise.

```
       AC Input
       (Sine Wave)
       ──[10k]───┬──────────────┤ 3 (-IN)
                 │              │
                ┌┴┐ 1N4148      │
                ▲ │ Clamp       │
                └┬┘             │
                 ├──────────────┤              LM311
                ┌┴┐ 1N4148      │            Comparator
                ▲ │ Clamp       │
                └┬┘             │             ┌───────┐
                 │              │             │ 8 (V+)├─── +5V (VCC)
                GND             │             │       │
                                │ 2 (+IN)     │ 7(COL)├───┬────────────── Digital Square Output (0V/5V)
       GND ─────────────────────┴──────┬──────┤       │   │
                                       │      │ 1(EMIT)├──┴──[1k]─── +5V (Pull-up)
                                       │      └───┬───┘
                                      ┌┴┐         │
                                      │ │ Rh      GND
                                      │ │ 1M
                                      └┬┘
                                       │
                                       └──────────┘ (Hysteresis Feedback Loop)
```

### Operation
- **Input Clamping:** The anti-parallel diodes (1N4148) clamp the input voltage between $-0.7\text{ V}$ and $+0.7\text{ V}$, protecting the sensitive comparator differential input from destructive high-amplitude input surges.
- **Hysteresis Feedback ($R_h$):** Resistor $R_h$ ($1\text{ M}\Omega$) provides a tiny positive feedback voltage ($\approx 5\text{ mV}$) back to pin 2. When the output switches, the input threshold shifts slightly, guaranteeing crisp transitions with zero chatter even for slowly varying or noisy input signals.

## Design considerations & common mistakes

- **Hysteresis is Mandatory for Clean Switching:** Because the LM311 has a high gain-bandwidth and fast $200\text{ ns}$ transition capability, any stray capacitance between the output (pin 7) and inputs (pins 2 and 3) will induce burst oscillations ($10\text{ MHz} \dots 50\text{ MHz}$) when an input signal crosses the threshold slowly. Always provide a small amount of positive feedback hysteresis ($5\text{ mV} \dots 20\text{ mV}$).
- **Pin 1 Must Be Grounded in Single-Supply Systems:** In standard single-supply applications ($+5\text{ V}$ and $\text{GND}$), pin 1 (`EMITTER`) must be tied directly to ground. Leaving pin 1 unconnected is a common error that leaves the output stage without a return path, causing pin 7 to remain permanently pulled up.
- **Floating Strobe / Balance Terminals:** If input offset adjustment and strobe gating are not needed, leave pins 5 and 6 **unconnected**. Never tie pin 6 to ground unless you intentionally want to mute or disable the output.
- **Pull-Up Resistor is Required:** The output on pin 7 is strictly an uncommitted open collector. Unlike op-amps, it cannot source current on its own. An external pull-up resistor or load connected to a positive supply is required.
