## Overview

The **DRV8880** is a complete microstepping bipolar stepper motor driver IC designed by Texas Instruments. It integrates two N-channel power MOSFET H-bridges, current-sensing regulation circuitry, a microstepping indexer, and TI's proprietary **AutoTune™** adaptive decay technology.

In conventional stepper drivers (such as the A4988 or DRV8825), designers must select a fixed fast/slow decay ratio or manually calibrate decay trimpots to prevent current waveform distortion, audible squeal, and missed steps as motor speed, back-EMF, and supply voltage change. The DRV8880 eliminates this manual tuning by dynamically monitoring the current decay on every PWM chopping cycle and adapting the decay mode between fast and slow decay to achieve an ideal current waveform.

Operating from a motor supply of $6.5\text{ V}$ to $45.0\text{ V}$, the DRV8880 delivers up to $1.4\text{ A}$ RMS ($2.0\text{ A}$ full-scale peak) per phase. It features dual digital torque scaling pins (`TRQ0`, `TRQ1`) that dynamically scale winding current down to 75%, 50%, or 25% for power reduction during holding or idle states without altering the analog $V_{REF}$ potentiometer. The IC is available in a 28-pin HTSSOP package with thermal PowerPAD and on standard 16-pin StepStick-compatible breakout carrier modules (such as Pololu #2971).

## Quick reference

| Parameter | Value | Notes |
|---|---|---|
| **Motor Supply Voltage ($V_M$)** | $6.5\text{ V}$ to $45.0\text{ V}$ DC | Absolute maximum $47\text{ V}$ |
| **Full-Scale Current ($I_{FS}$)** | Up to $2.0\text{ A}$ peak ($1.4\text{ A}$ RMS) | Set via $V_{REF}$, sense resistors, and torque inputs |
| **Logic Compatibility** | $3.3\text{ V}$ and $5\text{ V}$ logic compatible | Built-in $3.3\text{ V}$ LDO (`V3P3` pin, $10\text{ mA}$ max) |
| **Microstep Resolutions** | Full (100% or 71%), 1/2, 1/4, 1/8, 1/16 | Configured via `M0` and `M1` tri-state inputs |
| **Decay Modes** | AutoTune, Slow, Mixed (30% or 60% fast) | Selected via `DECAY` pin |
| **Torque Scaling** | 100%, 75%, 50%, 25% | Configured dynamically via `TRQ0` / `TRQ1` |
| **MOSFET $R_{DS(ON)}$** | $560\text{ m}\Omega$ typical | High-side + low-side switch total at $25^\circ\text{C}$ |
| **Protection Features** | UVLO, OCP, TSD, Charge Pump UVLO | Fault signaled via active-low open-drain `nFAULT` |

## Terminals

### StepStick breakout carrier pinout

The standard 16-pin carrier module format (Pololu pinout) organizes control and power connections along two 8-pin 0.1" pitch headers:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `ENABLE` | Digital Input | Active-low driver enable. Low = outputs enabled, High = outputs high-Z. |
| 2 | `M0` | Digital Input | Microstep resolution selector pin 0 (tri-state logic). |
| 3 | `M1` | Digital Input | Microstep resolution selector pin 1 (tri-state logic). |
| 4 | `TRQ0` | Digital Input | Torque scaling input 0 (internal pull-down). |
| 5 | `TRQ1` | Digital Input | Torque scaling input 1 (internal pull-down). |
| 6 | `SLEEP` | Digital Input | Active-low low-power sleep mode input. Low = sleep, High = normal operation. |
| 7 | `STEP` | Digital Input | Step pulse input. Rising edge advances the motor one indexer step. |
| 8 | `DIR` | Digital Input | Direction input. Logic High = clockwise, Low = counter-clockwise. |
| 9 | `GND` | Power | Logic and ground reference ($0\text{ V}$). |
| 10 | `FAULT` | Digital Output | Active-low open-drain fault indicator (`nFAULT`). Pull up externally. |
| 11 | `A2` | Motor Output | Bipolar stepper motor winding coil A (terminal 2). |
| 12 | `A1` | Motor Output | Bipolar stepper motor winding coil A (terminal 1). |
| 13 | `B1` | Motor Output | Bipolar stepper motor winding coil B (terminal 1). |
| 14 | `B2` | Motor Output | Bipolar stepper motor winding coil B (terminal 2). |
| 15 | `GND` | Power | Motor power ground reference. |
| 16 | `VMOT` | Power | Motor power supply ($+6.5\text{ V}$ to $+45.0\text{ V}$ DC). |

*Note: The carrier board also breaks out `V3P3` ($3.3\text{ V}$ internal regulator output), `VREF`, and `DECAY` via surface-mount test points or secondary header pins.*

### IC Pinout (28-pin HTSSOP PWP)

| Pin | Name | Function | Pin | Name | Function |
|---|---|---|---|---|---|
| 1 | `VM` | Motor supply rail | 15 | `V3P3` | 3.3V internal LDO output |
| 2 | `AOUT1` | H-bridge A output 1 | 16 | `nFAULT` | Fault indicator (active-low OD) |
| 3 | `TRQ1` | Torque scale input 1 | 17 | `M1` | Microstep configuration 1 |
| 4 | `AISEN` | H-bridge A current sense | 18 | `M0` | Microstep configuration 0 |
| 5 | `AOUT2` | H-bridge A output 2 | 19 | `DECAY` | Decay mode selection pin |
| 6 | `GND` | Ground | 20 | `TOFF` | Off-time selection pin |
| 7 | `CPH` | Charge pump fly-cap high | 21 | `TRQ0` | Torque scale input 0 |
| 8 | `CPL` | Charge pump fly-cap low | 22 | `VREF` | Reference voltage analog input |
| 9 | `VCP` | Charge pump reservoir cap | 23 | `nSLEEP` | Sleep mode input (active-low) |
| 10 | `BOUT2` | H-bridge B output 2 | 24 | `STEP` | Step clock input |
| 11 | `BISEN` | H-bridge B current sense | 25 | `DIR` | Direction input |
| 12 | `BOUT1` | H-bridge B output 1 | 26 | `ENABLE` | Enable input (active-low) |
| 13 | `GND` | Ground | 27 | `VINT` | Internal bias bypass capacitor |
| 14 | `V3P3OUT` | 3.3V LDO filter pin | 28 | `VM` | Motor supply rail |
| PAD | `PAD` | Exposed thermal pad (must be soldered to ground plane) | — | — | — |

## The technical core

### AutoTune™ adaptive decay mode

Conventional chopper drivers suffer from current distortion when motor back-EMF increases or during decreasing current half-cycles. Slow decay produces current runaway and waveform distortion when current decays slower than the back-EMF waveform envelope; fast decay causes high current ripple and acoustic motor hiss.

The DRV8880 solves this with **AutoTune™** mode, enabled by setting the `DECAY` pin to High ($3.3\text{ V}$) or leaving it configured as default on AutoTune carrier boards:
- AutoTune samples the winding current decay rate during the initial slow decay segment.
- If current fails to decay below the target regulation threshold within the allotted time, it automatically introduces an optimal ratio of fast decay for the remaining off-time.
- The decay ratio updates continuously on a cycle-by-cycle basis, adapting to speed variations, motor heating, and changing coil inductance without any user intervention.

### Microstep configuration

The microstep mode is configured through the tri-state inputs `M0` and `M1`:

| `M1` Level | `M0` Level | Microstep Resolution | Current Profile |
|---|---|---|---|
| Low | Low | Full Step | 100% current (high torque) |
| Low | High | Full Step | 71% current (balanced) |
| Low | Hi-Z (Floating) | 1/2 Step | Non-circular (100% torque) |
| High | Low | 1/2 Step | Circular (sine/cosine) |
| High | High | 1/4 Step | Circular (sine/cosine) |
| High | Hi-Z (Floating) | 1/8 Step | Circular (sine/cosine) |
| Hi-Z (Floating) | Low | 1/16 Step | Circular (sine/cosine) |
| Hi-Z (Floating) | High | 1/16 Step | Circular (sine/cosine) |

### Torque scaling DAC

The digital inputs `TRQ0` and `TRQ1` permit software-controlled real-time torque scaling:

| `TRQ1` | `TRQ0` | Current Scaling Factor ($\text{TRQ}\%$) | Typical Use Case |
|---|---|---|---|
| Low | Low | **100%** | High-acceleration / heavy payload movement |
| Low | High | **75%** | Standard cruising velocity |
| High | Low | **50%** | Low-speed maneuvering or low-load axes |
| High | High | **25%** | Motor holding / standstill power-saving mode |

### Current limiting calibration ($V_{REF}$)

The full-scale current limit ($I_{FS}$) per motor coil is established by the analog voltage on `VREF`, the external sense resistors ($R_{SENSE}$), and the torque scaling factor:

$$ I_{FS} = \frac{V_{REF}}{6.6 \times R_{SENSE}} \times \text{TRQ}\% $$

On typical StepStick breakout modules equipped with $0.200\ \Omega$ sense resistors and with torque set to 100% (`TRQ0` = Low, `TRQ1` = Low):

$$ I_{FS} = \frac{V_{REF}}{6.6 \times 0.200\ \Omega} = \frac{V_{REF}}{1.32\ \Omega} \approx 0.758 \times V_{REF} $$

$$\text{Conversely: } V_{REF} = I_{FS} \times 1.32\ \Omega $$

**Example:** To configure a peak phase current of $1.0\text{ A}$:
$$ V_{REF} = 1.0\text{ A} \times 1.32\ \Omega = 1.32\text{ V} $$

Measure $V_{REF}$ with a multimeter between the carrier trimmer wiper and `GND`.

### Electrical specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Motor Supply Voltage | $V_M$ | 6.5 | 24.0 | 45.0 | V | Operating range |
| Logic Input High | $V_{IH}$ | 2.0 | — | 5.5 | V | `STEP`, `DIR`, `ENABLE`, `SLEEP` |
| Logic Input Low | $V_{IL}$ | -0.3 | — | 0.7 | V | `STEP`, `DIR`, `ENABLE`, `SLEEP` |
| Internal LDO Output | $V_{3P3}$ | 3.15 | 3.30 | 3.45 | V | $I_{LOAD} \le 10\text{ mA}$ |
| High-Side MOSFET $R_{DS(ON)}$ | $R_{DS(ON)\_H}$ | — | 280 | — | $\text{m}\Omega$ | $I_O = 1\text{ A}$, $T_J = 25^\circ\text{C}$ |
| Low-Side MOSFET $R_{DS(ON)}$ | $R_{DS(ON)\_L}$ | — | 280 | — | $\text{m}\Omega$ | $I_O = 1\text{ A}$, $T_J = 25^\circ\text{C}$ |
| Overcurrent Trip Level | $I_{OCP}$ | 2.2 | 2.8 | 3.5 | A | Protection shutoff |
| Thermal Shutdown Temp | $T_{TSD}$ | 150 | 165 | 180 | °C | Junction temperature |
| Thermal Shutdown Hysteresis | $T_{HYS}$ | — | 15 | — | °C | Recovery band |
| Minimum Step Pulse Width | $t_{STEP\_PW}$ | 1.0 | — | — | µs | High or low minimum duration |

## Usage

### Wiring to a microcontroller

| DRV8880 Carrier Pin | → | Microcontroller / Power | Notes |
|---|---|---|---|
| `VMOT` | | Motor Power Supply ($+12\text{V}$ to $+36\text{V}$) | Place $100\ \mu\text{F}$ capacitor across VMOT/GND |
| `GND` (Motor) | | Power Supply Ground | Heavy power return |
| `GND` (Logic) | | MCU Ground | Common ground reference |
| `STEP` | | MCU Digital Pin (e.g. D2) | Pulse generator pin |
| `DIR` | | MCU Digital Pin (e.g. D3) | Direction signal |
| `ENABLE` | | MCU Digital Pin (e.g. D4) | Active-low; pull low to enable driver |
| `TRQ0` / `TRQ1` | | MCU Digital Pins or GND | Dynamic holding/run torque reduction |
| `SLEEP` | | MCU $3.3\text{V}$ or $5\text{V}$ | Must be tied High for active operation |
| `A1`, `A2` | | Stepper Motor Coil A | Bipolar motor lead pair 1 |
| `B1`, `B2` | | Stepper Motor Coil B | Bipolar motor lead pair 2 |

> [!WARNING]
> Inductive Spike Hazard:
> - Never disconnect or connect a stepper motor while `VMOT` is energized. Inductive flyback surges will instantly punch through the internal output MOSFETs.
> - A low-ESR bulk electrolytic capacitor (at least $47\ \mu\text{F}$ to $100\ \mu\text{F}$, rated for at least $50\text{ V}$) **MUST** be placed directly across `VMOT` and `GND` adjacent to the board pins to snub destructive LC resonant spikes.

### Arduino control example

```cpp
// DRV8880 Stepper Driver Demonstration with Dynamic Torque Scaling
const int pinStep   = 2;
const int pinDir    = 3;
const int pinEnable = 4;
const int pinTrq0   = 5;
const int pinTrq1   = 6;

void setTorque(uint8_t percent) {
  switch (percent) {
    case 100:
      digitalWrite(pinTrq1, LOW);
      digitalWrite(pinTrq0, LOW);
      break;
    case 75:
      digitalWrite(pinTrq1, LOW);
      digitalWrite(pinTrq0, HIGH);
      break;
    case 50:
      digitalWrite(pinTrq1, HIGH);
      digitalWrite(pinTrq0, LOW);
      break;
    case 25: // Holding current
    default:
      digitalWrite(pinTrq1, HIGH);
      digitalWrite(pinTrq0, HIGH);
      break;
  }
}

void stepMotor(int steps, int delayUs) {
  for (int i = 0; i < steps; i++) {
    digitalWrite(pinStep, HIGH);
    delayMicroseconds(delayUs);
    digitalWrite(pinStep, LOW);
    delayMicroseconds(delayUs);
  }
}

void setup() {
  pinMode(pinStep, OUTPUT);
  pinMode(pinDir, OUTPUT);
  pinMode(pinEnable, OUTPUT);
  pinMode(pinTrq0, OUTPUT);
  pinMode(pinTrq1, OUTPUT);

  // Enable driver (active-low)
  digitalWrite(pinEnable, LOW);
  setTorque(100);
}

void loop() {
  // Move clockwise with 100% torque
  setTorque(100);
  digitalWrite(pinDir, HIGH);
  stepMotor(3200, 400); // 3200 microsteps

  // Hold position with 25% standby current to save energy and keep driver cool
  setTorque(25);
  delay(1000);

  // Move counter-clockwise with 75% torque
  setTorque(75);
  digitalWrite(pinDir, LOW);
  stepMotor(3200, 400);

  setTorque(25);
  delay(1000);
}
```

## Common mistakes

- **Leaving `SLEEP` floating:** The `SLEEP` pin has no strong internal pull-up and floats low, keeping the device in standby mode where all outputs and charge pump are shut down. Tie `SLEEP` to logic High ($3.3\text{ V}$ or $5\text{ V}$) or `V3P3`.
- **Misunderstanding `TRQ0` / `TRQ1` defaults:** When left floating, the torque pins are pulled low internally, selecting 100% torque. If holding current is desired, actively drive them High.
- **Incorrect $V_{REF}$ calculation formula:** The DRV8880 current formula uses a gain factor of $K_V = 6.6$, unlike the A4988 ($K_V = 8.0$) or DRV8825 ($K_V = 2.0$). Using an A4988 or DRV8825 formula will severely miscalculate the phase current.
- **Missing bulk decoupling capacitor:** Ceramic capacitors without parallel electrolytic damping will form an LC tank circuit with supply wiring lead inductance, creating transient spikes above $50\text{ V}$ during switch-on that destroy the IC.

## Notes

- **AutoTune vs. DRV8825:** While the DRV8825 offers finer 1/32 microstepping, it requires careful decay tuning (or fast-decay diode hacks) to prevent mid-frequency resonance and missed steps at low speeds. The DRV8880 AutoTune feature provides smoother, quieter motion at 1/16 microstepping without manual tuning.
