## Overview

The **74HC595** is an 8-bit serial-in, parallel-out shift register with a storage register and 3-state outputs manufactured by Texas Instruments, Nexperia, and STMicroelectronics. It allows microcontrollers to expand 3 digital output pins into 8 (or more when daisy-chained) independent digital outputs.

Containing an 8-bit D-type shift register feeding an 8-bit D-type storage (latch) register, the 74HC595 updates its parallel outputs ($Q_A$–$Q_H$) simultaneously on a latch pulse, avoiding flicker during serial shifting. It is foundational in electronics education and is widely used to drive LED bars, 7-segment displays, relay arrays, and matrix displays on Arduino and Raspberry Pi.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 2.0 V to 6.0 V DC (5.0 V nominal) |
| **Logic family** | High-Speed CMOS (74HC family) |
| **Output channels** | 8 parallel outputs ($Q_A$ through $Q_H$) + 1 serial cascade output ($Q_H'$) |
| **Max output current** | $\pm 35\text{ mA}$ per pin ($\pm 70\text{ mA}$ continuous supply total) |
| **Max clock frequency** | 25 MHz (at 4.5 V / 5.0 V) |
| **Control interface** | 3 Digital Pins: Data (`SER`), Shift Clock (`SRCLK`), Latch Clock (`RCLK`) |

## Pinout (DIP-16 Package)

```
             ┌───┴───┐
         QB ─┤ 1   16├─ VCC
         QC ─┤ 2   15├─ QA
         QD ─┤ 3   14├─ SER (DS)
         QE ─┤ 4   13├─ OE (Output Enable)
         QF ─┤ 5   12├─ RCLK (Latch)
         QG ─┤ 6   11├─ SRCLK (Clock)
         QH ─┤ 7   10├─ SRCLR (Reset)
        GND ─┤ 8    9├─ QH' (Cascade Out)
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1–7, 15 | $Q_B$–$Q_H$, $Q_A$ | Output | Parallel data outputs 0 through 7 ($Q_A$ is Bit 0, $Q_H$ is Bit 7) |
| 8 | `GND` | Power | Ground reference (0 V) |
| 9 | $Q_H'$ | Output | Serial data output for cascading to next shift register |
| 10 | `SRCLR` | Input | Active-Low Shift Register Clear (connect to $V_{CC}$ for normal operation) |
| 11 | `SRCLK` | Input | Shift Register Clock Input (rising edge shifts data) |
| 12 | `RCLK` | Input | Storage Register (Latch) Clock Input (rising edge updates parallel outputs) |
| 13 | `OE` | Input | Active-Low Output Enable (connect to `GND` to enable outputs) |
| 14 | `SER` / `DS` | Input | Serial Data Input |
| 16 | `VCC` | Power | Power supply input (+2.0 V to +6.0 V DC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.0 | 5.0 | 6.0 | V | DC |
| High-Level Input | $V_{IH}$ | 3.15 | 5.0 | $V_{CC}$ | V | $V_{CC} = 4.5\text{ V}$ |
| Low-Level Input | $V_{IL}$ | 0 | 0 | 1.35 | V | $V_{CC} = 4.5\text{ V}$ |
| Output Source/Sink Current | $I_{out}$ | -35 | — | +35 | mA | Per individual output pin |
| Supply Current Total | $I_{CC}$ | -70 | — | +70 | mA | Max total current through $V_{CC}$ / `GND` |
| Shift Frequency | $f_{MAX}$ | — | 30 | 25 | MHz | $V_{CC} = 4.5\text{ V}$ |
| Propagation Delay | $t_{pd}$ | — | 15 | 30 | ns | `SRCLK` to $Q_H'$ at 4.5 V |

## Operating Principle & Daisy-Chaining

1. **Serial Shifting:** On each rising edge of `SRCLK` (Shift Register Clock), the logic state present on `SER` (Serial Data) is shifted into Bit 0, and all previous bits shift one position right ($Q_0 \to Q_1 \dots Q_6 \to Q_7$).
2. **Latch Transfer:** On a rising edge of `RCLK` (Register Clock / Latch), the 8 bits in the internal shift register are copied into the output storage register, updating pins $Q_A$–$Q_H$ simultaneously.
3. **Daisy-Chaining:** Connect $Q_H'$ (Pin 9) of Chip 1 to `SER` (Pin 14) of Chip 2 while sharing `SRCLK` and `RCLK` across all chips. Sending 16 clock pulses shifts data across both ICs seamlessly.

## Wiring

| 74HC595 Pin | → | Arduino Uno | ESP32 | Notes |
|---|---|---|---|---|
| 16 (`VCC`) | | 5V | 3.3V | Decoupling cap $0.1\ \mu\text{F}$ required |
| 8 (`GND`)  | | GND | GND | System ground |
| 10 (`SRCLR`)| | 5V / $V_{CC}$ | 3.3V | **Tie High** to disable auto-clear |
| 13 (`OE`)   | | GND | GND | **Tie Low** to enable outputs |
| 14 (`SER`)  | | Digital D11 (Data Pin) | GPIO 23 | Serial Data |
| 12 (`RCLK`) | | Digital D8 (Latch Pin)| GPIO 5 | Storage Register Latch Clock |
| 11 (`SRCLK`)| | Digital D13 (Clock Pin)| GPIO 18 | Shift Register Clock |

## Example

```cpp
const int dataPin = 11;   // SER (Pin 14)
const int latchPin = 8;   // RCLK (Pin 12)
const int clockPin = 13;  // SRCLK (Pin 11)

void setup() {
  pinMode(latchPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
}

void loop() {
  // Light LEDs one by one in a binary counter pattern
  for (int numberToDisplay = 0; numberToDisplay < 256; numberToDisplay++) {
    digitalWrite(latchPin, LOW);
    shiftOut(dataPin, clockPin, MSBFIRST, numberToDisplay);
    digitalWrite(latchPin, HIGH);
    delay(100);
  }
}
```

## Common mistakes

- **Leaving `SRCLR` (Pin 10) floating:** If left un-connected, electrostatic noise triggers internal clears, setting all outputs to 0 randomly. Tie Pin 10 to $V_{CC}$.
- **Leaving `OE` (Pin 13) floating:** If left un-connected, outputs enter a high-impedance tri-state mode. Tie Pin 13 to `GND`.
- **Exceeding $70\text{ mA}$ total chip current:** Driving 8 LEDs at $20\text{ mA}$ each draws $160\text{ mA}$, exceeding the $70\text{ mA}$ $V_{CC}$ package limit and damaging the IC. Use current-limiting resistors ($\ge 220\ \Omega$ per LED at 5V).

## Notes

- **74HC595 vs TPIC6B595:** The TPIC6B595 is a power MOSFET variant capable of sinking up to $150\text{ mA}$ per channel at 50V for high-current solenoid/relay loads.
