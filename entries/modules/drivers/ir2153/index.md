## Overview

The **IR2153** (and its modern successor **IRS2153D**) is an improved self-oscillating half-bridge gate driver IC manufactured by Infineon Technologies (originally developed by International Rectifier). It integrates a high-voltage ($600\text{ V}$) half-bridge driver core with a front-end oscillator circuit functionally equivalent to the classic CMOS 555 timer.

The IC is widely utilized in offline electronic ballasts for fluorescent and HID lighting, compact switch-mode power supplies (SMPS), induction heaters, high-frequency AC transformers, and DIY resonant inverters. By combining micropower startup circuitry ($< 100\,\mu\text{A}$), an internal $15.6\text{ V}$ Zener supply clamp, and an internal $1.2\,\mu\text{s}$ cross-conduction deadtime generator, the IR2153 allows a complete offline half-bridge inverter to be constructed with minimal external components.

## Quick reference

| | |
|---|---|
| **Driver Type** | Self-Oscillating High and Low Side Half-Bridge Gate Driver |
| **High-Side Floating Offset Voltage ($V_S$)** | Up to $600\text{ V}$ DC max |
| **Supply Voltage Range ($V_{CC}$)** | $10.0\text{ V}$ to $15.6\text{ V}$ DC ($V_{CC}$ clamped at $15.6\text{ V}$) |
| **Internal $V_{CC}$ Shunt Clamp** | $15.6\text{ V}$ nominal ($I_{CC} \le 25\text{ mA}$) |
| **UVLO Turn-On Threshold ($V_{CCUV+}$)** | $9.0\text{ V}$ typical ($8.1\text{ V} \dots 9.9\text{ V}$) |
| **UVLO Turn-Off Threshold ($V_{CCUV-}$)** | $8.0\text{ V}$ typical ($7.2\text{ V} \dots 8.8\text{ V}$) |
| **Gate Drive Output Current** | $+210\text{ mA}$ source / $-420\text{ mA}$ sink typical |
| **Internal Deadtime ($t_{dt}$)** | $1.2\,\mu\text{s}$ typical ($0.75\,\mu\text{s} \dots 1.65\,\mu\text{s}$) |
| **Oscillator Duty Cycle** | $50\%$ nominal (inherent via toggle flip-flop) |
| **Micropower Startup Current ($I_{QCC}$)** | $80\,\mu\text{A}$ typical ($150\,\mu\text{A}$ max) |
| **Packages** | 8-pin DIP (PDIP-8), 8-pin SOIC (SO-8) |

## Pin configuration

### 8-Pin DIP / SOIC Package

```
             ┌───┴───┐
        VCC 1│ 1   8 │ VB (High-Side Bootstrap Supply)
         RT 2│       │ 7 HO (High-Side Gate Drive)
         CT 3│ IR2153│ 6 VS (High-Side Floating Return)
        COM 4│       │ 5 LO (Low-Side Gate Drive)
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power Supply | Logic and low-side gate drive supply voltage (internally clamped at $15.6\text{ V}$) |
| 2 | `RT` | Passive I/O | Oscillator timing resistor connection; output drives charging/discharging of `CT` |
| 3 | `CT` | Analog Input | Oscillator timing capacitor connection to ground (`COM`) |
| 4 | `COM` | Power / Ground | IC ground and low-side driver return |
| 5 | `LO` | Gate Drive Output | Low-side power MOSFET / IGBT gate drive output |
| 6 | `VS` | Power Reference | High-side floating supply return / half-bridge switching node |
| 7 | `HO` | Gate Drive Output | High-side power MOSFET / IGBT gate drive output |
| 8 | `VB` | Power Supply | High-side floating bootstrap supply voltage |

## Functional description

### Internal Oscillator Operation

The front-end oscillator uses a comparator network similar to a 555 timer. The timing capacitor $C_T$ (connected between pin 3 and `COM`) is charged and discharged between $1/3\,V_{CC}$ and $2/3\,V_{CC}$ through timing resistor $R_T$ (connected between pin 2 and pin 3).

```
                 VCC
                  │
                [RT]
                  ├─────────── Pin 2 (RT)
                  │
                  ├─────────── Pin 3 (CT)
                [CT]
                  │
                 COM
