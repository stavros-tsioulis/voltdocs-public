## Overview

The **LM3671MF-3.3** (National Semiconductor / Texas Instruments) is a miniature, high-efficiency synchronous step-down (buck) DC-DC converter IC packaged in a 5-lead SOT-23 (DBV). Engineered specifically for single-cell Lithium-Ion / Lithium-Polymer battery systems ($2.7\text{ V}$ to $5.5\text{ V}$ input) and USB-powered mobile electronics, it delivers a factory-trimmed fixed **$+3.3\text{ V}$** DC output at up to **$600\text{ mA}$** continuous load current.

In battery-operated embedded systems (such as ESP32, Nordic nRF52, and STM32 IoT nodes), standard linear regulators (such as the AMS1117-3.3) are severely limited:
- When a fully charged single-cell LiPo battery ($4.2\text{ V}$) powers a $3.3\text{ V}$ system, a linear regulator burns $0.9\text{ V} \times I_{LOAD}$ directly into heat, capping battery conversion efficiency at under $78\%$.
- Furthermore, as the battery discharges below $3.6\text{ V}$, common linear regulators with high dropout voltages ($>1.0\text{ V}$) drop out of regulation prematurely, wasting up to 40% of the battery's usable energy capacity.

The LM3671 solves both problems: it maintains **up to 95% efficiency** across active operating loads and provides ultra-low dropout pass-through behavior. By switching at an ultra-high frequency of **$2.0\text{ MHz}$**, it utilizes tiny $2.2\ \mu\text{H}$ surface-mount inductors (such as 0805 or 0603 footprints) and small $4.7\ \mu\text{F} - 10\ \mu\text{F}$ ceramic capacitors. An automatic mode-switching architecture transitions between high-efficiency Pulse-Width Modulation (PWM) under moderate-to-heavy loads and low-quiescent Pulse Frequency Modulation (PFM) under light standby loads, drawing only **$16\ \mu\text{A}$** quiescent current.

## Quick reference

| Parameter | Value | Notes |
|---|---|---|
| **Converter Architecture** | Synchronous Step-Down (Buck) | Integrated high-side and low-side FETs |
| **Input Supply Voltage ($V_{IN}$)** | $2.7\text{ V}$ to $5.5\text{ V}$ DC | Single-cell LiPo/Li-Ion or USB 5V rail |
| **Fixed Output Voltage ($V_{OUT}$)** | $+3.3\text{ V}$ DC ($\pm 3\%$) | Internally trimmed; no external resistors |
| **Maximum Output Current** | $600\text{ mA}$ continuous | Suitable for ESP32/nRF52/Wi-Fi bursts |
| **Switching Frequency ($f_{SW}$)** | $2.0\text{ MHz}$ typical | Allows 0805/0603 size inductors |
| **Quiescent Current ($I_Q$)** | $16\ \mu\text{A}$ typical | In light-load PFM standby mode |
| **Shutdown Current ($I_{SD}$)** | $0.04\ \mu\text{A}$ typical | When `EN` pin is grounded |
| **Peak Efficiency** | Up to $95\%$ | At $150\text{ mA} - 300\text{ mA}$ load |
| **Package** | 5-lead SOT-23 (DBV) | Standard surface-mount package |

## Terminals

The LM3671 in the 5-pin SOT-23 package has the following terminal layout:

```
          +---+--+---+
    VIN --| 1    5 |-- SW
    GND --| 2      |
     EN --| 3    4 |-- FB
          +----------+
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VIN` | Power Input | Input voltage rail ($+2.7\text{ V}$ to $+5.5\text{ V}$ DC). Decouple with a $4.7\ \mu\text{F}$ ceramic capacitor. |
| 2 | `GND` | Ground | Common circuit ground reference ($0\text{ V}$). |
| 3 | `EN` | Digital Input | Enable control input (active-high). Pull High ($>1.0\text{ V}$) to enable, Low ($<0.4\text{ V}$) to shut down. Do not float. |
| 4 | `FB` | Feedback Sense | Feedback sense line. For the fixed 3.3V variant, connect directly to the $+3.3\text{ V}$ output capacitor. |
| 5 | `SW` | Switching Node | Inductor switching pin. Connect to the external power inductor. |

## The technical core

### Automatic PFM / PWM mode transitions

The LM3671 continuously monitors load current to optimize conversion efficiency over a wide dynamic load range:
- **PWM Mode (High Loads > 120 mA):** The device operates in fixed-frequency synchronous PWM mode at $2.0\text{ MHz}$. Both internal low-resistance switches actively commutate, producing low output voltage ripple ($< 10\text{ mV}_{p-p}$) ideal for sensitive RF transceivers.
- **PFM Mode (Light Loads < 70 mA):** When load current drops below the PFM threshold, the converter seamlessly switches to hysteretic Pulse Frequency Modulation. Switching pulses occur only when the output voltage dips below regulation threshold, reducing internal switching losses and slashing quiescent current to just $16\ \mu\text{A}$.
- **100% Duty Cycle Mode (Low Dropout):** When the battery voltage drops close to $3.3\text{ V}$, the high-side P-channel MOSFET turns on continuously ($100\%$ duty cycle). In this state, output voltage follows input voltage minus the small $I \times R_{DS(ON)}$ drop ($\approx 120\text{ mV}$ at $400\text{ mA}$), squeezing every last drop of usable run-time out of the battery.

