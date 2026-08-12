## Overview

The **PC817** (PC817X / LTV-817) is a universally deployed 4-pin photocoupler (optocoupler) IC manufactured by Sharp Microelectronics, Lite-On, and Everlight. It consists of an **GaAs infrared emitting diode** optically coupled to an **NPN silicon phototransistor** inside a compact 4-pin package.

Providing up to **$5000\text{ V}_{\text{RMS}}$ of galvanic isolation**, the PC817 breaks ground loops and isolates sensitive microcontroller digital logic pins from high-voltage AC/DC noise, noisy motor drivers, relays, and switch-mode power supply (SMPS) feedback circuits.

## Quick reference

| | |
|---|---|
| **Component Type** | 4-Pin Photocoupler / Optocoupler |
| **Isolation Voltage ($V_{ISO}$)**| $5000\text{ V}_{\text{RMS}}$ (1 minute) |
| **Collector-Emitter Voltage ($V_{CEO}$)**| $80\text{ V}$ max |
| **Input LED Forward Current ($I_F$)**| $50\text{ mA}$ max ($20\text{ mA}$ recommended) |
| **Collector Current ($I_C$)**| $50\text{ mA}$ max |
| **Current Transfer Ratio (CTR)**| 50% to 600% (Rank A: 80–160%, B: 130–260%, C: 200–400%, D: 300–600%) |
| **Response Time** | $4\ \mu\text{s}$ rise time / $3\ \mu\text{s}$ fall time |
| **Package** | 4-pin DIP / 4-pin SMD |

## Pinout (DIP-4 Package)

Looking at the top of the 4-pin package with dot indicator at Pin 1:

```
             ┌───┴───┐
     (A)  1 │ 1   4 │ 4  (C)
  ANODE     │ PC817 │    COLLECTOR
     (K)  2 │ 2   3 │ 3  (E)
  CATHODE   └───────┘    EMITTER
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `ANODE` (`A`) | Input | IR LED Anode (+) |
| 2 | `CATHODE` (`K`) | Input | IR LED Cathode (-) |
| 3 | `EMITTER` (`E`) | Output | Phototransistor Emitter (Output ground reference) |
| 4 | `COLLECTOR` (`C`) | Output | Phototransistor Collector (Output signal line) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| LED Forward Voltage | $V_F$ | 1.0 | 1.2 | 1.4 | V | $I_F = 20\text{mA}$ |
| LED Reverse Voltage | $V_R$ | — | — | 6.0 | V | $I_R = 10\ \mu\text{A}$ |
| Collector-Emitter Breakdown| $V_{(BR)CEO}$| 80 | — | — | V | $I_C = 0.1\text{mA}, I_F = 0$ |
| Collector Dark Current | $I_{CEO}$ | — | — | 100 | nA | $V_{CE} = 20\text{V}, I_F = 0$ |
| Collector Saturation Volts| $V_{CE(sat)}$| — | 0.1 | 0.2 | V | $I_F = 20\text{mA}, I_C = 1\text{mA}$ |

## Typical Applications

### Isolated Microcontroller Input Signal Buffer

Reading a $12\text{V}$ or $24\text{V}$ industrial sensor or push-button into a $3.3\text{V}$ / $5\text{V}$ MCU GPIO pin:

```
  +24V Sensor Line ───[ R1 = 2.2kΩ ]───► [Pin 1: ANODE]
                                             PC817
  Sensor Ground ──────────────────────► [Pin 2: CATHODE]

  +3.3V MCU Power Rail ───[ R2 = 10kΩ Pullup ]───┬─── [Pin 4: COLLECTOR]
                                                 │
                                                 ├─── MCU GPIO Pin (Active LOW)
                                                 │
  MCU Ground ────────────────────────────────────┴─── [Pin 3: EMITTER]
```

## Common mistakes

- **Forgetting input series current-limiting resistor:** Connecting a $5\text{V}$ or $12\text{V}$ control line directly across Pins 1 and 2 without a series resistor burns out the internal IR LED ($V_F \approx 1.2\text{V}$). Always size $R_{in} = (V_{in} - 1.2\text{V}) / 0.010\text{A}$.
- **Assuming 100% CTR across all operating temperatures:** The Current Transfer Ratio ($CTR = \frac{I_C}{I_F} \times 100\%$) degrades over time and at high temperatures. Design pull-up resistors assuming lower $CTR$ bounds.

## Notes

- **PC817 vs 6N137:** PC817 is a phototransistor optocoupler for DC and low-speed switching ($< 10\text{ kHz}$); 6N137 is a high-speed logic gate optocoupler ($10\text{ Mbps}$) for high-frequency SPI or fast UART isolation.
