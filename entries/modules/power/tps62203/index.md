## Overview

The **TPS62203DBVT** (part of the Texas Instruments TPS6220x family) is a miniature, high-efficiency synchronous step-down (buck) DC-DC converter IC supplied in a 5-lead SOT-23 package (TI designation DBV, with `-T` indicating tape-and-reel packaging). Specifically designed for single-cell Li-Ion/LiPo battery-powered wearables, smart sensors, and miniature IoT gadgets, the TPS62203 provides a factory-trimmed fixed **$+3.3\text{ V}$** DC output at up to **$300\text{ mA}$** continuous load current.

While standard linear regulators dissipate power proportionally to voltage drop ($P_D = (V_{IN} - V_{OUT}) \times I$), the TPS62203 delivers **up to 95% electrical efficiency**, vastly extending battery lifespan. At light loads, the converter automatically enters a power-save (PFM) mode that cuts device quiescent current down to just **$15\ \mu\text{A}$**.

Additionally, the TPS62203 incorporates a **100% duty cycle mode** (low-dropout pass-through): as a single-cell lithium battery discharges towards $3.3\text{ V}$, the internal high-side P-channel MOSFET turns on continuously, allowing the output voltage to track the battery voltage with only a minimal voltage drop ($I \times R_{DS(ON)}$). This extracts maximum energy capacity from the cell before system cutoff.

## Quick reference

| Parameter | Value | Notes |
|---|---|---|
| **Converter Architecture** | Synchronous Step-Down (Buck) | Integrated high-side and low-side switches |
| **Input Supply Voltage ($V_{IN}$)** | $2.5\text{ V}$ to $6.0\text{ V}$ DC | Suitable for 1S Li-ion or 3x NiMH cells |
| **Fixed Output Voltage ($V_{OUT}$)** | $+3.3\text{ V}$ DC ($\pm 3\%$) | Internally trimmed; no external resistors |
| **Maximum Output Current** | $300\text{ mA}$ continuous | Optimized for microcontrollers and sensors |
| **Switching Frequency ($f_{SW}$)** | $1.0\text{ MHz}$ typical | Fixed-frequency PWM at medium-to-high loads |
| **Quiescent Current ($I_Q$)** | $15\ \mu\text{A}$ typical | Light-load power-save mode |
| **Shutdown Current ($I_{SD}$)** | $0.1\ \mu\text{A}$ typical | When `EN` pin is tied Low |
| **Internal MOSFET $R_{DS(ON)}$** | $470\text{ m}\Omega$ (P-FET) / $350\text{ m}\Omega$ (N-FET) | Typical at $V_{IN} = 3.6\text{ V}$ |
| **Package** | 5-lead SOT-23 (DBV) | Miniature $2.9\times 1.6\text{ mm}$ footprint |

## Terminals

The TPS62203 uses the standard 5-pin SOT-23 configuration:

```
          +---+--+---+
     VI --| 1    5 |-- SW
    GND --| 2      |
     EN --| 3    4 |-- FB
          +----------+
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VI` | Power Input | Input power supply pin ($+2.5\text{ V}$ to $+6.0\text{ V}$ DC). Bypass with ceramic capacitor. |
| 2 | `GND` | Ground | Circuit ground reference ($0\text{ V}$). |
| 3 | `EN` | Digital Input | Enable control input (active-high). Drive High to enable, Low to shut down. Do not float. |
| 4 | `FB` | Feedback Sense | Output feedback sensing pin. Connect directly to the $+3.3\text{ V}$ output capacitor. |
| 5 | `SW` | Switching Node | Inductor switching terminal. Connect to external power inductor. |

## The technical core

### Automatic power save mode & 100% duty cycle

1. **Power Save (PFM) Mode:**
   - Under light load conditions ($< 50\text{ mA}$), the converter automatically transitions from continuous 1 MHz PWM to pulsed PFM mode.
   - The device skips switching cycles and draws only $15\ \mu\text{A}$ quiescent current from the battery, maintaining $>85\%$ efficiency even down to $1\text{ mA}$ standby loads.
