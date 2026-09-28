## Overview

The **TMC2130** is an ultra-silent two-phase bipolar stepper motor driver IC developed by Trinamic (now part of Analog Devices). Packaged in a compact 36-pin QFN and widely deployed on 16-pin "SilentStepStick" plug-in modules, the TMC2130 spearheaded the modern quiet 3D printing revolution, notably as the factory driver of the Prusa i3 MK3.

Unlike traditional analog-chopper stepper drivers (such as the A4988 or DRV8825) that generate noticeable magnetostrictive acoustic whine and mechanical vibration, the TMC2130 incorporates Trinamic's proprietary **StealthChop™** voltage-controlled PWM modulation, rendering motor movement virtually inaudible at low and moderate speeds.

In addition to whisper-quiet motion, the TMC2130 provides a full high-speed 4-wire **SPI communication bus**. Through SPI, firmware can configure motor current in milliamps without touching a physical potentiometer, tune microstepping resolutions up to 1/256, read internal diagnostic status (short circuits, open coils, temperature warnings), and configure **StallGuard2™**—a back-EMF sensing technology that detects physical mechanical endstops without requiring separate microswitches or wiring harness limit sensors ("sensorless homing").

## Quick reference

| Parameter | Value | Notes |
|---|---|---|
| **Motor Supply Voltage ($V_M$)** | $4.75\text{ V}$ to $46.0\text{ V}$ DC | Absolute maximum $48.0\text{ V}$ |
| **Logic Supply Voltage ($V_{IO}$)** | $3.3\text{ V}$ to $5.0\text{ V}$ DC | Compatible with $3.3\text{V}$ and $5\text{V}$ logic levels |
| **Phase Current ($I_{RMS}$)** | Up to $1.4\text{ A}$ RMS ($2.0\text{ A}$ peak) | Software programmable via SPI in $1\text{ mA}$ steps |
| **Microstep Resolutions** | Full step up to 1/256 native | 1/256 interpolation via internal MicroPlyer™ |
| **Silent Technology** | StealthChop™ | Noiseless voltage-mode operation at cruising speeds |
| **Dynamic Chopper** | SpreadCycle™ | Cycle-by-cycle current mode for high torque and velocity |
| **Sensorless Homing** | StallGuard2™ | High-precision back-EMF load measurement |
| **Energy Conservation** | CoolStep™ | Dynamic current reduction saving up to 75% energy |
| **Control Interfaces** | STEP/DIR + 4-Wire SPI | Shared bus with individual Chip Select (`CS`) lines |
| **MOSFET $R_{DS(ON)}$** | $500\text{ m}\Omega$ typical | High-side + low-side total per bridge |

## Terminals

### SilentStepStick module header pinout

On standard 16-pin SilentStepStick carrier boards (Watterott / BigTreeTech / FYSETC pinout), standard STEP/DIR signals occupy the outer edge headers, while SPI and diagnostic lines are accessible via side pins or dedicated top headers:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `EN` | Digital Input | Active-low driver enable (can also be managed via SPI register `CHOPCONF`) |
| 2 | `SDO` (`CFG0`) | SPI Output / Pin | SPI MISO (Master In Slave Out) serial data output |
| 3 | `CS` (`CFG1` / `CSN`) | SPI Input / Pin | SPI Chip Select (active-low; individual per driver axis) |
| 4 | `SCK` (`CFG2`) | SPI Input / Pin | SPI Serial Clock input |
| 5 | `SDI` (`CFG3`) | SPI Input / Pin | SPI MOSI (Master Out Slave In) serial data input |
| 6 | `DIAG1` | Digital Output | Diagnostic / StallGuard output 1 (used for sensorless homing) |
| 7 | `STEP` | Digital Input | Step pulse input. Advances rotor by one microstep on rising edge |
| 8 | `DIR` | Digital Input | Direction input signal |
| 9 | `GND` | Power | Logic ground ($0\text{ V}$) |
| 10 | `VIO` | Power | Digital logic supply voltage ($+3.3\text{ V}$ or $+5.0\text{ V}$) |
| 11 | `1B` (`B2`) | Motor Output | Stepper motor coil B terminal 2 |
| 12 | `1A` (`B1`) | Motor Output | Stepper motor coil B terminal 1 |
| 13 | `2A` (`A1`) | Motor Output | Stepper motor coil A terminal 1 |
| 14 | `2B` (`A2`) | Motor Output | Stepper motor coil A terminal 2 |
| 15 | `GND` | Power | Motor power ground reference |
| 16 | `VM` | Power | Motor supply voltage ($+4.75\text{ V}$ to $+46.0\text{ V}$ DC) |

*Top / auxiliary pins on SilentStepStick modules:*
- `DIAG0`: Diagnostic output 0 (overtemperature / driver error flag)
- `DIAG1`: StallGuard2 stall detection pulse output (routed to endstop input on controller board)

## The technical core

### StealthChop™ vs. SpreadCycle™

The TMC2130 provides two distinct motor commutation algorithms that can be automatically switched based on operating velocity:

