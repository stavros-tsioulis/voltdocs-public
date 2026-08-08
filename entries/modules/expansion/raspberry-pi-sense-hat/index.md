## Overview

The **Raspberry Pi Sense HAT** is an official multi-sensor expansion board manufactured by the Raspberry Pi Foundation. Developed originally for the **Astro Pi mission** onto the International Space Station (ISS), it turns any 40-pin Raspberry Pi into an integrated environmental and space science laboratory.

Fitting onto the 40-pin GPIO header, the Sense HAT integrates:
- An **$8 \times 8$ RGB LED matrix** driven by an ATtiny88 microcontroller and LED2472G constant-current drivers.
- A **5-button miniature directional joystick** (Up, Down, Left, Right, Center Click).
- An **LSM9DS1 9-DOF IMU** (3-axis accelerometer, 3-axis gyroscope, 3-axis magnetometer).
- An **LPS25H barometric pressure & temperature sensor**.
- An **HTS221 relative humidity & temperature sensor**.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 5.0 V DC (powered directly from Pi 40-pin header 5V rail) |
| **Form factor** | Standard Raspberry Pi HAT footprint ($65 \times 56\text{ mm}$) |
| **Display** | $8 \times 8$ RGB LED Matrix (15-bit color depth / 32,768 colors) |
| **Input control** | 5-way directional joystick (Up, Down, Left, Right, Enter) |
| **Motion sensing** | 9-DOF IMU (LSM9DS1: $\pm 16g$ accel, $\pm 2000\text{ dps}$ gyro, $\pm 16\text{ gauss}$ mag) |
| **Environmental sensing**| Pressure $260\dots 1260\text{ hPa}$ (LPS25H) & Humidity $0\dots 100\%$ RH (HTS221) |
| **Interface** | $I^2C$ bus 1 (`/dev/i2c-1`) |

## Onboard ICs & $I^2C$ Addresses

| Function | Integrated Circuit | $I^2C$ Address | Description |
|---|---|---|---|
| 9-DOF IMU (Accel & Gyro)| STMicroelectronics LSM9DS1 | **`0x6A`** | 3-axis accelerometer + 3-axis gyroscope |
| 9-DOF IMU (Magnetometer)| STMicroelectronics LSM9DS1 | **`0x1C`** | 3-axis digital magnetometer |
| Barometer & Temp | STMicroelectronics LPS25H | **`0x5C`** | $260\text{--}1260\text{ hPa}$ pressure sensor |
| Humidity & Temp | STMicroelectronics HTS221 | **`0x5F`** | $0\text{--}100\%$ relative humidity sensor |
| LED Matrix & Joystick | Atmel ATtiny88 MCU | **`0x46`** | Co-processor managing 64 RGB LEDs and joystick |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{5V}$ | 4.8 | 5.0 | 5.25 | V | Power from Pi 5V rail |
| Operating Current | $I_{CC}$ | — | 450 | 600 | mA | LEDs active at 100% brightness |
| Barometer Accuracy | $P_{acc}$ | -1.0 | $\pm 0.2$ | +1.0 | hPa | Relative pressure accuracy |
| Humidity Accuracy | $H_{acc}$ | -3.5 | $\pm 1.5$ | +3.5 | % RH | Across $20\%\text{ to }80\%\text{ RH}$ |
| Temperature Accuracy | $T_{acc}$ | -0.5 | $\pm 0.2$ | +0.5 | °C | Across $15^\circ\text{C}\text{ to }40^\circ\text{C}$ |
| Joystick Pins | — | — | 5 | — | — | Mapped to ATtiny88 register |

## Python Software Installation & Setup

Enable $I^2C$ and install the official Raspberry Pi `sense-hat` Python library:

```bash
sudo raspi-config # Enable I2C under Interface Options
sudo apt-get update
sudo apt-get install sense-hat
```

## Python Code Example

```python
from sense_hat import SenseHat
import time

sense = SenseHat()

# Clear LED matrix
sense.clear()

# Display scrolling text message
sense.show_message("Astro Pi Online!", scroll_speed=0.05, text_colour=[0, 255, 0])

# Read environmental sensors
temp = sense.get_temperature()
humidity = sense.get_humidity()
pressure = sense.get_pressure()

print(f"Temperature: {temp:.2f} °C")
print(f"Humidity:    {humidity:.2f} % RH")
print(f"Pressure:    {pressure:.2f} hPa")

# Read 9-DOF IMU Orientation (Yaw, Pitch, Roll)
orientation = sense.get_orientation_degrees()
print(f"Pitch: {orientation['pitch']:.1f}° | Roll: {orientation['roll']:.1f}° | Yaw: {orientation['yaw']:.1f}°")

# Display a red pixel at center (x=3, y=3)
sense.set_pixel(3, 3, 255, 0, 0)
time.sleep(2)
sense.clear()
```

## Common mistakes

- **CPU self-heating offset on temperature:** Because the Sense HAT sits directly above the warm Raspberry Pi CPU SoC, heat radiating from the Pi CPU warms the board PCB, causing temperature readings to read **$+3^\circ\text{C}$ to $+5^\circ\text{C}$ higher** than ambient room temperature. Use a GPIO ribbon cable or standoff tower to isolate the HAT, or apply CPU temperature offset compensation in software.
- **Forgetting $I^2C$ kernel module enablement:** If `sense.get_temperature()` throws an $I^2C$ device error, run `sudo raspi-config` and ensure $I^2C$ is enabled in the Raspberry Pi OS kernel.

## Notes

- **Sense HAT vs Sense HAT V2:** The original Sense HAT uses LSM9DS1 + LPS25H; updated revisions use LSM6DSOX + LIS3MDL + LPS22HB.
