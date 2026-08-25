## Overview

The **74LS14** (SN74LS14) is a monolithic Low-Power Schottky Transistor-Transistor Logic (**LS-TTL**) IC containing six independent inverting buffer gates with **Schmitt-trigger inputs**. Each gate functions as an inverter with built-in input hysteresis.

Because the input switching threshold differs for positive-going signals ($V_{T+} \approx 1.6\text{ V}$) and negative-going signals ($V_{T-} \approx 0.8\text{ V}$), the 74LS14 exhibits a typical hysteresis voltage of **$V_H \approx 0.8\text{ V}$**. This hysteresis transforms slowly varying, noisy, or corrupted analog inputs into sharp, jitter-free square-wave digital signals without false output transitions or oscillation. It is a staple component in retrocomputing, arcade boards, button debounce circuits, and simple RC relaxation clock generators.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | $4.75\text{ V}$ to $5.25\text{ V}$ DC ($5.0\text{ V}$ nominal $\pm 5\%$) |
| **Logic Family** | Low-Power Schottky Bipolar TTL (74LS) |
| **Circuit Function** | 6 Independent Schmitt-Trigger Inverters ($Y = \overline{A}$) |
| **Positive-Going Threshold ($V_{T+}$)** | $1.4\text{ V} \dots 1.9\text{ V}$ ($1.6\text{ V}$ typical) |
| **Negative-Going Threshold ($V_{T-}$)** | $0.5\text{ V} \dots 1.0\text{ V}$ ($0.8\text{ V}$ typical) |
| **Hysteresis Voltage ($V_H$)** | $0.4\text{ V} \dots 1.4\text{ V}$ ($0.8\text{ V}$ typical) |
| **Output Sink Current ($I_{OL}$)** | Up to $16.0\text{ mA}$ (or $8.0\text{ mA}$ min) |
| **Propagation Delay ($t_{pd}$)** | $15\text{ ns}$ typical ($22\text{ ns}$ max) |
| **Package Options** | 14-pin DIP / SOIC-14 |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
          1A 1│ 1   14│ VCC
          1Y 2│       │13 6A
          2A 3│       │12 6Y
          2Y 4│ 74LS14│11 5A
          3A 5│       │10 5Y
          3Y 6│       │9  4A
         GND 7│       │8  4Y
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `1A` | Schmitt Input | Inverter 1 Input with Hysteresis |
| 2 | `1Y` | TTL Output | Inverter 1 Output ($1Y = \overline{1A}$) |
| 3 | `2A` | Schmitt Input | Inverter 2 Input |
| 4 | `2Y` | TTL Output | Inverter 2 Output |
| 5 | `3A` | Schmitt Input | Inverter 3 Input |
| 6 | `3Y` | TTL Output | Inverter 3 Output |
| 7 | `GND` | Power | Ground reference (0 V) |
| 8 | `4Y` | TTL Output | Inverter 4 Output |
| 9 | `4A` | Schmitt Input | Inverter 4 Input |
| 10 | `5Y` | TTL Output | Inverter 5 Output |
| 11 | `5A` | Schmitt Input | Inverter 5 Input |
| 12 | `6Y` | TTL Output | Inverter 6 Output |
| 13 | `6A` | Schmitt Input | Inverter 6 Input |
| 14 | `VCC` | Power | Supply voltage (+4.75 V to +5.25 V DC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 4.75 | 5.00 | 5.25 | V | Operating commercial range |
| Positive Threshold Voltage | $V_{T+}$ | 1.4 | 1.6 | 1.9 | V | $V_{CC} = 5.0\text{V}$ |
| Negative Threshold Voltage | $V_{T-}$ | 0.5 | 0.8 | 1.0 | V | $V_{CC} = 5.0\text{V}$ |
| Hysteresis Voltage | $V_H$ | 0.4 | 0.8 | 1.4 | V | $V_{T+} - V_{T-}, V_{CC} = 5.0\text{V}$ |
| High-Level Output Voltage | $V_{OH}$ | 2.7 | 3.4 | — | V | $V_{CC} = 4.75\text{V}, I_{OH} = -400\ \mu\text{A}$ |
| Low-Level Output Voltage | $V_{OL}$ | — | 0.35 | 0.5 | V | $V_{CC} = 4.75\text{V}, I_{OL} = 8.0\text{ mA}$ |
| Output Low Current Sink | $I_{OL}$ | 8.0 | 16.0 | — | mA | $V_{CC} = 4.75\text{V}, V_{OL} \le 0.5\text{V}$ |
| Propagation Delay ($L \to H$) | $t_{PLH}$ | — | 15 | 22 | ns | $V_{CC} = 5.0\text{V}, C_L = 15\text{ pF}$ |
| Propagation Delay ($H \to L$) | $t_{PHL}$ | — | 15 | 22 | ns | $V_{CC} = 5.0\text{V}, C_L = 15\text{ pF}$ |
| Quiescent Supply Current | $I_{CC}$ | — | 8.6 | 16.0 | mA | Total IC current ($I_{CCL} + I_{CCH}$) |

## Typical Applications

### 1. Push-Button Debounce Circuit

Mechanical switches bounce rapidly for $2\text{ ms} \dots 10\text{ ms}$ upon contact. The RC filter absorbs rapid bounces, while the 74LS14 Schmitt trigger provides a clean, bounce-free digital transition:

```
      +5V
       │
      [ R1: 10kΩ ]
       │
 Switch ───┬────────[ R2: 1kΩ ]───► [Pin 1: 1A]
 (to GND)  │                         74LS14
        [ C1: 100nF ]              [Pin 2: 1Y] ──► Clean Debounced Logic Signal
           │
          GND
```

### 2. Single-Gate RC Relaxation Oscillator

```
            ┌─────[ R = 10kΩ ]─────┐
            │                      │
            ├───► [Pin 1: 1A]      │
            │       74LS14         ├────► Square Wave Clock Output
            │     [Pin 2: 1Y] ─────┘
        [ C = 100nF ]
            │
           GND
```

*Frequency: $f \approx \frac{1}{0.8 \times R \times C}$ (Keep $R \le 10\text{ k}\Omega$ to accommodate TTL input bias current).*

## Common mistakes

- **Using too large a feedback resistor in RC oscillators:** Unlike CMOS gates, a 74LS input draws up to $-0.4\text{ mA}$ when below $V_{T+}$. If $R > 10\text{ k}\Omega$, this input current will prevent the capacitor from discharging down to $V_{T-}$, stopping oscillation. Keep $R$ between $330\ \Omega$ and $4.7\text{ k}\Omega$ (or use a **74HC14** if large megohm resistors are needed).
- **Driving 5V CMOS directly without a pull-up resistor:** 74LS outputs only reach $V_{OH} \approx 3.4\text{ V}$. When interfacing with a standard 5V CMOS input ($V_{IH} \ge 3.5\text{ V}$), add a $2.2\text{ k}\Omega$ pull-up resistor to $+5\text{V}$.
- **Exceeding the 5.25V supply rail limit:** Operating above 5.5V will cause severe overheating and damage the bipolar transistors.

## Notes

- **Pin-Compatible Modern Equivalents:** 74HC14 (CMOS Schmitt inverter), 74HCT14 (TTL-compatible CMOS Schmitt inverter), 74AHCT14.
