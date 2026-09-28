## Overview

The **LV8729** (specifically the LV8729V) is a dedicated PWM current-controlled bipolar stepper motor driver IC originally designed by Sanyo (now ON Semiconductor) and widely popularized as a high-performance StepStick plug-in driver module for 3D printers and desktop CNC equipment.

Its defining hallmark is native support for ultra-high **1/128 microstepping** through standard hardware jumper pins (`MS1`, `MS2`, `MS3`), without requiring software register configuration or SPI/UART buses. By sub-dividing each full step into 128 microsteps, the LV8729 produces exceptionally smooth, low-vibration, and whisper-quiet motor positioning, eliminating low-speed resonance and acoustic buzz common to 1/16-step drivers like the Allegro A4988.

Capable of operating across a motor voltage supply span from $9.0\text{ V}$ to $32.0\text{ V}$ DC and delivering up to $1.5\text{ A}$ continuous ($1.8\text{ A}$ peak) per phase with proper heatsinking, the LV8729 is a direct mechanical and electrical drop-in replacement for A4988 and DRV8825 sockets on controller boards such as RAMPS 1.4, MKS Gen L, and BIGTREETECH SKR.

## Quick reference

| Parameter | Value | Notes |
|---|---|---|
| **Motor Supply Voltage ($V_M$)** | $9.0\text{ V}$ to $32.0\text{ V}$ DC | Absolute maximum $36\text{ V}$ |
| **Logic Supply Voltage ($V_{DD}$)** | $3.0\text{ V}$ to $5.5\text{ V}$ DC | Compatible with $3.3\text{ V}$ and $5\text{ V}$ MCUs |
| **Continuous Current per Phase** | $1.5\text{ A}$ | With heatsink and convective airflow |
| **Peak Output Current** | $1.8\text{ A}$ | Peak allowable winding surge current |
| **Microstep Resolutions** | Full, 1/2, 1/4, 1/8, 1/16, 1/32, 1/64, 1/128 | Configured via `MS1`, `MS2`, `MS3` logic pins |
| **Control Interface** | STEP / DIR pins | Standard StepStick clock pulse interface |
| **MOSFET $R_{DS(ON)}$** | $450\text{ m}\Omega$ typical | Upper + lower total $0.90\ \Omega$ at $25^\circ\text{C}$ |
| **Protection Features** | Thermal Shutdown (TSD), Low-Voltage Lockout | Auto-recovering thermal protection |

## Terminals

The LV8729 breakout module uses the standard 16-pin 0.1" pitch dual-in-line StepStick header configuration:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `ENABLE` | Digital Input | Active-low output bridge enable. Low = motor energized, High = high-Z floating. |
| 2 | `MS1` | Digital Input | Microstep resolution selector pin 1 (internal pull-down). |
| 3 | `MS2` | Digital Input | Microstep resolution selector pin 2 (internal pull-down). |
| 4 | `MS3` | Digital Input | Microstep resolution selector pin 3 (internal pull-down). |
| 5 | `RESET` | Digital Input | Active-low reset input. Internal logic reset; must be High for operation. |
| 6 | `SLEEP` | Digital Input | Active-low sleep mode input. Low = sleep mode (sub-µA), High = normal mode. |
| 7 | `STEP` | Digital Input | Step pulse input. Advances motor one microstep on each rising edge. |
| 8 | `DIR` | Digital Input | Direction control input. Sets rotational direction. |
| 9 | `GND` | Power | Logic & ground reference ($0\text{ V}$). |
| 10 | `VDD` / `VIO` | Power | Logic supply input ($+3.0\text{ V}$ to $+5.5\text{ V}$ DC). |
| 11 | `1B` | Motor Output | Bipolar stepper motor coil 1 (terminal B). |
| 12 | `1A` | Motor Output | Bipolar stepper motor coil 1 (terminal A). |
| 13 | `2A` | Motor Output | Bipolar stepper motor coil 2 (terminal A). |
| 14 | `2B` | Motor Output | Bipolar stepper motor coil 2 (terminal B). |
| 15 | `GND` | Power | Motor power ground reference. |
| 16 | `VMOT` | Power | Motor power rail ($+9.0\text{ V}$ to $+32.0\text{ V}$ DC). |