### Electrical specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Voltage Range | $V_{IN}$ | 2.7 | 3.7 / 5.0 | 5.5 | V | Operating range |
| Output Voltage (Fixed 3.3V) | $V_{OUT}$ | 3.201 | 3.300 | 3.399 | V | $V_{IN} = 3.6\text{ V}$, $I_O = 100\text{ mA}$ |
| High-Side FET Resistance | $R_{DS(ON)\_P}$ | — | 350 | 500 | $\text{m}\Omega$ | $V_{IN} = 3.6\text{ V}$ |
| Low-Side FET Resistance | $R_{DS(ON)\_N}$ | — | 250 | 400 | $\text{m}\Omega$ | $V_{IN} = 3.6\text{ V}$ |
| Switching Frequency | $f_{SW}$ | 1.6 | 2.0 | 2.4 | MHz | PWM mode |
| Quiescent Current (PFM) | $I_Q$ | — | 16 | 30 | µA | No-load standby |
| Shutdown Current | $I_{SD}$ | — | 0.04 | 1.0 | µA | $V_{EN} = 0\text{ V}$ |
| Peak Switch Current Limit | $I_{CL}$ | 750 | 950 | 1150 | mA | Cycle-by-cycle limit |
| Thermal Shutdown Temp | $T_{TSD}$ | — | 150 | — | °C | Auto-recovering |

## Usage

### Typical application circuit

```
       +2.7V to +5.5V DC
       (e.g. 1S LiPo / USB)
  VIN o--------+------------------------+
               |                        |
              === C_IN (4.7uF - 10uF)   |
              --- 10V Ceramic           |
               |                        |
               |        +-------+       |
               |      1 |       | 5     |
               +--------|VIN  SW|-------+----CCCC----+------> +3.3V DC Regulated
               |      3 |       |          L1 (2.2uH)|        (Up to 600mA)
   EN o--------+--------|EN     |                    |
                        |     FB|--------------------+
                        |       | 4                  |
                        |    GND|                   === C_OUT (10uF)
                        +---+---+                   --- 10V Ceramic
                            |                        |
  GND o---------------------+------------------------+------> 0V GND
```

#### Component recommendations:
- **Inductor ($L_1$):** $2.2\ \mu\text{H}$ power inductor rated for $I_{SAT} \ge 1.0\text{ A}$ with low DC resistance ($R_{DC} < 0.2\ \Omega$) such as Murata LQM21PN2R2MC0 or Coilcraft LPS3015-222ML.
- **Input Capacitor ($C_{IN}$):** $4.7\ \mu\text{F}$ or $10\ \mu\text{F}$ 10V X5R/X7R ceramic capacitor placed directly across pins 1 and 2.
- **Output Capacitor ($C_{OUT}$):** $10\ \mu\text{F}$ 6.3V or 10V X5R/X7R ceramic capacitor placed immediately between the inductor output and ground.

## Common mistakes

- **Leaving `EN` floating:** The `EN` pin has high input impedance. Leaving it unconnected allows stray electro-static noise to intermittently disable the regulator. Tie `EN` directly to `VIN` if hardware control is unneeded.
- **Using general-purpose electrolytic capacitors:** Electrolytic and tantalum capacitors have far too high ESR at $2.0\text{ MHz}$, resulting in massive output ripple and control loop instability. Use exclusively X5R or X7R multi-layer ceramic capacitors (MLCC).
- **Connecting feedback through a long, noisy trace:** The `FB` trace must connect cleanly at the output capacitor terminals and run away from the noisy, high $di/dt$ `SW` switching node.
- **Exceeding 5.5V input:** The LM3671 is a low-voltage CMOS IC ($5.5\text{ V}$ operating, $6.0\text{ V}$ absolute max). Connecting it directly to a $9\text{ V}$ battery or $12\text{ V}$ automotive rail will instantly destroy the device.

## Notes

- **Linear vs. Switching on Battery Power:** For deep-sleep nodes that spend $99\%$ of their time sleeping at $< 5\ \mu\text{A}$ (e.g. weather sensors waking once per hour), a specialized ultra-low-quiescent LDO (such as the MCP1700 with $1.6\ \mu\text{A}$ $I_Q$) may achieve comparable battery longevity. However, for devices with high active duty cycles (e.g., continuous BLE advertising or Wi-Fi data streaming), the LM3671 will typically double or triple the battery run-time.
