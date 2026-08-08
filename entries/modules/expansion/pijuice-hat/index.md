## Overview

The **PiJuice HAT** is an intelligent hardware Uninterruptible Power Supply (UPS) and battery management HAT engineered by Pi Supply (Nebra) for the Raspberry Pi (compatible with Pi 5, 4B, 3B+, 3A+, Zero, and Zero 2 W).

Equipped with an onboard **STM32 microcontroller**, a **1820 mAh Motorola BP6X LiPo battery** (swappable and expandable to larger LiPo/LiFePO4 cells up to 12,000+ mAh), a hardware Real-Time Clock (RTC), two programmable RGB status LEDs, and a soft power button, the PiJuice HAT ensures continuous 24/7 uptime during AC power outages. It streams battery percentage, charging current, voltage, and temperature telemetry over $I^2C$ (**`0x14`**).

## Quick reference

| | |
|---|---|
| **Input Power** | 4.2V to 10V DC via Micro-USB / USB-C / Solar Header |
| **Output Power** | 5.2V DC up to 2.5A continuous to Raspberry Pi GPIO 5V rail |
| **Default Battery** | 1820 mAh Motorola BP6X LiPo cell (included) |
| **Interface** | $I^2C$ (`0x14` default, software configurable) |
| **Power Management MCU**| Onboard STM32F030C8T6 32-bit ARM Cortex-M0 |
| **Battery Fuel Gauge** | LC709203F battery capacity fuel gauge IC |
| **Battery Charger IC** | TI BQ24160 highly-integrated switch-mode charger |
| **Hardware RTC** | Integrated Real-Time Clock with alarm wake-up |
| **Solar Input** | Dedicated onboard solar panel charging pads (4.2V–10V) |

## Pinout (Raspberry Pi 40-Pin GPIO Header Connections)

The PiJuice HAT plugs directly onto the Raspberry Pi 40-pin GPIO header:

| Pin | Name | Description |
|---|---|---|
| 2, 4 | `5V Power` | Supplies regulated 5.2V DC power from battery boost converter to Pi |
| 6, 9, 14, 20, 25 | `GND` | Common ground reference |
| 3 | `SDA (GPIO 2)` | $I^2C$ Data line (`0x14` address) |
| 5 | `SCL (GPIO 3)` | $I^2C$ Clock line |
| — | `Micro-USB / USB-C`| Power charge input on PiJuice PCB |
| — | `Solar Terminal` | 2-pin header for 4.2V–10V solar panel input |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Charge Input Voltage | $V_{in}$ | 4.2 | 5.0 | 10.0 | V | Micro-USB / Solar input |
| Regulated Output Voltage| $V_{out}$ | 5.1 | 5.2 | 5.3 | V | Boost converter to Pi 5V rail |
| Continuous Output Current| $I_{out}$ | — | 2.5 | 3.0 | A | Peak burst output |
| Included Battery Capacity| $Cap$ | — | 1820 | — | mAh | Standard BP6X LiPo cell |
| Standby Sleep Draw | $I_{sleep}$| — | 20 | — | µA | Low power deep sleep |
| Operating Temperature | $T_{opr}$ | -20 | — | 60 | °C | Thermal safety shutdown at 60°C |

## Soft Power Button & Automated Shutdown Features

- **Soft Power Off:** Pressing the onboard power button initiates a graceful OS shutdown script (`sudo shutdown -h now`) before cutting 5V power to the Pi.
- **Auto-Boot on Power Restoration:** When AC mains or solar power returns, the PiJuice automatically powers on the Pi once the battery reaches a configurable charge threshold (e.g. $>15\%$).
- **Watchdog Timer:** Onboard MCU acts as a hardware watchdog timer; if the Pi OS freezes, the PiJuice power-cycles the 5V power rail.

## Wiring (Stand-Alone Raspberry Pi Integration)

Simply mount the PiJuice HAT onto the 40-pin GPIO header of any Raspberry Pi model. Connect main USB power to the **PiJuice USB port** rather than the Raspberry Pi USB port.

## Example (Python `pijuice` Library)

```python
import time
from pijuice import PiJuice

# Connect to PiJuice I2C interface (Address 0x14)
pijuice = PiJuice(1, 0x14)

# Query battery status & charge percentage
status = pijuice.status.GetStatus()
charge = pijuice.status.GetChargeLevel()
voltage = pijuice.status.GetBatteryVoltage()
current = pijuice.status.GetBatteryCurrent()

print("--- PiJuice HAT Telemetry ---")
print(f"Battery Charge Level: {charge['data']}%")
print(f"Battery Voltage: {voltage['data']} mV")
print(f"Battery Current: {current['data']} mA")
print(f"Power Input Status: {status['data']['powerInput']}")
print(f"Battery Status: {status['data']['battery']}")
```

## Common mistakes

- **Plugging USB power into the Pi instead of the PiJuice:** Connecting the main USB power cable to the Raspberry Pi instead of the PiJuice micro-USB/USB-C port bypasses the charging circuit, leaving the battery uncharged.
- **Using an underpowered USB power brick:** Supplying $<2.0\text{A}$ from cheap phone chargers prevents the BQ24160 charger from simultaneously powering the Pi and charging the LiPo battery.

## Notes

- **PiJuice HAT vs Adafruit PowerBoost 1000C:** PiJuice includes an onboard MCU, RTC, $I^2C$ telemetry, software daemon, and Pi 40-pin GPIO header footprint; PowerBoost is a standalone boost/charger breakout PCB.
