## Overview

The **L293D** is a monolithic integrated high-voltage, high-current quadruple half-H driver chip manufactured by Texas Instruments and STMicroelectronics. It is designed to drive inductive loads such as DC motors, bipolar/unipolar stepper motors, relays, and solenoids.

The chip contains 4 independent half-H channels (capable of driving 2 bidirectional DC motors or 1 stepper motor) providing up to **600 mA continuous output current** per channel at voltages from **4.5 V to 36 V**. The "D" suffix variant integrates internal flyback clamp diodes to suppress inductive voltage spikes.

## Quick reference

| | |
|---|---|
| **Motor supply voltage (`VCC2` / Pin 8)** | 4.5 V to 36.0 V DC |
| **Logic supply voltage (`VCC1` / Pin 16)** | 4.5 V to 7.0 V DC (5 V nominal) |
| **Continuous current per channel** | 600 mA |
| **Peak output current per channel** | 1.2 A (non-repetitive pulse $<100\text{ }\mu\text{s}$) |
| **Internal flyback diodes** | Yes (integrated internal clamp diodes to $V_{CC2}$) |
| **Control logic inputs** | 5V TTL/CMOS compatible (`1A`–`4A`, `1,2EN`, `3,4EN`) |
| **Thermal protection** | Internal thermal shutdown protection |

## Pin configuration

### 16-Pin DIP / SOIC Package

```
           ┌──────────┐
    1,2EN ──│ 1     16 │── VCC1 (Logic 5V)
       1A ──│ 2     15 │── 4A
       1Y ──│ 3     14 │── 4Y
      GND ──│ 4     13 │── GND
      GND ──│ 5     12 │── GND
       2Y ──│ 6     11 │── 3Y
       2A ──│ 7     10 │── 3A
 VCC2 (M) ──│ 8      9 │── 3,4EN
           └──────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `1,2EN` | Digital Input | Enable driver channels 1 & 2 (`HIGH` = Active, `LOW` = High-impedance) |
| 2 | `1A` | Digital Input | Driver 1 input line |
| 3 | `1Y` | Driver Output | Driver 1 output line (connect to Motor 1 terminal A) |
| 4, 5 | `GND` | Power | Ground & Heat sink pins (solder to PCB copper plane) |
| 6 | `2Y` | Driver Output | Driver 2 output line (connect to Motor 1 terminal B) |
| 7 | `2A` | Digital Input | Driver 2 input line |
| 8 | `VCC2` | Power Input | Motor power supply voltage (+4.5 V to +36 V DC) |
| 9 | `3,4EN` | Digital Input | Enable driver channels 3 & 4 (`HIGH` = Active, `LOW` = High-impedance) |
| 10 | `3A` | Digital Input | Driver 3 input line |
| 11 | `3Y` | Driver Output | Driver 3 output line (connect to Motor 2 terminal A) |
| 12, 13 | `GND` | Power | Ground & Heat sink pins |
| 14 | `4Y` | Driver Output | Driver 4 output line (connect to Motor 2 terminal B) |
| 15 | `4A` | Digital Input | Driver 4 input line |
| 16 | `VCC1` | Power Input | Logic power supply voltage (+5.0 V DC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Motor Supply Voltage | $V_{CC2}$ | 4.5 | 12.0 | 36.0 | V | DC |
| Logic Supply Voltage | $V_{CC1}$ | 4.5 | 5.0 | 7.0 | V | DC |
| Continuous Output Current | $I_{O}$ | -600 | — | 600 | mA | Per channel |
| Peak Output Current | $I_{O,peak}$ | -1.2 | — | 1.2 | A | $t \le 100\text{ }\mu\text{s}$, non-repetitive |
| Input High Voltage | $V_{IH}$ | 2.3 | — | $V_{CC1}$ | V | TTL compatible |
| Input Low Voltage | $V_{IL}$ | -0.3 | — | 1.5 | V | TTL compatible |
| Saturation Voltage (Low) | $V_{OL}$ | — | 0.9 | 1.2 | V | $I_{O} = 600\text{ mA}$ |
| Saturation Voltage (High) | $V_{OH}$ | $V_{CC2}-1.8$ | $V_{CC2}-1.4$ | — | V | $I_{O} = -600\text{ mA}$ |
| Thermal Shutdown Temp | $T_{JSD}$ | — | 145 | — | °C | Junction temperature |

## Truth Table (per DC Motor Channel)

| `EN` | `1A` / `3A` | `2A` / `4A` | `1Y` / `3Y` | `2Y` / `4Y` | Motor Direction |
|---|---|---|---|---|---|
| **`HIGH`** | `HIGH` | `LOW` | **`HIGH`** | **`LOW`** | Forward rotation |
| **`HIGH`** | `LOW` | `HIGH` | **`LOW`** | **`HIGH`** | Reverse rotation |
| **`HIGH`** | `LOW` | `LOW` | **`LOW`** | **`LOW`** | Fast motor brake |
| **`HIGH`** | `HIGH` | `HIGH` | **`HIGH`** | **`HIGH`** | Fast motor brake |
| **`LOW`** | `X` | `X` | `Z` | `Z` | Coast (High-impedance) |

## Wiring

| L293D Pin | → | Microcontroller / Motor / Power | Notes |
|---|---|---|---|
| `VCC1` (Pin 16) | | `5V` | Logic power supply |
| `VCC2` (Pin 8) | | External Motor Power Supply (6V–36V) | **Dedicated high-current supply for motors** |
| `GND` (Pins 4,5,12,13) | | Common `GND` | Must connect to MCU GND & Motor Power GND |
| `1A`, `2A` (Pins 2, 7) | | Digital GPIO Pins (e.g. D4, D5) | Direction control for Motor 1 |
| `1,2EN` (Pin 1) | | PWM Pin (e.g. D3) | Speed control via 0–2500 Hz PWM |
| `1Y`, `2Y` (Pins 3, 6) | | Motor 1 Terminals | Outputs to DC Motor 1 |

> [!WARNING]
> High Internal Voltage Drop & Heat Generation:
> The L293D uses bipolar Darlington output transistors with a combined high/low side saturation voltage drop of **$\sim 2.6\text{ V}$**. When driving a 6V motor at 600 mA, nearly $1.5\text{ W}$ is dissipated as heat inside the chip. Ensure center GND pins (pins 4, 5, 12, 13) are soldered to large PCB copper ground planes.

## Common mistakes

- **Confusing L293 and L293D:** The basic **L293** (no "D") lacks internal flyback diodes. Using an L293 without external 1N4007 flyback diodes across the motor coils will destroy the chip. The **L293D** has integrated diodes.
- **Powering motors from VCC1 (5V logic rail):** Inductive motor spikes and current draw cause voltage drops, resetting the MCU.
- **Ignoring 2.6V Darlington voltage drop:** Supplying 6V to $V_{CC2}$ only delivers $\sim 3.4\text{ V}$ to the motor. For low-voltage motors (3V–6V), use a modern MOSFET driver like the **TB6612FNG**.

## Notes

- Pins 4, 5, 12, and 13 are internally connected together and serve as the main thermal heatsink path for the silicon die.
