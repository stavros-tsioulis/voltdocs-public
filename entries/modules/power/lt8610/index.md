## Overview

The **LT8610** is a benchmark monolithic synchronous step-down (buck) DC-DC regulator IC engineered by Linear Technology (now part of Analog Devices). Packaged in a compact 16-lead MSOP with an exposed thermal ground pad (MSE16), it is widely recognized across automotive, aerospace, industrial robotics, and RC telemetry designs for its remarkable combination of a wide input voltage window ($3.4\text{ V}$ to $42.0\text{ V}$), ultralow quiescent current (**$2.5\ \mu\text{A}$**), and high switching frequency capability up to **$2.2\text{ MHz}$**.

In harsh automotive and industrial 24V environments, switching regulators face two severe challenges:
1. **Electromagnetic Interference (EMI):** Automotive standards (such as CISPR 25) strictly forbid switching frequencies inside the AM broadcast band ($530\text{ kHz} - 1.8\text{ MHz}$). The LT8610 easily switches at $2.0\text{ MHz}$ or higher, keeping fundamental switching energy and harmonics completely above the sensitive radio spectrum.
2. **Fast Minimum On-Time ($50\text{ ns}$):** Stepping down from a high voltage (e.g. $16\text{ V}$ or $24\text{ V}$) directly to a low logic level ($1.8\text{ V}$ or $3.3\text{ V}$) at a high switching frequency ($2\text{ MHz}$) requires an exceptionally narrow duty cycle pulse:
   $$ t_{ON} = \frac{V_{OUT}}{V_{IN} \times f_{SW}} = \frac{3.3\text{ V}}{24\text{ V} \times 2\text{ MHz}} \approx 68.75\text{ ns} $$
   Most standard buck converters (with minimum on-times $>120\text{ ns}$) cannot achieve this and are forced to pulse-skip or reduce switching frequency. The LT8610's ultralow $50\text{ ns}$ minimum on-time permits direct single-stage conversion from 24V down to 3.3V even at 2 MHz.

Combined with integrated top ($115\text{ m}\Omega$) and bottom ($75\text{ m}\Omega$) synchronous power switches, internal compensation, and patented low-ripple Burst Mode® operation, the LT8610 delivers up to $2.5\text{ A}$ continuous output current at up to $96\%$ efficiency.

## Quick reference

| Parameter | Value | Notes |
|---|---|---|
| **Input Voltage Range ($V_{IN}$)** | $3.4\text{ V}$ to $42.0\text{ V}$ DC | Automotive load-dump transient tolerant |
| **Output Voltage Range ($V_{OUT}$)** | $0.97\text{ V}$ to $40.0\text{ V}$ DC | Set via feedback resistor divider |
| **Continuous Output Current** | $2.5\text{ A}$ | Across industrial temperature range |
| **Quiescent Current ($I_Q$)** | $2.5\ \mu\text{A}$ typical | Ultralow Burst Mode® operation |
| **Shutdown Current ($I_{SD}$)** | $1.0\ \mu\text{A}$ maximum | $V_{EN/UV} = 0\text{ V}$ |
| **Switching Frequency ($f_{SW}$)** | $200\text{ kHz}$ to $2.2\text{ MHz}$ | Resistor set or external clock sync |
| **Minimum Switch On-Time** | $50\text{ ns}$ typical | High step-down ratio at 2MHz |
| **Internal MOSFET $R_{DS(ON)}$** | $115\text{ m}\Omega$ (Top) / $75\text{ m}\Omega$ (Bottom) | Monolithic synchronous switches |
| **Feedback Reference Voltage** | $0.970\text{ V}$ ($\pm 1.0\%$) | High-accuracy reference |
| **Package** | 16-lead MSOP (MSE16) | Thermally enhanced with exposed ground pad |

## Terminals

### LT8610 MSE16 Pinout

