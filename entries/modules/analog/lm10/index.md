## Overview

The **LM10** (LM10CLN / LM10CN) is a landmark monolithic integrated circuit designed by legendary analog IC pioneer **Bob Widlar** for National Semiconductor (now Texas Instruments). Housed in an 8-pin through-hole **DIP-8** and **TO-99 metal can** package, it combines an independent high-gain operational amplifier with a dedicated adjustable **$200\text{ mV}$ precision voltage reference** on a single chip.

The defining breakthrough of the LM10 is its extraordinary operating voltage envelope: it can operate reliably from a single supply as low as **$1.1\text{V}$ DC** (a single depleted NiCd, NiMH, or alkaline battery cell) up to **$40.0\text{V}$ DC** (or $\pm 0.55\text{V} \dots \pm 20\text{V}$ split supplies) while drawing just **$270\ \mu\text{A}$** of quiescent current. With its common-mode input range extending to the negative rail ($V^-$) and an integrated reference buffer amplifier, the LM10 is renowned for **2-wire 4–20mA industrial current loop transmitters, floating battery monitors, low-voltage precision sensor amplifiers, and micropower linear voltage regulators**.

## Quick reference

| | |
|---|---|
| **Amplifier Type** | Precision Low-Voltage Op-Amp with Integrated Voltage Reference |
| **Package** | 8-pin DIP (DIP-8 / PDIP-8) / SOIC-8 / TO-99 Metal Can |
| **Supply Voltage Range ($V_S$)** | **$1.1\text{ V}$ to $40.0\text{ V}$** (or $\pm 0.55\text{V} \dots \pm 20\text{V}$) |
| **Quiescent Supply Current ($I_S$)**| **$270\ \mu\text{A}$ typ** ($400\ \mu\text{A}$ max) |
| **Built-in Precision Reference** | **$200\text{ mV}$** ($\pm 1\%$ initial accuracy) |
| **Reference Line Regulation** | **$0.002\% / \text{V}$** |
| **Op-Amp Input Offset Voltage**| **$2.0\text{ mV}$ typ** ($4.0\text{ mV}$ max) |
| **Op-Amp Output Drive Capability**| **$\pm 20\text{ mA}$** (Can drive LEDs and small relays directly) |
| **Common-Mode Input Range** | Includes negative rail ($V^-$) |

## Pinout (DIP-8 Package)

```
                            ┌───┴───┐
     (200mV Ref Out) REF OUT 1│ 1   8│ REF FEEDBACK (Ref Amp Feedback)
     (Op-Amp Invert)     -IN 2│ LM10│7│ V+ (+1.1V to +40V Supply)
     (Op-Amp Non-Inv)    +IN 3│     │6│ OUT (Op-Amp Output)
     (Negative / GND)     V- 4│DIP-8│5│ BALANCE (Offset Null)
                            └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `REF OUT` | Reference Output | $200\text{ mV}$ internal bandgap reference output |
| 2 | `-IN` | Analog Input | Operational amplifier inverting input |
| 3 | `+IN` | Analog Input | Operational amplifier non-inverting input |
| 4 | `V-` | Power | Negative power supply rail (or circuit Ground / $0\text{ V}$) |
| 5 | `BALANCE` | Analog Input | Input offset voltage balance / null adjustment |
| 6 | `OUT` | Analog Output | Operational amplifier output (Sinks/sources up to $20\text{ mA}$) |
| 7 | `V+` | Power | Positive power supply rail ($+1.1\text{ V}$ to $+40.0\text{ V}$) |
| 8 | `REF FEEDBACK`| Analog Input | Reference buffer amplifier feedback terminal |

## Typical Application: 1.2V Single-Cell Battery Low-Voltage Monitor

Because the LM10 operates down to $1.1\text{V}$, it can accurately monitor a 1.2V / 1.5V battery cell without requiring any charge pumps or boost converters:

```
  +1.2V Single Battery Cell (V+) ────────────────────────┬─────────┐
                                                         │         │
                                                   [Pin 7: V+]     │
                                                      LM10         │
  [ 200mV Ref Out: Pin 1 ] ───► [Pin 3: +IN]                       │
                                                      │            │
  Battery Voltage Divider ────► [Pin 2: -IN]                       │
  (R1 = 100kΩ, R2 = 20kΩ)                             │            │
                                                [Pin 6: OUT] ──► [ Red Low-Battery LED ]
                                                [Pin 4: V-]        │
                                                      │            │
  Battery Negative (0V) ──────────────────────────────┴────────────┴── Battery Return
```

## 2-Wire 4–20mA Current Transmitter

The LM10 is uniquely capable of "floating operation" where the entire circuit is powered by the loop current itself:

```
  +24V Current Loop Supply ────────────────────────┐
                                                   │
                                          [Pin 7: V+]
                                             LM10  ───► [ Output Pass Transistor (BD139) ]
  Sensor Input Signal ──► [Pin 3: +IN]             │           │
                          [Pin 1: REF OUT] ────────┤           │
                          [Pin 4: V-] ─────────────┴───────────┴──► 4-20mA Current Loop Return
```

## Common mistakes

- **Leaving Reference Feedback (Pin 8) floating:** Pin 8 is the inverting feedback input of the internal reference buffer. If using the default $200\text{ mV}$ reference, connect **Pin 8 directly to Pin 1 (REF OUT)**. If setting an amplified reference (e.g. 1.0V or 2.5V), use a resistive divider between Pin 1 and Pin 8.
- **Expecting high-speed performance:** The LM10 is optimized for micropower, low-voltage precision DC measurement, with a gain-bandwidth product of approximately **$300\text{ kHz}$**. It is not intended for high-speed audio or RF signal processing.

## Notes

- **Suffix Guide:** `LM10CLN` / `LM10CN` denotes commercial temperature range ($0^\circ\text{C} \dots 70^\circ\text{C}$) in standard plastic DIP-8; `LM10H` denotes hermetic TO-99 metal can.
