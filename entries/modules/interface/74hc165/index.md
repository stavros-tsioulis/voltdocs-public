## Overview

The **74HC165** (SN74HC165A) is an 8-bit Parallel-In / Serial-Out (PISO) shift register IC manufactured by Texas Instruments, Nexperia, and ON Semiconductor. Containing eight internal D-type flip-flops, it captures eight parallel digital inputs simultaneously and shifts them out serially over a single data line.

Operating from **2.0V to 6.0V DC**, the 74HC165 is the exact inverse of the 74HC595 shift register. While the 74HC595 expands microcontroller *outputs* (e.g. driving LEDs), the 74HC165 expands microcontroller *inputs* (reading push-buttons, DIP switches, or digital sensors) using just 3 micro-controller GPIO pins.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | 2.0 V to 6.0 V DC |
| **Logic Family** | High-Speed CMOS (74HC) / TTL Compatible (74HCT) |
| **Input Channels** | 8 Parallel Input Pins ($A \dots H$ or $D_0 \dots D_7$) |
| **Serial Outputs** | Complementary outputs $Q_7$ (Pin 9) and $\overline{Q_7}$ (Pin 7) |
| **Propagation Delay** | $15\text{ ns}$ typical at $VCC = 4.5\text{V}$ |
| **Cascade Ability** | Unlimited daisy-chaining via `SER` serial input pin |
| **Package** | 16-pin DIP / SOIC-16 / TSSOP-16 |

## Pinout (DIP-16 Package)

```
             ┌───┴───┐
       SH/LD 1│ 1   16│ VCC (+2V to +6V)
         CLK 2│       │15 CLK INH (GND)
           E 3│       │14 D
           F 4│ 74HC165│13 C
           G 5│       │12 B
           H 6│       │11 A
         /Q7 7│       │10 SER (Cascade In)
         GND 8│       │9  Q7 (Serial Data Out)
             └───────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `SH/LD` | Shift / Parallel Load (Low = Latch 8 parallel inputs; High = Enable serial shift) |
| 2 | `CLK` | Clock Input (Rising edge shifts data to $Q_7$) |
| 3 | `E` | Parallel Input Bit E ($D_4$) |
| 4 | `F` | Parallel Input Bit F ($D_5$) |
| 5 | `G` | Parallel Input Bit G ($D_6$) |
| 6 | `H` | Parallel Input Bit H ($D_7$) |
| 7 | `\Q7` | Inverted Serial Data Output |
| 8 | `GND` | Ground reference (0 V) |
| 9 | `Q7` | Serial Data Output (Connect to MCU MISO / Data In) |
| 10 | `SER` | Serial Input for Daisy-Chaining (Connect to $Q_7$ of preceding 74HC165) |
| 11 | `A` | Parallel Input Bit A ($D_0$) |
| 12 | `B` | Parallel Input Bit B ($D_1$) |
| 13 | `C` | Parallel Input Bit C ($D_2$) |
| 14 | `D` | Parallel Input Bit D ($D_3$) |
| 15 | `CLK INH` | Clock Inhibit Input (Connect to GND to enable clocking) |
| 16 | `VCC` | Power supply voltage (+2.0V to +6.0V DC) |

## Function & Truth Table

| SH/LD | CLK | CLK INH | Mode / Operation |
|---|---|---|---|
| Low ($L$) | X | X | **Parallel Load:** Latches inputs $A \dots H$ into internal registers |
| High ($H$) | $\uparrow$ | Low ($L$) | **Shift:** Shifts bits toward output $Q_7$ on clock rising edge |
| High ($H$) | X | High ($H$) | **Inhibit:** Holds clock state (no shift) |

## Example (Arduino Code - Reading 8 Buttons over SPI)

```cpp
const int loadPin  = 8;  // SH/LD (Pin 1)
const int clockPin = 9;  // CLK (Pin 2)
const int dataPin  = 10; // Q7 (Pin 9)

void setup() {
  pinMode(loadPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, INPUT);
  Serial.begin(115200);
}

void loop() {
  // Latch parallel inputs (Pulse SH/LD LOW)
  digitalWrite(loadPin, LOW);
  delayMicroseconds(5);
  digitalWrite(loadPin, HIGH);

  // Read 8 bits serially
  byte incomingData = shiftIn(dataPin, clockPin, MSBFIRST);

  Serial.print("8-Button State: 0b");
  Serial.println(incomingData, BIN);
  delay(200);
}
```

## Common mistakes

- **Leaving `CLK INH` (Pin 15) floating:** Pin 15 is Clock Inhibit. If left ungrounded, static noise causes clock signals to be ignored. Tie `CLK INH` directly to **GND**.
- **Leaving unused parallel inputs ($A \dots H$) floating:** Any unused parallel input pins must be tied to $V_{CC}$ or GND with pull-up/pull-down resistors to avoid unstable bit reads.

## Notes

- **74HC165 vs 74HC595:** 74HC165 is Parallel-In Serial-Out (reads inputs); 74HC595 is Serial-In Parallel-Out (drives outputs).
