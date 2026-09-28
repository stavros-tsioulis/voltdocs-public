## Overview

The **XC6206P332MR** is an ultra-low power, high-precision 3.3V low-dropout (LDO) positive voltage regulator manufactured by Torex Semiconductor and widely second-sourced across the electronics industry. Built using CMOS process and laser trimming technologies, the XC6206 series delivers up to $200\text{ mA}$ of continuous output current with an exceptionally low quiescent supply current of only $1.0\,\mu\text{A}$ typical.

It is easily recognizable by its **`662K`** top-side package marking on miniature 3-pin SOT-23 packages. Due to its minimal quiescent drain, low dropout voltage ($160\text{ mV}$ at $100\text{ mA}$), and compatibility with low-cost ceramic capacitors, the XC6206 is one of the most ubiquitous 3.3V regulator ICs found on ESP8266/ESP32 development boards, STM32 "Blue Pill" modules, wireless sensor nodes, and battery-powered IoT hardware.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Positive Fixed Low-Dropout (LDO) Linear Regulator |
| **Output Voltage ($V_{OUT}$)** | $3.3\text{ V}$ fixed ($\pm 2\%$ standard accuracy) |
| **Input Voltage Range ($V_{IN}$)** | $1.8\text{ V}$ to $6.0\text{ V}$ DC ($6.5\text{ V}$ abs max) |
| **Maximum Output Current ($I_{OUT}$)** | $200\text{ mA}$ continuous ($250\text{ mA}$ typical limit) |
| **Quiescent Current ($I_{SS}$)** | $1.0\,\mu\text{A}$ typical ($3.0\,\mu\text{A}$ max) |
| **Dropout Voltage ($V_{dif}$)** | $160\text{ mV}$ typ at $100\text{ mA}$ ($380\text{ mV}$ at $200\text{ mA}$) |
| **Ripple Rejection (PSRR)** | $30\text{ dB}$ at $1\text{ kHz}$ |
| **Output Capacitor Compatibility** | Ceramic MLCC $\ge 1.0\,\mu\text{F}$ (low ESR compatible) |
| **Common Top Marking** | `662K` (SOT-23-3) |
| **Package Options** | SOT-23-3 (MR), SOT-89 (PR), TO-92 (TH) |

## Pin configuration

### SOT-23-3 Package (Top View)

```
        ┌──────────┐
        │   662K   │
        │  [XC6206]│
        └─┬──────┬─┘
          │      │
       1  │      │  2
     (VSS)│      │(VOUT)
          │      │
          └──┬───┘
             │ 3 (VIN)
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VSS` | Power / Ground | Ground reference terminal ($0\text{ V}$) |
| 2 | `VOUT` | Power Output | Regulated $+3.3\text{ V}$ DC output voltage |
| 3 | `VIN` | Power Input | Unregulated DC input voltage ($+1.8\text{ V}$ to $+6.0\text{ V}$) |

### SOT-89 Package (Top View)

```
        ┌──────────┐
        │  [SOT89] │
        └──┬──┬──┬─┘
           │  │  │
           1  2  3
         VSS VIN VOUT (Tab = VIN)
```

> [!NOTE]
> Pin assignments differ between package types. In **SOT-23-3**, pin 2 is `VOUT` and pin 3 is `VIN`. In **SOT-89**, pin 2 (and the center tab) is `VIN` and pin 3 is `VOUT`. Always verify the package footprint before layout.

## Absolute maximum ratings

> [!WARNING]
> Exceeding these values will cause permanent device breakdown. The XC6206 is a low-voltage CMOS IC and cannot withstand raw $9\text{V}$, $12\text{V}$, or $24\text{V}$ power rails.

| Parameter | Symbol | Limit | Unit |
|---|---|---|---|
| Input Voltage | $V_{IN}$ | $-0.3$ to $+7.0$ | V |
| Output Current | $I_{OUT}$ | $500$ | mA |
| Output Voltage | $V_{OUT}$ | $-0.3$ to $V_{IN} + 0.3$ | V |
| Power Dissipation ($T_A = 25^\circ\text{C}$, SOT-23) | $P_D$ | $250$ | mW |
| Power Dissipation ($T_A = 25^\circ\text{C}$, SOT-89) | $P_D$ | $500$ | mW |
| Operating Ambient Temperature | $T_{opr}$ | $-40$ to $+85$ | °C |
| Storage Temperature Range | $T_{stg}$ | $-55$ to $+125$ | °C |

## Electrical characteristics

