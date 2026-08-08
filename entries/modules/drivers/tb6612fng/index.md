## Overview

The **TB6612FNG** is a dual H-bridge motor driver IC manufactured by Toshiba. Built using high-efficiency DMOS output power transistors instead of legacy bipolar transistors, it delivers much higher efficiency, lower heat output, and minimal voltage drop compared to traditional drivers like the L298N or L293D.

It can drive two independent DC motors or one 4-wire bipolar stepper motor at continuous output currents up to **1.2 A per channel** (3.2 A peak) with motor supply voltages from **2.5 V to 13.5 V DC**.

## Quick reference

| | |
|---|---|
| **Motor supply (`VM` / `VCC`)** | 2.5 V to 13.5 V DC |
| **Logic supply (`VCC` / `VCC1`)** | 2.7 V to 5.5 V DC (3.3V and 5V MCU compatible) |
| **Continuous current per channel** | 1.2 A |
| **Peak output current** | 3.2 A (single pulse $<20\text{ ms}$) |
| **MOSFSET $R_{DS(ON)}$** | $0.5\text{ }\Omega$ total (high + low side combined) |
| **PWM frequency** | Up to 100 kHz |
| **Standby control (`STBY`)** | Hardware standby pin (`LOW` = Power-down, `HIGH` = Active) |

## Pinout

### Standard Pololu / SparkFun Breakout Board Pinout

```
           ┌──────────┐
     VM ───│ 1     16 │─── A01
    VCC ───│ 2     15 │─── A02
    GND ───│ 3     14 │─── GND
    AO1 ───│ 4     13 │─── B02
    AO2 ───│ 5     12 │─── B01
    BO2 ───│ 6     11 │─── VM
    BO1 ───│ 7     10 │─── PWMB
   STBY ───│ 8      9 │─── BIN2
           └──────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1, 11 | `VM` | Power Input | Motor power supply voltage (+2.5 V to +13.5 V DC) |
| 2 | `VCC` | Power Input | Logic supply voltage (+2.7 V to +5.5 V DC) |
| 3, 14 | `GND` | Power | Ground (0 V) |
| 4 | `AO1` / `A01` | Driver Output | Motor A Output 1 |
| 5 | `AO2` / `A02` | Driver Output | Motor A Output 2 |
| 6 | `BO2` / `B02` | Driver Output | Motor B Output 2 |
| 7 | `BO1` / `B01` | Driver Output | Motor B Output 1 |
| 8 | `STBY` | Digital Input | Standby input (`LOW` = Power-down, `HIGH` = Enable outputs) |
| 9 | `BIN2` | Digital Input | Motor B Direction Input 2 |
| 10 | `PWMB` | Digital Input | Motor B PWM Speed Control input |
| 12 | `BIN1` | Digital Input | Motor B Direction Input 1 |
| 13 | `PWMA` | Digital Input | Motor A PWM Speed Control input |
| 15 | `AIN2` | Digital Input | Motor A Direction Input 2 |
| 16 | `AIN1` | Digital Input | Motor A Direction Input 1 |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Motor Voltage | $V_M$ | 2.5 | 6.0 / 12.0 | 13.5 | V | DC |
| Logic Voltage | $V_{CC}$ | 2.7 | 3.3 / 5.0 | 5.5 | V | DC |
| Output Current (Continuous) | $I_{OUT}$ | -1.2 | — | 1.2 | A | Per channel |
| Output Current (Peak Pulse) | $I_{PEAK}$ | -3.2 | — | 3.2 | A | $t < 20\text{ ms}$ |
| High-Side + Low-Side $R_{DS(ON)}$ | $R_{ON}$ | — | 0.5 | 0.7 | Ω | $I_{OUT} = 1\text{ A}$, $V_M = 5\text{ V}$ |
| PWM Frequency | $f_{PWM}$ | — | — | 100 | kHz | |
| Standby Current | $I_{STBY}$ | — | 0 | 10 | µA | $STBY = LOW$ |

## Control Logic Truth Table (Motor A)

| `STBY` | `AIN1` | `AIN2` | `PWMA` | `AO1` | `AO2` | Motor Mode |
|---|---|---|---|---|---|---|
| **`HIGH`** | `HIGH` | `LOW` | **`HIGH`** | **`HIGH`** | **`LOW`** | Forward |
| **`HIGH`** | `LOW` | `HIGH` | **`HIGH`** | **`LOW`** | **`HIGH`** | Reverse |
| **`HIGH`** | `HIGH` | `LOW` | **`LOW`** | **`LOW`** | **`LOW`** | Short Brake (Low-side ON) |
| **`HIGH`** | `LOW` | `LOW` | `X` | **`LOW`** | **`LOW`** | Short Brake (Low-side ON) |
| **`LOW`** | `X` | `X` | `X` | `Z` | `Z` | Standby / Coast (High-Z) |

## Wiring

| TB6612FNG Pin | → | Microcontroller / Motor / Power | Notes |
|---|---|---|---|
| `VCC` | | `3.3V` or `5V` | Logic supply |
| `GND` | | Common `GND` | MCU GND + Motor Power GND |
| `VM` | | External Motor Battery (+2.5 V to +13.5 V) | Dedicated motor power rail |
| `STBY` | | MCU `3.3V`/`5V` rail (or GPIO Pin) | **Must be pulled HIGH to enable driver** |
| `AIN1`, `AIN2` | | Digital GPIO Pins (e.g. D4, D5) | Direction control for Motor A |
| `PWMA` | | PWM Pin (e.g. D3) | Speed control for Motor A |
| `AO1`, `AO2` | | Motor A Terminals | Connects to DC Motor A |

> [!WARNING]
> Floating STBY Pin Failure:
> Pin `STBY` is active-HIGH. If `STBY` is left floating or connected to `LOW`, all driver outputs remain in high-impedance standby mode and the motor will not spin.

## Common mistakes

- **Leaving STBY pin disconnected:** Driver stays in ultra-low power standby mode.
- **Exceeding 13.5V motor voltage:** Unlike the L298N (which accepts up to 46V), the TB6612FNG maximum VM rating is **13.5 V DC**. Connecting a 4S LiPo battery (16.8V) will destroy the IC.
- **Forgetting common ground:** Not connecting motor battery ground to MCU ground prevents control logic signals from functioning.

## Notes

- Low internal MOSFET resistance ($0.5\text{ }\Omega$) delivers over 90% of supply voltage directly to the motor, producing significantly less heat than Darlington drivers.
