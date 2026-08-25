## Overview

The **MIC29302WU** (MIC29302) is a 3A high-current, ultra-low dropout (LDO) adjustable linear voltage regulator manufactured by Microchip Technology (originally Micrel Semiconductor). Housed in a surface-mount **TO-263-5 (D2PAK)** package (or through-hole TO-220-5 as MIC29302WT), it provides clean, adjustable output voltages from **$1.24\text{V}$ to $26\text{V}$** with an extraordinarily low typical dropout of only **$370\text{ mV}$ at full $3.0\text{A}$ load** ($250\text{ mV}$ at $1.5\text{A}$).

Using Micrel's proprietary Super βeta PNP process, the MIC29302 delivers high output current without the severe $1.5\text{V} \dots 2.5\text{V}$ dropout penalty of classic regulators like the LM317 or LM7805. Featuring a TTL-compatible `ENABLE` control pin for zero-current shutdown mode, reverse-battery protection, and thermal limiting, it is widely utilized for high-power FPGA/SDR core supplies, cellular/GSM modem power rails (which require high pulsed 2A–3A currents with minimal voltage sag), post-regulators for SMPS, and high-current battery chargers.

## Quick reference

| | |
|---|---|
| **Regulator Type** | High-Current Low-Dropout (LDO) Adjustable Regulator |
| **Package** | TO-263-5 (D2PAK SMD) / TO-220-5 (MIC29302WT) |
| **Adjustable Output Voltage ($V_{OUT}$)** | $+1.24\text{ V}$ to $+26.0\text{ V}$ DC |
| **Reference Voltage ($V_{REF}$)** | $1.240\text{ V}$ ($\pm 1\%$ initial tolerance) |
| **Maximum Output Current ($I_{OUT}$)** | $3.0\text{ A}$ continuous |
| **Dropout Voltage ($V_{DROP}$)** | $370\text{ mV}$ typ ($600\text{ mV}$ max) at $3.0\text{A}$ / $60\text{ mV}$ at $100\text{mA}$ |
| **Operating Input Voltage ($V_{IN}$)** | $2.0\text{ V}$ to $26.0\text{ V}$ (Withstands $+60\text{V}$ transients) |
| **Control Features** | Logic-Level `ENABLE` Pin (Active-HIGH, $< 1\ \mu\text{A}$ in shutdown) |

## Pinout (TO-263-5 / TO-220-5 Package)

Looking at the package from the front with pins pointing down:

