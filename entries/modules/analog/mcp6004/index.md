## Overview

The **MCP6004** is a low-power quad operational amplifier manufactured by Microchip Technology. Engineered for battery-powered, portable, and low-voltage embedded systems, the MCP6004 packs four independent operational amplifiers with full **Rail-to-Rail Input and Output (RRIO)** into a standard 14-pin DIP, SOIC, or TSSOP package.

Operating from a single supply voltage from **$1.8\text{ V}$ to $6.0\text{ V}$**, each amplifier draws an ultra-low quiescent current of only **$100\text{ }\mu\text{A}$** ($400\text{ }\mu\text{A}$ total for the entire quad IC). With a $1.0\text{ MHz}$ Gain Bandwidth Product (GBW), $0.6\text{ V/}\mu\text{s}$ slew rate, $1.0\text{ pA}$ input bias current, and a robust $90^\circ$ phase margin capable of driving up to $500\text{ pF}$ capacitive loads, the MCP6004 is the definitive modern, low-voltage alternative to the bipolar LM324 for $3.3\text{ V}$ microcontroller signal conditioning and multi-channel sensor front-ends.

## Quick reference

| | |
|---|---|
| **Function** | 1MHz Low-Power Rail-to-Rail Input/Output Quad Op-Amp |
| **Supply Voltage Range ($V_{DD} - V_{SS}$)** | $1.8\text{ V}$ to $6.0\text{ V}$ DC (single supply) |
| **Input Common-Mode Range** | Rail-to-Rail ($V_{SS} - 0.3\text{ V}$ to $V_{DD} + 0.3\text{ V}$) |
| **Output Swing** | Rail-to-Rail ($V_{SS} + 25\text{ mV}$ to $V_{DD} - 25\text{ mV}$ with $10\text{ k}\Omega$ load) |
| **Op-Amp Channels** | 4 independent operational amplifiers |
| **Quiescent Current (Total, 4 Ch)** | $400\text{ }\mu\text{A}$ typ ($100\text{ }\mu\text{A}$ per channel) |
| **Gain Bandwidth Product (GBW)** | $1.0\text{ MHz}$ typ |
| **Slew Rate (SR)** | $0.6\text{ V/}\mu\text{s}$ typ |
| **Input Bias Current ($I_B$)** | $1.0\text{ pA}$ typ at $25^\circ\text{C}$ ($1.0\text{ nA}$ max over temp) |
| **Input Offset Voltage ($V_{OS}$)** | $\pm 4.5\text{ mV}$ max |
| **Phase Margin** | $90^\circ$ ($C_L$ stable up to $500\text{ pF}$) |
| **Operating Temperature Range** | $-40^\circ\text{C}$ to $+125^\circ\text{C}$ |
| **Packages** | 14-pin PDIP (P), SOIC-14 (SL), TSSOP-14 (ST) |

## Pin configuration

### 14-Pin DIP / SOIC Package

```
               ┌──────────┐
        VOUTA ─┤ 1     14 ├─ VOUTD
        VINA- ─┤ 2     13 ├─ VIND-
        VINA+ ─┤ 3     12 ├─ VIND+
          VDD ─┤ 4     11 ├─ VSS (GND)
        VINB+ ─┤ 5     10 ├─ VINC+
        VINB- ─┤ 6      9 ├─ VINC-
        VOUTB ─┤ 7      8 ├─ VOUTC
               └──────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VOUTA` | Analog Output | Output of operational amplifier A |
| 2 | `VINA-` | Analog Input | Inverting input of operational amplifier A |
| 3 | `VINA+` | Analog Input | Non-inverting input of operational amplifier A |
| 4 | `VDD` | Power Supply | Positive DC power supply rail ($+1.8\text{V} \dots +6.0\text{V}$) |
| 5 | `VINB+` | Analog Input | Non-inverting input of operational amplifier B |
| 6 | `VINB-` | Analog Input | Inverting input of operational amplifier B |
| 7 | `VOUTB` | Analog Output | Output of operational amplifier B |
| 8 | `VOUTC` | Analog Output | Output of operational amplifier C |
| 9 | `VINC-` | Analog Input | Inverting input of operational amplifier C |
| 10 | `VINC+` | Analog Input | Non-inverting input of operational amplifier C |
| 11 | `VSS` | Power Supply | Negative supply rail / Ground ($0\text{ V}$) |
| 12 | `VIND+` | Analog Input | Non-inverting input of operational amplifier D |
| 13 | `VIND-` | Analog Input | Inverting input of operational amplifier D |
| 14 | `VOUTD` | Analog Output | Output of operational amplifier D |

## Functional description