*Note: On standard StepStick modules, `RESET` and `SLEEP` are frequently tied together or pulled up to `VDD` via onboard resistors.*

## The technical core

### Microstepping configuration truth table

The microstep resolution is selected using binary combination inputs on `MS1`, `MS2`, and `MS3`. When jumpers are inserted beneath the driver on 3D printer mainboards, the corresponding pin is pulled High ($V_{DD}$); open jumpers leave the pins pulled Low via internal resistors:

| `MS1` | `MS2` | `MS3` | Microstep Resolution | Steps per $1.8^\circ$ Revolution |
|---|---|---|---|---|
| Low | Low | Low | **Full Step** | 200 |
| High | Low | Low | **1/2 Step** | 400 |
| Low | High | Low | **1/4 Step** | 800 |
| High | High | Low | **1/8 Step** | 1,600 |
| Low | Low | High | **1/16 Step** | 3,200 |
| High | Low | High | **1/32 Step** | 6,400 |
| Low | High | High | **1/64 Step** | 12,800 |
| High | High | High | **1/128 Step** | 25,600 |

### Current limiting calibration ($V_{ref}$)

To prevent motor overheating or driver thermal shutdown, the peak phase current limit must be adjusted using the onboard miniature trimmer potentiometer.

The LV8729 internal current trip comparator uses a fixed division ratio of 5 against the current sense voltage across $R_{SENSE}$:

$$ I_{max} = \frac{V_{ref}}{5 \times R_{SENSE}} $$

Most standard commercially available LV8729 StepStick modules are manufactured with **$0.100\ \Omega$ ($R100$)** sense resistors:

$$ I_{max} = \frac{V_{ref}}{5 \times 0.100\ \Omega} = \frac{V_{ref}}{0.5\ \Omega} = 2 \times V_{ref} $$

$$\text{Conversely: } V_{ref} = \frac{I_{max}}{2} = 0.5 \times I_{max} $$

**Calculation Example:**
For a NEMA 17 stepper motor with a rated RMS current of $1.0\text{ A}$ (peak current $I_{max} = 1.0\text{ A} \times \sqrt{2} \approx 1.41\text{ A}$, or targeting $80\%$ continuous safety margin: $I_{target} = 1.0\text{ A}$):
$$ V_{ref} = \frac{1.0\text{ A}}{2} = 0.50\text{ V} = 500\text{ mV} $$

Measure the voltage with a multimeter positive probe on the metal potentiometer screw top and the negative probe on the `GND` pin with logic power energized.

### Electrical specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Motor Supply Voltage | $V_M$ | 9.0 | 24.0 | 32.0 | V | Operating range |
| Logic Supply Voltage | $V_{DD}$ | 3.0 | 3.3 / 5.0 | 5.5 | V | Logic rail |
| Standby Current | $I_{ST}$ | — | — | 10 | µA | `SLEEP` = Low |
| Quiescent Operating Current | $I_{DD}$ | — | 4.5 | 8.0 | mA | Driver active, outputs disabled |
| High-Side On-Resistance | $R_{ON\_H}$ | — | 0.45 | 0.65 | $\Omega$ | $I_{OUT} = 1.0\text{ A}$ |
| Low-Side On-Resistance | $R_{ON\_L}$ | — | 0.45 | 0.65 | $\Omega$ | $I_{OUT} = 1.0\text{ A}$ |
| Reference Input Voltage | $V_{REF}$ | 0.0 | — | 1.5 | V | Analog adjustment pin |
| Thermal Shutdown Temp | $T_{TSD}$ | 150 | 170 | 190 | °C | Silicon junction temp |
| Minimum Step Pulse Width | $t_{STEP}$ | 1.0 | — | — | µs | High or low pulse width |

