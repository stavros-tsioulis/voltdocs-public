## Overview

The **LM337** (LM337T) is a 3-terminal adjustable negative linear voltage regulator manufactured by Texas Instruments, ON Semiconductor, and STMicroelectronics. Capable of supplying continuous load currents up to **$1.5\text{ Amps}$** over an adjustable output voltage range of **$-1.25\text{V}$ to $-37\text{V}$**, it is the negative-voltage complement to the famous **LM317** positive regulator.

Widely used in dual symmetrical bench power supplies ($\pm 15\text{V}$, $\pm 12\text{V}$), op-amp rail supplies, audio preamplifiers, and analog active crossover networks, the LM337 requires only two external resistors to program the output voltage.

## Quick reference

| | |
|---|---|
| **Regulator Type** | 3-Terminal Adjustable Negative Linear Regulator |
| **Output Voltage Range ($V_{OUT}$)**| $-1.25\text{ V}$ to $-37.0\text{ V}$ DC |
| **Input-to-Output Differential** | $-3.0\text{ V}$ to $-40.0\text{ V}$ DC ($V_{IN} - V_{OUT}$) |
| **Continuous Output Current ($I_{OUT}$)**| Up to $1.5\text{ A}$ (with adequate heatsinking) |
| **Reference Voltage ($V_{REF}$)** | $-1.25\text{ V}$ (between `ADJ` and `OUT` pins) |
| **Line / Load Regulation** | $0.01\%/\text{V}$ line regulation, $0.3\%$ load regulation |
| **Package** | TO-220AB (LM337T) / TO-3 (LM337K) / SOT-223 |

## Pinout (TO-220AB Package — LM337T)

Looking at the **front labeled face** of the TO-220 package with leads pointing down:

```
        ┌─────────────┐
        │   O   [TAB] │  (Metal Mounting Tab = INPUT V_IN)
        ├─────────────┤
        │   LM337T    │  (Front Package Face)
        └─┬───┬───┬───┘
          1   2   3
         ADJ  IN OUT
```

| Pin | Name | Description |
|---|---|---|
| 1 | `ADJUST` (`ADJ`) | Adjustment Input (Resistor divider junction) |
| 2 | `INPUT` (`IN`) | Unregulated Negative DC Input Voltage (Tab is connected to IN!) |
| 3 | `OUTPUT` (`OUT`) | Regulated Negative DC Output Voltage |

> [!WARNING]
> Pinout Warning: LM337 vs LM317 Pinout Difference!
> - **LM337 (TO-220):** Pin 1 = `ADJ`, Pin 2 = `IN`, Pin 3 = `OUT` (**ADJ - IN - OUT**).
> - **LM317 (TO-220):** Pin 1 = `ADJ`, Pin 2 = `OUT`, Pin 3 = `IN` (**ADJ - OUT - IN**).
> - The middle pin on LM337 is **`INPUT`**, whereas on LM317 the middle pin is **`OUTPUT`**!

## Output Voltage Formula

The output voltage is set by resistor $R_1$ (typically $120\ \Omega$ to $240\ \Omega$) between `OUT` and `ADJ`, and resistor $R_2$ between `ADJ` and Ground:

$$ V_{OUT} = -1.25\text{V} \times \left(1 + \frac{R_2}{R_1}\right) + (I_{ADJ} \times R_2) $$

For $R_1 = 120\ \Omega$ and $R_2 = 1.3\text{ k}\Omega \implies V_{OUT} \approx -15.0\text{ Volts}$.

## Common mistakes

- **Reversing LM337 and LM317 pinouts:** Swapping LM337 and LM317 into identical footprint slots causes wrong connections on Pins 2 and 3.
- **Shorting metal tab to ground:** The metal tab of the TO-220 package is internally connected to **`INPUT`** (negative supply rail), NOT ground. When mounting both LM317 (tab is `OUT`) and LM337 (tab is `IN`) onto a shared metal heatsink, isolate both tabs with mica washers.
- **Omitting tantalum output capacitor:** Tantalum or low-ESR ceramic capacitors ($1.0\ \mu\text{F}$ on output, $10\ \mu\text{F}$ on $V_{IN}$) are required to prevent high-frequency oscillation.

## Notes

- **LM337 vs LM7915:** LM337 is an adjustable negative regulator; LM7915 is a fixed $-15\text{V}$ negative regulator. LM337 provides higher ripple rejection ($77\text{ dB}$) when an adjustment bypass capacitor is used.
