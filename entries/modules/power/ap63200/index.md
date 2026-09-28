## Overview

The **AP63200** (part number `AP63200WU-7`) is a 2A, wide input range ($3.8\text{ V}$ to $32.0\text{ V}$) synchronous step-down (buck) DC-DC converter manufactured by Diodes Incorporated. Housed in a low-profile 6-lead TSOT26 (thin SOT-23-6) package, it represents the modern generation of high-efficiency switching regulators designed to replace hot, power-dissipating linear regulators (like the 7805 and LM317) and bulky asynchronous buck modules (like the LM2596) in space-constrained industrial, automotive infotainment, and embedded IoT systems.

The AP63200 integrates a $125\text{ m}\Omega$ high-side power MOSFET and a $68\text{ m}\Omega$ low-side synchronous rectifier MOSFET, delivering up to $2.0\text{ A}$ continuous output current without requiring an external freewheeling diode. Operating at a nominal switching frequency of $500\text{ kHz}$, the device features proprietary gate-drive circuitry that prevents switching-node ringing without sacrificing MOSFET turn-on and turn-off times.

To simplify electromagnetic compliance (EMC), the AP63200 incorporates internal **Frequency Spread Spectrum (FSS)** modulation with a $\pm 6\%$ jitter envelope centered on the $500\text{ kHz}$ clock, spreading peak radiated and conducted harmonic energy and significantly easing CISPR 25 Class 5 certification. In addition, its ultra-low quiescent current ($22\ \mu\text{A}$ typical) and Pulse Frequency Modulation (PFM) mode provide exceptional efficiency exceeding 85% even down to $1\text{ mA}$ standby loads.

## Quick reference

| Parameter | Value | Notes |
|---|---|---|
| **Converter Architecture** | Synchronous Step-Down (Buck) | Integrated high-side and low-side MOSFETs |
| **Input Supply Voltage ($V_{IN}$)** | $3.8\text{ V}$ to $32.0\text{ V}$ DC | Absolute maximum $35.0\text{ V}$ |
| **Output Voltage Range ($V_{OUT}$)** | $0.8\text{ V}$ to $32.0\text{ V}$ DC | Adjustable via feedback resistor divider |
| **Continuous Output Current** | $2.0\text{ A}$ | Across industrial temperature range |
| **Switching Frequency ($f_{SW}$)** | $500\text{ kHz}$ nominal | Frequency Spread Spectrum ($\pm 6\%$ jitter) |
| **Quiescent Current ($I_Q$)** | $22\ \mu\text{A}$ typical | Light load PFM operation |
| **Shutdown Current ($I_{SD}$)** | $1.0\ \mu\text{A}$ typical | When `EN` pin is grounded |
| **Feedback Reference Voltage ($V_{FB}$)** | $0.800\text{ V}$ ($\pm 1.5\%$) | High-precision bandgap reference |
| **MOSFET On-Resistance** | $125\text{ m}\Omega$ (HS) / $68\text{ m}\Omega$ (LS) | Synchronous rectification |
| **Package** | TSOT26 (Thin SOT-23-6) | $2.9\times 2.8\times 1.0\text{ mm}$ footprint |

## Terminals

The AP63200 uses the 6-lead TSOT26 pinout:

