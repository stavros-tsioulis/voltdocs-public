## Overview

The **CD4553** (CD4553B) is a 3-digit BCD counter IC manufactured by Texas Instruments and ON Semiconductor. It contains three cascaded BCD counters, an internal quad 4-bit latch, and a multiplexing circuit that outputs the 4-bit BCD data of each digit sequentially over a single 4-bit bus (`Q0`–`Q3`) alongside three active-LOW digit select outputs ($\overline{DS1}, \overline{DS2}, \overline{DS3}$).

Operating from **3.0V to 18.0V DC**, the CD4553 is designed to drive 3-digit 7-segment LED displays when paired with a single BCD-to-7-segment decoder IC (such as the CD4511), dramatically reducing pin count in digital event counters, frequency meters, and digital panel meters.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VDD - VSS`)** | 3.0 V to 18.0 V DC |
| **Digits** | 3 Synchronous BCD Counter Digits (0 to 999 count capacity) |
| **Output Bus** | 4-Bit Time-Multiplexed BCD Bus (`Q0`, `Q1`, `Q2`, `Q3`) |
| **Digit Selection** | 3 Active-LOW Digit Select Lines ($\overline{DS1}, \overline{DS2}, \overline{DS3}$) |
| **Clock Frequency** | Up to $6.0\text{ MHz}$ at $VDD = 15\text{V}$ ($2.5\text{ MHz}$ at $5\text{V}$) |
| **Latch Memory** | Integrated 4-bit quad storage latches for display freezing |
| **Package** | 16-pin DIP / SOIC-16 |

## Pinout (DIP-16 Package)

```
             ┌───┴───┐
        C1A 1│ 1   16│ VDD (+3V to +18V)
        C1B 2│       │15 CLK (Clock Input)
        DIS 3│ CD4553│14 /DS3 (Digit 3 Select)
        C2A 4│       │13 /DS2 (Digit 2 Select)
        C2B 5│       │12 /DS1 (Digit 1 Select)
         LE 6│       │11 Q2 (BCD Bit 2)
         Q3 7│       │10 Q1 (BCD Bit 1)
   VSS(GND) 8│       │9  Q0 (BCD Bit 0)
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1, 2 | `C1A, C1B` | Input | Scan Oscillator Timing Capacitor Pins (Connect external capacitor) |
| 3 | `DIS` | Input | Disable / Reset Control Input (High = Reset counter to 000) |
| 4, 5 | `C2A, C2B` | Input | Secondary Timing Capacitor Pins |
| 6 | `LE` | Input | Latch Enable Input (High = Freeze display value; Low = Pass-through) |
| 7 | `Q3` | Output | Multiplexed BCD Output Bit 3 (MSB) |
| 8 | `VSS` | Power | Digital Ground (0 V) |
| 9 | `Q0` | Output | Multiplexed BCD Output Bit 0 (LSB) |
| 10 | `Q1` | Output | Multiplexed BCD Output Bit 1 |
| 11 | `Q2` | Output | Multiplexed BCD Output Bit 2 |
| 12 | `\DS1` | Output | Active-LOW Digit 1 (LSD) Select Output |
| 13 | `\DS2` | Output | Active-LOW Digit 2 Select Output |
| 14 | `\DS3` | Output | Active-LOW Digit 3 (MSD) Select Output |
| 15 | `CLK` | Input | Master Clock Input (Positive edge triggered) |
| 16 | `VDD` | Power | Positive Power Supply (+3.0V to +18.0V DC) |

## Multi-Digit Display Interface with CD4511 Decoder

```
   CD4553 Counter                  CD4511 Decoder               3-Digit 7-Seg LED Display
  ┌──────────────┐                ┌──────────────┐             ┌─────────────────────────┐
  │ Q0,Q1,Q2,Q3  ├───────────────►│ A, B, C, D   │             │   Common-Cathode LEDs   │
  │ (BCD Bus)    │                │ a,b,c,d,e,f,g├────────────►│ a,b,c,d,e,f,g (Parallel)│
  │              │                └──────────────┘             └─────────────────────────┘
  │ /DS1,/DS2,/DS3├───[PNP Transistors (BC557)]───────────────► Digits 1, 2, 3 Cathodes
  └──────────────┘
```

## Common mistakes

- **Leaving Latch Enable (`LE`, Pin 6) floating:** `LE` must be tied directly to **GND** for normal real-time counting. Leaving `LE` floating freezes the displayed value indefinitely.
- **Forgetting PNP driver transistors on Digit Select lines:** $\overline{DS1}, \overline{DS2}, \overline{DS3}$ are active-LOW logic signals designed to drive base leads of PNP transistors (like 2SA1015 or BC327) that switch high-side digit power in multiplexed displays.

## Notes

- **CD4553 vs 74HC393:** CD4553 provides 3 full BCD digits with built-in multiplexer logic; 74HC393 is a raw dual 4-bit binary counter requiring external multiplexing.
