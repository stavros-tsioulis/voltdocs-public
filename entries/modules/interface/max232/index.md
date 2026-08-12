## Overview

The **MAX232** (MAX232N) is a dual RS-232 line driver and receiver IC manufactured by Texas Instruments and Maxim Integrated (Analog Devices). It converts 5V TTL/CMOS serial UART logic signals into true **EIA/TIA-232-E (RS-232)** bipolar voltage levels ($\pm 9\text{V}$) and vice versa.

Equipped with an internal **dual capacitive charge-pump voltage generator**, the MAX232 generates $+10\text{V}$ and $-10\text{V}$ power rails internally using four external $1.0\ \mu\text{F}$ capacitors, operating completely from a single **+5.0V DC** power supply. It contains two independent transmitter channels (TTL to RS-232) and two receiver channels (RS-232 to TTL).

## Quick reference

| | |
|---|---|
| **Supply Voltage (`VCC`)** | 4.5 V to 5.5 V DC (+5.0 V nominal) |
| **Data Rate** | Up to $120\text{ kbps}$ |
| **Channels** | 2 Drivers (TTL/CMOS to RS-232) & 2 Receivers (RS-232 to TTL/CMOS) |
| **Charge Pump Capacitors** | 4x $1.0\ \mu\text{F}$ electrolytic/ceramic capacitors (or 0.1µF for MAX232A) |
| **RS-232 Output Voltage Level**| $\pm 9.0\text{ V}$ typical |
| **RS-232 Input Voltage Range** | $\pm 30.0\text{ V}$ max |
| **Package** | 16-pin DIP / SOIC-16 |

## Pinout (DIP-16 Package)

```
             ┌───┴───┐
        C1+ 1│ 1   16│ VCC (+5V)
        V+  2│       │15 GND
        C1- 3│       │14 T1OUT (RS-232 Level Out)
        C2+ 4│ MAX232│13 R1IN  (RS-232 Level In)
        C2- 5│       │12 R1OUT (TTL Level Out)
        V-  6│       │11 T1IN  (TTL Level In)
      T2OUT 7│       │10 T2IN  (TTL Level In)
       R2IN 8│       │9  R2OUT (TTL Level Out)
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `C1+` | Analog | Charge pump 1 positive capacitor pin |
| 2 | `V+` | Analog Output | $+10\text{V}$ charge pump output (Requires 1.0µF capacitor to GND) |
| 3 | `C1-` | Analog | Charge pump 1 negative capacitor pin |
| 4 | `C2+` | Analog | Charge pump 2 positive capacitor pin |
| 5 | `C2-` | Analog | Charge pump 2 negative capacitor pin |
| 6 | `V-` | Analog Output | $-10\text{V}$ charge pump output (Requires 1.0µF capacitor to GND) |
| 7 | `T2OUT` | RS-232 Out | Transmitter 2 Output (Connect to RS-232 DB9 Pin 2/3) |
| 8 | `R2IN` | RS-232 In | Receiver 2 Input (Connect to RS-232 DB9 Pin 3/2) |
| 9 | `R2OUT` | TTL Out | Receiver 2 Output (Connect to MCU RXD) |
| 10 | `T2IN` | TTL In | Transmitter 2 Input (Connect to MCU TXD) |
| 11 | `T1IN` | TTL In | Transmitter 1 Input (Connect to MCU TXD) |
| 12 | `T1OUT` | RS-232 Out | Transmitter 1 Output (Connect to RS-232 DB9 Pin 2/3) |
| 13 | `R1IN` | RS-232 In | Receiver 1 Input (Connect to RS-232 DB9 Pin 3/2) |
| 14 | `R1OUT` | TTL Out | Receiver 1 Output (Connect to MCU RXD) |
| 15 | `GND` | Ground | Ground reference (0 V) |
| 16 | `VCC` | Power | Positive supply input (+5.0 V DC) |

## Wiring (Single MCU UART Channel to RS-232 DB9 Connector)

```
  Charge Pump Capacitors Setup:
  - C1: 1.0µF between Pin 1 (C1+) & Pin 3 (C1-)
  - C2: 1.0µF between Pin 4 (C2+) & Pin 5 (C2-)
  - C3: 1.0µF between Pin 2 (V+)  & VCC (+5V)
  - C4: 1.0µF between Pin 6 (V-)  & GND

  Microcontroller 5V UART              MAX232                 DB9 Male RS-232 Connector
  ┌───────────────────┐        ┌───────────────────┐        ┌─────────────────────────┐
  │   MCU TXD         ├───────►│ Pin 11: T1IN      │        │                         │
  │                   │        │ Pin 14: T1OUT     ├───────►│ Pin 2: RXD (RS-232)     │
  │   MCU RXD         │◄───────┤ Pin 12: R1OUT     │        │                         │
  │                   │        │ Pin 13: R1IN      │◄───────┤ Pin 3: TXD (RS-232)     │
  │   GND             ├───────►│ Pin 15: GND       ├───────►│ Pin 5: GND              │
  └───────────────────┘        └───────────────────┘        └─────────────────────────┘
```

## Common mistakes

- **Reversing polarity of charge pump capacitors:** Electrolytic capacitors on $V+$ (Pin 2) and $V-$ (Pin 6) must have correct polarity: Pin 2 positive to $VCC$; Pin 6 negative to GND.
- **Connecting MAX232 directly to 3.3V MCUs:** The original MAX232 requires $VCC = 5.0\text{V}$ and outputs 5V TTL logic levels on R1OUT/R2OUT. When interfacing with a 3.3V microcontroller (such as ESP32 or STM32), use the 3.3V-native **MAX3232** IC instead.

## Notes

- **MAX232 vs MAX3232:** MAX232 operates on 5.0V only and requires 1.0µF capacitors; MAX3232 operates on 3.0V to 5.5V and uses smaller 0.1µF capacitors.
