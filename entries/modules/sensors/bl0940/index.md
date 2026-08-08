## Overview

The **BL0940** is a single-phase electricity metering IC manufactured by Shanghai Belling. Embedded inside Tuya, BlitzWolf, and Sonoff smart plugs and power sockets, it measures RMS voltage, RMS current, active power (W), fast power, and cumulative energy consumption over a 4,800 baud TTL UART interface.

Equipped with dual 16-bit Sigma-Delta ADCs, an internal high-precision temperature compensated voltage reference, and digital signal processing (DSP) logic, the BL0940 delivers Class 0.5 measurement accuracy across a 2000:1 dynamic range. It is natively supported by open-source firmware projects including **Tasmota**, **ESPHome**, and **OpenBK7231T**.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VDD`)** | 3.0 V to 3.6 V DC (3.3 V nominal) |
| **Interface** | TTL UART (4,800 bps, 8-N-1) |
| **Fixed UART Baud Rate** | 4,800 bps |
| **Measurement parameters** | $V_{RMS}$, $I_{RMS}$, Active Power ($P$), Cumulative Energy ($E$), Temperature |
| **ADC architecture** | Dual 16-bit Sigma-Delta ADCs |
| **Measurement accuracy** | Class 0.5 ($\pm 0.5\%$) |
| **Operating current** | $3.5\text{ mA}$ active |

## Pinout (10-Pin SSOP Package)

```
             ┌───┴───┐
         VDD ─┤ 1   10├─ GND
          IP ─┤ 2    9├─ RX / Mode
          IN ─┤ 3    8├─ TX
          VP ─┤ 4    7├─ CF / OverCurrent
         VN  ─┤ 5    6├─ NC / Test
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VDD` | Power | Core supply (+3.3 V DC) |
| 2 | `IP` | Analog Input | Positive current sense input (from shunt resistor) |
| 3 | `IN` | Analog Input | Negative current sense input |
| 4 | `VP` | Analog Input | Positive voltage sense input (from resistor divider) |
| 5 | `VN` | Analog Input | Negative voltage sense input |
| 7 | `CF` | Digital Output | Pulse frequency output / over-current alarm |
| 8 | `TX` | Digital Output | UART Transmit output pin (4,800 bps) |
| 9 | `RX` | Digital Input | UART Receive input pin |
| 10 | `GND` | Power | Ground reference (0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 3.0 | 3.3 | 3.6 | V | DC |
| Supply Current | $I_{DD}$ | — | 3.5 | 5.0 | mA | $V_{DD} = 3.3\text{ V}$ |
| Current Channel Input Range| $V_{IP-IN}$| -50 | — | +50 | mV Peak | Differential shunt voltage |
| Voltage Channel Input Range| $V_{VP-VN}$| -200 | — | +200 | mV Peak | Differential bus voltage |
| Measurement Accuracy | $E_{meter}$ | -0.5% | $\pm 0.1\%$| +0.5%| — | Active power range 2000:1 |
| Internal Voltage Ref | $V_{REF}$ | 1.18 | 1.218 | 1.25 | V | Low temperature coefficient |

## UART Frame Protocol

The BL0940 streams 22-byte serial telemetry frames continuously or on request over 4,800 baud UART:

- **Header byte:** `0x55` (Frame header).
- **Registers read:** $I_{RMS}$ (3 bytes), $V_{RMS}$ (3 bytes), Active Power $P$ (3 bytes), Energy Accumulator $E$ (3 bytes), Status (3 bytes), Checksum (1 byte).

$$ V_{RMS} = \frac{\text{Raw } V_{RMS} \text{ Register}}{K_v} \quad \text{Volts} $$

$$ I_{RMS} = \frac{\text{Raw } I_{RMS} \text{ Register}}{K_i} \quad \text{Amperes} $$

$$ P_{active} = \frac{\text{Raw } P \text{ Register}}{K_p} \quad \text{Watts} $$

## Wiring

Inside a smart plug, the BL0940 connects directly to an ESP8266, ESP32, or BK7231 Wi-Fi microcontroller:

| BL0940 Pin | → | MCU Pins | Notes |
|---|---|---|---|
| `VDD` | | 3.3V | Logic power |
| `GND` | | GND | Common ground |
| `TX`  | | MCU RX Pin (4800 baud) | Serial data from BL0940 |
| `RX`  | | MCU TX Pin (4800 baud) | Serial data to BL0940 |

> [!WARNING]
> High Voltage Safety Warning:
> - In commercial smart plugs, the BL0940 `GND` pin is connected directly to Neutral AC mains. Connecting a serial programmer to the UART pins while plugged into wall power will destroy computer USB ports and poses a lethal electric shock hazard. **Always use an isolated USB serial adapter or program via OTA.**

## Example (ESPHome Configuration)

```yaml
sensor:
  - platform: bl0940
    tx_pin: GPIO1
    rx_pin: GPIO3
    voltage:
      name: "Smart Plug Voltage"
    current:
      name: "Smart Plug Current"
    power:
      name: "Smart Plug Power"
    energy:
      name: "Smart Plug Energy"
```

## Common mistakes

- **Setting incorrect UART baud rate:** BL0940 operates strictly at **4,800 baud**. Setting 9,600 or 115,200 baud results in unreadable garbage data.
- **Forgetting calibration constants ($K_v, K_i, K_p$):** PCB trace layouts and resistor tolerances vary between smart plug manufacturers. Use a resistive load (such as a 60W incandescent bulb) to calibrate voltage, current, and power multipliers in Tasmota/ESPHome.

## Notes

- **BL0940 vs CSE7766 vs HLW8012:** BL0940 uses 4,800 baud UART; HLW8012 uses pulse frequencies; CSE7766 uses 4,800 baud UART with different packet headers.
