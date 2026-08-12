## Overview

The **74HC393** (SN74HC393N) is a dual 4-bit binary ripple counter IC manufactured by Texas Instruments, Nexperia, and ON Semiconductor. Containing two independent 4-bit binary ripple counters in a single 14-pin package, it divides incoming clock frequencies by $2, 4, 8, 16$ (per counter channel).

Operating from **2.0V to 6.0V DC**, each counter is triggered on negative-going clock edges ($\overline{1CLK}, \overline{2CLK}$) and includes an active-HIGH asynchronous master clear pin ($1CLR, 2CLR$). By connecting the MSB output of the first stage ($1Q_D$) to the clock input of the second stage ($\overline{2CLK}$), the two 4-bit counters form a single **8-bit binary counter ($0 \dots 255$)**.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | 2.0 V to 6.0 V DC |
| **Logic Family** | High-Speed CMOS (74HC) / TTL Compatible (74HCT) |
| **Channels** | 2 Independent 4-Bit Binary Ripple Counters ($1Q_A \dots 1Q_D$ and $2Q_A \dots 2Q_D$) |
| **Cascaded Mode** | 8-Bit Binary Counter ($00000000_2 \dots 11111111_2$) |
| **Clock Input Trigger** | Negative-Edge Triggered ($\downarrow$ HIGH-to-LOW transition) |
| **Clear Input** | Asynchronous Active-HIGH Master Clear ($1CLR, 2CLR$) |
| **Clock Frequency** | Up to $40\text{ MHz}$ at $VCC = 4.5\text{V}$ |
| **Package** | 14-pin DIP / SOIC-14 / TSSOP-14 |

## Pinout (DIP-14 Package)

```
             ┌───┴───┐
       /1CLK 1│ 1   14│ VCC (+2V to +6V)
        1CLR 2│       │13 /2CLK
         1QA 3│ 74HC  │12 2CLR
         1QB 4│  393  │11 2QA
         1QC 5│       │10 2QB
         1QD 6│       │9  2QC
         GND 7│       │8  2QD
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `\1CLK` | Input | Counter 1 Clock Input (Negative-edge triggered $\downarrow$) |
| 2 | `1CLR` | Input | Counter 1 Reset Input (Active HIGH: High = Reset $1Q_A \dots 1Q_D$ to $0000_2$) |
| 3–6 | `1QA, 1QB, 1QC, 1QD` | Output | Counter 1 Binary Outputs ($1Q_A$ LSB, $1Q_D$ MSB) |
| 7 | `GND` | Power | Ground reference (0 V) |
| 8–11 | `2QD, 2QC, 2QB, 2QA` | Output | Counter 2 Binary Outputs ($2Q_A$ LSB, $2Q_D$ MSB) |
| 12 | `2CLR` | Input | Counter 2 Reset Input (Active HIGH) |
| 13 | `\2CLK` | Input | Counter 2 Clock Input (Negative-edge triggered $\downarrow$) |
| 14 | `VCC` | Power | Positive Power Supply (+2.0V to +6.0V DC) |

## 8-Bit Counter Cascading Diagram

```
  Input Clock Signal ───► [Pin 1: /1CLK]
                               74HC393 (Counter 1)
                          [Pin 6: 1QD Output] ───► [Pin 13: /2CLK Input]
                                                        74HC393 (Counter 2)
  Outputs: (LSB) 1QA 1QB 1QC 1QD 2QA 2QB 2QC 2QD (MSB)
```

## Common mistakes

- **Leaving `1CLR` or `2CLR` floating:** Clear inputs ($1CLR, 2CLR$) are active-HIGH. If left ungrounded, static noise holds the counters in reset ($0000_2$). Connect unused clear inputs directly to **GND**.
- **Assuming rising-edge clock trigger:** The 74HC393 counts on **falling clock edges** ($\downarrow$).

## Notes

- **74HC393 vs 74HC163:** 74HC393 contains two independent 4-bit ripple counters in a 14-pin package; 74HC163 is a single 4-bit presettable synchronous counter in a 16-pin package.
