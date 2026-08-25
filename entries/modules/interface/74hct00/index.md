## Overview

The **74HCT00** (SN74HCT00) is a high-speed silicon-gate CMOS integrated circuit containing four independent 2-input **NAND** logic gates. It provides identical logical functionality and pinout to the standard 74HC00 and legacy 74LS00, but is fabricated with **TTL-compatible input switching thresholds**.

Operating from a standard $+5.0\text{V}$ power rail, the 74HCT00 recognizes any input above **$V_{IH} \ge 2.0\text{V}$** as a valid logic HIGH (and below **$V_{IL} \le 0.8\text{V}$** as a logic LOW), while driving full rail-to-rail CMOS outputs ($0\text{V}$ to $5\text{V}$). This makes the 74HCT00 an essential interface element for connecting 3.3V microcontroller outputs (ESP32, Raspberry Pi, ARM Cortex) or classic 74LS TTL chips directly to 5V CMOS logic gates.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | 4.5 V to 5.5 V DC (5.0 V nominal) |
| **Logic Family** | TTL-Compatible High-Speed CMOS (74HCT) |
| **Gate Count** | 4 Independent 2-Input NAND Gates |
| **Input Thresholds** | $V_{IH} \ge 2.0\text{ V}$, $V_{IL} \le 0.8\text{ V}$ (Direct 3.3V / TTL compatibility) |
| **Logic Function** | $Y = \overline{A \cdot B}$ |
| **Propagation Delay ($t_{pd}$)** | $10\text{ ns}$ typ ($20\text{ ns}$ max) at $V_{CC} = 4.5\text{V}$ |
| **Output Drive Current** | $\pm 4.0\text{ mA}$ at $V_{CC} = 4.5\text{V}$ |
| **Package Options** | 14-pin DIP / SOIC-14 / TSSOP-14 |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
          1A 1│ 1   14│ VCC
          1B 2│       │13 4B
          1Y 3│       │12 4A
          2A 4│74HCT00│11 4Y
          2B 5│       │10 3B
          2Y 6│       │9  3A
         GND 7│       │8  3Y
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1, 2 | `1A`, `1B` | Digital Input | Gate 1 Data Inputs (TTL/3.3V compatible) |
| 3 | `1Y` | Digital Output | Gate 1 NAND Output ($1Y = \overline{1A \cdot 1B}$) |
| 4, 5 | `2A`, `2B` | Digital Input | Gate 2 Data Inputs |
| 6 | `2Y` | Digital Output | Gate 2 NAND Output ($2Y = \overline{2A \cdot 2B}$) |
| 7 | `GND` | Power | Ground reference (0 V) |
| 8 | `3Y` | Digital Output | Gate 3 NAND Output ($3Y = \overline{3A \cdot 3B}$) |
| 9, 10 | `3A`, `3B` | Digital Input | Gate 3 Data Inputs |
| 11 | `4Y` | Digital Output | Gate 4 NAND Output ($4Y = \overline{4A \cdot 4B}$) |
| 12, 13 | `4A`, `4B` | Digital Input | Gate 4 Data Inputs |
| 14 | `VCC` | Power | Supply voltage (+4.5 V to +5.5 V DC) |

## Function Table

| Input A | Input B | Output Y ($\overline{A \cdot B}$) |
|---|---|---|
| Low ($L \le 0.8\text{V}$) | Low ($L \le 0.8\text{V}$) | High ($H \ge 4.4\text{V}$) |
| Low ($L \le 0.8\text{V}$) | High ($H \ge 2.0\text{V}$) | High ($H \ge 4.4\text{V}$) |
| High ($H \ge 2.0\text{V}$) | Low ($L \le 0.8\text{V}$) | High ($H \ge 4.4\text{V}$) |
| High ($H \ge 2.0\text{V}$) | High ($H \ge 2.0\text{V}$) | Low ($L \le 0.1\text{V}$) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 4.5 | 5.0 | 5.5 | V | Standard HCT range |
| High-Level Input Voltage | $V_{IH}$ | 2.0 | — | — | V | $V_{CC} = 4.5\text{V} \dots 5.5\text{V}$ |
| Low-Level Input Voltage | $V_{IL}$ | — | — | 0.8 | V | $V_{CC} = 4.5\text{V} \dots 5.5\text{V}$ |
| High-Level Output Voltage | $V_{OH}$ | 4.4 | 4.5 | — | V | $V_{CC} = 4.5\text{V}, I_{OH} = -20\ \mu\text{A}$ |
| High-Level Output Voltage (Load) | $V_{OH}$ | 3.84 | 4.32 | — | V | $V_{CC} = 4.5\text{V}, I_{OH} = -4.0\text{ mA}$ |
| Low-Level Output Voltage | $V_{OL}$ | — | 0.0 | 0.1 | V | $V_{CC} = 4.5\text{V}, I_{OL} = 20\ \mu\text{A}$ |
| Low-Level Output Voltage (Load) | $V_{OL}$ | — | 0.17 | 0.33 | V | $V_{CC} = 4.5\text{V}, I_{OL} = 4.0\text{ mA}$ |
| Propagation Delay | $t_{PLH}, t_{PHL}$ | — | 10 | 20 | ns | $V_{CC} = 4.5\text{V}, C_L = 50\text{ pF}$ |
| Quiescent Current | $I_{CC}$ | — | — | 2.0 | µA | $V_{IN} = V_{CC}\text{ or GND}$ |

## Common mistakes

- **Powering below 4.5V:** Standard 74HCT logic requires a regulated $5\text{V} \pm 10\%$ rail ($4.5\text{V} \dots 5.5\text{V}$). It cannot operate reliably at $3.3\text{V}$ or $2.0\text{V}$ (use 74HC00 or 74LVC00 for low-voltage supplies).
- **Leaving unused gate inputs floating:** Unconnected CMOS inputs float, generating internal shoot-through currents and sporadic output toggling. Tie unused input pins to $V_{CC}$ or $GND$.
- **Confusing 74HC00 with 74HCT00 for 3.3V logic translation:** A standard 74HC00 powered by 5V requires $V_{IH} \ge 3.15\text{V}$, which provides negligible margin for 3.3V signals. Always specify **74HCT00** when driving from 3.3V microcontrollers into 5V logic.

## Notes

- **Pin-Compatible Replacements:** 74HC00, 74LS00, 74ALS00, SN74HCT00N, CD74HCT00.