1. **StealthChop™ (Voltage PWM Mode):**
   - Regulates current by modulating voltage PWM duty cycle based on motor back-EMF.
   - Eliminates switching hysteresis noise and high-frequency magnetostrictive hiss.
   - Ideal for low to medium speeds where quiet operation is paramount.
2. **SpreadCycle™ (Cycle-by-Cycle Current Chopping):**
   - Uses a patented spread-frequency chopping scheme providing fast current response.
   - Delivers superior high-speed torque and dynamic acceleration without skipping steps.
   - Firmware automatically switches from StealthChop to SpreadCycle at high velocities via the `TPWMTHRS` velocity threshold register.

### StallGuard2™ sensorless homing

StallGuard2 measures the counter-electromotive force (back-EMF) induced in the motor windings during the off-time of each PWM cycle:
- As mechanical load on the motor increases, the rotor angle lags behind the stator magnetic field, reducing back-EMF.
- When the motor hits a physical mechanical endstop (such as the frame of a 3D printer), back-EMF drops sharply to zero.
- The TMC2130 reports this load value in the internal `DRV_STATUS` register ($SG\_RESULT$, 0 to 1023).
- When $SG\_RESULT$ drops to zero, the driver asserts the `DIAG1` pin Low, triggering a controller endstop interrupt.
- Sensitivity is calibrated via the signed 7-bit register `SGT` ($-64$ to $+63$): higher values increase sensitivity (stall detected with lighter contact), while lower values decrease sensitivity.

### SPI register architecture

The driver is configured by writing 32-bit words over SPI (Mode 3, CPOL=1, CPHA=1):

| Register | Address | Access | Description |
|---|---|---|---|
| `GCONF` | `0x00` | R/W | Global configuration (StealthChop enable, internal sense resistor scaling) |
| `GSTAT` | `0x01` | R/W | Global status flags (reset flag, undervoltage flag) |
| `IHOLD_IRUN` | `0x10` | W | Run current (bits 20..16) and hold current (bits 4..0) scaling ($0 \dots 31$) |
| `TPOWERDOWN` | `0x11` | W | Standby delay before entering hold-current mode |
| `TPWMTHRS` | `0x13` | W | Upper velocity limit for StealthChop voltage mode |
| `TCOOLTHRS` | `0x14` | W | Lower velocity threshold for CoolStep and StallGuard |
| `THIGH` | `0x15` | W | Velocity threshold above which driver switches to fullstep mode |
| `CHOPCONF` | `0x6C` | R/W | Chopper configuration (microstep resolution $MRES$, blank time, off time) |
| `COOLCONF` | `0x6D` | W | CoolStep smart energy reduction and StallGuard threshold |
| `DRV_STATUS` | `0x6F` | R | Status flags: stall flag, thermal warning, coil open-load, $SG\_RESULT$ |

### Software current setting calculation

Motor current in SPI mode is configured digitally via the 5-bit current scale register `CS` in `IHOLD_IRUN`:

$$ I_{RMS} = \frac{CS + 1}{32} \times \frac{V_{FS}}{R_{SENSE} \times \sqrt{2}} $$

Where:
- $CS \in [0, 31]$ (digital scale setting)
- $V_{FS} = 0.32\text{ V}$ (internal reference with standard `vsense = 0`)
- $R_{SENSE} = 0.110\ \Omega$ (standard SilentStepStick resistor value)

$$ I_{RMS\_MAX} = \frac{32}{32} \times \frac{0.32\text{ V}}{0.110\ \Omega \times 1.414} \approx 2.05\text{ A peak} \approx 1.45\text{ A RMS} $$

Firmware libraries (such as `TMCStepper`) automatically compute the optimal `CS` value from a desired target current in milliamps:

```cpp
driver.rms_current(800); // Set phase current directly to 800 mA RMS
```

### Electrical specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Motor Supply Voltage | $V_M$ | 4.75 | 24.0 | 46.0 | V | Operating range |
| Logic Supply Voltage | $V_{IO}$ | 3.3 | 3.3 / 5.0 | 5.25 | V | Logic interface |
| RMS Current per Phase | $I_{RMS}$ | — | 1.2 | 1.4 | A | With heatsink and fan |
| Peak Current per Phase | $I_{PEAK}$ | — | — | 2.0 | A | Brief acceleration peak |
| SPI Clock Frequency | $f_{CLK}$ | — | — | 4.0 | MHz | SPI communication clock |
| High-Side On-Resistance | $R_{DS(ON)\_H}$ | — | 250 | — | $\text{m}\Omega$ | $T_J = 25^\circ\text{C}$ |
| Low-Side On-Resistance | $R_{DS(ON)\_L}$ | — | 250 | — | $\text{m}\Omega$ | $T_J = 25^\circ\text{C}$ |
| Thermal Pre-Warning Temp | $T_{PW}$ | 110 | 120 | 130 | °C | Flagged in `DRV_STATUS` |
| Thermal Shutdown Temp | $T_{TSD}$ | 150 | 165 | 180 | °C | Full bridge shutoff |

## Usage

### Wiring to an Arduino / 3D printer controller (SPI mode)

