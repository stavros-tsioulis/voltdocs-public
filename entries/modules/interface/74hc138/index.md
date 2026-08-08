## Overview

The **74HC138** (SN74HC138) is a 3-to-8 line decoder/demultiplexer IC manufactured using high-speed silicon-gate CMOS technology. Designed for memory address decoding and routing applications in high-speed microcomputer systems, it converts a 3-bit binary address input (`A0`, `A1`, `A2`) into one of **8 mutually exclusive active-LOW outputs** ($\overline{Y0}$ to $\overline{Y7}$).

The device incorporates three enable inputs: one active-HIGH (`G1`) and two active-LOW ($\overline{G2A}$ and $\overline{G2B}$). All 8 outputs remain HIGH (disabled) unless `G1` is HIGH and both $\overline{G2A}$ and $\overline{G2B}$ are LOW. This versatile enable arrangement allows easy cascading to build 1-of-16, 1-of-32, or larger decoders without external logic gates.

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | 2.0 V to 6.0 V DC |
| **Logic Family** | High-Speed CMOS (74HC) / TTL Compatible (74HCT) |
| **Address Inputs** | 3 (`A0` LSB, `A1`, `A2` MSB) |
| **Decoded Outputs** | 8 Active-Low Outputs ($\overline{Y0}$ through $\overline{Y7}$) |
| **Enable Lines** | 3 (`G1` Active-High; $\overline{G2A}, \overline{G2B}$ Active-Low) |
| **Propagation Delay** | $15\text{ ns}$ typical at $VCC = 4.5\text{V}$ |
| **Package** | 16-pin DIP / SOIC-16 / TSSOP-16 |

## Pinout (DIP-16 Package)

```
             ┌───┴───┐
          A0 1│ 1   16│ VCC
          A1 2│       │15 /Y0
          A2 3│       │14 /Y1
        /G2A 4│74HC138│13 /Y2
        /G2B 5│       │12 /Y3
          G1 6│       │11 /Y4
         /Y7 7│       │10 /Y5
         GND 8│       │9  /Y6
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `A0` | Input | Address Input Bit 0 (LSB) |
| 2 | `A1` | Input | Address Input Bit 1 |
| 3 | `A2` | Input | Address Input Bit 2 (MSB) |
| 4 | `/G2A` | Input | Active-Low Enable Input A |
| 5 | `/G2B` | Input | Active-Low Enable Input B |
| 6 | `G1` | Input | Active-High Enable Input |
| 7 | `/Y7` | Output | Active-Low Decoded Output 7 (Selected when A2=1, A1=1, A0=1) |
| 8 | `GND` | Power | Ground reference (0 V) |
| 9–15 | `/Y6`–`/Y0`| Output | Active-Low Decoded Outputs 6 through 0 |
| 16 | `VCC` | Power | Positive supply power pin (+2.0V to +6.0V DC) |

## Function & Truth Table

| | Enable Inputs | | Address Inputs | | | | Active Output (LOW) |
|---|---|---|---|---|---|---|---|
| **G1** | **/G2A** | **/G2B** | **A2** | **A1** | **A0** | |
| Low ($L$) | X | X | X | X | X | None (All outputs HIGH) |
| X | High ($H$) | X | X | X | X | None (All outputs HIGH) |
| X | X | High ($H$) | X | X | X | None (All outputs HIGH) |
| High ($H$) | Low ($L$) | Low ($L$) | Low ($L$) | Low ($L$) | Low ($L$) | $\overline{Y0} = 0$ |
| High ($H$) | Low ($L$) | Low ($L$) | Low ($L$) | Low ($L$) | High ($H$) | $\overline{Y1} = 0$ |
| High ($H$) | Low ($L$) | Low ($L$) | Low ($L$) | High ($H$) | Low ($L$) | $\overline{Y2} = 0$ |
| High ($H$) | Low ($L$) | Low ($L$) | Low ($L$) | High ($H$) | High ($H$) | $\overline{Y3} = 0$ |
| High ($H$) | Low ($L$) | Low ($L$) | High ($H$) | Low ($L$) | Low ($L$) | $\overline{Y4} = 0$ |
| High ($H$) | Low ($L$) | Low ($L$) | High ($H$) | Low ($L$) | High ($H$) | $\overline{Y5} = 0$ |
| High ($H$) | Low ($L$) | Low ($L$) | High ($H$) | High ($H$) | Low ($L$) | $\overline{Y6} = 0$ |
| High ($H$) | Low ($L$) | Low ($L$) | High ($H$) | High ($H$) | High ($H$) | $\overline{Y7} = 0$ |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.0 | 5.0 | 6.0 | V | DC |
| High-Level Input Voltage | $V_{IH}$ | 3.15 | — | — | V | $V_{CC} = 4.5\text{V}$ |
| Low-Level Input Voltage | $V_{IL}$ | — | — | 1.35 | V | $V_{CC} = 4.5\text{V}$ |
| Propagation Delay ($An \rightarrow \overline{Yn}$) | $t_{PD}$ | — | 15 | 25 | ns | $V_{CC} = 4.5\text{V}, C_L = 50\text{pF}$ |
| Output Sink/Source Current | $I_{OUT}$ | — | — | $\pm 25$ | mA | $V_{CC} = 6.0\text{V}$ |
| Quiescent Supply Current | $I_{CC}$ | — | — | 4.0 | µA | $V_{IN} = V_{CC}\text{ or GND}$ |

## Typical Applications

### 8-Device SPI Chip-Select Address Decoder

Using 3 GPIO pins from a microcontroller to generate 8 active-LOW Chip-Select ($\overline{CS}$) lines for peripheral devices (SD cards, sensors, displays).

```
   MCU GPIO Pins                                    SPI Peripherals
  [Pin D2] ──────────► [Pin 1: A0]             [ /Y0 ] ───► /CS SD Card
  [Pin D3] ──────────► [Pin 2: A1]  74HC138    [ /Y1 ] ───► /CS Display
  [Pin D4] ──────────► [Pin 3: A2]             [ /Y2 ] ───► /CS Flash Memory
                           │                   [ /Y3..7 ] ─► /CS Sensors
                 +5V ──[Pin 6: G1]
                 GND ──[Pin 4: /G2A]
                 GND ──[Pin 5: /G2B]
```

## Common mistakes

- **Forgetting that outputs are active-LOW:** The selected output pin pulls **LOW ($0\text{V}$)** while all non-selected outputs remain **HIGH ($5\text{V}$)**. If driving active-HIGH chip selects, an inverter (such as 74HC04) or a 74HC238 (active-HIGH equivalent) is required.
- **Floating enable lines ($\overline{G2A}, \overline{G2B}, G1$):** If $G1$ is not tied HIGH or $\overline{G2A}/\overline{G2B}$ are not tied LOW, all outputs will remain permanently disabled (HIGH).
- **Cascading incorrectly:** When cascading two 74HC138s to make a 1-of-16 decoder, use the 4th address bit ($A3$) directly to drive $G1$ on the second IC and $\overline{G2A}$ on the first IC.

## Notes

- **74HC138 vs 74HC238:** 74HC138 has active-LOW outputs ($\overline{Y0}$–$\overline{Y7}$); 74HC238 is the exact same pinout but with active-HIGH outputs ($Y0$–$Y7$).
- **74HC138 vs 74HC154:** 74HC138 is a 3-to-8 decoder (16-pin DIP); 74HC154 is a 4-to-16 decoder (24-pin DIP).
