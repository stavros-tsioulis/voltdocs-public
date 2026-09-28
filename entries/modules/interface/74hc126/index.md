## Overview

The **74HC126** (such as the `SN74HC126N` or `74HC126D`) is a high-speed CMOS logic device providing four independent non-inverting buffer / line drivers with 3-state outputs in a standard 14-pin DIP or SOIC package.

The 74HC126 is the direct companion IC to the ubiquitous 74HC125. The essential difference lies in the polarity of the output enable pins:
- **74HC125:** Uses **active-LOW** output enables ($\overline{\text{OE}}$). Low = buffer enabled, High = high-impedance (Hi-Z).
- **74HC126:** Uses **active-HIGH** output enables (`OE`). High = buffer enabled ($Y = A$), Low = high-impedance (Hi-Z).

This active-HIGH control structure makes the 74HC126 particularly convenient in positive-logic control systems, address-decode lines, data selectors, and microcontroller GPIO buses where asserting a pin High enables a peripheral line without requiring external inverting gates.

Operating across a wide supply voltage range from $2.0\text{ V}$ to $6.0\text{ V}$ DC (or fixed $5.0\text{ V}$ with TTL-compatible input levels in the `74HCT126` variant), the outputs can source or sink up to $6\text{ mA}$ at $4.5\text{ V}$, driving up to 15 standard LSTTL loads.

## Quick reference

| Parameter | Value | Notes |
|---|---|---|
| **Logic Family** | High-Speed CMOS (74HC) | 74HCT variant available for TTL thresholds |
| **Supply Voltage Range ($V_{CC}$)** | $2.0\text{ V}$ to $6.0\text{ V}$ DC | $4.5\text{ V}$ to $5.5\text{ V}$ for 74HCT |
| **Number of Channels** | 4 independent buffer gates | Individual active-HIGH enables |
| **Propagation Delay ($t_{pd}$)** | $11\text{ ns}$ typical at $4.5\text{ V}$ | Fast high-bandwidth line driving |
| **Output Drive Current ($I_{OUT}$)** | $\pm 6.0\text{ mA}$ at $4.5\text{ V}$ | Drives 15 LSTTL loads |
| **3-State Off Leakage ($I_{OZ}$)** | $\pm 0.5\ \mu\text{A}$ maximum | High-Z bus disconnection |
| **Operating Temperature** | $-40^\circ\text{C}$ to $+125^\circ\text{C}$ | Industrial range |
| **Package** | 14-pin DIP / SOIC-14 / TSSOP-14 | Standard logic footprint |

## Terminals

