## Overview

The **TDA2003** (TDA2003V) is a 10W single-chip audio power amplifier IC manufactured by STMicroelectronics. Enclosed in a **5-lead Pentawatt package** (TO-220-5 style), it was developed as an improved drop-in replacement for the classic TDA2002 in car radios, CB transceivers, and 12V battery-powered portable PA systems.

Operating on a single supply voltage from **8.0V to 18.0V DC** (14.4V nominal car battery voltage), the TDA2003 delivers up to **10 Watts into a $2\ \Omega$ load** (or $6\text{W}$ into $4\ \Omega$) with high output peak current capability ($3.5\text{ A}$ continuous / $4.5\text{ A}$ peak). It features load-dump voltage surge protection (up to $40\text{V}$), thermal shutdown, and output AC/DC short-circuit protection.

## Quick reference

| | |
|---|---|
| **Amplifier Type** | Single-Supply Automotive Audio Power Amplifier |
| **Output Power** | $10\text{ W}$ into $2\ \Omega$ load / $6\text{ W}$ into $4\ \Omega$ load at $V_S = 14.4\text{V}$ |
| **Supply Voltage (`Vs`)** | 8.0 V to 18.0 V DC (Single supply) |
| **Peak Output Current** | $3.5\text{ A}$ continuous ($4.5\text{ A}$ peak) |
| **THD Distortion** | $0.15\%$ typical at $1\text{ kHz}, P_O = 0.5\text{W}, 4\ \Omega$ |
| **Quiescent Supply Current** | $44\text{ mA}$ typical ($65\text{ mA}$ max) |
| **Package** | 5-lead Pentawatt (TO-220-5 Vertical or Horizontal) |

## Pinout (5-Lead Pentawatt Package)

Looking at the **front labeled face** of the Pentawatt package with leads pointing down:

```
        ┌─────────────┐
        │   O   [TAB] │  (Metal Mounting Tab = GROUND / GND)
        ├─────────────┤
        │   TDA2003   │  (Front Package Face)
        └─┬─┬─┬─┬─┬───┘
          1 2 3 4 5
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `+IN` | Input | Non-Inverting Audio Signal Input |
| 2 | `-IN` | Input | Inverting Feedback Input |
| 3 | `GND` | Power | Ground Reference (0 V; Connected internally to Metal Tab!) |
| 4 | `OUT` | Output | Speaker Output (Single DC-decoupled output) |
| 5 | `Vs` | Power | Positive DC Power Supply (+8V to +18V DC) |

## Standard 12V Car Audio Application Circuit

```
  Audio Input ───[10µF Cap]───► [Pin 1: +IN]
                                    TDA2003
  +12V/14.4V DC Supply ───────► [Pin 5: Vs]
  Ground (GND) ───────────────► [Pin 3: GND & Metal Tab]

  [Pin 4: OUT] ───[ 1000µF Electrolytic Cap ]───► ( + ) $4\ \Omega$ Speaker
                                                  │
                                          [ 39Ω + 0.1µF Zobel to GND ]
```

## Common mistakes

- **Forgetting output DC-decoupling capacitor ($1000\ \mu\text{F}$):** Because the TDA2003 operates from a single supply rail, the output pin (Pin 4) sits at half supply voltage ($V_S / 2 \approx 7.2\text{V}$). A large $1000\ \mu\text{F}$ capacitor is mandatory in series with the speaker to block DC current.
- **Running without a heatsink at high volume:** Driving a $2\ \Omega$ or $4\ \Omega$ speaker near $10\text{W}$ generates substantial heat. Always attach the metal tab to a suitable heat sink.

## Notes

- **TDA2003 vs LM386 vs TDA2030:** LM386 produces $0.7\text{W}$; TDA2003 produces $10\text{W}$ on a single 12V supply; TDA2030 requires higher supply voltages ($>18\text{V}$ split or $30\text{V}$ single).
