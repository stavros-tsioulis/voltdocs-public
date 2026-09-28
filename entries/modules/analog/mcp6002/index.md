## Overview

The **MCP6002** is a general-purpose, low-power dual operational amplifier manufactured by Microchip Technology. Engineered specifically for battery-powered, portable, and microcontroller-based embedded systems, the MCP6002 features true **Rail-to-Rail Input and Output (RRIO)** across a wide supply range of **$1.8\text{ V}$ to $6.0\text{ V}$**.

With a modest quiescent current of just **$100\text{ }\mu\text{A}$ per amplifier**, a $1.0\text{ MHz}$ Gain Bandwidth Product (GBW), an ultra-low input bias current of $1.0\text{ pA}$, and a robust $90^\circ$ phase margin capable of directly driving up to $500\text{ pF}$ capacitive loads, the MCP6002 is the definitive modern, low-voltage replacement for aging bipolar op-amps like the LM358 in $3.3\text{ V}$ and $5\text{ V}$ single-supply Arduino, ESP32, and Raspberry Pi sensor conditioning designs.

## Quick reference

| | |
|---|---|
| **Function** | 1MHz Low-Power Rail-to-Rail Input/Output Dual Op-Amp |
| **Supply Voltage Range ($V_{DD} - V_{SS}$)** | $1.8\text{ V}$ to $6.0\text{ V}$ DC (single supply) |
| **Input Common-Mode Range** | Rail-to-Rail ($V_{SS} - 0.3\text{ V}$ to $V_{DD} + 0.3\text{ V}$) |
| **Output Swing** | Rail-to-Rail ($V_{SS} + 25\text{ mV}$ to $V_{DD} - 25\text{ mV}$ with $10\text{ k}\Omega$ load) |
| **Quiescent Current** | $100\text{ }\mu\text{A}$ per channel typ ($170\text{ }\mu\text{A}$ max) |
| **Gain Bandwidth Product (GBW)** | $1.0\text{ MHz}$ typ |
| **Slew Rate (SR)** | $0.6\text{ V/}\mu\text{s}$ typ |
| **Input Bias Current ($I_B$)** | $1.0\text{ pA}$ typ at $25^\circ\text{C}$ ($1.0\text{ nA}$ max over temp) |
| **Input Offset Voltage ($V_{OS}$)** | $\pm 4.5\text{ mV}$ max |
| **Phase Margin** | $90^\circ$ ($C_L$ stable up to $500\text{ pF}$) |
| **Operating Temperature Range** | $-40^\circ\text{C}$ to $+125^\circ\text{C}$ (Industrial/Extended) |
| **Packages** | 8-pin PDIP (P), SOIC-8 (SN), MSOP-8 (MS), TSSOP-8 (ST) |

## Pin configuration

### 8-Pin DIP / SOIC / MSOP Package

```
               ┌──────────┐
        VOUTA ─┤ 1      8 ├─ VDD (+1.8V to +6.0V)
        VINA- ─┤ 2      7 ├─ VOUTB
        VINA+ ─┤ 3      6 ├─ VINB-
   VSS (GND)  ─┤ 4      5 ├─ VINB+
               └──────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VOUTA` | Analog Output | Output of operational amplifier A |
| 2 | `VINA-` | Analog Input | Inverting input of operational amplifier A |
| 3 | `VINA+` | Analog Input | Non-inverting input of operational amplifier A |
| 4 | `VSS` | Power Supply | Negative supply rail / System Ground ($0\text{ V}$) |
| 5 | `VINB+` | Analog Input | Non-inverting input of operational amplifier B |
| 6 | `VINB-` | Analog Input | Inverting input of operational amplifier B |
| 7 | `VOUTB` | Analog Output | Output of operational amplifier B |
| 8 | `VDD` | Power Supply | Positive DC power supply rail ($+1.8\text{V} \dots +6.0\text{V}$) |

## Functional description

- **Rail-to-Rail Input (RRI):** Uses complementary PMOS and NMOS differential input pairs operating in parallel. The common-mode input range extends $300\text{ mV}$ beyond both supply rails ($V_{SS} - 0.3\text{ V}$ to $V_{DD} + 0.3\text{ V}$), preventing clipping when sensing signals ground-referenced or tied to $V_{DD}$.
- **Rail-to-Rail Output (RRO):** The output stage uses common-source CMOS drivers, allowing the output voltage to swing within $25\text{ mV}$ of either rail into a $10\text{ k}\Omega$ load, preserving dynamic range in low-voltage $3.3\text{ V}$ ADC signal paths.
- **Capacitive Load Drive:** An internal $90^\circ$ phase margin ensures that the amplifier remains unity-gain stable even when driving capacitive loads up to $500\text{ pF}$ (such as long shielded cables or ADC input sample-and-hold capacitors) without requiring external series isolation resistors.

## Absolute maximum ratings

> [!WARNING]
> Stresses beyond these absolute ratings cause permanent damage. Functional operation at these limits is not implied.

