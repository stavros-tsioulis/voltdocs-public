## Overview

The **ACS712** is a fully integrated Hall-effect linear current sensor IC manufactured by Allegro MicroSystems. It measures both AC and DC current by sensing the magnetic field generated when current flows through an internal $1.2\text{ m}\Omega$ copper conduction path.

Because the current path is electrically isolated from the sensor electronics, the ACS712 provides **$2.1\text{ kV}_{\text{RMS}}$ galvanic isolation**, making it safe for measuring high-voltage AC loads (such as household appliances or motors) with low-voltage microcontrollers.

## Quick reference

| | |
|---|---|
| **Operating Voltage (`VCC`)** | 4.5 V to 5.5 V DC (5.0 V nominal) |
| **Output Offset Voltage** | $V_{CC} / 2$ ($2.50\text{ V}$ at 0 Amperes current) |
| **Galvanic Isolation Voltage** | $2.1\text{ kV}_{\text{RMS}}$ (50/60 Hz for 1 minute) |
| **Conductor Resistance** | $1.2\text{ m}\Omega$ (ultra-low power loss) |
| **Bandwidth** | 80 kHz |
| **Variant Current Ratings** | 5 A variant (`185 mV/A`), 20 A variant (`100 mV/A`), 30 A variant (`66 mV/A`) |
| **Output Type** | Ratiometric Analog Voltage (`OUT`) |

## Variant Sensitivity Comparison

| Variant Part Number | Max Current Range | Sensitivity ($S$) | Zero Current Output ($V_{OUT,0}$) |
|---|---|---|---|
| **ACS712-05B** | $\pm 5\text{ A}$ | **$185\text{ mV / A}$** | $2.50\text{ V}$ ($V_{CC} / 2$) |
| **ACS712-20A** | $\pm 20\text{ A}$ | **$100\text{ mV / A}$** | $2.50\text{ V}$ ($V_{CC} / 2$) |
| **ACS712-30A** | $\pm 30\text{ A}$ | **$66\text{ mV / A}$** | $2.50\text{ V}$ ($V_{CC} / 2$) |

## Pinout

### Standard Breakout Board Header & Screw Terminal

| Pin / Terminal | Name | Type | Description |
|---|---|---|---|
| Screw Terminal 1 | `IP+` | High-Current Input | Conductor input (in series with AC/DC load) |
| Screw Terminal 2 | `IP-` | High-Current Output | Conductor output (to load) |
| Header Pin 1 | `VCC` | Power | Supply voltage (+4.5 V to +5.5 V DC) |
| Header Pin 2 | `GND` | Power | Ground (0 V) |
| Header Pin 3 | `OUT` | Analog Output | Analog output voltage proportional to current |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 4.5 | 5.0 | 5.5 | V | DC |
| Supply Current | $I_{CC}$ | — | 10 | 13 | mA | $V_{CC} = 5.0\text{ V}$ |
| Sensitivity Error | $E_{SENS}$ | — | $\pm 1.5$ | — | % | $T_A = 25^\circ\text{C}$ |
| Total Output Error | $E_{TOT}$ | — | $\pm 1.5$ | $\pm 4.0$ | % | $I_{P} = I_{P,max}$ |
| Response Time | $t_{response}$ | — | 5 | — | µs | Output rise time to 90% |
| Frequency Bandwidth | $BW$ | — | 80 | — | kHz | $C_{FILTER} = 1\text{ nF}$ |

## Current Measurement Formulas

### DC Current Formula

$$I_{DC}\text{ (Amperes)} = \frac{V_{OUT}\text{ (in mV)} - 2500\text{ mV}}{\text{Sensitivity } S\text{ (in mV/A)}}$$

Example for **ACS712-05B** ($185\text{ mV/A}$) with a $2.87\text{ V}$ ADC output reading:

$$I_{DC} = \frac{2870\text{ mV} - 2500\text{ mV}}{185\text{ mV/A}} = \frac{370}{185} = +2.0\text{ A}$$

### AC RMS Current Formula

For 50/60 Hz AC current, sample $V_{OUT}$ over several full AC wave cycles ($\sim 100\text{ ms}$), find the peak-to-peak voltage ($V_{pp}$ in mV), and calculate RMS current:

$$I_{RMS} = \left(\frac{V_{pp}\text{ (in mV)}}{2 \sqrt{2}}\right) \div \text{Sensitivity } S\text{ (in mV/A)}$$

## Wiring

```
           [ ACS712 Screw Terminal ]
           │                       │
     AC/DC Power (+ Line)       AC/DC Load (+ Line)
```

| ACS712 Breakout Pin | → | Microcontroller (Arduino Uno / ESP32) |
|---|---|---|
| `VCC` | | `5V` |
| `GND` | | `GND` |
| `OUT` | | Analog Input Pin `A0` (or ADC with voltage divider for 3.3V MCUs) |

> [!WARNING]
> High Voltage Safety & 3.3V ADC Compatibility:
> - **Mains AC Safety:** Although the ACS712 IC provides $2.1\text{ kV}$ isolation, cheap breakout PCBs may have insufficient creepage/clearance distance between high-voltage screw terminals and logic header pins. Exercise extreme caution when measuring 110V/230V mains voltage!
> - **3.3V Microcontrollers (ESP32/Raspberry Pi):** The ACS712 outputs up to $4.5\text{ V}$ when measuring positive current. Use a $10\text{ k}\Omega / 20\text{ k}\Omega$ resistor voltage divider on `OUT` before connecting to 3.3V ADC inputs.

## Common mistakes

- **External Magnetic Interference:** Hall-effect sensors are sensitive to external magnetic fields. Keep motors, transformers, and heavy inductors away from the ACS712 package.
- **Powering from 3.3V:** Operating the ACS712 on 3.3V shifts the zero-current baseline away from $2.5\text{ V}$ and reduces sensitivity non-linearly. Always power with **5.0 V DC**.
- **Measuring small currents with 20A/30A variants:** Measuring $< 500\text{ mA}$ with an ACS712-30A produces tiny voltage changes ($33\text{ mV}$ for 0.5A) that get lost in ADC noise. Use the 5A variant or an **INA219** for low-current applications.

## Notes

- Solder jumper / capacitor on the `FILTER` pin allows adjusting the high-frequency cutoff to reduce output noise.
