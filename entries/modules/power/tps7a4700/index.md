## Overview

The **TPS7A4700** (part number `TPS7A4700RGWT`) is a state-of-the-art positive low-dropout (LDO) linear voltage regulator manufactured by Texas Instruments, housed in a $5\times 5\text{ mm}$ 20-pin VQFN package (RGW) with an exposed thermal pad. It is recognized as an industry benchmark in high-end audiophile electronics, software-defined radio (SDR), VCO/PLL clock generation, and precision 24-bit/32-bit instrumentation.

The defining characteristic of the TPS7A4700 is its ultra-low output voltage noise of just **$4.17\ \mu\text{V}_{RMS}$** across the audio band ($10\text{ Hz}$ to $100\text{ kHz}$) and exceptional power supply ripple rejection (**$82\text{ dB}$ at 100 Hz**, $>55\text{ dB}$ up to 100 kHz). This enables the regulator to clean up high-frequency ripple from upstream switching converters with near-battery purity.

Unlike conventional adjustable regulators (such as the LM317 or LT1963) that require external feedback resistor dividers (which introduce thermal drift and act as antennas for RF noise), the TPS7A4700 features TI's innovative **ANY-OUT™** pin-programmable architecture. A set of binary-weighted internal precision resistors allows the user to program any output voltage from **$1.4\text{ V}$ to $20.5\text{ V}$** in $50\text{ mV}$ increments simply by grounding the appropriate pins or jumper pads on the PCB.

## Quick reference

| Parameter | Value | Notes |
|---|---|---|
| **Regulator Architecture** | Bipolar Pass LDO with ANY-OUT™ | Resistor-free pin-programmable |
| **Output Voltage Range ($V_{OUT}$)** | $1.4\text{ V}$ to $20.5\text{ V}$ DC | $50\text{ mV}$ discrete resolution steps |
| **Input Supply Voltage ($V_{IN}$)** | $3.0\text{ V}$ to $36.0\text{ V}$ DC | Absolute maximum $38.0\text{ V}$ |
| **Output Current ($I_{OUT}$)** | Up to $1.0\text{ A}$ continuous | Thermally limited by PCB pad |
| **Output Noise Voltage** | $4.17\ \mu\text{V}_{RMS}$ ($10\text{ Hz} \dots 100\text{ kHz}$) | Clean enough for ultra-low-jitter clocks |
| **Power Supply Rejection (PSRR)** | $82\text{ dB}$ (100 Hz) / $55\text{ dB}$ (100 kHz) | High attenuation of switcher ripple |
| **Dropout Voltage ($V_{DO}$)** | $307\text{ mV}$ typical at $1.0\text{ A}$ | Low headroom operation |
| **Enable Control (`EN`)** | CMOS logic compatible | Active-high enable, $1.1\ \mu\text{A}$ shutdown |
| **Package** | 20-pin VQFN ($5\times 5\text{ mm}$, RGW) | Standard high-density audio/RF module |

## Terminals

