## Overview

The **YL-69** (also sold as **FC-28**) is a 2-prong resistive soil moisture sensor widely used in DIY plant watering, smart garden, and automated irrigation projects.

It consists of two exposed copper PCB traces inserted into soil and an LM393 voltage comparator driver PCB (YL-38). Moisture in the soil acts as a conductor: wet soil lowers electrical resistance between the prongs (producing a lower analog voltage output), whereas dry soil increases electrical resistance (producing a higher analog voltage output near $V_{CC}$).

## Quick reference

| | |
|---|---|
| **Operating Voltage (`VCC`)** | 3.3 V to 5.0 V DC |
| **Sensing Principle** | Electrical resistance / conductivity through soil |
| **Outputs** | Analog voltage (`AO`: 1.2V wet to 5.0V dry) / Digital threshold (`DO` via LM393) |
| **Operating Current** | ~15 mA |
| **Probe Dimensions** | $60 \times 20\text{ mm}$ (fork length 48 mm) |

## Pinout

### Standard Driver PCB (YL-38 Driver Board Header)

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | Supply voltage (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground (0 V) |
| 3 | `DO` | Digital Output | Digital threshold output (`HIGH` in dry soil, `LOW` in wet soil) |
| 4 | `AO` | Analog Output | Analog voltage output (proportional to soil electrical resistance) |

### 2-Pin Probe Header (Connects Driver to YL-69 Fork Probe)

- Connect the 2 pins on the probe fork to the 2-pin header on the driver PCB (non-polarized).

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 3.3 | 5.0 | 5.5 | V | DC |
| Operating Current | $I_{CC}$ | — | 15 | 20 | mA | Active measurement |
| Dry Air Output Voltage | $V_{dry}$ | $V_{CC}-0.3$ | $V_{CC}$ | $V_{CC}$ | V | Probe in dry air |
| Water Immersion Output | $V_{wet}$ | 1.0 | 1.2 | 1.8 | V | Probe submerged in water |
| Probe Plating | $Plate$ | — | Nickel / HASL | — | — | Standard PCB coating |

## Calibration & Voltage Response

Because soil composition, salt density, and mineral levels vary significantly:
- **Dry Air Baseline (0% Moisture):** Analog output voltage reading $\approx 1023$ (on 10-bit 5V ADC) / $100\%$ dry.
- **Submerged in Water Baseline (100% Moisture):** Analog output voltage reading $\approx 250$ to $300$ / $100\%$ wet.

$$\text{Soil Moisture (\%)} = 100 \times \left(1 - \frac{\text{ADC Reading} - \text{ADC}_{\text{water}}}{\text{ADC}_{\text{air}} - \text{ADC}_{\text{water}}}\right)$$

## Wiring

| YL-69 Driver Board Pin | → | Microcontroller (Arduino / ESP32) | Notes |
|---|---|---|---|
| `VCC` | | GPIO Output Pin (or `5V`/`3.3V`) | **Power via GPIO pin to prevent corrosion!** |
| `GND` | | `GND` | Ground |
| `AO` | | Analog Pin `A0` (or ESP32 ADC) | Reads voltage proportional to moisture |
| `DO` | | Digital Pin (optional threshold trigger) | Threshold adjusted via potentiometer |

> [!WARNING]
> Electrolytic Corrosion Warning:
> Leaving constant DC voltage applied to the exposed copper prongs of the YL-69 probe causes **rapid galvanic electrolysis corrosion**. Copper plating dissolves into the soil, ruining the probe within days/weeks.
> **Corrosion Prevention:** Connect sensor `VCC` to a digital GPIO output pin on the microcontroller. Set GPIO `HIGH` for 50 ms only when taking a reading, then set GPIO `LOW` to turn off sensor power. For permanent outdoor soil monitoring, upgrade to a **Capacitive Soil Moisture Sensor**.

## Common mistakes

- **Leaving power ON 24/7:** Continuous DC current causes rapid probe corrosion.
- **Submerging driver PCB in soil/water:** Only insert the 2-prong fork into soil up to the white line; the electronic driver board is NOT waterproof.
- **Assuming linear percentage without calibration:** Raw ADC values vary based on soil compaction and salinity.

## Notes

- Obsolete for long-term deployments; replace with v1.2/v2.0 Capacitive Soil Moisture Sensors for corrosion resistance.
