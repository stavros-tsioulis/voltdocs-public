## Overview

The **100nF (0.1 µF)** ceramic capacitor—universally stamped with the 3-digit code **`104`**—is the single most ubiquitous and heavily stocked passive component in modern electronics.

Its primary mission is **high-frequency digital power-rail decoupling (bypassing)**. Every digital integrated circuit (microcontrollers, logic gates, memory chips, op-amps) draws sharp, nanosecond-scale bursts of transient current every time internal transistors switch states. Because PCB power traces have parasitic series inductance, these rapid current spikes cause instantaneous voltage dips and high-frequency ringing on the power rail ("ground bounce" and $V_{CC}$ sag).

A 100nF ceramic capacitor placed immediately adjacent to an IC's power and ground pins acts as an ultra-low-inductance local charge reservoir, delivering energy in nanoseconds to suppress power rail noise. It is also the staple value for analog DC blocking, AC signal coupling, differentiator networks, and low-pass noise filters.

## Quick reference

| Parameter | Value | Notes |
|---|---|---|
| **Nominal Capacitance** | $100\text{ nF} = 0.1\ \mu\text{F} = 100,000\text{ pF}$ | Universal decoupling baseline |
| **Marking Code** | `104` | 10 followed by 4 zeros in pF |
| **Common Dielectric** | X7R (Stable) or Y5V (General) | Multi-Layer Ceramic (MLCC) |
| **Standard Voltage Rating** | $50.0\text{ V}$ DC (typical radial leaded) | $16\text{V} - 50\text{V}$ for SMD |
| **Tolerance** | $\pm 10\%$ (`K`) or $\pm 20\%$ (`M`) | Standard commercial tolerance |
| **Polarity** | Non-polarized (Bi-directional) | Can be inserted in either orientation |
| **ESR / ESL** | Ultralow ($10\text{ m}\Omega - 50\text{ m}\Omega$, $< 1\text{ nH}$) | Superior high-frequency performance |
| **Physical Packages** | Radial Monolithic Bead (0.1" pitch) / 0805 SMD / 0603 SMD | Breadboard and PCB standard |

## Value & markings

### The 3-digit capacitor code decoded

Monolithic radial ceramic capacitors are stamped with a standard 3-digit EIA value code:

| Digit Position | Meaning | Value for "104" |
|---|---|---|
| 1st Digit | 1st significant digit | `1` |
| 2nd Digit | 2nd significant digit | `0` |
| 3rd Digit (Multiplier) | Number of trailing zeros (in pF) | `4` ($\times 10^4 = \times 10,000$) |
| **Calculated Value** | **$10 \times 10^4\text{ pF}$** | **$100,000\text{ pF} = 100\text{ nF} = 0.1\ \mu\text{F}$** |

```
              +-------------+
             /     104K      \    <-- "104" = 100nF, "K" = +/-10%
            |       50V       |   <-- Voltage rating (50V DC)
             \               /
              +------+------+
                     |
              +------+------+
              |             |
           Lead 1        Lead 2    (Non-polarized: orientation does not matter)
```

#### Tolerance Letter Suffix:
- **`J`** = $\pm 5\%$
- **`K`** = $\pm 10\%$ (most common for X7R)
- **`M`** = $\pm 20\%$
- **`Z`** = $+80\% / -20\%$ (common for Y5V)

## Key parameters

| Parameter | Typical Value | Unit | Notes |
|---|---|---|---|
| Capacitance | 100 | nF | Measured at $1\text{ kHz}$, $1.0\text{ V}_{RMS}$ |
| Rated DC Working Voltage ($V_R$)| 50 | V | Safe continuous working voltage |
| Dielectric Type | X7R | — | $-55^\circ\text{C} \dots +125^\circ\text{C}$, $\pm 15\%$ capacitance change |
| Equivalent Series Resistance (ESR)| 25 | $\text{m}\Omega$ | At $1\text{ MHz}$ resonance |
| Equivalent Series Inductance (ESL)| 0.8 | nH | Dependent on lead length / SMD size |
| Self-Resonant Frequency (SRF) | 15 - 25 | MHz | Low impedance valley for digital noise |
| Insulation Resistance | $> 10$ | $\text{G}\Omega$ | Negligible DC leakage |

## Types & dielectrics

Ceramic capacitors vary dramatically depending on the ceramic dielectric material:

1. **X7R (Class II - Recommended):**
   - Temperature stable: capacitance shifts less than $\pm 15\%$ across $-55^\circ\text{C}$ to $+125^\circ\text{C}$.
   - Moderate DC bias effect: effective capacitance decreases by $15\% - 30\%$ at rated voltage.
   - The universal choice for digital decoupling, analog filters, and power supplies.
2. **Y5V / Z5U (Class III - Budget):**
   - High capacitance per volume, but extreme temperature drift ($+22\% / -82\%$).
   - Extreme DC bias sensitivity: at 80% rated voltage, capacitance can drop by over $70\%$.
   - Avoid for timing, filters, or critical decoupling.
3. **C0G / NP0 (Class I):**
   - Near-zero temperature drift ($\pm 30\text{ ppm}/^\circ\text{C}$), zero DC bias voltage effect, zero aging.
   - Best for RF, audio, and precision oscillators, but physically larger at 100nF.

## Combinations

### Parallel connection (additive capacitance)
Connecting multiple capacitors in parallel adds their capacitances together and lowers total ESR:
$$ C_{total} = C_1 + C_2 + C_3 $$
*Example:* Two 100nF capacitors in parallel yield $200\text{ nF}$.

### Series connection (voltage rating sharing)
$$ \frac{1}{C_{total}} = \frac{1}{C_1} + \frac{1}{C_2} \implies C_{total} = \frac{C_1 \times C_2}{C_1 + C_2} $$
*Example:* Two 100nF capacitors in series yield $50\text{ nF}$ with double the combined voltage rating.

## Typical uses

### 1. Digital IC power decoupling (bypass)
Placed within $5\text{ mm}$ of every microcontroller, logic IC, and op-amp power pin:

```
        +5V Rail
   o-------+------------------------------+
           |                              |
          === C_bypass (100nF Ceramic)   +--+---+
          --- (Code 104)                 | VCC  |
           |                             |  MCU |
   o-------+-----------------------------| GND  |
  GND (0V)                               +------+
```

### 2. High/low frequency dual-rail decoupling pair
In power supply output stages, a $100\text{ nF}$ ceramic capacitor is placed in parallel with a $100\ \mu\text{F}$ electrolytic capacitor:
- The $100\ \mu\text{F}$ electrolytic smooths low-frequency line ripple ($100\text{ Hz} - 100\text{ kHz}$).
- The $100\text{ nF}$ ceramic bypasses high-frequency switching spikes ($1\text{ MHz} - 50\text{ MHz}$) that the inductive leads of the electrolytic capacitor cannot absorb.

## Common mistakes

- **Placing decoupling capacitors far from the IC pins:** A capacitor placed $50\text{ mm}$ away across long PCB traces adds tens of nanohenries of lead inductance ($L_{trace} \approx 1\text{ nH/mm}$), completely neutralizing its ability to filter fast nanosecond switching spikes. Keep bypass caps within $3\text{ mm} - 5\text{ mm}$ of IC power pins.
- **Ignoring DC bias voltage derating in tiny SMD packages:** In miniature 0402 or 0603 SMD packages, applying $12\text{ V}$ to a $16\text{ V}$-rated 100nF X7R capacitor can reduce its actual capacitance down to $30\text{ nF} - 50\text{ nF}$. Use a $25\text{ V}$ or $50\text{ V}$ rated capacitor to maintain full capacitance under bias.
- **Microphonic piezo noise in sensitive analog/audio audio paths:** High-dielectric Class II ceramics (X7R, Y5V) exhibit a piezoelectric effect—mechanical vibration or tapping on the board generates audible electrical voltage spikes. In sensitive pre-amp audio paths, use film capacitors (polyester/polypropylene) instead.

## Notes

- **Breadboarding Standard:** In radial through-hole packages, 100nF capacitors have a standard $2.54\text{ mm}$ (0.1") lead spacing, fitting directly into adjacent breadboard tie points.
