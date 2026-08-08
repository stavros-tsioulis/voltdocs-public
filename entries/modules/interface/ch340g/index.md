## Overview

The CH340G is a popular, low-cost USB-to-UART bridge IC produced by Nanjing Qinheng Microelectronics (WCH). It provides a full-duplex asynchronous serial UART interface with hardware modem control signals (RTS, CTS, DTR, DSR, DCD, RI) over a USB 2.0 Full-Speed (12 Mbps) physical layer.

Widely adopted across open-source hardware, budget microcontroller development boards (including Arduino Uno/Nano clones, ESP8266 NodeMCU, and ESP32 dev boards), and standalone USB-to-TTL serial adapters, the CH340G offers a direct replacement for FT232R and CP2102 ICs at a fraction of the cost. The CH340G variant operates with an external 12 MHz crystal resonator and features built-in 3.3V power regulator for internal transceiver logic.

## Quick reference

| | |
|---|---|
| **Function** | USB 2.0 to Full-Duplex UART Serial Bridge |
| **Supply range** | 3.3 V to 5.0 V DC |
| **Baud rate** | 50 bps to 2,000,000 bps (2 Mbps) |
| **Required oscillator** | 12.000 MHz Crystal / Ceramic Resonator |
| **Packages** | SOP-16 (150 mil width) |
| **Logic level** | 5 V TTL or 3.3 V CMOS |

## Pin configuration

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` | Power | Ground connection (0 V) |
| 2 | `TXD` | Output | Transmit Data output (UART serial output to MCU RXD) |
| 3 | `RXD` | Input | Receive Data input (UART serial input from MCU TXD, 5V tolerant) |
| 4 | `V3` | Power | 3.3V Internal Regulator Bypass. Connect to VCC for 3.3V mode; connect 100nF cap to GND in 5V mode |
| 5 | `UD+` | I/O | USB D+ Differential Signal Line |
| 6 | `UD-` | I/O | USB D- Differential Signal Line |
| 7 | `XI` | Input | 12 MHz Crystal Oscillator Input |
| 8 | `XO` | Output | 12 MHz Crystal Oscillator Output |
| 9 | `CTS#` | Input | Clear To Send modem control input (active low) |
| 10 | `DSR#` | Input | Data Set Ready modem control input (active low) |
| 11 | `RI#` | Input | Ring Indicator modem control input (active low) |
| 12 | `DCD#` | Input | Data Carrier Detect modem control input (active low) |
| 13 | `DTR#` | Output | Data Terminal Ready modem control output (active low, used for auto-reset) |
| 14 | `RTS#` | Output | Request To Send modem control output (active low) |
| 15 | `RS232` | Input | Auxiliary control pin (tie low for normal UART mode) |
| 16 | `VCC` | Power | Positive power supply input (3.3V or 5.0V) |

## Functional description

The CH340G contains a USB Function Controller, USB Transceiver, Serial Engine (SIE), FIFO Buffer, and Baud Rate Generator. On the USB side, it enumerates as a standard USB Communication Device Class (CDC) or proprietary WCH Serial COM Port.

On the UART side, the baud rate generator derives precision serial clocks from the external 12 MHz crystal input across standard baud rates (300, 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200, 230400, 460800, 921600, up to 2 Mbps). It supports 5, 6, 7, or 8 data bits, odd/even/mark/space/no parity, and 1 or 2 stop bits.

When `VCC` is supplied with 5.0V, an internal LDO generates a 3.3V reference on the `V3` pin, which requires a 100 nF decoupling capacitor to ground. When operating natively on a 3.3V supply, `V3` must be connected directly to `VCC`.

## Absolute maximum ratings

> [!WARNING] Stresses beyond these values cause permanent damage. These are limits, not operating conditions.

| Parameter | Rating | Unit |
|---|---|---|
| Supply Voltage (`VCC`) | -0.5 to +6.0 | V |
| Input Voltage (`RXD`, `CTS#`, `DSR#`, `RI#`, `DCD#`) | -0.5 to `VCC` + 0.5 | V |
| Operating Ambient Temperature | -40 to +85 | °C |
| Storage Temperature | -55 to +125 | °C |

## Electrical characteristics

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (5V Mode) | `VCC` | 4.5 | 5.0 | 5.3 | V | Standard 5V USB Bus |
| Supply Voltage (3.3V Mode)| `VCC` | 3.0 | 3.3 | 3.6 | V | Direct 3.3V VCC Mode |
| Operating Current | `ICC` | 4 | 12 | 20 | mA | Active UART transmission |
| Standby Current | `ISB` | 50 | 150 | 250 | µA | USB Suspend mode |
| High-Level Output Voltage | `VOH` | `VCC` - 0.5 | — | — | V | `IOH` = -4 mA (`TXD`, `DTR#`, `RTS#`) |
| Low-Level Output Voltage | `VOL` | — | — | 0.5 | V | `IOL` = 4 mA |
| Input High Voltage | `VIH` | 2.0 | — | `VCC` + 0.5 | V | 5V TTL compatible |
| Input Low Voltage | `VIL` | -0.5 | — | 0.8 | V | |

## Typical application

```
          +5V USB VBUS
               |
        +------+------+
        |             |
     100nF          10uF
        |             |
       GND           GND
        |             |
        +------+------+----------+
               |                 |
            +--+-----------------+--+
            | 16                4   |
            | VCC              V3   |
            |                       |
 USB D+ ----| 5 UD+                 |
 USB D- ----| 6 UD-        TXD  2 --+---> MCU RXD (5V or 3.3V)
            |                       |
  12MHz     | 7 XI         RXD  3 --+<--- MCU TXD
  +--[X1]---| 8 XO                  |
  |    |    |             DTR# 13 --+---> [100nF Cap] ---> MCU RESET
 22pF 22pF  |             GND   1   |
  |    |    +---------------+-------+
 GND  GND                   |
                           GND
```

## Common mistakes

- **Missing 100 nF capacitor on `V3` in 5V mode:** If `V3` is left floating without a decoupling capacitor when powered from 5V, internal logic becomes unstable causing random USB disconnects or dropped serial bytes.
- **Floating `V3` when using 3.3V `VCC`:** In 3.3V operation, `V3` MUST be connected directly to `VCC`. Leaving it disconnected will cause the internal transceivers to fail to operate.
- **Incorrect Crystal Load Capacitors:** The CH340G requires a 12.000 MHz crystal with two 22 pF load capacitors to ground. Omitting these caps or using a different crystal frequency (e.g. 16 MHz) will cause incorrect baud rates or USB enumeration failure.
- **TXD/RXD Line Swap:** Remember that CH340G `TXD` connects to the target MCU's `RXD`, and CH340G `RXD` connects to the MCU's `TXD`.

## Notes & further reading

- Driver support: WCH provides official signed drivers for Windows (CH341SER.EXE), macOS, Linux (included in kernel 2.6.24+ as `ch341`), and Android.
- `DTR#` Auto-Reset Circuit: Arduino boards place a 100 nF series capacitor between CH340G `DTR#` pin and the ATmega328P `RESET#` pin with a 10 kΩ pull-up to generate a low pulse when the IDE opens the serial port.