| TMC2130 Pin | → | Microcontroller / Motherboard | Notes |
|---|---|---|---|
| `VM` | | Motor Supply ($+12\text{V}$ or $+24\text{V}$) | Dedicated bulk $100\ \mu\text{F}$ capacitor required |
| `GND` (Motor) | | Power Supply Ground | Heavy ground return |
| `VIO` | | Logic Supply ($+3.3\text{V}$ or $+5.0\text{V}$) | Match MCU logic level |
| `GND` (Logic) | | MCU Ground | Common ground |
| `STEP` | | MCU Digital Pin (Step Clock) | Hardware timer pin |
| `DIR` | | MCU Digital Pin (Direction) | Standard I/O pin |
| `CS` | | MCU Digital Pin (e.g. D10) | Unique Chip Select pin per axis |
| `SCK` | | MCU SPI Clock (SCK, D13) | Shared SPI bus |
| `SDI` | | MCU SPI MOSI (MOSI, D11) | Shared SPI bus |
| `SDO` | | MCU SPI MISO (MISO, D12) | Shared SPI bus |
| `DIAG1` | | MCU Endstop Input Pin | Connect for StallGuard sensorless homing |

> [!WARNING]
> Power Sequencing Caution:
> - **Always ensure motor power ($V_M$) is energized before or simultaneously with logic power ($V_{IO}$).**
> - If $V_{IO}$ is applied while $V_M$ is completely disconnected, current can back-feed through internal electrostatic discharge (ESD) protection diodes into the motor rail, causing erratic behavior and potential thermal damage to the driver IC.
> - Never disconnect motor windings while powered; inductive transients will instantly destroy the MOSFETs.

### Arduino code example using `TMCStepper`

```cpp
#include <TMCStepper.h>

#define EN_PIN       7  // Enable
#define DIR_PIN      8  // Direction
#define STEP_PIN     9  // Step
#define CS_PIN      10  // Chip Select
#define R_SENSE  0.11f  // SilentStepStick 0.11 Ohm sense resistor

TMC2130Stepper driver(CS_PIN, R_SENSE);

void setup() {
  Serial.begin(115200);
  SPI.begin();

  pinMode(EN_PIN, OUTPUT);
  pinMode(DIR_PIN, OUTPUT);
  pinMode(STEP_PIN, OUTPUT);
  digitalWrite(EN_PIN, LOW); // Enable driver in hardware

  // Initialize TMC2130 via SPI
  driver.begin();
  driver.toff(5);                 // Enable driver chopper
  driver.rms_current(800);        // Set motor current to 800mA RMS
  driver.microsteps(16);          // 1/16 microstepping with 1/256 interpolation
  driver.en_pwm_mode(true);       // Enable StealthChop for silent operation
  driver.pwm_autoscale(true);     // Dynamic voltage compensation
  driver.diag1_stall(true);       // Route StallGuard to DIAG1
  driver.sgt(2);                  // StallGuard sensitivity (-64 to +63)
}

void loop() {
  digitalWrite(DIR_PIN, HIGH);
  for (int i = 0; i < 3200; i++) {
    digitalWrite(STEP_PIN, HIGH);
    delayMicroseconds(200);
    digitalWrite(STEP_PIN, LOW);
    delayMicroseconds(200);
  }
  delay(1000);

  digitalWrite(DIR_PIN, LOW);
  for (int i = 0; i < 3200; i++) {
    digitalWrite(STEP_PIN, HIGH);
    delayMicroseconds(200);
    digitalWrite(STEP_PIN, LOW);
    delayMicroseconds(200);
  }
  delay(1000);
}
```

## Common mistakes

- **Solder jumpers configured in Standalone mode:** Many SilentStepStick breakout modules are shipped from the factory with surface-mount solder jumpers bridged for standalone mode (using external CFG pins for microstepping). To use SPI mode, the underside solder jumpers must be desoldered or configured for SPI mode according to the module manufacturer's schematic.
- **Connecting DIAG1 directly to 5V pulled-up endstop headers:** The DIAG pins on the TMC2130 operate at $3.3\text{ V}$ logic levels. Connecting a DIAG pin to an older 8-bit board with a hard $5\text{ V}$ pull-up resistor can overvoltage the open-drain pin and cause latch-up.
- **Incorrect StallGuard `SGT` threshold calibration:** StallGuard sensitivity depends heavily on motor speed, temperature, and mechanical friction. Setting `SGT` too high causes false triggers during normal acceleration; setting it too low results in violent grinding against axis frames before stall is detected.
- **Inadequate cooling in StealthChop mode:** StealthChop dissipates slightly more thermal energy in the motor coils and driver silicon than SpreadCycle. Always attach the provided aluminum heatsink and maintain active fan airflow in 3D printer electronics bays.

## Notes

- **TMC2130 vs TMC2209:** While the TMC2130 uses a traditional 4-wire SPI bus (requiring separate CS pins for each axis), the newer TMC2209 uses a single-wire UART bus with 4 hardware addresses, higher current capability ($2.0\text{ A}$ RMS), and lower heat generation. However, the TMC2130 remains a benchmark driver due to its deterministic, high-bandwidth SPI interface.
