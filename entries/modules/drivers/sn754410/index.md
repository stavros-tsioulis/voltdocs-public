## Overview

The **SN754410** is a monolithic integrated quadruple high-current half-H motor driver IC manufactured by Texas Instruments. Designed as an upgraded, higher-current pin-compatible alternative to the ubiquitous **L293D**, the SN754410 is engineered to provide bidirectional drive currents up to **$1.0\text{ A}$ continuous** ($2.0\text{ A}$ peak) per channel at operating voltages from **$4.5\text{ V}$ to $36.0\text{ V}$**.

Housed in a 16-pin PowerDIP (`NE`) package with internal heat-sink ground pins, the SN754410 can control two bidirectional DC motors, a single bipolar four-wire stepper motor, or four independent inductive loads (such as solenoids and relays). The chip integrates output clamp diodes for inductive transient suppression and accepts standard 5V TTL/CMOS logic inputs with separate logic ($V_{CC1}$) and motor supply ($V_{CC2}$) power rails.

## Quick reference

| | |
|---|---|
| **Function** | Quadruple Half-H / Dual Full H-Bridge Motor Driver |
| **Motor Supply Voltage ($V_{CC2}$ / Pin 8)** | $4.5\text{ V}$ to $36.0\text{ V}$ DC |
| **Logic Supply Voltage ($V_{CC1}$ / Pin 16)** | $4.5\text{ V}$ to $5.5\text{ V}$ DC ($5\text{ V}$ nominal) |
| **Continuous Output Current (per channel)** | $1.0\text{ A}$ continuous |
| **Peak Output Current (per channel)** | $2.0\text{ A}$ non-repetitive ($t \le 5\text{ ms}$) |
| **Channels** | 4 Half-H Drivers (2 Independent Full H-Bridges) |
| **Internal Clamp Diodes** | Yes (integrated output clamp diodes to $V_{CC2}$ and GND) |
| **Logic Compatibility** | 5V TTL / CMOS (`HIGH` $\ge 2.0\text{V}$, `LOW` $\le 0.8\text{V}$) |
| **Operating Temperature Range** | $-40^\circ\text{C}$ to $85^\circ\text{C}$ |
| **Package** | 16-pin PowerDIP (`NE` package) |

## Pin configuration

### 16-Pin PowerDIP (NE Package)

