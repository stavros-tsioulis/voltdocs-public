## Overview

The **TL081** (TL081CP) is a high-speed JFET-input single general-purpose operational amplifier manufactured by Texas Instruments, STMicroelectronics, and ON Semiconductor. Incorporating well-matched high-voltage JFETs and bipolar transistors on a monolithic chip, the TL081 was engineered as a high-performance modern replacement for classic bipolar op-amps such as the $\mu\text{A}741$.

With a fast slew rate of **$13\text{ V}/\mu\text{s}$**, a gain-bandwidth product of **$3\text{ MHz}$**, and an exceptionally high input impedance of **$10^{12}\,\Omega$** ($1\text{ T}\Omega$) with picoampere input bias currents (**$30\text{ pA}$** typical), the TL081 eliminates the loading errors and slew-rate distortion inherent in older general-purpose op-amps. It uses the industry-standard single op-amp 8-pin pinout, allowing direct drop-in upgrading of 741-based circuits in active filters, high-impedance sensor buffers, integrators, and audio preamps.

## Quick reference

| | |
|---|---|
| **Op-Amp Channels** | 1 (Single Op-Amp) |
| **Input Architecture** | High-Impedance JFET Differential Input |
| **Supply Voltage Range ($V_S$)** | $\pm 3.5\text{ V}$ to $\pm 18.0\text{ V}$ (Dual) / $7.0\text{ V}$ to $36.0\text{ V}$ (Single) |
| **Slew Rate ($SR$)** | $13.0\text{ V}/\mu\text{s}$ typical |
| **Gain-Bandwidth Product ($GBW$)** | $3.0\text{ MHz}$ typical |
| **Input Bias Current ($I_B$)** | $30\text{ pA}$ typical ($200\text{ pA}$ max at $25^\circ\text{C}$) |
| **Input Offset Voltage ($V_{OS}$)** | $3.0\text{ mV}$ typical ($15.0\text{ mV}$ max for standard grade) |
| **Input Resistance ($R_{IN}$)** | $10^{12}\,\Omega$ ($1\text{ T}\Omega$) |
| **Supply Current ($I_{CC}$)** | $1.4\text{ mA}$ typical ($2.5\text{ mA}$ max) |
| **Packages** | 8-pin PDIP (P), SOIC-8 (D), TSSOP-8 (PW) |

## Pin configuration

### 8-Pin DIP / SOIC Package