2. **100% Duty Cycle Mode (Low-Dropout Operation):**
   - As the battery cell voltage depletes and approaches $3.3\text{ V}$, the switching duty cycle increases to $100\%$.
   - In $100\%$ duty cycle mode, the internal P-channel MOSFET switch stays continuously on.
   - The dropout voltage across the regulator is purely resistive:
     $$ V_{dropout} = I_{OUT} \times (R_{DS(ON)\_P} + R_{L\_DCR}) \approx 300\text{ mA} \times (0.47\ \Omega + 0.15\ \Omega) \approx 186\text{ mV} $$
   - This ensures the device continues to power $3.3\text{ V}$ microcontrollers safely down to $V_{IN} \approx 3.48\text{ V}$ at full load and down to $3.32\text{ V}$ at low load.

### Electrical specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Voltage Range | $V_I$ | 2.5 | 3.6 / 5.0 | 6.0 | V | Operating range |
| Output Voltage (Fixed 3.3V) | $V_O$ | 3.20 | 3.30 | 3.40 | V | $V_I = 2.5 \dots 6.0\text{ V}$, $I_O = 0 \dots 300\text{ mA}$ |
| High-Side Switch Resistance | $R_{DS(ON)\_P}$ | — | 470 | 670 | $\text{m}\Omega$ | $V_I = 3.6\text{ V}$ |
| Low-Side Switch Resistance | $R_{DS(ON)\_N}$ | — | 350 | 500 | $\text{m}\Omega$ | $V_I = 3.6\text{ V}$ |
| Switching Frequency | $f_{SW}$ | 0.8 | 1.0 | 1.2 | MHz | PWM mode, $I_O = 200\text{ mA}$ |
| Quiescent Current | $I_Q$ | — | 15 | 25 | µA | Power save mode, $I_O = 0$ |
| Shutdown Current | $I_{SD}$ | — | 0.1 | 1.0 | µA | $V_{EN} = 0\text{ V}$ |
| Switch Peak Current Limit | $I_{LIM}$ | 450 | 590 | 730 | mA | High-side current limit |
| Thermal Shutdown | $T_{TSD}$ | — | 160 | — | °C | Auto-recovering |

## Usage

### Minimal application circuit

```
       +2.5V to +6.0V DC
       (e.g. 1S LiPo / 3.7V)
   VI o--------+------------------------+
               |                        |
              === C_IN (4.7uF - 10uF)   |
              --- 10V Ceramic           |
               |                        |
               |        +-------+       |
               |      1 |       | 5     |
               +--------|VI   SW|-------+----CCCC----+------> +3.3V DC Regulated
               |      3 |       |          L1 (10uH) |        (Up to 300mA)
   EN o--------+--------|EN     |                    |
                        |     FB|--------------------+
                        |       | 4                  |
                        |    GND|                   === C_OUT (10uF)
                        +---+---+                   --- 10V Ceramic
                            |                        |
  GND o---------------------+------------------------+------> 0V GND
```

#### External components:
- **Power Inductor ($L_1$):** $4.7\ \mu\text{H}$ to $10\ \mu\text{H}$ shielded power inductor with $I_{SAT} \ge 600\text{ mA}$ (e.g. Murata LQH32CN100K53 or Coilcraft DO3314-103ML).
- **Input Capacitor ($C_{IN}$):** $4.7\ \mu\text{F}$ or $10\ \mu\text{F}$ 10V X5R/X7R ceramic capacitor directly across pins 1 and 2.
- **Output Capacitor ($C_{OUT}$):** $10\ \mu\text{F}$ 6.3V or 10V X5R/X7R ceramic capacitor directly across the output node and ground.

## Common mistakes

- **Leaving `EN` pin floating:** The `EN` pin has high impedance and will float into indeterminate states, causing random power shutdowns. Tie `EN` directly to `VI` if software power control is not needed.
- **Using high-ESR tantalum or electrolytic capacitors:** The control loop relies on low output ESR. Using electrolytic capacitors causes elevated ripple and loop instability. Always use multi-layer ceramic capacitors (MLCC).
- **Connecting feedback through noisy routing:** Route the `FB` pin connection as a dedicated trace to the output capacitor pad, shielding it from the high-frequency switching `SW` pad.

## Notes

- **TPS62203 vs LM3671:** The TPS62203 operates at $1.0\text{ MHz}$ and delivers up to $300\text{ mA}$ with a $15\ \mu\text{A}$ quiescent current. The LM3671 operates at $2.0\text{ MHz}$ and delivers up to $600\text{ mA}$. Both share identical 5-pin SOT-23 pinouts and serve as top-tier replacements for linear regulators in wearable battery electronics.