```
               ┌──────────┐
        1,2EN ─┤ 1     16 ├─ VCC1 (Logic 5V)
           1A ─┤ 2     15 ├─ 4A
           1Y ─┤ 3     14 ├─ 4Y
     GND/HEAT ─┤ 4     13 ├─ GND/HEAT
     GND/HEAT ─┤ 5     12 ├─ GND/HEAT
           2Y ─┤ 6     11 ├─ 3Y
           2A ─┤ 7     10 ├─ 3A
     VCC2 (M) ─┤ 8      9 ├─ 3,4EN
               └──────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `1,2EN` | Digital Input | Enable driver channels 1 & 2 (`HIGH` = outputs active, `LOW` = high-Z) |
| 2 | `1A` | Digital Input | Driver 1 logic input line |
| 3 | `1Y` | Driver Output | Driver 1 output line (connect to Motor 1 terminal A) |
| 4, 5 | `GND` | Power / Heatsink | Ground and thermal heatsink pins (connect to large copper fill) |
| 6 | `2Y` | Driver Output | Driver 2 output line (connect to Motor 1 terminal B) |
| 7 | `2A` | Digital Input | Driver 2 logic input line |
| 8 | `VCC2` | Power Input | Motor / load supply voltage ($+4.5\text{ V}$ to $+36.0\text{ V}$ DC) |
| 9 | `3,4EN` | Digital Input | Enable driver channels 3 & 4 (`HIGH` = outputs active, `LOW` = high-Z) |
| 10 | `3A` | Digital Input | Driver 3 logic input line |
| 11 | `3Y` | Driver Output | Driver 3 output line (connect to Motor 2 terminal A) |
| 12, 13 | `GND` | Power / Heatsink | Ground and thermal heatsink pins (connect to large copper fill) |
| 14 | `4Y` | Driver Output | Driver 4 output line (connect to Motor 2 terminal B) |
| 15 | `4A` | Digital Input | Driver 4 logic input line |
| 16 | `VCC1` | Power Input | Logic supply voltage ($+4.5\text{ V}$ to $+5.5\text{ V}$ DC) |

## Functional description

- **Dual Full-Bridge Control:** Drivers 1 and 2 form H-Bridge 1 (controlled by `1,2EN`), while drivers 3 and 4 form H-Bridge 2 (controlled by `3,4EN`). Pulling an enable pin `LOW` disables both outputs in that pair into a high-impedance state, allowing motors to coast.
- **Direction & Braking Truth Table:**

| `EN` | `A` (Input 1) | `B` (Input 2) | `Y1` (Output 1) | `Y2` (Output 2) | Motor Action |
|---|---|---|---|---|---|
| **`HIGH`** | `HIGH` | `LOW` | **`HIGH`** | **`LOW`** | Forward rotation |
| **`HIGH`** | `LOW` | `HIGH` | **`LOW`** | **`HIGH`** | Reverse rotation |
| **`HIGH`** | `HIGH` | `HIGH` | **`HIGH`** | **`HIGH`** | Dynamic braking (both terminals shorted high) |
| **`HIGH`** | `LOW` | `LOW` | **`LOW`** | **`LOW`** | Dynamic braking (both terminals shorted to GND) |
| **`LOW`** | `X` | `X` | **`Z`** | **`Z`** | Coast (High-impedance off) |

- **PWM Speed Modulation:** Applying a PWM signal (typically $1\text{ kHz}$ to $5\text{ kHz}$) to the `EN` pin modulates the effective voltage and motor speed, while fixed logic levels on `1A` and `2A` dictate motor direction.

## Absolute maximum ratings

> [!WARNING]
> Stresses beyond these ratings cause permanent damage. Exposure to absolute-maximum conditions for extended periods affects device reliability.

| Parameter | Rating | Unit |
|---|---|---|
| Logic Supply Voltage ($V_{CC1}$) | 7.0 | V |
| Output / Motor Supply Voltage ($V_{CC2}$) | 36.0 | V |
| Input Voltage Range ($V_I$) | $-0.3$ to $V_{CC1} + 0.3$ | V |
| Continuous Output Current ($I_O$, per channel) | $\pm 1.1$ | A |
| Peak Output Current ($I_{O,peak}$, non-repetitive $t \le 5\text{ ms}$) | $\pm 2.0$ | A |
| Operating Free-Air Temperature Range ($T_A$) | -40 to 85 | °C |
| Continuous Total Power Dissipation ($T_A = 25^\circ\text{C}$) | 2.07 | W |
| Lead Temperature ($1.6\text{ mm}$ from case for $10\text{ s}$) | 260 | °C |

## Electrical characteristics

$V_{CC1} = 5\text{ V}$, $V_{CC2} = 24\text{ V}$, $T_A = 25^\circ\text{C}$, unless otherwise noted.

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| High-Level Input Voltage | $V_{IH}$ | 2.0 | — | $V_{CC1}$ | V | TTL compatible |
| Low-Level Input Voltage | $V_{IL}$ | -0.3 | — | 0.8 | V | TTL compatible |
| High-Level Output Voltage | $V_{OH}$ | $V_{CC2}-1.8$ | $V_{CC2}-1.4$ | — | V | $I_O = -1.0\text{ A}$ |
| Low-Level Output Voltage | $V_{OL}$ | — | 1.2 | 1.8 | V | $I_O = 1.0\text{ A}$ |
| Output Clamp Diode Forward Volts | $V_{F}$ | — | 1.4 | 2.0 | V | $I_F = 1.0\text{ A}$ |
| Clamp Reverse Leakage Current | $I_R$ | — | — | 100 | $\mu\text{A}$ | $V_R = 36\text{ V}$ |
| Logic Quiescent Current | $I_{CC1}$ | — | 22 | 35 | mA | Outputs open, all inputs high |
| Motor Supply Quiescent Current | $I_{CC2}$ | — | 2 | 6 | mA | Outputs open, all inputs high |

## Comparison: SN754410 vs L293D vs L298N

| Specification | SN754410 | L293D | L298N |
|---|---|---|---|
| **Continuous Current / Channel** | **$1.0\text{ A}$** | $0.6\text{ A}$ ($600\text{ mA}$) | **$2.0\text{ A}$** |
| **Peak Current / Channel** | **$2.0\text{ A}$** | $1.2\text{ A}$ | **$3.0\text{ A}$** |
| **Integrated Output Clamp Diodes**| **Yes** | **Yes** | No (External fast diodes required) |
| **Operating Motor Voltage** | $4.5\text{ V}$ to $36\text{ V}$ | $4.5\text{ V}$ to $36\text{ V}$ | $4.5\text{ V}$ to $46\text{ V}$ |
| **Package** | 16-pin PowerDIP | 16-pin PowerDIP | Multiwatt-15 / PowerSO20 |
| **Pin Compatibility** | **Direct drop-in for L293D** | Reference pinout | Distinct 15-pin layout |

## Wiring

| SN754410 Pin | → | Microcontroller / Power Supply / Motor | Description |
|---|---|---|---|
| `VCC1` (Pin 16) | | `5V` Logic Power Rail | Powers internal TTL logic gates |
| `VCC2` (Pin 8) | | External Motor Power Supply ($6\text{V} \dots 36\text{V}$) | Dedicated motor DC supply |
| `GND` (Pins 4, 5, 12, 13) | | Common System Ground | Solder to large PCB copper ground plane |
| `1,2EN` (Pin 1) | | Microcontroller PWM Pin (e.g. D9) | Speed control via PWM duty cycle |
| `1A` (Pin 2) | | Microcontroller GPIO Pin (e.g. D7) | Direction input line 1 |
| `2A` (Pin 7) | | Microcontroller GPIO Pin (e.g. D8) | Direction input line 2 |
| `1Y` (Pin 3) | | Motor 1 Terminal (+) | Output to DC Motor 1 |
| `2Y` (Pin 6) | | Motor 1 Terminal (-) | Output to DC Motor 1 |

> [!WARNING]
> Darlington Thermal Dissipation:
> The SN754410 uses bipolar Darlington transistors. The total voltage drop across high-side ($V_{CC2} - V_{OH} \approx 1.4\text{V}$) and low-side ($V_{OL} \approx 1.2\text{V}$) switches equals approximately **$2.6\text{ V}$**. At $1.0\text{ A}$ continuous load current, the chip dissipates:
> $$P_D \approx 2.6\text{ V} \times 1.0\text{ A} = 2.6\text{ Watts}$$
> This exceeds the free-air rating ($2.07\text{ W}$). You **must** solder pins 4, 5, 12, and 13 to substantial PCB copper pours or attach a clip-on DIP heatsink when running currents above $500\text{ mA}$.

## Common mistakes

- **Relying Solely on Internal Diodes for Large Inductive Loads:** While the SN754410 includes internal clamp diodes, inductive flyback energy from high-current motors produces high instantaneous heat within the silicon die. When driving large stepper motors or high-inductance DC motors, adding external fast-recovery Schottky diodes (such as **1N5819**) across the motor outputs prevents thermal overstress.
- **Powering Motors from the Microcontroller 5V Rail:** Connecting $V_{CC2}$ to the 5V MCU power supply causes severe voltage droop and inductive noise spikes that cause microcontroller brownouts and resets. Always power $V_{CC2}$ from an independent battery or motor power supply with a shared ground.
- **Neglecting the 2.6V Voltage Drop with Low-Voltage Motors:** If using a 6V battery pack on $V_{CC2}$, the motor will only receive $\sim 3.4\text{ V}$ due to internal transistor saturation losses. For battery-powered projects using 3V to 6V motors, modern low-$R_{DS(on)}$ MOSFET H-bridges like the **TB6612FNG** or **DRV8833** offer drastically higher efficiency and near-zero voltage loss.

## Notes

- **Pin Compatibility:** The SN754410 is a direct pin-for-pin replacement for the **L293D** and **L293B**, offering an immediate 66% increase in continuous current rating ($1.0\text{ A}$ vs $0.6\text{ A}$).
- **Ground / Heatsink Pins:** Pins 4, 5, 12, and 13 are tied together through the internal lead frame and form the primary thermal conduction path from the silicon die.
