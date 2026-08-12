## Overview

The **MAX1771** (MAX1771CSA / MAX1771CPA) is a high-efficiency current-mode step-up (boost) DC-DC controller IC manufactured by Analog Devices (Maxim Integrated). Designed to drive an external N-channel power MOSFET, it is legendary among electronics makers as the gold-standard controller for building **high-voltage ($170\text{V} \dots 200\text{V}$ DC) Nixie tube power supplies** from low-voltage $9\text{V} \dots 12\text{V}$ DC wall adapters.

Operating across an input supply voltage range of **2.0V to 16.5V DC**, the MAX1771 utilizes a BiCMOS pulse-frequency modulation (PFM) control scheme to achieve up to **90% efficiency** while drawing an ultra-low quiescent current of just **$110\ \mu\text{A}$**.

## Quick reference

| | |
|---|---|
| **Input Supply Voltage (`V+`)** | 2.0 V to 16.5 V DC |
| **Output Voltage Range** | Adjustable up to $200\text{ V}+$ DC (Determined by external MOSFET rating & feedback divider) |
| **Control Scheme** | Current-Limited PFM (Pulse-Frequency Modulation) |
| **Max Switching Frequency** | Up to $300\text{ kHz}$ |
| **Quiescent Current** | $110\ \mu\text{A}$ typical ($11\ \mu\text{A}$ in shutdown mode) |
| **Reference Voltage (`REF`)** | $1.5\text{ V}$ precision output reference pin |
| **Package** | 8-pin SOIC / 8-pin DIP |

## Pinout (DIP-8 / SOIC-8 Package)

```
             ┌───┴───┐
        EXT 1│ 1   8 │ CS (Current Sense Input)
         V+ 2│       │ 7 GND (Power Ground)
         FB 3│MAX1771│ 6 AGND (Analog Ground)
       SHDN 4│       │ 5 REF (1.5V Reference Out)
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `EXT` | Output | External N-Channel MOSFET Gate Drive Output |
| 2 | `V+` | Power | Positive Supply Voltage Input (+2.0V to +16.5V DC) |
| 3 | `FB` | Input | Feedback Voltage Sense Input ($1.5\text{V}$ reference to AGND) |
| 4 | `SHDN` | Input | Active-HIGH Shutdown Input (High = Shutdown; Low = Normal Operation) |
| 5 | `REF` | Output | Internal 1.5V Reference Output (Decouple with 0.1µF capacitor to AGND) |
| 6 | `AGND` | Power | Analog Signal Ground (Connect to GND near chip) |
| 7 | `GND` | Power | Heavy Current Power Ground |
| 8 | `CS` | Input | Current Sense Input (Connect to sense resistor $R_{SENSE}$ in series with N-FET source) |

## High-Voltage Nixie Tube Boost Supply Circuit (12V to 180V DC)

```
                       ┌───[ Fast High-Voltage Inductor 220µH ]───┬─── High-Voltage Output (+180V DC)
                       │                                          │
  +12V DC Supply ──────┴───────────┐                       [UF4007 Ultra-Fast Diode]
                                   │                              │
                           [Pin 2: V+]                            ├─── [Pin 1: EXT] ─── Gate N-FET (IRF640 / IRF840)
                               MAX1771                            │
                           [Pin 3: FB] ◄───[Feedback Divider]─────┤
                                                                  └─── [Pin 8: CS] ─── R_SENSE (0.05Ω) ─── GND
```

## High Voltage Safety Warning

> [!CAUTION]
> High Voltage Hazard!
> Nixie power supply circuits built with the MAX1771 generate **$180\text{V} \dots 200\text{V}$ DC**. Though non-lethal at low currents, contact causes painful electrical shocks and burns. Always discharge output capacitors before handling.

## Common mistakes

- **Using a standard slow rectifier diode (like 1N4007):** Standard 50Hz rectifiers cannot turn off fast enough at 300 kHz, causing thermal breakdown. Always use an **ultra-fast recovery diode** (such as the **UF4007** or **MUR160**).
- **Poor PCB ground layout:** High peak switching currents ($> 3\text{A}$) through the MOSFET source resistor will corrupt the analog feedback input (`FB`). Keep power ground (`GND`) separate from analog ground (`AGND`) until a single star point near Pin 6.

## Notes

- **MAX1771 vs MC34063:** MAX1771 drives external high-voltage MOSFETs at up to 90% efficiency; MC34063 uses internal switches restricted to lower efficiency and lower voltages ($40\text{V}$).