The 20-pin VQFN (RGW) package layout and common breakout module pin definitions:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1, 2 | `OUT` | Power Output | Regulated low-noise DC output. Connect $10\ \mu\text{F} - 47\ \mu\text{F}$ ceramic capacitor to ground. |
| 3 | `FB` / `NC` | Sense | Internal feedback node. Leave open or connect per datasheet. |
| 4 | `50mV` | ANY-OUT Pin | Grounding this pin adds $+50\text{ mV}$ to the baseline $1.4\text{ V}$ output. |
| 5 | `100mV` | ANY-OUT Pin | Grounding this pin adds $+100\text{ mV}$. |
| 6 | `200mV` | ANY-OUT Pin | Grounding this pin adds $+200\text{ mV}$. |
| 7 | `400mV` | ANY-OUT Pin | Grounding this pin adds $+400\text{ mV}$. |
| 8 | `800mV` | ANY-OUT Pin | Grounding this pin adds $+800\text{ mV}$. |
| 9 | `1.6V` | ANY-OUT Pin | Grounding this pin adds $+1.6\text{ V}$. |
| 10 | `3.2V` | ANY-OUT Pin | Grounding this pin adds $+3.2\text{ V}$. |
| 11 | `6.4V` | ANY-OUT Pin | Grounding this pin adds $+6.4\text{ V}$ (pin 1). |
| 12 | `6.4V` | ANY-OUT Pin | Grounding this pin adds $+6.4\text{ V}$ (pin 2). |
| 13, 14| `GND` | Ground | Circuit ground reference ($0\text{ V}$). |
| 15, 16| `NC` | — | No internal connection. Leave floating. |
| 17 | `EN` | Digital Input | Regulator enable. High = active, Low = shutdown. |
| 18, 19| `IN` | Power Input | Unregulated DC input ($+3.0\text{ V}$ to $+36.0\text{ V}$ DC). Bypass with ceramic cap. |
| 20 | `NR` | Filter Pin | Noise-reduction pin. Connect $1.0\ \mu\text{F}$ capacitor to `GND`. |
| PAD | `PAD` | Thermal Ground | Exposed bottom pad. Must be soldered to ground plane. |

## The technical core

### ANY-OUT™ output voltage programming

The baseline output voltage with all ANY-OUT pins left floating is **$1.4\text{ V}$**. Each ANY-OUT pin connected to **Ground (`GND`)** activates an internal binary-weighted laser-trimmed resistor that adds a precise increment:

$$ V_{OUT} = 1.4\text{ V} + \sum V_{ANY-OUT\_GND} $$

| Desired $V_{OUT}$ | Pins Connected to `GND` | Calculation |
|---|---|---|
| **$1.8\text{ V}$** | `400mV` | $1.4\text{ V} + 0.4\text{ V} = 1.8\text{ V}$ |
| **$2.5\text{ V}$** | `800mV`, `200mV`, `100mV` | $1.4\text{ V} + 0.8\text{ V} + 0.2\text{ V} + 0.1\text{ V} = 2.5\text{ V}$ |
| **$3.3\text{ V}$** | `1.6V`, `200mV`, `100mV` | $1.4\text{ V} + 1.6\text{ V} + 0.2\text{ V} + 0.1\text{ V} = 3.3\text{ V}$ |
| **$5.0\text{ V}$** | `3.2V`, `400mV` | $1.4\text{ V} + 3.2\text{ V} + 0.4\text{ V} = 5.0\text{ V}$ |
| **$9.0\text{ V}$** | `6.4V`, `800mV`, `400mV` | $1.4\text{ V} + 6.4\text{ V} + 0.8\text{ V} + 0.4\text{ V} = 9.0\text{ V}$ |
| **$12.0\text{ V}$** | `6.4V`, `3.2V`, `800mV`, `200mV` | $1.4\text{ V} + 6.4\text{ V} + 3.2\text{ V} + 0.8\text{ V} + 0.2\text{ V} = 12.0\text{ V}$ |
| **$15.0\text{ V}$** | `6.4V` (x2), `800mV` | $1.4\text{ V} + 6.4\text{ V} + 6.4\text{ V} + 0.8\text{ V} = 15.0\text{ V}$ |

Because these resistors are internal and shielded, this eliminates external resistor parasitic inductance, resistance tolerance drift, and RF electromagnetic pickup.