```
        ┌──────────────┐
        │   TO-263-5   │
        │  MIC29302WU  │
        └─┬──┬───┬──┬──┘
          1  2   3  4  5
         EN VIN GND VOUT ADJ
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `ENABLE` | Digital Input | Logic-level enable control (Active-HIGH $\ge 2.4\text{V}$, Low $\le 0.8\text{V}$ shuts off). Tie to `VIN` if unused. |
| 2 | `INPUT` (`VIN`) | Power Input | Unregulated DC input ($+2.0\text{ V}$ to $+26.0\text{ V}$) |
| 3 / Tab | `GROUND` (`GND`) | Ground | Common circuit ground and heatsink thermal tab |
| 4 | `OUTPUT` (`VOUT`) | Power Output | Regulated DC output (Requires $\ge 10\ \mu\text{F}$ output capacitor) |
| 5 | `ADJUST` (`ADJ`) | Analog Input | Voltage feedback node ($1.240\text{V}$ reference set by external divider) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Reference Voltage ($25^\circ\text{C}$) | $V_{REF}$ | 1.228 | 1.240 | 1.252 | V | $I_L = 10\text{mA}$ ($\pm 1\%$) |
| Reference Voltage (Full Temp) | $V_{REF}$ | 1.215 | 1.240 | 1.265 | V | $-40^\circ\text{C} \le T_J \le +125^\circ\text{C}$ |
| Dropout Voltage ($3.0\text{A}$) | $V_{DROP}$ | — | 370 | 600 | mV | $\Delta V_{OUT} = 100\text{mV}, I_L = 3.0\text{A}$ |
| Dropout Voltage ($1.5\text{A}$) | $V_{DROP}$ | — | 250 | 450 | mV | $I_L = 1.5\text{A}$ |
| Ground Current ($I_{OUT} = 3\text{A}$) | $I_{GND}$ | — | 60 | 100 | mA | $V_{IN} = V_{OUT} + 1\text{V}, I_L = 3\text{A}$ |
| Shutdown Supply Current | $I_{SD}$ | — | 0.05 | 10 | µA | $V_{ENABLE} \le 0.4\text{V}, V_{IN} = 26\text{V}$ |
| Current Limit | $I_{CL}$ | 3.5 | 4.5 | — | A | $V_{OUT} = 0\text{V}$ |

## Voltage Setting Calculation

The output voltage is configured with a two-resistor divider between `VOUT`, `ADJUST`, and `GND`:

$$ V_{OUT} = V_{REF} \times \left(1 + \frac{R_1}{R_2}\right) = 1.240\text{V} \times \left(1 + \frac{R_1}{R_2}\right) $$

- Set $R_2 \approx 10\text{ k}\Omega$ (so the divider current is $\approx 124\ \mu\text{A}$, minimizing bias current error).
- **For $V_{OUT} = 3.3\text{V}$:** $R_2 = 10\text{ k}\Omega \implies R_1 = 16.6\text{ k}\Omega$ (use standard $16.5\text{ k}\Omega$ 1%).
- **For $V_{OUT} = 5.0\text{V}$:** $R_2 = 10\text{ k}\Omega \implies R_1 = 30.3\text{ k}\Omega$ (use standard $30.1\text{ k}\Omega$ 1%).

## Typical Application Circuit

```
  Unregulated DC In (e.g. 5V or 12V)
           │
           ├───[ C_IN: 10µF Tantalum/Electrolytic ]───┐
           │                                          │
       [Pin 2: INPUT]                                 │
      MIC29302WU                                      │
  MCU ─[Pin 1: ENABLE]                                │
       [Pin 3: GROUND] ───────────────────────────────┼─── Common System GND
       [Pin 4: OUTPUT] ────┬──────────────────────────┤
           │               │                          │
           │             [ R1: 16.5kΩ ]               │
           │               │                          │
           │               ├──► [Pin 5: ADJUST]       │
           │               │                          │
           │             [ R2: 10kΩ ]                 │
           │               │                          │
           ├───[ C_OUT: 22µF - 47µF (ESR > 0.05Ω) ]───┘
           │
  Regulated +3.3V DC Output (Up to 3.0A High-Current Rail)
```

## Capacitor Stability Requirements

- **Output Capacitor:** The MIC29302 requires an output capacitor of **$\ge 10\ \mu\text{F}$** (recommend $22\ \mu\text{F} \dots 47\ \mu\text{F}$) between `OUTPUT` and `GROUND`.
- **ESR Considerations:** The ESR must be between **$0.05\ \Omega$ and $2.0\ \Omega$**. If using ceramic MLCC output capacitors, add a small $0.22\ \Omega$ series resistor to ensure LDO control loop phase margin stability.

## Common mistakes

- **Leaving the `ENABLE` pin floating:** The `ENABLE` pin has internal high impedance. Leaving it disconnected may cause erratic shutdown/startup behavior. Tie directly to `INPUT` (`VIN`) for always-on operation.
- **Neglecting PCB thermal dissipation at 3A:** At $3\text{A}$ load with $1.5\text{V}$ voltage drop ($V_{IN} - V_{OUT}$), power dissipation is $4.5\text{ Watts}$. Ensure ample PCB copper ground plane area is connected to the TO-263 tab.

## Notes

- **Suffix Identification:** "WU" designates TO-263-5 (D2PAK) surface mount; "WT" designates TO-220-5 through-hole package.