($V_{IN} = 4.3\text{ V}$, $C_{IN} = C_{OUT} = 1\,\mu\text{F}$, $T_A = 25^\circ\text{C}$ unless otherwise noted)

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Output Voltage | $V_{OUT}$ | 3.234 | 3.300 | 3.366 | V | $I_{OUT} = 30\text{ mA}$ ($\pm 2\%$) |
| Maximum Output Current | $I_{OUT(MAX)}$ | 200 | — | — | mA | $V_{IN} = 4.3\text{ V}$ |
| Load Regulation | $\Delta V_{OUT}$ | — | 15 | 40 | mV | $I_{OUT} = 1\text{ mA to } 100\text{ mA}$ |
| Dropout Voltage | $V_{dif1}$ | — | 160 | 250 | mV | $I_{OUT} = 100\text{ mA}$ |
| | $V_{dif2}$ | — | 380 | 600 | mV | $I_{OUT} = 200\text{ mA}$ |
| Supply Current (Quiescent) | $I_{SS}$ | — | 1.0 | 3.0 | µA | $I_{OUT} = 0\text{ mA}$ |
| Line Regulation | $\Delta V_{OUT} / (\Delta V_{IN} \cdot V_{OUT})$ | — | 0.05 | 0.20 | %/V | $V_{IN} = 4.3\text{ V to } 6.0\text{ V}, I_{OUT} = 30\text{ mA}$ |
| Input Voltage Range | $V_{IN}$ | 1.8 | — | 6.0 | V | Normal operation |
| Short-Circuit Current | $I_{short}$ | — | 50 | — | mA | $V_{OUT} = 0\text{ V}$ |

## Typical application circuit

```
       VIN (+3.5V to +5.5V)
       ────────────────────────┬─────────────────────┐
                               │                     │
                            ┌──┴──┐               ┌──┴──┐
                            │ C1  │               │ 3   │ (VIN)
                            │ 1µF │             ┌─┴─────┴─┐
                            │MLCC │             │ XC6206  │
                            └──┬──┘             │  (662K) │
                               │                └─┬─────┬─┘
                               │                1 │     │ 2
                               │            (VSS) │     │ (VOUT)
       GND ────────────────────┴──────────────────┴──┬──┼──────────────── GND
                                                     │  │
                                                  ┌──┴──┴──┐
                                                  │   C2   │
                                                  │ 1µF    │
                                                  │ MLCC   │
                                                  └──┬─────┘
                                                     │
       VOUT (+3.3V Regulated) ───────────────────────┴─────────────────── VCC_3V3 (to MCU / ESP32)
```

### Component Selection
- **Input Capacitor ($C_1$):** $1.0\,\mu\text{F}$ to $4.7\,\mu\text{F}$ ceramic capacitor (X5R or X7R dielectric) placed as close as possible between pin 3 (`VIN`) and pin 1 (`VSS`).
- **Output Capacitor ($C_2$):** $1.0\,\mu\text{F}$ to $10\,\mu\text{F}$ low-ESR multi-layer ceramic capacitor (MLCC). The XC6206 internal phase compensation network is specifically tuned for stable operation with low-ESR ceramic capacitors ($0.1\,\Omega \le \text{ESR} \le 5\,\Omega$).

## Design considerations & common mistakes

- **Strict 6.0V Input Voltage Limit:** Unlike bipolar regulators like the LM317 ($40\text{ V}$) or AMS1117 ($15\text{ V}$), the XC6206 is built on a submicron CMOS process with a thin gate oxide. Feeding raw $9\text{V}$ batteries, $12\text{V}$ automotive rails, or unregulated wall adapters will instantly destroy the device. The XC6206 is intended for $5\text{V}$ USB rails, single-cell Li-ion batteries ($3.7\text{ V} \dots 4.2\text{ V}$), or $3\times$ AA/AAA battery packs.
- **SOT-23 Thermal Limitations:** In an SOT-23 package, the maximum continuous power dissipation is typically $250\text{ mW}$ on standard FR4. If powering from a $5.0\text{ V}$ USB rail ($V_{IN} = 5\text{V}$) to provide $3.3\text{ V}$ at $150\text{ mA}$:
  $$P_D = (V_{IN} - V_{OUT}) \times I_{OUT} = (5.0\text{ V} - 3.3\text{ V}) \times 0.15\text{ A} = 0.255\text{ W}$$
  This reaches the package thermal ceiling and will trigger thermal throttling or high die temperatures. For continuous loads above $120\text{ mA}$ from a $5\text{ V}$ rail, use a larger package (SOT-89) or a higher-dissipation LDO like the AMS1117-3.3.
- **Wi-Fi RF Peak Current Bursts:** An ESP8266 or ESP32 module can draw brief transmit pulses of $250\text{ mA} \dots 450\text{ mA}$. While some XC6206 clones survive these bursts if backed by a large bulk capacitor ($10\,\mu\text{F} \dots 47\,\mu\text{F}$ at $V_{OUT}$), the regulator is rated for $200\text{ mA}$ continuous. Repeated peak current events without adequate reservoir capacitance will cause $V_{OUT}$ to droop below the MCU's brownout threshold ($2.7\text{ V}$).
- **Clone Variations:** Due to its massive market presence, numerous Chinese manufacturers fabricate compatible "662K" parts. Quiescent current on clones may measure $2\,\mu\text{A} \dots 5\,\mu\text{A}$ instead of Torex's specified $1.0\,\mu\text{A}$, and current limit thresholds can vary between $180\text{ mA}$ and $300\text{ mA}$.
