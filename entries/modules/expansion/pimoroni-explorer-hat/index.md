## Overview

The **Pimoroni Explorer HAT Pro** is a beginner-friendly, multifunction expansion board designed for the Raspberry Pi. Fitting directly onto the 40-pin GPIO header, it turns the Pi into a prototyping and robotics workstation by adding motor drivers, analog sensing, 5V buffered outputs, touch inputs, and mini breadboard prototyping space.

The HAT integrates three specialized ICs:
1. **Texas Instruments DRV8833:** Dual H-bridge motor driver capable of driving two DC motors or one 4-wire stepper motor at up to $1.2\text{ A}$ peak per channel.
2. **Texas Instruments ADS1015:** 4-channel 12-bit Analog-to-Digital Converter (ADC) allowing 5V analog sensors (potentiometers, light sensors, distance sensors) to be read by the Pi over $I^2C$.
3. **Microchip CAP1204:** 4-channel capacitive touch controller driving 4 touch pads (labeled 1, 2, 3, 4) on the HAT surface.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 5.0 V DC (powered from Pi 40-pin header 5V pins) |
| **Form factor** | Standard Raspberry Pi HAT footprint ($65 \times 56\text{ mm}$) |
| **Motor driver** | Dual H-bridge (DRV8833) for 2 DC motors (200 mA continuous / 1.2 A peak) |
| **Analog inputs** | 4 channels (ADS1015 12-bit ADC, $0\text{ to }5\text{V}$ input range) |
| **Buffered 5V outputs** | 4 5V-tolerant sinking outputs (Darlington array, $500\text{ mA}$ max total) |
| **Touch inputs** | 4 capacitive touch pads + 4 alligator clip pads |
| **Status LEDs** | 4 color LEDs (Blue, Green, Yellow, Red) |
| **Prototyping area** | Mini 170-point solderless breadboard pre-attached to HAT center |

## Onboard ICs & $I^2C$ Addresses

- **ADS1015 ADC:** $I^2C$ address **`0x48`** (Reads analog channels 1, 2, 3, 4).
- **CAP1204 Touch Controller:** $I^2C$ address **`0x28`** (Reads touch pads 1, 2, 3, 4 and alligator clip pads).
- **DRV8833 Motor Driver:** Controlled directly via Pi GPIO pins:
  - Motor 1: GPIO 19 (`M1+`) & GPIO 20 (`M1-`)
  - Motor 2: GPIO 21 (`M2+`) & GPIO 26 (`M2-`)

## Pinout & Connector Headers

### Screw Terminals & 0.1" Female Headers

| Header Label | Function | Voltage / Logic | Description |
|---|---|---|---|
| `Motor 1` (`+` / `-`)| Motor 1 Output | 5V PWM | Connect DC Motor 1 |
| `Motor 2` (`+` / `-`)| Motor 2 Output | 5V PWM | Connect DC Motor 2 |
| `Analog 1`–`4` | Analog Inputs | 0V to 5V DC | ADS1015 ADC Inputs 1, 2, 3, 4 |
| `Output 1`–`4` | 5V Buffered Out | 5V Sinking (500mA) | Drive relays, solenoids, or high-current LEDs |
| `Input 1`–`4` | 5V Tolerant In | 3.3V / 5V Logic | Protected digital inputs with pull-down resistors |
| `Touch 1`–`4` | Capacitive Touch | Touch sense | Capacitive touch pads on PCB edge |
| `5V` / `GND` | Power Rails | 5.0V / 0V | Power supply rail for external sensors |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{5V}$ | 4.8 | 5.0 | 5.25 | V | Power from Pi 5V rail |
| Motor Continuous Current | $I_{motor}$ | — | 200 | 500 | mA | Continuous load per channel |
| Motor Peak Current | $I_{peak}$ | — | 1200 | 1500 | mA | $<500\text{ ms}$ stall current |
| Analog Input Voltage Range| $V_{analog}$| 0.0 | — | 5.0 | V | 5V protected inputs |
| ADC Resolution | $Res_{ADC}$ | — | 12 | — | bits | ADS1015 ($1\text{ mV}$ LSB) |
| Output Sink Current Total | $I_{out\_total}$| — | — | 500 | mA | All 4 outputs combined |

## Python Software Installation & Architecture

Pimoroni provides an official Python library (`explorerhat`):

```bash
sudo apt-get update
sudo apt-get install python3-pip
sudo pip3 install explorerhat
```

## Python Code Example

```python
import explorerhat
import time

print("Explorer HAT Pro Test Script")

# Light status LEDs
explorerhat.light.blue.on()
explorerhat.light.green.on()

# Read 5V Analog input channel 1
analog_val = explorerhat.analog.one.read()
print(f"Analog Channel 1 Voltage: {analog_val:.2f} V")

# Run DC Motor 1 forward at 80% speed for 2 seconds
print("Running Motor 1 forward...")
explorerhat.motor.one.forwards(80)
time.sleep(2)
explorerhat.motor.one.stop()

# Define capacitive touch callback function
def touch_callback(channel, event):
    print(f"Touch pad {channel} was {event}!")
    explorerhat.light.red.toggle()

# Register callback for touch pad 1
explorerhat.touch.one.pressed(touch_callback)

print("Touch pads active. Press Ctrl+C to exit.")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    explorerhat.light.off()
    explorerhat.motor.stop()
```

## Common mistakes

- **Connecting high-voltage motors ($>5\text{V}$):** The Explorer HAT motor driver is powered directly from the Raspberry Pi's 5V power bus. Do not connect motors that draw $>5\text{V}$ or $>1.2\text{ A}$, as excessive current draw causes Raspberry Pi brownout resets.
- **Forgetting common ground for external sensors:** When powering external sensors from an external power supply, ensure external `GND` is tied to the Explorer HAT `GND` header pin.

## Notes

- **Explorer HAT vs Explorer HAT Pro:** The Pro version adds the DRV8833 dual motor driver, 4 5V-tolerant analog inputs, and 4 5V-buffered outputs; the standard non-Pro version lacks motor control and analog inputs.
