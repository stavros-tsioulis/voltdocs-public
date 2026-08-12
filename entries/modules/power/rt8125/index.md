## Overview

The **RT8125** (RT8125A / RT8125B) is a single-phase synchronous step-down (buck) PWM controller IC manufactured by Richtek Technology. Enclosed in a tiny **WDFN-10L ($3 \times 3\text{ mm}$)** or **SOP-8** package, it drives external high-side and low-side N-channel power MOSFETs to convert $5\text{V}$ or $12\text{V}$ DC power rails down to low-voltage high-current outputs ($0.8\text{V} \dots 3.3\text{V}$).

Operating over a supply range of **4.5V to 13.2V DC**, the RT8125 features a fixed **300 kHz** switching frequency, precision **$0.8\text{V}$ internal reference voltage**, adaptive shoot-through protection, loss-less over-current protection ($R_{DS(ON)}$ sensing), and thermal shutdown.

## Quick reference

| | |
|---|---|
| **Input Supply Voltage (`VCC` / `PVCC`)** | 4.5 V to 13.2 V DC |
| **Output Voltage Range** | Adjustable down to $0.8\text{ V}$ DC |
| **Reference Voltage (`VFB`)** | $0.8\text{ V}$ ($\pm 1.5\%$ accuracy) |
| **Gate Drivers** | Integrated High-Side (`UGATE`) and Low-Side (`LGATE`) N-FET Gate Drivers |
| **Switching Frequency** | $300\text{ kHz}$ fixed frequency |
| **Protection** | Over-Voltage Protection (OVP), Under-Voltage Protection (UVP), Over-Current Protection (OCP via low-side $R_{DS(ON)}$) |
| **Package** | WDFN-10L ($3 \times 3\text{ mm}$) / SOP-8 |

## Pinout (WDFN-10L Package)

```
                       ┌─────────────┐
                [BOOT] 1│ 1        10│ [UGATE] (High-Side Gate Out)
                [VCC]  2│            │9  [PHASE] (Phase Node Input)
                 [FB]  3│   RT8125   │8  [PVCC] (Power Supply)
                 [COMP]4│   WDFN-10  │7  [LGATE] (Low-Side Gate Out)
                 [EN]  5│            │6  [GND]
                       └─────────────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `BOOT` | Power | High-Side Gate Driver Bootstrap Voltage Supply Input (Connect diode & cap to PHASE) |
| 2 | `VCC` | Power | Controller Supply Voltage Input (+4.5V to +13.2V DC) |
| 3 | `FB` | Input | Feedback Sense Input ($0.8\text{V}$ reference to GND) |
| 4 | `COMP` | Output | Error Amplifier Compensation Node |
| 5 | `EN` | Input | Chip Enable Pin (High = Enable; Low = Shutdown) |
| 6 | `GND` | Power | Ground Reference (0 V) |
| 7 | `LGATE` | Output | Synchronous Low-Side MOSFET Gate Drive Output |
| 8 | `PVCC` | Power | MOSFET Gate Driver Supply Voltage Input |
| 9 | `PHASE` | Power | High-Side Driver Return & Current Sense Phase Node |
| 10 | `UGATE` | Output | High-Side MOSFET Gate Drive Output |

## Output Voltage Formula

$$ V_{OUT} = 0.8\text{V} \times \left(1 + \frac{R_1}{R_2}\right) $$

Where $R_1$ is connected between $V_{OUT}$ and `FB`, and $R_2$ is connected between `FB` and `GND`.

## Common mistakes

- **Omitting the bootstrap diode & capacitor (`BOOT` to `PHASE`):** The high-side N-channel MOSFET requires a gate voltage higher than $V_{IN}$ to turn on. Connect a fast Schottky diode from `VCC` to `BOOT` and a $0.1\ \mu\text{F}$ ceramic capacitor between `BOOT` and `PHASE`.

## Notes

- **RT8125A vs RT8125B:** RT8125A includes internal soft-start and OCP latched shutdown; RT8125B features hiccup mode over-current protection.
