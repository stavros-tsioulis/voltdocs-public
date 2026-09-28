## Overview

The **LM331** (originally National Semiconductor, now Texas Instruments) is an industry-standard precision voltage-to-frequency (V-to-F) and frequency-to-voltage (F-to-V) converter integrated circuit housed in an 8-pin DIP or SOIC package.

Operating on a temperature-compensated bandgap reference and an internal charge-balancing comparator loop, the LM331 produces an output pulse train whose frequency is directly proportional to an analog input voltage ($f_{OUT} \propto V_{IN}$). It delivers an outstanding non-linearity specification down to **$0.01\%$** (LM331A) and a wide dynamic range exceeding **$100\text{ dB}$** (from $1\text{ Hz}$ to over $100\text{ kHz}$).

The LM331 is widely employed in:
1. **Galvanically Isolated Analog Telemetry:** Transmitting an analog sensor voltage over an optocoupler or optical fiber as a digital pulse frequency, avoiding ground loops, common-mode noise, and analog signal degradation.
2. **Simple Analog-to-Digital Conversion:** Allowing any micro-controller with a simple digital counter or input-capture timer pin (such as an Arduino, PIC, or ESP32) to measure an analog voltage with 12 to 16 bits of effective resolution without an ADC chip.
3. **Frequency-to-Voltage Demodulation:** Converting tachometer signals, optical encoder pulses, or flow-meter pulse streams back into a proportional DC voltage.

## Quick reference

| Parameter | Value | Notes |
|---|---|---|
| **Primary Function** | Precision Voltage-to-Frequency (V-to-F) | Also operates as F-to-V converter |
| **Supply Voltage Range ($V_{CC}$)** | $4.0\text{ V}$ to $40.0\text{ V}$ DC | Single or split supplies ($\pm 2\text{V} \dots \pm 20\text{V}$) |
| **Full-Scale Output Frequency** | $1.0\text{ Hz}$ to $100.0\text{ kHz}$ | Set by external $R_t$, $C_t$, $R_s$, $R_L$ |
| **Non-Linearity Error** | $0.01\%$ typ ($0.03\%$ max for LM331A) | Exceptional linearity over 4 decades |
| **Dynamic Range** | $> 100\text{ dB}$ | At $10\text{ kHz}$ full scale |
| **Temperature Coefficient** | $50\text{ ppm/}^\circ\text{C}$ typical | Internal bandgap reference |
| **Output Type** | Open-collector NPN transistor | Compatible with TTL, CMOS, and optocouplers |
| **Current Consumption** | $1.2\text{ mA}$ to $2.0\text{ mA}$ | Low quiescent operating current |
| **Package** | 8-pin DIP (PDIP-8) / SOIC-8 | Breadboard and prototyping standard |

## Terminals

