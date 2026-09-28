## Overview

The **L-7113LGD** (standard Kingbright catalog part number **WP7113LGD**) is a ubiquitous 5mm (T-1 3/4) low-current green diffused through-hole light-emitting diode (LED). Built with a Gallium Phosphide (GaP) green light-emitting diode die encapsulated in a green-tinted diffused epoxy dome, it is a standard fixture in Arduino starter kits, breadboard prototyping assortments, and commercial equipment status panels.

As a **low-current (`LGD`)** variant, the diode is optimized to deliver crisp, eye-pleasing green indication ($3.5\text{ mcd}$ typical luminous intensity) at a forward current of just **$2.0\text{ mA}$**, compared to standard $10\text{ mA} - 20\text{ mA}$ LEDs (`L-7113GD`). This makes it exceptionally valuable in battery-operated circuits, microcontroller output pins with tight current budgets, and dense multi-LED status arrays where reducing overall supply draw is critical.

The package features a wide **$60^\circ$ viewing angle** ($2\theta_{1/2}$) with soft, even light diffusion, eliminating sharp blinding hotspots and ensuring clear visibility from wide angles.

## Quick reference

| Parameter | Value | Notes |
|---|---|---|
| **Emitted Color** | Green | Peak $565\text{ nm}$, Dominant $568\text{ nm}$ |
| **Lens Appearance** | Green Diffused Epoxy | Soft uniform illumination |
| **Typical Forward Voltage ($V_F$)**| $2.2\text{ V}$ (typical at $2\text{ mA}$) | Max $2.5\text{ V}$ |
| **Rated Test Current ($I_F$)** | $2.0\text{ mA}$ | Low-current optimized |
| **Absolute Max Forward Current** | $25.0\text{ mA}$ DC ($140\text{ mA}$ pulse) | Continuous maximum rating |
| **Luminous Intensity ($I_V$)** | $1.0\text{ mcd}$ min, $3.5\text{ mcd}$ typ | At $I_F = 2.0\text{ mA}$ |
| **Viewing Angle ($2\theta_{1/2}$)** | $60^\circ$ | Full viewing cone |
| **Peak Reverse Voltage ($V_R$)** | $5.0\text{ V}$ maximum | Reverse breakdown limit |
| **Package** | 5mm (T-1 3/4) Radial Through-Hole | Standard $2.54\text{ mm}$ (0.1") lead spacing |

## Terminals

The 5mm radial package uses the standard polarity convention:

```
            +---------+
           /   GREEN   \
          |  DIFFUSED   |
          |    DOME     |
          |  [ANODE]    |
          +-+---------+-+
          | | (FLAT)  | |  <-- Flat notch on base rim marks CATHODE (-)
          +-+---------+-+
            |         |
            |         |
            |         |
            |         |
            | (Long)  | (Short)
            |         |
          ANODE    CATHODE
           (+)       (-)
```

| Terminal | Lead Length | Package Physical Indicator | Description |
|---|---|---|---|
| **Anode ($+$)** | Longer lead | Rounded edge of package rim | Positive terminal. Connect through series resistor to positive supply / GPIO. |
| **Cathode ($-$)** | Shorter lead | Flat notch on rim; larger internal flag | Negative terminal. Connect to ground ($0\text{ V}$) or active-low sinking driver. |

## The technical core

### Current-limiting resistor calculation

LEDs must always be driven with a current-limiting element in series:

$$ R_{limit} = \frac{V_{supply} - V_F}{I_F} $$

Because green GaP LEDs have a slightly higher bandgap energy than red GaAsP LEDs, $V_F$ is typically **$2.2\text{ V}$** (compared to $2.0\text{ V}$ for red):

#### Standard Resistor Values for 2 mA Low-Current Drive:
- **$3.3\text{ V}$ Logic / Microcontroller:**
  $$ R_{limit} = \frac{3.3\text{ V} - 2.2\text{ V}}{0.002\text{ A}} = \frac{1.1\text{ V}}{0.002\text{ A}} = 550\ \Omega \quad \implies \text{Use } \mathbf{560\ \Omega} \text{ or } \mathbf{680\ \Omega} $$
- **$5.0\text{ V}$ Arduino / 5V Logic:**
  $$ R_{limit} = \frac{5.0\text{ V} - 2.2\text{ V}}{0.002\text{ A}} = \frac{2.8\text{ V}}{0.002\text{ A}} = 1,400\ \Omega \quad \implies \text{Use } \mathbf{1.5\text{ k}\Omega} $$
- **$12.0\text{ V}$ Power Supply / Automotive Rail:**
  $$ R_{limit} = \frac{12.0\text{ V} - 2.2\text{ V}}{0.002\text{ A}} = \frac{9.8\text{ V}}{0.002\text{ A}} = 4,900\ \Omega \quad \implies \text{Use } \mathbf{4.7\text{ k}\Omega} \text{ or } \mathbf{5.1\text{ k}\Omega} $$

### Electrical specifications ($T_A = 25^\circ\text{C}$)

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Forward Voltage | $V_F$ | 1.9 | 2.2 | 2.5 | V | $I_F = 2.0\text{ mA}$ |
| Luminous Intensity | $I_V$ | 1.0 | 3.5 | 6.0 | mcd | $I_F = 2.0\text{ mA}$ |
| Dominant Wavelength | $\lambda_{dom}$ | — | 568 | — | nm | $I_F = 2.0\text{ mA}$ |
| Peak Emission Wavelength | $\lambda_{peak}$ | — | 565 | — | nm | $I_F = 2.0\text{ mA}$ |
| Spectral Line Half-Width | $\Delta \lambda$ | — | 30 | — | nm | $I_F = 2.0\text{ mA}$ |
| Capacitance | $C$ | — | 15 | — | pF | $V_F = 0\text{ V}$, $f = 1\text{ MHz}$ |
| Reverse Breakdown Voltage | $V_R$ | 5.0 | — | — | V | $I_R = 10\ \mu\text{A}$ |
| Power Dissipation | $P_D$ | — | — | 62.5 | mW | $T_A = 25^\circ\text{C}$ |

## Usage

### Power-on status indicator circuit

```
       +5V Supply
           |
          [ ] R_limit (1.5k Ohm, 1/4W)
           |
          [+]
        +-----+
        | LED |  L-7113LGD (Green Diffused)
        +-----+
          [-]
           |
          GND (0V)
```

## Common mistakes

- **Using standard $220\ \Omega$ resistors on low-current LEDs:** While a $220\ \Omega$ resistor will not destroy the LED (drawing $\approx 12.7\text{ mA}$, within the $25\text{ mA}$ maximum rating), it defeats the low-current purpose and wastes over $6\times$ more battery power than necessary.
- **Ignoring $V_F$ differences between colors:** Green LEDs drop $\approx 2.2\text{ V}$, whereas red LEDs drop $\approx 2.0\text{ V}$ and blue/white LEDs drop $\approx 3.0\text{ V} - 3.2\text{ V}$. On low-voltage $3.3\text{ V}$ supplies, this difference significantly alters the current if using the same resistor.
- **Reverse voltage damage:** GaP LEDs cannot withstand more than $5.0\text{ V}$ in reverse bias. Never connect backwards across high-voltage rails.

## Notes

- **Green vs Red Human Perception:** The human eye photopic sensitivity curve peaks at $555\text{ nm}$ (very close to the GaP green peak of $565\text{ nm}$). Because human eyes are significantly more sensitive to green than red, a green LED operating at only $2\text{ mA}$ frequently appears visually brighter than a red LED at the same current.