| Parameter | Rating | Unit |
|---|---|---|
| Supply Voltage ($V_{DD} - V_{SS}$) | 7.0 | V |
| All Inputs and Outputs | $V_{SS} - 1.0$ to $V_{DD} + 1.0$ | V |
| Difference Input Voltage | $|V_{DD} - V_{SS}|$ | V |
| Output Short-Circuit Current | Continuous | — |
| Operating Temperature Range | -40 to 125 | °C |
| Storage Temperature Range | -65 to 150 | °C |

## Electrical characteristics

$V_{DD} = +1.8\text{ V}$ to $+5.5\text{ V}$, $V_{SS} = 0\text{ V}$, $T_A = 25^\circ\text{C}$, $V_{CM} = V_{DD}/2$, $R_L = 10\text{ k}\Omega$ to $V_{DD}/2$, unless otherwise noted.

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Offset Voltage | $V_{OS}$ | — | $\pm 1.0$ | $\pm 4.5$ | mV | Full temperature range |
| Input Offset Voltage Drift | $dV_{OS}/dT$ | — | $\pm 2.0$ | — | $\mu\text{V/}^\circ\text{C}$ | Over temperature |
| Input Bias Current | $I_B$ | — | $\pm 1.0$ | — | pA | $T_A = 25^\circ\text{C}$ |
| Common-Mode Input Range | $V_{CMR}$ | $V_{SS}-0.3$ | — | $V_{DD}+0.3$ | V | Full temperature range |
| Common-Mode Rejection Ratio | $\text{CMRR}$ | 60 | 76 | — | dB | $V_{CM} = -0.3\text{ V}$ to $5.3\text{ V}$ (at $V_{DD}=5.0\text{V}$) |
| Power Supply Rejection Ratio | $\text{PSRR}$ | 70 | 86 | — | dB | $V_{DD} = 1.8\text{ V}$ to $5.5\text{ V}$ |
| High-Level Output Swing | $V_{OH}$ | $V_{DD}-0.05$ | $V_{DD}-0.025$ | — | V | $R_L = 10\text{ k}\Omega$ to $V_{DD}/2$ |
| Low-Level Output Swing | $V_{OL}$ | — | $V_{SS}+0.025$ | $V_{SS}+0.05$ | V | $R_L = 10\text{ k}\Omega$ to $V_{DD}/2$ |
| Gain Bandwidth Product | $\text{GBW}$ | — | 1.0 | — | MHz | $V_{DD} = 5.5\text{ V}$ |
| Slew Rate | $\text{SR}$ | — | 0.6 | — | $\text{V/}\mu\text{s}$ | Unity gain |
| Quiescent Current (per amp) | $I_Q$ | 50 | 100 | 170 | $\mu\text{A}$ | $I_O = 0$ |

## Typical application

### 3.3V Microcontroller Active Sensor Conditioning Circuit

The MCP6002 is widely used as a single-supply buffer and low-pass filter to clean up analog signals (e.g. from an electret microphone, thermistor, or photodiode) before entering a 3.3V MCU ADC:

```
      Analog Sensor Signal
               │
          [ R1 = 10kΩ ]
               │
               ├───[ R2 = 10kΩ ]─────┬────────────────┐
               │                     │                │
              [C1]                   │            ┌───┴───┐
               │                     └───[C2]─────┤ -IN   │
              GND                                 │MCP6002├───► To MCU ADC Input (0V to 3.3V)
                              3.3V ───[100kΩ]──┬──┤ +IN   │
                                               │  └───────┘
                               GND ───[100kΩ]──┘
```

Because both input and output can swing all the way to $0\text{ V}$ and $+3.3\text{ V}$, the full 12-bit dynamic range of the microcontroller ADC is utilized without deadbands.

## Common mistakes

- **Exceeding the 6.0V Absolute Maximum Supply Voltage:** The MCP6002 is a low-voltage CMOS IC. Connecting it to a standard unregulated 9V battery or a 12V automotive rail will instantly destroy the gate oxide. Always regulate power to $1.8\text{ V} \dots 5.5\text{ V}$ before feeding pin 8.
- **Assuming Low Offset Voltage for High-Precision DC Metrology:** With an input offset voltage up to $\pm 4.5\text{ mV}$, the MCP6002 is not suited for high-precision microvolt sensor conditioning (e.g. thermocouples or strain gauges). Use an auto-zero/chopper op-amp like the **MCP6V01** or **OPA333** for precision DC tasks.
- **Overlooking Phase Margin at Low Gains with Excessive Capacitance:** Although exceptionally stable up to $500\text{ pF}$, driving cables with $>1000\text{ pF}$ capacitance in unity-gain follower configuration can cause peaking. Add a small $47\text{ }\Omega$ series isolation resistor at the output pin.

## Notes

- **Family Variants:** **MCP6001** (single op-amp in SC-70-5 and SOT-23-5), **MCP6002** (dual op-amp in 8-pin packages), **MCP6004** (quad op-amp in 14-pin packages).
- **Comparison with MCP602:** The MCP6002 operates down to $1.8\text{ V}$ (vs $2.7\text{ V}$ for MCP602) and consumes only $100\text{ }\mu\text{A}$ per amplifier (vs $325\text{ }\mu\text{A}$ for MCP602), but has lower bandwidth ($1\text{ MHz}$ vs $2.8\text{ MHz}$).
