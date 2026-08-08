## Overview

The **NE556** (LM556 / SA556) is a dual precision timing circuit in a 14-pin DIP/SOIC package manufactured by Texas Instruments, STMicroelectronics, and ON Semiconductor. Containing two fully independent 555-type timers sharing common power supply (`VCC`) and ground (`GND`) pins, each half can generate accurate time delays or oscillations from microseconds up to hours.

Operating across a supply range of **4.5V to 16.0V DC**, both output drivers can sink or source up to **200mA**. The NE556 is ideal for dual-stage timing applications, two-tone sirens, cascaded pulse generators, and PWM motor/LED controllers where two 555 timers are required in a single IC package.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | 4.5 V to 16.0 V DC |
| **Output Sink / Source Current** | Up to $200\text{ mA}$ per channel |
| **Independent Timers** | 2 (Timer 1 and Timer 2) |
| **Operating Modes** | Astable (Oscillator), Monostable (One-Shot), PWM, Bistable |
| **Timing Accuracy** | $< 1\%$ typical drift across temperature |
| **Max Oscillation Frequency** | Up to $500\text{ kHz}$ |
| **Package** | 14-pin DIP / SOIC-14 |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
     1DISCH 1│ 1   14│ VCC
     1THRES 2│       │13 2DISCH
    1CONT  3│       │12 2THRES
     1RESET 4│ NE556 │11 2CONT
      1OUT  5│       │10 2RESET
     1TRIG  6│       │9  2OUT
       GND  7│       │8  2TRIG
             └───────┘
```

| Pin | Name | Timer | Description |
|---|---|---|---|
| 1 | `1DISCH` | Timer 1 | Discharge pin (Open-collector transistor to GND) |
| 2 | `1THRES` | Timer 1 | Threshold input pin (Triggers output LOW when $V > \frac{2}{3}V_{CC}$) |
| 3 | `1CONT` | Timer 1 | Control voltage pin (Access to $\frac{2}{3}V_{CC}$ reference divider) |
| 4 | `1RESET` | Timer 1 | Active-Low Reset pin (Forces output LOW when $<0.4\text{V}$) |
| 5 | `1OUT` | Timer 1 | Timer 1 Output (Push-pull, drives up to 200mA) |
| 6 | `1TRIG` | Timer 1 | Trigger input pin (Triggers output HIGH when $V < \frac{1}{3}V_{CC}$) |
| 7 | `GND` | Common | Common Ground reference (0 V) |
| 8 | `2TRIG` | Timer 2 | Trigger input pin |
| 9 | `2OUT` | Timer 2 | Timer 2 Output |
| 10 | `2RESET` | Timer 2 | Active-Low Reset pin |
| 11 | `2CONT` | Timer 2 | Control voltage pin |
| 12 | `2THRES` | Timer 2 | Threshold input pin |
| 13 | `2DISCH` | Timer 2 | Discharge pin |
| 14 | `VCC` | Common | Positive Supply Power pin (+4.5V to +16.0V DC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 4.5 | 12.0 | 16.0 | V | DC |
| Supply Current (Both Timers) | $I_{CC}$ | — | 6.0 | 12.0 | mA | $V_{CC} = 5\text{V}, V_{OUT} = \text{Low}$ |
| High Output Voltage Drop | $V_{OH}$ | $V_{CC}-1.5$ | $V_{CC}-1.2$ | — | V | $I_{SOURCE} = 100\text{mA}, V_{CC} = 15\text{V}$ |
| Low Output Voltage | $V_{OL}$ | — | 0.1 | 0.25 | V | $I_{SINK} = 10\text{mA}, V_{CC} = 5\text{V}$ |
| Trigger Voltage Threshold | $V_{TRIG}$ | 1.45 | 1.67 | 1.9 | V | $V_{CC} = 5\text{V}$ |
| Threshold Voltage Level | $V_{THRES}$ | 3.1 | 3.33 | 3.5 | V | $V_{CC} = 5\text{V}$ |

## Typical Applications

### Cascaded Sequential Timer (Delayed Pulse Generator)

Timer 1 operates as a monostable one-shot. When Timer 1's output (`1OUT`) completes its pulse and drops LOW, it triggers Timer 2 (`2TRIG`) to start a second timed pulse.

```
                      +5V
                       │
  Trigger In ──► [Pin 6: 1TRIG]   [Pin 5: 1OUT] ───[10nF Cap]───► [Pin 8: 2TRIG]
                       │                                                │
                 NE556 Timer 1                                    NE556 Timer 2
                       │                                                │
                 [Pin 1: 1DISCH]                                  [Pin 9: 2OUT] ──► Output Pulse 2
```

## Common mistakes

- **Confusing NE556 14-pin pinout with 8-pin NE555:** Pin numbers are completely different. For instance, Pin 4 on a 555 is `RESET`, whereas Pin 4 on an NE556 is `1RESET` (Reset for Timer 1 only), and Pin 8 on a 555 is `VCC` whereas Pin 8 on an NE556 is `2TRIG`.
- **Leaving `1RESET` or `2RESET` floating:** If reset pins are left floating, environmental noise can trigger unpredictable resets. Connect `1RESET` (Pin 4) and `2RESET` (Pin 10) directly to **`VCC`** if not used.
- **Cross-talk between Timer 1 and Timer 2 during output switching:** Internal bipolar transistors produce power supply current spikes up to $300\text{mA}$ during output transitions. Without a **$10\ \mu\text{F} \dots 100\ \mu\text{F}$ electrolytic capacitor** paired with a **$100\text{ nF}$ ceramic capacitor** placed close across Pin 14 (`VCC`) and Pin 7 (`GND`), Timer 1 transitions will inadvertently trigger Timer 2.

## Notes

- **NE555 vs NE556 vs NE558:** NE555 is a single timer (DIP-8); NE556 is a dual timer (DIP-14); NE558 is a quad timer (DIP-16).