```
           +---+--+---+
     BST --| 1   16 |-- EN/UV
      SW --| 2   15 |-- VIN
      SW --| 3   14 |-- VIN
    SYNC --| 4   13 |-- BIAS
    TR/SS -| 5   12 |-- INTVCC
     RT ---| 6   11 |-- GND
      FB --| 7   10 |-- GND
      PG --| 8    9 |-- NC
           +----------+
            EXPOSED PAD
             (GROUND)
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `BST` | Power | High-side bootstrap pin. Connect $0.1\ \mu\text{F}$ capacitor to `SW`. |
| 2, 3 | `SW` | Switch Output | Inductor switching node. Connect to external power inductor. |
| 4 | `SYNC/MODE`| Config / Clock | Mode select and external clock synchronization pin. Ground for Burst Mode; connect clock to sync. |
| 5 | `TR/SS` | Analog Input | Output soft-start ramp and tracking programming pin. Connect capacitor to `GND`. |
| 6 | `RT` | Analog Input | Oscillator frequency program pin. Connect resistor $R_T$ to `GND`. |
| 7 | `FB` | Feedback Input | Output voltage feedback sensing pin. Regulates to $0.970\text{ V}$ via external resistor divider. |
| 8 | `PG` | Digital Output | Power Good open-drain indicator flag. Pull up to logic rail. |
| 11, PAD| `GND` | Ground | Circuit ground and primary thermal heat-sinking path. |
| 12 | `INTVCC` | Power Output | Internal $3.4\text{ V}$ LDO bypass. Connect $1.0\ \mu\text{F}$ ceramic capacitor to `GND`. |
| 13 | `BIAS` | Power Input | Optional gate driver bias input ($3.2\text{V} - 25\text{V}$). Connect to $V_{OUT}$ to boost efficiency. |
| 14, 15| `VIN` | Power Input | High-voltage power supply rail ($+3.4\text{ V}$ to $+42.0\text{ V}$ DC). Bypass with ceramic cap. |
| 16 | `EN/UV` | Digital Input | Enable and precision undervoltage lockout input ($1.00\text{ V}$ threshold). |

## The technical core

### High-efficiency `BIAS` pin optimization

To minimize internal power dissipation during continuous switching, the LT8610 features a dedicated `BIAS` pin (pin 13):
- Normally, the internal gate drivers and analog circuitry are powered from $V_{IN}$ through an internal LDO regulator ($INTVCC = 3.4\text{ V}$).
- At $V_{IN} = 24\text{ V}$, powering the gate drivers from $24\text{ V}$ burns significant quiescent power:
  $$ P_{LDO} = (24\text{ V} - 3.4\text{ V}) \times I_{gate\_drive} $$
- By connecting the `BIAS` pin directly to the regulated output rail (e.g. $V_{OUT} = 3.3\text{ V}$ or $5.0\text{ V}$), internal logic and gate power is drawn directly from the efficient buck output rather than the high-voltage input rail.
- This raises overall efficiency by an additional $2\% - 4\%$ and keeps the IC noticeably cooler.

### Setting switching frequency ($R_T$)

The switching frequency is programmed by a single resistor $R_T$ from the `RT` pin to ground:

| Desired Frequency | $R_T$ Resistor Value |
|---|---|
| $200\text{ kHz}$ | $221\text{ k}\Omega$ |
| $400\text{ kHz}$ | $107\text{ k}\Omega$ |
| $700\text{ kHz}$ | $60.4\text{ k}\Omega$ |
| $1.0\text{ MHz}$ | $41.2\text{ k}\Omega$ |
| **$2.0\text{ MHz}$** | **$18.7\text{ k}\Omega$** |

### Output voltage calculation

$$ V_{OUT} = V_{FB} \times \left(1 + \frac{R_1}{R_2}\right) = 0.970\text{ V} \times \left(1 + \frac{R_1}{R_2}\right) $$

Choosing $R_2 = 100\text{ k}\Omega$ (for ultralow standby drain):
- For $3.3\text{ V}$ output: $R_1 = 100\text{ k}\Omega \times (3.3 / 0.97 - 1) \approx 240\text{ k}\Omega$ (standard 1% value $243\text{ k}\Omega$).
- For $5.0\text{ V}$ output: $R_1 = 100\text{ k}\Omega \times (5.0 / 0.97 - 1) \approx 415\text{ k}\Omega$ (standard 1% value $412\text{ k}\Omega$).

## Usage

### Typical 2MHz automotive application circuit

```
       +6V to +42V DC
  VIN o--------+-------------------------+
               |                         |
              === C_IN (4.7uF)           |
              --- 50V Ceramic            |
               |                         |
               |        +-------+        |
               |     15 |       | 1      |
               +--------|VIN BST|--------+---||---+ (100nF C_BST)
               |     16 |       | 2,3             |
EN/UV o--------+--------|EN   SW|-----------------+----CCCC----+------> VOUT (+5.0V / 2.5A)
                        |       |                      L1 (2.2uH|
                        |   BIAS|-------------------------------+
                        |       | 13                            |
                        |     FB|----+                         === C_OUT (47uF)
                        |       | 7  |                         --- Ceramic
                        |    GND|   [R1]                        |
                        +---+---+    |                          |
                            |       [R2]                        |
                            |        |                          |
  GND o---------------------+--------+--------------------------+------> 0V GND
```

## Common mistakes

- **Leaving exposed pad unsoldered:** The bottom exposed thermal pad must be soldered to a ground plane with multiple thermal vias. The small MSOP-16 package cannot dissipate heat through its pins alone at $>1.5\text{ A}$ continuous load.
- **Incorrect `BIAS` connection on high voltages:** The `BIAS` pin has a maximum rating of $25.0\text{ V}$. If $V_{OUT}$ is higher than $25\text{ V}$ (e.g. 28V), tie `BIAS` to ground rather than output.
- **High ESR input capacitors:** Ceramic capacitors are required at the $V_{IN}$ pins. Aluminum electrolytics will not absorb the nanosecond $di/dt$ transitions of 2MHz switching.

## Notes

- **LT8610 Family Variants:** The standard LT8610 is rated for $2.5\text{ A}$. The **LT8610A** variant increases continuous output current to $3.5\text{ A}$ and reduces minimum switch on-time from $50\text{ ns}$ to $30\text{ ns}$.
