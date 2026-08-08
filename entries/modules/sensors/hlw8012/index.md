## Overview

The **HLW8012** is a low-cost single-phase electricity metering IC manufactured by HLW (Zhongshan Belling). Most famously embedded inside the original **Sonoff POW** Wi-Fi smart switch, it measures active power (W), RMS voltage (V), and RMS current (A).

Rather than using serial UART data packets, the HLW8012 outputs **dual 50% duty-cycle frequency pulse trains**:
1. **`CF` (Power Frequency):** Outputs a high-frequency pulse train whose frequency is directly proportional to active power (W).
2. **`CF1` (Voltage/Current Frequency):** Outputs a pulse train whose frequency is proportional to either RMS voltage or RMS current, determined by the logic level on the **`SEL` (Select)** pin.

It is natively supported in ESPHome, Tasmota, and the Arduino `HLW8012` library.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VDD`)** | 4.5 V to 5.5 V DC (5.0 V nominal) |
| **Output interface** | Dual Pulse Frequency Outputs (`CF`, `CF1`) + Mode Select (`SEL`) |
| **Active power signal (`CF`)** | High frequency ($0\text{ to }3.4\text{ kHz}$) proportional to active power |
| **Voltage/Current signal (`CF1`)** | Frequency proportional to $V_{RMS}$ (when `SEL` is High) or $I_{RMS}$ (when `SEL` is Low) |
| **Measurement accuracy** | Class 0.5 ($\pm 0.5\%$) |
| **High-voltage sense inputs** | $V_P$ (voltage divider, $\le 43.7\text{ mV}$) & $V_{IP}/V_{IN}$ (shunt resistor, $\le 43.7\text{ mV}$) |
| **Operating current** | $3.0\text{ mA}$ typical |

## Pinout (SOP-8 Package)

```
             ┌───┴───┐
          VDD ─┤ 1    8├─ GND
          V1P ─┤ 2    7├─ SEL
          V1N ─┤ 3    6├─ CF1
           V2P ─┤ 4    5├─ CF
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VDD` | Power | Logic power supply (+4.5 V to +5.5 V DC) |
| 2 | `V1P` | Analog Input | Positive current sense input (from $1\ \text{m}\Omega$ shunt) |
| 3 | `V1N` | Analog Input | Negative current sense input |
| 4 | `V2P` | Analog Input | Voltage sense input (from resistor divider; $V_{2N}$ connected to GND) |
| 5 | `CF` | Digital Output | Active power pulse frequency output pin |
| 6 | `CF1` | Digital Output | Voltage/Current pulse frequency output pin |
| 7 | `SEL` | Digital Input | Select pin (HIGH = read Voltage on `CF1`, LOW = read Current on `CF1`) |
| 8 | `GND` | Power | Ground reference (0 V) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{DD}$ | 4.5 | 5.0 | 5.5 | V | DC |
| Supply Current | $I_{DD}$ | — | 3.0 | 5.0 | mA | Active operation |
| Current Channel Input Range| $V_{V1P-V1N}$| -43.7 | — | +43.7 | mV Peak | Differential shunt voltage |
| Voltage Channel Input Range| $V_{V2P}$ | -43.7 | — | +43.7 | mV Peak | Single-ended voltage |
| Active Power Accuracy | $E_P$ | -0.5% | $\pm 0.1\%$| +0.5%| — | Dynamic range 1000:1 |
| Max `CF` Output Frequency | $f_{CF\_max}$ | — | 3.4 | — | kHz | Rated power load |
| Max `CF1` Output Frequency| $f_{CF1\_max}$| — | 890 | — | Hz | Rated voltage/current load |

## Frequency Math & Time Periods

To read power, voltage, and current on a microcontroller:

1. **Active Power (W):** Measure pulse period $T_{CF}$ on pin `CF` using interrupts:

$$ P\text{ (W)} = \frac{K_P}{T_{CF}} \quad \text{(or } P = f_{CF} \times K_P \text{)} $$

2. **Voltage (V):** Set `SEL` High, wait $200\text{ ms}$ for frequency stabilization, measure $T_{CF1}$:

$$ V_{RMS}\text{ (V)} = \frac{K_V}{T_{CF1}} $$

3. **Current (A):** Set `SEL` Low, wait $200\text{ ms}$ for frequency stabilization, measure $T_{CF1}$:

$$ I_{RMS}\text{ (A)} = \frac{K_I}{T_{CF1}} $$

## Wiring (Sonoff POW Internal Connections)

| HLW8012 Pin | → | ESP8266 GPIO | Notes |
|---|---|---|---|
| `VDD` | | 5V (from internal LDO) | Power rail |
| `GND` | | GND | Common ground (connected to Neutral AC) |
| `CF`  | | GPIO 14 (Interrupt) | Power pulse frequency |
| `CF1` | | GPIO 13 (Interrupt) | Voltage/Current pulse frequency |
| `SEL` | | GPIO 12 (Output) | Mode Select pin |

> [!WARNING]
> Lethal High Voltage Hazard:
> - HLW8012 `GND` is tied directly to AC Neutral. Connecting an un-isolated FTDI serial adapter or logic analyzer to a powered Sonoff POW will destroy connected computer equipment and create a lethal electric shock hazard. **Always flash/debug Sonoff POW boards while disconnected from AC mains power.**

## Example (ESPHome Configuration)

```yaml
sensor:
  - platform: hlw8012
    sel_pin: GPIO12
    cf_pin: GPIO14
    cf1_pin: GPIO13
    current_resistor: 0.001 # 1 mOhm shunt
    voltage_divider: 2400   # 2.4 MOhm / 1 kOhm divider
    voltage:
      name: "Sonoff POW Voltage"
    current:
      name: "Sonoff POW Current"
    power:
      name: "Sonoff POW Power"
```

## Common mistakes

- **Switching `SEL` without waiting for frequency settling:** After toggling `SEL` between High (Voltage) and Low (Current), wait at least $200\text{ ms}$ before measuring `CF1` pulse period to allow internal frequency multipliers to settle.
- **Forgetting input pull-up / interrupt edge setup:** `CF` and `CF1` output square-wave pulses. Ensure hardware interrupts trigger on `FALLING` or `RISING` edges.

## Notes

- **HLW8012 vs CSE7766:** Modern Sonoff devices (Sonoff POW R2 and Sonoff S31) replaced the HLW8012 with the CSE7766 UART power chip, which eliminates interrupt timing overhead on the host MCU.
