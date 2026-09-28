## Overview

The **TL494** is an industry-standard fixed-frequency pulse-width modulation (PWM) control integrated circuit manufactured by Texas Instruments. Originally developed as an all-in-one controller for switch-mode power supplies (SMPS), it became one of the most widely deployed power management ICs in electronics history, notably powering generations of desktop PC ATX power supplies, car audio DC-DC step-up converters, half-bridge inverters, and battery chargers.

The TL494 incorporates all the primary building blocks required for PWM control: an internal linear sawtooth oscillator, two uncommitted error amplifiers, an on-chip precision 5.0V reference regulator, an adjustable dead-time control (DTC) comparator, a pulse-steering flip-flop, and two 200mA uncommitted output transistors. The chip can be easily configured for either single-ended (parallel) or alternating push-pull operation.

## Quick reference

| | |
|---|---|
| **Function** | Fixed-Frequency Pulse-Width Modulation (PWM) Controller |
| **Supply Voltage Range ($V_{CC}$)** | $7.0\text{ V}$ to $40.0\text{ V}$ DC |
| **Internal Reference Output ($V_{REF}$)** | $5.0\text{ V} \pm 1\%$ (at $I_{REF} = 10\text{ mA}$) |
| **Output Sink / Source Current** | $200\text{ mA}$ max per output transistor |
| **Oscillator Frequency Range** | $1\text{ kHz}$ to $300\text{ kHz}$ |
| **Output Modes** | Push-Pull or Single-Ended (Pin 13 selectable) |
| **Packages** | 16-pin PDIP, SOIC-16, TSSOP-16 |

## Pin configuration

### 16-Pin DIP / SOIC Pinout

```
               ┌──────────┐
         1IN+ ─┤ 1     16 ├─ 2IN+
         1IN- ─┤ 2     15 ├─ 2IN-
     FEEDBACK ─┤ 3     14 ├─ REF (5.0V)
          DTC ─┤ 4     13 ├─ OUTPUT CTRL
           CT ─┤ 5     12 ├─ VCC
           RT ─┤ 6     11 ├─ C2
          GND ─┤ 7     10 ├─ E2
           C1 ─┤ 8      9 ├─ E1
               └──────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `1IN+` | Analog Input | Error Amplifier 1 non-inverting input |
| 2 | `1IN-` | Analog Input | Error Amplifier 1 inverting input |
| 3 | `FEEDBACK` | Analog I/O | Error amplifier output / PWM comparator input (compensation loop) |
| 4 | `DTC` | Analog Input | Dead-time control input (sets minimum off-time; 0V to 3.3V) |
| 5 | `CT` | Timing | Timing capacitor connection (determines oscillator frequency) |
| 6 | `RT` | Timing | Timing resistor connection ($R_T \ge 1.0\text{ k}\Omega$) |
| 7 | `GND` | Ground | System ground (0 V) |
| 8 | `C1` | Open Collector | Collector of internal output transistor 1 (up to 40V, 200mA) |
| 9 | `E1` | Open Emitter | Emitter of internal output transistor 1 |
| 10 | `E2` | Open Emitter | Emitter of internal output transistor 2 |
| 11 | `C2` | Open Collector | Collector of internal output transistor 2 (up to 40V, 200mA) |
| 12 | `VCC` | Power Supply | Positive DC supply voltage (+7.0 V to +40.0 V) |
| 13 | `OUTPUT CTRL` | Digital Input | Output mode: Tie to GND for parallel single-ended; tie to REF for push-pull |
| 14 | `REF` | Power Output | 5.0 V precision reference output (up to 10 mA load) |
| 15 | `2IN-` | Analog Input | Error Amplifier 2 inverting input (typically used for current limiting) |
| 16 | `2IN+` | Analog Input | Error Amplifier 2 non-inverting input |

## Functional description

The TL494 coordinates PWM power conversion via several interconnected stages:

1. **Oscillator:** Charges timing capacitor $C_T$ with a constant current set by $R_T$, producing a linear sawtooth waveform.
   - For **single-ended output** (Pin 13 = `GND`): $f_{osc} = \frac{1}{R_T \times C_T}$
   - For **push-pull output** (Pin 13 = `REF`): $f_{out} = \frac{1}{2 \times R_T \times C_T}$
   - Recommended component values: $1.0\text{ k}\Omega \le R_T \le 500\text{ k}\Omega$, $470\text{ pF} \le C_T \le 10\text{ }\mu\text{F}$.
2. **Dead-Time Control (Pin 4 DTC):** Compares the sawtooth ramp with the voltage at pin 4. Grounding pin 4 provides a built-in minimum dead-time of $\sim 3\%$. Applying an external voltage from $0\text{ V}$ to $3.3\text{ V}$ proportionally increases dead-time from $3\%$ to $100\%$, providing soft-start and preventing shoot-through in half-bridge converters.
3. **Error Amplifiers:** Two independent high-gain op-amps configured as a wired-OR junction driving the PWM comparator. The common-mode input range extends from $-0.3\text{ V}$ to $V_{CC} - 2\text{ V}$. One amplifier is typically dedicated to voltage regulation while the second handles over-current limiting.
4. **Output Stage:** Two independent NPN transistors with uncommitted collectors (`C1`, `C2`) and emitters (`E1`, `E2`). They can be wired as common-emitter switches or emitter-followers driving external MOSFETs or BJTs.

## Absolute maximum ratings

> [!WARNING]
> Stresses beyond these absolute maximum ratings cause permanent damage. Functional operation at these limits is not implied.

| Parameter | Rating | Unit |
|---|---|---|
| Supply Voltage ($V_{CC}$) | 41 | V |
| Collector Output Voltage ($V_{C1}, V_{C2}$) | 41 | V |
| Collector Output Current ($I_{C1}, I_{C2}$) | 250 | mA |
| Error Amplifier Input Voltage Range | $-0.3$ to $V_{CC} + 0.3$ | V |
| Operating Free-Air Temperature ($T_A$, TL494C) | 0 to 70 | °C |
| Operating Free-Air Temperature ($T_A$, TL494I) | -40 to 85 | °C |
| Storage Temperature Range | -65 to 150 | °C |

## Electrical characteristics

$V_{CC} = 15\text{ V}$, $T_A = 25^\circ\text{C}$, unless otherwise noted.

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Reference Output Voltage | $V_{REF}$ | 4.75 | 5.00 | 5.25 | V | $I_{REF} = 1.0\text{ mA}$ |
| Reference Line Regulation | $\Delta V_{REF}$ | — | 2 | 25 | mV | $V_{CC} = 7\text{ V}$ to $40\text{ V}$ |
| Reference Load Regulation | $\Delta V_{REF}$ | — | 1 | 15 | mV | $I_{REF} = 1.0\text{ mA}$ to $10\text{ mA}$ |
| Oscillator Frequency | $f_{osc}$ | 90 | 100 | 110 | kHz | $C_T = 0.001\text{ }\mu\text{F}, R_T = 10\text{ k}\Omega$ |
| Error Amp Input Offset Voltage | $V_{IO}$ | — | 2 | 10 | mV | $V_O (\text{pin 3}) = 2.5\text{ V}$ |
| Error Amp Open-Loop Gain | $A_{VD}$ | 70 | 95 | — | dB | $\Delta V_O = 3\text{ V}, R_L = 2\text{ k}\Omega$ |
| Error Amp Common-Mode Range | $V_{ICR}$ | -0.3 | — | $V_{CC}-2$ | V | $V_{CC} = 7\text{ V}$ to $40\text{ V}$ |
| Collector Saturation Voltage | $V_{CE(sat)}$ | — | 1.1 | 1.3 | V | Common emitter: $I_C = 200\text{ mA}$ |
| Emitter-Follower Output Volts | $V_O$ | $V_{CC}-2.5$ | $V_{CC}-1.5$ | — | V | Emitter follower: $I_E = -200\text{ mA}$ |
| Quiescent Current | $I_{CC}$ | — | 9 | 15 | mA | $V_{CC} = 15\text{ V}$, outputs open |

## Typical application

### Push-Pull DC-DC Inverter / Converter

```
                      +12V Battery Power Input
                               │
                ┌──────────────┴──────────────┐
                │      Center Tap of XFMR     │
                │                             │
             ┌──┴──┐                       ┌──┴──┐
             │ XFMR│                       │ XFMR│  Secondary ──► High Voltage Output
             └──┬──┘                       └──┬──┘
                │                             │
          Drain │                       Drain │
             [MOSFET 1]                    [MOSFET 2]
          Gate  │                       Gate  │
           ┌────┘                        ┌────┘
           │                             │
           │ Pin 9 (E1)                  │ Pin 10 (E2)
       ┌───┴─────────────────────────────┴───┐
       │     C1, C2 tied to +12V VCC         │
       │                                     │
       │                 TL494               │
       │                                     │
       │ Pin 13 (OUTPUT CTRL) ──► Pin 14 REF │ (Push-Pull alternating mode)
       │ Pin 4  (DTC) ──────────► Soft-Start │ (Cap to REF, Resistor to GND)
       │ Pin 6  (RT) ───────────► 12kΩ to GND│
       │ Pin 5  (CT) ───────────► 1nF to GND │ (Frequency ≈ 40 kHz per phase)
       └─────────────────────────────────────┘
