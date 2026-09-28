## Overview

The **OP07** is an industry-standard ultra-low offset voltage bipolar operational amplifier manufactured by Texas Instruments and Analog Devices (originally introduced by Precision Monolithics Inc. / PMI). It was specifically designed to eliminate the need for external calibration potentiometers in high-accuracy DC instrumentation, thermocouple signal conditioning, strain-gauge load cell bridges, and low-frequency analog computing circuits.

Featuring an ultra-low input offset voltage down to **$75\text{ }\mu\text{V}$** (with premium grades achieving $10\text{ }\mu\text{V}$ to $25\text{ }\mu\text{V}$), very low temperature drift ($1.3\text{ }\mu\text{V/}^\circ\text{C}$ max), low input bias current ($\pm 4\text{ nA}$ max), and an extremely high open-loop voltage gain of **$400\text{ V/mV}$** ($112\text{ dB}$ min), the OP07 remains the gold standard low-cost precision DC amplifier. It shares the classic 741 8-pin DIP pinout with dedicated offset nulling pins on pins 1 and 8.

## Quick reference

| | |
|---|---|
| **Function** | Ultra-Low Offset Voltage Precision Operational Amplifier |
| **Supply Voltage Range (Single Supply)** | $6.0\text{ V}$ to $36.0\text{ V}$ DC |
| **Supply Voltage Range (Split Supply)** | $\pm 3.0\text{ V}$ to $\pm 18.0\text{ V}$ DC |
| **Input Offset Voltage ($V_{OS}$)** | $75\text{ }\mu\text{V}$ max ($25\text{ }\mu\text{V}$ typ, OP07E/C) |
| **Input Offset Voltage Drift ($dV_{OS}/dT$)** | $1.3\text{ }\mu\text{V/}^\circ\text{C}$ max |
| **Input Bias Current ($I_B$)** | $\pm 4.0\text{ nA}$ max ($\pm 1.5\text{ nA}$ typ) |
| **Open-Loop Voltage Gain ($A_{VD}$)** | $400\text{ V/mV}$ ($112\text{ dB}$) min |
| **Common-Mode Rejection Ratio (CMRR)** | $106\text{ dB}$ min ($120\text{ dB}$ typ) |
| **Unity Gain Bandwidth** | $0.6\text{ MHz}$ typ |
| **Slew Rate** | $0.3\text{ V/}\mu\text{s}$ typ |
| **Supply Current** | $2.0\text{ mA}$ typ ($3.0\text{ mA}$ max) |
| **Packages** | 8-pin PDIP (P), SOIC-8 (D) |

## Pin configuration

### 8-Pin DIP / SOIC Package