### Electrical specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Voltage Range | $V_{IN}$ | 3.0 | — | 36.0 | V | Operating range |
| Baseline Output Voltage | $V_{OUT\_BASE}$| 1.372 | 1.400 | 1.428 | V | All ANY-OUT open |
| Max Programmable Output | $V_{OUT\_MAX}$ | — | 20.5 | — | V | All ANY-OUT grounded |
| Maximum Output Current | $I_{OUT}$ | 1.0 | — | — | A | Limited by thermals |
| Dropout Voltage | $V_{DO}$ | — | 307 | 450 | mV | $I_{OUT} = 1.0\text{ A}$, $V_{OUT} = 5.0\text{ V}$ |
| Output Noise Spectral Density | $e_n$ | — | 4.17 | — | $\mu\text{V}_{RMS}$ | $10\text{ Hz} \dots 100\text{ kHz}$, $C_{NR} = 1\ \mu\text{F}$ |
| Ripple Rejection (PSRR) | $PSRR$ | 75 | 82 | — | dB | $f = 100\text{ Hz}$, $I_{OUT} = 1.0\text{ A}$ |
| Ripple Rejection (PSRR) | $PSRR$ | 50 | 55 | — | dB | $f = 100\text{ kHz}$, $I_{OUT} = 1.0\text{ A}$ |
| Quiescent Ground Current | $I_{GND}$ | — | 16 | 21 | mA | $I_{OUT} = 1.0\text{ A}$ |
| Shutdown Current | $I_{SHDN}$ | — | 1.1 | 3.0 | µA | $V_{EN} \le 0.4\text{ V}$ |

## Usage

### Ultra-clean audio DAC power supply circuit

```
       +6V to +12V DC
  VIN o--------+-------------------------+
               |                         |
              === C_IN (10uF)            |
              --- 50V Ceramic            |
               |                         |
               |        +-------+        |
               |     18 |       | 1,2    |
               +--------|IN  OUT|--------+------------------------------+------> +5.0V Low-Noise DC
               |     17 |       |                                       |        (To Audio DAC / Op-Amp)
   EN o--------+--------|EN     |                                      === C_OUT (22uF)
                        |       |                                      --- Low-ESR Ceramic
                        |     NR|--------||----+ (1.0uF C_NR)           |
                        |       | 20           |                        |
                        |   3.2V|--------------+ (Ground for 5.0V)      |
                        |  400mV|--------------+ (Ground for 5.0V)      |
                        |    GND|              |                        |
                        +---+---+              |                        |
                            |                  |                        |
  GND o---------------------+------------------+------------------------+------> 0V GND
```

#### Key layout & component guidelines:
1. **Noise-Reduction Capacitor ($C_{NR}$):** A $1.0\ \mu\text{F}$ ceramic capacitor from pin 20 (`NR`) to `GND` filters the internal bandgap reference. Do not omit this capacitor; without it, noise increases by a factor of four.
2. **Output Capacitor ($C_{OUT}$):** Minimum $10\ \mu\text{F}$ (recommended $22\ \mu\text{F}$ to $47\ \mu\text{F}$) low-ESR ceramic capacitor placed directly at the `OUT` pins.
3. **Thermal Pad:** Solder the exposed center pad to an expansive ground copper plane with multiple thermal vias to dissipate heat at high currents.

## Common mistakes

- **Leaving the noise-reduction capacitor ($C_{NR}$) unpopulated:** The extreme low-noise specification ($4.17\ \mu\text{V}_{RMS}$) is only achieved when a $1.0\ \mu\text{F}$ X7R ceramic capacitor is connected to pin 20.
- **Connecting ANY-OUT pins to $V_{OUT}$ instead of `GND`:** ANY-OUT pins must be connected to **Ground** to add their voltage contribution. Tying them to $V_{OUT}$ will not engage the internal pull-down dividers.
- **Underestimating linear power dissipation:** As a linear regulator, $P_D = (V_{IN} - V_{OUT}) \times I_{OUT}$. Stepping $12\text{ V}$ down to $5\text{ V}$ at $1\text{ A}$ produces $(12 - 5) \times 1 = 7\text{ W}$ of heat, which will trigger thermal shutdown without a dedicated heatsink. Pre-regulate with a switching buck converter down to $6.0\text{ V}$ ($1.0\text{ V}$ headroom) to achieve cool, ultra-clean power.

## Notes

- **TPS7A4700 vs TPS7A4701:** The TPS7A4700 uses dedicated ANY-OUT pins exclusively. The companion **TPS7A4701** allows both ANY-OUT pin configuration and external feedback resistors for non-standard intermediate voltages.
