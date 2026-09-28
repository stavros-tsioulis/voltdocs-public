## Overview

The **L-7113ID** (Kingbright catalog part number **WP7113ID**) is the quintessential 5mm (T-1 3/4) red diffused through-hole light-emitting diode (LED). Representing the single most common discrete visual indicator component in electronics history, it serves as the benchmark red LED populated across starter kits, student breadboard labs, bench instrumentation, and industrial control panels.

Fabricated with a Gallium Arsenide Phosphide on Gallium Phosphide (GaAsP/GaP) semiconductor die and enclosed in a red-tinted diffused epoxy package, the L-7113ID delivers an intense, vibrant **$625\text{ nm}$** dominant red wavelength. Operating at standard current levels ($10\text{ mA} - 20\text{ mA}$), it outputs $12\text{ mcd}$ to over $50\text{ mcd}$ (typically **$30\text{ mcd}$**) of wide-angle ($60^\circ$) diffused light.

Functionally interchangeable parts from other manufacturers include the Vishay `TLHR5400`, Cree `C503B-RAN`, Lite-On `LTL-4223`, OptoSupply `OSNX3131A`, and generic electronics kit 5mm red LEDs.

## Quick reference

| Parameter | Value | Notes |
|---|---|---|
| **Emitted Color** | High Efficiency Red | Peak $635\text{ nm}$, Dominant $625\text{ nm}$ |
| **Lens Appearance** | Red Diffused Epoxy | Smooth wide-angle dispersion |
| **Typical Forward Voltage ($V_F$)**| $2.0\text{ V}$ (typical at $20\text{ mA}$) | Max $2.5\text{ V}$ |
| **Rated Test Current ($I_F$)** | $20.0\text{ mA}$ | Full brightness standard |
| **Absolute Max Forward Current** | $30.0\text{ mA}$ DC ($160\text{ mA}$ pulse) | Continuous limit |
| **Luminous Intensity ($I_V$)** | $12\text{ mcd}$ min, $30\text{ mcd}$ typ | At $I_F = 20\text{ mA}$ |
| **Viewing Angle ($2\theta_{1/2}$)** | $60^\circ$ | Full viewing cone |
| **Reverse Breakdown Voltage** | $5.0\text{ V}$ maximum | Sensitive to reverse polarity |
| **Package** | 5mm (T-1 3/4) Radial Through-Hole | $2.54\text{ mm}$ (0.1") lead spacing |

## Terminals

```
            +---------+
           /    RED    \
          |  DIFFUSED   |
          |    DOME     |
          |  [ANODE]    |
          +-+---------+-+
          | | (FLAT)  | |  <-- Flat edge on package rim marks CATHODE (-)
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

| Terminal | Lead Length | Package Physical Feature | Description |
|---|---|---|---|
| **Anode ($+$)** | Longer lead | Rounded rim edge | Positive terminal. Connect to positive supply / GPIO via series resistor. |
| **Cathode ($-$)** | Shorter lead | Flat notch on rim; larger internal anvil flag | Negative terminal. Connect to ground ($0\text{ V}$) or open-drain sinking driver. |

## The technical core

### Current-limiting resistor selection ($V_F = 2.0\text{ V}$)

$$ R_{limit} = \frac{V_{supply} - V_F}{I_F} = \frac{V_{supply} - 2.0\text{ V}}{I_F} $$

The classic Arduino and hobbyist resistor selections:

| Supply Voltage ($V_{supply}$) | Desired Current ($I_F$) | Calculated Resistance | Standard Resistor Choice | Typical Brightness |
|---|---|---|---|---|
| **$5.0\text{ V}$ (Arduino Uno / 5V)** | $10\text{ mA}$ | $\frac{5.0 - 2.0}{0.010} = 300\ \Omega$ | **$330\ \Omega$** | Normal / Clean Indication |
| **$5.0\text{ V}$ (Arduino Uno / 5V)** | $13.6\text{ mA}$ | $\frac{5.0 - 2.0}{0.0136} = 220\ \Omega$| **$220\ \Omega$** | High / Full Brightness |
| **$3.3\text{ V}$ (ESP32 / Raspberry Pi)**| $10\text{ mA}$ | $\frac{3.3 - 2.0}{0.010} = 130\ \Omega$ | **$150\ \Omega$** | Normal Indication |
| **$3.3\text{ V}$ (ESP32 / Raspberry Pi)**| $13\text{ mA}$ | $\frac{3.3 - 2.0}{0.013} = 100\ \Omega$ | **$100\ \Omega$** | High Brightness |
| **$12.0\text{ V}$ (Automotive / Industrial)**| $15\text{ mA}$ | $\frac{12.0 - 2.0}{0.015} = 667\ \Omega$ | **$680\ \Omega$ (1/4W)** | High Brightness |

### Electrical specifications ($T_A = 25^\circ\text{C}$)

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Forward Voltage | $V_F$ | 1.8 | 2.0 | 2.5 | V | $I_F = 20\text{ mA}$ |
| Luminous Intensity | $I_V$ | 12 | 30 | 50 | mcd | $I_F = 20\text{ mA}$ |
| Dominant Wavelength | $\lambda_{dom}$ | — | 625 | — | nm | $I_F = 20\text{ mA}$ |
| Peak Emission Wavelength | $\lambda_{peak}$ | — | 635 | — | nm | $I_F = 20\text{ mA}$ |
| Spectral Bandwidth | $\Delta \lambda$ | — | 45 | — | nm | $I_F = 20\text{ mA}$ |
| Capacitance | $C$ | — | 15 | — | pF | $V_F = 0\text{ V}$, $f = 1\text{ MHz}$ |
| Reverse Breakdown Voltage | $V_R$ | 5.0 | — | — | V | $I_R = 10\ \mu\text{A}$ |
| Power Dissipation | $P_D$ | — | — | 75 | mW | Continuous rating |

## Usage

### Arduino "Blink" reference wiring

```
       +5V Supply
         |
  +------+------+
  | Arduino Uno |
  |             |
  |    Pin D13  |-------[ R_limit (220 Ohm or 330 Ohm) ]-------+
  |             |                                              |
  |         GND |---+                                      [+] |
  +-------------+   |                                     +----+----+
                    |                                     | L-7113ID|
                    |                                     +----+----+
                    |                                      [-] |
                    +------------------------------------------+
```

## Common mistakes

- **Omitting the series resistor:** Never connect directly to a $5\text{ V}$ or $3.3\text{ V}$ supply. Unregulated current will instantly destroy the internal PN junction bond wire.
- **Exceeding microcontroller GPIO total current limit:** An ATmega328P allows up to $20\text{ mA}$ per GPIO pin, but the **entire microcontroller chip** has a maximum total supply limit of $200\text{ mA}$. If driving 10 or more LEDs simultaneously, use $1\text{ k}\Omega$ series resistors or external buffer drivers (such as the 74HC595 or ULN2003A).
- **Trimming leads without noting polarity:** Once the long/short leads are cut flush, look for the flat notch on the plastic rim or inspect the internal leadframe: the larger triangular anvil flag is always the cathode ($-$).

## Notes

- **L-7113ID vs L-53LID:** Standard L-7113ID LEDs are designed for optimal brightness at $10\text{ mA} - 20\text{ mA}$. When designing battery-powered circuits where every milliamp counts, use the low-current **L-53LID** or **L-7113LGD**, which deliver comparable visual contrast at only $2\text{ mA}$.