```
               ┌──────────┐
    OFFSET N1 ─┤ 1      8 ├─ OFFSET N2
          -IN ─┤ 2      7 ├─ V+
          +IN ─┤ 3      6 ├─ OUT
           V- ─┤ 4      5 ├─ NC
               └──────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `OFFSET N1` | Analog Input | Input offset voltage trim terminal 1 |
| 2 | `-IN` | Analog Input | Inverting input terminal |
| 3 | `+IN` | Analog Input | Non-inverting input terminal |
| 4 | `V-` | Power Supply | Negative supply rail ($-\text{V}_S$) or Ground in single-supply systems |
| 5 | `NC` | No Connect | No internal connection |
| 6 | `OUT` | Analog Output | Op-amp output terminal |
| 7 | `V+` | Power Supply | Positive supply rail ($+\text{V}_S$) |
| 8 | `OFFSET N2` | Analog Input | Input offset voltage trim terminal 2 |

## Functional description

- **Precision Bipolar Front-End:** The OP07 utilizes low-noise super-beta input transistors and internal thin-film resistor trimming during wafer manufacturing to achieve exceptional DC precision without chopper-stabilization noise or switching artifacts.
- **Offset Nulling Circuitry:** For applications requiring zero offset, pins 1 and 8 connect across an external $20\text{ k}\Omega$ trim potentiometer whose wiper connects to **$V+$** (pin 7). Adjusting the wiper trims any residual input offset voltage down to sub-microvolt levels without degrading temperature drift.
- **High Common-Mode & Supply Rejection:** With CMRR and PSRR typically exceeding $120\text{ dB}$, input offset remains rock-solid despite supply voltage fluctuations or high common-mode input voltages.

## Absolute maximum ratings

> [!WARNING]
> Stresses beyond these ratings cause permanent damage. Functional operation at these limits is not guaranteed.

| Parameter | Rating | Unit |
|---|---|---|
| Supply Voltage ($V_S = V+ - V-$) | 44 ($\pm 22$) | V |
| Differential Input Voltage | $\pm 30$ | V |
| Input Common-Mode Voltage Range | $\pm 22$ (not to exceed supply rails) | V |
| Output Short-Circuit Duration | Continuous to Ground or either rail | — |
| Operating Free-Air Temperature (OP07C) | 0 to 70 | °C |
| Operating Free-Air Temperature (OP07E) | -40 to 85 | °C |
| Storage Temperature Range | -65 to 150 | °C |

## Electrical characteristics

$V_S = \pm 15\text{ V}$, $T_A = 25^\circ\text{C}$, unless otherwise noted.

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Offset Voltage | $V_{OS}$ | — | 25 | 75 | $\mu\text{V}$ | $V_{CM} = 0\text{ V}$ (OP07E/C) |
| Input Offset Voltage Drift | $dV_{OS}/dT$ | — | 0.5 | 1.3 | $\mu\text{V/}^\circ\text{C}$ | $T_A = 0^\circ\text{C}$ to $70^\circ\text{C}$ |
| Input Offset Current | $I_{OS}$ | — | 0.8 | 3.0 | nA | $V_{CM} = 0\text{ V}$ |
| Input Bias Current | $I_B$ | — | $\pm 1.5$ | $\pm 4.0$ | nA | $V_{CM} = 0\text{ V}$ |
| Input Voltage Range | $V_{ICR}$ | $\pm 13.0$ | $\pm 14.0$ | — | V | $V_S = \pm 15\text{ V}$ |
| Output Voltage Swing | $V_O$ | $\pm 12.0$ | $\pm 13.0$ | — | V | $R_L \ge 2\text{ k}\Omega$ |
| Large-Signal Voltage Gain | $A_{VD}$ | 400 | 500 | — | $\text{V/mV}$ | $R_L \ge 2\text{ k}\Omega, V_O = \pm 10\text{ V}$ |
| Common-Mode Rejection Ratio | $\text{CMRR}$ | 106 | 120 | — | dB | $V_{CM} = \pm 13\text{ V}$ |
| Power Supply Rejection Ratio | $\text{PSRR}$ | 100 | 110 | — | dB | $V_S = \pm 3\text{ V}$ to $\pm 18\text{ V}$ |
| Slew Rate | $\text{SR}$ | 0.1 | 0.3 | — | $\text{V/}\mu\text{s}$ | $R_L \ge 2\text{ k}\Omega$ |
| Unity-Gain Bandwidth | $\text{B}_1$ | 0.4 | 0.6 | — | MHz | $f = 10\text{ kHz}$ |
| Supply Current | $I_{CC}$ | — | 2.0 | 3.0 | mA | $V_O = 0\text{ V}$, No load |

## Typical application

### Precision Thermocouple Signal Conditioning with Offset Null Potentiometer

```
                 +15V
                  │
             ┌────┴──────────────────────────┐
             │       20kΩ Potentiometer      │
             └───[/\/\/\/\/\/\/\/\/\/\/\/\\]─┘
                   │                      │
             Pin 1 │ (OFFSET N1)    Pin 8 │ (OFFSET N2)
             ┌─────┴──────────────────────┴─────┐
             │                                  │
             │           OP07                   │
  (+) ───────┤ Pin 3 (+IN)                      │
Thermocouple │                                  │
  (-) ──┬────┤ Pin 2 (-IN)         Pin 6 (OUT)  ├────► Amplified Sensor Output
        │    │                                  │
        │    └──────────────────┬───────────────┘
        │                       │
       [R1 = 100Ω]             [Rf = 100kΩ] (Gain = 1001)
        │                       │
       GND ─────────────────────┘
```

The OP07 amplifies small millivolt-range thermocouple voltages with negligible offset errors ($75\text{ }\mu\text{V}$ represents only $\sim 1.8^\circ\text{C}$ uncalibrated error on a K-type thermocouple, which can be trimmed to zero using the offset potentiometer).

## Common mistakes

- **Using the OP07 for Audio or High-Speed Signals:** The OP07 is strictly a precision DC/low-frequency amplifier. Its slew rate is only $0.3\text{ V/}\mu\text{s}$ and its bandwidth is $0.6\text{ MHz}$. For audio or AC instrumentation, use the higher-speed **OP27** ($2.8\text{ V/}\mu\text{s}$, $8\text{ MHz}$) or **OPA2140** ($20\text{ V/}\mu\text{s}$, $11\text{ MHz}$).
- **Connecting the Offset Trim Wiper to V- Instead of V+:** The OP07 null circuit is designed so the trim potentiometer wiper connects to **$V+$** (Pin 7). Connecting the wiper to $V-$ (which is standard on some other op-amps like the 741) will not null the offset and can damage the input stage.
- **Assuming Rail-to-Rail Input or Output:** The OP07 is not a rail-to-rail op-amp. On $\pm 15\text{V}$ supplies, the inputs must stay within $\pm 13\text{V}$, and the output can only swing to $\pm 12.5\text{V}$. In a single 5V supply system, the linear operating range is severely constricted; use a modern rail-to-rail precision op-amp like the OPA333 or MCP6001 for low-voltage single-supply designs.

## Notes

- **Suffix Guide:** `OP07C` (commercial grade, 0°C to 70°C), `OP07E` (higher precision industrial grade, -40°C to 85°C), `OP07D` (standard grade). Suffix `P` denotes PDIP-8; suffix `D` or `S` denotes SOIC-8.
- **Pin Compatibility:** The OP07 is a direct pin-compatible precision drop-in upgrade for the ubiquitous **LM741**, **LF351**, and **TL071** in low-speed circuits.