```

### Soft-Start Configuration

Connect a capacitor between Pin 14 (`REF`) and Pin 4 (`DTC`), with a parallel resistor to `GND`. At power-on, the discharged capacitor pulls `DTC` up to 5V (forcing 0% duty cycle). As the capacitor charges through the ground resistor, `DTC` ramps down to 0V, gradually increasing the maximum duty cycle to its operating point without high inrush current.

## Common mistakes

- **Leaving Dead-Time Control (Pin 4) floating:** Pin 4 has high input impedance. If left floating, capacitive pickup can pull the pin high, suppressing output switching and causing the power supply to appear dead. If dead-time adjustment is not required, tie Pin 4 directly to `GND`.
- **Leaving the second error amplifier floating:** The TL494 has two error amplifiers connected in a wired-OR configuration. If the unused amplifier is left floating, its output can randomly swing high and override the voltage regulation loop. Always tie the unused amplifier's non-inverting input (`IN+`) to `GND` and its inverting input (`IN-`) to `REF`.
- **Incorrect Output Control (Pin 13) wiring in push-pull converters:** Tying Pin 13 to `GND` sets the outputs to parallel single-ended mode, causing both output transistors to switch simultaneously. In push-pull or half-bridge topologies, this causes catastrophic shoot-through. For push-pull, Pin 13 **must** be tied to Pin 14 (`REF`).
- **Exceeding Error Amplifier common-mode range:** The inputs cannot sense voltages within 2V of $V_{CC}$. In high-side current sensing applications, always use a dedicated high-side current-sense amplifier or sense in the ground return path.

## Notes

- **Suffixes:** `TL494CN` is the commercial temperature (0°C to 70°C) 16-pin PDIP. `TL494IN` is the industrial temperature (-40°C to 85°C) 16-pin PDIP.
- **Cross-Reference / Equivalents:** Pin-compatible second-source equivalents include Samsung/Fairchild **KA7500B**, Daewoo **DBL494**, and Fujitsu **MB3759**.