- **Rail-to-Rail Input (RRI):** An internal complementary PMOS/NMOS differential input stage accepts signals that swing beyond both power supply rails (from $V_{SS} - 0.3\text{ V}$ up to $V_{DD} + 0.3\text{ V}$), eliminating the input clipping common to traditional bipolar op-amps.
- **Rail-to-Rail Output (RRO):** The CMOS output stage swings within $25\text{ mV}$ of either supply rail under a $10\text{ k}\Omega$ load, maximizing ADC dynamic range in $3.3\text{ V}$ and $5\text{ V}$ microcontrollers.
- **Capacitive Drive Capability:** The generous $90^\circ$ phase margin allows the MCP6004 to drive capacitive loads up to $500\text{ pF}$ without external compensation, preventing ringing when driving long coaxial cables or ADC sampling capacitors.

## Absolute maximum ratings

> [!WARNING]
> Stresses beyond these ratings cause permanent damage. Functional operation at these limits is not guaranteed.

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
| Input Offset Drift | $dV_{OS}/dT$ | — | $\pm 2.0$ | — | $\mu\text{V/}^\circ\text{C}$ | Over temperature |
| Input Bias Current | $I_B$ | — | $\pm 1.0$ | — | pA | $T_A = 25^\circ\text{C}$ |
| Common-Mode Input Range | $V_{CMR}$ | $V_{SS}-0.3$ | — | $V_{DD}+0.3$ | V | Full temperature range |
| Common-Mode Rejection Ratio | $\text{CMRR}$ | 60 | 76 | — | dB | $V_{CM} = -0.3\text{ V}$ to $5.3\text{ V}$ (at $V_{DD}=5.0\text{V}$) |
| Power Supply Rejection Ratio | $\text{PSRR}$ | 70 | 86 | — | dB | $V_{DD} = 1.8\text{ V}$ to $5.5\text{ V}$ |
| High-Level Output Swing | $V_{OH}$ | $V_{DD}-0.05$ | $V_{DD}-0.025$ | — | V | $R_L = 10\text{ k}\Omega$ to $V_{DD}/2$ |
| Low-Level Output Swing | $V_{OL}$ | — | $V_{SS}+0.025$ | $V_{SS}+0.05$ | V | $R_L = 10\text{ k}\Omega$ to $V_{DD}/2$ |
| Gain Bandwidth Product | $\text{GBW}$ | — | 1.0 | — | MHz | $V_{DD} = 5.5\text{ V}$ |
| Slew Rate | $\text{SR}$ | — | 0.6 | — | $\text{V/}\mu\text{s}$ | Unity gain |
| Quiescent Current (Total 4 Ch)| $I_Q$ | 200 | 400 | 680 | $\mu\text{A}$ | All 4 amplifiers, $I_O = 0$ |

## Typical application

### 4-Channel Single-Supply Sensor Conditioning / Active Filter

A single MCP6004 conditioning four separate analog sensor signals (photodiodes, thermistors, gas sensors, or piezoelectric elements) directly from a $3.3\text{ V}$ battery bus:

```
  Sensor Input 1 ──►[ Amp A (Filter) ]──► ADC Ch 0 (0V to 3.3V)
  Sensor Input 2 ──►[ Amp B (Filter) ]──► ADC Ch 1 (0V to 3.3V)
  Sensor Input 3 ──►[ Amp C (Filter) ]──► ADC Ch 2 (0V to 3.3V)
  Sensor Input 4 ──►[ Amp D (Filter) ]──► ADC Ch 3 (0V to 3.3V)
```

Unlike the LM324, which cannot swing above $\sim 1.8\text{ V}$ on a $3.3\text{ V}$ rail, the MCP6004 utilizes the entire $0\text{ V}$ to $3.3\text{ V}$ input range of modern 12-bit ADCs.

## Common mistakes

- **Exceeding 6.0V Supply Voltage:** The MCP6004 cannot be connected to a 9V or 12V supply. The absolute maximum supply voltage is $7.0\text{ V}$. For higher-voltage industrial supplies ($>6\text{ V}$), use the **LM324** or **MCP604**.
- **Leaving Unused Channels Floating:** If only two or three channels are used, always configure unused op-amps as unity-gain buffers with their non-inverting input tied to a stable DC voltage (such as $V_{DD}/2$ or Ground) and output tied to the inverting input.
- **Assuming Low Offset Voltage for Microvolt DC Sensing:** With an offset voltage up to $\pm 4.5\text{ mV}$, the MCP6004 is not intended for precision thermocouple or strain-gauge conditioning without calibration.

## Notes

- **Family Variants:** **MCP6001** (single op-amp), **MCP6002** (dual op-amp), **MCP6004** (quad op-amp).
- **Comparison with LM324:** The MCP6004 provides true rail-to-rail input and output, lower supply voltage down to $1.8\text{ V}$, and sub-pA bias currents, making it far superior for modern low-voltage digital electronics.