```
            +---+--+---+
      1OE -| 1   14 |-- VCC
       1A -| 2   13 |-- 4OE
       1Y -| 3   12 |-- 4A
      2OE -| 4   11 |-- 4Y
       2A -| 5   10 |-- 3OE
       2Y -| 6    9 |-- 3A
      GND -| 7    8 |-- 3Y
            +----------+
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `1OE` | Digital Input | Gate 1 Active-HIGH Output Enable. High = Enabled, Low = Hi-Z. |
| 2 | `1A` | Digital Input | Gate 1 Data Input. |
| 3 | `1Y` | Digital Output | Gate 1 3-State Output. |
| 4 | `2OE` | Digital Input | Gate 2 Active-HIGH Output Enable. |
| 5 | `2A` | Digital Input | Gate 2 Data Input. |
| 6 | `2Y` | Digital Output | Gate 2 3-State Output. |
| 7 | `GND` | Ground | Common ground reference ($0\text{ V}$). |
| 8 | `3Y` | Digital Output | Gate 3 3-State Output. |
| 9 | `3A` | Digital Input | Gate 3 Data Input. |
| 10 | `3OE` | Digital Input | Gate 3 Active-HIGH Output Enable. |
| 11 | `4Y` | Digital Output | Gate 4 3-State Output. |
| 12 | `4A` | Digital Input | Gate 4 Data Input. |
| 13 | `4OE` | Digital Input | Gate 4 Active-HIGH Output Enable. |
| 14 | `VCC` | Power | Positive DC supply rail ($+2.0\text{ V}$ to $+6.0\text{ V}$ DC). |

## The technical core

### Function truth table (each buffer gate)

| Output Enable (`OE`) | Data Input (`A`) | Output (`Y`) | Operational State |
|---|---|---|---|
| **High ($H$)** | Low ($L$) | **Low ($L$)** | Non-inverting buffer drive |
| **High ($H$)** | High ($H$) | **High ($H$)** | Non-inverting buffer drive |
| **Low ($L$)** | $X$ (Don't Care) | **High-Z ($Z$)** | High-impedance isolation |

### Electrical specifications (74HC126 at $25^\circ\text{C}$)

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.0 | 5.0 | 6.0 | V | Operating range |
| High-Level Input Voltage | $V_{IH}$ | 3.15 | — | — | V | $V_{CC} = 4.5\text{ V}$ |
| Low-Level Input Voltage | $V_{IL}$ | — | — | 1.35 | V | $V_{CC} = 4.5\text{ V}$ |
| High-Level Output Voltage | $V_{OH}$ | 3.84 | 4.2 | — | V | $V_{CC} = 4.5\text{ V}$, $I_{OH} = -6.0\text{ mA}$ |
| Low-Level Output Voltage | $V_{OL}$ | — | 0.17 | 0.33 | V | $V_{CC} = 4.5\text{ V}$, $I_{OL} = 6.0\text{ mA}$ |
| Propagation Delay ($A \to Y$) | $t_{pd}$ | — | 11 | 18 | ns | $V_{CC} = 4.5\text{ V}$, $C_L = 50\text{ pF}$ |
| 3-State Enable Time ($OE \to Y$)| $t_{en}$ | — | 14 | 25 | ns | $V_{CC} = 4.5\text{ V}$, $C_L = 50\text{ pF}$ |
| 3-State Disable Time ($OE \to Y$)| $t_{dis}$ | — | 14 | 25 | ns | $V_{CC} = 4.5\text{ V}$, $C_L = 50\text{ pF}$ |
| 3-State Leakage Current | $I_{OZ}$ | — | — | $\pm 0.5$ | µA | $V_{OUT} = V_{CC}$ or $GND$ |

## Usage

### 2-to-1 digital bus multiplexer circuit

Using two gates of a 74HC126 to select between two digital data streams (`Data A` and `Data B`) sharing a single output line:

```
                  +5V
                   |
                +--+---+
                | VCC  |
  Data A -------| 1A 1Y|----------------+------> Selected Data Output
                |      |                |
  Sel (High=A) -| 1OE  |                |
                |      |                |
  Data B -------| 2A 2Y|----------------+
                |      |
  Inv Sel ------| 2OE  |  (Inv Sel = NOT Sel via small inverter or transistor)
                | GND  |
                +--+---+
                   |
                  GND
```

When `Sel` is High:
- Gate 1 is enabled (`1OE` = High), transmitting `Data A` to the output line.
- Gate 2 is disabled (`2OE` = Low), placing `2Y` into high-impedance mode (Hi-Z) so it does not interfere with `Data A`.

## Common mistakes

- **Confusing enable polarity with 74HC125:** The 74HC126 requires a logic High on the enable pin to transmit data. Designers accustomed to the 74HC125 (active-LOW) will find that tying enable to ground completely mutes all outputs into Hi-Z.
- **Floating unused inputs:** CMOS inputs must never be left floating. Unconnected inputs float into the threshold linear region ($V_{CC}/2$), causing internal cross-conduction shoot-through current and erratic power draw. Tie unused inputs to $V_{CC}$ or ground.
- **Directly shorting two active outputs:** When building a multi-transmitter bus, ensure that two enable pins are never asserted High simultaneously with opposite logic levels. This creates a hard short circuit between $V_{CC}$ and $GND$ through the internal output stages.

## Notes

- **74HC126 vs 74HC125:** Choose the **74HC125** when driving buses governed by active-low chip select signals (such as SPI $\overline{\text{CS}}$ or memory select lines). Choose the **74HC126** when bus drivers are controlled by active-high microcontroller GPIO pins or positive-logic decode strobes.