```

The oscillation frequency ($f_{osc}$) is calculated by:
$$f_{osc} \approx \frac{1}{1.4 \times (R_T + 75\,\Omega) \times C_T} \approx \frac{1}{1.4 \times R_T \times C_T}$$

The internal latch is triggered alternately by the oscillator thresholds, feeding a toggle flip-flop. Because the high-side (`HO`) and low-side (`LO`) channels are steered by this flip-flop, the output duty cycle is precisely **$50\%$** (minus the fixed deadtime).

### Deadtime and Shoot-Through Elimination

To prevent hazardous "shoot-through" cross-conduction where both the high-side and low-side MOSFETs are briefly ON simultaneously, the IR2153 enforces an internal fixed **$1.2\,\mu\text{s}$ deadtime** between the turn-off of one output and the turn-on of the opposite output.

### Micropower Startup & Zener Clamp

Prior to operation, while $V_{CC}$ is below the undervoltage lockout threshold ($V_{CCUV+} \approx 9.0\text{V}$), the IC draws less than $100\,\mu\text{A}$. This allows the IC to start up directly from a high-voltage DC bus ($+300\text{ V}$) through a high-value trickle resistor ($R_{start} \approx 150\text{ k}\Omega \dots 330\text{ k}\Omega$). Once running, power can be supplied by an auxiliary transformer winding or charge pump. The internal $15.6\text{ V}$ shunt Zener clamp protects $V_{CC}$ from overvoltage without requiring an external regulator.

## Absolute maximum ratings

> [!WARNING]
> Stresses beyond these ratings will cause irreversible breakdown. Ensure floating bootstrap voltage ($V_B - V_S$) never exceeds absolute limits.

| Parameter | Symbol | Min | Max | Unit |
|---|---|---|---|---|
| High-Side Floating Supply Absolute Voltage | $V_B$ | $-0.3$ | $+625$ | V |
| High-Side Floating Supply Offset Voltage | $V_S$ | $V_B - 25$ | $V_B + 0.3$ | V |
| High-Side Output Voltage | $V_{HO}$ | $V_S - 0.3$ | $V_B + 0.3$ | V |
| Low-Side Output Voltage | $V_{LO}$ | $-0.3$ | $V_{CC} + 0.3$ | V |
| Timing Resistor Pin Voltage | $V_{RT}$ | $-0.3$ | $V_{CC} + 0.3$ | V |
| Timing Capacitor Pin Voltage | $V_{CT}$ | $-0.3$ | $V_{CC} + 0.3$ | V |
| Supply Current (Zener Clamped) | $I_{CC}$ | — | $25$ | mA |
| Allowable Offset Slew Rate | $dV_S/dt$ | — | $50$ | V/ns |
| Maximum Power Dissipation ($T_A = 25^\circ\text{C}$, DIP-8) | $P_D$ | — | $1.0$ | W |
| Junction Operating Temperature | $T_J$ | $-55$ | $+150$ | °C |

## Electrical characteristics

($V_{BIAS} (V_{CC}, V_{BS}) = 12\text{ V}$, $C_L = 1000\text{ pF}$, $T_A = 25^\circ\text{C}$ unless otherwise specified)

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| $V_{CC}$ Rising Turn-On Threshold | $V_{CCUV+}$ | 8.1 | 9.0 | 9.9 | V | $V_{CC}$ increasing |
| $V_{CC}$ Falling Turn-Off Threshold | $V_{CCUV-}$ | 7.2 | 8.0 | 8.8 | V | $V_{CC}$ decreasing |
| $V_{CC}$ Under-Voltage Hysteresis | $V_{CCUVH}$ | 0.5 | 1.0 | — | V | — |
| $V_{CC}$ Internal Zener Clamp Voltage | $V_{CLAMP}$ | 14.6 | 15.6 | 16.8 | V | $I_{CC} = 5\text{ mA}$ |
| Micropower Startup Current | $I_{QCC}$ | — | 80 | 150 | µA | $V_{CC} < V_{CCUV+}$ |
| Operating Quiescent Current | $I_{CC}$ | — | 0.8 | 1.5 | mA | $f_{osc} = 20\text{ kHz}$ |
| Output Peak Source Current | $I_{O+}$ | 180 | 210 | — | mA | $V_O = 0\text{ V}, t_{pulse} \le 10\,\mu\text{s}$ |
| Output Peak Sink Current | $I_{O-}$ | 360 | 420 | — | mA | $V_O = 12\text{ V}, t_{pulse} \le 10\,\mu\text{s}$ |
| Turn-On Rise Time | $t_r$ | — | 80 | 150 | ns | $C_L = 1000\text{ pF}$ |
| Turn-Off Fall Time | $t_f$ | — | 40 | 100 | ns | $C_L = 1000\text{ pF}$ |
| Internal Deadtime | $t_{dt}$ | 0.75 | 1.20 | 1.65 | µs | — |

## Typical application circuit

```
       +300V High-Voltage DC Bus
       ────────────────────────┬──────────────────────────┬─────────────────────────────┐
                               │                          │                             │
                             ┌─┴──┐                       │                          ┌──┴──┐
                             │Rst │ (180k, 1W)            │                          │ Q1  │ NMOS
                             │    │                    ┌──┴──┐ Dboot                 │     │ (IRF840)
                             └─┬──┘                    │ ▲   │ (UF4007)              └──┬──┘
                               │                       └─┬───┘                          │
                               │                         │                              ├─── Half-Bridge Node
                               ├────────────┬────────────┼───────────┐                  │    (to load / LC tank)
                               │            │            │           │                  │
                             ┌─┴──┐       ┌─┴──┐       ┌─┴──┐     ┌──┴──┐            ┌──┴──┐
                             │C1  │       │ 1  │(VCC)  │ 8  │(VB) │     │ Rg (22Ω)   │ Q2  │ NMOS
                             │47µF│       │    └───────┘    │     │ 7   ├───[/\/\/\ ]┤     │ (IRF840)
                             │25V │       │                 │     │(HO) │     HO     └──┬──┘
                             └──┬─┘       │                 ├─────┤ 6   │               │
                                │         │                 │     │(VS) ├───────────────┤
                                │         │                 │     └──┬──┘               │
                       ┌────────┤         │     IR2153      │        │                  │
                       │        │         │                 │     ┌──┴──┐               │
                      ┌┴──┐     │         │                 │     │ 5   │ Rg (22Ω)      │
                   RT │   │     │         │                 │     │(LO) ├───[/\/\/\ ]───┤ LO
                      └┬──┘     │         │                 │     └──┬──┘               │
                       ├────────┼─────────┤ 2 (RT)          │        │                  │
                       │        │         │                 │        │                  │
                      ┌┴──┐     │         │ 3 (CT)   4 (COM)│        │                  │
                   CT │   │     │         └──┬───────────┬──┘        │                  │
                      └──┬┘     │            │           │           │                  │
                         │      │            │           │           │                  │
       HV Ground ────────┴──────┴────────────┴───────────┴───────────┴──────────────────┴─── COM (0V)
