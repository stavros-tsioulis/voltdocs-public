## Overview

The **SCT-013-030** is a non-invasive split-core AC current transformer (CT) clamp manufactured by YHDC. Designed for home energy monitoring, heat pump telemetry, and sub-metering, it clamps around a single insulated AC conductor wire to measure alternating currents from **$0\text{ to }30\text{ Amperes RMS}$** without cutting live high-voltage wiring.

Equipped with an internal **$62\ \Omega$ burden resistor**, the SCT-013-030 outputs a continuous **$0\text{ to }1.0\text{ V}$ AC RMS voltage** across a standard 3.5 mm TRS audio plug. It is natively supported by **OpenEnergyMonitor**, **ESPHome (`ct_clamp`)**, and Arduino ADC sampling circuits.

## Quick reference

| | |
|---|---|
| **Max AC current input ($I_{RMS}$)** | $0\text{ to }30\text{ A}$ AC RMS |
| **Max AC voltage output ($V_{RMS}$)**| $0\text{ to }1.0\text{ V}$ AC RMS (at rated 30A input) |
| **Internal burden resistor** | $62\ \Omega$ built-in burden resistor |
| **Operating frequency** | 50 Hz / 60 Hz (Mains power frequency) |
| **Opening aperture** | $13\text{ mm} \times 13\text{ mm}$ split-core window |
| **Non-linearity** | $\pm 1\%$ across $10\%\text{ to }120\%$ rated current |
| **Dielectric insulation** | $6.0\text{ kV}$ AC / 1 min (high-voltage safety isolation) |
| **Connector** | 3.5 mm TRS stereo audio jack (Tip & Sleeve connected to coil) |

## Connector Wiring & 3.5mm Jack Pinout

```
             ┌────────────────────────────────┐
             │ Tip: AC Voltage Signal (+)     │
             │ Ring: No Connection            │
             │ Sleeve: AC Voltage Signal (-) │
             └────────────────────────────────┘
```

- **Tip:** Secondary coil AC output (+)
- **Sleeve:** Secondary coil AC output (-)
- **Ring:** Unconnected

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Rated Input Current | $I_{rated}$ | 0 | — | 30 | A | AC RMS ($50/60\text{ Hz}$) |
| Output Voltage at 30A | $V_{out}$ | — | 1.0 | — | V | AC RMS voltage |
| Turn Ratio | $Ratio$ | — | 1800:1 | — | — | Internal secondary winding turns |
| Burden Resistor | $R_B$ | — | 62 | — | Ω | Internal voltage conversion resistor |
| Non-Linearity Error | $E_{NL}$ | -1.0% | $\pm 0.5\%$| +1.0%| — | Within 3A to 36A range |
| Max Aperture Wire Diameter| $Dia_{wire}$| — | 13.0 | — | mm | Insulated wire diameter |

## Interfacing with Microcontroller ADCs (DC Bias Circuit)

Microcontroller ADCs (such as Arduino or ESP32) measure only positive DC voltages ($0\text{V}$ to $3.3\text{V}$ or $5\text{V}$). Because the SCT-013-030 outputs a bi-directional sine wave ($\pm 1.414\text{V}$ peak-to-peak at 30A RMS), a **DC bias offset circuit** ($V_{CC} / 2$) must be added:

```
        3.3V Power Rail
           │
        [10kΩ]
           │
           ├─── Voltage Divider Center Point (1.65V DC Offset)
           │     │
        [10kΩ]  [10µF Cap] ─── GND
           │     │
          GND    ├─── SCT-013 Sleeve (Audio Jack (-) Lead)
                 │
                 ├─── SCT-013 Tip (Audio Jack (+) Lead) ─── Microcontroller ADC Pin
```

### RMS Current Calculation Math

$$ I_{RMS} = \text{Calibration Factor} \times \sqrt{ \frac{1}{N} \sum_{i=1}^{N} (V_{sample}[i] - V_{offset})^2 } $$

For the SCT-013-030 (1V output at 30A input), the ideal calibration multiplier is **30.0**:

$$ I_{RMS}\text{ (A)} = 30.0 \times V_{RMS\_AC} $$

## Wiring

| SCT-013-030 3.5mm Plug | → | Bias Circuit & MCU | Notes |
|---|---|---|---|
| Tip | | MCU Analog Pin (A0 / ESP32 ADC) | Reads AC sine wave centered at 1.65V |
| Sleeve | | 1.65V DC Bias Node ($V_{CC}/2$) | Virtual AC ground reference |

> [!WARNING]
> High Voltage & Clamping Rules:
> - Clamp the SCT-013 **around a single conductor wire** (either Live/Phase OR Neutral). Clamping around a two-conductor power cord (carrying both Live and Neutral together) causes magnetic fields to cancel out, resulting in zero current output.
> - Ensure the ferrite split-core latch snaps completely shut. Air gaps between ferrite pole faces decrease inductance and cause massive calibration errors.

## Example (ESPHome Configuration)

```yaml
sensor:
  - platform: ct_clamp
    sensor: adc_sensor
    name: "Main Circuit Current"
    update_interval: 2s
    filters:
      - calibrate_linear:
          - 0.0 -> 0.0
          - 1.0 -> 30.0

  - platform: esp32_adc
    id: adc_sensor
    pin: GPIO34
    attenuation: 11db
```

## Common mistakes

- **Clamping both Live and Neutral together:** Clamping over an intact power cord yields $0\text{A}$ because $I_{Live} + I_{Neutral} = 0$. Strip outer jacket and clamp over the Live wire alone.
- **Conflating SCT-013-030 and SCT-013-000:** The SCT-013-030 has an **internal $62\ \Omega$ burden resistor** outputting $0\text{--}1\text{V}$ voltage; the SCT-013-000 has **NO internal burden resistor** and outputs $0\text{--}50\text{mA}$ current (requires an external burden resistor).

## Notes

- **SCT-013 Current Rating Family:** SCT-013-000 (50mA current output), SCT-013-005 (5A), SCT-013-015 (15A), SCT-013-030 (30A), SCT-013-050 (50A), SCT-013-100 (100A).
