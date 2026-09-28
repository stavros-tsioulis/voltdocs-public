## Overview

The **FP6291** (commonly ordered as the `FP6291LR-G1`) is a compact, high-efficiency current-mode pulse-width modulation (PWM) step-up (boost) DC-DC converter IC manufactured by Feeling Technology. Housed in a miniature 6-lead SOT-23-6 package, it is widely utilized across portable power banks, handheld electronics, battery chargers, LED drivers, and compact hobby boost modules.

Operating from a low input supply range of $2.6\text{ V}$ to $5.5\text{ V}$ DC (tailored specifically for single-cell Lithium-Ion / Lithium-Polymer batteries and standard $5\text{ V}$ USB power rails), the FP6291 integrates an internal low-resistance ($0.2\ \Omega$) N-channel power MOSFET switch capable of delivering peak switch currents up to $2.5\text{ A}$. With an internal fixed switching frequency of $1.0\text{ MHz}$, external inductor and filter capacitor sizes are minimized, enabling tiny PCB footprints.

The device includes an accurate $0.6\text{ V}$ ($\pm 2\%$) feedback reference voltage, internal soft-start circuitry to suppress inrush current during startup, over-voltage protection (OVP), over-temperature shutdown (OTP), and an adjustable cycle-by-cycle over-current protection threshold programmed via a single external resistor on the `OC` pin.

## Quick reference

| Parameter | Value | Notes |
|---|---|---|
| **Converter Topology** | Current-Mode Step-Up (Boost) | Asynchronous with external Schottky diode |
| **Input Supply Voltage ($V_{IN}$)** | $2.6\text{ V}$ to $5.5\text{ V}$ DC | Absolute maximum $6.0\text{ V}$ |
| **Output Voltage Range ($V_{OUT}$)** | Up to $+12.0\text{ V}$ DC | Set via feedback resistor divider |
| **Switch Current Limit ($I_{SW}$)** | $0.5\text{ A}$ to $2.5\text{ A}$ (Adjustable) | Configured via resistor on `OC` pin |
| **Switching Frequency ($f_{SW}$)** | $1.0\text{ MHz}$ (Fixed) | Allows compact surface-mount inductors |
| **Internal MOSFET $R_{DS(ON)}$** | $200\text{ m}\Omega$ typical | Integrated low-side N-channel switch |
| **Feedback Reference Voltage ($V_{FB}$)** | $0.60\text{ V}$ ($\pm 2\%$) | Internal bandgap reference |
| **Shutdown Current ($I_{SD}$)** | $0.1\ \mu\text{A}$ typical | When `EN` is pulled Low |
| **Package** | SOT-23-6L (SOT-26) | Ultra-compact 6-lead SMT package |

## Terminals

The FP6291 is packaged in a standard 6-lead SOT-23-6:

```
          +---+--+---+
     LX --| 1    6 |-- OC
    GND --| 2    5 |-- VCC
     FB --| 3    4 |-- EN
          +----------+
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `LX` | Power Switch | Inductor switching node. Connected to the drain of the internal N-MOSFET. |
| 2 | `GND` | Ground | Signal and power ground reference ($0\text{ V}$). |
| 3 | `FB` | Feedback Input | Output voltage feedback input. Regulates to $0.60\text{ V}$ via external resistor divider. |
| 4 | `EN` | Digital Input | Enable control input (active-high). Pull High ($>1.5\text{ V}$) to enable, Low ($<0.4\text{ V}$) to shut down. |
| 5 | `VCC` | Power Supply | IC bias power supply pin ($+2.6\text{ V}$ to $+5.5\text{ V}$ DC). Bypass with ceramic capacitor. |
| 6 | `OC` | Configuration | Over-current protection threshold program pin. Connect resistor $R_{OC}$ to `GND`. |

## The technical core

### Boost converter circuit architecture

The FP6291 operates as an asynchronous boost converter requiring an external power inductor ($L_1$), a fast recovery Schottky barrier diode ($D_1$), and low-ESR ceramic input/output capacitors:

```
        L1 (3.3uH - 4.7uH)          D1 (SS34)
  VIN ------CCCC-----------------+---->|----------------+------> VOUT (e.g. 5V or 9V)
                 |               |                      |
                 |             +-+-+                    |
                 |          1  |   | 6                  |
                 +-------------|LX |OC |----+           === C_OUT (22uF)
                               |   |   |    |           |
                 +-------------|VCC|FB |----+--[ R1 ]---+
                 |          5  |   | 3 |                |
  VIN -----------+             |   |   |               [R2]
                 |          4  |   | 2 |                |
  EN  -----------+-------------|EN |GND|----+-----------+------> GND
                               +---+---+    |           |
                                            |          [R_OC]
                                            |           |
  GND --------------------------------------+-----------+
