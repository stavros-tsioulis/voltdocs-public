## Overview

The **74LS00** (SN74LS00) is the definitive 14-pin Low-Power Schottky Transistor-Transistor Logic (**LS-TTL**) IC containing four independent 2-input **NAND** gates. Introduced in the 1970s, it served as the ubiquitous standard logic building block powering early personal computers (Apple II, Commodore 64, IBM PC/XT), arcade video games, and industrial control logic.

Unlike CMOS logic families (74HC), the 74LS00 uses bipolar NPN transistor junction technology with Schottky clamping diodes to prevent transistor deep saturation, delivering typical gate propagation delays of **$9.5\text{ ns}$ to $10\text{ ns}$**. It requires a tightly regulated $+5.0\text{ V} \pm 5\%$ power supply and exhibits classic TTL input/output current dynamics: inputs source $-0.4\text{ mA}$ when pulled LOW and naturally float to logic HIGH when left open.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | $4.75\text{ V}$ to $5.25\text{ V}$ DC ($5.0\text{ V}$ nominal $\pm 5\%$) |
| **Logic Family** | Low-Power Schottky Bipolar TTL (74LS) |
| **Gate Count** | 4 Independent 2-Input NAND Gates |
| **Input Switching Levels** | $V_{IH} \ge 2.0\text{ V}$, $V_{IL} \le 0.8\text{ V}$ |
| **Input Load Current ($I_{IL}$)** | $-0.4\text{ mA}$ max (Input sources current to ground when driven LOW) |
| **Output Sink / Source** | $I_{OL} = 8.0\text{ mA}$ (Strong sink), $I_{OH} = -0.4\text{ mA}$ (Weak source) |
| **Propagation Delay ($t_{pd}$)** | $9.5\text{ ns}$ typical ($15\text{ ns}$ max) |
| **Package Options** | 14-pin DIP / SOIC-14 |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
          1A 1│ 1   14│ VCC
          1B 2│       │13 4B
          1Y 3│       │12 4A
          2A 4│ 74LS00│11 4Y
          2B 5│       │10 3B
          2Y 6│       │9  3A
         GND 7│       │8  3Y
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1, 2 | `1A`, `1B` | TTL Input | Gate 1 Data Inputs |
| 3 | `1Y` | TTL Output | Gate 1 NAND Output ($1Y = \overline{1A \cdot 1B}$) |
| 4, 5 | `2A`, `2B` | TTL Input | Gate 2 Data Inputs |
| 6 | `2Y` | TTL Output | Gate 2 NAND Output ($2Y = \overline{2A \cdot 2B}$) |
| 7 | `GND` | Power | Ground reference (0 V) |
| 8 | `3Y` | TTL Output | Gate 3 NAND Output ($3Y = \overline{3A \cdot 3B}$) |
| 9, 10 | `3A`, `3B` | TTL Input | Gate 3 Data Inputs |
| 11 | `4Y` | TTL Output | Gate 4 NAND Output ($4Y = \overline{4A \cdot 4B}$) |
| 12, 13 | `4A`, `4B` | TTL Input | Gate 4 Data Inputs |
| 14 | `VCC` | Power | Supply voltage (+4.75 V to +5.25 V DC) |

## Function Table

| Input A | Input B | Output Y ($\overline{A \cdot B}$) |
|---|---|---|
| Low ($L \le 0.8\text{V}$) | Low ($L \le 0.8\text{V}$) | High ($H \ge 2.7\text{V}$) |
| Low ($L \le 0.8\text{V}$) | High ($H \ge 2.0\text{V}$) | High ($H \ge 2.7\text{V}$) |
| High ($H \ge 2.0\text{V}$) | Low ($L \le 0.8\text{V}$) | High ($H \ge 2.7\text{V}$) |
| High ($H \ge 2.0\text{V}$) | High ($H \ge 2.0\text{V}$) | Low ($L \le 0.5\text{V}$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 4.75 | 5.00 | 5.25 | V | Commercial operating range |
| High-Level Input Voltage | $V_{IH}$ | 2.0 | — | — | V | Guaranteed logic high |
| Low-Level Input Voltage | $V_{IL}$ | — | — | 0.8 | V | Guaranteed logic low |
| High-Level Output Voltage | $V_{OH}$ | 2.7 | 3.4 | — | V | $V_{CC} = 4.75\text{V}, I_{OH} = -400\ \mu\text{A}$ |
| Low-Level Output Voltage | $V_{OL}$ | — | 0.35 | 0.5 | V | $V_{CC} = 4.75\text{V}, I_{OL} = 8.0\text{ mA}$ |
| Input Low Current | $I_{IL}$ | — | -0.36 | -0.4 | mA | $V_{CC} = 5.25\text{V}, V_I = 0.4\text{V}$ |
| Input High Current | $I_{IH}$ | — | — | 20 | µA | $V_{CC} = 5.25\text{V}, V_I = 2.7\text{V}$ |
| Propagation Delay ($L \to H$) | $t_{PLH}$ | — | 9 | 15 | ns | $V_{CC} = 5.0\text{V}, C_L = 15\text{ pF}, R_L = 2\text{ k}\Omega$ |
| Propagation Delay ($H \to L$) | $t_{PHL}$ | — | 10 | 15 | ns | $V_{CC} = 5.0\text{V}, C_L = 15\text{ pF}, R_L = 2\text{ k}\Omega$ |
| Supply Current (Total IC) | $I_{CCH}$ | — | 2.4 | 4.4 | mA | All outputs HIGH |
| Supply Current (Total IC) | $I_{CCL}$ | — | 4.4 | 8.8 | mA | All outputs LOW |

## Common mistakes

- **Driving pure 5V CMOS inputs directly from 74LS00 outputs:** The minimum $V_{OH}$ of a 74LS gate is only **$2.7\text{ V}$**, whereas a 5V 74HC gate expects $V_{IH} \ge 3.5\text{ V}$ ($0.7 \times V_{CC}$). Add a **$1\text{ k}\Omega \dots 4.7\text{ k}\Omega$ pull-up resistor** from the LS output to $+5\text{V}$ or use a **74HCT** series device instead.
- **Using weak pull-down resistors on inputs:** Because an LS-TTL input sources up to $0.4\text{ mA}$ when grounded, a pull-down resistor must be $\le 1\text{ k}\Omega$ (preferably $\le 470\ \Omega$) to ensure the voltage drop remains below $V_{IL} = 0.8\text{ V}$. A standard $10\text{ k}\Omega$ pull-down resistor will drop $4\text{ V}$ and fail to register a LOW state.
- **Exceeding the 5.25V supply rail limit:** Bipolar TTL lacks wide supply latitude. Operating above $5.5\text{V}$ causes rapid thermal breakdown.

## Notes

- **Pin-Compatible Drop-In Alternatives:** 74HC00 (CMOS upgrade), 74HCT00 (TTL-compatible CMOS drop-in), 74ALS00 (Advanced Low-Power Schottky).