```

### Component Selection
- **Startup Resistor ($R_{st}$):** $150\text{ k}\Omega$ to $330\text{ k}\Omega$ ($1\text{ W} \dots 2\text{ W}$) drops high-voltage DC down to charge capacitor $C_1$.
- **Bootstrap Diode ($D_{boot}$):** Must be an **ultra-fast recovery diode** ($t_{rr} \le 75\text{ ns}$) rated for $\ge 600\text{ V}$, such as the **UF4007**, **MUR160**, or **HER107**. Never use standard rectifier diodes like the 1N4007.
- **Bootstrap Capacitor ($C_{boot}$):** $0.1\,\mu\text{F} \dots 1.0\,\mu\text{F}$ low-ESR ceramic or high-grade film capacitor rated for $\ge 25\text{ V}$ placed between pin 8 (`VB`) and pin 6 (`VS`).
- **Gate Resistors ($R_g$):** $10\,\Omega \dots 47\,\Omega$ damp gate ringing and parasitic oscillation without delaying turn-off unduly.

## Design considerations & common mistakes

- **Never Use a Standard 1N4007 as the Bootstrap Diode:** The bootstrap diode switches at the full converter frequency ($20\text{ kHz} \dots 100\text{ kHz}$) across up to $400\text{ V}$. A standard 1N4007 has a recovery time of $2\,\mu\text{s} \dots 30\,\mu\text{s}$, causing severe reverse current spikes, destructive heating, and catastrophic failure of both the diode and the IR2153.
- **Negative Voltage Spikes on Pin 6 (`VS`):** During inductive switching transitions and body diode conduction of low-side MOSFET $Q_2$, pin 6 can undershoot ground (`COM`) by $-2\text{ V} \dots -5\text{ V}$. Sustained negative undershoots below $-5\text{ V}$ pull charge out of internal isolation wells, triggering latch-up. Solder a fast Schottky diode (e.g., BAT54 or 1N5819) with cathode to `VS` and anode to `COM` directly at the IC pins to clamp undershoot.
- **Floating Supply Sag at Low Frequencies:** The high-side bootstrap capacitor only recharges while the low-side MOSFET $Q_2$ is ON and pin 6 (`VS`) is grounded. If operating below $10\text{ kHz}$, ensure $C_{boot}$ is large enough ($\ge 1\,\mu\text{F}$) so leakage current and gate charge do not deplete $V_{BS}$ below the $8.0\text{ V}$ UVLO threshold before the cycle completes.
- **Oscillator Noise Coupling:** Pins 2 (`RT`) and 3 (`CT`) operate with high impedance and sensitive comparator trip points. Route traces to $R_T$ and $C_T$ tightly adjacent to the IC pins, away from the fast-switching high-voltage nodes $V_S$ and $V_B$ ($dV/dt \ge 10\text{ V/ns}$), to avoid erratic frequency jitter.