```

### Output voltage programming

The regulated output voltage $V_{OUT}$ is established by an external resistive divider connected between $V_{OUT}$, the feedback pin (`FB`), and `GND`:

$$ V_{OUT} = V_{FB} \times \left(1 + \frac{R_1}{R_2}\right) = 0.60\text{ V} \times \left(1 + \frac{R_1}{R_2}\right) $$

To minimize feedback divider quiescent current while preserving noise immunity, choose $R_2$ in the range of $10\text{ k}\Omega$ to $47\text{ k}\Omega$, then calculate $R_1$:

$$ R_1 = R_2 \times \left(\frac{V_{OUT}}{0.60\text{ V}} - 1\right) $$

**Standard Values:**
- **For $5.0\text{ V}$ Output:** With $R_2 = 15\text{ k}\Omega \implies R_1 = 15\text{ k}\Omega \times (5.0 / 0.6 - 1) = 110\text{ k}\Omega$ (standard 1% resistor).
- **For $9.0\text{ V}$ Output:** With $R_2 = 10\text{ k}\Omega \implies R_1 = 10\text{ k}\Omega \times (9.0 / 0.6 - 1) = 140\text{ k}\Omega$.
- **For $12.0\text{ V}$ Output:** With $R_2 = 10\text{ k}\Omega \implies R_1 = 10\text{ k}\Omega \times (12.0 / 0.6 - 1) = 190\text{ k}\Omega$.

### Over-current protection calibration ($R_{OC}$)

The maximum peak inductor current limit $I_{OCP}$ is adjustable from $0.5\text{ A}$ to $2.5\text{ A}$ via resistor $R_{OC}$ placed between pin 6 (`OC`) and `GND`:

$$ I_{OCP} \approx \frac{K_{OC}}{R_{OC}} $$

Typical values for $R_{OC}$:
- $R_{OC} = 24\text{ k}\Omega \implies I_{OCP} \approx 2.5\text{ A}$ (maximum rated limit)
- $R_{OC} = 36\text{ k}\Omega \implies I_{OCP} \approx 1.8\text{ A}$
- $R_{OC} = 56\text{ k}\Omega \implies I_{OCP} \approx 1.0\text{ A}$

### Electrical specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Supply Voltage | $V_{IN}$ | 2.6 | 3.7 / 5.0 | 5.5 | V | Operating range |
| Output Voltage Range | $V_{OUT}$ | $V_{IN}$ | — | 12.0 | V | Boost configuration |
| Feedback Voltage | $V_{FB}$ | 0.588 | 0.600 | 0.612 | V | $T_A = 25^\circ\text{C}$ |
| Switching Frequency | $f_{SW}$ | 0.8 | 1.0 | 1.2 | MHz | Internal oscillator |
| Maximum Duty Cycle | $D_{MAX}$ | 88 | 92 | — | % | — |
| Switch On-Resistance | $R_{DS(ON)}$ | — | 200 | 300 | $\text{m}\Omega$ | $I_{SW} = 1.0\text{ A}$ |
| Quiescent Current | $I_Q$ | — | 250 | 450 | µA | Active, non-switching |
| Shutdown Current | $I_{SD}$ | — | 0.1 | 1.0 | µA | $V_{EN} = 0\text{ V}$ |
| Enable Threshold High | $V_{EN\_H}$ | 1.5 | — | — | V | Device enabled |
| Enable Threshold Low | $V_{EN\_L}$ | — | — | 0.4 | V | Device shut down |
| Thermal Shutdown | $T_{TSD}$ | — | 160 | — | °C | Automatic recovery |

## Usage

### Component selection guidelines

1. **Power Inductor ($L_1$):**
   - Use a shielded power inductor with an inductance of $3.3\ \mu\text{H}$ to $4.7\ \mu\text{H}$.
   - Ensure the inductor's DC saturation current rating ($I_{SAT}$) exceeds the programmed peak switch current ($I_{OCP}$) by at least 25% to avoid core saturation.
2. **Schottky Diode ($D_1$):**
   - Must be a high-speed Schottky diode rated for reverse voltage $V_R > V_{OUT} + 3\text{ V}$ (e.g. `SS34`, `B240A`, or `MBR0520`).
   - Average forward current rating should match the expected load current. Standard PN silicon diodes (such as 1N4148 or 1N4007) are completely unsuitable due to reverse recovery losses at 1.0 MHz.
3. **Decoupling Capacitors:**
   - Input capacitor ($C_{IN}$): $10\ \mu\text{F}$ X5R/X7R ceramic capacitor directly across $V_{IN}$ and $GND$.
   - Output capacitor ($C_{OUT}$): $22\ \mu\text{F}$ or dual $10\ \mu\text{F}$ low-ESR ceramic capacitors placed immediately between the cathode of $D_1$ and $GND$.

> [!WARNING]
> No Disconnect in Asynchronous Boost Converters:
> In any standard boost converter topology, an intrinsic DC conduction path exists from input to output through the inductor $L_1$ and the diode $D_1$.
> - Setting `EN` Low disables high-frequency switching, but **does not disconnect $V_{IN}$ from $V_{OUT}$**. The output voltage will float at $V_{IN} - V_{diode}$ (e.g. $\approx 3.4\text{ V}$ from a $3.7\text{ V}$ battery).
> - If true zero-current load isolation is required in shutdown, an external P-channel MOSFET switch or dedicated load switch IC must be added on the output rail.

## Common mistakes

- **Input over-voltage:** Supplying more than $5.5\text{ V}$ (absolute maximum $6.0\text{ V}$) to $V_{CC}$ will punch through the internal low-voltage CMOS control circuitry. Do not connect to $12\text{ V}$ automotive or $9\text{ V}$ battery rails directly.
- **Using a standard rectifier diode:** Substituting a slow general-purpose diode (like 1N4001 or 1N4007) instead of a fast Schottky diode causes extreme switching losses, overheating the diode and dropping efficiency below 40%.
- **Saturating the inductor:** Using an undersized miniature SMD inductor rated for only $300\text{ mA}$ causes the core to saturate during current ramping, pulling massive spike currents through the internal MOSFET and tripping overcurrent shutdown.
- **Poor PCB ground loop layout:** Keep the high-current loop consisting of $L_1 \to D_1 \to C_{OUT} \to GND$ as short and wide as possible to prevent excessive ringing and false triggering of the `FB` comparator.

## Notes

- **FP6291 vs MT3608:** Both ICs are popular 6-pin boost converters for hobby electronics. The MT3608 operates at $1.2\text{ MHz}$ with a $0.6\text{ V}$ reference, while the FP6291 operates at $1.0\text{ MHz}$ and adds an explicit adjustable overcurrent limit pin (`OC`), making it particularly attractive for battery-powered power banks with strict cell current limits.