## Usage

### Wiring to a 3D printer / microcontroller

| LV8729 Pin | → | Microcontroller / Motherboard | External Supply |
|---|---|---|---|
| `VMOT` | | — | $+12\text{V}$ to $+24\text{V}$ DC (with $100\ \mu\text{F}$ cap) |
| `GND` (Motor) | | — | DC Power Supply Ground |
| `VDD` | | MCU $+5\text{V}$ or $+3.3\text{V}$ | — |
| `GND` (Logic) | | MCU Ground | — |
| `STEP` | | MCU Step Output Pin | — |
| `DIR` | | MCU Direction Output Pin | — |
| `ENABLE` | | MCU Enable Output Pin | Active-low |
| `1A`, `1B` | | Stepper Motor Phase A | — |
| `2A`, `2B` | | Stepper Motor Phase B | — |

> [!WARNING]
> High Microstepping Pulse Rate Bottleneck:
> At 1/128 microstepping, a standard $1.8^\circ$ stepper motor requires **25,600 pulses per revolution**.
> - At a travel speed of $100\text{ mm/s}$ with a 20-tooth GT2 pulley ($40\text{ mm/rev}$), the controller must output $64\text{ kHz}$ of continuous step pulses per axis.
> - Classic 8-bit microcontrollers (such as the ATmega2560 running Marlin) cannot maintain step frequencies beyond $20\text{ kHz} - 30\text{ kHz}$ reliably and will freeze, stutter, or drop steps.
> - **Use a 32-bit ARM Cortex-M controller** (e.g. STM32, RP2040, LPC1768) running Marlin 2.x, Klipper, or RepRapFirmware when configuring 1/64 or 1/128 microstepping.

### Arduino code example

```cpp
// Basic LV8729 Step & Direction Test
const int pinStep   = 3;
const int pinDir    = 4;
const int pinEnable = 5;

void setup() {
  pinMode(pinStep, OUTPUT);
  pinMode(pinDir, OUTPUT);
  pinMode(pinEnable, OUTPUT);

  // Enable driver
  digitalWrite(pinEnable, LOW);
  digitalWrite(pinDir, HIGH);
}

void loop() {
  // Rotate smoothly: generate high-frequency pulses
  for (int i = 0; i < 25600; i++) { // One full revolution at 1/128 microstepping
    digitalWrite(pinStep, HIGH);
    delayMicroseconds(10);
    digitalWrite(pinStep, LOW);
    delayMicroseconds(10);
  }
  delay(1000);

  // Reverse direction
  digitalWrite(pinDir, !digitalRead(pinDir));
}
```

## Common mistakes

- **Running 1/128 microstepping on 8-bit hardware:** Attempting to run high speeds on an Arduino Mega / RAMPS 1.4 at 1/128 will overrun the CPU interrupt budget, leading to jittery prints or complete axis stalling. On 8-bit boards, limit resolution to 1/32 or 1/16.
- **Operating without heatsink or cooling:** Because the total bridge resistance is $\approx 0.90\ \Omega$, thermal dissipation at $1.5\text{ A}$ continuous is over $2\text{ W}$, which will trigger thermal shutdown in seconds without an aluminum heatsink and cooling fan.
- **Hot-plugging motor connectors:** Disconnecting the stepper motor connector while $V_M$ is energized creates massive inductive voltage transients that permanently destroy the driver IC.
- **Confusing orientation with other StepSticks:** Check the pin markings (`GND`, `DIR`, `VMOT`) on the underside of the PCB before seating the module into the socket.

## Notes

- **LV8729 vs TMC2208/TMC2209:** While Trinamic drivers use internal interpolation (MicroPlyer) from 16 native steps to 256 interpolated microsteps, the LV8729 generates true native 1/128 microstepping directly from the input step clock. This gives exceptionally smooth trajectories, provided the host processor can supply the required step pulse frequency.