```
            +---+--+---+
     I_OUT -| 1    8 |-- VCC
     I_REF -| 2    7 |-- COMP_IN
     F_OUT -| 3    6 |-- THRESHOLD
       GND -| 4    5 |-- R_C
            +----------+
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `I_OUT` | Current Output | Switched current source output. Delivers precision current pulses into the integrator node. |
| 2 | `I_REF` | Reference Current | Reference current set pin. An external resistor $R_S$ to ground sets reference current ($I_{REF} = 1.90\text{ V} / R_S$). |
| 3 | `F_OUT` | Digital Output | Pulse frequency output. Open-collector NPN transistor (sinks up to $10\text{ mA}$). Pull up to logic supply. |
| 4 | `GND` | Ground | Circuit ground reference ($0\text{ V}$). |
| 5 | `R_C` | Timing Node | One-shot RC timing node. Connect external timing resistor $R_t$ and capacitor $C_t$. |
| 6 | `THRESHOLD`| Analog Input | Internal comparator threshold / reset input. Connected to $R_t/C_t$ network. |
| 7 | `COMP_IN` | Analog Input | Voltage comparator input. Connects to the analog input signal $V_{IN}$. |
| 8 | `VCC` | Power | Positive supply rail ($+4.0\text{ V}$ to $+40.0\text{ V}$ DC). |

## The technical core

### Conversion transfer function

The LM331 employs a charge-balancing conversion architecture. The relationship between input voltage ($V_{IN}$) and output frequency ($f_{OUT}$) is determined exclusively by external passive components:

$$ f_{OUT} = \frac{V_{IN}}{2.09\text{ V}} \times \frac{R_S}{R_L} \times \frac{1}{R_t \times C_t} $$

Where:
- $V_{IN}$ is the input voltage applied to pin 7.
- $R_S$ is the gain-adjustment resistor from pin 2 to ground.
- $R_L$ is the input scaling resistor from pin 1 to ground.
- $R_t$ is the timing resistor from $V_{CC}$ to pin 5.
- $C_t$ is the timing capacitor from pin 5 to ground.

When $R_S$ is calibrated such that $R_S / R_L = 2.09$:

$$ f_{OUT} = \frac{V_{IN}}{R_t \times C_t} $$

**Design Example ($0\text{ V} \dots 10.0\text{ V} \implies 0\text{ Hz} \dots 10.0\text{ kHz}$):**
- Choose timing components: $R_t = 6.8\text{ k}\Omega$, $C_t = 0.01\ \mu\text{F}$ ($10\text{ nF}$ low-drift film or C0G/NP0 ceramic).
- Input resistor: $R_L = 100\text{ k}\Omega$ 1%.
- Reference setting: $R_S \approx 12\text{ k}\Omega$ (use a $10\text{ k}\Omega$ precision metal-film resistor in series with a $5\text{ k}\Omega$ multi-turn trimpot for full-scale calibration).

### Electrical specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 4.0 | 15.0 | 40.0 | V | Operating range |
| Internal Reference Voltage | $V_{REF}$ | 1.77 | 1.89 | 2.01 | V | Pin 2 reference |
| Non-Linearity Error | $NL$ | — | 0.01 | 0.03 | % | $f = 10\text{ Hz} \dots 10\text{ kHz}$, LM331A |
| Max Operating Frequency | $f_{MAX}$ | 100 | 150 | — | kHz | $V_{CC} = 15\text{ V}$ |
| Output Saturation Voltage | $V_{OL}$ | — | 0.25 | 0.5 | V | $I_{SINK} = 5.0\text{ mA}$ |
| Output Leakage Current | $I_{OH}$ | — | 0.01 | 1.0 | µA | $V_{PULLUP} = 15\text{ V}$ |
| Supply Current | $I_{CC}$ | — | 1.2 | 2.5 | mA | $V_{CC} = 15\text{ V}$ |

## Usage

### Basic 0 to 10V to 0 to 10kHz converter circuit

```
       +15V DC
  VCC o------+--------------------------+-----------------------+
             |                          |                       |
            [ ] R_t (6.8k)             [ ] R_pullup (10k)      [ ] R_IN (100k)
             |                          |                       |
             +-------------+ (Pin 8)    |                       |
             |             |            |                       |
             +-------------+ (Pin 5)    |                       |
             |             |            |                       |
             |          +--+---+        |                       |
             |          | VCC  |        |                       |
             |          |      | 3      |                       |
             |          | F_OUT|--------+----> Pulse Frequency  |
             |          |      |              Output to MCU     |
             |          |COMPIN|--------------------------------+---o VIN (0 to 10V)
             |          |      | 7
             |          | THRES|----------------+
             |          |      | 6              |
             |          |  R_C |----------------+ (Pins 5 & 6 shorted)
             |          |      | 5
             |          |I_OUT |----+
             |          |      | 1  |
             |          |I_REF |    |
             |          |  GND |    |
             |          +--+---+    |
            ===            | 4     [ ] R_L (100k)
      C_t   --- (10nF)     |        |
             |             |       === C_L (1uF)
             |             |        |
  GND o------+-------------+--------+---[ R_S (12k trim) ]----o GND
```

## Common mistakes

- **Omitting the output pull-up resistor:** Pin 3 (`F_OUT`) is an open-collector output with no internal pull-up. Without an external resistor to the target microcontroller logic rail ($3.3\text{ V}$ or $5\text{ V}$), the output will stay permanently low.
- **Using poor-dielectric timing capacitors:** Using high-dielectric-constant ceramic capacitors (such as Y5V or Z5U) for $C_t$ causes severe thermal drift and non-linearity. Always use **polypropylene film, polystyrene, or C0G/NP0 ceramic** capacitors for $C_t$.
- **Ground loops in analog-to-digital telemetry:** Connect the analog ground reference directly to the input sensor return, keeping high-frequency pulse return currents separated until the star ground point.

## Notes

- **Voltage-to-Frequency vs ADC:** While modern microcontrollers include built-in ADCs, the LM331 excels where analog signals must traverse high-voltage galvanic barriers (using cheap optocouplers) or where electrical noise along long industrial wire cables corrupts analog voltages.