```
          +---+--+---+
     FB --| 1    6 |-- BST
     EN --| 2    5 |-- SW
    VIN --| 3    4 |-- GND
          +----------+
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `FB` | Feedback Input | Feedback voltage sense input. Regulates to $0.800\text{ V}$ via external resistor divider. |
| 2 | `EN` | Digital Input | Enable control input. Pull High ($>1.2\text{ V}$) to enable, Low ($<0.4\text{ V}$) to shut down. |
| 3 | `VIN` | Power Input | Main power input rail ($+3.8\text{ V}$ to $+32.0\text{ V}$ DC). Bypass with low-ESR ceramic capacitor. |
| 4 | `GND` | Ground | Circuit ground reference ($0\text{ V}$). |
| 5 | `SW` | Switching Output | Inductor switching node. Connect to output inductor and bootstrap capacitor. |
| 6 | `BST` | Bootstrap Input | High-side gate driver boost supply. Connect $100\text{ nF}$ ceramic capacitor between `BST` and `SW`. |

## The technical core

### Frequency Spread Spectrum (FSS) EMI reduction

Standard fixed-frequency DC-DC converters generate sharp spectral energy spikes at the fundamental switching frequency ($500\text{ kHz}$) and its integer harmonics ($1.0\text{ MHz}$, $1.5\text{ MHz}$, etc.). These high-amplitude spikes frequently fail FCC and CISPR radiated and conducted EMI tests.

The AP63200 eliminates sharp harmonic peaks through integrated **Frequency Spread Spectrum (FSS)**:
- The internal oscillator is modulated by a pseudo-random triangle waveform that jitters the switching frequency by $\pm 6\%$ around the $500\text{ kHz}$ center frequency.
- The spectral energy of each harmonic is distributed across a wider bandwidth, lowering peak EMI emissions by up to $10\text{ dB}\mu\text{V}$ without external shielding or bulky common-mode chokes.
- Combined with a controlled MOSFET gate-drive slew rate that eliminates high-frequency switching ringing, the AP63200 complies with stringent CISPR 25 Class 5 automotive limits.

### Output voltage calculation

The output voltage is programmed via a resistor divider between $V_{OUT}$, `FB`, and `GND`:

$$ V_{OUT} = V_{FB} \times \left(1 + \frac{R_1}{R_2}\right) = 0.800\text{ V} \times \left(1 + \frac{R_1}{R_2}\right) $$

For optimal loop response and low-power standby operation, select $R_2 = 10\text{ k}\Omega$ to $40\text{ k}\Omega$, then calculate $R_1$:

$$ R_1 = R_2 \times \left(\frac{V_{OUT}}{0.800\text{ V}} - 1\right) $$

**Standard Divider Resistor Pairs ($R_2 = 10.0\text{ k}\Omega$):**
- **$1.8\text{ V}$ Output:** $R_1 = 12.5\text{ k}\Omega$ (standard $12.4\text{ k}\Omega$ or $12.7\text{ k}\Omega$)
- **$3.3\text{ V}$ Output:** $R_1 = 31.25\text{ k}\Omega$ (standard $31.6\text{ k}\Omega$ 1%)
- **$5.0\text{ V}$ Output:** $R_1 = 52.5\text{ k}\Omega$ (standard $52.3\text{ k}\Omega$ or $53.6\text{ k}\Omega$)
- **$12.0\text{ V}$ Output:** $R_1 = 140\text{ k}\Omega$

### Electrical specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Voltage Range | $V_{IN}$ | 3.8 | 12.0 / 24.0 | 32.0 | V | Operating range |
| Feedback Reference Voltage | $V_{FB}$ | 0.788 | 0.800 | 0.812 | V | $T_A = 25^\circ\text{C}$ |
| High-Side Switch On-Resistance | $R_{DS(ON)\_H}$ | — | 125 | 170 | $\text{m}\Omega$ | $V_{IN} = 12\text{ V}$ |
| Low-Side Switch On-Resistance | $R_{DS(ON)\_L}$ | — | 68 | 95 | $\text{m}\Omega$ | $V_{IN} = 12\text{ V}$ |
| Nominal Switching Frequency | $f_{SW}$ | 450 | 500 | 550 | kHz | Center frequency |
| FSS Jitter Range | $\Delta f_{FSS}$ | — | $\pm 6$ | — | % | Spread spectrum modulation |
| Quiescent Current (PFM) | $I_Q$ | — | 22 | 40 | µA | No load, $V_{IN} = 12\text{ V}$ |
| Shutdown Current | $I_{SD}$ | — | 1.0 | 3.0 | µA | $V_{EN} = 0\text{ V}$ |
| Peak Switch Current Limit | $I_{PEAK}$ | 2.5 | 3.0 | 3.6 | A | High-side current trip |
| Thermal Shutdown Temp | $T_{TSD}$ | — | 160 | — | °C | Auto-recovery |

## Usage

### Typical application circuit

```
       +3.8V to +32V DC
  VIN o--------+-------------------------+
               |                         |
              === C_IN (10uF)            |
              --- 50V Ceramic            |
               |                         |
               |        +-------+        |
               |      3 |       | 6      |
               +--------|VIN BST|--------+---||---+ (100nF C_BST)
               |      2 |       | 5               |
   EN o--------+--------|EN   SW|-----------------+----CCCC----+------> VOUT (e.g. 5V / 2A)
                        |       |                      L1 (4.7uH)|
                        |     FB|----+                           |
                        |       | 1  |                          === C_OUT (22uF x 2)
                        |    GND|    |                          --- Ceramic
                        +---+---+    |                           |
                            |       [R1]                         |
                            |        |                           |
                            +--------+--+                        |
                            |           |                        |
                            |          [R2]                      |
                            |           |                        |
  GND o---------------------+-----------+------------------------+------> 0V GND
```

#### External components:
- **Inductor ($L_1$):** $4.7\ \mu\text{H}$ to $10\ \mu\text{H}$ with saturation current $I_{SAT} \ge 3.2\text{ A}$.
- **Input Capacitor ($C_{IN}$):** $10\ \mu\text{F}$ 50V X7R ceramic placed as close as possible to pins 3 (`VIN`) and 4 (`GND`).
- **Output Capacitor ($C_{OUT}$):** Two $22\ \mu\text{F}$ 16V X7R ceramic capacitors in parallel.
- **Bootstrap Capacitor ($C_{BST}$):** $100\text{ nF}$ (0.1 µF) 16V ceramic capacitor between `BST` and `SW`.

## Common mistakes

- **Exceeding 32V input voltage:** While rated for $32.0\text{ V}$ operating and $35.0\text{ V}$ absolute maximum, industrial $24\text{ V}$ systems often experience inductive load-dump voltage spikes reaching $40\text{ V} - 60\text{ V}$. Always add an input TVS diode (e.g. `SMBJ30A`) to clamp inductive voltage spikes.
- **Connecting `EN` to an unmanaged floating trace:** Leaving `EN` floating makes the chip susceptible to capacitive noise coupling. Tie `EN` directly to `VIN` through a $100\text{ k}\Omega$ pull-up resistor or drive actively with a microcontroller GPIO.
- **Omitting bootstrap capacitor ($C_{BST}$):** The high-side N-channel MOSFET requires a charge pump supply higher than $V_{IN}$ to turn on. Leaving $C_{BST}$ disconnected prevents the switch from closing, producing 0V on the output.
- **Trace inductance on the `VIN`/`GND` loop:** High $di/dt$ switching currents through long PCB traces induce voltage spikes that defeat the low-EMI advantages of the IC. Place $C_{IN}$ within $2\text{ mm}$ of pins 3 and 4.

## Notes

- **AP63200 vs AP63203:** While the AP63200 features an adjustable output and 500 kHz switching frequency, the companion **AP63203** operates at a higher frequency of $1.1\text{ MHz}$ and provides an internally trimmed fixed $3.3\text{ V}$ output, saving space and eliminating the external feedback resistor divider entirely.