```
             ┌───┴───┐
     OFFSET 1│ 1   8 │ NC (No Connection)
        -IN 2│       │ 7 V+ (Positive Supply)
        +IN 3│ TL081 │ 6 OUT (Op-Amp Output)
         V- 4│       │ 5 OFFSET (Trim)
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `OFFSET` | Analog Input | Input offset null terminal 1 (connect to trim potentiometer) |
| 2 | `-IN` | Analog Input | Inverting op-amp input |
| 3 | `+IN` | Analog Input | Non-inverting op-amp input |
| 4 | `V-` | Power Supply | Negative supply rail ($-3.5\text{ V} \dots -18.0\text{ V}$ or GND) |
| 5 | `OFFSET` | Analog Input | Input offset null terminal 2 (connect to trim potentiometer) |
| 6 | `OUT` | Analog Output | Op-amp output |
| 7 | `V+` | Power Supply | Positive supply rail ($+3.5\text{ V} \dots +18.0\text{ V}$) |
| 8 | `NC` | Unconnected | No internal connection |

## Comparison: TL081 vs. µA741

The TL081 shares the exact physical pinout of the classic 741 op-amp while vastly improving every high-frequency and input metric:

| Parameter | TL081 (JFET) | µA741 (Bipolar) | Improvement |
|---|---|---|---|
| **Input Bias Current ($I_B$)** | **$30\text{ pA}$** | $80\text{ nA}$ ($80,000\text{ pA}$) | **$2,600\times$ lower loading** |
| **Input Resistance ($R_{IN}$)** | **$10^{12}\,\Omega$ ($1\text{ T}\Omega$)** | $2\times 10^6\,\Omega$ ($2\text{ M}\Omega$) | **$500,000\times$ higher impedance** |
| **Slew Rate ($SR$)** | **$13.0\text{ V}/\mu\text{s}$** | $0.5\text{ V}/\mu\text{s}$ | **$26\times$ faster response** |
| **Bandwidth ($GBW$)** | **$3.0\text{ MHz}$** | $1.0\text{ MHz}$ | **$3\times$ wider frequency range** |
| **Supply Current ($I_{CC}$)** | $1.4\text{ mA}$ | $1.7\text{ mA}$ | Lower power consumption |

## Absolute maximum ratings

> [!WARNING]
> Stresses beyond these ratings cause permanent breakdown. Exceeding maximum differential input voltage can damage the input JFET gates.

| Parameter | Symbol | Min | Max | Unit |
|---|---|---|---|---|
| Supply Voltage ($V+ - V-$) | $V_S$ | — | $36.0$ | V |
| Differential Input Voltage | $V_{ID}$ | — | $\pm 30.0$ | V |
| Input Voltage Range | $V_I$ | $(V-) - 0.3$ | $(V+) + 0.3$ | V |
| Duration of Output Short Circuit | $t_{sc}$ | Continuous | Continuous | — |
| Operating Free-Air Temperature | $T_A$ | $0$ | $+70$ | °C |
| Storage Temperature Range | $T_{stg}$ | $-65$ | $+150$ | °C |

## Electrical characteristics

($V_S = \pm 15\text{ V}, T_A = 25^\circ\text{C}$ unless otherwise noted)

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Offset Voltage | $V_{OS}$ | — | 3.0 | 15.0 | mV | $R_S \le 10\text{ k}\Omega$ |
| Offset Voltage Temp Drift | $\Delta V_{OS}/\Delta T$ | — | 10 | — | µV/°C | — |
| Input Offset Current | $I_{OS}$ | — | 5.0 | 100.0 | pA | — |
| Input Bias Current | $I_B$ | — | 30.0 | 200.0 | pA | — |
| Common-Mode Input Range | $V_{ICR}$ | $\pm 11$ | $+15 / -12$ | — | V | — |
| Common-Mode Rejection Ratio | $CMRR$ | 70 | 86 | — | dB | $R_S \le 10\text{ k}\Omega$ |
| Large-Signal Voltage Gain | $A_{VD}$ | 25 | 200 | — | V/mV | $V_O = \pm 10\text{ V}, R_L \ge 2\text{ k}\Omega$ |
| Output Voltage Swing | $V_O$ | $\pm 12.0$ | $\pm 13.5$ | — | V | $R_L \ge 2\text{ k}\Omega$ |
| | | $\pm 10.0$ | $\pm 12.0$ | — | V | $R_L \ge 10\text{ k}\Omega$ |
| Slew Rate | $SR$ | 8.0 | 13.0 | — | V/µs | $G = 1, 10\text{ V step}$ |
| Gain-Bandwidth Product | $GBW$ | — | 3.0 | — | MHz | — |
| Equivalent Input Noise | $e_n$ | — | 18.0 | — | nV/√Hz | $f = 1\text{ kHz}$ |
| Quiescent Current | $I_{CC}$ | — | 1.4 | 2.5 | mA | No load |

## Typical application circuit: High-Impedance Sensor Buffer with Offset Null

```
                 +15V
                  │
                ┌─┴──┐
                │ 7  │ (V+)
                │    │
       High-Z   │    │
       Input ───┤ 3  │
       Signal   │(+IN)    TL081
                │         Op-Amp
                │ 2       6
                │(-IN)  (OUT)──────────┬────────────── Output to ADC / Filter
                └───┬─────┴─┐          │
                    │       │          │
                    └───────┴──────────┘ (Unity-Gain Voltage Follower)
                 │     │
            ┌────┘     └────┐
          1 │               │ 5
       (NULL)               (NULL)
          │    ┌─────────┐  │
          └───┤ 10k Pot ├───┘
               └───┬─────┘
                   │ Wiper
                   │
                ┌──┴───┐
                │ 4(V-)│
                └──┬───┘
                   │
                 -15V
```

### Offset Null Procedure
Connect a $10\text{ k}\Omega$ to $100\text{ k}\Omega$ trim potentiometer across pins 1 and 5, with the wiper tied to pin 4 ($V-$). Ground the non-inverting input (pin 3) and adjust the potentiometer until the output voltage measured at pin 6 reaches $0.00\text{ V}$.

## Design considerations & common mistakes

- **Phase Inversion Hazard:** Like many classic JFET-input op-amps, the TL081 exhibits **input phase reversal** if either input voltage is driven too close to the negative supply rail ($V-$). If an input dips within $\approx 3\text{ V}$ of $V-$, the input stage saturates, causing the op-amp output to violently flip to the positive rail ($V+$). In single-supply configurations, bias inputs at least $3\text{ V}$ above ground, or add clamp diodes.
- **Not Suited for Low-Voltage Single-Rail Systems:** The internal biasing circuits of the TL081 require a minimum total supply of $7.0\text{ V}$ ($V+ - V- \ge 7\text{ V}$). Attempting to power the TL081 from a single $+3.3\text{ V}$ or $+5.0\text{ V}$ rail will result in failure to operate. For $3.3\text{V} / 5\text{V}$ single-supply designs, choose a modern CMOS rail-to-rail op-amp such as the **MCP6001** or **MCP601**.
- **Leave Offset Pins Open if Not Trimming:** If DC offset trimming is unnecessary, leave pins 1 and 5 **completely disconnected**. Grounding pins 1 or 5 will cause severe imbalance and huge output offset voltages.
- **Power Supply Decoupling:** To prevent high-frequency oscillations due to the $13\text{ V}/\mu\text{s}$ slew rate, always bypass pin 7 ($V+$) and pin 4 ($V-$) to ground with a $0.1\,\mu\text{F}$ ceramic capacitor placed within a few millimeters of the IC.
