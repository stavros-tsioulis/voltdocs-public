## Overview

The **OPA333** (Texas Instruments) is an ultra-high-precision, micropower operational amplifier utilizing proprietary **zero-drift (chopper-stabilized)** CMOS technology. Available in miniature 5-pin SOT-23 (DBV) and SC70 packages, the OPA333 is engineered specifically for low-voltage sensor conditioning, battery-powered medical instruments, strain-gauge load cells, and precision weighing scales.

Conventional op-amps suffer from offset voltages in the hundreds of microvolts or millivolts, along with significant thermal drift ($2\ \mu\text{V}/^\circ\text{C} - 10\ \mu\text{V}/^\circ\text{C}$) and $1/f$ low-frequency flicker noise that severely distorts microvolt-level sensor signals. The OPA333 solves this by dynamically auto-zeroing its input stage continuously:
- Maximum input offset voltage is held below **$10\ \mu\text{V}$** ($2\ \mu\text{V}$ typical).
- Offset voltage thermal drift is virtually zero: **$0.05\ \mu\text{V}/^\circ\text{C}$ maximum** ($0.01\ \mu\text{V}/^\circ\text{C}$ typical).
- $1/f$ flicker noise is completely eliminated down to DC.

Operating from a single supply as low as **$1.8\text{ V}$** up to **$5.5\text{ V}$** DC and drawing just **$17\ \mu\text{A}$** quiescent current, the OPA333 features true **rail-to-rail input and output (RRIO)** swing, allowing full-scale dynamic signal capture with low-voltage 3.3V microcontrollers and ADCs.

## Quick reference

| Parameter | Value | Notes |
|---|---|---|
| **Architecture** | Auto-Zeroing / Chopper-Stabilized | Zero $1/f$ flicker noise |
| **Supply Voltage Range ($V_S$)** | $1.8\text{ V}$ to $5.5\text{ V}$ DC | Single supply or $\pm 0.9\text{V} \dots \pm 2.75\text{V}$ |
| **Input Offset Voltage ($V_{OS}$)** | $10\ \mu\text{V}$ maximum ($2\ \mu\text{V}$ typ) | Laser-trimmed auto-calibration |
| **Offset Voltage Drift** | $0.05\ \mu\text{V}/^\circ\text{C}$ maximum | Extreme stability across $-40^\circ\text{C} \dots +125^\circ\text{C}$ |
| **Quiescent Current ($I_Q$)** | $17\ \mu\text{A}$ typical per channel | Battery and wearable friendly |
| **Gain Bandwidth Product (GBW)**| $350\text{ kHz}$ | Ideal for DC / slow precision sensors |
| **CMRR / PSRR** | $130\text{ dB}$ typical | Rejects supply noise and common-mode shifts |
| **Input Bias Current ($I_B$)** | $70\text{ pA}$ typical | High input impedance CMOS inputs |
| **Input / Output Range** | Rail-to-rail input and output | $100\text{ mV}$ beyond supply rails on input |
| **Package** | 5-pin SOT-23 (DBV) / SC70-5 | Ultra-compact single channel |

## Terminals

The 5-pin SOT-23 (DBV) terminal configuration follows the standard single op-amp pinout:

```
          +---+--+---+
    OUT --| 1    5 |-- V+
     V- --| 2        |
    IN+ --| 3    4 |-- IN-
          +----------+
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `OUT` | Analog Output | Rail-to-rail amplifier output terminal. |
| 2 | `V-` (`GND`) | Power | Negative power supply rail or ground reference ($0\text{ V}$). |
| 3 | `IN+` | Analog Input | Non-inverting operational amplifier input. |
| 4 | `IN-` | Analog Input | Inverting operational amplifier input. |
| 5 | `V+` | Power | Positive power supply rail ($+1.8\text{ V}$ to $+5.5\text{ V}$ DC). Bypass with $0.1\ \mu\text{F}$ ceramic cap. |

## The technical core

### Zero-drift auto-zeroing architecture

In standard bipolar or CMOS amplifiers, low-frequency $1/f$ noise (flicker noise) increases inversely with frequency below $\approx 1\text{ kHz}$, degrading the measurement of slowly varying DC signals (such as temperature, pressure, or weight).

The OPA333 employs an internal switched-capacitor chopper topology:
1. The input differential signal is modulated up to a high internal chopping frequency ($\approx 125\text{ kHz}$).
2. The high-frequency chopped signal is amplified by the internal gain stage, leaving the op-amp's inherent DC offset and $1/f$ noise unchopped.
3. A synchronous demodulator demodulates the amplified signal back down to DC while simultaneously modulating the offset and $1/f$ noise up to $125\text{ kHz}$.
4. A low-pass filter strips away the $125\text{ kHz}$ high-frequency components, leaving a pure, ultra-clean DC signal with **zero $1/f$ noise** and negligible offset.

### Electrical specifications ($V_S = 5.0\text{ V}$, $T_A = 25^\circ\text{C}$)

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Offset Voltage | $V_{OS}$ | — | 2 | 10 | µV | $V_{CM} = (V+) - 1.3\text{ V}$ |
| Offset Voltage vs Temp | $dV_{OS}/dT$ | — | 0.01 | 0.05 | $\mu\text{V}/^\circ\text{C}$ | $-40^\circ\text{C} \le T_A \le 125^\circ\text{C}$ |
| Input Bias Current | $I_B$ | — | 70 | 200 | pA | $T_A = 25^\circ\text{C}$ |
| Common-Mode Rejection | $CMRR$ | 110 | 130 | — | dB | $(V-) - 0.1\text{ V} \le V_{CM} \le (V+) + 0.1\text{ V}$ |
| Power Supply Rejection | $PSRR$ | 110 | 130 | — | dB | $V_S = 1.8\text{ V} \dots 5.5\text{ V}$ |
| Open-Loop Voltage Gain | $A_{OL}$ | 110 | 130 | — | dB | $R_L = 10\text{ k}\Omega$ |
| Gain Bandwidth Product | $GBW$ | — | 350 | — | kHz | $C_L = 50\text{ pF}$ |
| Slew Rate | $SR$ | — | 0.16 | — | $\text{V}/\mu\text{s}$ | Unity gain step |
| Quiescent Current | $I_Q$ | — | 17 | 25 | µA | $I_O = 0$ |
| Short-Circuit Current | $I_{SC}$ | — | $\pm 5$ | — | mA | Output shorted to rail |

## Usage

### High-precision low-side current shunt amplifier

Measuring current through a $10\text{ m}\Omega$ current sense resistor down to $1\text{ mA}$ requires measuring a tiny $10\ \mu\text{V}$ signal—where standard op-amp offsets would cause $>100\%$ error:

```
        Load Current Return
    o------------+-------------------------------------+
                 |                                     |
                [ ] R_shunt (0.010 Ohm, 1%)            |
                 |                                     |
    o------------+--------[ R1 (1k) ]---------+        |
   GND                                        |        |
                                             === C1    |
                                       (1nF) ---       |
                                              |        |
                                         3 +--+---+    |
                                           | IN+  |    |
                                           |      | 1  |
                                           |  OUT |----+-----> VOUT to MCU ADC
                                           |      |    |       (1.0V per Ampere)
                                         4 | IN-  |    |
                                      +----+--+---+    |
                                      |       | 5      |
                                     [ ] R2   | V+    [ ] R_f (100k)
                                    (1k)      +--+     |
                                      |          |     |
                                     === C2     +5V    |
                               (1nF) ---               |
                                      |                |
  GND o-------------------------------+----------------+
```

With Gain $A_V = 1 + R_f / R_2 = 1 + 100\text{ k}\Omega / 1\text{ k}\Omega = 101$:
- At $I_{load} = 1.0\text{ A}$, $V_{shunt} = 10\text{ mV} \implies V_{OUT} = 1.01\text{ V}$.
- At $I_{load} = 1.0\text{ mA}$, $V_{shunt} = 10\ \mu\text{V} \implies V_{OUT} = 1.01\text{ mV}$.
- Because the OPA333 input offset is only $2\ \mu\text{V}$, measurement precision remains accurate across three decades of current range.

## Common mistakes

- **Attempting to amplify high-frequency signals:** The OPA333 has a modest Gain Bandwidth Product ($350\text{ kHz}$) and slew rate ($0.16\text{ V}/\mu\text{s}$). It is designed for DC and sub-kilohertz signals; attempting to amplify $50\text{ kHz}$ signals with gain will result in heavy attenuation and phase lag.
- **Driving heavy capacitive loads directly:** Driving capacitive loads $>100\text{ pF}$ directly from the output can degrade phase margin and cause ringing. Insert a small isolation resistor ($50\ \Omega - 100\ \Omega$) between the output and capacitive loads.
- **Inadequate supply decoupling:** The internal chopper generates small switching transients at $125\text{ kHz}$. Always solder a $0.1\ \mu\text{F}$ low-ESR ceramic decoupling capacitor within $2\text{ mm}$ of the $V+$ pin.

## Notes

- **OPA333 vs INA333:** When amplifying full differential Wheatstone bridge sensors (load cells or pressure sensors) with significant common-mode DC offset, the **INA333** integrates three zero-drift op-amps with laser-trimmed internal matching resistors into a single instrumentation amplifier IC.
