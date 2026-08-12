## Overview

The **LT1963A-3.3** (commonly **LT1963EQ-3.3** in TO-263-5 / DDPAK-5 or **LT1963EST-3.3** in SOT-223) is a $1.5\text{ A}$ low dropout (LDO) linear regulator manufactured by Analog Devices (originally Linear Technology). Optimized for fast transient response and low output noise (**$40\ \mu\text{Vrms}$** over $10\text{ Hz} \dots 100\text{ kHz}$), it provides a clean, stable **$+3.3\text{ V}$** DC power rail.

With a low dropout voltage of **$340\text{ mV}$ at full $1.5\text{ A}$ load** and stability using low-ESR ceramic output capacitors (minimum $10\ \mu\text{F}$), the LT1963A-3.3 is widely specified for sensitive RF transceivers, high-resolution ADCs/DACs, FPGA core rails, and high-fidelity audio equipment.

## Quick reference

| | |
|---|---|
| **Regulator Type** | Low-Noise Fast Transient Response LDO Linear Regulator |
| **Package** | TO-263-5 (DDPAK-5) / SOT-223 / TO-220-5 / SOIC-8 EP |
| **Input Voltage Range ($V_{IN}$)** | $3.8\text{ V}$ to $20.0\text{ V}$ DC |
| **Output Voltage ($V_{OUT}$)** | $+3.3\text{ V}$ DC (Fixed $\pm 3\%$ precision over temperature) |
| **Max Output Current ($I_{OUT}$)** | $1.5\text{ A}$ continuous |
| **Dropout Voltage ($V_{DROP}$)** | $340\text{ mV}$ typical at $I_{OUT} = 1.5\text{A}$ |
| **Output Noise Voltage** | $40\ \mu\text{Vrms}$ ($10\text{ Hz}$ to $100\text{ kHz}$) |
| **Quiescent Supply Current** | $1.0\text{ mA}$ typical ($10\ \mu\text{A}$ in shutdown) |

## Pinout (TO-263-5 / DDPAK-5 Package)

```
        ┌──────────────────┐
        │   LT1963A-3.3    │  (Top View)
        └─┬──┬──┬──┬──┬────┘
          1  2  3  4  5
```

| Pin | Name | Description |
|---|---|---|
| 1 | `~SHDN~` | Active-LOW Shutdown input pin (Low = Power Down $<10\mu\text{A}$, High = Enabled) |
| 2 | `IN` | Unregulated DC Input power pin (+3.8V to +20.0V DC) |
| 3 | `GND` | Ground reference connection (Solder large tab to ground plane) |
| 4 | `OUT` | Regulated $+3.3\text{V}$ output pin (Bypass with $\ge 10\mu\text{F}$ capacitor) |
| 5 | `SENSE` | Output voltage sense pin (Connect directly to Pin 4 / load rail) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Input Supply Voltage | $V_{IN}$ | 3.8 | 5.0 | 20.0 | V | Operating range for 3.3V output |
| Output Voltage Precision| $V_{OUT}$ | 3.23 | 3.30 | 3.37 | V | $10\text{mA} \le I_{OUT} \le 1.5\text{A}$ |
| Dropout Voltage | $V_{DROP}$ | — | 340 | 550 | mV | $I_{OUT} = 1.5\text{A}$ |
| Output Noise Voltage | $e_n$ | — | 40 | — | $\mu\text{Vrms}$ | $C_{OUT} = 10\mu\text{F}, 10\text{Hz} \dots 100\text{kHz}$ |
| Ripple Rejection (PSRR)| $PSRR$ | 55 | 63 | — | dB | $f = 120\text{Hz}, V_{IN} = 4.3\text{V} + 0.5\text{Vp-p}$ |
| Shutdown Current | $I_{SHDN}$ | — | 1.0 | 10 | $\mu\text{A}$ | $\overline{SHDN} = 0\text{V}$ |

## Common mistakes

- **Leaving SENSE pin (Pin 5) unconnected:** Pin 5 (`SENSE`) feeds output voltage back into the internal error amplifier. Leaving Pin 5 floating causes the output to jump to the input rail ($V_{IN}$)! Always tie Pin 5 directly to Pin 4 (`OUT`).
- **Insufficient PCB copper for thermal dissipation at 1.5A:** Dropping 5V down to 3.3V at 1.5A dissipates $P_D = (5\text{V} - 3.3\text{V}) \times 1.5\text{A} = 2.55\text{ W}$. Solder the TO-263 / SOT-223 tab to a large copper ground plane to prevent thermal shutdown.

## Notes

- **LT1963 vs LT1963A:** The "A" revision eliminates reverse current flow back into the input pin when the input is grounded or pulled low, protecting upstream circuitry.
