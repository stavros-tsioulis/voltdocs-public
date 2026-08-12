## Overview

The **DRV8301** (DRV8301DCAR) is an integrated 3-phase gate driver IC manufactured by Texas Instruments. It is famous in open-source hardware communities as the foundational motor gate driver chip powering **VESC (Vedder Electronic Speed Controller)** electric skateboard motor controllers, high-power drones, combat robotics, and industrial BLDC servo drives.

Operating across a wide supply voltage range of **6.0V to 60.0V DC** ($2\text{S} \dots 14\text{S}$ LiPo batteries), the DRV8301 drives six external N-channel power MOSFETs arranged in a 3-phase inverter bridge with peak currents up to **1.7A source / 2.3A sink**. It incorporates an integrated **1.5A step-down buck regulator** (powering the system MCU at 3.3V or 5V), **two low-offset current-shunt amplifiers** for Field Oriented Control (FOC) current sensing, and an **SPI interface** for fault diagnostics and configuration.

## Quick reference

| | |
|---|---|
| **Power Supply Voltage (`PVDD`)**| 6.0 V to 60.0 V DC (65V absolute maximum) |
| **Gate Drive Current** | $1.7\text{ A}$ Peak Source / $2.3\text{ A}$ Peak Sink |
| **Integrated Buck Converter** | Adjustable $1.5\text{ A}$ output (3.3V or 5.0V step-down LDO supply) |
| **Current Sense Amplifiers** | 2x Independent programmable-gain current-shunt amplifiers |
| **PWM Control Modes** | 6-channel PWM inputs (Independent High/Low side control per phase) |
| **Protection Features** | Overcurrent Protection (OCP), Overtemperature (OTS), Short-Circuit, UVLO |
| **SPI Interface** | 4-wire SPI slave interface for fault reporting & register programming |
| **Package** | 56-pin HTSSOP (PowerPAD down) |

## Pinout & System Architecture (HTSSOP-56 Package)

```
       +6V to +60V Power Battery Rail
                  │
        ┌─────────┴─────────┐
        │     DRV8301       │ ──► [Phase A Gate High/Low] ──► 2x N-Channel FETs ──► Motor Phase A
        │  3-Phase Driver   │ ──► [Phase B Gate High/Low] ──► 2x N-Channel FETs ──► Motor Phase B
        │   + Buck Reg      │ ──► [Phase C Gate High/Low] ──► 2x N-Channel FETs ──► Motor Phase C
        └────┬──────────┬───┘
             │          │
   3.3V Power Out   SPI Diagnostics
   (Powers MCU)     & Config (nCS, SCLK, SDI, SDO)
```

## Key Pins

| Pin Name | Function | Description |
|---|---|---|
| `PVDD1`, `PVDD2` | Power Supply | Main battery power supply inputs (6V to 60V DC) |
| `BST_A`, `BST_B`, `BST_C` | Bootstrap | Bootstrap capacitor connections for High-side N-FET driving |
| `GH_A`, `GL_A` | Gate Drive | Phase A High-side (`GH_A`) & Low-side (`GL_A`) MOSFET Gate outputs |
| `GH_B`, `GL_B` | Gate Drive | Phase B High-side (`GH_B`) & Low-side (`GL_B`) MOSFET Gate outputs |
| `GH_C`, `GL_C` | Gate Drive | Phase C High-side (`GH_C`) & Low-side (`GL_C`) MOSFET Gate outputs |
| `PWM_H_A`, `PWM_L_A` | Control Input | Phase A High/Low PWM inputs from MCU |
| `SO1`, `SO2` | Analog Output | Current Shunt Amplifier 1 & 2 analog outputs to MCU ADC pins |
| `SCLK`, `SDI`, `SDO`, `nSCS` | SPI Bus | SPI communication interface pins for status & register setup |
| `nOCTW`, `nFAULT` | Fault Interrupt | Open-drain fault and overtemperature warning interrupt outputs |
| `VSENSE` | Power | Buck converter feedback voltage sense pin |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Operating Supply Voltage | $V_{PVDD}$ | 6.0 | 24.0/48.0| 60.0 | V | DC |
| Gate Drive Source Current| $I_{SOURCE}$| 1.0 | 1.7 | — | A | $V_{BST} - V_{SH} = 10\text{V}$ |
| Gate Drive Sink Current | $I_{SINK}$ | 1.3 | 2.3 | — | A | $V_{SH} = 10\text{V}$ |
| Current Sense Gain Options| $G_{CSA}$ | 10 | 20 | 80 | V/V | Programmable via SPI (10, 20, 40, 80 V/V) |
| Buck Output Voltage | $V_{BUCK}$ | 3.3 | 3.3 | 5.0 | V | Adjustable via resistor divider |
| Buck Output Current | $I_{BUCK}$ | — | 1.5 | — | A | Step-down converter |

## Common mistakes

- **Inadequate PCB PowerPAD Thermal Soldering:** The thermal pad beneath the 56-pin HTSSOP package dissipates gate drive heat. Incomplete ground plane copper coverage or bad reflow leads to thermal shutdown.
- **Excessive parasitic inductance on current shunt leads:** High $di/dt$ switching noise can corrupt the current sense amplifier inputs (`SP1`/`SN1` and `SP2`/`SN2`). Route current sense traces as tightly matched differential pairs away from high-power switching nodes.

## Notes

- **DRV8301 vs DRV8302 vs DRV8323:** DRV8301 has SPI interface + 2 current sense amps; DRV8302 uses hardware pins instead of SPI; DRV8323 supports higher voltages ($100\text{V}$) with smart gate drive architecture (IDRIVE).
